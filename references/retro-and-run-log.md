# Run log and retro — the learning loop

Read when starting step_retro, the final step of a run.

## run-log.md convention

`run-log.md` is created from the run-log template at init and kept during
the run as a raw-signal log — not prose. Record as you go:

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
2. Read the run-log and distill recurring signals into candidate rules:
   what fired, what the user corrected, what a judge kept flagging.
3. Cap the sweep: consult at most 3 previous application runs' signals per
   sweep, and propose at most 10 rules per sweep. Pick the highest-signal
   learnings; leave the rest in the log.
4. Write each candidate as a rule file in `rules/` (format below), status
   `proposed`.
5. Present the batch to the user for approval. On approval, batch-activate:
   flip `status: proposed → active`, set `last_validated` to the approval
   date, and open/append `CHANGELOG.md` with a batch entry (date, run, rule
   list, one-line learning each).
6. Never activate a rule without explicit user approval.

## Rule-file format

One rule per file: a YAML header (machine-parsed facts only) plus three
Markdown zones. Rubric bullets can never break parsing.

| Field | Meaning |
|---|---|
| id | snake_case, mirrors the kebab-case filename |
| inventory | item number in the extraction batch |
| type | check · protocol · style · judgment · architecture |
| applies_to | step ids from the canonical map, or `[all]` |
| expect | check rules: the verifiable condition |
| on_fail | what happens when the rule fires |
| provenance | date, app, source, detail |
| related | other rule ids this one touches |

`detail: reconstructed` marks a rule whose Learned-from narrative was partly
rebuilt from session summaries: the incident is real, the specifics may be
off. Those files are checked hardest and corrected first.

The evidence rules of this skill apply to the rules themselves: no
fabricated learnings, corrections propagate to related rules, user memory
outranks stored records.

## Scope limits

- The retro touches only the `rules/` directory, `CHANGELOG.md`, and the
  run-log itself. Nothing else changes at this step.
- Proposed rules must be atomic (one rule per file), traceable to a
  run-log signal or user directive, and state their on_fail behavior.
- A run ends with step_retro approved; `progress.py --status` reports the
  run complete.
