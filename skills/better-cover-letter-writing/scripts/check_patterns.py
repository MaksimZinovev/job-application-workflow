#!/usr/bin/env python3
"""Finish gate for the pattern audit of one cover letter.

Usage: python3 scripts/check_patterns.py --letter <path> [--audit <path>] [--gate]
       python3 scripts/check_patterns.py --letter <path> --next [--baseline <path>]
       python3 scripts/check_patterns.py --selftest

--next presents exactly one open row: its name, its rule file, and the
rubric scales, minimums and triggers parsed from that rule's frontmatter
at emit time, plus the evidence contract. With --baseline it also prints
what the baseline claimed for the row and asks for a fresh verdict;
disagreement is recorded as a note starting "delta:". A baseline must
itself be a completed 17-row audit.

Empty score, coverage, or evidence means the row is open. Exit 0 only when
every pattern row is closed and no refusal was raised.
"""
import argparse
import contextlib
import io
import re
import sys
import tempfile
from pathlib import Path

import yaml

SKILL_ROOT = Path(__file__).resolve().parent.parent
QUALITY = ["poor", "acceptable", "good", "excellent"]
COMPLETENESS = ["none", "partial", "most", "all"]
PATTERN_COUNT = 17  # ponytail: single count source; assumes contiguous rows 1..N
ARROW = chr(0x2192)
AUDIT_DASH = chr(0x2014)
LQUOTE = chr(0x201C)
RQUOTE = chr(0x201D)


def die(msg, fix):
    print(f"check: {msg}", file=sys.stderr)
    print(f"fix: {fix}", file=sys.stderr)
    sys.exit(2)


def parse_frontmatter(text):
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        return {}
    data = yaml.safe_load("\n".join(lines[1:end]))
    return data if isinstance(data, dict) else {}


def rule_for(n):
    hits = sorted((SKILL_ROOT / "rules").glob(f"rule-pattern-{n:02d}-*.md"))
    return hits[0] if hits else None


def norm(s):
    s = s.replace(LQUOTE, '"').replace(RQUOTE, '"')
    return re.sub(r"\s+", " ", s).strip()


def parse_rows(text):
    rows = {}
    for line in text.splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) < 5 or not cells[0].isdigit():
            continue
        no = int(cells[0])
        if 1 <= no <= PATTERN_COUNT:
            rows[no] = cells[1:5]
    return rows


def evidence_refusal(evidence, letter_norm):
    evidence = evidence.replace(LQUOTE, '"').replace(RQUOTE, '"')
    spans = re.findall(r'"([^"]+)"', evidence)
    if spans:
        cut = evidence.rfind(ARROW)
        tail = evidence[cut + 1:] if cut != -1 else evidence
        pool = re.findall(r'"([^"]+)"', tail) or spans
        if not any(norm(sp) in letter_norm for sp in pool):
            return ("the quoted evidence is not in the letter",
                    "quote a line that appears word for word in the letter, "
                    "or fix the letter so it does")
    elif not evidence.lower().startswith("confirm"):
        return ("the evidence is neither a quote nor a confirmation",
                "quote a line from the letter verbatim, or start the note "
                "with confirm:")
    if evidence.lower().startswith("confirm"):
        body = evidence.split(":", 1)[1].strip() if ":" in evidence else ""
        if len(body) < 20 or "todo" in body.lower():
            return ("the confirm note is too thin",
                    "write at least 20 characters after the first colon and "
                    "remove any TODO")
    return None


def level_refusal(kind, value, levels, rule, min_key, default):
    if value not in levels:
        return (f"{kind} '{value}' is not a valid level",
                "use one of: " + ", ".join(levels))
    if rule is None:
        return None
    need = str(parse_frontmatter(rule.read_text()).get(min_key, default))
    if need in levels and levels.index(value) < levels.index(need):
        return (f"{kind} '{value}' is below the rule minimum '{need}'",
                "do more of the work, or score honestly at "
                f"'{need}' or higher")
    return None


