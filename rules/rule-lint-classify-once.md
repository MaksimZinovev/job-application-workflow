---
id: rule_lint_classify_once
inventory: 17
type: check
applies_to: [step_3, step_4]
expect: "lint findings classified against precedent before any fix decision"
on_fail:
  action: "classify novel findings, fix or surface them; log the house-style classes"
provenance:
  date: 2026-09-09
  app: 07_reo_group, 08_peoplebank
  source: "verification lint runs on both letters"
  detail: verified
status: active
last_validated: 2026-09-17
---

## Learned from
The 08 letter lints at 13 warnings: MD041 (first-line title), MD033
(inline HTML letter format), MD060 (table pipe alignment). The
approved 07 Reo letter lints at the same classes. Re-litigating
identical warnings every run burns attention.

## Rule
Classify lint findings once, against precedent files. Warnings that
match an approved precedent's classes (letter-format MD041, MD033,
MD060) are house style, not action items. Only novel findings
escalate to fixes, and the classification is recorded for the
retro.

## Rubric
- [ ] Lint run on the delivered artifact
- [ ] Findings diffed against the precedent classification
- [ ] House-style classes named, not fixed
- [ ] Novel findings fixed or surfaced at the checkpoint