# Run progress — <NN_slug>

Human checklist for one application run. The machine state lives in
`progress.json`; `progress.py` is the only writer. Check a box only when
the matching step is approved in `progress.json`.

- [ ] step_0 — context: preflight sources, init run folder (`references/operating-principles.md`)
- [ ] step_1 — JD analysis, rubric scoring, promotion gate (`references/jd-analysis.md`)
- [ ] step_2 — matches.md lists + gaps + rubric-validated paragraph plan (`references/matches-and-plan.md`)
- [ ] step_3 — cover letter v1 + Tier 1 judge (`references/cover-letter-writing.md`)
- [ ] step_4 — unslop + better-cover-letter-writing passes, v2, conditional delta judge (`references/writing-passes.md`)
- [ ] step_audit — full verify matrix + Tier 2 peer judge (`references/operating-principles.md`)
- [ ] step_retro — run-log distillation + batch rule approval (`references/retro-and-run-log.md`)

Steps 5-7 are reserved for the resume-and-prep companion skill and never
appear in a run of this skill.
