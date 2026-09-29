---
name: better-cover-letter-writing
description: Rewrite professional writing to sound natural, specific, and credible. Remove AI clichés, inflated claims, forced lists, and vague praise while preserving the author's actual meaning and evidence.
---
# Better cover letter writing

Rewrite text so it sounds like something a thoughtful person actually
wrote. The goal is **specific, restrained, natural, and credible**,
not casual and not deliberately imperfect.

## Patterns to fix

Each pattern is a just-in-time rule: read its rule file only when you
work that pattern on the letter.

| No | Pattern | Rule file |
|----|---------|-----------|
| 1 | Grand claims → observable actions | rules/rule-pattern-01-grand-claims.md |
| 2 | Colon + three-item list → natural sentence | rules/rule-pattern-02-colon-three-item-list.md |
| 3 | Abstract praise → concrete explanation | rules/rule-pattern-03-abstract-praise.md |
| 4 | Impressive verb → accurate verb | rules/rule-pattern-04-impressive-verb.md |
| 5 | Sweeping claim → specific example | rules/rule-pattern-05-sweeping-claim.md |
| 6 | Absolute statement → accurate qualification | rules/rule-pattern-06-absolute-statement.md |
| 7 | Importance statement → outcome | rules/rule-pattern-07-importance-statement.md |
| 8 | Self-description → evidence | rules/rule-pattern-08-self-description-evidence.md |
| 9 | Marketing language → plain description | rules/rule-pattern-09-marketing-language.md |
| 10 | AI-style symmetry → natural rhythm | rules/rule-pattern-10-ai-style-symmetry.md |
| 11 | Marketing echo → cut | rules/rule-pattern-11-marketing-echo.md |
| 12 | Template completeness → empty slot | rules/rule-pattern-12-template-completeness.md |
| 13 | Performative self-qualification → plain fact | rules/rule-pattern-13-performative-self-qualification.md |
| 14 | Homework name-dropping → detail that does work | rules/rule-pattern-14-homework-name-dropping.md |
| 15 | Editorial subheading → plain functional label | rules/rule-pattern-15-editorial-subheading.md |
| 16 | Intro paragraph (exec summary) | rules/rule-pattern-16-intro-paragraph.md |

## Preserve the author's voice

Do not humanize by adding slang, unnecessary contractions, jokes,
deliberate mistakes, casual tone, or opinions the author did not
express. Natural does not mean informal.

## Evidence and ownership

Never strengthen a claim beyond the available evidence. If the source
says "I helped automate regression testing," do not rewrite it as
"I led the automation of the company's regression testing." If a
stronger claim might be true but is not supported, keep the weaker
version.

Use "led" or "owned" only when the text provides evidence of that
level of responsibility. The ladder, weakest to strongest: observed,
contributed to, helped with, worked on, owned, led.

**Never remove content silently. Never fabricate. Ask when unsure.**

## Grounded audit

1. Run `python3 scripts/init.py --letter <path>` from the skill
   directory. It stubs the pattern-audit table next to the letter;
   the table's own header carries the loop.
2. The pass is claimed only when
   `python3 scripts/check_patterns.py --letter <path>` exits 0.

The stubbed table is the map. The rule files are the territory.

## Rewrite process

1. Identify the author's actual claim.
2. Separate facts from promotional language.
3. Replace vague or inflated phrases with concrete actions or
   outcomes. Break forced lists and repetitive structures. Cut
   filler words.
4. Read it once as if it appeared on a real CV or LinkedIn profile:
   could a real person plausibly have written this without trying to
   sound impressive?

## Final self-check

Close the audit table's final self-check line before returning: read
the result once more as its author would. If a sentence sounds
polished for the sake of sounding polished, simplify it.

Return the rewritten text directly unless the user asks for an
explanation.