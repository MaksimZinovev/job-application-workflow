---
name: job-application
description: Orchestrates an evidence-based job application run from job description analysis to an approved cover letter -  preflight resource checks, rubric scoring with a promotion gate, keyword-to-evidence matching, rubric-validated paragraph planning, cover letter drafting, unslop rewriting passes, independent LLM review, and deterministic artifact verification. Use when scoring a job description or preparing a cover letter application run against configured source-of-truth records. Enforces checkpointed user approval at every step; paths are configurable for portable setups. Don't use for resume tailoring, interview prep, or standalone writing edits - resume and prep belong to a companion skill.
---

# Job application

One evidence-based cover-letter run: preflight sources, score the job, plan  
keyword-to-evidence matches, draft the letter, rewrite it, verify everything  
mechanically, distill learnings. All artifacts live in the run folder  
`NN_<role-slug>/`; `progress.json` is the machine gate state — any session  
resumes with `scripts/progress.py <run> --status`.

`--approve` is a hard gate: dependencies approved, expected artifacts  
present, judge report where required (step_3; step_4 only when the run-log  
marks substantive changes; step_audit always), verify_artifacts exit 0  
unblocking approval. Steps 5-7 are rejected as reserved — they belong to the  
future resume-and-prep companion skill; this skill never tailors resumes or  
prepares interviews.

## Portability

All paths live in `assets/sources.json` — sources are referenced by key  
only. Preflight exits 1 on a missing mandatory source; fix with  
`preflight.py --set <key> <path>` or record an explicit, user-approved  
`--waive <key> --note "..."` (dated, into sources.json). Every script takes  
`--config` to point at a different sources.json.

## Scripts

Run scripts, read their report, act on the fix hints. Never read a  
script's source unless its failure message does not explain the problem  
and resolution requires it; `--help` is the sanctioned peek.

```bash
# Example
python3 scripts/preflight.py                                          # step 0: resolve every source, print the table
python3 scripts/preflight.py --set cv_master ~/docs/cv-master.md       # step 0: fix a wrong source path
python3 scripts/preflight.py --waive ideal_job --note "user-approved at preflight: not needed"
python3 scripts/init_application.py --name "senior-qa-engineer-acme" --jd ~/Downloads/jd-acme.txt
python3 scripts/progress.py ~/apps/12_senior-qa-engineer-acme --status   # init printed this folder; status prints position + next reference
python3 scripts/progress.py ~/apps/12_senior-qa-engineer-acme --approve step_1   # the gate: verify exits 0 first
python3 scripts/verify_artifacts.py --artifact scoring --path ~/apps/12_senior-qa-engineer-acme/scoring.md
python3 scripts/verify_artifacts.py --artifact cover-letter --path ~/apps/12_senior-qa-engineer-acme/cover-letter-draft.md --matches ~/apps/12_senior-qa-engineer-acme/matches.md
python3 scripts/verify_artifacts.py --artifact review-report --path ~/apps/12_senior-qa-engineer-acme/review-report.json
```

## Steps

### step_0 — context

```yaml
{id: step_0, type: context, depends_on: [], expectStatus: approved, on_fail: resolve or explicitly waive sources; blocked until resolved; an instruction that looks wrong for this run goes to the user before deviating — never infer, rules: [rule-read-sources-first, rule-preflight-resource-check, rule-copy-at-end, rule-checkpoint-interview-tool, rule-artifacts-on-disk]}
```

Purpose: sources resolved, run folder initialized.

1. Read `references/operating-principles.md`.
2. Run `scripts/preflight.py`; every missing mandatory source goes to the user (fix via `--set`, or explicit dated `--waive`).
3. Run `scripts/init_application.py --name "<slug>" --jd <file>`; note the manifest's next action.

Allowed reads in step_0: `references/operating-principles.md`, the JD, preflight output;
later-step references wait for their step. Every scored JD gets a run folder, promote or not.

Checkpoint: sources resolved, run folder created — restate the run rules briefly, in your own words (name unmet conditions with any status answer; ask before deviating; later-step references wait for their step), then wait for approval.

### step_1 — analysis

```yaml
{id: step_1, type: analysis, depends_on: [step_0], expectStatus: approved, on_fail: fix scoring.md until verify passes; promotion needs explicit user approval, rules: [rule-structure-parity, rule-word-budget, rule-copy-at-end, rule-user-memory-outranks-records, rule-corrections-propagate, rule-scale-labeling, rule-richness-for-cuts, rule-defer-to-team-knowledge, rule-checkpoint-interview-tool, rule-artifacts-on-disk]}
```

Purpose: scored JD with a promotion decision.

