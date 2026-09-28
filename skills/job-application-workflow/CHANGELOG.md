# Changelog

Rule governance log for the `job-application` skill. One entry per retro
batch: activation date, provenance, the rule list with the learning each
one encodes, and notes on reconstructed files.

## 2026-09-28 — the repo becomes a skills container; the writing skill moves in

- **Provenance:** user-directed restructure. The repo root now holds
  only `skills/`. The workflow skill is complete and unchanged inside
  `skills/job-application-workflow/`: SKILL.md, rules, references,
  assets, scripts, examples, agents, and plans all moved as one tree,
  so every relative path inside the skill still resolves. Scripts
  anchor on their own file location, which the move preserved.
- **better-cover-letter-writing** moved from
  `~/repos/wiki/.pi/skills/` to `skills/better-cover-letter-writing/`
  (SKILL.md, assets/patterns.md, scripts/init.py; no .DS_Store). The
  workflow's sources.json now points its `better_cover_letters` key
  here, the README's symlink instructions and the wiki's
  project-local `job-application` symlink target the new nested
  path, and the wiki's superseded pointer names the new path. The
  wiki copy is removed.

## 2026-09-26 — queue item: root README caught up; wiki draft marked superseded

- **Provenance:** queued staleness. The README still named a SKILL.md
  line count and a rules count that had both moved, its folder tree
  missed cover-letter-template.md and the tier-2 judge exemplar,
  matches-gold was described as curated though it is verbatim, and the
  wiki's first workflow draft carried no sign that it is superseded.
- **What changed:** the tree lists every file (checked mechanically
  against the directories; nothing missing, nothing phantom); the
  rot-prone counts are gone from the tree (the digest and
  rules/README are the live sources for rule counts);
  matches-gold and the examples paragraph say verbatim; the
  how-it-works item 1 now records the judge-capability preflight;
  and the wiki's master-templates/workflow.md opens with a
  superseded note pointing at this skill.
- Checked and deliberately not changed: the "like the unslop skill"
  example in Setup (unslop_skill is a real optional source key);
  the Usage dialog lines and other pre-session wording.

## 2026-09-26 — queue item: the gate redoes the math on measure rules

- **Provenance:** queued after the fix series, in three parts. A
  measure rule's proof was a number typed by hand, and the gate
  only checked that a digit exists. The only exemplar showing the
  measure kind fails on purpose, so nothing anywhere showed a
  passing measure entry. And the digest printed today's date on
  every rebuild, so a rebuild that changed nothing still showed a
  diff (it reached a commit once).
- **Recompute:** scripts/rules_meta.py gains measure_artifact(),
  the single place that measures an artifact against its budget
  (letter words Dear-to-signoff, the Scoring Results section's
  chars, matches.md content chars). Both gates call it and check
  three things: the stated number must match the computed value
  (plain or comma format), a pass over budget must record the
  user's growth approval in the evidence, and a fail on an
  under-budget artifact is refused. verify_artifacts checks judge
  reports; check_rules checks the writer's check files. All four
  refusal paths tested live, plus the pass path.
- **The flip teaching is now true end to end:** the honest passing
  measure entry exists. The Tyro v1 shipped at 1,187 words with
  the user's growth approval, so the flipped needs-fixes file
  passes the step_3 gate with verdict pass and that number
  recorded (proven live: the flipped file verifies clean). The
  flip teaching in the exemplar note and operating-principles now
  says this: the word-budget entry flips with the honest outcome,
  not a rubber stamp. The needs-fixes file keeps its fail entry;
  it is the state at flag time, and it recomputes consistently.
- **Digest no-op:** build_digests now compares the rebuilt content
  against the file on disk, ignoring only the header line. A
  rebuild that changes nothing prints "ok: digest unchanged" and
  writes nothing (proven: two rebuilds, one write).
- **Unslop completion:** the earlier sweep missed check_rules.py,
  rules_meta.py, and build_digests.py, which were not in the
  grep. Every em dash in lines written this session in those
  files is now a period or a comma, including the generated
  digest's header comment and step headers. The empty-value dash
  markers never fire (checked) and stay.

## 2026-09-26 — follow-up: the template decides, the gold's omissions named (alpha fix-5)

- **Provenance:** alpha's fix-5 minor 2, queued: the structure-parity
  check diffs against two files that disagree. matches-gold has 6 of
  the template's 12 sections, and a reader diffing both hit the gap
  with no explanation.
