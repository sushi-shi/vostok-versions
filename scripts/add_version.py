#!/usr/bin/env python3
"""
add_version.py - ingest one Survarium build into the version database.

    python3 scripts/add_version.py <label> <source> [options]

<source> is either an InnoSetup installer (.exe) or a directory that already
contains survarium.exe + survarium.pdb. Steps:

  1. resolve source -> a dir holding survarium.{exe,pdb}
     (installer: innoextract into cache/<label>/; directory: used as-is)
  2. vostok-delinker  -> versions/<label>/objects/   (per-function COFF .obj)
  3. pdb_parser       -> versions/<label>/structure/  (readable stubs; --no-structure to skip)
  4. write versions/<label>/meta.json (build hashes, sizes, object count, ...)

The first version added (or one passed with --base) is recorded as the matching
base in config.json; later versions diff against it.

Folded-symbol naming: each version writes its own symbol map. For stable diffs
*against the base*, pass `--align-to <base-label>` so this build reuses the
base's folded-group names instead of choosing its own.

If <source> is omitted, the label is looked up in versions.json and the build is
fetched + extracted from archive.org via the flake (`nix build .#version-<label>`).

Run inside vostok-review's `nix develop` (provides the tools).
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as c  # noqa: E402


def resolve_source(label: str, source: Path, keep_cache: bool) -> tuple[Path, Path]:
    if source.is_dir():
        c.log("add", f"source is a directory: {source}")
        return c.find_exe_pdb(source)

    if not source.is_file():
        sys.exit(f"error: source {source} is neither a file nor a directory")

    # Installer: extract once into cache/<label>/ (gitignored).
    c.require_tool(c.innoextract())
    dest = c.CACHE_DIR / label
    if dest.exists() and not keep_cache:
        shutil.rmtree(dest)
    dest.mkdir(parents=True, exist_ok=True)
    c.log("add", f"innoextract {source.name} -> {dest}")
    subprocess.run([c.innoextract(), "-d", str(dest), str(source)], check=True)
    return c.find_exe_pdb(dest)


def delink(label: str, exe: Path, pdb: Path, engine_path: str, align_to: str | None) -> Path:
    c.require_tool(c.delinker())
    out = c.VERSIONS_DIR / label / "objects"
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True, exist_ok=True)

    own_map = c.VERSIONS_DIR / label / "symbol-map.tsv"
    # Align this build's folded-group names to the base's, when asked and possible;
    # otherwise let the delinker choose and record them in our own map.
    symbol_flags: list[str] = []
    if align_to:
        base_map = c.VERSIONS_DIR / align_to / "symbol-map.tsv"
        if base_map.exists() and c.delinker_supports("--read-symbol-map"):
            symbol_flags = ["--read-symbol-map", str(base_map)]
            c.log("add", f"aligning folded symbols to base {align_to!r}")
        else:
            c.log("add", f"--align-to {align_to!r}: base map or flag missing; writing own map")
    if not symbol_flags and c.delinker_supports("--write-symbol-map"):
        symbol_flags = ["--write-symbol-map", str(own_map)]

    c.log("add", f"delinking {exe.name} -> {out}")
    subprocess.run(
        [c.delinker(),
         "--pdb-path", str(pdb),
         "--exe-path", str(exe),
         "--output-path", str(out),
         "--engine-path", engine_path,
         *symbol_flags],
        check=True,
    )
    return out


def make_structure(label: str, pdb: Path, engine_path: str) -> None:
    if shutil.which(c.pdb_parser()) is None:
        c.log("add", "pdb_parser absent; skipping structure stubs")
        return
    out = c.VERSIONS_DIR / label / "structure"
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True, exist_ok=True)
    c.log("add", f"pdb_parser -> {out}")
    # Structure stubs are readability-only; the delinked objects (what we diff)
    # are already done. pdb_parser panics on some PDBs (e.g. "Enums cannot be of
    # different length"), so never let it sink the whole ingest.
    try:
        subprocess.run(
            [c.pdb_parser(),
             "--output-path", str(out),
             "--pdb-path", str(pdb),
             "--engine-path", engine_path],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        c.log("add", f"pdb_parser failed (exit {e.returncode}); skipping structure stubs")
        shutil.rmtree(out, ignore_errors=True)


def main() -> None:
    ap = argparse.ArgumentParser(description="Ingest one Survarium build into the version DB.")
    ap.add_argument("label", help="short version label, e.g. v0.100b-build802")
    ap.add_argument("source", type=Path, nargs="?",
                    help="installer .exe OR a dir with survarium.{exe,pdb}; "
                         "omit to fetch from versions.json via the flake")
    ap.add_argument("--engine-path", default=None,
                    help=f"PDB source-path prefix to strip (default: registry value or {c.ENGINE_PATH_DEFAULT})")
    ap.add_argument("--align-to", metavar="LABEL",
                    help="reuse this base version's folded-symbol map for stable diffs")
    ap.add_argument("--base", action="store_true", help="record this version as the matching base")
    ap.add_argument("--no-structure", action="store_true", help="skip pdb_parser structure stubs")
    ap.add_argument("--keep-cache", action="store_true", help="reuse an existing cache/<label> extract")
    ap.add_argument("--force", action="store_true", help="re-ingest even if meta.json already exists")
    args = ap.parse_args()

    entry = c.registry_entry(args.label) or {}
    engine_path = args.engine_path or entry.get("engine_path") or c.ENGINE_PATH_DEFAULT
    is_base = args.base or entry.get("base", False)

    meta_path = c.VERSIONS_DIR / args.label / "meta.json"
    if meta_path.exists() and not args.force:
        c.log("add", f"{args.label} already ingested (meta.json present); --force to redo")
        cfg = c.load_config()
        if is_base:
            cfg["base"] = args.label
            c.save_config(cfg)
        return

    if args.source is not None:
        exe, pdb = resolve_source(args.label, args.source, args.keep_cache)
    elif entry:
        c.log("add", f"fetching {args.label!r} from archive.org via flake")
        src_dir = c.fetch_from_flake(args.label)
        exe, pdb = c.find_exe_pdb(src_dir)
    else:
        sys.exit(f"error: no source given and {args.label!r} not in versions.json")

    objects = delink(args.label, exe, pdb, engine_path, args.align_to)
    n_objects = sum(1 for _ in objects.rglob("*.obj"))
    if not args.no_structure:
        make_structure(args.label, pdb, engine_path)

    meta = {
        "label": args.label,
        "source": args.source.name if args.source else (entry.get("url") or "flake"),
        "engine_path": engine_path,
        "aligned_to": args.align_to,
        "exe": {"name": exe.name, "size": exe.stat().st_size, "sha256": c.sha256_file(exe)},
        "pdb": {"name": pdb.name, "size": pdb.stat().st_size, "sha256": c.sha256_file(pdb)},
        "n_objects": n_objects,
        "added": c.now_iso(),
    }
    meta_path.write_text(json.dumps(meta, indent=2) + "\n")

    cfg = c.load_config()
    cfg.setdefault("versions", [])
    if args.label not in cfg["versions"]:
        cfg["versions"].append(args.label)
    if is_base or "base" not in cfg:
        cfg["base"] = args.label
        c.log("add", f"base version = {args.label!r}")
    c.save_config(cfg)

    c.log("add", f"done: {args.label}  ({n_objects} objects)  base={cfg['base']}")


if __name__ == "__main__":
    main()
