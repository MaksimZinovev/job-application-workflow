---
id: rule_richness_for_cuts
inventory: 18
type: judgment
applies_to: [step_1, step_2, step_3]
on_fail:
  action: "justify the keep with a keyword hole or role-shape argument, or cut"
provenance:
  date: 2026-09-08
  app: 07_reo_group
  source: "user feedback during matches drafting"
  detail: reconstructed
status: active
last_validated: 2026-09-17
---

## Learned from
Cutting evidence during matches drafting: the user's bar was not
volume but difference. Evidence stays only when it closes a keyword
hole the JD actually asks for, or supports the shape of the role.
Richness for its own sake is noise. The workflow enforces the same
bar with its caps: 5-7 items per list, 3-5 gaps, 10K characters.

## Rule
When trimming, score each piece of evidence by whether it closes a
keyword hole or supports the role shape. Keep on yes; cut on no.
Name the cuts at the checkpoint so the user can veto.

## Rubric
- [ ] Every borderline keep justified by keyword hole or role shape
- [ ] Cuts listed at the checkpoint for veto
- [ ] No evidence kept purely for volume