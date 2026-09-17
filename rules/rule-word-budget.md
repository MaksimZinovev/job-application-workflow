---
id: rule_word_budget
inventory: 2
type: check
applies_to: [step_1, step_2, step_3]
expect: "artifact size within the budget the workflow states for it"
on_fail:
  action: "trim once to a stated target, re-verify, deliver"
provenance:
  date: 2026-09-08
  app: 07_reo_group
  source: "budget whack-a-mole: matches 14.2K down to 9,998 chars, scoring section 5,309 down to 4,990"
  detail: reconstructed
status: active
last_validated: 2026-09-17
---

## Learned from
The 07 run produced two over-budget artifacts, both trimmed only
after the fact. matches.md landed around 14.2K characters against the
10K budget the workflow sets (item 1.4), and a Scoring Results
section hit 5,309 against its 5,000-character cap (item 1.2). Each
came down through repeated measure-and-trim cycles, because the
budget was never a constraint at writing time.

## Rule
Know the budget before drafting. matches.md stays under 10K
characters, the Scoring Results section under 5,000, and the letter
content budget is confirmed with the user whenever it needs to grow
(workflow step 2.1: always ask and justify). Write to the budget,
verify once after writing, and if over, trim once to a stated target
and re-verify. No blind trim-and-hope cycles.

## Rubric
- [ ] Budget named for the artifact before drafting starts
- [ ] One verification pass after writing
- [ ] If over budget: one trim pass to target, then re-verify