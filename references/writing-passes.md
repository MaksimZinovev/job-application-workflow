# Writing passes — unslop and credibility rewrite

Read when starting step_4. Two passes turn the approved v1 draft into v2;
both rewrite toward a human, credible voice while preserving meaning. If the
optional skills configured at the `unslop_skill` / `better_cover_letters`
keys are unavailable, run the degraded mode: the banned-terms scan via
`verify_artifacts.py` only, and say so at the checkpoint.

## Version preservation

Write the result as `cover-letter-draft-v2.md`; v1 stays untouched, forever.
Copies and renames are the last action of the pass. Any post-copy mutation
is re-verified. Never edit the approved v1.

## Pass 1 — unslop (human voice)

Rewrite for a human, interview-natural voice. Process: scan for the
patterns below, rewrite preserving meaning and intended tone, add soul, then
self-audit — "What makes this obviously AI generated?" — and fix the rest.

- Em dashes: avoid entirely. Use periods or commas only. If a thought needs
  separation, end the sentence or use a comma. Parentheses, en dashes and
  hyphen-as-dash substitutes just trade one AI tell for another.
- No AI vocabulary: additionally, crucial, delve, enhance, fostering,
  interplay, intricate, landscape (abstract), pivotal, showcase, testament,
  underscore, vibrant, and similar. Replace with plain words.
- No forced three-part lists or AI-style symmetry: use the natural number.
- No "not just X, but Y"; state the point directly.
- No superficial -ing phrases ("highlighting...", "ensuring...",
  "fostering...") — delete or expand with real sources.
- No puffery ("testament to", "evolving landscape") — state what happened.
- No vague attributions ("Experts believe...") — name the source or delete.
- Fancy ways to say "is" ("serves as", "stands as", "boasts") — just say is
  or has.
- Filler ("in order to" → "to"; "due to the fact that" → "because"; "it is
  important to note that" → deleted).
- Active voice, cut adverbs or use stronger verbs, prefer the plain word,
  shorten or split dense sentences, one idea per sentence.
- Colons: fine before a list or example; not as mid-sentence connectors.
- Adding soul: have opinions, vary rhythm (short then long), acknowledge
  complexity, use "I" when it fits, let some mess in, be specific. Natural
  does not mean informal — no slang, no forced jokes, no deliberate
  mistakes.

## Targeted rewrites per user feedback

Only address what the user specifies. Common requests: rewrite specific
table rows to derive evidence from a specific role; de-cliché subhead
labels to plain human language. Do not change other parts. When the user
says "only address what I mentioned", that is the whole instruction.

## Pass 2 — credibility rewrite

Run the grounded pattern audit first: the skill configured at
`better_cover_letters` ships `scripts/init.py`; run
`python3 <that skill's dir>/scripts/init.py --letter <draft>` to stub a
table (No, pattern, verdict, notes), read the full skill end to end, and
fill every row with a verdict quoting the letter. The pattern list below
is a digest; the skill itself is the source. An empty row means the pass
is not done.

Scan for the remaining patterns and fix:

- Grand claims → observable actions ("played a key role" → "helped move...").
  Choose the strongest verb the evidence supports: helped, built,
  introduced, worked on, moved, added, set up, supported.
- Colon + three-item list → a natural sentence.
- Abstract praise → concrete explanation: ask what the claim actually means,
  then describe that.
- Impressive verbs → accurate verbs; do not turn participation into
  ownership.
- Sweeping claims → specific examples.
- Absolute statements → accurate qualifications (watch: always, never,
  exactly, completely, every, none, guaranteed, eliminates, solves,
  ensures). Replace only when the evidence does not support the stronger
  claim.
- Importance statements → outcomes: do not say something was important,
  explain what changed.
- Self-descriptions → evidence: replace personality, mindset and leadership
  claims with the action that demonstrates them. Every such replacement
  needs user review — never remove content silently.
- Marketing language (pivotal, key, crucial, transformative, robust,
  seamless, cutting-edge, innovative, powerful, significant,
  comprehensive) → plain description; keep the word only when surrounding
  evidence makes the claim precise.
- Marketing echo → cut: restating the company's own pitch as motivation;
  motivation is specifics tied to your own work. Homework name-dropping
  (their office address, awards) → keep only details that do work.
- Template completeness → an empty slot is information: if the honest answer
  for a planned section is "nothing real to say here", leave it out.
- Performative self-qualification ("comfortable with", "at ease with") →
  plain fact.
- Editorial subheadings → plain functional labels: a bold run-in names what
  the paragraph contains, it is not a campaign line.
- Ownership ladder: observed, contributed to, helped with, worked on, owned,
  led — use "led"/"owned" only when the text evidences that responsibility.
- Evidence rule: never strengthen a claim beyond the available evidence; if
  a stronger claim might be true but is not supported, keep the weaker
  version.

Rewrite process: identify the actual claim; separate facts from promotional
language; replace vague or inflated phrases with concrete actions or
outcomes; break forced lists; remove filler; check the rewrite does not
increase claimed responsibility; read it once as if on a real CV; ask
"could a real person plausibly have written this without trying to sound
impressive?"; simplify anything still polished for polish's sake.

Final self-check: meaning preserved; nothing invented; ownership not
exaggerated; vague claims replaced with concrete information; unnecessary
praise removed; no forced colon+list or three-part structures; ordinary
language; credible rather than promotional; the author would realistically
say this in an interview.

## Substantive-changes flag

After the passes, set the flag in `run-log.md`:

- `substantive_changes: yes` — a paragraph was rewritten, evidence was
  swapped, or structure moved → the conditional delta judge runs (see the
  judge protocol in operating-principles.md).
- `substantive_changes: no` — only small targeted fixes (de-clichéing,
  typo edits, user-flagged single replacements) → no judge run.

Then verify: `verify_artifacts.py --artifact cover-letter --path
<run>/cover-letter-draft-v2.md --matches <run>/matches.md` — zero flagged
words, zero em dashes, no fabricated evidence, ownership not exaggerated,
keyword coverage intact.

Checkpoint: present the result; wait for feedback and approval.
