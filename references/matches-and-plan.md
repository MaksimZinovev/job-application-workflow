# Matches and paragraph planning

Read when starting step_2, together with `paragraph-rubric.md` (which
validates the plan before any drafting). Only a promoted job reaches this
step.

## Build matches.md

Create `matches.md` from the matches template (stubbed at init). Resolve
every source key (`experience_records`, `cv_master`) via the preflight table
(`python3 scripts/preflight.py`) or `assets/sources.json`, and open the
resolved file only when the procedure below calls for it. Extract from the
job description:

- **Target roles** — what roles the ad is really hiring for
- **Keywords Skills** and **Keywords Tools** — the ad's own vocabulary,
  grouped; these feed keyword coverage later
- **Role type** — maintenance, all-rounder, framework-starter, mixed, etc.

Hard cap: `word_budgets.matches_max_chars` in `assets/sources.json` (default
10000 characters). Three lists follow, each capped in items:

1. **Mapping List 1 — recent role.** Match keywords to the most relevant
   records from `experience_records`: responsibilities, tools, soft skills,
   achievements, role context. 5-7 items.
2. **Mapping List 2 — previous roles.** Match keywords to records from the
   CV source of truth (`cv_master`). 5-7 items.
3. **Remaining gaps.** 3-5 items. Distinguish gaps coverable by previous
   roles or side projects from remaining gaps — skills that appear nowhere
   in the records. For remaining gaps, propose honest framing options (what
   is adjacent in the records, what is genuinely new territory).

List items cite their source concretely: name the project, attribute the
company, cite scale. Evidence scale must match claim scale, and side-project
evidence is labeled as such. Keep evidence only if it closes a keyword hole
or supports the role shape — richness for its own sake is cut.

## The hidden-question map

Extract the key questions the cover letter must answer. They map to letter
sections:

| # | Question | Maps to |
|---|----------|---------|
| 1 | Who is the ideal candidate? (years, role in team, fit with company maturity, established practices, expected outcomes) | Intro paragraph |
| 2 | What are the key requirements, with evidence backing each claim? | Evidence table |
| 3 | Primary hidden question, derived from the ideal-candidate profile's most important attribute(s) | 1st bold run-in subhead paragraph after the table |
| 4 | Secondary hidden question (2nd most important attributes) | 2nd run-in paragraph |
| 5 | Third hidden question, same approach | 3rd run-in paragraph |
| 6 | Honest reflection: gaps between the ideal candidate and this profile | 4th run-in paragraph — admit the gap, find the reasons and evidence why it closes rather than blocks |
| 7 | Any employer questions stated in the ad | 5th run-in paragraph |
| 8 | Outro: call to action + sign-off, working rights and availability, thanks | Closing paragraph |

The hidden questions derive from the ad's own wording. A question with no
wording behind it is an invention.

## Evidence ranking

For each hidden question, list and rank evidence:

**direct evidence > closely transferable evidence > indirect evidence >
claim without evidence.**

This prevents choosing an impressive-sounding but weak example. Mark any
sub-question whose only support is intent as `intent-only` explicitly; a
silent hole is the only invalid answer.

## Plan the letter

- Outline the writing plan and 1-2 alternatives for each section — a
  wireframe, not full details.
- Load `paragraph-rubric.md` and validate the plan before drafting:
  decompose each hidden question into 2-4 sub-questions traceable to ad
  wording, assign evidence to each, sketch each paragraph arc.
- Run `verify_artifacts.py --artifact matches --path <run>/matches.md`;
  exit 0 is required before the checkpoint.

Checkpoint: present matches.md and the plan with alternatives; wait for
feedback and approval before drafting.
