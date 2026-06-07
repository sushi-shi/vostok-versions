#!/usr/bin/env python3
"""
common.py - shared helpers for the Survarium cross-version diff project.

Every version is an *internal* Survarium build that shipped with both
survarium.exe and survarium.pdb. The PDB is what makes a build tractable:
vostok-delinker uses it to split the EXE into per-function COFF .obj files, and
objdiff then diffs one version's objects against another's. No PDB -> no symbols,
no clean per-function objects, and this whole approach does not apply.

The toolchain (vostok-delinker, pdb_parser, objdiff-cli, innoextract) is provided
by the sibling vostok-review Nix devShell. Run these scripts inside its
`nix develop`, or point the *_BIN env vars at the binaries.
"""

from __future__ import annotations

import datetime
import hashlib
import json
import os
import shutil
import struct
import subprocess
import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
REPO_DIR = SCRIPTS_DIR.parent
VERSIONS_DIR = REPO_DIR / "versions"
DIFFS_DIR = REPO_DIR / "diffs"
CACHE_DIR = REPO_DIR / "cache"        # extracted installers (exe/pdb) - gitignored
CONFIG_PATH = REPO_DIR / "config.json"

# Real shipped Survarium PDBs record source paths under this prefix; the delinker
# and pdb-parser strip it to recover engine-relative unit names. Override per
# version with --engine-path if a build used a different root.
ENGINE_PATH_DEFAULT = "c:/survarium/sources"


def log(tag: str, msg: str) -> None:
    print(f"[{tag}] {msg}", flush=True)


# --- tool resolution -------------------------------------------------------

def _tool(env_var: str, default: str) -> str:
    return os.environ.get(env_var, default)


def delinker() -> str:
    return _tool("VOSTOK_DELINKER", "vostok-delinker")


def pdb_parser() -> str:
    return _tool("PDB_PARSER", "pdb_parser")


def objdiff_cli() -> str:
    return _tool("OBJDIFF_CLI", "objdiff-cli")


def innoextract() -> str:
    return _tool("INNOEXTRACT", "innoextract")


def require_tool(binary: str) -> str:
    """Return `binary` if on PATH, else exit with a devShell hint."""
    if shutil.which(binary) is None:
        sys.exit(
            f"error: {binary!r} not found on PATH.\n"
            "  Run inside vostok-review's `nix develop` (it provides "
            "vostok-delinker, pdb_parser, objdiff-cli, innoextract),\n"
            "  or set the matching *_BIN / VOSTOK_DELINKER env var."
        )
    return binary


def delinker_supports(flag: str) -> bool:
    """Whether the delinker advertises `flag` in --help (newer flags may be absent)."""
    try:
        out = subprocess.run(
            [delinker(), "--help"], capture_output=True, text=True, check=False
        )
        return flag in (out.stdout + out.stderr)
    except OSError:
        return False


# --- assets ----------------------------------------------------------------

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def find_exe_pdb(root: Path) -> tuple[Path, Path]:
    """Locate the game survarium.exe + survarium.pdb under `root`.

    Picks the largest non-uninstaller survarium.exe (mirrors vostok-review's
    flake heuristic), then the .pdb sitting beside it.
    """
    exes = sorted(
        (p for p in root.rglob("*.exe")
         if p.name.lower() == "survarium.exe" and "uninstall" not in str(p).lower()),
        key=lambda p: p.stat().st_size, reverse=True,
    )
    if not exes:
        sys.exit(f"error: no survarium.exe found under {root}")
    exe = exes[0]
    pdb = exe.with_suffix(".pdb")
    if not pdb.exists():
        cand = list(exe.parent.glob("*.pdb"))
        if not cand:
            sys.exit(f"error: no .pdb beside {exe} (a symbol-less build is not usable here)")
        pdb = cand[0]
    return exe, pdb


# --- repo config (which label is the base) ---------------------------------

def load_config() -> dict:
    if CONFIG_PATH.exists():
        return json.loads(CONFIG_PATH.read_text())
    return {}


def save_config(cfg: dict) -> None:
    CONFIG_PATH.write_text(json.dumps(cfg, indent=2) + "\n")


def now_iso() -> str:
    return datetime.datetime.now().replace(microsecond=0).isoformat()


# --- engine vs third-party classification ----------------------------------
# First-party engine/game code lives under sources/vostok/, so its delinked
# units are "vostok/...". Everything else (boost, bullet, stlport, scaleform,
# vorbis, opcode, speedtree, zlib, ogg, wildmagic, _msvc_internal, ...) is
# third-party and is the main source of cross-version diff noise.

def is_engine_unit(unit: str) -> bool:
    return unit.startswith("vostok/")


# --- version registry (versions.json) + flake fetch ------------------------
# versions.json is the single source of truth, read by BOTH this script (json)
# and flake.nix (builtins.fromJSON). Each entry: label, url, sha256, and
# optionally base (bool) + engine_path. The flake turns each into a
# `version-<label>` package: the archive.org installer, innoextracted to a dir
# holding survarium.{exe,pdb}.

REGISTRY_PATH = REPO_DIR / "versions.json"


def registry() -> list[dict]:
    if REGISTRY_PATH.exists():
        return json.loads(REGISTRY_PATH.read_text())
    return []


def registry_entry(label: str) -> dict | None:
    return next((v for v in registry() if v.get("label") == label), None)


def flake_attr(label: str) -> str:
    """Package attribute for a label: dots -> underscores so the `nix build .#attr`
    CLI path isn't split on '.' (the flake applies the same transform)."""
    return "version-" + label.replace(".", "_")


def fetch_from_flake(label: str) -> Path:
    """`nix build .#version-<label>` and return the extracted-build out path.
    stderr streams through so flake build errors are visible, not swallowed."""
    require_tool("nix")
    out = subprocess.run(
        ["nix", "build", f".#{flake_attr(label)}", "--no-link", "--print-out-paths"],
        cwd=REPO_DIR, stdout=subprocess.PIPE, text=True, check=True,
    )
    return Path(out.stdout.strip().splitlines()[-1])


# --- objdiff config emission (vendored from vostok-review) ------------------

def write_dummy_obj(path: Path) -> None:
    """A minimal valid empty COFF .obj, used as the base side for a unit that
    exists in the target version but not the base (i.e. an added unit)."""
    symbol_table_offset = 20 + 40
    header = struct.pack("<HHIIIHH", 0x14C, 1, 0, symbol_table_offset, 0, 0, 0)
    section = struct.pack("<8sIIIIIIHHI", b".text\0\0\0",
                          0, 0, 0, 0, 0, 0, 0, 0, 0x60000020)
    string_table = struct.pack("<I", 4)
    with path.open("wb") as f:
        f.write(header)
        f.write(section)
        f.write(string_table)