def trigger_refusal(coverage, rule, letter_text):
    if rule is None or coverage != "all":
        return None
    low = letter_text.lower()
    hits = [t for t in parse_frontmatter(rule.read_text()).get("triggers") or []
            if low.count(str(t).lower())]
    if not hits:
        return None
    found = ", ".join(f"'{t}' x{low.count(str(t).lower())}" for t in hits)
    return ("coverage all but these triggers remain in the letter: " + found,
            "rewrite every remaining trigger phrase, then rescore")


def run_checks(letter, audit):
    letter_text = letter.read_text()
    rows = parse_rows(audit.read_text())
    missing = [n for n in range(1, PATTERN_COUNT + 1) if n not in rows]
    if missing:
        die(f"audit table has {len(rows)} of the {PATTERN_COUNT} "
            f"expected rows",
            "rebuild the table with scripts/init.py and fill every row")
    open_rows = [n for n in range(1, PATTERN_COUNT + 1)
                 if not all(rows[n][i].strip() for i in (1, 2, 3))]
    passed, refusals = [], []
    for n in range(1, PATTERN_COUNT + 1):
        if n in open_rows:
            continue
        cells = rows[n]
        rule = rule_for(n)
        if rule is None:
            die(f"no rule file for pattern {n}",
                f"restore rules/rule-pattern-{n:02d}-*.md; the gate "
                "will not run without it")
        found = [r for r in (
            level_refusal("score", cells[1], QUALITY, rule, "minimum", "poor"),
            level_refusal("coverage", cells[2], COMPLETENESS, rule,
                          "coverage_minimum", "none"),
            trigger_refusal(cells[2], rule, letter_text)) if r]
        if not found:
            ev = evidence_refusal(cells[3], norm(letter_text))
            if ev:
                found = [ev]
        for msg, fix in found:
            refusals.append((n, msg, fix))
        if not found:
            passed.append((n, cells[1], cells[2]))
    return {"open": open_rows, "passed": passed, "refusals": refusals}


def emit_row(n, letter, audit, baseline):
    """One row emission, self-documenting; the rule file is the source."""
    rule = rule_for(n)
    if rule is None:
        die(f"no rule file for pattern {n}",
            f"restore rules/rule-pattern-{n:02d}-*.md; the loop "
            "will not run without it")
    fm = parse_frontmatter(rule.read_text())
    rows = parse_rows(audit.read_text())
    lines = [f"row {n}/{PATTERN_COUNT}: {rows[n][0]}",
             f"rule file: {rule}",
             "read that rule file now; it is this pattern's only text source.",
             f"rubric: {fm.get('rubric', 'quality')} "
             f"(scale: {', '.join(QUALITY)}), "
             f"minimum: {fm.get('minimum', 'poor')}",
             f"coverage: {fm.get('coverage', 'completeness')} "
             f"(scale: {', '.join(COMPLETENESS)}), "
             f"coverage_minimum: {fm.get('coverage_minimum', 'none')}"]
    lines.append("rubric definitions: "
                 f"{SKILL_ROOT / 'references/quality-rubric.md'} and "
                 f"{SKILL_ROOT / 'references/completeness-rubric.md'}; "
                 "read them when scoring a row.")
    triggers = fm.get("triggers") or []
    if triggers:
        lines.append("triggers: " + ", ".join(f'"{t}"' for t in triggers))
    lines.append("evidence contract: quote a line that appears word for "
                 "word in the letter, or confirm: what you checked and "
                 "found.")
    if baseline is not None:
        bpath, brows = baseline
        cells = brows[n]
        lines.append(f"baseline ({bpath}) claims for this row: "
                     f"score={cells[1]} coverage={cells[2]} evidence: "
                     f"{cells[3][:60]}")
        lines.append("re-derive this verdict fresh against the current "
                     "letter; never carry it over. A quote that still "
                     "appears is re-confirmed, not inherited. On "
                     'disagreement, add a note starting "delta:" naming '
                     "what changed.")
    lines.append("work ONLY this pattern: scan the letter for it, fix the "
                 "letter if it is violated, score the row, fill it in, "
                 "then run --next again.")
    return lines


