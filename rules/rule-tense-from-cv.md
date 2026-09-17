---
id: rule_tense_from_cv
inventory: 4
type: check
applies_to: [step_3]
expect: "tense of every employer mention matches the CV's employment status"
on_fail:
  action: "fix tense against the CV, sweep all artifacts for the same employer"
provenance:
  date: 2026-09-08
  app: 07_reo_group
  source: "annotation round"
  detail: reconstructed
status: active
last_validated: 2026-09-17
---

## Learned from
A letter described a departed employer in the present tense. The
phrasing was inherited from a precedent letter rather than checked
against the CV, which the workflow names as the source of truth for
facts, alongside its warning not to rely on facts from previous
applications.

## Rule
Employment tense comes from the CV, never from precedent letters or
memory. Current employer reads in the present tense, departed
employers in the past tense. Check every employer mention against
the CV before delivery.

## Rubric
- [ ] Every employer mention checked against the CV's employment status
- [ ] No tense inherited from another letter's phrasing
- [ ] Tense fixes propagate to every artifact in the run