---
id: rule_checkpoint_chat
inventory: 16
type: protocol
evidence: confirm
applies_to: [all]
on_fail:
  action: "re-present the checkpoint in chat, plain language, nothing hidden"
provenance:
  date: 2026-09-29
  app: all_runs
  source: "user directive 2026-09-29: the skill is portable, no interview tool assumed; checkpoints go to chat in plain language. Supersedes the 2026-09-09 structured-options directive's delivery layer; its alternatives-and-recommendation content lives on."
  detail: verified
status: active
last_validated: 2026-09-29
---

## Learned from
First directive (2026-09-09): at decision points, present options
with alternatives and a recommendation, never buried in prose.
Second directive (2026-09-29): the skill must be portable. No
harness tool is assumed. The checkpoint is a chat message in plain
language.

## Rule
Every decision checkpoint is a chat message the user reads in plain
language. Shape it: what was done; issues found, with every skip,
workaround, and failure named, nothing silent; what to read, with
paths; what to act on, explicit; recommendation with reasoning;
the decision asked plainly. Keep it 5 to 10 lines, adapted to the
situation. Applies at every step: the step_1 promote decision,
per-step checkpoints, and any mid-run fork. Never bury a decision
in prose and hope the user notices.

## Before → After

Before (run 14, tool era):
Questions JSON written to a file, the tool misread inline JSON as a
path, then rejected a field's schema, a temp file sat in the run
folder, and only then the form opened. Four turns of mechanics
before the user saw anything.

After (chat, plain):
"step_1 done. Scored the Upstate JD: (8.3/10)-(2?), verdict
PROMOTE. Issues: none skipped; the two ?/10 rows are honest
unknowns, not guesses. Read: scoring.md, the research-grounded
table. Action: reply promote to continue, or give scoring feedback
first. Recommendation: promote. Strongest applied-AI fit of the
run."

## Rubric
- [ ] Plain language, 5 to 10 lines, adapted to the situation
- [ ] Done, issues, read, action all present; nothing silent
- [ ] Recommendation with reasoning; the decision asked plainly
