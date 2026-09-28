#!/usr/bin/env python3
"""Finish gate for the pattern audit of one cover letter.

Usage: python3 scripts/check_patterns.py --letter <path> [--audit <path>]
       python3 scripts/check_patterns.py --selftest

Empty score, coverage, or evidence means the row is open. Exit 0 only when
all 16 rows are closed and no refusal was raised.
"""
import argparse
import re
import sys
import tempfile
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
QUALITY = ["poor", "acceptable", "good", "excellent"]
COMPLETENESS = ["none", "partial", "most", "all"]
ARROW = chr(0x2192)
AUDIT_DASH = chr(0x2014)

try:
    import yaml
except ImportError:
    yaml = None


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
    if yaml is not None:
        try:
            data = yaml.safe_load("\n".join(lines[1:end]))
            return data if isinstance(data, dict) else {}
        except Exception:
            pass
    out = {}
    for line in lines[1:end]:
        if line.startswith((" ", "#")) or ":" not in line:
            continue
        key, _, val = line.partition(":")
        val = val.strip()
        if val.startswith("[") and val.endswith("]"):
            out[key.strip()] = [s.strip().strip("\"'")
                                for s in val[1:-1].split(",") if s.strip()]
        else:
            out[key.strip()] = val.strip("\"'")
    return out


def rule_for(n):
    hits = sorted((SKILL_ROOT / "rules").glob(f"rule-pattern-{n:02d}-*.md"))
    return hits[0] if hits else None


def norm(s):
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
        if 1 <= no <= 16:
            rows[no] = cells[1:5]
    return rows


def evidence_refusal(evidence, letter_norm):
    spans = re.findall(r'"([^"]+)"', evidence)
    if spans:
        cut = evidence.rfind(ARROW)
        tail = evidence[cut + 1:] if cut != -1 else evidence
        pool = re.findall(r'"([^"]+)"', tail) or spans
        if not any(norm(sp) in letter_norm for sp in pool):
            return ("the quoted evidence is not in the letter",
                    "quote a line that appears word for word in the letter, "
                    "or fix the letter so it does")
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
    missing = [n for n in range(1, 17) if n not in rows]
    if missing:
        die(f"audit table has {len(rows)} of the 16 expected rows",
            "rebuild the table with scripts/init.py and fill every row")
    open_rows = [n for n in range(1, 17)
                 if not all(rows[n][i].strip() for i in (1, 2, 3))]
    passed, refusals, struct_only = [], [], []
    for n in range(1, 17):
        if n in open_rows:
            continue
        cells = rows[n]
        rule = rule_for(n)
        if rule is None:
            struct_only.append(n)
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
    return {"open": open_rows, "passed": passed, "refusals": refusals,
            "struct_only": struct_only}


def selftest():
    def audit(letter, row1):
        head = f"# Pattern audit {AUDIT_DASH} {letter}\n"
        head += "| No | Pattern | Score | Coverage | Evidence |\n"
        head += "|----|---------|-------|----------|----------|\n"
        rest = "\n".join(f"| {n} | p{n} | acceptable | all | swept every paragraph. |"
                         for n in range(2, 17))
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
        low = '| 1 | Grand claims | poor | all | "I helped test the suite." |'
        assert case("lowscore", base, low)["refusals"], "low score passed"
        res = case("trigger", "I was pivotal in the launch.\n",
                   '| 1 | Grand claims | acceptable | all | '
                   '"I was pivotal in the launch." |')
        assert any("trigger" in r[1] for r in res["refusals"]), "trigger missed"
        res = case("openrow", base, "| 1 | Grand claims | | | |")
        assert res["open"] == [1], "open row missed"
    print("selftest: PASS")
    sys.exit(0)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--letter", help="path to the letter being audited")
    p.add_argument("--audit", help="audit file to check (default: "
                   "patterns-audit.md next to the letter)")
    p.add_argument("--selftest", action="store_true",
                   help="run the built-in selftest and exit")
    a = p.parse_args()
    if a.selftest:
        selftest()
    if not a.letter:
        die("no letter given", "pass --letter <path to the draft>")
    letter = Path(a.letter).expanduser()
    if not letter.is_file():
        die(f"letter not found: {letter}",
            "pass --letter <path to the draft being audited>")
    audit = (Path(a.audit).expanduser() if a.audit
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
    res = run_checks(letter, audit)
    for n in res["struct_only"]:
        print(f"pattern {n}: no rule file yet, structural checks only")
    for n, score, coverage in res["passed"]:
        print(f"pattern {n}: PASS score={score} coverage={coverage}")
    for n, msg, fix in res["refusals"]:
        print(f"check: pattern {n}: {msg}", file=sys.stderr)
        print(f"fix: {fix}", file=sys.stderr)
    open_count = len(res["open"])
    print(f"{16 - open_count}/16 rows closed; {open_count} open")
    if open_count or res["refusals"]:
        sys.exit(2)


if __name__ == "__main__":
    main()