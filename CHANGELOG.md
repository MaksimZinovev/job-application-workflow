# Changelog

Rule governance log for the `job-application` skill. One entry per retro
batch: activation date, provenance, the rule list with the learning each
one encodes, and notes on reconstructed files.

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
