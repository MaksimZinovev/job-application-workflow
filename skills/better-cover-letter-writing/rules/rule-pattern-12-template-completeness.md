---
id: pattern_12_template_completeness
inventory: 12
type: fix
evidence: [quote, confirm]
applies_to: [letter]
rubric: quality
minimum: acceptable
coverage: completeness
coverage_minimum: all
triggers: ["[company]", "[insert", "[todo", "todo:", "tbd"]
expect: "no template slot is filled with filler; an honest empty slot is information"
on_fail:
  action: "rewrite per the rule, rescore, re-sweep"
provenance:
  date: 2026-09-28
  app: better-cover-letter-writing
  source: "SKILL.md pattern 12, packaged verbatim for JIT"
status: active
---

# Pattern 12: Template completeness → empty slot

Read this rule, fix the letter, score the applied level, record evidence. One rule at a time.

## Rule

Filling every planned section even when the honest answer is "nothing real to say here". An empty slot is information.

## Before → After

Before:
"Why this company: I am passionate about your products and confident
I can make a significant impact."

After:
Drop the section, or write the one real reason if there is one.

The before fills a slot with a sentence that commits to nothing. The
empty slot tells the reader more.

## Rubric

Quality: references/quality-rubric.md, minimum acceptable.
Coverage: references/completeness-rubric.md, minimum all.

## Coverage

Sweep every planned section of the letter. A section filled with nothing real is the violation: an empty slot is information.

The checker recounts these phrases in the letter:
"[company]", "[insert", "[todo", "todo:", "tbd". Coverage all requires zero
remaining. The "[insert" and "[todo" triggers are unclosed openers on
purpose: a filled placeholder always starts with them. "todo:" catches
the inline TODO marker; the bare word todo alone, describing a tool
(as in a linter finding TODOs), is not a placeholder.

## Ask

- Does this section say something real, or is it filled because the template has a slot?

## Do not

- Do not fill a section to avoid an empty slot.
