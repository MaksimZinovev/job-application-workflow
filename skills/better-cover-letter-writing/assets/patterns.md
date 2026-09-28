# Pattern audit — {{LETTER}}

Date: {{DATE}}. Skill: better-cover-letter-writing. One row per pattern.
Before filling a row, read the rule for that pattern (rules/rule-pattern-01-grand-claims.md
is pattern 1; the other rules are packaged one at a time), fix the letter,
score quality against references/quality-rubric.md and coverage against
references/completeness-rubric.md, and use the minimums stated in the rule.
Evidence is a verbatim quote from the letter or a concise written
confirmation of what was checked or resolved. Empty Score, Coverage, or
Evidence means the pass is not done.

| No | Pattern | Score | Coverage | Evidence (verbatim quote or written confirmation) |
|----|---------|-------|----------|---------------------------------------------------|
| 1 | Grand claims → observable actions | | | |
| 2 | Colon + three-item list → natural sentence | | | |
| 3 | Abstract praise → concrete explanation | | | |
| 4 | Impressive verb → accurate verb | | | |
| 5 | Sweeping claim → specific example | | | |
| 6 | Absolute statement → accurate qualification | | | |
| 7 | Importance statement → outcome | | | |
| 8 | Self-description → evidence | | | |
| 9 | Marketing language → plain description | | | |
| 10 | AI-style symmetry → natural rhythm | | | |
| 11 | Marketing echo → cut | | | |
| 12 | Template completeness → empty slot | | | |
| 13 | Performative self-qualification → plain fact | | | |
| 14 | Homework name-dropping → detail that does work | | | |
| 15 | Editorial subheading → plain functional label | | | |
| 16 | Intro paragraph (exec summary) | | | |

Final self-check (fill after all rows close): meaning preserved, nothing
invented, ownership not exaggerated, ordinary language, credible rather
than promotional. Pass verdict:

When every row is filled, run `python3 scripts/check_patterns.py --letter <path>`. It must exit 0 before you claim the audit done.
