---
id: rule_user_memory_outranks_records
inventory: 6
type: judgment
applies_to: [step_1, step_2, step_3]
on_fail:
  action: "downgrade the claim to the user-confirmed version, flag the source record"
provenance:
  date: 2026-09-08
  app: 07_reo_group
  source: "annotation (SmartCore)"
  detail: verified
status: active
last_validated: 2026-09-17
related: [rule_corrections_propagate]
---

## Learned from
The fact-check passed 12/12 while containing a false claim: "both
frameworks, IWS and SmartCore" matched matches.md, which inherited it
from experience-pieces.json [ai-009]. The user, the primary source,
did not remember SmartCore in the analysis. Second case: 6 sessions
from a stale JSON where the true count was 8.

## Rule
Fact verification terminates at a primary source. Letter to
matches.md to experience-pieces.json is a circular chain, not
verification. When user memory conflicts with a stored record, the
user wins. Corrections propagate to every artifact carrying the fact,
and the source record gets flagged for correction at origin.

## Rubric
- [ ] Each number and named system traces to a user-confirmed source
- [ ] User corrections applied to all artifacts, not only the annotated one
- [ ] Conflicting source records surfaced with a proposed source edit