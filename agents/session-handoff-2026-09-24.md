# Session Handoff — 2026-09-24 · job-application-workflow skill review

Project: enhance the job-application skill with examples, a rule-loading
mechanism, and teaching material. Five chunks, all built, reviewed with
the user file-annotation by file-annotation, and committed.

## Verified Now

- What is currently working:
  - `scripts/build_digests.py` → `references/rule-digests.md`: 103
    lines, 21 active rules, 7 steps, zero warnings. Proposed rules are
    invisible at run time and reported on stdout.
  - `scripts/check_rules.py`: per-rule loop (`--next` one rule per
    attention window, `--gate` closes a step). Guards: verbatim quote
    for content rules, written confirmation for process rules,
    verdict/score consistency, fail→fix, siblings-checked, filler ban,
    threshold (`rule_check.min_score: 2`), stray files. Aggregates
    `<run>/rule-checks.json` for the retro.
  - `scripts/verify_artifacts.py`: all modes green — scoring, matches,
    cover-letter, review-report (rules_audit completeness + quote
    authenticity via `--artifact-path`), and the new `rule-check` mode
    (re-validates a step's check files at step_audit via the shared
    `check_rules.validate()`).
  - Rules: 21 active, 2 activated this session (rule-context-per-
    evidence at step_3+step_4; rule-example-maintenance at step_retro),
    wired into SKILL.md step lists, CHANGELOG retro #2 entry written.
  - Exemplars: approved judge report passes the full gate (5/5
    rules_audit); needs-fixes fails only by design (12/12 rules_audit
    valid; verdict + unresolved flags).
- What verification actually ran: ruff clean on scripts/; sandbox
  runs of every check_rules guard (happy path 15/15, each guard fired
  with the right message, including the substitution guards: quote
  cannot replace confirmation and vice versa); exemplar verifies with
  `--artifact-path` against the real wiki letters; 25/25 real quotes in
  the teaching files machine-verified verbatim; gold letter body
  byte-identical to the approved wiki v2 (re-checked after every
  annotation edit).

## Changed This Session

- Code or behavior added: chunks (i)-(v) —
  (i) `examples/` gold artifacts (Tyro letter with 6 seam annotations,
  matches, scoring, run log, two judge exemplars);
  (ii) rule-loading mechanism (rules_meta.py, build_digests.py,
  check_rules.py, verify_artifacts rules_audit, sibling-scan clause,
  every step runs the loop);
  (iii) craft teaching (before/after pairs for the 9 don'ts + labels +
  intro in cover-letter-writing.md; three-version failure gallery in
  paragraph-rubric.md; blind-trim-cycle entry in jd-analysis.md;
  workflow.md restorations: hidden-question derivation method, ranked
  linkage, ideal-candidate intro derivation, table purpose framing,
  inline don't examples);
  (iv) retro extension (worst-rules signal from rule-checks.json,
  wins→examples with diversity check, example maintenance) + two rules
  proposed then activated on user approval;
  (v) mechanical teeth (check_rules.validate() extraction,
  rule-check verify mode, gap gate learned "ramp", not-but hint fixed,
  gold annotation 3 updated).
- Infrastructure or harness changes: review protocol ran through
  `.local/` handover files (gitignored): review-chunk-i…v-handover.md
  with user annotation rounds; two commits: `237d1b0` (chunks i-iii),
  `2d95b8d` (chunk iv + activation + chunk v), branch
  `feat/enhance-examples-address-gaps`, tree clean before this
  handoff. Post-commit edits (uncommitted): retro cap 10→5 rules
  (references/retro-and-run-log.md + SKILL.md, user-directed) and this
  handoff file.

## Broken Or Unverified

- Known defect: none open. The gold letter's two remaining gate
  failures are documented seams by user decision (a): its own
  "not worked in, but" sentence and the 1050/1000 word budget.
- Unverified path: the whole mechanism has never run on a REAL
  application run — all testing was sandbox-based. rule-checks.json
  has no real scores yet, so the worst-rules retro signal has nothing
  to feed on until a run happens.
- Risk for the next session: README staleness (below) invites
  confusion; and the per-rule loop adds ~7-21 check files per run —
  watch that the first real run does not bloat context or runtime.

## Next Best Step

- Highest-priority unfinished feature: the two stale README facts, then
  the first real run through the upgraded skill.
- Why it is next: the README fix is two lines and keeps docs honest;
  the real run is the only unverified path left and it starts the
  learning loop (rule-checks.json scores, wins→examples nominations).
- What counts as passing: README matches reality (163 lines, 21 active
  rules); a real run closes every step gate green without manual
  intervention and lands rule-checks.json with real scores.
- What must not change during that step: the gold letter stays
  byte-identical (user decision (a)); the 1000-word budget stays (user
  decision); rules activate only through the retro protocol.

## Remaining todos (from the user-approved close-out list)

1. README staleness fix, queued for user go (no edits without it):
   "SKILL.md # operational spec, 137 lines" → 163 lines;
   "rules/ # 19 active rules + README" → 21 active rules.
2. BCL skill (better-cover-letter-writing) follow-up, separate project
   by user decision: per-pattern check loop for the 16-pattern audit
   table (same JIT design as check_rules.py), pattern #15 shallow-pass
   enforcement (the Revenue NSW incident).
3. First real run through the upgraded skill (validation + retro
   signal + first wins→examples nomination).
4. Optional, user call: deprecation pointer on the wiki's
   master-templates/workflow.md (superseded by this skill).
5. Superseded unless the user reopens: step_audit process-rule audit
   from run-log quotes (the all-rules confirmation design covers
   process rules at write time); peer-agent loop variant (Architecture
   B, optional experiment).

## Commands

- Startup: `python3 scripts/progress.py <run> --status` (resume any
  run); `python3 scripts/build_digests.py` (rebuild the digest after
  rule changes).
- Verification: `python3 scripts/verify_artifacts.py --artifact
  <mode> --path <artifact>`; `python3 scripts/check_rules.py <run>
  --step <step> --gate`; `ruff check scripts/`.
- Focused debug: `python3 scripts/check_rules.py <run> --step <step>
  --next --rule <rule-id>` (re-present one rule);
  `python3 scripts/verify_artifacts.py --artifact rule-check --path
  <run> --step <step>` (re-validate one step's checks at audit time).