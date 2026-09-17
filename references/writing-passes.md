# Writing passes — unslop and credibility rewrite

Read when starting step_4. Two passes turn the approved v1 draft into v2.
Each pass is driven by its source skill, read end to end — the pattern
catalogs live there, not here. If the optional skills configured at the
`unslop_skill` / `better_cover_letters` keys are unavailable, run the
degraded mode: the banned-terms scan via `verify_artifacts.py` only, and
say so at the checkpoint.

## Version preservation

Write the result as `cover-letter-draft-v2.md`; v1 stays untouched, forever.
Copies and renames are the last action of the pass. Any post-copy mutation
is re-verified. Never edit the approved v1.

## Pass 1 — unslop (human voice)

Read the skill configured at `unslop_skill` end to end and run its full
process: scan for its patterns, rewrite preserving meaning and tone, add
soul, then self-audit ("What makes this obviously AI generated?") and fix
the rest. The machine gate (`verify_artifacts.py`) catches what it can
measure: banned terms and em dashes.

## Pass 2 — credibility rewrite

Run the grounded pattern audit first: the skill configured at
`better_cover_letters` ships `scripts/init.py`; run
`python3 <that skill's dir>/scripts/init.py --letter <draft>` to stub a
table (No, pattern, verdict, notes), read the full skill end to end, and
fill every row with a verdict quoting the letter. An empty row means the
pass is not done. The skill owns its patterns, the rewrite process, the
evidence and ownership rules, and the final self-check — apply them from
there.

## Targeted rewrites per user feedback

Only address what the user specifies. Common requests: rewrite specific
table rows to derive evidence from a specific role; de-cliché subhead
labels to plain human language. Do not change other parts. When the user
says "only address what I mentioned", that is the whole instruction.

## Substantive-changes flag

After the passes, set the flag in `run-log.md`:

- `substantive_changes: yes` — a paragraph was rewritten, evidence was
  swapped, or structure moved → the conditional delta judge runs (see the
  judge protocol in operating-principles.md).
- `substantive_changes: no` — only small targeted fixes (de-clichéing,
  typo edits, user-flagged single replacements) → no judge run.

Then verify: `verify_artifacts.py --artifact cover-letter --path
<run>/cover-letter-draft-v2.md --matches <run>/matches.md` — zero flagged
words, zero em dashes, no fabricated evidence, ownership not exaggerated,
keyword coverage intact.

Checkpoint: present the result; wait for feedback and approval.