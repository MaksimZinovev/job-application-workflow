<!--
GOLD EXAMPLE, matches.md (format precedent)

Source: run 10_quality-engineer-ai-12-months-contract-tyro, matches.md
(wiki). Verbatim: no curation needed; it passes the skill's own gate
(sections, list counts 7/6/4, under the 10,000-char budget) exactly as
the run wrote it. Read for: the two-list source split (experience_records
vs cv_master), JD-verbatim quotes in mapping items, record-id citations,
and the honest-gap framing.

Why this file has fewer sections than the template: the run happened
before the template existed. The run's matches.md was delivered
2026-09-11; the template was written 2026-09-17. The template decides
what sections a new matches.md needs, because every run starts from
its stub. This file has 6 of its 12: Target role, Keywords Skills,
Keywords Tools, Mapping Lists 1-2, and Remaining gaps (the ⚠️ in its
heading is the run's own touch; it is the same section as the
template's). It does not have Employer questions, Key notes, Mapping
List 3, the key-questions mapping, or the writing plan. The run's
question map and wireframe went to the step_2 checkpoint instead of
matches.md, and the run-log records that. When this file and the
template disagree, follow the template. Keep every template section
unless you name and justify the cut at the checkpoint.
-->

# Keyword Matches — Tyro Quality Engineer - AI (12-month contract, Sydney)

Keywords from [job-description.md](./job-description.md) (scored 2026-09-10: **(8.1/10)-(1?)**). Sources: `~/repos/jobkit/experience-pieces.json` (current role, Intellihub) and master CV + GitHub (previous roles). Session count reflects your latest working-copy edit (8 sessions — uncommitted).

## Target role

- Primary: **Hybrid AI + testing** — rubric band 10 (primary target): a QE seat built to shift a team to AI-powered quality engineering
- Role type: **mixed** — maintain/extend existing automation suites + operate/improve agentic AI tooling + steward the AI knowledge base + upskill the team. Not a from-scratch framework build; not a pure enablement seat either.

## Keywords Skills

1. Hands-on AI agents to analyse code changes against requirements
2. Directing/prompting AI tooling to produce reliable test scripts and cases
3. Maintaining and continuously improving an AI knowledge base (test definitions, regression/smoke, performance, test data, pen-test definitions)
4. Self-evolving test suite: feeding new/changing test patterns back into the knowledge base
5. Analysing AI-assisted results: genuine defect vs test needing evolution (triage feedback loop)
6. Design/build/maintain test automation suites; review coverage, identify deficiencies
7. Functional + non-functional testing (performance, accessibility, security)
8. CI/CD + DevOps practices; test data management; systems thinking
9. Upskilling the QE team in AI-assisted practices; stakeholder communication

## Keywords Tools

- AI: Rovo Agents / Rovo Dev (Atlassian) — JD says "e.g. … Claude, GitHub Copilot, or similar"; you have Claude + Copilot hands-on
- Automation suite stack unstated (ask at screen); Tyro backend is Kotlin/Node.js per sibling postings; Atlassian stack implied (Rovo)
- CI/CD; test data management; performance + accessibility + security testing; pen-testing (in-house capability evaluation)

## Mapping List 1 — Current role: Intellihub (experience-pieces.json)

1. **AI agents on code changes** — JD: "Work hands-on with AI agents… to analyse code changes against requirements" ↔ [ai-003] AI PR-review agent: structured review reports (verdict/summary/suggestions), 5–10% time saved per review + [res-003] PR reviews across IWS and SmartCore + [res-006] coordinated PR reviews catching issues before merge + [ach-007] defects caught before production.
2. **Prompting AI for reliable output** — JD: "Direct and prompt AI tooling effectively to translate… requirements into accurate test coverage" ↔ [ai-002] 15+ personal AI skills and prompts + [ai-011] designed instructions and rubrics so a small LLM produces structured, confidence-scored classifications + [ai-012] diagnosed a Copilot multiline-prompt bug and implemented the repo-recommended workaround (knows where prompting breaks, not just where it works).
3. **AI knowledge base** — JD: "Maintain and continuously improve the AI knowledge base underpinning the QE ecosystem" ↔ [ai-001] 5 shared Copilot Skills used daily by 2–3 team members + [ai-004]/[ach-005] Agents.md + copilot-instructions.md repo-context files for both frameworks + [ach-003] AutomationHub: BDD step library, metrics tracking, SharePoint hub.
4. **Defect-vs-test-evolution triage** — JD: "distinguishing genuine defects from tests requiring evolution, and route fixes back through the appropriate channels" ↔ [ai-005] failure-cause analysis tool (likely causes, suggested next steps, confidence of analysis) running daily against regression tests in the testing environment + [ai-009] scheduled AI reports classifying every failure as defect / test script issue / environment issue, with audience-tailored versions for stakeholders and engineers.
5. **Self-evolving feedback loop** — JD: "identify new or changing test patterns and feed them back into the knowledge base so automated test generation improves over time" ↔ [ai-010] agentic report workflow (planning, tool use, self-reflection, specialized agents; reused an existing domain-knowledge skill, built new ones) + [proj-003] groundcrew: CI bot that recalls past failures and human corrections so repeated issues get flagged, not re-explained + [skill-005]/[ach-004] BDD steps in plain language, reused across testers, BAs, business team members.
6. **Automation suites + CI/CD** — JD: "Design, build and help maintain test automation suites for our services" ↔ [skill-001] Python (IWS) + [skill-002] Playwright/TypeScript (SmartCore) + [mgr-001] manager-validated across IWS/IMDM/SmartCore + [ach-001] BDD scenarios running daily in CI + [ach-002] Jenkins CI/CD ownership + [cicd-002] automated environment monitoring.
7. **Upskilling the QE team** — JD: "Champion and help upskill the wider Quality Engineering team in effective use of AI-assisted testing tools" ↔ [ach-009] 8 knowledge-sharing sessions over 8 months (AI-assisted development, testing, automation) + [col-002]/[col-003] sessions became self-sustaining — others started presenting + [col-001] coached Sonya (env setup, Playwright, AI-in-coding) + [ai-008] shared skills, agents, recordings, blog posts.

### Gaps from List 1 (touched, but no dedicated record — see Remaining gaps)

- Performance / accessibility / security testing depth — adjacent only: [cicd-002] env monitoring + WYWM exposure (List 2)
- Rovo Agents / Rovo Dev — no hands-on, I am familiar with Rovo Dev cli, tried it for personal projects but switched to other coding agent, conept is the same as other CLI coding agents; adjacent via Claude/Copilot + Jira/Confluence ([skill-010]); I used Claude  code extensivly in the past but switched to Pi agent which I like more
- Test data management as a named practice — only classification-side evidence ([ai-011] test-data failure category)

## Mapping List 2 — Previous roles + GitHub (master CV)

1. **Non-functional exposure** — JD: "non-functional testing such as performance, accessibility and security" ↔ WYWM: manual core across functional, security, accessibility, usability, exploratory + 300+-test regression suite (performance itself remains a growth area).
2. **Suite building from scratch** — JD: "Design, build and help maintain test automation suites" ↔ Figtree: Playwright UI suite with 50+ scripts implemented from scratch, saving 4–6 hours per regression run + Vitest/TypeScript unit-testing framework + WYWM: key role transitioning the team to test automation (TestComplete).
3. **AI-output quality concepts** — JD: "bug-prevention, testability… and other advanced quality concepts" ↔ [proj-004] docfence (catches AI-introduced TODOs, broken links, missing sections) + [proj-007] starlord (validation script rejects LLM claims without a source) + [proj-005] compass-skills (agent skills guiding testers/QAs/PMs through domain knowledge and BDD scenarios).
4. **Exploratory + manual craft** — JD: "regardless of whether they are performed manually or through automation" ↔ Aerofiler: team recognition for exceptional exploratory testing + RST Explored (2021) + WYWM exploratory core.
5. **API + integration testing** — JD: "Ensure testing and quality checks are appropriately applied across our services" ↔ WYWM Postman monitors + REST/GraphQL collections for test-data prep + Aerofiler integration validation (Salesforce, DocuSign, AdobeSign, Zapier, Dropbox).
6. **Stakeholder reporting** — JD: "Build and maintain effective working relationships with key stakeholders" ↔ [ai-009] two audience-tailored report versions with progressive disclosure + [ach-011] shareable test reports for stakeholders.

## Remaining gaps (⚠️ not covered by any record)

1. **Rovo Agents / Rovo Dev** — no hands-on record (nobody outside Atlassian-first shops has). Honest framing: the JD's "e.g." list includes Claude and Copilot — you operate agentic tooling daily; Jira/Confluence fluency is real; Rovo is platform ramp-up, not concept ramp-up. Tyro explicitly wants curiosity + upskilling habit — your strongest evidence. I am familiar with Rovo Dev cli, tried it for personal projects but switched to other coding agent, conept is the same as other CLI coding agents
2. **Payments domain** — no record anywhere. Honest framing: smart metering is also a regulated, data-integrity-critical platform (40+ retailers, 99.5% reliable delivery); domain ramp-up is expected of any hire; the JD lists payments as "nice to have".
3. **Formal AI/ML credential** — Agentic AI course (20% done) + ISTQB-GenAI (in progress). Honest framing: the JD accepts "demonstrated self-directed learning in AI" — 8 sessions, 15+ skills, public AI repos are exactly that; in-progress certs name the habit.
4. **Non-functional depth + pen-test support** — performance = genuine growth area (adjacent: env monitoring, report scoring rules); accessibility/security = WYWM exposure; in-house pen-testing evaluation support = no record. Honest framing: name performance as a growth area with adjacent evidence; security/pen-test exposure honestly limited.
