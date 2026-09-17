---
id: rule_defer_to_team_knowledge
inventory: 11
type: check
applies_to: [step_1, step_2, step_3]
expect: "every how-I-would-start passage defers to existing team knowledge before proposing changes"
on_fail:
  action: "add the deferral before the proposal"
provenance:
  date: 2026-09-08
  app: 07_reo_group
  source: "annotation round"
  detail: reconstructed
status: active
last_validated: 2026-09-17
---

## Learned from
A how-I-would-start section jumped straight to what the user would
change. The annotation: that reads as ignoring the incumbent team.
Defer to existing team knowledge first.

## Rule
Any passage describing how the user would start must first defer to
the existing team's knowledge and current practice, then propose
changes on that foundation. This is the question-3 hidden-question
paragraph (workflow 1.8), so the expectation applies from the mapping
in matches.md through the letter draft.

## Rubric
- [ ] Deferral present and specific, not a generic nod
- [ ] Deferral names what to learn and from whom
- [ ] Proposals follow the deferral, never precede it