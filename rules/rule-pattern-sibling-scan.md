---
id: rule_pattern_sibling_scan
inventory: 13
type: protocol
applies_to: [step_4]
on_fail:
  action: "present siblings with proposed rewrites, wait for approval"
provenance:
  date: 2026-09-09
  app: 08_peoplebank
  source: "annotation round 3"
  detail: verified
status: active
last_validated: 2026-09-17
related: [rule_no_enumeration_colons, rule_label_vs_enumeration_colon]
---

## Learned from
User flagged line 24 (colon introducing a four-cause enumeration) as
an AI tell. Fixing it left three sibling instances in prose the user
had already approved. Editing those silently was off-limits, so they
were surfaced with proposed rewrites instead.

## Rule
When the user flags a pattern instance: fix that instance, then scan
the document for siblings of the same pattern class. Present siblings
with proposed rewrites at the next checkpoint. Never silently edit
approved prose. The workflow already forbids changing parts the user
did not specify (3.2); scanning and surfacing is how that stays
honest. Classify before fixing: label colons ("Honest scope note:")
are normal usage; enumeration colons are the tell.

## Rubric
- [ ] Flagged instance fixed in the same document
- [ ] Sibling scan run; results listed with proposed rewrites
- [ ] Genuine tells discriminated from normal usage, normal cases named
- [ ] No edits beyond the flagged instance without explicit approval