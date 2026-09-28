---
id: pattern_05_sweeping_claim
inventory: 5
type: fix
evidence: [quote, confirm]
applies_to: [letter]
rubric: quality
minimum: acceptable
coverage: completeness
coverage_minimum: all
triggers: ["exactly", "comprehensively"]
expect: "claims about what something does come with the specific example instead"
on_fail:
  action: "rewrite per the rule, rescore, re-sweep"
provenance:
  date: 2026-09-28
  app: better-cover-letter-writing
  source: "SKILL.md pattern 5, packaged verbatim for JIT"
status: active
---

# Pattern 5: Sweeping claim → specific example

Read this rule, fix the letter, score the applied level, record
evidence. One rule at a time.

## Rule

Specific examples are usually more convincing than claims about what
a tool does "exactly" or "comprehensively."

## Before → After

Before:
"Docfence catches the exact defects AI assistants leave behind."

After:
"Docfence finds defects that AI assistants often leave behind, including TODOs, broken links, and missing sections."

## Rubric

Quality: references/quality-rubric.md, minimum acceptable.
Coverage: references/completeness-rubric.md, minimum all.

## Coverage triggers

The checker recounts these phrases in the letter:
"exactly", "comprehensively". Coverage all requires zero remaining.

Sweep for claims about what a tool or person does exactly,
comprehensively, or always. Replace each with the specific example.

## Ask

- What is one real case that shows this?

## Do not

- Do not claim exactness the evidence does not show.