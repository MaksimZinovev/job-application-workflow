---
id: rule_context_per_evidence
inventory: 1
type: check
applies_to: [step_3, step_4]
expect: "every evidence sentence names who did the work, where, and what changed; facts from different roles never share a sentence"
on_fail:
  action: "rewrite with the record-grounded context, re-verify"
provenance:
  date: 2026-09-24
  app: 06_mitti
  source: "two review rounds on the 06 letter: claim without context, then context without author"
  detail: verified
status: active
last_validated: 2026-09-24
related: [rule_name_projects_attribute_companies]
---

## Learned from
The 06 letter shipped a claim-only opener ("I keep pipelines
trustworthy.") followed by a fact with no employer and no author. The
first fix attached the employer but still described company state, not
authored action — the reviewer asked "what does it have to do with me?".
The approved fix named who (I built), where (At Intellihub), and what
changed (on demand → daily), with every clause tracing to the CV
record. The full three-version sequence lives in the paragraph rubric's
failure gallery.

## Rule
Every evidence sentence passes three tests. Who — an authored action in
first person ("I built", not "scenarios run"). Where — employer or
project named, or inherited from an explicit transition in the previous
sentence. What changed — the outcome visible without the reader
supplying context. Facts from different roles never share a sentence.
Whether the fact belongs in the letter at all stays a separate,
evidence-economy decision.

## Rubric
- [ ] Every evidence sentence carries an authored first-person action
- [ ] Employer or project named, or an explicit transition in the prior sentence
- [ ] The outcome is visible without the reader supplying context
- [ ] No sentence carries facts from two different roles