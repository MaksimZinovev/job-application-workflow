#!/usr/bin/env python3
"""Stub a grounded pattern-audit table for one letter.

Usage: python3 scripts/init.py --letter <path> [--out <path>]

Creates a table with every pattern from this skill, Score, Coverage,
and Evidence empty. For each pattern, read its rule one at a time,
fix the letter, score quality and coverage against the two rubrics
in references/, and record evidence in the row. Then run
scripts/check_patterns.py and make it exit 0.
"""
import argparse
import sys
from datetime import date
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = SKILL_ROOT / "assets" / "patterns.md"


def die(msg: str, fix: str):
    print(f"init: {msg}", file=sys.stderr)
    print(f"fix: {fix}", file=sys.stderr)
    sys.exit(2)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--letter", required=True,
                   help="path to the letter being audited")
    p.add_argument("--out",
                   help="audit file to create (default: patterns-audit.md next to the letter)")
    a = p.parse_args()

    letter = Path(a.letter).expanduser()
    if not letter.is_file():
        die(f"letter not found: {letter}",
            "pass --letter <path to the draft being audited>")
    out = Path(a.out).expanduser() if a.out else letter.parent / "patterns-audit.md"
    if not TEMPLATE.is_file():
        die(f"template missing: {TEMPLATE}",
            "assets/patterns.md ships with this skill; restore it")
    if out.exists():
        die(f"audit file already exists: {out}",
            "fill the existing table, or pass --out <new path>")

    text = (TEMPLATE.read_text()
            .replace("{{LETTER}}", str(letter))
            .replace("{{DATE}}", date.today().isoformat()))
    out.write_text(text)
    print(f"stubbed: {out}")
    print("next: for each pattern, read its rule, fix the letter, score "
          "quality and coverage against the rubrics in references/, record "
          "evidence in each row, then run scripts/check_patterns.py until "
          "it exits 0.")


if __name__ == "__main__":
    main()