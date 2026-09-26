# Changelog

Rule governance log for the `job-application` skill. One entry per retro
batch: activation date, provenance, the rule list with the learning each
one encodes, and notes on reconstructed files.

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
  had to be empty — the independent final judgment was mechanically
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
