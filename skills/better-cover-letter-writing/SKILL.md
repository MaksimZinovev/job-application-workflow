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

This pattern is packaged as a just-in-time rule. Read
rules/rule-pattern-01-grand-claims.md before working it. The rule file
has the before and after example, the prefer list, the rubric minimums,
the coverage triggers, and the ask and do-not notes.

### 2. Colon + three-item list → natural sentence
This pattern is packaged as a just-in-time rule. Read
rules/rule-pattern-02-colon-three-item-list.md before working it. The
rule file has the rule, the before and after example, the rubric
minimums, the coverage sweep, and the ask and do-not notes.

### 3. Abstract praise → concrete explanation
This pattern is packaged as a just-in-time rule. Read
rules/rule-pattern-03-abstract-praise.md before working it. The rule
file has the rule, the before and after example, the rubric minimums,
the coverage sweep, and the ask and do-not notes.

### 4. Impressive verb → accurate verb
This pattern is packaged as a just-in-time rule. Read
rules/rule-pattern-04-impressive-verb.md before working it. The rule
file has the rule, the two before and after examples, the rubric
minimums, the coverage triggers, and the ask and do-not notes.

### 5. Sweeping claim → specific example
This pattern is packaged as a just-in-time rule. Read
rules/rule-pattern-05-sweeping-claim.md before working it. The rule
file has the rule, the before and after example, the rubric minimums,
the coverage triggers, and the ask and do-not notes.

### 6. Absolute statement → accurate qualification
This pattern is packaged as a just-in-time rule. Read
rules/rule-pattern-06-absolute-statement.md before working it. The
rule file has the rule, the before and after example, the watch list,
the rubric minimums, the coverage triggers, and the ask and do-not
notes.

### 7. Importance statement → outcome
This pattern is packaged as a just-in-time rule. Read
rules/rule-pattern-07-importance-statement.md before working it. The
rule file has the rule, the before and after example, the rubric
minimums, the coverage triggers, and the ask and do-not notes.

### 8. Self-description → evidence
This pattern is packaged as a just-in-time rule. Read
rules/rule-pattern-08-self-description-evidence.md before working it.
The rule file has the rule, the before and after example, the human
review note, the rubric minimums, the coverage triggers, and the ask
and do-not notes.

### 9. Marketing language → plain description
This pattern is packaged as a just-in-time rule. Read
rules/rule-pattern-09-marketing-language.md before working it. The
rule file has the rule, the word list, the rubric minimums, the
coverage sweep, and the ask and do-not notes.

### 10. AI-style symmetry → natural rhythm
This pattern is packaged as a just-in-time rule. Read
rules/rule-pattern-10-ai-style-symmetry.md before working it. The
rule file has the rule, the before and after example, the rubric
minimums, the coverage sweep, and the ask and do-not notes.

### 11.  Marketing echo→ cut it
This pattern is packaged as a just-in-time rule. Read
rules/rule-pattern-11-marketing-echo.md before working it. The rule
file has the rule, the rubric minimums, the coverage sweep, and the
ask and do-not notes.

### 12. Template completeness → empty slot
This pattern is packaged as a just-in-time rule. Read
rules/rule-pattern-12-template-completeness.md before working it. The
rule file has the rule, the rubric minimums, the coverage triggers,
and the ask and do-not notes.

### 13. Performative self-qualification → plain fact
This pattern is packaged as a just-in-time rule. Read
rules/rule-pattern-13-performative-self-qualification.md before
working it. The rule file has the rule, its worked example, the rubric
minimums, the coverage triggers, and the ask and do-not notes.

### 14. Homework name-dropping → detail that does work
This pattern is packaged as a just-in-time rule. Read
rules/rule-pattern-14-homework-name-dropping.md before working it. The
rule file has the rule, its worked example, the rubric minimums, the
coverage sweep, and the ask and do-not notes.

### 15. Editorial subheading → plain functional label
This pattern is packaged as a just-in-time rule. Read
rules/rule-pattern-15-editorial-subheading.md before working it. The
rule file has the rule, the before and after examples, the rubric
minimums, the coverage sweep, and the ask and do-not notes.

## 16 Intro paragraph
This pattern is packaged as a just-in-time rule. Read
rules/rule-pattern-16-intro-paragraph.md before working it. The rule
file has the rule, the rubric minimums, the coverage sweep, and the
ask and do-not notes.

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

1. Run `python3 scripts/init.py --letter <path>` from the skill
   directory. It stubs the pattern-audit table next to the letter.
2. Work one pattern at a time. Read that pattern's rule file, fix the
   letter, score the applied level and the sweep against the rule's
   named rubrics, and record evidence: a verbatim quote or a concise
   written confirmation.
3. Run `python3 scripts/check_patterns.py --letter <path>`. The pass is
   claimed only when it exits 0. An empty row means the pass is not
   done.

The stubbed table is the map. The rule files are the territory.

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