def check_baseline(arg):
    """Validate --baseline: exists, 17 pattern rows, every row closed."""
    path = Path(arg).expanduser()
    if not path.is_file():
        die(f"baseline not found: {path}",
            "pass --baseline <path to the completed earlier audit>")
    rows = parse_rows(path.read_text())
    missing = [n for n in range(1, PATTERN_COUNT + 1) if n not in rows]
    if missing:
        die(f"baseline {path} has {len(rows)} of the {PATTERN_COUNT} "
            "expected rows",
            "point --baseline at a completed 17-row audit, or close every "
            "row in this file first")
    open_rows = [n for n in range(1, PATTERN_COUNT + 1)
                 if not all(rows[n][i].strip() for i in (1, 2, 3))]
    if open_rows:
        die(f"baseline row {open_rows[0]} is open",
            "a baseline must be a completed audit; fill score, coverage "
            "and evidence in every row first")
    return rows


def next_lines(letter, audit, baseline_arg=None):
    """The lines --next prints: one open row, or the all-closed handoff."""
    baseline = None
    if baseline_arg:
        baseline = (baseline_arg, check_baseline(baseline_arg))
    res = run_checks(letter, audit)
    if res["open"]:
        return emit_row(res["open"][0], letter, audit, baseline)
    return ["all rows closed; run --gate"]


def run_next(letter, audit, baseline_arg):
    for line in next_lines(letter, audit, baseline_arg):
        print(line)
    sys.exit(0)


def resolve(letter_arg, audit_arg):
    if not letter_arg:
        die("no letter given", "pass --letter <path to the draft>")
    letter = Path(letter_arg).expanduser()
    if not letter.is_file():
        die(f"letter not found: {letter}",
            "pass --letter <path to the draft being audited>")
    audit = (Path(audit_arg).expanduser() if audit_arg
             else letter.parent / "patterns-audit.md")
    if not audit.is_file():
        die(f"audit file not found: {audit}",
            "run scripts/init.py first, or pass --audit <path>")
    lines = audit.read_text().splitlines()
    m = re.match(r"^#\s*Pattern audit\s+[^\w\s]*\s*(\S.*)$",
                 lines[0] if lines else "")
    if not m or Path(m.group(1).strip()).expanduser().resolve() != letter.resolve():
        die(f"audit header does not name this letter: {audit}",
            "pass --letter with the path named in the audit header, or "
            "rebuild the audit with scripts/init.py")
    return letter, audit


