# Peer review — alpha (glm-5.3-flash) · 2026-09-24

Session changes 237d1b0 + 2d95b8d; scripts were run, not just
prose-read.

## Major issues

1. **Quote guard vs unquotable rules, step_1 worst.** `needs_quote()`
   keys on rule type, not on whether the rule's subject exists in the
   artifact. Six step_1 rules demand scoring.md quotes: defer-to-team
   cannot bind there; word-budget is a measurement — the needs-fixes
   exemplar "proves" its violation with an empty span, ritual
   compliance the guard was built to prevent. Fix: per-rule×step quote
   map; note evidence for measurements; prune step_1.
2. **Tier 2 audit is vacuous.** step_audit has 0 content rules:
   rules_audit must be empty, SKILL.md's `--artifact-path` instruction
   verifies nothing, conscientious entries fail the check. Scope it to
   the judged artifact's step, or state the vacuity is intended.
3. **"Accumulated review reports" have no storage:** one
   review-report.json path; step_4 delta overwrites tier-1, tier-2
   overwrites delta. Name per-gate files or drop the claim.
4. **rules/README.md stale past the two known facts:** pre-remap wiring
   in the inventory table contradicting frontmatter/SKILL/digest;
   "draft for review" language; points to the superseded workflow.md.
5. **Dead "workflow 1.3/1.8" numbering in rule bodies**
   (checkpoint-tool, defer-to-team, structure-parity, word-budget),
   amplified into the digest on every step_0 read.
6. **Judge mechanism unspecified:** no defined way to instantiate the
   fresh-context / tier-2 judge; the gate-clearing exemplar passes
   with a placeholder identity.

## Ambiguities

step_2 checkpoint line lacks punctuation (misparse risk) · step_3 item
4 is incomplete, overlaps the Tier 1 judge · missing
`substantive_changes` silently means "no" instead of erroring ·
`min_score: 2` lets an all-borderline run pass, unstated · yaml step
blocks aren't valid YAML.

## Overengineering

53 rule slots per run; copy-at-end at step_1/2 forces an empty
confirmation; preflight-resource-check duplicates preflight.py's
exit-1 · two wiring truths (SKILL.md lists vs applies_to), no
cross-check · evidence-kind rule restated in ~6 places (10→5 cap
needed a two-file edit) · digest `built <today>` header = diff noise.

## Missing

No exemplar check file or rule-checks.json in examples/ · no
DO-NOT-PROMOTE example; `progress.py --approve step_1` never reads the
verdict line · no concrete Tier 1 judge input bundle.

## Minor

Exemplars stamp schema @1 (template @2, unvalidated) · keyword
coverage substring-matches ("ai" in "email") · FILLER ban can hit
legit "n/a" in quotes · check_report ignores run/artifact fields.

## Verdict

Strong core: shared validator, loud drift failures, by-design failing
exemplars, byte-identity discipline. Problems: ritual quotes where
artifacts cannot carry the rule, vacuous tier-2 audit, unsupported
accumulation story, doc drift. Fixable without redesign — best before
the first real run.