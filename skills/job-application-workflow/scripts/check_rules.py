#!/usr/bin/env python3
"""Per-rule check loop. The script is the state machine; the agent is the
per-rule executor. EVERY rule of EVERY step gets its own check file. One
isolated attention window per rule, closed before the step checkpoint.

WHERE IT IS INVOKED
  Every step procedure in SKILL.md runs this after the step's work and
  verify, before the checkpoint (step_3: before the judge):
    scripts/check_rules.py <run> --step step_N --next   # one rule at a time
    scripts/check_rules.py <run> --step step_N --gate   # closes the step
  references/rule-digests.md lists every step's rules and, per rule, what
  the gate demands: `quote`, `confirm` or `measure`.

THREE EVIDENCE KINDS (the gate checks all automatically; each rule
declares its kind in its frontmatter `evidence:` field)
  quote: the check file must carry a `quote`, a span copied verbatim
  from the step's artifact. The gate re-opens the artifact and finds
  it; paraphrase fails.
  confirm: the check file must carry a `confirmation`, a written
  statement of how the rule is honored (what you did, or what you
  will do at the checkpoint). The gate checks it is present and
  substance, not truth: fabrication is a separate problem.
  measure: the check file must state the measurement in `note`, with
  its number (budget and size rules). A pasted sentence proves
  nothing: the gate recomputes the artifact and requires the true
  number (a pass over budget records the user's growth approval).
  A quote is optional here; at steps with an artifact, the gate
  verifies any quote it finds verbatim.

--gate re-validates every check file (evidence guards, verdict/score
consistency, fix-required-on-fail, sibling attestation, score
threshold: rule_check.min_score in sources.json) and aggregates scores into
<run>/rule-checks.json for the retro. Exit 0 on --gate is part of the
step checkpoint; a failed gate is a finding, not an obstacle: apply the
named fixes and re-check with --rule <id>.

Check file format (checks/<step>/<rule-id>.md, one line per field):
  rule: <rule-id>
  verdict: pass | fail
  score: 0-3   (3 clean pass | 2 borderline, acceptable |
                1 violation, fix proposed | 0 violation, not fixed)
  quote: "<span copied verbatim from the artifact>"    (evidence: quote)
  confirmation: <how this rule is honored>              (evidence: confirm)
  note: <required for measure rules: the measurement with its number;
         optional otherwise: what you scanned>
  fix: <required when verdict: fail, the concrete rewrite>
  siblings-checked: yes
"""

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import rules_meta as rm

FIELDS = ("rule", "verdict", "score", "quote", "confirmation",
          "note", "fix", "siblings-checked")
FILLER = ("n/a", "tbd", "placeholder")


def bail(msgs, code: int = 1, hints: str = "") -> None:
    for m in msgs if isinstance(msgs, list) else [msgs]:
        print(f"FAIL: {m}", file=sys.stderr)
    if hints:
        print(f"  fix: {hints}", file=sys.stderr)
    sys.exit(code)


def read_config(path: Path) -> dict:
    try:
        return json.loads(path.read_text()).get("rule_check", {})
    except (json.JSONDecodeError, OSError) as e:
        bail(f"config unreadable: {path} ({e})", hints="fix the JSON syntax")


