---
id: rule_checkpoint_interview_tool
inventory: 16
type: protocol
applies_to: [all]
on_fail:
  action: "re-present the decision as structured options with a recommendation"
provenance:
  date: 2026-09-09
  app: all_runs
  source: "user directive in prompts/new-job-appl.md and the workflow working-style section"
  detail: verified
status: active
last_validated: 2026-09-17
---

## Learned from
Stated twice by the user, on disk: the base prompt
(prompts/new-job-appl.md) and the workflow's working-style section
both direct that at decision points the question or interview tool
is used, with alternatives and a recommendation.

## Rule
Decision checkpoints go through the structured question tool:
options enumerated as choices, each alternative labeled, one
recommendation with its reasoning, a free-text path always open.
Applies to every gate: the 1.3 promote decision, per-step
checkpoints, and any mid-run fork. Never bury a decision in prose
and hope the user notices the question mark.

## Rubric
- [ ] Decision presented as structured options, not prose
- [ ] Recommendation explicit, with reasoning
- [ ] Free-text alternative available