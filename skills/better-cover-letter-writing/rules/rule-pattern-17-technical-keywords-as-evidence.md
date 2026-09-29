---
id: pattern_17_technical_keywords_as_evidence
inventory: 17
type: fix
evidence: [quote, confirm]
applies_to: [letter]
rubric: quality
minimum: acceptable
coverage: completeness
coverage_minimum: all
expect: "technical terms that match the role are retained, but important terms are tied to concrete implementation or outcomes rather than presented as a keyword list"
on_fail:
  action: "rewrite per the rule, rescore, re-sweep"
provenance:
  date: 2026-09-28
  app: better-cover-letter-writing
  source: "SKILL.md pattern 17, packaged verbatim for JIT"
status: active
---

# Pattern 17: Technical keywords must be backed by evidence

Read this rule, fix the letter, score the applied level, record evidence. One rule at a time.

## Rule

Keep technical terms that directly match the role. Do not remove useful terminology just because it sounds technical or appears in the job description.
The problem is **keyword cataloguing without evidence**. Technical terms should describe something you actually built, designed, used, or changed.

Before:
> "The design used agentic patterns, planning, tool use, self-reflection and specialised agents..."

After:
> "The workflow uses deterministic steps for the repeatable parts, then an LLM analyses the failures. I used planning, tool calls, self-reflection and specialised agents where they added value, with rubrics checking the smaller model's output."

Now the terminology is doing useful work rather than sounding like a keyword list.

Use concrete details around the terminology, for example:

- what the system reads or receives
- what it does
- what it produces
- where the result goes
- who uses it
- what changed as a result

The goal is not to hide job-description keywords. The goal is to make the keywords **evidence of experience rather than substitutes for evidence**.

## Rubric

Quality: references/quality-rubric.md, minimum acceptable.
Coverage: references/completeness-rubric.md, minimum all.

## Coverage

Sweep technical sections and examples. For each important keyword, check whether the surrounding text shows how it was used in real work. Keep keywords that strengthen role alignment. Rewrite or remove terminology that adds no information.

## Ask

- Does the surrounding sentence show what I actually did with it?
- Could I replace the term with a concrete action without losing useful job-description alignment?

## Do not

- Do not remove technical keywords solely because they match the job description.
- Do not turn every paragraph into a list of AI or engineering concepts.
- Do not use technical terminology where concrete evidence would communicate more.
