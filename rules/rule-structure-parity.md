---
id: rule_structure_parity
inventory: 1
type: check
evidence: quote
applies_to: [step_1, step_2, step_3]
expect: "every canonical section from the step template and the example file is present in the delivered artifact"
on_fail:
  action: "add the missing sections, re-run the parity diff before delivery"
provenance:
  date: 2026-09-08
  app: 07_reo_group
  source: "user deviation report"
  detail: verified
status: active
last_validated: 2026-09-17
---

## Learned from
User report after the 07 matches delivery: "you deviated from the
workflow and guidance several times." The self-audit found a missing
Keywords Tools section, no soft-skills mapping, no gaps List 3, and
an employer-questions cop-out (question 7). None of it was visible
until user review.

## Rule
Before delivering matches.md, diff its structure against the step
template (assets/matches-template.md) and the example file
(examples/matches-gold.md). Before delivering a letter draft, diff
its sections against the key-questions mapping in matches.md.
Missing sections are fixed before the checkpoint, not after the
user finds them.

## Rubric
- [ ] Section set matches the example file and the step template, or the deviation is named and justified
- [ ] Every structural keyword has a home: skills and tools, soft skills, role type and context
- [ ] List 1, List 2, and the gaps List 3 all present, within their caps
- [ ] Employer questions are real anticipated questions with answers