- **Resolution:** the template wins, and the gold is a real run's
  file. The Tyro run predates the template (delivered 2026-09-11,
  the template was written 2026-09-17), and the gold's body is
  verbatim by the gold rules, so the missing sections are history,
  not error. rule-structure-parity now says: when the two files
  disagree, the template wins, because every run starts from its
  stub; the gold shows what filled sections look like, and its
  header lists what it omits. matches-and-plan.md's precedent
  pointer says the same in one sentence.
- **Teaching error fixed while in the header:** the gold's "Read
  for" list claimed the question-to-section map and the wireframe
  plan, which the file does not contain (a header error from the
  session that built the examples). Both dropped, the honest-gap
  framing added (the file's strongest teachable feature), and the
  map and wireframe named as step_2 checkpoint output in the
  header note.
- **Gate bug found and fixed while writing the header:**
  check_matches counted the whole file, comments included, so the
  new note pushed the gold to 10,226 chars against its 10,000
  budget and the gate failed it. The letter check counts only the
  salutation-to-signoff body and the scoring check only the
  Scoring Results section; matches now measures content after
  HTML comments, like its siblings. Proven both ways: a
  5,000-char comment with under-budget content passes, and a tiny
  comment with over-budget content fails on content (10,991 chars
  reported). Real runs carry no comments, so nothing changes for
  them. The gold passes at 8,991/10,000 content chars.
- Digest regenerated: the 3 structure-parity rows (steps 1-3).
  The gold's body is still verbatim against the wiki file
  (checked mechanically); the exemplar battery and the letter
  check are unchanged.

## 2026-09-26 — mechanism fix: judge instantiation defined, placeholders refused (peer review, fix 6)

- **Provenance:** major issue 6 of the peer review. No defined way
  to instantiate the fresh-context or tier-2 judge, and the
  gate-clearing exemplar passed with a placeholder identity
  (verify only checked non-emptiness).
- **What changed:** operating-principles.md gains "Instantiating
  the judge": per-kind recipes (subagent opens a second agent
  session sharing nothing with the drafting conversation;
  different-model is the same recipe with a different model;
  peer-agent is a second agent on the same machine or hub, never
  a session that watched the drafting; self-review is the
  disclosed fallback), the review inputs the judge receives
  (artifact, matches.md, locked criteria, resolved
  better_cover_letters, report template, the judged step's digest
  rows), what the independent judge never receives (the drafting
  conversation, the writer's intentions, the chat history), and
  the capability check as a preflight fact. Never an invented
  identity.
- **Teeth:** verify_artifacts.py refuses template-shaped identities
  (angle brackets), judge kinds outside subagent/different-model/
  peer-agent/self-review, and non-date dates; progress.py mirrors
  the placeholder refusal at --approve. Both layers tested:
  placeholder identity, bad kind, placeholder date, and empty
  identity all refused; real values accepted.
- **Exemplars:** the three constructed exemplars replace the
  template placeholder with an honest identity ("constructed
  exemplar, no real judge") plus a note sentence saying a real
  report names the model or agent that judged; the template keeps
  its placeholders (correct there) and its notes now state the
  requirement and point at the recipe.
- **After the user's annotation on the fix-6 handover (same day):
  the "fresh-context self-judge" concept is gone. It was
  incoherent: a fresh context is a separate agent and session,
  not a self. Tier 1 is an independent judge by default (subagent,
  separate agent session, or peer, whichever the harness has);
  kinds are subagent | different-model | peer-agent | self-review.
  Preflight now asks and records judge_capability
  (preflight.py --judge-capability, stored in sources.json,
  stamped into progress.json at init, shown by --status); when it
  is none, tier 1 falls back to a self-review, recorded as such
  and approved explicitly by the user at the checkpoint. SKILL.md
  step_0 and README's judge phrase updated; the two tier-1
  exemplars now teach kind subagent.

## 2026-09-26 — mechanism fix: dead workflow numbering in rule bodies (peer review, fix 5)

- **Provenance:** major issue 5 of the peer review. Four rule bodies
  still cited the superseded wiki workflow's item numbers (1.3, 1.4,
  1.5, 1.7, 1.8, step 2.1), unresolvable to today's reader, and
  build_digests amplified two of them into every step's read
  (rule-checkpoint-interview-tool has no expect field, so its Rule
  prose, with the "1.3 promote decision", became the digest expect
  at all seven steps).
- **What changed:** the promote decision cites step_1 (SKILL.md names
  that checkpoint "promotion gate"); the hidden-question paragraph
  cites the step_2 key questions in matches.md; the 07 incident
  narrative keeps its facts and drops the four item numbers (the
  named sections, Keywords Tools, soft-skills mapping, gaps List 3,
  and employer questions, all still exist); structure parity now diffs
  against the skill's own step template and gold example instead of
  the wiki example path and the "workflow item list", and the letter
  diff cites the key-questions mapping in matches.md; word-budget
  drops its two item numbers and its dead "workflow step 2.1"
  pointer, replaced by the live truth (budgets live in
  assets/sources.json word_budgets; verify_artifacts.py enforces
  them).
- **Digest:** regenerated. 10 rows changed, exactly the two
  amplified rules (checkpoint-interview-tool at all seven steps via
  Rule-prose fallback, structure-parity at steps 1-3 via expect);
  the other 19 rules' rows byte-identical. No applies_to, evidence
  kind, or type touched.
- Checked and deliberately not changed: references/jd-analysis.md's
  budget pointer (assets/sources.json word_budgets, verified
  accurate); the needs-fixes exemplar's word-budget entry (the
  1000-word default is live); the "question-to-section map" phrases
  in matches-gold and run-log-gold annotations (generic descriptions
  of content, not dead pointers).
  After alpha's re-review (pass with notes, same day): the sweep had
  missed the unnumbered pointer variant. word-budget's expect still
  said "the budget the workflow states" (digested at steps 1-3,
  contradicting the rule's own new sources.json sentence one
  paragraph below it) and its incident line "the 10K budget the
  workflow sets"; expect now points at assets/sources.json
  word_budgets and the incident clause dropped. checkpoint-tool's
  "Applies to every gate" (the list is checkpoints, not gates;
  amplified at all seven steps) became "Applies at every step".
  Queued per alpha's minor 2: the gold/template section divergence
  it surfaced (matches-gold lacks the template's Employer
  questions, Key notes, key-questions mapping, writing plan, and
  Mapping List 3. Reconcile in a later batch, or state that the
  template decides and the gold's header lists its omissions.)

## 2026-09-26 — mechanism fix: rules/README describes the corpus as it stands (peer review, fix 4)

- **Provenance:** major issue 4 of the peer review. rules/README.md
  still described the active corpus as a one-time review draft: the
  header said "draft for review", the inventory table carried the
  pre-remap step wiring (contradicting the frontmatter, digest, and
  SKILL.md wiring in 14 of 19 rows), the intro pointed at the
  superseded wiki workflow.md, and "How to review" instructed the
  user through the completed retro-#1 approval form.
- **What changed:** header and intro reframed (the corpus is active
  and gate-wired via the digest and the per-rule loop; origin kept
  as history; the wiki workflow.md named as superseded by SKILL.md);
  the inventory table rebuilt from live frontmatter with all 21
  rules and a "frontmatter is the truth source" note; the format
  table's inventory row describes the numbering (the retro-#1
  extraction table is no longer in the repo) and the expect row
  reflects reality (every check rule carries one; the protocol rule
  example-maintenance also does); the 25-line claim replaced with
  the measured 30-45; "How to review" replaced by "How rules change",
  the standing retro loop (at most 5 proposed rules per sweep,
  proposed stays out of the digest and gates, approval flips status
  and last_validated and lands a CHANGELOG entry, examples checked
  in the same batch per rule 21); "Not here yet, by design" became
  "Elsewhere in this repo".
