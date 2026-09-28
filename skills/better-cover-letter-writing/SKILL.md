---
name: better-cover-letter-writing
description: Rewrite professional writing to sound natural, specific, and credible. Remove AI clichés, inflated claims, forced lists, and vague praise while preserving the author's actual meaning and evidence.
---
# Better cover letter writing

Rewrite text so it sounds like something a thoughtful person actually wrote.

The goal is not to make writing casual or deliberately imperfect. The goal is to make it **specific, restrained, natural, and credible**.

## Core rules

1. Prefer facts over claims about importance.
2. Prefer concrete actions over abstract descriptions.
3. Prefer ordinary words over impressive-sounding vocabulary.
4. Avoid exaggerating the author's ownership or impact.
5. Remove predictable AI writing patterns.
6. Optional, when relevant: Preserve the author's actual meaning, achievements, and level of responsibility.
7. Do not invent evidence, metrics, outcomes, or responsibilities.
8. Let the facts demonstrate that something was valuable instead of explicitly calling it valuable.

## Patterns to fix

### 1. Grand claims → observable actions

Before:
"Played a key role in the team's shift from manual to automated testing."

After:
"Helped move the team from manual to automated testing."

Why:
"Played a key role" declares importance without explaining what happened.

Prefer:

- "helped..."
- "built..."
- "introduced..."
- "worked on..."
- "moved..."
- "added..."
- "set up..."
- "supported..."

Choose the strongest verb supported by the evidence.

### 2. Colon + three-item list → natural sentence

Before:
"I learned how the platform works: what it does, who uses it, and how data moves through it."

After:
"I spent the first few weeks getting to know the platform, its users, and how data moves through it."

Do not automatically structure sentences as:

"X: A, B, and C."

A colon is fine when genuinely useful, but avoid using it to introduce a predictable three-part list.

### 3. Abstract praise → concrete explanation

Before:
"My Playwright suite was built to last."

After:
"My Playwright suite was designed as a maintainable test suite rather than a collection of recorded scripts."

Ask:
"What does this claim actually mean?"

Then describe that instead.

### 4. Impressive verb → accurate verb

Before:
"Drove the transformation toward automation."

After:
"Helped move the team toward automation."

Before:
"Championed a new testing strategy."

After:
"Worked with the team on a new testing strategy."

Do not turn participation into ownership.

### 5. Sweeping claim → specific example

Before:
"Docfence catches the exact defects AI assistants leave behind."

After:
"Docfence finds defects that AI assistants often leave behind, including TODOs, broken links, and missing sections."

Specific examples are usually more convincing than claims about what a tool does "exactly" or "comprehensively."

### 6. Absolute statement → accurate qualification

Before:
"AI-generated systems do not behave the same way twice."

After:
"AI-generated output can change from one run to the next."

Avoid absolute language unless the fact is genuinely absolute.

Watch for:

- always
- never
- exactly
- completely
- every
- none
- guaranteed
- eliminates
- solves
- ensures

Replace only when the evidence does not support the stronger claim.

### 7. Importance statement → outcome

Before:
"This was a pivotal improvement to our testing process."

After:
"This reduced the amount of manual regression testing we had to repeat."

Do not tell the reader that something was important. Explain what changed.

### 8. Self-description → evidence

Before:
"I brought a quality-first mindset to the team."

After:
"I added automated checks to the areas we tested most often."

Avoid claims about personality, mindset, leadership, or impact when an action can demonstrate the same thing.

**CRITICAL:** Always let user review the evidence claims you added. Each self-description turned to evidence must be reviewed by human.  Do not remove content silently. Do not fabricate.  Ask if unsure or need more information.

### 9. Marketing language → plain description

Avoid words such as:

- pivotal
- key
- crucial
- transformative
- groundbreaking
- robust
- seamless
- cutting-edge
- innovative
- powerful
- significant
- comprehensive

These words are not forbidden. Use them only when the surrounding evidence makes the claim precise.

### 10. AI-style symmetry → natural rhythm

Before:
"I researched the problem, evaluated the options, and implemented the solution."

After:
"I looked into the problem first, then tested a few approaches before implementing the one that worked."

