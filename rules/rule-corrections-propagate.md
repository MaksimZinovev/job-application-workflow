---
id: rule_corrections_propagate
inventory: 7
type: protocol
applies_to: [step_1, step_2, step_3]
on_fail:
  action: "sweep every run artifact for the stale value, update all, flag the source record"
provenance:
  date: 2026-09-08
  app: 07_reo_group
  source: "annotation (6 to 8 sessions)"
  detail: verified
status: active
last_validated: 2026-09-17
related: [rule_user_memory_outranks_records]
---

## Learned from
A stale count (6 sessions, true value 8) lived in experience-pieces.json
and had already flowed into matches.md and the letter. Fixing only the
annotated file would have left the stale number free to resurface in
the next artifact built from the same source.

## Rule
When a fact is corrected, propagate the fix to every artifact in the
current run that carries it, and flag the source record for
correction at origin. A correction applied in one place is not a
correction.

## Rubric
- [ ] All run artifacts carrying the fact updated, not just the flagged one
- [ ] Source record flagged with a proposed correction
- [ ] Run folder swept for the stale value before the checkpoint closes