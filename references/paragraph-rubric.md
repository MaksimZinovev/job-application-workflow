# Paragraph rubric — a story that answers its hidden question

Use while planning (step_2) to decompose hidden questions and assign
evidence, and after writing (step_3, step_4) to assess every body paragraph.
This file is the judge's locked criteria source for the rubric dimensions.

## Before writing — decompose the hidden question

For each hidden question from matches.md:

1. Quote the ad bullet the hidden question derives from, verbatim.
2. Split it into 2-4 sub-questions, each traceable to that wording (quote or
   paraphrase the JD phrase beside it). A sub-question with no JD wording
   behind it is an invention and fails, however sensible it sounds.
3. Assign at least one evidence piece per sub-question. If a sub-question has
   no evidence, mark it `intent-only` explicitly. A silent hole is the only
   invalid answer.
4. Run the **anywhere-company test** on each candidate evidence: would this
   sentence impress an employer with the opposite working model just as much?
   If yes, it answers "is a good engineer", not this question.

## Rubric (per paragraph)

Score every body paragraph. A paragraph is the unit; the rubric applies
while writing (guidance) and after writing (assessment).

| # | Dimension | Fail | Partial | Pass |
|---|-----------|------|---------|------|
| 1 | Question coverage | A sub-question has no sentence addressing it | All touched, one only vaguely | Every sub-question has a dedicated sentence/clause |
| 2 | Source fidelity | Sub-question untraceable to the ad's wording, or evidence fails the anywhere-company test or contradicts the role's model | Traceable but the link needs the reader to squint | Every sub-question and its evidence visibly belong to this ad's question |
| 3 | Demonstration | Trait asserted, no interaction or outcome ("My reviews flagged oversized PRs") | Action shown, outcome missing | Who + action + outcome visible ("I flagged X early; we landed the fixes before merge") |
| 4 | Story continuity | Stacked facts; reads as bullets without the subhead | Mostly connected, one seam | One arc; each sentence grows from the previous |
| 5 | Evidence economy | Snippet repeats the table or another paragraph, or floats unlinked to its claim | One weak or duplicated snippet | Every snippet is new, placed, and visibly earns its spot |
| 6 | Reader ease | Assessor must infer the fit | Answer findable but generic or buried | Skim test: the sentence answering each sub-question is underlineable in one pass |

## The 2-minute check (after writing)

- Tag each sentence with the sub-question it answers, and each sub-question
  with the JD phrase it derives from.
- A sentence whose chain ends at a sub-question with no JD phrase is
  decoration or invention — cut it.
- An untagged sentence is decoration: cut it or reconnect it.
- Two sentences with the same tag: merge or differentiate them.
- Read the tags alone: if they do not add up to the hidden question, coverage
  is broken regardless of prose quality.
- Anywhere-company probe: any sentence that would survive unchanged in an
  application to a differently-modelled company is not answering the
  question.

## Worked example — two rounds on one paragraph

Round 1, paragraph P3 ("squad fit in Scrum"), the demonstration failure:
sub-questions as then listed: rhythm / role / interpersonal. The sentence
"My reviews flagged oversized PRs and flaky tests from other teams" scores
Fail on Demonstration (asserts an honest reviewer, no who or outcome) and
Fail on Reader ease (the squad-fit link is left to the reader). The round-1
fix — "In PR reviews with the developers and offshore engineers, I flagged
oversized PRs and flaky tests early, and we landed the fixes before merge" —
fixed the prose but not the question.

Round 2, the invented sub-question: "Interpersonal fit" sounded plausible,
but no ad wording backs it. The evidence chosen for it ("called out oversized
PRs", "weekend production rollouts") is true and demonstrated, yet fails
Source fidelity: both would impress a waterfall employer equally, and weekend
big-bang releases contradict Scrum's small increments. Re-anchored to the
actual bullet ("Demonstrable testing within an Agile delivery model,
preferably Scrum"): sprint cadence, cross-functional collaboration, shared
ownership across testers, analysts and business.

Moral: check the sub-questions against the ad before scoring the prose
against the sub-questions.
