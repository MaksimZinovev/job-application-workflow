# Alpha peer review: BCLW JIT rules and finish gate (2026-09-28)

Reviewer: alpha (peer agent, own /tmp scratch, repo untouched). Scope:
commit 158b540 plus the uncommitted self-review pass. Verdict:
pass with notes. Condensed from the full reply; the reply lives in
the session log.

## What alpha verified itself

- All my claims reproduced: selftest, the Peoplebank pass audit
  (16/16, honest acceptable scores visible in the artifact), the
  Tyro refusal probe (key role x1, todo x2), uniform frontmatter
  contract across all 16, heading unification, the +75/-35 diff.
- Its own probes on a /tmp copy of the skill: the arrow rule is
  sound (before-versions exempt, one real span after the last
  arrow required, whitespace-normalized), strict level matching,
  coverage minimums, confirm hygiene, header binding all work.

## Major 1 (landed): the evidence contract was not enforced

Any non-quote, non-confirm evidence string closed a row. Probes
that passed exit 0 before the fix: "swept all grand claims away.",
"ok", and curly-quoted spans the ASCII regex never saw. Fix landed
in evidence_refusal: refuse evidence with neither a quoted span nor
a confirm prefix, normalize curly quotes before span matching.
Selftest gained both cases; the gaming probe now refuses live.

## Minor findings (all landed)

1. A deleted rule file silently degraded enforcement to exit 0
   (verified live with rule 7 deleted and a trigger word in the
   letter). Fix: the structural-only branch is gone, replaced with
   die() on a missing rule file; yaml is now a hard import, the
   silent fallback parser is deleted.
2. Trigger census: keep the design. One narrowing taken: pattern
   12's todo trigger is placeholder-shaped now ([todo, todo:) so
   product-domain uses survive; the Tyro probe now refuses only on
   key role, which is the honest result.
3. SKILL.md index drift: pattern 11's pointer names its new
   example; pattern 8's pointer says the human review requirement
   lives in the ask and do-not notes; heading typos fixed (11
   double space and arrow spacing, 16 is now ### with the table's
   name "Intro paragraph (exec summary)").
4. Quality rubric said "refuses contradictions"; now says what it
   does: refuses a score below the rule's minimum.

## Alpha's answers to my questions

Contract honest and uniform; the arrow rule sound; the restructures
keep force (the positive Rule statements are stronger teaching than
the old Do-not duplicates); the rubrics exploit-resistant in the
sense that matters; SKILL.md as index loses nothing operational; the
audit table documents the loop, the checker verifies final state,
and no mechanical proof of the one-at-a-time process is possible or
needed. One claim in my request overreached: pattern 9 has no
before/after pair (its SKILL.md section never had one; left honest).

## Post-fix verification (mine)

Ruff clean, py_compile clean, selftest PASS (five plus two new
cases), thin evidence refused live, curly span passes live,
missing rule dies live, Peoplebank 16/16 exit 0, Tyro exit 2 on the
key role trigger alone, 16 frontmatters parse, no literal em dashes.
One cascade disclosed during the fix: a broken && chain made two
probe exits read as refusals when the fixture files were never
written; the fixtures were rebuilt and the probes rerun clean.