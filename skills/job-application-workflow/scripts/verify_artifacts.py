#!/usr/bin/env python3
"""Tier 0 mechanical checks for job-application run artifacts (exit 0 is what
unblocks progress.py --approve); the LLM judge never sees text that fails here.
stdout: report | stderr: failures + fix hints | exit 0 pass / 1 failed / 2 usage.
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import NoReturn

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_rules as cr
import rules_meta as rm

SKILL_ROOT = Path(__file__).resolve().parent.parent
BANNED = SKILL_ROOT / "assets" / "banned-terms.json"
DIMENSIONS = [
    "question coverage",
    "source fidelity",
    "demonstration",
    "story continuity",
    "evidence economy",
    "reader ease",
]


def bail(msgs, p: Path | None = None, code: int = 1, hints: str = "") -> NoReturn:
    for m in msgs if isinstance(msgs, list) else [msgs]:
        print(f"FAIL {p.name}: {m}" if p else f"verify: {m}", file=sys.stderr)
    if hints:
        print(f"  fix: {hints}", file=sys.stderr)
    sys.exit(code)


def list_items(text: str, heading: str) -> list[str]:
    """Bullet/numbered lines under the section named by regex `heading`."""
    m = re.search(rf"(?im)^#+\s*{heading}(?!\w)", text)
    if not m:
        return []
    body = text[m.end() :].split("\n#", 1)[0]  # up to the next markdown heading
    return [
        re.sub(r"^\s*(?:[-*]|\d+[.)])\s+", "", ln).strip()
        for ln in body.splitlines()
        if re.match(r"^\s*(?:[-*]|\d+[.)])\s+\S", ln)
    ]


def keyword_covered(item: str, letter: str, cfg: dict) -> bool:
    """Smoke check: every non-skipped keyword carries >=1 core token into the
    letter; substance is judged by the rubric + judge, never by this check."""
    if re.search(cfg["skip_markers"], item, re.I):
        return True  # explicitly excluded from the letter in matches.md
    phrase = re.sub(r"\*\*|`", "", re.split(r"\s+[—–]\s+", item)[0])
    for sub in re.split(r"[;·]", phrase):
        tokens = [
            t
            for t in re.findall(r"[a-z0-9][a-z0-9'+./-]*", sub.lower())
            if len(t) >= 2 and t not in cfg["stop_tokens"]
        ]
        hit = any(t in letter or (t.endswith("e") and t[:-1] in letter) for t in tokens)
        if not tokens or hit:  # suffixed / e-stem forms match too (evolve->evolving)
            return True
    return False


def check_scoring(p: Path, max_chars: int) -> None:
    text = p.read_text()
    head = re.search(r"(?im)^#+\s*.*Scoring Results.*$", text)
    sec = text[head.end() :].split("\n#", 1)[0] if head else ""
    if not sec.strip():
        bail(
            "'Scoring Results' section missing",
            p,
            hints="add it per assets/scoring-template.md",
        )
    if len(sec) > max_chars:
        bail(
            f"Scoring Results is {len(sec)} chars, expected <= {max_chars}",
            p,
            hints="one trim pass to a stated target, re-verify (rule_word_budget)",
        )
    rub = re.search(r"(?im)^\s*[-*]?\s*rubric used:\s*(\S+)", text)
    rows = [
        ln
        for ln in sec.splitlines()
        if ln.strip().startswith("|") and not re.match(r"^\s*\|[\s:|-]+\|\s*$", ln)
    ]
    problems = [] if rub else ["no 'Rubric used:' line — name the rubric by its key"]
    if len(rows) < 4:
        problems.append(f"per-criterion rows: {len(rows) - 1}, expected >= 3")
    if not re.search(
        r"(?im)verdict:\s*(promote|do\s*not\s*promote|do-not-promote)", sec
    ):
        problems.append(
            "no verdict line — end with 'verdict: PROMOTE'/'DO NOT PROMOTE'"
        )
    if problems:
        bail(problems, p)
    print(
        f"ok: scoring — section {len(sec)}/{max_chars} chars, rubric "
        f"{rub.group(1) if rub else '?'}, {len(rows) - 1} rows, verdict present"
    )


def check_matches(p: Path, max_chars: int) -> None:
    text, problems = p.read_text(), []
    # measure the artifact's content, not its annotations: HTML
    # comments (a gold file's provenance header) are excluded, the
    # same way the letter check counts only the salutation-to-signoff
    # body and the scoring check only the Scoring Results section.
    content = re.sub(r"(?s)<!--.*?-->", "", text)
    if len(content) > max_chars:
        problems.append(f"{len(content)} chars, expected < {max_chars} (rule_word_budget)")
    missing = [
        h
        for h in ("Target role", "Keywords Skills", "Keywords Tools")
        if not re.search(rf"(?im)^#+\s*.*{re.escape(h)}", content)
    ]
    if missing:
        problems.append(f"required sections missing: {', '.join(missing)}")
    if not re.search(r"(?im)^\s*[-*]?\s*role type:\s*\S", content):
        problems.append("'Role type:' line missing from Target role")
    for name, lo, hi in (
        ("Mapping List 1", 5, 7),
        ("Mapping List 2", 5, 7),
        ("Remaining gaps", 3, 5),
    ):
        n = len(list_items(content, re.escape(name)))
        (
            print(f"ok: matches — {name}: {n} items")
            if lo <= n <= hi
            else problems.append(f"{name} has {n} items, expected {lo}-{hi}")
        )
    if problems:
        bail(problems, p)
    print(f"ok: matches — sections + role type present, {len(content)}/{max_chars} chars")


def check_letter(p: Path, matches: Path | None, max_words: int) -> None:
    try:
        catalog = json.loads(BANNED.read_text())
    except (json.JSONDecodeError, KeyError) as e:
        bail(f"banned-terms catalog unreadable: {e}", hints=f"check {BANNED}")
    text = p.read_text()
    norm = text.lower().replace("\u2019", "'")
    misses = []

    def add(cond: bool, msg: str) -> None:
        if not cond:
            misses.append(msg)

    for t in catalog["terms"] + catalog["letter_structure"]:
        pat = t.get("pattern", t.get("count_pattern", ""))
        hits = [m.group(0)[:60] for m in re.finditer(pat, norm, re.I | re.M)]
        if t.get("min") is not None:  # structure count check (run-in subheads)
            add(len(hits) >= t["min"], t["message"].format(n=len(hits)))
        elif t.get("max") is not None:  # ceiling check (em-dash = 0)
            add(len(hits) <= t["max"], t["message"].format(n=len(hits)))
        elif t.get("require"):  # structure presence check
            add(bool(hits), t["message"])
        elif hits and t["severity"] == "fail":
            misses.append(
                f'banned term [{t["id"]}] x{len(hits)}: "{hits[0]}" — {t["hint"]}'
            )
        elif hits:
            print(
                f'WARNING banned term [{t["id"]}] x{len(hits)}: "{hits[0]}" — review only'
            )
    add(
        bool(re.search(r"(?ims)^dear\b[^|]{80,}", text)),
        "no intro paragraph before the table — the intro is the executive summary "
        "(references/cover-letter-writing.md)",
    )
    mt = matches.read_text() if matches else ""
    items = (
        list_items(mt, r"Keywords\s+Skills") + list_items(mt, r"Keywords\s+Tools")
        if mt
        else []
    )
    if not matches:
        print("WARNING keyword coverage skipped: --matches <matches.md> not given")
    gaps = [
        i for i in items if not keyword_covered(i, norm, catalog["keyword_coverage"])
    ]
    if gaps:
        misses.append(
            f"keyword coverage {len(items) - len(gaps)}/{len(items)}, expected "
            f"100% — not covered: {'; '.join(gaps[:4])}"
        )
    body = re.search(
        r"(?ims)^dear\b(.*?)(?=^\s*(?:sincerely|kind regards|regards|best regards)[,.!]?\s*$)",
        text,
    )
    words = len(re.findall(r"\S+", body.group(1) if body else text))
    if "v2" in p.name and not p.with_name(p.name.replace("-v2", "")).is_file():
        misses.append(f"version preservation: {p.name} exists but v1 is missing")
    if words > max_words:
        misses.append(
            f"word budget: {words}, expected <= {max_words} — trim once "
            "(rule_word_budget); growth needs user approval"
        )
    if misses:
        bail(misses, p)
    print(
        f"ok: letter — body {words}/{max_words} words, keyword coverage "
        f"{len(items) - len(gaps)}/{len(items) or 1}, em-dash 0, structure complete"
    )


def check_report(p: Path, art: Path | None = None,
                 budgets: dict | None = None) -> None:
    try:
        rep = json.loads(p.read_text())
    except json.JSONDecodeError as e:
        bail(
            f"{p}: not valid JSON ({e})", hints="use assets/review-report-template.json"
        )
    flags, problems = rep.get("flagged_items", []), []
    # quote verification is default-on: with no --artifact-path, resolve
    # the report's own `artifact` field against the report's folder (the
    # run folder for a real report). Degrade to the trailing note only
    # when that file is absent, so exemplars verified from examples/
    # keep working; --artifact-path remains the override (peer review
    # fix 2: the strongest check must not depend on the runner's
    # obedience to one SKILL.md instruction).
    if art is None:
        candidate = p.parent / str(rep.get("artifact", ""))
        if candidate.is_file():
            art = candidate
    j = rep.get("judge") or {}
    ident = str(j.get("identity") or "")
    if not ident:
        problems.append("judge identity not recorded")
    elif re.search(r"<[^>]*>", ident):
        problems.append(
            "judge identity is a template placeholder: name the "
            "model or agent that judged (instantiation recipe in "
            "operating-principles.md)"
        )
    if j.get("kind") not in ("subagent", "different-model",
                             "peer-agent", "self-review"):
        problems.append(
            f"judge kind {j.get('kind')!r} not in ('subagent', "
            "'different-model', 'peer-agent', 'self-review')"
        )
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(j.get("date", ""))):
        problems.append("judge date not recorded (YYYY-MM-DD)")
    if ident == "constructed exemplar, no real judge (see _exemplar)" \
            and "_exemplar" not in rep:
        problems.append(
            "judge identity names the constructed exemplar without its "
            "_exemplar key: a real report names the model or agent that judged"
        )
    for field, allowed in (
        ("verdict", ("approved", "needs-fixes")),
        ("tier", (1, 2)),
        ("scope", ("full", "delta")),
    ):
        if rep.get(field) not in allowed:
            problems.append(f"{field} {rep.get(field)!r} not in {allowed}")
    if [d.get("name", "").lower() for d in rep.get("dimensions", [])] != DIMENSIONS:
        problems.append("dimensions do not match the 6 paragraph-rubric dimensions")
    problems += [
        f"flagged item {f.get('id', '?')} has no resolved field"
        for f in flags
        if "resolved" not in f
    ]
    # rules_audit (schema @3): one entry per quote-or-measure rule of the
    # judged artifact's step (confirm rules are the writer's check files'
    # job). The scope comes from the report's `artifact` field, falling
    # back to `step`: a tier-2 report runs at step_audit but judges a
    # letter, and scoping it to its own step demanded an empty audit,
    # which verified nothing (peer review fix 2).
    step = rep.get("step", "")
    scope = rm.step_for_artifact(rep.get("artifact", "")) or step
    art_name = str(rep.get("artifact", ""))
    if art_name and rm.step_for_artifact(art_name) == "":
        problems.append(f"artifact {art_name!r} matches no step artifact: "
                        "name the bare file: scoring.md, matches.md, "
                        "cover-letter-draft.md or cover-letter-draft-v2.md")
    loop = rm.audit_rules(scope) if scope else []
    audit = rep.get("rules_audit")
    if not step:
        problems.append("step field missing: say which step produced "
                        "this report")
    if not scope:
        problems.append("rules_audit scope unresolvable: the report "
                        "names no known step artifact and no step")
    elif not loop:
        problems.append(f"rules_audit scope {scope!r} carries no quote "
                        "or measure rules: a review report must judge "
                        "a step artifact (scoring.md, matches.md or a "
                        "letter draft); a report judging only its own "
                        "step audits nothing")
    if not isinstance(audit, list):
        problems.append(
            "rules_audit missing or not a list: schema @3 requires one "
            "entry per quote-or-measure rule of the judged artifact's "
            "step (see review-report-template.json)"
        )
    else:
        want = [rm.display(m["id"]) for m in loop]
        got = [e.get("id", "?") for e in audit]
        for rid in want:
            if rid not in got:
                problems.append(f"rules_audit missing entry for {rid}")
        for rid in got:
            if rid not in want:
                problems.append(
                    f"rules_audit entry {rid!r} is not audited at {scope} "
                    "(only that step's quote and measure rules carry "
                    "rules_audit entries)"
                )
        art_text = None
        if art is not None:
            if art.is_file():
                art_text = re.sub(r"\s+", " ", art.read_text())
            else:
                problems.append(f"artifact-path not found: {art}")
        kinds = {rm.display(m["id"]): rm.evidence_kind(m, scope) for m in loop}
        for e in audit:
            rid = e.get("id", "?")
            if e.get("verdict") not in ("pass", "fail"):
                problems.append(
                    f"rules_audit {rid}: verdict {e.get('verdict')!r} "
                    "not in ['pass', 'fail']"
                )
            if not (e.get("evidence") or "").strip():
                problems.append(
                    f"rules_audit {rid}: evidence empty. Say what you checked"
                )
            q = (e.get("quote") or "").strip()
            if kinds.get(rid) == "measure":
                # measurement rules: the gate redoes the math. The number
                # in evidence must match what the artifact actually
                # measures, and the verdict must match the budget state
                # (pass over budget needs the user's growth approval).
                ev = (e.get("evidence") or "").strip()
                if not re.search(r"\d", ev):
                    problems.append(
                        f"rules_audit {rid}: evidence states no measurement. "
                        "A measure entry needs its number, e.g. 'body "
                        "1,187 words against the 1,000-word budget'"
                    )
                m = rm.measure_artifact(art, budgets)
                if m:
                    unit, val, budget = m
                    if str(val) not in ev and f"{val:,}" not in ev:
                        problems.append(
                            f"rules_audit {rid}: measurement does not "
                            f"recompute. The artifact measures {val} {unit} "
                            "against its budget; state that number "
                            "(the gate redid the math)"
                        )
                    approved = "user" in ev.lower() and "approv" in ev.lower()
                    if e.get("verdict") == "pass" and val > budget \
                            and not approved:
                        problems.append(
                            f"rules_audit {rid}: pass on an over-budget "
                            f"artifact ({val} {unit} against {budget}). "
                            "Growth past the budget needs the user's "
                            "approval, recorded in the evidence"
                        )
                    if e.get("verdict") == "fail" and val <= budget:
                        problems.append(
                            f"rules_audit {rid}: fail on an under-budget "
                            f"artifact ({val} {unit} against {budget}). "
                            "The measurement contradicts the verdict"
                        )
                if q and art is not None and art_text is not None \
                        and re.sub(r"\s+", " ", q) not in art_text:
                    problems.append(
                        f"rules_audit {rid}: quote not found verbatim in "
                        f"{art.name}: {q[:60]!r}…"
                    )
            else:
                if not q:
                    problems.append(
                        f"rules_audit {rid}: quote empty. Cite a span from the artifact"
                    )
                elif art is not None and art_text is not None and re.sub(r"\s+", " ", q) not in art_text:
                    problems.append(
                        f"rules_audit {rid}: quote not found verbatim in "
                        f"{art.name}: {q[:60]!r}…"
                    )
        if rep.get("verdict") == "approved":
            bad = [e.get("id", "?") for e in audit if e.get("verdict") != "pass"]
            if bad:
                problems.append(
                    f"verdict approved but rules_audit fails: {', '.join(bad)}"
                )
    unres = [f.get("id", "?") for f in flags if not f.get("resolved")]
    if rep.get("verdict") != "approved":
        problems.append(
            f"verdict {rep.get('verdict')!r}. The gate requires 'approved'"
        )
    if unres:
        problems.append(f"flagged items unresolved: {', '.join(unres)}")
    if problems:
        bail(problems, p)
    print(
        f"ok: review-report — verdict={rep['verdict']}, tier={rep['tier']}, "
        f"scope={rep['scope']}, judge={rep['judge']['identity']}, "
        f"{len(flags)} flagged, rules_audit {len(audit)}/{len(loop)} "
        f"(rules of {scope})"
    )
    if art is None:
        print(
            "note: rules_audit quotes NOT verbatim-checked. Pass "
            "--artifact-path <judged file>, or place the report next to "
            "the artifact it names, to enable the guard"
        )


def check_rulecheck(run: Path, step: str, cfg: Path) -> None:
    """Re-validate a step's per-rule check files at step_audit: the same
    guards check_rules.py --gate applies (single source of truth:
    check_rules.validate), so a step whose gate was green at draft time
    is proven green again at the audit."""
    v = cr.validate(run, step, cfg)
    if v["problems"]:
        bail([f"rule-check {step}: {p}" for p in v["problems"]], run,
             hints=f"scripts/check_rules.py {run} --step {step} --next "
                   "for each failed rule; --gate to close the step")
    kinds = [rm.evidence_kind(m, step) for m in v["loop"]]
    n_q, n_m = kinds.count("quote"), kinds.count("measure")
    print(
        f"ok: rule-check {step} — {len(v['rows'])}/{len(v['loop'])} rules "
        f"valid ({n_q} quote(s) verbatim, {n_m} measurement(s), "
        f"{len(kinds) - n_q - n_m} confirmation(s)), scores ≥ {v['min_score']}"
    )


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Tier 0 mechanical checks for run artifacts."
    )
    ap.add_argument(
        "--artifact",
        required=True,
        choices=["scoring", "matches", "cover-letter", "review-report",
                 "rule-check"],
    )
    ap.add_argument("--path", required=True, help="artifact file to check")
    ap.add_argument("--matches", help="matches.md, for cover-letter keyword coverage")
    ap.add_argument(
        "--max-words", type=int, help="override the cover-letter word budget"
    )
    ap.add_argument("--config", help="alternative sources.json for budgets")
    ap.add_argument(
        "--artifact-path",
        help="file the report judged (enables the rules_audit quote guard)",
    )
    ap.add_argument(
        "--step",
        help="step id, with --artifact rule-check (re-validates that "
        "step's check files the same way check_rules.py --gate does)",
    )
    a = ap.parse_args()
    p = Path(a.path).expanduser()
    if a.artifact == "rule-check":
        if not a.step:
            bail("--step <step_id> is required with --artifact rule-check")
        if not p.is_dir():
            bail(f"run folder not found: {p}",
                 hints="rule-check takes the run folder as --path")
        check_rulecheck(p, a.step,
                        Path(a.config).expanduser() if a.config
                        else SKILL_ROOT / "assets" / "sources.json")
        print("verify: PASS")
        return
    if not p.is_file():
        bail(f"artifact not found: {p}", hints="check --path")
    budgets = {
        "cover_letter_default": 1000,
        "scoring_results_max_chars": 5000,
        "matches_max_chars": 10000,
    }
    cfg = (
        Path(a.config).expanduser()
        if a.config
        else SKILL_ROOT / "assets" / "sources.json"
    )
    if a.config and not cfg.is_file():
        bail(f"config not found: {cfg}", hints="check --config")
    try:
        budgets.update(json.loads(cfg.read_text()).get("word_budgets", {}))
    except (json.JSONDecodeError, OSError) as e:
        bail(f"config unreadable: {cfg} ({e})", hints="fix the JSON syntax")
    m = Path(a.matches).expanduser() if a.matches else None
    if a.matches and not (m and m.is_file()):
        bail(
            f"matches file not found: {a.matches}",
            hints="pass the run folder's matches.md",
        )
    runs = {
        "scoring": lambda: check_scoring(p, budgets["scoring_results_max_chars"]),
        "matches": lambda: check_matches(p, budgets["matches_max_chars"]),
        "cover-letter": lambda: check_letter(
            p, m, a.max_words or budgets["cover_letter_default"]
        ),
        "review-report": lambda: check_report(
            p, Path(a.artifact_path).expanduser() if a.artifact_path else None,
            budgets
        ),
    }
    runs[a.artifact]()
    print("verify: PASS")


if __name__ == "__main__":
    main()
