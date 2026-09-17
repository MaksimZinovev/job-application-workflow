# Job description analysis and scoring

Read when starting step_1. The job description lives in the run folder as
`job-description.md`.

## Read the context sources first

Read the configured sources before writing anything, and treat them as the
source of truth — never rely on facts remembered from previous applications:

- `job_search_context` (optional) — search context and constraints
- `ideal_job` (optional) — the ideal-role profile used later for hidden
  questions
- `rubric_full_time`, `rubric_part_time_gig` — the scoring rubrics
- `cv_master` — the CV source of truth for tense, facts, achievements
- `experience_records` — one or more evidence files: recent-role pieces plus
  prepared STAR stories (responsibilities, tools, soft skills, achievements,
  role context)

Each source exists to feed a specific later step; read it with its downstream
function in mind, and peek rather than ingest when a file is long. Missing
optional sources are flagged at preflight — the affected step adapts; missing
mandatory sources block everything until fixed or explicitly waived.

Resolve every key via the preflight table (`python3 scripts/preflight.py`)
or `assets/sources.json`; open the resolved file itself only when the step's
procedure calls for it. The rubrics and the ideal-role profile ship bundled
in `assets/` as working defaults; override with
`preflight.py --set <key> <path>` to score with your own.

The scoring template from init carries the exact format. If a look at a
past scoring file still helps, read one precedent, tail only.

## Pick the rubric by job class

- Full-time roles → the rubric configured at `rubric_full_time`.
- Platform gigs and salaried part-time roles → `rubric_part_time_gig`.

If the job class is unclear, ask the user before scoring.

## Scoring procedure

1. Understand the job description: the role, the stack, the environment, the
   outcomes the employer expects.
2. Score the job against the selected rubric, criterion by criterion.
3. Append a `Scoring Results` section to `scoring.md` (create from the
   scoring template at init). Hard cap: `word_budgets.scoring_results_max_chars`
   in `assets/sources.json` (default 5000 characters). The rubric id, one row
   per criterion, and a verdict line are required structure — the stub
   template carries their exact section names.
4. Use web search to enrich and ground the scoring: verify the company is
   real and what it actually does, the product's scale and claims, anything
   the rubric asks about employer context. Ground claims in what the search
   returns, not in assumptions. Five results per search is enough.
5. Run `verify_artifacts.py --artifact scoring --path <run>/scoring.md`.
   Exit 0 is required before the checkpoint.

## Promotion gate (checkpoint)

Present the scoring result and ask the user:

1. any feedback on the scoring itself;
2. whether to promote this job from scoring to application.

Only an explicitly promoted job proceeds to planning (step_2). No promotion,
no next step — record the decision in the checkpoint and stop.
