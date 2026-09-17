#!/usr/bin/env python3
"""Create a new application run folder for the job-application skill.

Refuses to proceed while mandatory sources are unresolved (preflight gate),
derives the next NN_ prefix by scanning applications_root, copies the job
description, stubs the run artifacts from skill assets, and writes
progress.json (step_0..step_4 + step_audit + step_retro; steps 5-7 stay
reserved for the resume-and-prep companion skill).

Usage:
  init_application.py --name "<slug>" --jd <jd-text-file> [--config <sources.json>]

stdout  created-file manifest + next action
exit    0 ok · 1 refused (gate, collision, overwrite) · 2 usage error
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

from preflight import SKILL_ROOT, check, die, load_config

ASSETS = SKILL_ROOT / "assets"
SCHEMA = "job-application/progress@1"

# (id, type, depends_on, expect_artifacts, JIT reference, review gate or None)
STEPS = [
    ("step_0", "context", [], ["job-description.md"],
     "references/operating-principles.md", None),
    ("step_1", "analysis", ["step_0"], ["scoring.md"],
     "references/jd-analysis.md", None),
    ("step_2", "planning", ["step_1"], ["matches.md"],
     "references/matches-and-plan.md", None),
    ("step_3", "drafting", ["step_2"], ["cover-letter-draft.md", "review-report.json"],
     "references/cover-letter-writing.md", {"tier": 1, "scope": "full"}),
    ("step_4", "rewriting", ["step_3"], ["cover-letter-draft-v2.md"],
     "references/writing-passes.md", {"tier": 1, "scope": "delta",
                                      "trigger": "substantive-changes"}),
    ("step_audit", "verification", ["step_4"], ["review-report.json"],
     "references/operating-principles.md", {"tier": 2, "scope": "delta"}),
    ("step_retro", "learning-loop", ["step_audit"], ["run-log.md"],
     "references/retro-and-run-log.md", None),
]

STUBS = [  # (template, target, label)
    ("scoring-template.md", "scoring.md", "stub from assets/scoring-template.md"),
    ("matches-template.md", "matches.md", "stub from assets/matches-template.md"),
    ("progress-template.md", "progress.md", "stub from assets/progress-template.md"),
    ("run-log-template.md", "run-log.md", "stub from assets/run-log-template.md"),
]


def next_run_folder(apps_root: Path, slug: str) -> Path:
    if not apps_root.is_dir():
        die(f"applications_root does not exist: {apps_root}",
            "create it or fix the key: preflight.py --set applications_root <dir>")
    nums = []
    for d in apps_root.iterdir():
        m = re.match(r"^(\d+)_", d.name)
        if d.is_dir() and m:
            try:
                nums.append(int(m.group(1)))
            except ValueError:
                continue
    n = (max(nums) + 1) if nums else 1
    folder = apps_root / f"{n:02d}_{slug}"
    if folder.exists():
        die(f"run folder already exists: {folder}", "choose a different --name slug")
    return folder


def build_progress(folder: Path, created: str) -> dict:
    steps = {}
    for sid, stype, deps, arts, ref, review in STEPS:
        steps[sid] = {
            "type": stype, "status": "pending", "depends_on": deps,
            "expect_artifacts": arts, "reference": ref,
            **({"review": review} if review else {}),
        }
    return {"schema": SCHEMA, "run": folder.name, "created": created, "steps": steps}


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Create a new application run folder (preflight-gated).",
        epilog="stdout: manifest · exit 0 created / 1 refused / 2 usage")
    ap.add_argument("--name", required=True, help="run slug, e.g. \"senior-qa-engineer-acme\"")
    ap.add_argument("--jd", required=True, help="path to a text file holding the job description")
    ap.add_argument("--config", help="alternative sources.json (default: assets/sources.json)")
    a = ap.parse_args()

    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", a.name):
        die(f"invalid slug: {a.name!r}", "use lowercase letters, digits, single hyphens")

    cfg_path, cfg = load_config(a.config)
    _, missing = check(cfg)
    if missing:
        for m in missing:
            print(f"BLOCKED mandatory source missing: {m['key']} ({m['function']})\n"
                  f"  fix: preflight.py --set {m['key']} <path>", file=sys.stderr)
        sys.exit(1)

    jd = Path(a.jd).expanduser()
    if not jd.is_file():
        die(f"job description file not found: {jd}", "pass --jd <path-to-text-file>")

    apps_root = Path(cfg["applications_root"]).expanduser()
    folder = next_run_folder(apps_root, a.name)
    created = datetime.now().isoformat(timespec="seconds")
    manifest = []

    def write(rel: str, text: str, label: str) -> None:
        target = folder / rel
        if target.exists():
            die(f"refusing overwrite: {target}", "run folders are created once")
        target.write_text(text)
        manifest.append(f"  {rel:<24} <- {label}")

    folder.mkdir(parents=True)
    write("job-description.md", jd.read_text() if not jd.name.endswith(".pdf")
          else die("PDF job description: convert to text first", "--jd needs a text file"),
          f"copied from {jd.name}")
    for tpl, target, label in STUBS:
        src = (ASSETS / tpl).read_text()
        write(target, src.replace("<NN_slug>", folder.name), label)
    write("progress.json",
          json.dumps(build_progress(folder, created), indent=2) + "\n",
          "machine state (all steps pending)")

    print(f"created run folder: {folder}")
    print("\n".join(manifest))
    print(f"next: python3 {SKILL_ROOT / 'scripts' / 'progress.py'} {folder} --status")


if __name__ == "__main__":
    main()
