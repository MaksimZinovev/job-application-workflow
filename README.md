# job-application

Score the job, plan the evidence, draft the letter, rewrite it until it sounds like a person, prove every artifact with scripts. You approve each step. Nothing advances without you.

## How it works

Scripts do the grunt work. Preflight, run setup, gates, and checks are deterministic Python and cost no tokens. The LLM reads facts and writes prose. Every step ends at a checkpoint you control.

1. Preflight resolves your sources from `assets/sources.json`. A missing mandatory file blocks the run until you fix the path or waive it on record.
2. Score the job against your rubric, grounded by web search. You decide: promote this job to application, or stop.
3. Build matches.md: keywords against your experience records, lists capped, gaps named honestly. Plan each paragraph from a hidden question the ad implies. The rubric validates the plan before any drafting.
4. Draft v1. Mechanical checks run first: em dashes, clichés, keyword coverage, word budget. A fresh-context judge then scores it against the six-dimension paragraph rubric and writes `review-report.json`.
5. Rewrite to v2: unslop pass for human voice, credibility pass for honest verbs. v1 stays on disk forever. Substantive changes trigger a delta judge; small fixes skip it.
6. Final audit: full verify matrix plus a peer judge, delta-based. The retro distills the run log into proposed rules for the next application.

## Usage

**Start a new run**

> **You:** I want to apply for this: ~/Downloads/jd-acme.txt
>
> **Assistant:** Preflight first. All sources resolve, so I created run folder `12_senior-qa-engineer-acme` and copied the JD in. I read the context sources and scored the ad against the full-time rubric. Here is the Scoring Results table. My verdict: promote. Any feedback, and do you want to promote this job to application?

Actions: preflight, run init, sources read, scoring.md written and verified, promotion gate asked.

**Resume after a break**

> **You:** where was i on the Acme application?
>
> **Assistant:** Reading the gate state. Step 2, planning, is in progress with no blockers. I will build matches.md from your experience records, then plan the paragraphs. Here is the plan with two section alternatives; pick one or adjust.

Actions: progress --status, references loaded, matches.md built and verified, checkpoint.

## Skill folder

```text
job-application-workflow/
├── SKILL.md                    # operational spec, 137 lines, orchestration only
├── scripts/                    # tiny CLIs, deterministic, no tokens
│   ├── preflight.py            # resolve sources; block on missing mandatory
│   ├── init_application.py     # create the run folder, stubs, gate state
│   ├── progress.py             # the machine gate; --status resumes any session
│   └── verify_artifacts.py    # tier 0 checks; exit 0 unblocks approval
├── references/                 # read just in time, one per step
│   ├── operating-principles.md  # checkpoints, no-fabrication, judge protocol
│   ├── jd-analysis.md           # rubric choice, scoring, promotion gate
│   ├── matches-and-plan.md     # keyword lists, hidden questions, evidence ranking
│   ├── paragraph-rubric.md      # 6 dimensions, decomposition, 2-minute check
│   ├── cover-letter-writing.md  # structure, per-paragraph guide, don'ts
│   ├── writing-passes.md        # unslop + credibility passes, flag semantics
│   └── retro-and-run-log.md     # run log convention, rule format, caps
├── assets/
│   ├── sources.json              # every path lives here; edit for your setup
│   ├── scoring-rubric-full-time.md    # bundled default, override via --set
│   ├── scoring-rubric-part-time-gig.md # bundled default, override via --set
│   ├── ideal-job-2026.md          # bundled ideal-role profile
│   ├── banned-terms.json         # cliche catalog, fail + review severities
│   ├── scoring-template.md       # scoring.md skeleton
│   ├── matches-template.md       # matches.md skeleton
│   ├── review-report-template.json # judge report schema
│   ├── progress-template.md      # human checklist
│   └── run-log-template.md       # raw-signal log skeleton
├── rules/                      # 19 active rules + README, learned from real runs
├── CHANGELOG.md                # rule governance log, one entry per retro batch
└── plans/                      # build-plan archive, not skill payload
```

## Output

Each run produces one folder under your `applications_root`, auto-numbered:

```text
12_senior-qa-engineer-acme/
├── job-description.md         # the ad, copied at init
├── scoring.md                 # rubric id, Scoring Results, verdict
├── matches.md                 # keyword evidence lists + honest gaps
├── cover-letter-draft.md      # v1, preserved forever
├── cover-letter-draft-v2.md  # after the passes
├── review-report.json        # judge verdict, tier, flagged items
├── progress.json              # machine gate state
├── progress.md                # human checklist
└── run-log.md                 # raw signals for the retro
```

The deliverable is `cover-letter-draft-v2.md` with its `review-report.json`. Everything else is traceable evidence behind it.

## Setup

```bash
ln -s ~/repos/job-application-workflow ~/.pi/agent/skills/job-application
# or project-local: ln -s ~/repos/job-application-workflow <project>/.pi/skills/job-application
```

Paths live in `assets/sources.json`. The rubrics and the ideal-role profile ship bundled in `assets/`; point `cv_master` and `experience_records` at your files, and override any bundled default with `preflight.py --set <key> <path>`. Optional sources, like the unslop skill, drop to degraded mode with a warning when missing.

## Design decisions

- Evidence beats vibes. Every claim traces to a configured source. Gaps stay gaps, framed honestly.
- Gates live in scripts, not memory. `progress.py` refuses to advance until dependencies are approved, artifacts exist, and the judge report says approved.
- Judge cost scales with risk. One full review after the first draft, delta reviews after substantive rewrites, a peer review at the audit. Small fixes cost nothing.
- Portable by config, not convention. One JSON file holds every path. Clone, edit, run.

Resume tailoring and interview prep belong to a future companion skill. This one ends at the approved letter.