def selftest():
    def audit(letter, row1):
        head = f"# Pattern audit {AUDIT_DASH} {letter}\n"
        head += "| No | Pattern | Score | Coverage | Evidence |\n"
        head += "|----|---------|-------|----------|----------|\n"
        rest = "\n".join(f"| {n} | p{n} | acceptable | all | confirm: swept every paragraph and found nothing to fix. |"
                         for n in range(2, PATTERN_COUNT + 1))
        return head + row1 + "\n" + rest + "\n"

    with tempfile.TemporaryDirectory() as tmp:
        d = Path(tmp)
        base = "I helped test the suite and shipped the fix on time.\n"

        def case(name, body, row1):
            lp, ap = d / (name + ".txt"), d / (name + "-audit.md")
            lp.write_text(body)
            ap.write_text(audit(lp, row1))
            return run_checks(lp, ap)

        row_ok = ('| 1 | Grand claims | acceptable | all | Did the sweep: '
                  '"I helped test the suite and shipped the fix on time." |')
        res = case("good", base, row_ok)
        assert not res["open"] and not res["refusals"], "pass path broke"
        bad = ('| 1 | Grand claims | acceptable | all | '
               '"I rewrote every claim by hand." |')
        assert case("badquote", base, bad)["refusals"], "bad quote passed"
        thin = '| 1 | Grand claims | good | all | swept it all away. |'
        assert case("thin", base, thin)["refusals"], \
            "content-free evidence passed"
        curly = ('| 1 | Grand claims | good | all | Did the sweep: '
                 '\u201cI helped test the suite and shipped the fix on '
                 'time.\u201d |')
        assert not case("curly", base, curly)["refusals"], \
            "curly quotes broke the span match"
        low = '| 1 | Grand claims | poor | all | "I helped test the suite." |'
        assert case("lowscore", base, low)["refusals"], "low score passed"
        res = case("trigger", "I was pivotal in the launch.\n",
                   '| 1 | Grand claims | acceptable | all | '
                   '"I was pivotal in the launch." |')
        assert any("trigger" in r[1] for r in res["refusals"]), "trigger missed"
        res = case("openrow", base, "| 1 | Grand claims | | | |")
        assert res["open"] == [1], "open row missed"

        # --next cases: the emission is self-documenting, one open row each
        def table(letter, open_row):
            head = f"# Pattern audit {AUDIT_DASH} {letter}\n"
            head += "| No | Pattern | Score | Coverage | Evidence |\n"
            head += "|----|---------|-------|----------|----------|\n"
            body = []
            for i in range(1, PATTERN_COUNT + 1):
                if i == open_row:
                    body.append(f"| {i} | p{i} | | | |")
                else:
                    body.append(f"| {i} | p{i} | acceptable | all | "
                                "confirm: swept every paragraph, "
                                f"row {i} clean. |")
            return head + "\n".join(body) + "\n"

        def exits2(fn):
            try:
                with contextlib.redirect_stderr(io.StringIO()):
                    fn()
            except SystemExit as e:
                return e.code == 2
            return False

        lpn = d / "next.txt"
        lpn.write_text(base)
        apn = d / "next-audit.md"
        apn.write_text(table(lpn, 3))
        lines = next_lines(lpn, apn)
        assert lines[0] == f"row 3/{PATTERN_COUNT}: p3", lines[0]
        blob = "\n".join(lines)
        assert "rule-pattern-03" in blob, "rule file missing from --next"
        assert "evidence contract" in blob and "rubric definitions" in blob \
            and "--next again." in blob
        apdone = d / "done-audit.md"
        apdone.write_text(table(lpn, None))
        assert next_lines(lpn, apdone) == ["all rows closed; run --gate"]
        base_b = d / "baseline-done.md"
        base_b.write_text(table(lpn, None))
        blob = "\n".join(next_lines(lpn, apn, base_b))
        assert "baseline (" in blob and "delta:" in blob, blob
        short = d / "baseline-16.md"
        short.write_text(table(lpn, None).replace(
            "| 17 | p17 | acceptable | all | confirm: swept every "
            "paragraph, row 17 clean. |\n",
            "| 16b | extra | | | |\n"))
        assert exits2(lambda: next_lines(lpn, apdone, short)), \
            "16-row baseline passed"
        opn = d / "baseline-open.md"
        opn.write_text(table(lpn, 4))
        assert exits2(lambda: next_lines(lpn, apdone, opn)), \
            "open-row baseline passed"
    print("selftest: PASS")
    sys.exit(0)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--letter", help="path to the letter being audited")
    p.add_argument("--audit", help="audit file to check (default: "
                   "patterns-audit.md next to the letter)")
    p.add_argument("--selftest", action="store_true",
                   help="run the built-in selftest and exit")
    p.add_argument("--next", action="store_true",
                   help="present the next open pattern row")
    p.add_argument("--gate", action="store_true",
                   help="run the finish gate (default without a mode flag)")
    p.add_argument("--baseline",
                   help="completed earlier audit to re-derive against "
                   "(use with --next)")
    a = p.parse_args()
    if a.selftest:
        selftest()
    if a.next and a.gate:
        die("--next and --gate are exclusive", "pass one mode flag")
    letter, audit = resolve(a.letter, a.audit)
    if a.next:
        run_next(letter, audit, a.baseline)
    res = run_checks(letter, audit)
    for n, score, coverage in res["passed"]:
        print(f"pattern {n}: PASS score={score} coverage={coverage}")
    for n, msg, fix in res["refusals"]:
        print(f"check: pattern {n}: {msg}", file=sys.stderr)
        print(f"fix: {fix}", file=sys.stderr)
    open_count = len(res["open"])
    print(f"{PATTERN_COUNT - open_count}/{PATTERN_COUNT} rows closed; "
          f"{open_count} open")
    if open_count or res["refusals"]:
        sys.exit(2)


if __name__ == "__main__":
    main()
