# Run log and retro — the learning loop

Read when starting step_retro, the final step of a run.

## run-log.md convention

`run-log.md` is created from the run-log template at init and kept during
the run as a raw-signal log — not prose. Format precedent:
`examples/run-log-gold.md`. Record as you go:

- which sources were read (by key) and anything odd about them;
- which checks fired and what fixed them;
- what the user flagged, in their words;
- judge findings and what was changed in response;
- the substantive-changes flag for step_4: set
  `substantive_changes: yes` when a pass rewrote a paragraph, swapped
  evidence or moved structure; `substantive_changes: no` for small targeted
  fixes. progress.py reads this flag to decide whether the delta judge must
  run before step_4 can be approved.

Raw signals, not conclusions — the retro distills them.

## Retro procedure

1. Wait until step_audit is approved.
2. Read the run-log and the run's `rule-checks.json`, and distill
   recurring signals into candidate rules: what fired, what the user
   corrected, what a judge kept flagging. The rule-check scores are the
   worst-rules signal: a rule that keeps scoring 2 across runs is noisy —
   reinforce its explanation or example, or propose rewording or
   retirement; any 0 or 1 marks a rule the run violated, and the retro
   asks why the check missed it at writing time.
3. Cap the sweep: consult at most 3 previous application runs' signals per
   sweep, and propose at most 5 rules per sweep. Pick the highest-signal
   learnings; leave the rest in the log.
4. Write each candidate as a rule file in `rules/` (format below), status
   `proposed`.
5. Present the batch to the user for approval. On approval, batch-activate:
   flip `status: proposed → active`, set `last_validated` to the approval
   date, open/append `CHANGELOG.md` with a batch entry (date, run, rule
   list, one-line learning each), and check the gold examples and
   teaching pairs that demonstrate any rule in the batch — update them in
   the same batch so they teach the rule as it now stands.
6. Wins become examples. When this run's artifacts are user-approved, ask
   whether any of them is gold-example material: strong on the rubric,
   real, with lessons worth preserving. Run the diversity check first —
   look at what `examples/` already covers and prefer a nomination that
   fills a gap (a different job class, a different failure type, a
   different scenario) over another example of what the set already
   shows. A nomination copies the artifact with a provenance header and
   known-seam annotations, following the bundled gold set's curation,
   and is presented at the checkpoint for approval.
7. Never activate a rule or add an example without explicit user
   approval.

## Rule-file format

One rule per file: a YAML header (machine-parsed facts only) plus three
Markdown zones. Rubric bullets can never break parsing.

| Field | Meaning |
|---|---|
| id | snake_case, mirrors the kebab-case filename |
| inventory | item number in the extraction batch |
| type | check · protocol · style · judgment · architecture |
| evidence | quote · confirm · measure: the proof the gate demands in the check file |
| applies_to | step ids from the canonical map, or `[all]` = wired at every SKILL.md step |
| expect | check rules: the verifiable condition |
| on_fail | what happens when the rule fires |
| provenance | date, app, source, detail |
| status | active · proposed: proposed stays out of the digest and every gate until user approval |
| last_validated | date of the last user-approved activation |
| related | other rule ids this one touches |

`detail: reconstructed` marks a rule whose Learned-from narrative was partly
rebuilt from session summaries: the incident is real, the specifics may be
off. Those files are checked hardest and corrected first.

The evidence rules of this skill apply to the rules themselves: no
fabricated learnings, corrections propagate to related rules, user memory
outranks stored records.

## Scope limits

- The retro touches only the `rules/` directory, `CHANGELOG.md`, the
  run-log itself and — for approved example nominations — `examples/` and
  the README tree. Nothing else changes at this step.
- Proposed rules must be atomic (one rule per file), traceable to a
  run-log signal or user directive, and state their on_fail behavior.
- A run ends with step_retro approved; `progress.py --status` reports the
  run complete.
