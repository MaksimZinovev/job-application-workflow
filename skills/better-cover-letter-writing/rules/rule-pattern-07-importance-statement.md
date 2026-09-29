---
id: pattern_07_importance_statement
inventory: 7
type: fix
evidence: [quote, confirm]
applies_to: [letter]
rubric: quality
minimum: acceptable
coverage: completeness
coverage_minimum: all
triggers: ["important", "crucial", "valuable"]
expect: "no sentence tells the reader something was important without saying what changed"
on_fail:
  action: "rewrite per the rule, rescore, re-sweep"
provenance:
  date: 2026-09-28
  app: better-cover-letter-writing
  source: "SKILL.md pattern 7, packaged verbatim for JIT"
status: active
---

# Pattern 7: Importance statement → outcome

Read this rule, fix the letter, score the applied level, record
evidence. One rule at a time.

## Rule

Replace every importance declaration with the outcome it produced.
Say what changed, not that it mattered.

## Before → After

Before:
"This was a pivotal improvement to our testing process."

After:
"This reduced the amount of manual regression testing we had to
repeat."

## Rubric

Quality: references/quality-rubric.md, minimum acceptable.
Coverage: references/completeness-rubric.md, minimum all.

## Coverage

Sweep for sentences that declare importance (important, crucial,
valuable, pivotal). Each must be replaced by the outcome it produced.

The checker recounts these phrases in the letter:
"important", "crucial", "valuable". Coverage all requires zero
remaining.

## Ask

- What changed because of this?

## Do not

- Do not tell the reader that something was important. Explain what
  changed.
