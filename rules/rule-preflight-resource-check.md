---
id: rule_preflight_resource_check
inventory: 15
type: check
applies_to: [step_0]
expect: "every referenced skill, template, and source file exists at its expected path"
on_fail:
  action: "surface the missing dependency before drafting starts, propose a substitute"
provenance:
  date: 2026-09-09
  app: 08_peoplebank
  source: "claude-skill removal scare + job-kit README naming missing scripts"
  detail: verified
status: active
last_validated: 2026-09-17
---

## Learned from
The user removed a skill (claude-skill) between runs. The workflow's
dependent skills could have gone the same way, and the check that
confirmed unslop and better-cover-letter-writing intact ran only
after the worry surfaced mid-run. The working-style section already
says to pause and flag unavailable resources, and the repo keeps
proving the need: job-kit's README names matches.toml,
cover-letter.toml, and validate-cover-letter.py while its
references/ and scripts/ folders are empty.

## Rule
At preflight, verify every referenced skill, template, and source
file exists at its expected path before any step depends on it: the
two writing skills, the scoring rubric, the example matches.md, the
master CV, and experience-pieces.json, which lives outside this
repo at ~/repos/jobkit. A dependency missing at step 0 costs a
minute; found at step 3 it costs the run.

## Rubric
- [ ] Dependency list compiled from the workflow's references
- [ ] Existence verified at step 0, including cross-repo files
- [ ] Missing dependencies surfaced with a proposed substitute before drafting starts