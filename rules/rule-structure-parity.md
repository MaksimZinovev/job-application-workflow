---
id: rule_structure_parity
inventory: 1
type: check
applies_to: [step_1, step_2, step_3]
expect: "every canonical section from the example file and the workflow item list is present in the delivered artifact"
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
Keywords Tools section (workflow 1.4), no soft-skills mapping (1.5), no
gaps List 3 (1.7), and an employer-questions cop-out (1.8, question
7). None of it was visible until user review.

## Rule
Before delivering matches.md, diff its structure against the example
file (notes/2026-applications/examples/matches.md) and the workflow
item list. Before delivering a letter draft, diff its sections against
the question-to-section mapping. Missing sections are fixed before
the checkpoint, not after the user finds them.

## Rubric
- [ ] Section set matches the example file and the workflow items, or the deviation is named and justified
- [ ] Every structural keyword has a home: skills and tools, soft skills, role type and context
- [ ] List 1, List 2, and the gaps List 3 all present, within their caps
- [ ] Employer questions are real anticipated questions with answers