def collapse(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def parse_check(path: Path) -> dict:
    fields: dict[str, str] = {}
    for line in path.read_text().splitlines():
        m = re.match(r"^([a-z][\w-]*):\s*(.*)$", line)
        if m and m.group(1) in FIELDS:
            key = m.group(1)
            val = m.group(2).strip().strip('"')
            if key in fields:  # duplicate field: last one wins, but note it
                fields.setdefault("_duplicates", "")
                fields["_duplicates"] += f" {key}"
            fields[key] = val
    return fields


def validate(run: Path, step: str, config_path: Path | None = None) -> dict:
    """Gate validation with no side effects and no exit. Single source of
    truth for the check-file guards: used by --gate here and by
    verify_artifacts.py --artifact rule-check (step_audit re-checks a
    closed step). Returns: rows (id/verdict/score per rule with a check
    file), problems (empty list = the gate passes), loop (the step's
    rules), artifact (the step's artifact or None), min_score."""
    config = read_config(config_path
                         or rm.SKILL_ROOT / "assets" / "sources.json")
    min_score = int(config.get("min_score", 2))
    budgets = config.get("word_budgets", {})
    rules, steps = rm.load_rules(), rm.load_steps()
    empty = {"rows": [], "problems": [], "loop": [], "artifact": None,
             "min_score": min_score}
    if step not in {s["id"] for s in steps}:
        empty["problems"] = [f"unknown step {step!r} (steps: "
                             + ", ".join(s["id"] for s in steps) + ")"]
        return empty
    artifact = (run / rm.STEP_ARTIFACTS[step]
                if step in rm.STEP_ARTIFACTS else None)
    loop = rm.loop_rules(step, rules, steps)
    cdir = run / "checks" / step
    empty["loop"] = loop
    if artifact is not None and not artifact.is_file():
        empty["problems"] = [f"artifact not found: {artifact}. Run the "
                             "loop after verify_artifacts passes on the "
                             "artifact"]
        return empty
    if not cdir.is_dir():
        empty["problems"] = [f"no check files for {step} ({cdir} missing). "
                             "run --next and check each rule first"]
        return empty
    art_text = collapse(artifact.read_text()) if artifact is not None else ""
    problems, rows = [], []
    for meta in loop:
        rid = rm.display(meta["id"])
        cpath = cdir / f"{rid}.md"
        if not cpath.is_file():
            problems.append(f"{rid}: no check file at checks/{step}/"
                            f"{rid}.md: run --next and write the check file")
            continue
        f = parse_check(cpath)
        tag = f"{rid}: "
        if f.get("rule", "") != rid:
            problems.append(tag + f"rule field {f.get('rule')!r} does not "
                          f"match the filename")
        if "verdict" not in f or f.get("verdict") not in ("pass", "fail"):
            problems.append(tag + f"verdict {f.get('verdict')!r} not in "
                          "['pass', 'fail']")
        try:
            score = int(f.get("score", ""))
            assert 0 <= score <= 3
        except (ValueError, AssertionError):
            problems.append(tag + f"score {f.get('score')!r} not in 0-3 "
                          f"in checks/{step}/{rid}.md: write 0-3 "
                          "(3 clean pass, 2 acceptable, 1 violation fix "
                          "proposed, 0 not fixed)")
            score = None
        if score is not None and f.get("verdict") in ("pass", "fail"):
            want = {2, 3} if f["verdict"] == "pass" else {0, 1}
            if score not in want:
                problems.append(tag + f"score {score} contradicts verdict "
                              f"{f['verdict']!r} (pass→2-3, fail→0-1)")
        if not meta.get("evidence_raw"):
            problems.append(tag + "rule file declares no `evidence:` "
                          "field: declare quote, confirm or measure "
                          "(build_digests enforces this too)")
        kind = rm.evidence_kind(meta, step)
        q = f.get("quote", "")
        if kind == "quote":
            if not q:
                problems.append(tag + "quote missing. A quote-rule check "
                              "without a verbatim span proves nothing")
            elif collapse(q) not in art_text:
                where = (f"in {rm.STEP_ARTIFACTS[step]}"
                         if step in rm.STEP_ARTIFACTS else "in the artifact")
                problems.append(tag + f"quote not found {where}: "
                              f"{q[:60]!r}… "
                              "(quotes must be verbatim from the artifact)")
        elif kind == "confirm":
            c = f.get("confirmation", "")
            if not c:
                problems.append(tag + "confirmation missing. State how "
                              "this rule is honored (what you did or will do)")
        else:  # measure: the gate redoes the math, not the writer's word
            n = f.get("note", "")
            if not n:
                problems.append(tag + "note missing. Measure rules state "
                              "the measurement (its number) in the note")
            elif not re.search(r"\d", n):
                problems.append(tag + "note carries no number. A "
                              "measurement needs a digit, e.g. '4,912 chars "
                              "against the 5,000 cap'")
            m = rm.measure_artifact(artifact, budgets)
            if m and n:
                unit, val, budget = m
                if str(val) not in n and f"{val:,}" not in n:
                    problems.append(tag + "measurement does not recompute. "
                                  f"The artifact measures {val} {unit} "
                                  "against its budget; state that number "
                                  "(the gate redid the math)")
                approved = "user" in n.lower() and "approv" in n.lower()
                if f.get("verdict") == "pass" and val > budget \
                        and not approved:
                    problems.append(tag + "pass on an over-budget artifact "
                                  f"({val} {unit} against {budget}). Growth "
                                  "past the budget needs the user's "
                                  "approval, recorded in the note")
                if f.get("verdict") == "fail" and val <= budget:
                    problems.append(tag + "fail on an under-budget artifact "
                                  f"({val} {unit} against {budget}). The "
                                  "measurement contradicts the verdict")
        if q and kind != "quote" and artifact is not None \
                and collapse(q) not in art_text:
            problems.append(tag + f"quote not found in "
                          f"{rm.STEP_ARTIFACTS[step]}: {q[:60]!r}… "
                          "(any quote a check file claims is verified "
                          "verbatim)")
        if f.get("verdict") == "fail" and not f.get("fix", "").strip():
            problems.append(tag + "verdict fail but no fix field")
        if f.get("siblings-checked", "") != "yes":
            problems.append(tag + f"siblings-checked must be 'yes' in "
                          f"checks/{step}/{rid}.md. Scan the artifact for "
                          "siblings of any issue found and set it")
        for fld in ("quote", "confirmation", "note", "fix"):
            val = f.get(fld, "")
            hit = next((x for x in FILLER if x in val.lower()), "")
            if val and hit:
                remedy = ('on a pass verdict write "fix: none required '
                          '(verdict pass, no violation to repair)"; on a '
                          'fail verdict state the repair action'
                          if fld == "fix" else
                          f'replace "{hit}" with the real {fld} content')
                problems.append(tag + f'banned filler "{hit}" in {fld}\n'
                                f"  file: checks/{step}/{rid}.md\n"
                                f"  fix: {remedy}")
        if f.get("_duplicates"):
            problems.append(tag + f"duplicate fields:{f['_duplicates']}")
        rows.append({"id": rid, "verdict": f.get("verdict"),
                     "score": score if score is not None else -1})
    for stray in sorted(p.name for p in cdir.glob("*.md")):
        if stray[:-3] not in {rm.display(m["id"]) for m in loop}:
            problems.append(f"stray check file {stray}, not a rule of "
                            f"{step}")
    for r in rows:
        if r["score"] >= 0 and r["score"] < min_score:
            problems.append(f"{r['id']}: score {r['score']} below threshold "
                            f"{min_score}. Apply the fix and re-check "
                            f"with --rule {r['id']}")
    return {"rows": rows, "problems": problems, "loop": loop,
            "artifact": artifact, "min_score": min_score}


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Per-rule check loop: one rule per attention window."
    )
    ap.add_argument("run", help="run folder, e.g. ~/apps/12_senior-qa-engineer-acme")
    ap.add_argument("--step", required=True, help="step id from SKILL.md")
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--next", action="store_true",
                      help="present the next unchecked rule")
    mode.add_argument("--gate", action="store_true",
                      help="validate all check files, aggregate scores")
    ap.add_argument("--rule", help="re-present a specific rule (with --next)")
    ap.add_argument("--config", help="alternative sources.json")
    a = ap.parse_args()

    run = Path(a.run).expanduser()
    if not run.is_dir():
        bail(f"run folder not found: {run}", hints="check the path")
    rules, steps = rm.load_rules(), rm.load_steps()
    if a.step not in {s["id"] for s in steps}:
        bail(f"unknown step {a.step!r}",
             hints=f"steps: {', '.join(s['id'] for s in steps)}")
    artifact = (run / rm.STEP_ARTIFACTS[a.step]
                if a.step in rm.STEP_ARTIFACTS else None)
    if artifact is not None and not artifact.is_file():
        bail(f"artifact not found: {artifact}",
             hints="run the loop after verify_artifacts passes on the artifact")

    loop = rm.loop_rules(a.step, rules, steps)
    cdir = run / "checks" / a.step

    if a.next:
        cdir.mkdir(parents=True, exist_ok=True)
        if a.rule:
            key = rm.norm(a.rule)
            todo = [m for m in loop if m["id"] == key]
            if not todo:
                bail(f"{a.rule!r} is not a rule of {a.step}",
                     hints=f"rules: {', '.join(rm.display(m['id']) for m in loop)}")
            meta = todo[0]
            pos = [m["id"] for m in loop].index(key) + 1
            done = "already checked, this is a re-check" if \
                (cdir / f"{rm.display(key)}.md").is_file() else "unchecked"
        else:
            todo = [m for m in loop
                    if not (cdir / f"{rm.display(m['id'])}.md").is_file()]
            if not todo:
                print(f"all {len(loop)} rules checked. Run --gate to close "
                      f"{a.step}")
                return
            meta = todo[0]
            pos = [m["id"] for m in loop].index(meta["id"]) + 1
            done = "unchecked"
        cpath = cdir / f"{rm.display(meta['id'])}.md"
        kind = rm.evidence_kind(meta, a.step)
        print(f"rule {pos}/{len(loop)}: {rm.display(meta['id'])}  "
              f"({meta['type']}, {done})")
        print(f"expect: {meta['expect']}")
        print(f"on_fail: {meta['on_fail'] or '—'}")
        print()
        if kind == "quote":
            print(f"Check ONLY this rule against {artifact}.")
        elif kind == "measure":
            print(f"Measure ONLY this rule against {artifact}: state the "
                  "measurement and its true number in the note field. The "
                  "gate recomputes the artifact: the number must match, "
                  "and a pass over budget must record the user's growth "
                  "approval. A quote is optional and, if added, must be "
                  "verbatim from the artifact.")
        else:
            print("Check ONLY this rule. It governs how you work, not the "
                  "artifact text: confirm in writing how it is honored, "
                  "what you did or what you will do at the checkpoint.")
        print(f"Then write {cpath} (one line per field):")
        print()
        print(f"  # rule-check: {rm.display(meta['id'])}")
        print(f"  rule: {rm.display(meta['id'])}")
        print("  verdict: pass            # pass | fail")
        print("  score: 3                  # 3 clean pass | 2 borderline, "
              "acceptable | 1 violation, fix proposed | 0 violation, not fixed")
        if kind == "quote":
            print('  quote: "<span copied verbatim from the artifact. The '
                  'gate rejects paraphrase>"')
        elif kind == "measure":
            print("  note: <required: the measurement with its number "
                  "for this step's artifact, e.g. '1,912 chars against "
                  "the 5,000 cap'>")
        else:
            print("  confirmation: <how this rule is honored: what you did "
                  "or will do>")
        if kind != "measure":
            print("  note: <optional: a measurement or what you scanned>")
        print("  fix: <required when verdict: fail — the concrete rewrite>")
        print("  siblings-checked: yes")
        print()
        print("The gate rejects: missing check files, the wrong or missing "
              "evidence for this rule, fail without a fix, siblings "
              "unchecked, scores below the threshold. Then run --next again.")
        return

    # --gate (guards live in validate(), shared with
    # verify_artifacts.py --artifact rule-check)
    v = validate(run, a.step,
                 Path(a.config).expanduser() if a.config else None)
    rows, loop, min_score, problems = (v["rows"], v["loop"],
                                       v["min_score"], v["problems"])
    if problems:
        for p in problems:
            print(f"FAIL: {p}", file=sys.stderr)
        bad = [r["id"] for r in rows if r["score"] in (0, 1)]
        print(f"  fix: {len(problems)} problem(s); "
              + (f"re-check: {', '.join(bad)}; " if bad else "")
              + "a failed gate is a finding, not an obstacle",
              file=sys.stderr)
        sys.exit(1)

    # aggregate for the retro (worst-rules signal, chunk iv)
    agg_path = run / "rule-checks.json"
    agg = {"run": run.name, "steps": {}}
    if agg_path.is_file():
        try:
            agg = json.loads(agg_path.read_text())
        except json.JSONDecodeError:
            pass  # corrupted aggregate: rebuild rather than block the gate
    agg.setdefault("steps", {})[a.step] = {
        "checked": date.today().isoformat(),
        "artifact": rm.STEP_ARTIFACTS.get(a.step, ""),
        "rules": [{"id": r["id"], "verdict": r["verdict"], "score": r["score"]}
                  for r in rows],
    }
    agg_path.write_text(json.dumps(agg, indent=2) + "\n")

    avg = sum(r["score"] for r in rows) / len(rows)
    print(f"ok: {a.step} rule gate: {len(rows)}/{len(loop)} rules, "
          f"min {min(rows and [r['score'] for r in rows])}, "
          f"avg {avg:.1f}, threshold {min_score}")
    print(f"ok: aggregated to {agg_path.name} (retro signal)")
    print(f"  {'pass' if all(r['verdict'] == 'pass' for r in rows) else 'mixed'}: "
          + ", ".join(f"{r['id']}={r['score']}" for r in rows))


if __name__ == "__main__":
    main()