# Cover letter writing

Read when planning (step_2) and again when drafting (step_3): the plan
assigns each paragraph its hidden question, and this file decides how
that paragraph is built — reading it at planning keeps the plan
buildable, so drafting is execution, not rework. Fill the
`cover-letter-draft.md` stub created at init in the run folder. The
paragraph rubric (loaded at planning) is reused here as the assessment
rubric for every body paragraph, alongside the don'ts below.

## Required structure

The verification script enforces these mechanically — keep them in:

1. A salutation opening the letter (`Dear ...`).
2. An intro paragraph (see below).
3. An evidence table — the recruiter's skim layer, one row per key
   requirement, with a header row naming the evidence column
   (`| # | Your requirement | My evidence |` works). The table answers
   "what is the evidence that I am a good candidate": each row maps a
   requirement to concrete records — company, nature of business, tech
   stack, responsibilities, achievements — and may include interests,
   GitHub projects or courses where they close the requirement. Bold the
   load-bearing keywords in both columns: the ad's key phrases on the
   left, the evidence highlights on the right
   (`examples/cover-letter-gold.md` is the bundled format precedent —
   read it before drafting).
4. At least three bold run-in subhead paragraphs after the table
   (`**Label.**` followed by prose). Labels are plain functional noun or
   first-person phrases ("The AI work.", "How I would start.", "What I have
   not used yet."), not slogans or essay titles. Each label links clearly
   to the hidden question its paragraph answers, from the plan: a
   skimming recruiter reads the label and immediately sees that the
   paragraph addresses something this ad asked for. Vary the head word
   across labels: three labels ending in the same noun read as a list,
   not a letter.
5. A gap paragraph among them, if there are gaps: admit the gaps between
   the ideal candidate and this profile, then find the reasons and
   evidence that explain why the gap closes rather than blocks. If this
   profile genuinely has no gap for this ad, adapt — do not invent one or
   fill the space with meaningless content.
6. A projects list when the record carries public work: 1-3 relevant
   GitHub projects or portfolio links, each with a one-line description,
   grounded in `cv_master`'s portfolio row or the experience records.
   Only strong, relevant projects earn a line; if unsure whether a
   project clears that bar, ask the user. More than three is an
   exception, taken only when every project is relevant, every line adds
   value, and the user approves (the bundled gold letter runs four on
   that exception). Skip it when nothing relevant exists; an empty slot
   is information.
7. An outro: call to action + sign-off, working rights and availability,
   thanks for the reader's time.

## The intro paragraph

The intro answers the plan's first question: who is the ideal candidate,
and why does this profile fit that shape? Derive the ideal candidate from
the ad and the ideal-role profile — experience (years), role in team (QA,
test automation, AI, mixed), and the fit with the existing context:
company maturity, nature of the business, established engineering
practices and tools, expected outcomes (build from scratch vs support
existing frameworks). Then state the job-candidate fit plainly: what kind
of environments you have worked in, the scale and nature of the systems,
and the level of ownership.

The intro must not compete with the table and later sections. Its job is
to establish the core message that makes you an attractive candidate for
this role — the fit, stated in one plain paragraph — while the metrics,
smaller details, and examples prove that claim later. The intro works as
an executive summary, not a compressed version of the evidence that
follows: just enough to understand the fit, deliberately saving metrics
and specific achievements for the later sections.

## Per-paragraph construction

The paragraph order comes from the plan's ranked hidden-question map
(matches-and-plan.md): the primary hidden question — derived from the
ideal-candidate profile's most important attribute(s) for this role —
gets the first subhead paragraph, the secondary question the second, the
third question the third. Derive each question per ad; do not read the
pattern as "always write a 'How I would start' paragraph". The method:
ask what the employer most wants to know up front about this attribute,
how the candidate would work toward their goals with it, and which past
experience proves it — the answer names the paragraph.

IMPORTANT: 
Anti-pattern: 
Terminology is presented as a catalogue of concepts rather than being tied directly to what you built. Keep the terminology that matches the role, but anchor it in the implementation.


For each hidden-question paragraph:

- Answer this hidden employer question: [QUESTION], derived from the ad's
  own wording: [JD QUOTE]. Use only the evidence items assigned at planning.
- Build the paragraph around what I actually did → specific context →
  evidence/result → what this demonstrates for this role.
- Prefer concrete actions, project names, technologies, scope, and metrics
  where available. Explain relevance through the evidence rather than saying
  "a strong fit", "passionate", "results-driven".
- Preserve the actual level of ownership. Do not invent or strengthen
  claims.
- Make the paragraph read as part of a continuous story, not a list of
  achievements or resume snippets. It must clearly support and answer the
  hidden question, and make it easy for the reader to see why the candidate
  matches the role expectations for that area.
- Avoid repeating evidence used elsewhere.
- Use ordinary, natural language; remove generic corporate language and
  predictable AI phrasing.
- Remove claim-only sentences such as "The loop you are building is one I
  already run" — the examples demonstrate it more convincingly.

Example of a clear narrative arc (AI in real QE work → code changes →
reliable prompting → failure analysis → feedback loop): the AI work has been
part of the day-to-day testing workflow rather than separate
experimentation; at a named employer an AI PR-review agent returned a
structured verdict, summary and suggestions for pull requests, saving
measured review time and catching issues before merge; instructions and
rubrics made a smaller LLM produce structured, confidence-scored
classifications; a failure-cause analysis tool suggested likely causes and
next steps behind a human review step; a side project extends the same idea
to CI failures.

## The don'ts

1. Don't make claims before evidence — lead with what I actually did.
2. Don't turn the paragraph into an achievement or keyword list — build one
   coherent narrative.
3. Don't explain what the evidence "demonstrates" — let actions, context and
   results speak.
4. Don't inflate ownership or experience — accurately distinguish work,
   personal projects and learning.
5. Don't use generic AI/corporate language — avoid clichés,
   impressive-sounding vocabulary and repetitive AI-style phrasing.
6. Don't use vague statements: if it doesn't say what you actually did or
   what changed, remove it. Example: "Coverage review was part of how we
   ran pull requests."
7. Don't include what the recruiter doesn't need to know (credentials that
   interrupt the narrative, internal validation details).
8. Don't glue together facts from different projects or areas — one
   paragraph, one project context. Example: "removed hardcoded waits to
   kill flakiness, made feedback daily, then pointed AI at the failure
   analysis that remained" welds SmartCore and IWS work into one arc.
9. Don't use unclear phrases — "made feedback daily" isn't immediately
   understandable; say what was done and what changed.

## Before and after — real sentences from real runs

Every bad sentence below shipped in a real draft or review round; every good
one is the approved fix that replaced it (provenance in parentheses; quotes
are verbatim). Read the bad sentence, say what is wrong in it in your own
words, then compare with the diagnosis. Pairs marked "constructed" were
built for teaching and say so; everything else is real. The middle versions
that failed review teach more than the clean pairs — the full three-version
sequences live in the paragraph rubric's failure gallery.

**Intro — grand framing → plain core message** (real run, draft →
approved fix)
- Bad: "It is a mandate to turn a QE team's AI ambitions into day-to-day
  machinery, which is what my recent work has been:"
- Diagnosis: reads like a mission statement the recruiter must take on
  faith, and the "which is what my recent work has been:" bridge claims
  instead of showing.
- Good: "I work to help testing teams implement the AI systems they
  envision, and that's been the focus of my recent work."
- Why: a plain claim the reader can hold the letter to; proof waits for
  the table and the paragraphs, which is the intro's job.

**Labels — slogan → plain function** (real run, draft → approved fix)
- Bad: "**A knowledge base is a garden, not a dump.**"
- Good: "**The knowledge-base work.**"
- Why: a label helps the recruiter find the paragraph; it does not win an
  argument. Slogans and essay titles read as AI voice. Vary the head word
  too — three labels ending in "work" read as a list, not a letter.

**Don't 1 — claims before evidence** (real run, draft → approved fix)
- Bad: "The loop you are building, I already run."
- Diagnosis: a claim with no work behind it. What loop? Run where? The
  reader has nothing to hold.
- Good: "**The AI work** I've done has been part of my day-to-day testing
  workflow rather than separate experimentation."
- Why: the claim is gone and the paragraph that follows demonstrates the
  loop with real work (PR-review agent, prompting rubrics, failure-cause
  tool). Cut the claim; let the assigned evidence talk.

**Don't 2 — achievement list → one narrative** (constructed; good side
improved per user review)
- Bad: "Built automation across IWS, SmartCore, IMDM. Wrote first BDD
  scenarios. Removed hardcoded waits. Owned Jenkins pipelines."
