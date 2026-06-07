#!/usr/bin/env python3
"""
diff_versions.py - diff one Survarium version against another, function by function.

    python3 scripts/diff_versions.py <target>            # base = config.json base
    python3 scripts/diff_versions.py <base> <target>     # explicit pair

Builds an objdiff project under diffs/<base>__<target>/ that pairs each unit's
COFF object from the two versions, runs objdiff-cli, and writes:

  report.json   - raw objdiff report (per-unit, per-function fuzzy %)
  summary.md    - human summary: identical / changed / new / removed, top churn
  summary.json  - machine-readable counts + lists

objdiff is target-centric (base is the thing we build toward). Here the *base*
version is the older one we match from, the *target* is the newer one whose
changes we want to see. So a function at:
  100%  -> unchanged between the two builds
  1-99% -> changed (the interesting churn)
  0%    -> present in target, absent/totally-rewritten in base (effectively new)
Units present in base but gone in target are reported separately as "removed".

Passing the same label as base and target is allowed: it's an identity check
that should report 100% on every function and validates the objdiff wiring.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as c  # noqa: E402


def units_of(label: str) -> dict[str, Path]:
    """Map unit-name -> .obj path for a version's delinked objects."""
    root = c.VERSIONS_DIR / label / "objects"
    if not root.is_dir():
        sys.exit(f"error: {root} missing - add version {label!r} first")
    out = {}
    for obj in root.rglob("*.obj"):
        unit = obj.relative_to(root).as_posix().removesuffix(".obj")
        out[unit] = obj
    return out


def write_objdiff_project(diff_dir: Path, base: str, target: str) -> None:
    base_units = units_of(base)
    target_units = units_of(target)
    diff_dir.mkdir(parents=True, exist_ok=True)
    c.write_dummy_obj(diff_dir / "dummy.obj")

    units = []
    for unit in sorted(target_units):
        # Paths are relative to diff_dir (where objdiff.json lives).
        target_rel = _rel(target_units[unit], diff_dir)
        base_rel = _rel(base_units[unit], diff_dir) if unit in base_units else "./dummy.obj"
        units.append({
            "name": unit,
            "target_path": target_rel,
            "base_path": base_rel,
            "scratch": {"platform": "win32", "compiler": "msvc8.0"},
        })

    project = {"build_base": False, "build_target": False, "units": units}
    (diff_dir / "objdiff.json").write_text(json.dumps(project, indent=2) + "\n")


def _rel(path: Path, start: Path) -> str:
    return "./" + os.path.relpath(path, start)


def summarize(diff_dir: Path, base: str, target: str) -> dict:
    report = json.loads((diff_dir / "report.json").read_text())
    identical, changed, new = [], [], []
    for unit in report.get("units", []):
        for fn in unit.get("functions", []):
            pct = fn.get("fuzzy_match_percent", 0.0)
            name = fn.get("metadata", {}).get("demangled_name") or fn.get("name", "?")
            entry = (pct, unit.get("name"), name)
            if pct >= 100.0:
                identical.append(entry)
            elif pct > 0.0:
                changed.append(entry)
            else:
                new.append(entry)

    base_units = set(units_of(base))
    target_units = set(units_of(target))
    removed_units = sorted(base_units - target_units)

    changed.sort()  # lowest match (most changed) first
    summary = {
        "base": base, "target": target,
        "counts": {
            "identical": len(identical),
            "changed": len(changed),
            "new_or_rewritten": len(new),
            "removed_units": len(removed_units),
        },
        "top_changed": [{"pct": p, "unit": u, "fn": n} for p, u, n in changed[:50]],
        "new_or_rewritten": [{"unit": u, "fn": n} for _, u, n in sorted(new)[:200]],
        "removed_units": removed_units,
    }
    (diff_dir / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    _write_summary_md(diff_dir, summary)
    return summary


def _write_summary_md(diff_dir: Path, s: dict) -> None:
    cn = s["counts"]
    lines = [
        f"# {s['base']} -> {s['target']}",
        "",
        f"- identical: **{cn['identical']}**",
        f"- changed: **{cn['changed']}**",
        f"- new / rewritten (0% vs base): **{cn['new_or_rewritten']}**",
        f"- units removed in target: **{cn['removed_units']}**",
        "",
        "## Most-changed functions (lowest match first)",
        "",
        "| match % | unit | function |",
        "| ---: | --- | --- |",
    ]
    for e in s["top_changed"]:
        lines.append(f"| {e['pct']:.2f} | {e['unit']} | `{e['fn']}` |")
    if s["removed_units"]:
        lines += ["", "## Units present in base but gone in target", ""]
        lines += [f"- {u}" for u in s["removed_units"]]
    (diff_dir / "summary.md").write_text("\n".join(lines) + "\n")


def main() -> None:
    ap = argparse.ArgumentParser(description="Diff two delinked Survarium versions.")
    ap.add_argument("a", help="base label, or target label if it's the only arg")
    ap.add_argument("b", nargs="?", help="target label (if omitted, base = config.json base)")
    args = ap.parse_args()

    if args.b is None:
        base = c.load_config().get("base")
        if not base:
            sys.exit("error: no base in config.json; pass both <base> <target>")
        target = args.a
    else:
        base, target = args.a, args.b

    if base == target:
        c.log("diff", f"identity check: {base} vs itself - expect 100% on every function")

    c.require_tool(c.objdiff_cli())
    diff_dir = c.DIFFS_DIR / f"{base}__{target}"
    c.log("diff", f"{base} -> {target}")
    write_objdiff_project(diff_dir, base, target)

    report = diff_dir / "report.json"
    subprocess.run(
        [c.objdiff_cli(), "report", "generate", "-p", str(diff_dir), "-o", str(report)],
        check=True,
    )
    s = summarize(diff_dir, base, target)
    cn = s["counts"]
    c.log("diff", "identical {} | changed {} | new/rewritten {} | removed units {}".format(
        cn["identical"], cn["changed"], cn["new_or_rewritten"], cn["removed_units"]))
    c.log("diff", f"summary: {diff_dir / 'summary.md'}")


if __name__ == "__main__":
    main()
