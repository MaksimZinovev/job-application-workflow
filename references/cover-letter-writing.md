# Cover letter writing

Read when starting step_3. Draft into `cover-letter-draft.md` in the run
folder. The paragraph rubric (loaded at planning) is reused here as the
assessment rubric for every body paragraph, alongside the don'ts below.

## Required structure

The verification script enforces these mechanically — keep them in:

1. A salutation opening the letter (`Dear ...`).
2. An intro paragraph (see below).
3. An evidence table — the recruiter's skim layer, one row per key
   requirement, with a header row naming the evidence column
   (`| # | Your requirement | My evidence |` works). Bold the load-bearing
   keywords in both columns: the ad's key phrases on the left, the evidence
   highlights on the right (the 06 mitti letter is the format precedent).
4. At least three bold run-in subhead paragraphs after the table
   (`**Label.**` followed by prose). Labels are plain functional noun or
   first-person phrases ("The AI work.", "How I would start.", "What I have
   not used yet."), not slogans or essay titles.
5. A gap paragraph among them: admit the gaps between the ideal candidate
   and this profile, then find the reasons and evidence that explain why the
   gap closes rather than blocks.
6. A projects list when the record carries public work: 1-3 relevant
   GitHub projects or portfolio links, each with a one-line description,
   grounded in `cv_master`'s portfolio row or the experience records (the
   06 mitti letter lists groundcrew, docfence, clickworks.me). Skip it
   when nothing relevant exists; an empty slot is information.
7. An outro: call to action + sign-off, working rights and availability,
   thanks for the reader's time.

## The intro paragraph

The intro must not compete with the table and later sections. Its job is to
establish the core message that makes you an attractive candidate for this
role; the metrics, smaller details, and examples prove that claim later. The
intro works as an executive summary, not a compressed version of the
evidence that follows: just enough to understand what kind of environments
you have worked in, the scale and nature of the systems, and the level of
ownership — while deliberately saving metrics and specific achievements for
the later sections.

## Per-paragraph construction

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
   what changed, remove it.
7. Don't include what the recruiter doesn't need to know (credentials that
   interrupt the narrative, internal validation details).
8. Don't glue together facts from different projects or areas — one
   paragraph, one project context.
9. Don't use unclear phrases — "made feedback daily" isn't immediately
   understandable; say what was done and what changed.

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
  gate artifact for approving this step.

Checkpoint: present the draft, wait for feedback and approval.
