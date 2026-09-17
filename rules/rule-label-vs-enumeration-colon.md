---
id: rule_label_vs_enumeration_colon
inventory: 14
type: style
applies_to: [step_4]
on_fail:
  action: "keep the label colon; rewrite only the enumeration colon"
provenance:
  date: 2026-09-09
  app: 08_peoplebank
  source: "annotation round 3, colon census"
  detail: verified
status: active
last_validated: 2026-09-17
related: [rule_no_enumeration_colons]
---

## Learned from
Scanning the letter for colon tells surfaced label colons too:
"Intellihub:", "Honest scope note:", "two versions: one for
engineers". Those are normal human usage. Rewriting them would
damage approved prose.

## Rule
Classify colons before fixing. Label and lead-in colons (a name, a
scope note, a ratio) are normal. Enumeration colons (a list dumped
after the colon) are the tell. Only enumeration colons get
rewritten.

## Rubric
- [ ] Colon census run with each colon classified
- [ ] Label colons named and left alone
- [ ] Only enumeration colons rewritten