- **Frontmatter:** rule-context-per-evidence and
  rule-example-maintenance (both from the 2026-09 skill-review
  session) had collided with retro-#1 numbers 1 and 2; renumbered
  to the next free numbers 20 and 21 by session arrival order. No
  other frontmatter touched; `inventory` is parsed by nothing, and
  the digest is unchanged (verified).
  After alpha's re-review (pass with notes, same day): the intro's
  "wired into the step gates" softened to "wired into the workflow's
  steps" (step_0 and step_retro rules have no gate, only the check
  loop); the evidence row no longer implies a check-type-only field
  ("the proof the check loop demands"); the inventory row's "20, 21
  so far" reworded as the dated fact "the 2026-09 batch took 20 and
  21" (a historical statement cannot rot); "How rules change" now
  names its canonical definition (references/retro-and-run-log.md),
  which "Elsewhere in this repo" also lists.

## 2026-09-26 — mechanism fix: per-gate report storage + artifact pin (peer review, fix 3)

- **Provenance:** major issue 3 of the peer review, plus the fold-ins
  alpha named in its fix-2 re-review: one review-report.json path meant
  each gate overwrote the last, so "accumulated review reports" was
  aspirational; and no gate pinned which artifact its report judges.
  Fixed after user review.
- **Action:** every gate keeps its own file, review-report-<step>.json
  (step_3 tier-1 full on v1, step_4 tier-1 delta on v2 when
  substantive, step_audit tier-2 delta on v2). init_application stubs
  the per-gate names into expect_artifacts and pins the judged
  artifact per gate; progress.py reads only its gate's file and
  refuses a report that judges the wrong artifact (closes the
  down-scoped gaming path from alpha's fix-2 review), and --status
  prints a judge-gate line per reporting step. The step_audit matrix
  verifies every accumulated report against its own artifact (the
  fix-2 auto-resolve makes each verify flagless next to its letter);
  the tier-2 peer consumes review-report-step_3.json and
  review-report-step_4.json by name. Reports accumulate and each gate
  reads only its own, so an earlier approval stays valid after later
  gates run; re-doing an earlier step rewrites that report and later
  approvals must be re-earned (documented in operating-principles).
  SKILL.md, operating-principles, both run-log templates, the report
  template and README updated; the gold run-log annotation and the
  tier-2 exemplar note now name the real files. Propagation fix
  folded in: operating-principles item 3 still described the quote
  guard as opt-in after fix 2 made it default-on.
  After alpha's re-review (same day): the approved exemplar re-shaped
  to the step_4 delta gate's true shape (scope full → delta; it now
  clears the exact gate its _exemplar names, and the needs-fixes
  exemplar teaches the step_3 flip instead of pointing across gates);
  the report's step field must name its gate; the previously-dead
  "trigger" key is consumed by progress.py (the step_4 condition is
  data now, not a hardcoded id); the report filename is derived in
  build_progress and never spelled as a literal anywhere; the
  missing-file refusal names the legacy rename; unpinned run states
  print a non-blocking notice instead of degrading silently; --status
  prints "judge gate: skipped" when step_4's delta judge must not run.

