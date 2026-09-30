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
  gate applies — its own `review-report-<step>.json` carries verdict `approved`
  at the required tier and scope, judging the artifact that gate requires. A
  refused gate is a finding, not an obstacle: fix the named gap and re-run.
  Never edit gate state by hand.
- At a decision point with several viable paths, present the alternatives with
  a short pro/con each and one professional recommendation. Let the user pick.
- Keep responses concise unless the user asks for more detail. When unsure,
  ask. Pause and flag it if any configured resource is missing or hard to
  locate rather than improvising around it.
- Every step lands its output on disk before its checkpoint closes. Unsaved
  work is lost work.
- End every file written in the run folder with a newline; the wiki linter
  rewrites files without one and forces a re-read.
- Every step closes its rule loop before its checkpoint:
  `scripts/check_rules.py <run> --step <step> --gate` exits 0 — every rule
  of the step confirmed in its own attention window: quote rules with a
  verbatim span from the artifact, measure rules with the measurement
  stated in the note (its number, checked by the gate), confirm rules
  with a written statement of how they are honored, scores recorded in
  `rule-checks.json` for the retro. A failed gate is a finding: apply the
  named fixes, re-check those rules, close the gate.

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

## Sibling scans

When you fix a flagged instance of any pattern or rule — yours, the user's,
or the judge's — scan the whole artifact for siblings of the same class
before touching anything else. Fix the flagged instance; list every sibling
found with a proposed rewrite; never silently edit prose the user has
already approved. The scan is judgment; the claim is guarded: every
per-rule check file carries `siblings-checked: yes`, and `check_rules.py
--gate` rejects a check without the attestation. Classify before fixing:
label colons and other normal usage are named as normal, not "fixed" —
the sibling list is where the discrimination shows.

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

## Checkpoint decision points

