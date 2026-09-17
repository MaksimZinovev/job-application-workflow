---
id: rule_no_enumeration_colons
inventory: 12
type: style
applies_to: [step_3, step_4]
on_fail:
  action: "rewrite as first-person process or plain prose"
provenance:
  date: 2026-09-09
  app: 08_peoplebank
  source: "annotation round 3, line 24"
  detail: verified
status: active
last_validated: 2026-09-17
related: [rule_label_vs_enumeration_colon, rule_pattern_sibling_scan]
---

## Learned from
Annotation round 3 on the 08 letter flagged a colon introducing a
four-cause enumeration ("the failure point usually belongs to a small
set of causes: environment, test data, test script, or the
application itself") as an AI tell. The unslop mandate already
forbids forced three-part lists; this is the same family. The fix
kept the taxonomy but made it the tester's habit: "I first ask
whether ... is at fault."

## Rule
A colon that dumps an enumeration is an AI tell. Rewrite the list as
first-person process or plain prose, keeping the full content. Apply
while drafting and again in the unslop pass.

## Rubric
- [ ] No enumeration colons in delivered prose
- [ ] Rewrites keep the full content of the original list
- [ ] The rewrite stays in first-person voice