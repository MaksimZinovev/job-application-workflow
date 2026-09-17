---
id: rule_read_sources_first
inventory: 10
type: protocol
applies_to: [step_0]
on_fail:
  action: "stop drafting, read the unread source, restart the step"
provenance:
  date: 2026-09-08
  app: 07_reo_group
  source: "deviation report self-audit"
  detail: reconstructed
status: active
last_validated: 2026-09-17
---

## Learned from
The deviation self-audit found drafting had started before all step 0
sources were read. The workflow lists the sources with their
downstream functions: the master CV feeds facts, tense, and the
List 2 records; the STAR stories doc feeds the hidden-question
paragraphs; experience-pieces.json feeds the List 1 records; the
ai-adoption essay feeds the AI positioning; the job-search files
feed context and strategy.

## Rule
Read every step 0 source before writing anything, and treat them as
the source of truth rather than facts remembered from previous
applications. Each source must have its downstream function named.
If you cannot say what a source feeds, you have not read it.

## Rubric
- [ ] All step 0 sources read before step 1 begins
- [ ] Downstream function named for each source
- [ ] No facts inherited from previous application runs