- Good: "At Intellihub I designed and maintained automation across three
  frameworks: IWS (Python), SmartCore (Playwright/TypeScript) and IMDM
  (Java). On SmartCore I introduced the first BDD scenarios to run daily
  in CI instead of on demand, and was recognised for advocating for best
  practices in automation code; for example, I authored the PR that
  removed a large number of hardcoded waits that made the tests flaky
  and slow."
- Why: same facts, but each sentence grows from the previous one; a list
  makes the reader do the assembly.

**Don't 3 — explaining what the evidence demonstrates** (constructed)
- Bad: "This shows my strong ownership and my passion for quality."
- Good: the evidence sentence itself, and nothing after it.
- Why: the reader decides what evidence demonstrates; an explanation
  sentence answers no sub-question and dies in the 2-minute check.

**Don't 4 — inflated ownership** (bad constructed; good = a real
approved letter)
- Bad: "I led the team's automation transformation end to end."
- Good: "On IWS I owned the Jenkins pipelines and automated environment
  monitoring, so a broken test service surfaced before the pipeline did."
- Why: ownership verbs must match the records (rule-ownership-calibration);
  the interviewer probes exactly where the letter sounds bigger than the
  record.

**Don't 5 — generic AI/corporate language** (real run, draft → approved
fix)
- Bad: docfence "catches the defects AI assistants leave behind in
  documents"
