# job-application — rules/ (draft for review)

Atomic learned rules for the job-application workflow
(`notes/2026-applications/master-templates/workflow.md`), extracted
from the 07 Reo Group and 08 Peoplebank runs plus the user's standing
directives. This batch is retro #1, activated 2026-09-17 after review.
See CHANGELOG.md for the batch entry.

## Format

One rule per file: a YAML header (machine-parsed facts only) plus
three Markdown zones (prose). Rubric bullets can never break parsing.

| Field | Meaning |
|---|---|
| id | snake_case, mirrors the kebab-case filename |
| inventory | item number in the Checkpoint 1 extraction table |
| type | check · protocol · style · judgment · architecture |
| applies_to | step ids from the map below, or `[all]` |
| expect | check rules: the verifiable condition |
| on_fail | what happens when the rule fires |
| provenance | date, app, source, detail |
| related | other rule ids this one touches |

`detail: reconstructed` means at least part of the Learned-from
narrative was rebuilt from session summaries. The incidents are real;
the specifics may be off. Those files: 2, 3, 4, 5, 9, 10, 11, 18.
Check them hardest and correct anything misattributed. The evidence
rules in this folder apply to the rules themselves.

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

| # | File | Type | Steps | Detail | Learning |
|---|---|---|---|---|---|
| 1 | rule-structure-parity | check | 1, 2 | verified | Diff output structure against the example file before delivery |
| 2 | rule-word-budget | check | 1, 2 | reconstructed | Write to the stated budget, verify once, trim once |
| 3 | rule-copy-at-end | protocol | 0, 1, 5 | reconstructed | Copies are the last action; re-verify after any post-copy mutation |
| 4 | rule-tense-from-cv | check | 2 | reconstructed | Tense comes from the CV source of truth, never from precedent letters |
| 5 | rule-ownership-calibration | judgment | 2, 3 | reconstructed | Ownership verbs must match org-context records |
| 6 | rule-user-memory-outranks-records | judgment | 1, 2 | verified | Verification ends at a primary source; user memory wins over stored records |
| 7 | rule-corrections-propagate | protocol | 1, 2 | verified | A correction lands in every artifact and flags the source record |
| 8 | rule-scale-labeling | judgment | 1, 2 | verified | Evidence scale matches claim scale; side projects are labeled |
| 9 | rule-name-projects-attribute-companies | style | 2 | reconstructed | Name projects, attribute companies, cite concrete scale |
| 10 | rule-read-sources-first | protocol | 0 | reconstructed | Every step 0 source read before writing, each with its downstream function |
| 11 | rule-defer-to-team-knowledge | check | 1, 2 | reconstructed | How-I-would-start defers to existing team knowledge before proposing changes |
| 12 | rule-no-enumeration-colons | style | 2, 3 | verified | Colon-into-enumeration is an AI tell; rewrite as first-person process |
| 13 | rule-pattern-sibling-scan | protocol | 3 | verified | Fix the flagged instance, surface siblings, never silently edit approved prose |
| 14 | rule-label-vs-enumeration-colon | style | 3 | verified | Label colons are normal usage; only enumeration colons are tells |
| 15 | rule-preflight-resource-check | check | 0 | verified | Verify referenced skills, templates, and files exist before steps depend on them |
| 16 | rule-checkpoint-interview-tool | protocol | all | verified | Decision checkpoints use the question tool, with alternatives and a recommendation |
| 17 | rule-lint-classify-once | check | 2, 3 | verified | House-style lint classes are classified once via precedent, not re-litigated |
| 18 | rule-richness-for-cuts | judgment | 1, 2 | reconstructed | Keep evidence only if it closes a keyword hole or supports the role shape |
| 19 | rule-artifacts-on-disk | architecture | all | verified | Every step lands its output on disk before its checkpoint closes |

## How to review

1. Skim the table, then open files in any order (each is about 25 lines).
2. Fix prose directly, or note corrections in the question form that
   follows this batch.
3. The form also asks the design questions: home, relationship to
   workflow.md, rule granularity, learning-loop cadence, retro scope,
   and whether to flip these files to active.

## Not here yet, by design

- SKILL.md — exists; encodes steps step_0..step_4, step_audit, step_retro
  with YAML headers; steps 5-7 reserved for the companion skill.
- CHANGELOG.md — opened at the retro #1 batch activation.
- The corpus lives in the skill repo's `rules/` directory (previously
  local-only under `.pi/`; the skill now ships it).