## 2026-09-26 — mechanism fix: tier-2 audit scoped to the judged artifact (peer review, fix 2)

- **Provenance:** the peer review of the 2026-09-24 session
  (agents/peer-review-alpha-2026-09-24.md, major issue 2): step_audit
  carries no quote or measure rules, so a tier-2 report's rules_audit
  had to be empty, so the independent final judgment was mechanically
  verified for nothing, and a conscientious judge writing letter
  entries failed the gate. Fixed after user review.
- **Action:** the rules_audit scope now derives from the report's
  `artifact` field (the inverse of STEP_ARTIFACTS in rules_meta.py),
  falling back to `step`. A tier-2 report runs at step_audit but
  judges cover-letter-draft-v2, so its rules_audit covers step_4's
  five quote rules, quotes verified against v2; an empty rules_audit
  fails the gate, and a report whose scope resolves to no quote or
  measure rules fails with "audits nothing". New teaching exemplar
  `examples/review-report-gold-tier2.json` (constructed like its
  siblings; the run predates the tiered protocol). SKILL.md step_audit
  item 4, the operating-principles judge protocol and the report
  template's tier guide state the scope rule. Quote verification is
  now default-on: with no --artifact-path the gate resolves the
  report's own `artifact` field against the report's folder, degrading
  to a note only when that file is absent (exemplars verified from
  examples/ keep working), and an artifact that names no step artifact
  fails by name; SKILL.md step_3 and step_4 now verify the report
  right after each judge runs, closing the chain gap where a fabricated
  tier-1 audit could pass progress.py and be overwritten before any
  script ever saw it. No rule wiring changed; the digest is untouched.
  Both tier-1 exemplars behave exactly as before (their artifact
  fields resolve to their own steps).

## 2026-09-25 — mechanism fix: evidence kinds made explicit (peer review, fix 1)

- **Provenance:** the peer review of the 2026-09-24 session
  (agents/peer-review-alpha-2026-09-24.md, major issue 1): the gate
  demanded verbatim quotes from rules whose proof cannot be a pasted
  sentence, teaching ritual compliance. Fixed after user review.
- **Action:** three evidence kinds replace the two-kind type inference.
  Every active rule now declares `evidence:` in frontmatter (12 quote,
  8 confirm, 1 measure). `rule-word-budget` is the measure kind: the
  proof is the measurement with its number, stated in the note field
  (writer loop) or the evidence field (judge audit); the gate requires
  a digit there. `rule-defer-to-team-knowledge` is unwired from step_1
  (its own prose applies it from matches.md onward; scoring.md carries
  nothing it could quote) and its `applies_to` matches the new wiring.
  build_digests now fails on a missing or unknown `evidence:` field, on
  a quote/measure rule wired at a step without an artifact, and on
  `applies_to` disagreeing with the SKILL.md wiring; the writer's gate
  bails on an evidence-less rule file too, and the rule-file format
  tables (rules/README.md, retro-and-run-log.md) gained the `evidence`
  row in the same batch, with the missing status and last_validated
  rows restored. The needs-fixes exemplar's word-budget audit entry
  dropped its ritual quote: the measurement in its evidence field was
  already the honest proof; measure entries may carry an optional,
  verified quote. Review-report schema stamped @3 (the rules_audit
  shape changed: quoteless measure entries). Digest regenerated
  (21 rules; step_1 now lists 9).

