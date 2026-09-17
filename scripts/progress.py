#!/usr/bin/env python3
"""Machine gate for a job-application run.

progress.json in the run folder is the single machine state; any session
resumes via --status, which prints the current step together with the
reference file to read for it (JIT pointer, fights drift).

Usage:
  progress.py <run-folder> --status
  progress.py <run-folder> --start <step_id>
  progress.py <run-folder> --approve <step_id>

stdout  status table / gate report
stderr  refusal details (missing dependency, artifact, or judge report)
exit    0 ok · 1 gate refused · 2 usage error
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import NoReturn

SCHEMA = "job-application/progress@1"
RESERVED = {"step_5", "step_6", "step_7"}

VERIFY_CMD = {
    "step_1": "verify_artifacts.py --artifact scoring --path <run>/scoring.md",
    "step_2": "verify_artifacts.py --artifact matches --path <run>/matches.md",
    "step_3": "verify_artifacts.py --artifact cover-letter --path <run>/cover-letter-draft.md --matches <run>/matches.md",
    "step_4": "verify_artifacts.py --artifact cover-letter --path <run>/cover-letter-draft-v2.md --matches <run>/matches.md",
}

NEXT_ACTION = {
    "step_0": "sources resolved, run folder initialized; confirm context with the user, then ask for approval",
    "step_1": "score the JD against the rubric (by key) with web enrichment, write Scoring Results, verify, run the promotion-gate question",
    "step_2": "build the matches lists + gaps and the rubric-validated paragraph plan, verify, ask for approval",
    "step_3": "draft v1 per the writing reference, run the Tier 1 judge (full scope), fix flags, verify, ask for approval",
    "step_4": "apply the unslop + credibility passes to v2 (v1 preserved), delta judge only if run-log marks substantive changes, verify, ask for approval",
    "step_audit": "run the full verify matrix + Tier 2 peer judge (delta) + evidence cross-check, ask for approval",
    "step_retro": "distill the run-log into rule proposals, batch-approve, update CHANGELOG.md",
}


def die(msg: str, hint: str = "", code: int = 1) -> NoReturn:
    print(f"progress: {msg}", file=sys.stderr)
    if hint:
        print(f"  fix: {hint}", file=sys.stderr)
    sys.exit(code)


def load_state(run: Path) -> tuple[Path, dict]:
    p = run / "progress.json"
    if not p.is_file():
        die(f"progress.json not found in {run}", "run init_application.py first")
    try:
        state = json.loads(p.read_text())
    except json.JSONDecodeError as e:
        die(f"progress.json is not valid JSON: {e}", "fix or re-init the run folder")
    if state.get("schema") != SCHEMA:
        die(f"unexpected schema in {p}: {state.get('schema')!r}", f"expected {SCHEMA}")
    return p, state


def substantive_changes(run: Path) -> bool:
    log = run / "run-log.md"
    if not log.is_file():
        die("run-log.md missing", "step_4 gating reads its substantive_changes flag")
    m = re.search(r"(?im)^substantive_changes:\s*(yes|no)\s*$", log.read_text())
    return bool(m and m.group(1) == "yes")


def review_problems(run: Path, sid: str, meta: dict) -> list[str]:
    """Gate the judge report: step_3 tier1/full, step_4 delta (only when
    substantive), step_audit tier2/delta. Enforced mechanically, not by memory."""
    if sid == "step_4" and not substantive_changes(run):
        return []
    req = meta.get("review")
    if not req:
        return []  # no judge gate on step_0/step_1/step_2/step_retro
    rr = run / "review-report.json"
    if not rr.is_file():
        return [f"{sid}: review-report.json missing — an approved judge report is required "
                f"(references/operating-principles.md, reflection protocol)"]
    try:
        rep = json.loads(rr.read_text())
    except json.JSONDecodeError as e:
        return [f"{sid}: review-report.json is not valid JSON ({e})"]
    problems = []
    if (rep.get("judge") or {}).get("identity", "") in ("", None):
        problems.append(f"{sid}: judge identity not recorded in review-report.json")
    if rep.get("verdict") != "approved":
        problems.append(f"{sid}: review-report.json verdict is {rep.get('verdict')!r}, expected 'approved'")
    unresolved = [f.get("id", "?") for f in rep.get("flagged_items", []) if not f.get("resolved")]
    if unresolved:
        problems.append(f"{sid}: flagged items unresolved in review-report.json: {', '.join(unresolved)}")
    want = req or {}
    if want.get("tier") is not None and rep.get("tier") != want["tier"]:
        problems.append(f"{sid}: judge tier is {rep.get('tier')!r}, expected {want['tier']}")
    if want.get("scope") and rep.get("scope") != want["scope"]:
        problems.append(f"{sid}: judge scope is {rep.get('scope')!r}, expected {want['scope']!r}")
    return problems


def gate(sid: str, state: dict, run: Path) -> list[str]:
    steps = state["steps"]
    if sid not in steps:
        if sid in RESERVED:
            return [f"{sid} is reserved for the resume-and-prep companion skill — "
                    f"it never appears in a run of this skill"]
        return [f"unknown step id: {sid} (known: {', '.join(steps)})"]
    problems = []
    for dep in steps[sid].get("depends_on", []):
        if steps[dep]["status"] != "approved":
            problems.append(f"{sid}: dependency {dep} is {steps[dep]['status']}, expected approved")
    for art in steps[sid].get("expect_artifacts", []):
        f = run / art
        if not f.is_file() or f.stat().st_size == 0:
            problems.append(f"{sid}: expected artifact missing or empty: {art}")
    problems += review_problems(run, sid, steps[sid])
    return problems


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Read or advance the machine gate for an application run.",
        epilog="stdout: report · exit 0 ok / 1 gate refused / 2 usage")
    ap.add_argument("run_folder", help="the NN_<slug> run folder")
    group = ap.add_mutually_exclusive_group(required=True)
    group.add_argument("--status", action="store_true", help="print current step + JIT reference")
    group.add_argument("--start", metavar="ID", help="mark a step in_progress (deps must be approved)")
    group.add_argument("--approve", metavar="ID", help="approve a step through the full gate")
    a = ap.parse_args()

    run = Path(a.run_folder).expanduser()
    if not run.is_dir():
        die(f"run folder not found: {run}", "check the path (init_application.py creates it)", 2)
    state_path, state = load_state(run)
    steps = state["steps"]
    order = list(steps)

    if a.status:
        print(f"run: {state['run']}")
        for sid in order:
            s = steps[sid]
            print(f"  {sid:<11} {s['status']}")
        current = next((sid for sid in order if steps[sid]["status"] in ("pending", "in_progress")), None)
        if current is None:
            print("current: none — all steps approved; the run is complete")
        else:
            s = steps[current]
            print(f"current: {current} ({s['type']})")
            unmet = [d for d in s.get("depends_on", []) if steps[d]["status"] != "approved"]
            if unmet:
                print(f"blockers: unapproved dependencies: {', '.join(unmet)}")
            else:
                print("blockers: none")
            print(f"next: {NEXT_ACTION.get(current, 'consult references/')}")
            print(f"read now: {s['reference']}   (JIT pointer for {current})")
            if current in VERIFY_CMD:
                print(f"gate: {VERIFY_CMD[current].replace('<run>', str(run))} then progress.py --approve {current}")
        return

    sid = a.start or a.approve
    action = "start" if a.start else "approve"
    if sid in RESERVED:
        die(f"{sid} is reserved for the resume-and-prep companion skill — "
            f"it never appears in this skill's run state")
    if sid not in steps:
        die(f"unknown step id: {sid}", f"known: {', '.join(steps)}", 2)
    problems = gate(sid, state, run) if action == "approve" else \
        [f"{sid}: dependency {d} is {steps[d]['status']}, expected approved"
         for d in steps[sid].get("depends_on", []) if steps[d]["status"] != "approved"]
    if problems:
        for p in problems:
            print(f"REFUSED {p}", file=sys.stderr)
        sys.exit(1)
    if action == "start":
        steps[sid]["status"] = "in_progress"
        steps[sid]["started_at"] = datetime.now().isoformat(timespec="seconds")
    else:
        steps[sid]["status"] = "approved"
        steps[sid]["approved_at"] = datetime.now().isoformat(timespec="seconds")
    state_path.write_text(json.dumps(state, indent=2) + "\n")
    print(f"{action}d: {sid} ({steps[sid]['status']})")
    nxt = next((s for s in order if steps[s]["status"] in ("pending", "in_progress")), None)
    if nxt:
        print(f"next: {nxt} — read now: {steps[nxt]['reference']}")


if __name__ == "__main__":
    main()