- Good: "finds AI-introduced TODOs, broken links and missing sections in
  documents."
- Why: the grand version is marketing voice that could describe any tool;
  the plain one says what the thing observably does. The full cliché
  catalog is `assets/banned-terms.json` (the verify gate enforces it).

**Don't 6 — vague statements** (a real run's letter; full sequence in
the rubric gallery)
- Bad: "I keep pipelines trustworthy."
- Diagnosis: a trait asserted, no interaction, no outcome. What did you
  actually do?
- Good: "At Intellihub I built the first BDD scenarios to run daily in CI.
  Until then, scenarios ran only on demand; now the team gets regression
  feedback every morning."

**Don't 7 — what the recruiter doesn't need** (real run, draft →
approved fix)
- Bad: "I design and maintain automation across three frameworks, IWS
  (Python), SmartCore (Playwright/TypeScript) and IMDM, manager-validated"
- Good: "At Intellihub I designed and maintained automation across three
  frameworks: IWS (Python), SmartCore (Playwright/TypeScript) and IMDM
  (Java)."
- Why: two defects in one sentence. "manager-validated" is internal
  process detail interrupting the evidence to argue with nobody, and the
  verbs are present tense for a past employer (rule-tense-from-cv); the
  approved fix corrected both. Credentials and internal validation go
  unless the ad asks for them.

**Don't 8 — gluing facts from different projects** (a real run's
letter; full sequence in the rubric gallery)
- Bad: "I removed hardcoded waits to cut flakiness, and Postman monitors
  have run scheduled API checks against multiple production instances
  since my previous role."
- Good: "At Intellihub I removed hardcoded waits from the automation
  frameworks to cut flaky runs. At my previous employer, WithYouWithMe, I
  introduced Postman monitors into the team's test practice, scheduled
  API checks running against multiple production instances to catch
  issues faster."
- Why: two employers welded into one sentence — the reader cannot tell
  who did what where. One sentence, one context.

**Don't 9 — unclear phrases** (real run, draft → approved fix)
- Bad: "running **daily in against regression tests in testing
  environment **"
- Good: "running **daily against regression tests in the testing
  environment**"
- Why: a typo inside bold markers survived self-review. Read the rendered
  text aloud; "made feedback daily"-style phrases fail the "does this
  make sense?" test long before any gate does.

## Budgets and verification

- Word budget: `word_budgets.cover_letter_default` in
  `assets/sources.json` (default 1000 words, counted on the letter body,
  salutation through signature). An increase is allowed only when necessary
  and approved by the user — always ask and justify.
- Verify before the checkpoint:
  `verify_artifacts.py --artifact cover-letter --path
  <run>/cover-letter-draft.md --matches <run>/matches.md`.
- Cross-check facts against matches.md and `cv_master` before presenting.
- The Tier 1 judge then reviews the full draft against the locked criteria
  (see the judge protocol in operating-principles.md); its report is the
  gate artifact for approving this step. Judge format exemplars:
  `examples/review-report-gold-approved.json` (what clears the gate) and
  `examples/review-report-gold-needs-fixes.json` (what needs-fixes looks
  like, reconstructed from this skill's real v1→v2 fix history).

Checkpoint: present the draft, wait for feedback and approval.
