# Goal

Turn `/Users/maksim/repos/wiki/notes/2026-applications/master-templates/workflow.md`
(the "Job application workflow - search, score, match, apply" master template)
into a high-quality agent skill following the skills-best-practices authoring
procedure (agentskills.io spec: validated metadata, progressive disclosure,
<500-line SKILL.md, scripts/references/assets structure).

Core behaviors that must survive the conversion:

- Checkpoint/milestone collaboration model (agent stops, waits for explicit approval)
- Scoring -> promotion-to-application -> matching -> cover letter -> unslop pipeline
- Evidence-based, no-fabrication writing rules (hidden questions, evidence ranking, paragraph rubric)
- Programmatic verification (word count, keyword coverage, em-dash count, character budgets, lint)
- Cross-references to companion skills: unslop, better-cover-letter-writing
- Existing learned-rules corpus at `~/repos/wiki/.pi/skills/job-application/rules/`
