# Operating principles

Cross-cutting rules for every step of an application run. Read at run start
(step_0) and again at the verification step (step_audit). Sources are referenced
by key from `assets/sources.json`; the preflight script resolves the paths.

## Checkpoint protocol

- Work milestone by milestone. Never advance past a step until its checkpoint
  closes: present the artifact, ask for feedback, wait for explicit approval.
- Follow every step in full, in order. If an instruction looks wrong for
  this run, ask the user before deviating — never infer a deviation, never
  skip silently. Deviation by inference is a defect; a user-approved change
  is a decision.
- A checkpoint is done only when every listed condition is met. Answer a
  status question by naming any unmet condition in the same breath — a bare
  "yes" that buries one is a false report.
- `progress.py` is the machine gate. A step is approved only when its
  dependencies are approved, its expected artifacts exist, and — where the judge
  gate applies — `review-report.json` carries verdict `approved` at the required
  tier and scope. A refused gate is a finding, not an obstacle: fix the named
  gap and re-run. Never edit gate state by hand.
- At a decision point with several viable paths, present the alternatives with
  a short pro/con each and one professional recommendation. Let the user pick.
- Keep responses concise unless the user asks for more detail. When unsure,
  ask. Pause and flag it if any configured resource is missing or hard to
  locate rather than improvising around it.
- Every step lands its output on disk before its checkpoint closes. Unsaved
  work is lost work.

## No fabrication

- Strictly no fabricated claims — ever. Every sentence in a scored or drafted
  artifact must trace to a configured source (the CV source of truth by key
  `cv_master`, the recent-role evidence under `experience_records`, or an
  artifact already on disk in the run folder).
- Verification ends at a primary source. Stored records are strong, but the
  user's own memory of an event outranks any stored record. When they
  conflict, ask; never silently pick one.
- A correction lands in every downstream artifact, and the source record
  itself is flagged for repair — do not patch one file and leave the rest.
- Never strengthen a claim beyond its evidence. If a stronger claim might be
  true but is not evidenced, keep the weaker version.
- Do not remove content silently during any rewriting pass. Do not invent
  evidence, metrics, outcomes, or responsibilities. Ask when unsure.

## Context economy

- Context is a limited resource. Read and explore only what the current step
  needs; peek into a file before committing to a full read; ask the user when
  in doubt about scope.
- Read reference files just in time: `progress.py --status` prints the
  reference for the next step. Do not preload every reference at once.
- Do not read a later step's references early. That is drift, not
  preparation. If more context feels needed, ask the user first.
- Scripts are black-box tools. Invoke them with the sample commands in
  SKILL.md (or `--help`), read the stdout report and stderr fix hints, and
  act on those. Never read a script's source unless its failure message
  does not explain the problem and resolution requires it; if it does,
  treat it as a skill defect and record it in the run log for the retro.
- The run folder is the working scope for a step. Do not wander into other
  application folders except to consult an approved precedent the user names.

## Interview-tool decision points

Use the interview/question tool with concrete alternatives and a
recommendation at these points:

1. **Missing mandatory source** (preflight exits 1): ask the user to fix the
   path (then `preflight.py --set <key> <path>`) or to explicitly waive the
   source. A waiver is recorded, dated, only by `preflight.py --waive <key>
   --note "..."` after the user explicitly approves it. Approval is never
   silent; the workflow does not advance without a resolved or waived source.
2. **Promotion gate** (after scoring): ask whether to promote this job from
   scoring to application, and collect any scoring feedback first.
3. **Ambiguous requirements**: whenever the job description or user intent is
   unclear, ask a targeted set of questions before proceeding.
4. **Checkpoints**: after each delivery, ask for feedback and approval.

## Scope limits

- This skill covers one cover-letter application run: analysis, planning,
  drafting, rewriting, verification, retro. It does not build resumes, tailor
  documents, or prepare interviews — those belong to a companion skill, and
  steps 5-7 are reserved for it. Do not improvise them here.
- Do not modify anything outside the run folder, the configured sources, and
  the skill's own `rules/` directory (retro only).
- Preserve previous versions: `cover-letter-draft.md` (v1) is never edited
  after v2 exists; copies are the last action of a step, and any post-copy
  mutation is re-verified.

## Tiered judge protocol

Programmatic checks (verify_artifacts.py) catch budgets, structure, and
clichés. Rubric dimensions — question coverage, source fidelity,
demonstration, story continuity, evidence economy, reader ease — need
judgment. The judge runs in tiers so token cost stays proportional to risk.

- **Tier 0 — mechanical gate, always first, zero LLM cost.**
  `verify_artifacts.py` runs before any judge. The judge never sees text that
  fails mechanical checks, and no tokens are spent re-discovering what a
  regex catches.
- **Tier 1 — fresh-context judge after the first full draft (step_3).** The
  first full draft is where issues live. The judge gets the locked criteria
  (the paragraph rubric, the writing don'ts, the evidence rules), the full
  draft, and matches.md — no run context. Fresh context is most of the
  independence value: a fresh-context self-judge or a different cheap model
  both qualify; a different model is a bonus, not a requirement. Scope: full.
- **step_4 — conditional delta judge.** Writing passes are mostly mechanically
  checkable. The judge runs only when the run-log marks
  `substantive_changes: yes` (a paragraph rewritten, evidence swapped,
  structure moved). Small targeted fixes — de-clichéing, typo edits,
  user-flagged single replacements — skip it. When it runs, it is
  delta-based: the previous review-report plus changed paragraphs only,
  verifying fixes and spot-checking neighbors. Never a fresh full-letter pass.
- **Tier 2 — peer judge at step_audit, the paid final gate.** An independent
  peer agent or second model, delta-based: consumes the accumulated review
  reports, judges the delta since last approval, and cross-checks
  evidence-to-matches traceability. Escalate from Tier 1 early when the Tier 1
  judge flags something contested or the writer disagrees with a flag.

Protocol per run:

1. Tier 0 passes, then the judge runs at the tier above and writes
   `review-report.json` from the review-report template: verdict,
   per-dimension scores, every flagged sentence, judge identity, tier, scope.
2. Fix every flagged item; re-judge; re-judge rounds are capped at 2 per gate.
   Anything still contested escalates to the human checkpoint.
3. The gate is mechanical: `verify_artifacts.py --artifact review-report`
   fails a missing or unapproved report, and `progress.py --approve` blocks
   step_3, step_4 (substantive changes only), and step_audit without it.
   Enforcement lives in scripts, not memory.

Every judge run is one exhaustive structured pass (all dimensions scored,
every flagged sentence listed) so re-runs stay minimal.
