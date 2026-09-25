<!--
GOLD EXAMPLE, run-log.md (raw-signal format precedent)

Source: run 10_quality-engineer-ai-12-months-contract-tyro. The run
predates the run-log convention; this file reconstructs the real signals
from the run's step1-checkpoint.md (which recorded all seven review
rounds) and the session records. User flags are paraphrased themes where
verbatim capture did not exist; quotes are verbatim where recorded.
Reconstructed, not byte-historical: read it as the format exemplar for
raw-signal logging, not a transcript.

Read for: one section per step; flags in the user's words; which checks
fired and what fixed them; the source-of-truth change that rippled
through every artifact; the substantive-changes flag that decides the
delta judge; no prose, no conclusions; the retro distills.
-->

# Run log — 10_quality-engineer-ai-12-months-contract-tyro

Raw signals only: what happened, what the user said, what changed and why.
The step_retro distills this into rule proposals. No polishing, no prose.

## Flags

substantive_changes: yes

<!-- step_4 writing passes: `yes` because the review rounds rewrote the
     intro, three body paragraphs, and the projects list; a pass rewrote
     prose, not just single words. progress.py --approve step_4 requires
     a delta review-report.json when this flag is `yes`. -->

## Log

### 2026-09-10 — step_0 / step_1

- sources read by key: job_search_context, cv_master, experience_records,
  rubric_full_time, ideal_job; JD from Indeed (Tyro Payments, 12-month
  fixed-term, Sydney CBD, hybrid 3 days)
- scored (8.1/10)-(1? team) against rubric_full_time; strongest AI-in-QE
  fit scored to date (Roles 10: hybrid AI+testing primary band); weak
  legs: 12-month term horizon, 600-staff scale, salary unstated (Tyro
  benchmarks: median $114.5K, SWE median comp $137K)
- promotion gate: user picked promote; step1-checkpoint.md opened to
  carry the step-2 checkpoint record

### 2026-09-10 — step_2

- matches.md built (7/6/4 lists, under the 10,000-char cap on first
  write); question-to-section map + claim-evidence wireframe delivered
- user feedback themes (rounds 1-2): table rows need the Description
  column discipline; GitHub links added to the plan

### 2026-09-10 — step_3 → step_4 (seven review rounds)

- v1 flags the user caught: claim-only subhead ("The loop you are
  building, I already run."); docfence grand claim ("catches the
  defects AI assistants leave behind"); "manager-validated" internal
  detail; a bold-marked typo ("daily in against regression tests in
  testing environment"); abstract intro framing ("It is a mandate to
  turn a QE team's AI ambitions into day-to-day machinery,")
- full flag-by-flag record: examples/review-report-gold-needs-fixes.json
- round 3: 8 changes applied; round 4: automation paragraph rewritten
  (~153 to 124 words incl. subhead), present-tense Intellihub verbs kept
  out (tense rule); round 5: general review pass; round 6: knowledge-base
  paragraph rewrite; round 7: record alignment (below)
- v2 verification: em/en dashes 0, curly quotes 0, trailing whitespace 0;
  lint clean except expected MD041 (name line); total 1204 words (was
  1233; −29 from removed claims + tightened WYWM line); keyword coverage
  holds: agent 13, Copilot 7, knowledge base 6, CI 11, regression 5, BDD
  5, Playwright 6, Python 4, test data 3, self-evolving 2, Rovo 2,
  payments 1
- substantive_changes flipped to yes (paragraph rewrites across rounds)

### 2026-09-11 — step_4 (round 7): source-of-truth change

- user rewrote [ai-005] in experience-pieces.json (uncommitted at the
  time): "daily in production" and "human review step before approval"
  REMOVED from the record; the tool "runs daily against test
  environment" instead
- user memory outranks stored records (rule-user-memory-outranks-records
  fired for real): the correction propagated to matches.md and both
  letter versions; the human-review-step line was cut from the letter
  (rule-corrections-propagate)
- round-5 wording tension also aligned with the current record

### 2026-09-11 — delivery

- cover-letter.pdf produced; interview-day-preparation-notes.md written
- retro signals: (1) the v1 claim patterns escaped the first writing pass;
  per-rule attention is spread thin across all patterns at once; (2) the
  record itself drifted from the user's memory between runs; preflight
  should surface record freshness; (3) the seven-round loop is the normal
  cost of a first full judged run; the rules corpus (19 rules) was
  distilled from runs like this one