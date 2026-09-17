---
id: rule_copy_at_end
inventory: 3
type: protocol
applies_to: [step_0, step_1, step_2, step_6]
on_fail:
  action: "re-copy from the current source and diff to confirm parity"
provenance:
  date: 2026-09-08
  app: 07_reo_group
  source: "stale copy after a decision line landed post-copy"
  detail: reconstructed
status: active
last_validated: 2026-09-17
---

## Learned from
A file copied during the 07 run went stale: the source gained a
decision line after the copy was made, and the delivered copy no
longer matched. The mismatch surfaced late, after the copy had been
treated as current.

## Rule
Make file copies as the last action of the step that needs them
(job description into the run folder at step 0, master resume at
step 5). If a source mutates after the copy, re-copy or re-verify
before the copy is used or delivered. A copy is a point in time, not
a live reference.

## Rubric
- [ ] Copies happen at the end of the step, after content decisions
- [ ] Post-copy source changes trigger a re-copy or a diff check
- [ ] Delivered copies diffed against the current source