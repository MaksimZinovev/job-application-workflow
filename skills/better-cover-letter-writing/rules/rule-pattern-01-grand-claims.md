---
id: pattern_01_grand_claims
inventory: 1
type: fix
evidence: [quote, confirm]
applies_to: [letter]
rubric: quality
minimum: acceptable
coverage: completeness
coverage_minimum: all
triggers: ["key role", "instrumental in", "pivotal", "crucial role", "driving force"]
expect: "no importance declaration stands without the observable action behind it"
on_fail:
  action: "rewrite with the strongest verb the evidence supports, rescore, re-sweep"
provenance:
  date: 2026-09-28
  app: better-cover-letter-writing
  source: "SKILL.md pattern 1, packaged verbatim for JIT"
status: active
---

# Pattern 1: Grand claims → observable actions

Read this rule, fix the letter, score the applied level, record
evidence. One rule at a time.

## Rule

"Played a key role" declares importance without explaining what
happened. Replace every importance declaration with the observable
action behind it.

## Before → After

Before:
"Played a key role in the team's shift from manual to automated testing."

After:
"Helped move the team from manual to automated testing."

## Prefer

- "helped..."
- "built..."
- "introduced..."
- "worked on..."
- "moved..."
- "added..."
- "set up..."
- "supported..."

Choose the strongest verb supported by the evidence.

## Rubric

Quality: references/quality-rubric.md, minimum acceptable.
Coverage: references/completeness-rubric.md, minimum all.

## Coverage

The checker recounts these phrases in the letter:
"key role", "instrumental in", "pivotal", "crucial role",
"driving force". Coverage all requires zero remaining.

## Ask

- What did this person actually do?
- Which verb does the evidence support, no stronger?

## Do not

- Do not swap one grand phrase for another. "Instrumental in" is the
  same claim.
- Do not invent an action the records do not show.