Ask the user at these points, in chat, plain language, with
alternatives and a recommendation (rule-checkpoint-chat):

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
- **Tier 1 — independent judge after the first full draft (step_3).**
  The first full draft is where issues live. The judge gets the locked
  criteria (the paragraph rubric, the writing don'ts, the evidence rules),
  the full draft, and matches.md, with no run context. By default it runs
  independently: a subagent or separate agent session the harness spawns,
  or a peer agent when one is reachable, whichever the preflight
  capability check recorded (a different model is a bonus, not a
  requirement). When no independent mechanism exists, the fallback is a
  self-review by the drafting agent: weaker (it cannot un-know the
  drafting), recorded as kind self-review, and approved explicitly by
  the user at the checkpoint. Scope: full.
- **Letter-review criteria source.** Any judge reviewing cover-letter text
  also gets the skill configured at `better_cover_letters`, in full, as
  review criteria: its patterns, evidence rule, ownership rule, and final
  self-check. The invoking agent hands the resolved skill file in with the
  review inputs. Once the grounded pattern-audit table exists (step_4
  onward), it is part of the input too: every row populated, verdicts
  quoting the letter. When the source does not resolve, the judge reviews
  against the locked criteria only and says so at the checkpoint.
- **step_4 — conditional delta judge.** Writing passes are mostly mechanically
  checkable. The judge runs only when the run-log marks
  `substantive_changes: yes` (a paragraph rewritten, evidence swapped,
  structure moved). Small targeted fixes — de-clichéing, typo edits,
  user-flagged single replacements — skip it. When it runs, it is
  delta-based: review-report-step_3.json plus changed paragraphs only,
  verifying fixes and spot-checking neighbors. Never a fresh full-letter pass.
- **Tier 2 — peer judge at step_audit, the paid final gate.** An independent
  peer agent or second model, delta-based: consumes the accumulated reports
  (`review-report-step_3.json`, `review-report-step_4.json` when it exists),
  judges the delta since last approval, and cross-checks
  evidence-to-matches traceability. Its rules_audit is scoped to the judged
  artifact's step, not step_audit (the gate derives the scope from the
  report's `artifact` field), so the peer pass re-audits the letter's quote
  and measure rules with fresh eyes; an empty rules_audit fails the gate.
  Escalate from Tier 1 early when the Tier 1 judge flags something contested
  or the writer disagrees with a flag.

### Instantiating the judge

The tiers say when and what; this says how a judge comes to exist.
The judge block's kinds are instantiated, not declared:

- **subagent (tier 1 default).** The harness spawns a second agent
  session that shares nothing with the drafting conversation: the
  judge starts from the artifact, not from memory of writing it.
  Hand it the review inputs only: the judged artifact, matches.md,
  the locked criteria (paragraph rubric, writing don'ts, evidence
  rules), the resolved better_cover_letters skill, the
  review-report template, and the digest rows for the judged step
  (its quote and measure rules are the rules_audit scope). It
  returns the completed report. Identity names the judging model or
  agent; kind subagent.
- **different-model.** The same recipe with a different model
  behind the subagent. Identity names that model; kind
  different-model.
- **peer-agent (tier 2, or tier 1 when one is reachable).** An
  independent peer: a second agent on the same machine or hub,
  never a session that watched the drafting. Hand it the accumulated
  gate reports plus the delta inputs the tier describes. Identity
  names the peer; kind peer-agent.
- **self-review (the fallback).** The drafting agent judges its own
  letter against the locked criteria, in the same conversation. It
  cannot un-know the drafting, so it is the weakest kind; it runs
  only when the preflight check found no independent mechanism.
  Record it honestly (kind self-review) and get explicit user
  approval at the checkpoint.
- The independent judge never receives the drafting conversation,
  the writer's intentions, or the run's chat history. A judge that
  saw the drafting is a self-review; that is exactly why
  independence is the default and the fallback is named.
- Which kinds exist here is a preflight fact, not a per-run guess:
  at step_0, preflight.py asks and records judge_capability
  (subagent | peer-agent | none) in sources.json; init stamps it
  into the run's progress.json and --status shows it. When it is
  none, tier 1 runs the self-review fallback with explicit user
  approval (rule 16 presents the choice). Never invent an identity.
  The gate refuses template placeholders, and a faked judge poisons
  every report built on it.

Protocol per run:

1. Tier 0 passes, then the judge runs at the tier above and writes its
   gate's own file from the review-report template (`review-report-step_3.json`
   for tier 1 full, `review-report-step_4.json` for the tier 1 delta,
   `review-report-step_audit.json` for tier 2): verdict,
   per-dimension scores, every flagged sentence, judge identity, tier,
   scope, and a rules_audit — one entry per quote or measure rule of
   the judged artifact's step (the `quote` and `measure` rows of that
   step in `references/rule-digests.md`), each with a verdict: quote
   entries carry a span copied verbatim from the judged artifact,
   measure entries state the measurement with its number. An approved
   report requires every rules_audit verdict pass. Format
   exemplars: `examples/review-report-gold-approved.json` (the
   step_4 delta gate's approved shape), `examples/review-report-gold-needs-fixes.json`
   (the step_3 full report at flag time; fails the gate by design) and
   `examples/review-report-gold-tier2.json` (the step_audit peer pass;
   rules scoped to the judged letter). The approved step_3 shape is
   deliberately not a separate exemplar: it is the needs-fixes file
   flipped, verdict approved with every flag resolved. The word-budget
   measure entry flips with the honest outcome, not a rubber stamp: the
   Tyro v1 shipped at 1,187 words with the user's growth approval, so
   the flipped entry passes with that number and the approval recorded
   (the gate recomputes the artifact and checks both).
   Reports accumulate: every gate keeps its own file, the tier-2 peer
   consumes the earlier ones, and each stays independently verifiable
   against its own artifact at the audit. Each gate reads only its own
   file, so an earlier approval stays valid after later gates run;
   re-doing an earlier step rewrites that step's report, and the later
   gates' approvals must then be re-earned.
2. Fix every flagged item; re-judge; re-judge rounds are capped at 2 per gate.
   Anything still contested escalates to the human checkpoint.
3. The gate is mechanical: `verify_artifacts.py --artifact review-report`
   fails a missing or unapproved report, an incomplete rules_audit, or an
   audit whose quotes are not verbatim in the judged artifact (quotes are
   verified against the artifact named in the report's own `artifact`
   field when it sits next to the report; pass `--artifact-path` to
   override), and `progress.py --approve`
   checks the gate's run-state requirements on top of that shape:
   tier, scope, the judged artifact, and that the report's `step`
   names the gate it was written for.
   blocks step_3, step_4 (substantive changes only), and step_audit
   without it. Enforcement lives in scripts, not memory.

Every judge run is one exhaustive structured pass (all dimensions scored,
every flagged sentence listed) so re-runs stay minimal.
