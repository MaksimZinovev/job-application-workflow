<!--
GOLD EXAMPLE, cover letter (format + prose precedent)

Source: run 10_quality-engineer-ai-12-months-contract-tyro,
cover-letter-draft-v2.md (wiki: notes/2026-applications/10_...).
Approved by the user 2026-09-10 after seven review rounds (the run's
step1-checkpoint.md records the full feedback loop).

Verified against the skill gates: 0 em dashes; keyword coverage 100% vs
the bundled matches; structure complete. Three checks the letter does NOT
pass today, each because the letter predates the rule (annotations below
name each and its cure): budget 1050/1000 against the default; one
contrastive-conjunction term; the gap-paragraph label pattern.
This run also predates the tiered judge protocol; the bundled
review-report exemplars reconstruct its real v1 to v2 fix history.

Curation: the letter body below is byte-identical to the approved
artifact. Known-seam annotations live after the signature so the body
stays pristine. Read it for structure, evidence density, bolding
discipline, and voice; read the annotations for what the next run does
better.

Portability: this is one user's approved artifact (real names, links,
metrics). Structure and discipline transfer to any candidate; a new
user's own runs + retro nominate their own gold examples over time.
-->

Maksim Zinovev
Waitara, NSW 2077 • 0415 182 769 • <mzn@fastmail.com>

September 10, 2026

Re: Quality Engineer - AI (12-month contract)
Tyro, Sydney NSW

Dear Tyro team,

I am applying for the Quality Engineer - AI contract role. I work to help testing teams implement the AI systems they envision, and that's been the focus of my recent work. At Intellihub, the largest smart-metering company in Australia and New Zealand, I designed and maintained test automation across Python and Playwright/TypeScript, and the AI toolkit I built around it is still in daily team use. Five-plus years in testing and automation, two test suites built from scratch, and a habit of leaving behind systems other people keep using.

| Your requirement                                                                                   | My evidence                                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Work hands-on with **AI agents** to **analyse code changes** against requirements                  | (Intellihub) AI **PR review agent**: structured **verdicts, summaries and suggestions** per pull request, an estimated **5 to 10 percent time saved per review**; code reviews across IWS (**Python**) and SmartCore (**Playwright/TypeScript**) catching issues before merge; defects caught before production                                                                                            |
| **Prompt AI tooling** for reliable **test scripts and test cases**                                 | **15+ personal AI skills and prompts**; instructions and rubrics that make a small model return **structured, confidence-scored classifications**; diagnosed a Copilot **multiline-prompt bug** and applied the recommended workaround                                                                                                                                                                     |
| **Maintain and improve the AI knowledge base** (test definitions, regression and smoke, test data) | (Intellihub) **5 shared Copilot Skills** in daily use by 2 to 3 teammates; **Agents.md** and copilot-instructions.md repo-context files for both frameworks; **AutomationHub** (BDD step library, metrics, SharePoint); personal markdown knowledge base with **indexed search and query-time synthesis** (github.com/MaksimZinovev/wiki)                                                                  |
| **Distinguish genuine defects from tests needing evolution**, route fixes back                     | (Intellihub) **failure-cause analysis tool** (likely causes, suggested next steps, confidence of analysis) running **daily against regression tests in the testing environment**; scheduled AI reports classifying every failure as defect / test script / environment / **test data**, in stakeholder and engineer versions                                                                               |
| **Self-evolving test suite**: feed new patterns back so generation **improves over time**          | (Intellihub) **agentic report workflow** (planning, tool use, self-reflection, specialised agents); (personal project) **groundcrew** CI bot recalling past failures and human corrections so repeats get flagged, not re-explained                                                                                                                                                                        |
| **Design, build, maintain automation suites**; **CI/CD**; review coverage                          | (Intellihub) automation across IWS (**Python**), SmartCore (**Playwright/TypeScript**) and IMDM; **first BDD scenarios running daily in CI**; **Jenkins pipeline ownership**; automated environment monitoring; (WYWM) key role moving the team onto test automation, **300+ test regression suite**; (Figtree) **Playwright suite built from zero, 50+ scenarios, 4 to 6 hours saved per regression run** |
| **Upskill the QE team** in AI-assisted practices; **stakeholder relationships**                    | (Intellihub) **8 knowledge-sharing sessions over 8 months**, now self-sustaining with teammates presenting their own; coached an engineer from environment setup to independent AI-assisted coding; shared skills, agents, recordings and blog posts; shareable stakeholder reports                                                                                                                        |

- github.com/MaksimZinovev/groundcrew (CI bot recalling past failures and human corrections)
- github.com/MaksimZinovev/docfence (finds AI-introduced TODOs, broken links and missing sections in documents)
- github.com/MaksimZinovev/starlord (rejects LLM claims that cite no source)
- github.com/MaksimZinovev/compass-skills (agent skills guiding testers through domain knowledge and BDD)