Do not force every sentence into a neat three-part structure.

### 11.  Marketing echo→ cut it

&#x20;Restating the company's own pitch (mission, awards, culture) as motivation. If their marketing team could write the sentence,
&#x20; cut it. Motivation = specifics tied to your own work.

### 12. Template completeness → empty slot

Filling every planned section even when the honest answer is "nothing real to say here". An empty slot is information.

### 13. Performative self-qualification → plain fact

"Comfortable with", "happy to", "at ease with" announce an internal state to tick a box, mirroring the job ad's arrangement back as a personal trait. If the arrangement is standard for the role, state the fact and stop. "I am comfortable with hybrid work" becomes "I am based in Sydney".

### 14. Homework name-dropping → detail that does work

Telling the company what it already knows (office address, awards, founding year) to signal "I researched you". Keep researched details only where they do work: a product decision, a real question, a link to your own work. "Hybrid work from your Market Street office" becomes "hybrid work in Sydney".

### 15. Editorial subheading → plain functional label

Before:
"**Quality you can see.**"
"**From QE-led to self-serve quality.**"

After:
"**How I make quality visible.**"
"**The quality ladder.**"

Why:
A bolded inline subheading should name what the paragraph contains, not craft a slogan or essay title. Prefer plain noun phrases ("The AI work.") or first-person phrases ("How I would start.", "What I have not used yet."). If it reads like a campaign line, rename it.

## 16 Intro paragraph

The intro should **not compete with the table and later sections**. Its job is to establish the core message that makes you attractive candidate and matches the role. The metrics, smaller details and examples can then prove that claim later. The intro should work as an **executive summary**, not a compressed version of the evidence that follows. Just enough to understand **what kind of environments you’ve worked in, the scale/nature of the systems, and the level of ownership**, while deliberately saving metrics and specific achievements for the later sections


## Preserve the author's voice

Do not "humanize" writing by:

- adding slang
- adding unnecessary contractions
- inserting jokes
- deliberately introducing grammatical mistakes
- making professional writing overly casual
- adding personal opinions that the author did not express

Natural does not mean informal.

## Evidence rule

Never strengthen a claim beyond the available evidence.

If the source says:
"I helped automate regression testing."

Do not rewrite it as:
"I led the automation of the company's regression testing."

If a stronger claim might be true but is not supported, keep the weaker version.

## Ownership rule

Distinguish carefully between:

- observed
- contributed to
- helped with
- worked on
- owned
- led

Use "led" or "owned" only when the text provides evidence of that level of responsibility.

**CRITICAL**: do not remove content silently. Do not fabricate.  Ask if unsure or need more information.

## Grounded audit

Before claiming any rewrite done:

1. Run `python3 scripts/init.py --letter <path>` from this skill's
   directory. It stubs a pattern-audit table (No, pattern, verdict,
   notes) next to the letter.
2. Read this skill end to end, then fill every verdict from the
   pattern's own definition, quoting the letter. The stubbed table is a
   map; the pattern definitions above are the territory.
3. A pattern pass is claimed only with the table fully populated. An
   empty row means the pass is not done.

## Rewrite process

1. Identify the author's actual claim.
2. Separate facts from promotional language.
3. Find vague or inflated phrases.
4. Replace them with concrete actions or outcomes.
5. Break up forced lists and repetitive sentence structures.
6. Remove unnecessary qualifiers and filler.
7. Check that the rewrite does not increase the author's claimed responsibility.
8. Read it once as if it appeared on a real CV or LinkedIn profile.
9. Ask: "Could a real person plausibly have written this without trying to sound impressive?"
10. If a sentence still sounds polished for the sake of sounding polished, simplify it.

## Final self-check

Before returning the rewrite, check:

- Did I preserve the original meaning?
- Did I invent anything?
- Did I exaggerate ownership?
- Did I replace vague claims with concrete information?
- Did I remove unnecessary praise?
- Did I avoid forced colon + list constructions?
- Did I avoid repetitive three-part structures?
- Did I use ordinary language where possible?
- Does the result sound credible rather than promotional?
- Would the author realistically say this in an interview?

Return the rewritten text directly unless the user asks for an explanation.