## 2026-09-24 — retro #2: skill-review batch (2 rules)

- **Provenance:** the 2026-09-24 skill-review project (chunks (iii)-(iv)):
  the mitti-letter review rounds and the teaching-layer build, plus the
  user's approval. Activated in batch after user review.
- **Action:** both proposed rule files flipped `status: proposed →
  active`; `last_validated: 2026-09-24` set on each.
  `rule-context-per-evidence` wired into the step_3 and step_4 rule
  lists (check rule, quote-guarded in the loop);
  `rule-example-maintenance` wired into the step_retro list (protocol
  rule, confirmation-guarded). Digest regenerated (21 active rules).
  Affected examples checked in the same batch, per the new rule itself:
  both judge exemplars gained their rule-context-per-evidence audit
  entries (quotes verified against the real letters); the paragraph
  rubric's failure gallery now cites the rule by name.
- **rule-context-per-evidence** — every evidence sentence names who did
  the work, where, and what changed; facts from different roles never
  share a sentence. Learning: the 06 letter shipped a claim with no
  context, then a fix with context but no author; the third version
  passed because it named all three.
- **rule-example-maintenance** — when a rule batch changes a rule, the
  examples that teach it are checked and updated in the same batch.
  Learning: the teaching layer was built to encode the rules; silent
  drift would make it teach the wrong thing.

## 2026-09-17 — retro #1: initial batch activation (19 rules)

- **Provenance:** 07 Reo Group + 08 Peoplebank application runs, plus the
  user's standing directives. Extracted, reviewed, and corrected over the
  2026-09-08 to 2026-09-16 sessions; activated in batch after user review.
- **Action:** all 19 rule files flipped `status: proposed → active`;
  `last_validated: 2026-09-17` set on each. `applies_to` remapped to the
  canonical step ids (old step_1 scoring part → step_1, matches/question
  part → step_2; old step_2 → step_3; old step_3 → step_4; old plan
  extraction/resume/interview-prep steps → reserved step_5/6/7). Prose
  untouched — metadata-only change.
- **Detail: reconstructed** — 8 files carry partially rebuilt Learned-from
  narratives (incident real, specifics may be off): rule-word-budget,
  rule-copy-at-end, rule-tense-from-cv, rule-ownership-calibration,
  rule-name-projects-attribute-companies, rule-read-sources-first,
  rule-defer-to-team-knowledge, rule-richness-for-cuts. Check these
  hardest when a future retro revisits them.

### Rules in this batch (one-line learning each)

1. rule-structure-parity — diff output structure against the example file
   before delivery.
2. rule-word-budget — write to the stated budget, verify once, trim once.
3. rule-copy-at-end — copies are the last action; re-verify after any
   post-copy mutation.
4. rule-tense-from-cv — tense comes from the CV source of truth, never
   from precedent letters.
5. rule-ownership-calibration — ownership verbs must match org-context
   records.
6. rule-user-memory-outranks-records — verification ends at a primary
   source; user memory wins over stored records.
7. rule-corrections-propagate — a correction lands in every artifact and
   flags the source record.
8. rule-scale-labeling — evidence scale matches claim scale; side projects
   are labeled.
9. rule-name-projects-attribute-companies — name projects, attribute
   companies, cite concrete scale.
10. rule-read-sources-first — every step-0 source read before writing, each
    with its downstream function.
11. rule-defer-to-team-knowledge — how-I-would-start defers to existing
    team knowledge before proposing changes.
12. rule-no-enumeration-colons — colon-into-enumeration is an AI tell;
    rewrite as first-person process.
13. rule-pattern-sibling-scan — fix the flagged instance, surface siblings,
    never silently edit approved prose.
14. rule-label-vs-enumeration-colon — label colons are normal usage; only
    enumeration colons are tells.
15. rule-preflight-resource-check — verify referenced skills, templates,
    and files exist before steps depend on them.
16. rule-checkpoint-interview-tool — decision checkpoints use the question
    tool, with alternatives and a recommendation.
17. rule-lint-classify-once — house-style lint classes are classified once
    via precedent, not re-litigated.
18. rule-richness-for-cuts — keep evidence only if it closes a keyword hole
    or supports the role shape.
19. rule-artifacts-on-disk — every step lands its output on disk before its
    checkpoint closes.