**The AI work** I've done has been part of my day-to-day testing workflow rather than separate experimentation. At Intellihub, I built an AI PR-review agent that returned a structured verdict, summary and suggestions for pull requests, saving around 5 to 10 percent of review time and helping catch issues before merge. I also wrote instructions and rubrics that made a smaller LLM produce structured, confidence-scored classifications. For test failures, I built a scheduled AI-powered analysis workflow (Jenkins pipeline, Python, Copilot CLI, wrapped into plain language BDD steps) that derives failure nature (defect, test script issue, environment, test-data issue), next suggested steps, confidence of analysis, labels with domain and component tags. Outside work, my Groundcrew project helps me with test automation volunteering work I am doing for Scoolendar.com: when a CI failure occurs, AI step analyses and generates a summary which is sent to Telegram chat , so I stay up to date with the regression execution status  and save time on opening CI or email notifications.

**The automation work.** At Intellihub I designed and maintained automation across three frameworks: IWS (Python), SmartCore (Playwright/TypeScript) and IMDM (Java). On SmartCore I introduced the first BDD scenarios to run daily in CI instead of on demand, and removed the hardcoded waits that made the tests flaky and slow. On IWS I owned the Jenkins pipelines and automated environment monitoring, so a broken test service surfaced before the pipeline did. Before Intellihub I built a Playwright UI suite from zero for an insurance and claims SaaS, 50+ scenarios saving 4 to 6 hours per regression run. Non-functional testing I know from the manual side at WYWM, security, accessibility and usability, exposure rather than a speciality.

**The knowledge-base work.** At Intellihub I built and maintained the AI knowledge base: five shared Copilot Skills, still in daily team use; Agents.md and copilot-instructions.md files that give agents repo context; and an AutomationHub holding the BDD step library and its metrics. The BDD steps are in plain language, so testers, BAs and business people reuse them. Outside work I keep a personal knowledge base, plain markdown on GitHub with indexed search and lightweight query-time synthesis, no vector-database or server infrastructure to babysit. I compared the RAG, embeddings and vector-store options, ChromaDB, Pinecone and Postgres with pgvector among them, before choosing this setup. Agents take on part of the upkeep; docfence finds AI-introduced TODOs, broken links and missing sections in documents. The knowledge-sharing sessions I started, eight in eight months, became self-sustaining with teammates presenting their own, and the engineer I coached now works independently.

**Where I would be ramping up.** Two gaps, named plainly. Rovo I have not used at work, though I have run the Rovo Dev CLI on personal projects; its concepts are the ones I used daily through Claude and Copilot, your ad's own examples, so this is platform ramp-up, not concept ramp-up. Payments I have not worked in, but smart metering is regulated and data-integrity-critical, with meter data for 40+ electricity retailers delivered 99.5 percent reliably, so regulated data is familiar ground. On formal credentials, my Agentic AI course and the ISTQB-GenAI certification are in progress.

I am an Australian citizen based in Sydney and available immediately.  Please contact me at your convenience to arrange a conversation. Thank you for your time and consideration.

Sincerely,
Maksim Zinovev
<mzn@fastmail.com> • 0415 182 769


---

## Annotations, known seams (post-approval review; the body above stays verbatim)

1. **Word budget.** Gate body count 1050/1000. The 1000-word default was
   set after this run; growth past the cap needs explicit user approval
   (rule-word-budget). Options: keep verbatim as the prose exemplar
   (budget rule still governs new runs) or trim to budget in a curated
   variant.
2. **The payments sentence.** It joins the gap and the good news in a
   single breath, a sentence shape the unslop skill bans as an AI tell.
   The gate now flags that shape on sight. The cure is two short
   sentences instead of one pivot: "Payments I have not worked in.
   Smart metering is regulated and data-integrity-critical, so
   regulated data is familiar ground."
3. **The gap paragraph label.** The letter has a gap paragraph:
   "**Where I would be ramping up.**" The checking script cannot see it.
   The script looks for words like gap, grow, still, honest or willing
   inside the bold label. "Ramping" is missing from that word list. Two
   fixes are planned: teach the script the word, or use a recognized
   word in new letters. This copy keeps the original text.
4. **The bold labels.** Two notes. First: "The AI work" has no
   period at the end. The skill format is "**Label.**" followed by
   prose, and the other three labels do carry the period. Second, the
   three main labels all end in "work" (AI, automation, knowledge-base).
   The wording is plain and honest, which is right. But the same head
   word three times reads monotonous, like a
   paragraph where every sentence starts with "I built", "I created",
   "I started". New letters vary the noun: "The AI practice." "The
   frameworks." "The knowledge base and its upkeep." The paragraph
   under the first label is the best one in the letter.
5. **The projects list.** The skill says to list one to three
   projects. This letter lists four (groundcrew, docfence, starlord,
   compass-skills). That is an allowed exception. Every project is
   relevant, every line adds value, and the user approved the list. A
   new letter stays at one to three unless the same holds.
6. **Where the rules came from.** The first draft of this letter taught
   the skill real lessons. It opened the AI paragraph with a claim:
   "**The loop you are building, I already run.**" A claim with no work
   behind it. The writing guide now quotes that exact sentence in its
   per-paragraph rules: cut claim-only sentences, let the work speak.
   The draft also called docfence a thing that "catches the defects AI
   assistants leave behind" (a big claim with no specifics), kept the
   words "manager-validated" (inside detail a recruiter does not need),
   and carried a typo inside a bold marker. The v2 above fixed them
   all. Every flag with its quote sits in
   examples/review-report-gold-needs-fixes.json. Read that file before
   a re-judge, so the needs-fixes shape looks familiar.
