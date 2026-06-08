# vostok-versions

Cross-version analysis of **Survarium** (Vostok Engine / X-Ray 2.0) builds: unpack
several game versions, delink each into per-function COFF objects, and diff one
version against another so we can see exactly how the engine binary evolved.

The **oldest** build is the canonical **base** — every diff is computed
base → newer. Diffs show which functions are unchanged, which churned, and which
are new, so matching effort can be prioritized and forward-ported.

## Hard requirement: every build needs a PDB

This only works on builds that shipped **`survarium.exe` + `survarium.pdb`**
(internal/dev builds — the publicly distributed closed-alpha builds archived on
archive.org). The PDB gives
`vostok-delinker` the symbol names and function boundaries it splits the EXE on;
objdiff then matches functions by name across versions. A symbol-less retail
`survarium.exe` cannot be processed this way.

## Toolchain: the Nix devShell

The binaries — `vostok-delinker`, `pdb_parser`, `objdiff-cli`, `innoextract` —
are built by this repo's flake. `nix develop` puts them all on PATH:

    nix develop      # puts the tools on PATH

`vostok-delinker` and `vostok-pdb-parser` are built from their public source repos
(`github:srp-survarium/*`); `objdiff-cli` is the upstream prebuilt binary;
`innoextract`/`p7zip` come from nixpkgs. (Or point `VOSTOK_DELINKER` / `PDB_PARSER`
/ `OBJDIFF_CLI` / `INNOEXTRACT` at binaries yourself.)

## Where versions come from: `versions.json` + the flake

Versions are fetched from **archive.org**, not dropped in by hand.
`versions.json` is the single registry (label, url, sha256, base, engine_path),
read by *both* `flake.nix` (`builtins.fromJSON`) and the Python scripts (`json`).
Each entry becomes a flake package `version-<label>` = the installer fetched and
innoextracted to a dir with `survarium.{exe,pdb}`.

To add a new build: append its archive.org `url` + `sha256` to `versions.json`
(get the hash with `nix-prefetch-url <url>`), then run `add_version.py <label>`.

## Workflow

Add a version — with no source path it's fetched from the registry via the flake:

    python3 scripts/add_version.py v0.100b-build802            # base (per versions.json)
    python3 scripts/add_version.py v0.200 --align-to v0.100b-build802

You can still pass an explicit installer `.exe` or an extracted dir as a second
arg to bypass the registry. `--align-to <base>` reuses the base's folded-symbol
names so version-to-version diffs stay stable.

Diff two versions (oldest = base):

    python3 scripts/diff_versions.py v0.100b-build802 v0.200
    python3 scripts/diff_versions.py v0.200            # base taken from config.json

Read `diffs/v0.100b-build802__v0.200/summary.md`.

### Identity sanity test

Diffing a version against itself must report 100% on every function — a good
end-to-end check of the delink + objdiff wiring before trusting real diffs:

    python3 scripts/add_version.py v0.100b-build802
    python3 scripts/diff_versions.py v0.100b-build802 v0.100b-build802

## Layout

    scripts/
      common.py          shared helpers + tool resolution + vendored objdiff config bits
      add_version.py      installer/dir -> delink -> objects + structure + meta.json
      diff_versions.py    base,target -> objdiff project -> report.json + summary.{md,json}
    versions/<label>/
      objects/            per-function COFF .obj (the delinked build; committed)
      structure/          pdb_parser readable stubs
      symbol-map.tsv      folded-symbol naming for stable diffs
      meta.json           build id, exe/pdb sha256 + sizes, object count
    diffs/<base>__<target>/
      objdiff.json  report.json  summary.md  summary.json
    cache/                extracted exe/pdb (gitignored - large)
    config.json           { "base": <label>, "versions": [...] }

## The base: v0.100b build 802 (May 2013)

The oldest known PDB-bearing Survarium build (from archive.org) is version #1 /
base, and the first entry in `versions.json`. Bootstrap it straight from the flake:

    python3 scripts/add_version.py v0.100b-build802

(fetches the archive.org installer, extracts, delinks). You can also pass an
explicit installer `.exe` or extracted dir as a second arg to bypass the registry.