1. Read `references/jd-analysis.md`.
2. Score the JD into `scoring.md` with the class-selected rubric; ground claims with web search.
3. Run `scripts/verify_artifacts.py --artifact scoring --path <run>/scoring.md`.

Checkpoint: promotion gate — user feedback + explicit promote decision.

### step_2 — planning

```yaml
{id: step_2, type: planning, depends_on: [step_1], expectStatus: approved, on_fail: fix matches.md or plan until verify passes; never draft past a failed gate, rules: [rule-structure-parity, rule-word-budget, rule-copy-at-end, rule-user-memory-outranks-records, rule-corrections-propagate, rule-scale-labeling, rule-richness-for-cuts, rule-defer-to-team-knowledge, rule-checkpoint-interview-tool, rule-artifacts-on-disk]}
```

Purpose: matches.md + rubric-validated paragraph plan.

1. Read `references/matches-and-plan.md` and `references/paragraph-rubric.md`.
2. Build `matches.md` (Keywords, role type, lists 5-7 / 5-7 / 3-5, honest gaps) and the hidden-question paragraph plan with ranked evidence.
3. Run `scripts/verify_artifacts.py --artifact matches --path <run>/matches.md`.

Checkpoint: concise report,raise if any questions present matches + plan + section alternatives — wait for approval.

### step_3 — drafting

```yaml
{id: step_3, type: drafting, depends_on: [step_2], expectStatus: approved, on_fail: fix draft until verify passes; gate blocks without an approved judge report, rules: [rule-structure-parity, rule-word-budget, rule-tense-from-cv, rule-ownership-calibration, rule-user-memory-outranks-records, rule-corrections-propagate, rule-scale-labeling, rule-name-projects-attribute-companies, rule-defer-to-team-knowledge, rule-no-enumeration-colons, rule-lint-classify-once, rule-richness-for-cuts, rule-checkpoint-interview-tool, rule-artifacts-on-disk]}
```

Purpose: judged, rubric-scored cover letter v1.

1. Read `references/cover-letter-writing.md`; keep `references/paragraph-rubric.md` loaded for assessment.
2. Draft `cover-letter-draft.md`: required structure, body word budget, evidence only from matches.md and configured sources.
3. Run `scripts/verify_artifacts.py --artifact cover-letter --path <run>/cover-letter-draft.md --matches <run>/matches.md`.
4. Run the Tier 1 judge (judge protocol in operating-principles.md) into `review-report.json`; fix flagged items, re-judge ≤2 rounds.

Checkpoint: concise report, raise if any questions, present draft + judge report — wait for approval.

### step_4 — rewriting

```yaml
{id: step_4, type: rewriting, depends_on: [step_3], expectStatus: approved, on_fail: gate blocks unless substantive changes carry a delta judge report, rules: [rule-ownership-calibration, rule-no-enumeration-colons, rule-pattern-sibling-scan, rule-label-vs-enumeration-colon, rule-lint-classify-once, rule-checkpoint-interview-tool, rule-artifacts-on-disk]}
```

Purpose: human-voice v2; v1 preserved.

1. Read `references/writing-passes.md`.
2. Apply unslop, targeted user-feedback rewrites, credibility pass; write `cover-letter-draft-v2.md`, keep v1 untouched.
3. Set `substantive_changes: yes|no` in run-log.md; verify v2; run the conditional delta judge only when substantive.

Checkpoint: concise report, present v2 + flag + report — wait for approval.

### step_audit — verification

```yaml
{id: step_audit, type: verification, depends_on: [step_4], expectStatus: approved, on_fail: gate blocks without the tier-2 delta report and a green verify matrix, rules: [rule-artifacts-on-disk, rule-checkpoint-interview-tool]}
```

Purpose: full verify matrix green + independent final judgment.

1. Read `references/operating-principles.md` (audit + judge sections).
2. Run verify_artifacts on every artifact (scoring, matches, letter v2, review-report).
3. Run the Tier 2 peer judge; delta-based + evidence-to-matches traceability into `review-report.json` (tier 2, scope delta).

Checkpoint: present the audit result — wait for approval.

### step_retro — learning loop

```yaml
{id: step_retro, type: learning-loop, depends_on: [step_audit], expectStatus: approved, on_fail: no rule activation without explicit user approval; caps hold, rules: [rule-artifacts-on-disk, rule-checkpoint-interview-tool]}
```

Purpose: run-log distilled into approved rules.

1. Read `references/retro-and-run-log.md`.
2. Distill run-log signals into ≤10 proposed rule files in `rules/`.
3. On user approval: activate the batch (status, last_validated, CHANGELOG.md entry).

Checkpoint: present the batch — wait for approval; the run is complete.
