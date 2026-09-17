---
id: rule_artifacts_on_disk
inventory: 19
type: architecture
applies_to: [all]
on_fail:
  action: "land the output on disk before the checkpoint closes"
provenance:
  date: 2026-09-09
  app: 08_peoplebank
  source: "session interruption during step 3"
  detail: verified
status: active
last_validated: 2026-09-17
---

## Learned from
A session cut out mid-run during the 08 step 3. The continuation
recovered and finished verification because the v2 write had already
landed on disk. Nothing needed from the run lived only in the
conversation.

## Rule
Every workflow step lands its output on disk in the run folder
before its checkpoint closes. The run folder NN_<role>/ is the
source of truth, not the chat. Any future change to step design
must preserve interrupted-run recoverability: an interrupted run
resumes from artifacts, not from conversation memory.

## Rubric
- [ ] Each step's output written to the run folder before the checkpoint
- [ ] Nothing exists only in conversation memory
- [ ] Skill design edits checked against this invariant