#!/usr/bin/env python3
"""
chain_report.py - one report covering consecutive diffs across all ingested
versions (oldest -> newest), engine (vostok/*) functions only.

    python3 scripts/chain_report.py

For each adjacent pair A -> B it reports, by demangled function name:
  - added    : names in B not in A
  - deleted  : names in A not in B
  - changed  : names in both whose match < 100% (magnitude = lowest match)

objdiff is target-centric (it lists the target's functions), so deletions come
from the reverse diff B -> A. Both directions are generated on demand and reused.
Output: reports/CHAIN_REPORT.md (+ .json).

Run inside this repo's `nix develop` (needs objdiff-cli).
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common as c  # noqa: E402

REPORTS_DIR = c.REPO_DIR / "reports"
LIST_CAP = 400  # cap per-list output; note the remainder


def ingested_ordered() -> list[dict]:
    """Registry entries that are actually delinked, oldest build first."""
    out = []
    for v in c.registry():
        label = v["label"]
        if (c.VERSIONS_DIR / label / "objects").is_dir() and (c.VERSIONS_DIR / label / "meta.json").exists():
            out.append(v)
    return sorted(out, key=lambda v: v.get("build", 0))


def ensure_report(base: str, target: str) -> Path:
    diff_dir = c.DIFFS_DIR / f"{base}__{target}"
    if not (diff_dir / "report.json").exists():
        subprocess.run(
            [sys.executable, str(c.SCRIPTS_DIR / "diff_versions.py"), base, target],
            check=True,
        )
    return diff_dir / "report.json"


def reportable_funcs(report_path: Path, include_generated: bool) -> dict[str, float]:
    """Demangled name -> lowest match% across units, hand-written engine only
    (compiler-generated included when asked)."""
    rep = json.loads(report_path.read_text())
    out: dict[str, float] = {}
    for unit in rep.get("units", []):
        uname = unit.get("name", "")
        for fn in unit.get("functions", []):
            name = fn.get("metadata", {}).get("demangled_name") or fn.get("name", "?")
            cls = c.classify(uname, name)
            if cls == "engine" or (cls == "generated" and include_generated):
                pct = fn.get("fuzzy_match_percent", 0.0)
                out[name] = min(pct, out.get(name, 100.0))
    return out


def diff_pair(a: str, b: str, include_generated: bool) -> dict:
    fb = reportable_funcs(ensure_report(a, b), include_generated)   # target = b, % vs a
    fa = reportable_funcs(ensure_report(b, a), include_generated)   # target = a, % vs b
    names_a, names_b = set(fa), set(fb)
    both = names_a & names_b
    changed = sorted(((fb[n], n) for n in both if fb[n] < 100.0))
    return {
        "added": sorted(names_b - names_a),
        "deleted": sorted(names_a - names_b),
        "changed": [{"pct": p, "fn": n} for p, n in changed],
        "identical": len(both) - len(changed),
    }


def _capped(items: list, render) -> list[str]:
    lines = [render(x) for x in items[:LIST_CAP]]
    if len(items) > LIST_CAP:
        lines.append(f"- _...and {len(items) - LIST_CAP} more_")
    return lines


def main() -> None:
    ap = argparse.ArgumentParser(description="Chain report across consecutive ingested versions.")
    ap.add_argument("--with-generated", action="store_true",
                    help="include compiler-generated functions (thunks, deleting dtors, ...)")
    args = ap.parse_args()

    versions = ingested_ordered()
    if len(versions) < 2:
        sys.exit("chain_report: need >= 2 ingested versions")
    REPORTS_DIR.mkdir(exist_ok=True)

    steps = []
    for a, b in zip(versions, versions[1:]):
        d = diff_pair(a["label"], b["label"], args.with_generated)
        d["a"], d["b"] = a, b
        steps.append(d)

    # --- machine-readable ---
    (REPORTS_DIR / "CHAIN_REPORT.json").write_text(json.dumps(
        {"versions": [v["label"] for v in versions], "steps": [
            {"from": s["a"]["label"], "to": s["b"]["label"],
             "added": s["added"], "deleted": s["deleted"], "changed": s["changed"],
             "identical": s["identical"]} for s in steps]}, indent=2) + "\n")

    # --- markdown ---
    scope = ("hand-written engine + compiler-generated" if args.with_generated
             else "hand-written engine (compiler-generated excluded)")
    md = ["# Survarium cross-version chain report",
          "",
          f"{scope} functions under `vostok/*`, deduped by demangled name. "
          "`changed` magnitude is the lowest match % across units.",
          "",
          "## Overview",
          "",
          "| step | from | to | +added | -deleted | ~changed | =identical |",
          "| --- | --- | --- | ---: | ---: | ---: | ---: |"]
    for i, s in enumerate(steps, 1):
        md.append("| {} | {} | {} | {} | {} | {} | {} |".format(
            i, s["a"]["label"], s["b"]["label"],
            len(s["added"]), len(s["deleted"]), len(s["changed"]), s["identical"]))

    for s in steps:
        a, b = s["a"], s["b"]
        md += ["", "---", "",
               f"## {a['label']} → {b['label']}",
               f"_{a.get('date', '?')} → {b.get('date', '?')} · "
               f"+{len(s['added'])} / -{len(s['deleted'])} / ~{len(s['changed'])}_",
               ""]
        md += [f"### Changed ({len(s['changed'])})", "",
               "| match % | function |", "| ---: | --- |"]
        md += _capped(s["changed"], lambda e: f"| {e['pct']:.2f} | `{e['fn']}` |")
        md += ["", f"### Added ({len(s['added'])})", ""]
        md += _capped(s["added"], lambda n: f"- `{n}`") or ["_none_"]
        md += ["", f"### Deleted ({len(s['deleted'])})", ""]
        md += _capped(s["deleted"], lambda n: f"- `{n}`") or ["_none_"]

    (REPORTS_DIR / "CHAIN_REPORT.md").write_text("\n".join(md) + "\n")
    c.log("chain", f"{len(steps)} steps -> {REPORTS_DIR / 'CHAIN_REPORT.md'}")


if __name__ == "__main__":
    main()
