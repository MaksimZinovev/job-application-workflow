# job-application — rules/

Atomic learned rules for the job-application workflow encoded in
SKILL.md. The corpus is active: every rule here is wired into the
workflow's steps through the generated digest
(references/rule-digests.md) and closed out by the per-rule check
loop (scripts/check_rules.py).

The first 19 rules are retro #1: extracted from the 07 Reo Group and
08 Peoplebank runs plus the user's standing directives, activated
2026-09-17 after review. Rules 20 and 21 came from the 2026-09
skill-review session. See CHANGELOG.md for the batch entries. The
workflow's first prose draft still lives in the wiki at
`notes/2026-applications/master-templates/workflow.md`; SKILL.md
supersedes it.

## Format

One rule per file: a YAML header (machine-parsed facts only) plus
three Markdown zones (prose). Each file is a single page, 30-45
lines. Rubric bullets can never break parsing.

| Field | Meaning |
|---|---|
| id | snake_case, mirrors the kebab-case filename |
| inventory | corpus position: retro #1 batch order (1-19); rules from later batches take the next free number (the 2026-09 batch took 20 and 21) |
| type | check · protocol · style · judgment · architecture |
| evidence | quote · confirm · measure: the proof the check loop demands |
| applies_to | step ids from the map below, or `[all]` = wired at every SKILL.md step |
| expect | the verifiable condition; every check rule carries one, protocol rules may |
| on_fail | what happens when the rule fires |
| provenance | date, app, source, detail |
| status | active · proposed: proposed stays out of the digest and every gate until user approval |
| last_validated | date of the last user-approved activation |
| related | other rule ids this one touches |

`provenance.detail: reconstructed` means at least part of the
Learned-from narrative was rebuilt from session summaries. The
incidents are real; the specifics may be off. Those files: 2, 3, 4,
5, 9, 10, 11, 18. Check them hardest and correct anything
misattributed. The evidence rules in this folder apply to the rules
themselves.

## Step map

| id | step focus |
|---|---|
| step_0 | context: preflight sources, init run folder |
| step_1 | analysis: JD understanding, rubric scoring, promotion gate |
| step_2 | planning: matches.md lists + gaps, hidden questions, evidence ranking, rubric-validated paragraph plan |
| step_3 | drafting: cover letter v1, judged + rubric-scored |
| step_4 | rewriting: unslop + credibility passes, conditional delta judge |
| step_audit | verification: full verify matrix, tier-2 peer judge, evidence cross-check |
| step_retro | learning loop: run-log distilled into proposed rules, batch approval |
| step_5/6/7 | RESERVED for the resume-and-prep companion skill |

Runs live in the `NN_<role>/` folders under `notes/2026-applications/`.
That pattern is rule 19 in action; the skill inherits it, nothing moves.

## Inventory

Steps are the step ids from the map above (step_1 → 1); `all` =
wired at every step. The frontmatter is the truth source; this table
mirrors it.

| # | File | Type | Steps | Detail | Learning |
|---|---|---|---|---|---|
| 1 | rule-structure-parity | check | 1, 2, 3 | verified | Diff output structure against the example file before delivery |
| 2 | rule-word-budget | check | 1, 2, 3 | reconstructed | Write to the stated budget, verify once, trim once |
| 3 | rule-copy-at-end | protocol | 0, 1, 2 | reconstructed | Copies are the last action; re-verify after any post-copy mutation |
| 4 | rule-tense-from-cv | check | 3 | reconstructed | Tense comes from the CV source of truth, never from precedent letters |
| 5 | rule-ownership-calibration | judgment | 3, 4 | reconstructed | Ownership verbs must match org-context records |
| 6 | rule-user-memory-outranks-records | judgment | 1, 2, 3 | verified | Verification ends at a primary source; user memory wins over stored records |
| 7 | rule-corrections-propagate | protocol | 1, 2, 3 | verified | A correction lands in every artifact and flags the source record |
| 8 | rule-scale-labeling | judgment | 1, 2, 3 | verified | Evidence scale matches claim scale; side projects are labeled |
| 9 | rule-name-projects-attribute-companies | style | 3 | reconstructed | Name projects, attribute companies, cite concrete scale |
| 10 | rule-read-sources-first | protocol | 0 | reconstructed | Every step 0 source read before writing, each with its downstream function |
| 11 | rule-defer-to-team-knowledge | check | 2, 3 | reconstructed | How-I-would-start defers to existing team knowledge before proposing changes |
| 12 | rule-no-enumeration-colons | style | 3, 4 | verified | Colon-into-enumeration is an AI tell; rewrite as first-person process |
| 13 | rule-pattern-sibling-scan | protocol | 4 | verified | Fix the flagged instance, surface siblings, never silently edit approved prose |
| 14 | rule-label-vs-enumeration-colon | style | 4 | verified | Label colons are normal usage; only enumeration colons are tells |
| 15 | rule-preflight-resource-check | check | 0 | verified | Verify referenced skills, templates, and files exist before steps depend on them |
| 16 | rule-checkpoint-interview-tool | protocol | all | verified | Decision checkpoints use the question tool, with alternatives and a recommendation |
| 17 | rule-lint-classify-once | check | 3, 4 | verified | House-style lint classes are classified once via precedent, not re-litigated |
| 18 | rule-richness-for-cuts | judgment | 1, 2, 3 | reconstructed | Keep evidence only if it closes a keyword hole or supports the role shape |
| 19 | rule-artifacts-on-disk | architecture | all | verified | Every step lands its output on disk before its checkpoint closes |
| 20 | rule-context-per-evidence | check | 3, 4 | verified | Evidence sentences name who did the work, where, and what changed; facts from different roles never share a sentence |
| 21 | rule-example-maintenance | protocol | retro | verified | When a rule batch changes a rule, the examples teaching it are checked in the same batch |

## How rules change

Retro is the only path. A run's step_retro distills the run-log and
rule-checks.json signals into at most 5 proposed rule files per
sweep, each `status: proposed` and out of the digest and every gate
until approval. The user approves or rejects the batch at the
checkpoint; approval flips `status` to active, sets `last_validated`
to the approval date, and lands a CHANGELOG entry. Never activate a
rule without explicit user approval. When a batch changes a rule,
the examples that teach it are checked in the same batch (rule 21).
The loop's home is references/retro-and-run-log.md; this section is
a summary, not a second definition.

## Elsewhere in this repo

- SKILL.md: the workflow itself. Steps step_0..step_4, step_audit,
  step_retro with YAML headers; steps 5-7 reserved for the companion
  skill.
- CHANGELOG.md: batch history, opened at retro #1 activation.
- references/retro-and-run-log.md: the retro loop's definition.
  How a run's log is kept, how proposals are batched and activated.
- references/rule-digests.md: the generated digest. Rebuild with
  scripts/build_digests.py after any batch. scripts/check_rules.py
  runs the per-rule check loop.
- The corpus previously lived local-only under `.pi/`; the skill now
  ships it in this folder.