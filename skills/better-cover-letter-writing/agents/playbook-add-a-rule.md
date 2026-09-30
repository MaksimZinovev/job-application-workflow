# Playbook: add a new rule

A rule is one writing pattern: how it reads, why it hurts, how to
fix it. The gate proves the fix. Copy pattern 17's shape.

## The moving parts

- `rules/rule-pattern-NN-slug.md` — the rule: teaching plus a
  machine contract in frontmatter.
- `assets/patterns.md` — the audit table stubbed next to each
  letter; row NN holds the canonical name.
- `SKILL.md` — the Patterns table, the index read first.
- `scripts/check_patterns.py` — the gate; `PATTERN_COUNT` is the
  only number you edit in it.
- `references/` — the two rubrics; rules point at them.

## Steps

1. Copy a rule file to `rules/rule-pattern-NN-slug.md`. Keep
   the frontmatter shape: `inventory`, `rubric: quality`,
   `minimum: acceptable`, `coverage: completeness`,
   `coverage_minimum: all`, `evidence: [quote, confirm]`, one-line
   `expect`.
2. Fill the body: `## Rule` (one positive principle),
   `## Before → After` (a real bad and good pair), `## Rubric`,
   `## Coverage`, `## Ask`, `## Do not`.
3. Add the row to `assets/patterns.md`: `| NN | name | | | |`.
   The name is two short phrases joined by an arrow.
4. Copy that name and path into SKILL.md's table, byte for byte;
   the index must not drift from the stub.
5. In `scripts/check_patterns.py` set `PATTERN_COUNT` to NN. That
   is the whole script change.
6. Verify: the selftest prints PASS and `ruff check` comes back
   clean. Run one real letter: honest rows, exit 0; one trigger
   phrase left in, exit 2.
7. Commit rule, stub row, SKILL.md row, and constant together.
   Half-wired rules fail the gate for everyone.

## Rules of thumb

- `triggers` are literal strings, matched case-insensitively. Add
  them only when the phrase cannot honestly stay in a finished
  letter; semantic patterns get none.
- No em dashes. End every file with a newline; the wiki linter
  rewrites files without one and forces re-reads.
- "no rule file for pattern NN"? The commit is missing. The gate is
  right; restore the file.
