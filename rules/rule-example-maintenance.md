---
id: rule_example_maintenance
inventory: 2
type: protocol
evidence: confirm
applies_to: [step_retro]
expect: "when a rule batch activates, the examples that teach the affected rules are checked and updated in the same batch"
on_fail:
  action: "update the affected examples before the batch lands"
provenance:
  date: 2026-09-24
  app: skill_review_project
  source: "chunk (iii) built the teaching pairs and failure gallery; the rules they teach must not drift from them"
  detail: verified
status: active
last_validated: 2026-09-24
related: [rule_corrections_propagate]
---

## Learned from
The teaching layer — before/after pairs, the failure gallery, the gold
examples — was built to encode the rules as they stand. When a rule
changes (activation, rewording, retirement), the examples that
demonstrate it silently go stale and start teaching the wrong thing.
The corrections rule already demands propagation across a run's
artifacts; the same principle applies to the skill's own teaching
material.

## Rule
When a retro batch changes a rule, list every gold example and teaching
pair that demonstrates that rule, and check each one in the same batch.
Update the annotation, the diagnosis or the pair so it still teaches
the rule as it now stands, or confirm in writing that it is still
correct. Present what changed together with the batch.

## Rubric
- [ ] Affected examples listed when the rule batch is presented
- [ ] Each affected example updated or explicitly confirmed still correct
- [ ] Example changes presented with the batch for approval