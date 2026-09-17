---
id: rule_ownership_calibration
inventory: 5
type: judgment
applies_to: [step_3, step_4]
on_fail:
  action: "downgrade the verb to what the org-context records support"
provenance:
  date: 2026-09-08
  app: 07_reo_group
  source: "annotation round"
  detail: reconstructed
status: active
last_validated: 2026-09-17
---

## Learned from
A draft claimed ownership of work that the org-context records show
was owned by a Lead the user reported to. The annotation round
downgraded the claim. The better-cover-letter-writing pass encodes
the same bar: use led or owned only when evidenced.

## Rule
Ownership verbs (own, lead, responsible for) must match the
org-context records. Where the records show reporting into a Lead,
say designed, developed, maintained, extended. Calibrated verbs beat
impact verbs, because the interviewer will probe exactly there.

## Rubric
- [ ] Every own/led/responsible claim checked against org-context records
- [ ] Unearned ownership verbs rewritten to calibrated ones
- [ ] Ambiguous records surfaced at the checkpoint instead of guessed