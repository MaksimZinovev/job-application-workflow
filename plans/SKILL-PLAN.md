# Plan — `job-application` skill (cover-letter scope)

Turn the job-application workflow into a spec-compliant, portable agent skill,
honoring the locked 2026-09-09 decisions (per-step YAML headers, one file per
rule, run-log + retro cadence) and the annotation feedback rounds.
**Physical home: `~/repos/job-application-workflow/`** (standalone portable repo,
git-initialized); the wiki consumes it via the symlink
`~/repos/wiki/.pi/skills/job-application -> /Users/maksim/repos/job-application-workflow`.

## 0. Scope split (review round 2, item 1)

Two skills instead of one bloated one:

- **This sprint — `job-application` (cover-letter skill):** the application run from
  preflight through the **approved cover letter** — step_0 context, step_1 JD
  analysis + scoring + promotion gate, step_2 matches + paragraph plan, step_3
  draft v1, step_4 writing passes → v2, plus step_audit (pre-delivery audit) and
  step_retro (learning loop). It owns the run folder and the promotion gate.
- **Future sprint — `resume-and-prep` companion:** plan extraction
  (cover-letter-plan.md), resume tailoring, interview prep. Step ids
  `step_5/6/7` stay **reserved** in the rules corpus so both skills share one
  stable id vocabulary; this skill's artifacts (approved letter + matches.md) are
  its natural inputs.

The folder/name stays `job-application` — it is the entry skill that starts every
application run. Rename optional; say the word and it becomes mechanical.

## 1. Metadata (re-validated for the narrowed scope ✅)

```yaml
name: job-application
description: Orchestrates an evidence-based job application run from job
  description analysis to an approved cover letter: preflight resource checks,
  rubric scoring with a promotion gate, keyword-to-evidence matching,
  rubric-validated paragraph planning, cover letter drafting, unslop rewriting
  passes, independent LLM review, and deterministic artifact verification. Use
  when scoring a job description or preparing a cover letter application run
  against configured source-of-truth records. Enforces checkpointed user
  approval at every step; paths are configurable for portable setups. Don't use
  for resume tailoring, interview prep, or standalone writing edits - resume
  and prep belong to a companion skill.
```

## 2. Skill directory structure

```
job-application/
├── SKILL.md                       # operational spec — HARD BUDGET: ≤150 lines (§6)
├── CHANGELOG.md                    # NEW — rule governance log; opens at retro #1 activation
├── scripts/                        # tiny single-purpose CLIs; stdout=report, stderr=failure; errors self-describing
│   ├── preflight.py
│   │   # args: [--config <sources.json>] [--set <key> <path>] [--waive <key> --note "..."]
│   │   # 1. load assets/sources.json (portable config: keys, paths, required flag, function)
│   │   # 2. expanduser+existence-check every entry; bundled skill assets checked too
│   │   # 3. mandatory missing → exit 1; stderr lists key, path, function, fix command
│   │   #    ("preflight.py --set <key> <path>" or edit sources.json); workflow is blocked
│   │   # 4. optional missing → warning on stderr, exit 0, flagged for the interview tool
│   │   # 5. --waive records an explicit user approval into sources.json `waived` (dated)
│   │   # stdout: resolved-path table (key | required | status | resolved path)
│   ├── init_application.py
│   │   # args: --name "<slug>" --jd <path-or-text-file> [--config <sources.json>]
│   │   # 1. refuse to proceed if mandatory sources unresolved (calls preflight logic)
│   │   # 2. derive next NN_ prefix by scanning configured applications_root/NN_* folders
│   │   # 3. create run folder; copy JD → job-description.md (refuses overwrite: exit 1)
│   │   # 4. stub scoring.md from assets/scoring-template.md   ← review round 1, item 13
│   │   # 5. stub matches.md from assets/matches-template.md
│   │   # 6. create progress.md checklist + run-log.md from assets templates
│   │   # 7. create progress.json: step_0..step_4, step_audit, step_retro (all mandatory),
│   │   #    status=pending, deps, expectStatus — steps 5-7 reserved for the companion skill
│   │   # stdout: created-file manifest + next action ("run progress.py --status")
│   ├── progress.py
│   │   # args: <run-folder> [--status] [--start <id>] [--approve <id>]
│   │   # 1. --status: print current step, blocker(s), next action + THE reference file
│   │   #    to read for that step (JIT pointer carried in state, fights drift)
│   │   # 2. --approve <id>: gate — only if depends_on approved AND expected artifacts
│   │   #    exist AND (step_3, step_audit; step_4 only when run-log marks
│   │   #    substantive changes) review-report.json verdict == approved
│   │   #    else exit 1 naming the missing dependency — no optional steps in v1
│   │   # 3. progress.json is the single machine state; any session resumes via --status
│   │   # stdout (status): step | state | deps | artifacts | next action
│   └── verify_artifacts.py
│       # args: --artifact {scoring|matches|cover-letter|review-report} --path <file>
│       #       [--matches <matches.md>] [--max-words N] [--config <sources.json>]
│       # 1. scoring: "Scoring Results" section ≤5,000 chars (config key); required
│       #    headings present (rubric id, per-criterion rows, verdict)
│       # 2. matches: <10,000 chars; sections present (target roles, Keywords Skills,
│       #    Keywords Tools, role type); list sizes 5-7 / 5-7 / 3-5
│       # 3. cover-letter: em-dash count = 0; banned-terms "fail" entries = 0, "review"
│       #    entries reported as warnings (see §4b); keyword coverage vs matches.md
│       #    (fail <100%); required structure (intro, evidence table, ≥3 bold run-in
│       #    subhead paragraphs, gap paragraph, outro); version preservation
│       #    (v1 exists when v2 does); word budget (config default, --max-words override)
│       # 4. review-report: exists, verdict == approved, every flagged item resolved,
│       #    judge identity recorded — starlord conformance-guard gate: a missing or
│       #    unapproved report blocks progress.py --approve for step_3/step_4/step_audit
│       # per-failure stderr: file, check name, expected vs actual, one-line fix hint
│       # exit 0 only when all checks pass → this is what unblocks progress.py --approve
├── references/                     # bulky rule sets, read JIT (loading enforced, see §6)
│   ├── operating-principles.md     # checkpoint protocol, no-fabrication, context economy,
│   │                               # interview-tool decision points, scope limits
│   ├── jd-analysis.md               # rubric selection (full-time vs gig), scoring procedure,
│   │                               # web-search enrichment, promotion-gate decision format
│   ├── matches-and-plan.md         # 3 lists construction, budgets, gaps framing,
│   │                               # 8 hidden-question map, evidence ranking
│   ├── paragraph-rubric.md          # the 6-dimension rubric + worked examples — read at
│   │                               # PLANNING (step_2) to decompose hidden questions, assign
│   │                               # evidence, sketch each paragraph arc BEFORE drafting
│   │                               # (review round 2, item 2); reused at step_3/4 as assessment
│   ├── cover-letter-writing.md     # per-paragraph writing guidelines, don'ts, worked example
│   ├── writing-passes.md            # unslop + better-cover-letter-writing integration,
│   │                               # targeted-rewrite protocol, version preservation
│   └── retro-and-run-log.md         # run-log convention, retro procedure, caps (≤3 runs,
│                                   # ≤10 rules per sweep), rule-file format
├── assets/                          # machine-consumed; section names here == checks in verify_artifacts.py
│   ├── sources.json                # PORTABLE CONFIG (see §4) — defaults = current paths
│   ├── banned-terms.json           # two severities: "fail" (hard tells) and "review"
│   │                               # (noisy patterns, reported not blocking); adapted from
│   │                               # simonw/tools llm-cliche-highlighter (attribution kept):
│   │                               # ai-vocab, not-just/not-but, note-that, testament,
│   │                               # crucial-role, landscape, participle-tail,
│   │                               # vague-experts, despite-challenges, performative-honesty,
│   │                               # turns-out, ai-leftovers = fail; colon-triple,
│   │                               # stacked-questions = review (legit-prose noise risk)
│   ├── scoring-template.md         # scoring.md skeleton
│   ├── matches-template.md         # matches.md skeleton
│   ├── review-report-template.json # judge report schema: verdict, per-dimension scores,
│   │                               # flagged items, judge identity, tier (1/2), scope (full/delta)
│   ├── progress-template.md        # human checklist
│   └── run-log-template.md         # raw-signal log skeleton
├── rules/                           # UNCHANGED location — 19 rule files + README (see §9)
└── .local/                          # NOT part of the skill; gitignored historical artifacts
    └── session-handoff.md          # moved here (round 1, items 5/17)
```

## 3. Run-folder structure produced by the skill

```
<applications_root>/12_senior-qa-engineer-acme/     # NN prefix auto-derived
├── job-description.md        # JD text (copied at init)
├── scoring.md                # rubric id + Scoring Results (stubbed at init)
├── matches.md                # List 1 (recent role), List 2 (previous roles), gaps
├── cover-letter-draft.md     # v1 — preserved forever
├── cover-letter-draft-v2.md  # after writing passes (v1 kept)
├── review-report.json        # independent-judge verdict (gate artifact, starlord pattern)
├── progress.json             # machine gate state (progress.py)
├── progress.md               # human checklist
└── run-log.md                # raw signals for the retro
```

(cover-letter-plan.md, resume.md, interview-prep.md move to the future
resume-and-prep companion skill.)

## 4. Portability and configuration

`assets/sources.json` — the only place paths live; SKILL.md and references/ reference
sources **by key**, never by hardcoded path:

```json
{
  "applications_root": "~/repos/wiki/notes/2026-applications",
  "word_budgets": { "cover_letter_default": 1000, "scoring_results_max_chars": 5000, "matches_max_chars": 10000 },
  "sources": {
    "mandatory": {
      "cv_master":            { "path": "~/repos/wiki/notes/2026-applications/master-templates/2026-09-Maksim-Zinovev-Automation-Tester-CV-master.md", "function": "CV source of truth: tense, facts, achievements; List 2 evidence" },
      "experience_records":   { "path": "~/repos/jobkit/experience-pieces.json", "function": "recent-role evidence pieces for matches List 1" },
      "rubric_full_time":     { "path": "~/repos/wiki/notes/2026-applications/scoring-rubric-full-time.md", "function": "scoring rubric for full-time roles" },
      "rubric_part_time_gig": { "path": "~/repos/wiki/notes/2026-applications/scoring-rubric-part-time-gig.md", "function": "scoring rubric for gig/part-time roles" }
    },
    "optional": {
      "job_search_context":  { "path": "~/repos/wiki/notes/job-search/job-search-2026.md", "function": "search context and constraints" },
      "ideal_job":            { "path": "~/repos/wiki/notes/job-search/ideal-job-2026.md", "function": "ideal-role profile" },
      "unslop_skill":         { "path": "~/repos/unslop/SKILL.md", "function": "human-voice rewriting pass; degraded mode = banned-terms scan only" },
      "better_cover_letters": { "path": "~/repos/wiki/.pi/skills/better-cover-letter-writing/SKILL.md", "function": "credibility rewrite pass; degraded mode = banned-terms scan only" }
    }
  },
  "waived": {}
}
```

Gate protocol: missing **mandatory** source → preflight exit 1 → agent asks the user
(interview tool, alternatives + recommendation) to fix the path or explicitly waive;
waiver recorded dated in `sources.json.waived` — approval is never silent, workflow
does not advance without it. Missing **optional** source → warning + flag; the
affected step adapts. `--config` points all scripts at a different sources.json.

## 4b. Tiered reflection protocol (cost-optimized LLM judge — starlord conformance-guard pattern)

Programmatic checks catch budgets/structure/clichés; the paragraph-rubric dimensions
(question coverage, source fidelity, demonstration, story continuity, evidence
economy, reader ease) need judgment. The judge runs in tiers so token cost stays
proportional to risk:

**Tier 0 — mechanical gate (always, zero LLM cost).** `verify_artifacts.py` runs
first; the judge never sees text that fails mechanical checks. No LLM tokens are
spent re-discovering what a regex catches.

**Tier 1 — fresh-context judge after step_3 draft (the one full run).** First full
draft is where issues live. Judge gets the locked criteria
(references/paragraph-rubric.md + cover-letter-writing.md don'ts + evidence rules),
the full draft, and matches.md — no run context. Fresh **context** is most of the
independence value, so this tier can be a cheap local Ollama model or a
fresh-context self-judge; a different model is a bonus, not a requirement.

**step_4 — conditional delta judge only.** Writing passes are ~90% mechanically
checkable (banned terms, em dashes, vocabulary — Tier 0). Judge runs **only if the
pass made substantive changes** (paragraph rewritten, evidence swapped, structure
moved); small targeted fixes (de-clichéing, typo edits, user-flagged single
replacements) skip it. When it runs, it is **delta-based**: previous
review-report.json + changed paragraphs only, verifying fixes and spot-checking
neighbors — never a fresh full-letter pass.

**Tier 2 — peer judge at step_audit (the paid final gate).** Independent peer
agent on the coms-net hub, or a second model; delta-based — consumes accumulated
review reports and judges the delta since last approval plus evidence-to-matches
traceability. Escalate from Tier 1 to Tier 2 early when the Tier 1 judge flags
something contested or the writer disagrees with a flag.

**Bounded and exhaustive.** Every judge run is one exhaustive structured pass (all
dimensions scored, every flagged sentence listed, JSON output per template) so
re-runs stay minimal. **Re-judge rounds capped at ≤2** per gate; anything still
contested escalates to the human checkpoint — every step already ends at a human
gate, so the LLM judge does not need to reach perfection.

Protocol per run:

1. Tier 0 passes → judge runs (tier per above); report written to
   `review-report.json` (from assets template): verdict, per-dimension scores,
   flagged items, judge identity, tier, scope (full/delta).
2. Fix every flagged item; re-judge (≤2 rounds), then escalate to the user.
3. Gate: `verify_artifacts.py --artifact review-report` fails the run when the
   report is missing or the verdict ≠ approved where required (step_3, step_audit,
   and step_4 only when its change log marks substantive changes);
   `progress.py --approve` for those steps is blocked without it. The reflection
   is enforced mechanically, not by memory.

Cost shape: 3 full judge runs → 1 full (step_3) + 1 conditional delta (step_4) +
1 delta (audit) ≈ half the token cost, most of the value intact.

## 4c. Scope enforcement model + script black-box contract (post-publish review, round 3)

Per-step scope (the "Scope" column of §10) is enforced in three layers:

1. **Mechanical** — script write surfaces are physically confined:
   `init_application.py` writes only inside the run folder it just created and
   refuses overwrite; `preflight.py` reads existence and records config only;
   `progress.py` dep gates refuse any out-of-order `--start/--approve`, so
   out-of-scope work cannot advance the gate; `verify_artifacts.py` validates
   only the step's expected artifacts — stray work earns nothing at the gate.
2. **Procedural** — each SKILL.md step defines its action list and a single
   output surface (step_0: preflight + init only; step_1: append Scoring
   Results to scoring.md, then the promotion gate: "record the decision and
   stop"). References repeat the boundary ("Only a promoted job reaches this
   step").
3. **Instructional** — references/operating-principles.md Scope limits: the run
   folder is the working scope; nothing outside the run folder, the configured
   sources, and `rules/` (retro only) is modified.

Residual gap (documented): raw tool calls are not physically sandboxed — stray
writes inside the run folder are possible but never gate artifacts; reads
outside scope are bounded only by layers 2-3. **Pending patch (round 3):**
add one line to operating-principles.md Scope limits — "All file writes go
through the skill's scripts; no raw writes outside the run folder." — to be
applied and committed with the next skill change.

**Script black-box contract:** agents consume script output, never script
source. Invocation comes from SKILL.md's scripts block, the per-step
procedures, and `progress.py --status` (which prints the current step's verify
command); `--help` is the only sanctioned peek. **Error-completeness invariant:**
every failure path in every script carries a `fix:` hint (verified true at
code review of all four scripts); a future script edit that adds a failure
path without a hint is a retro-level defect. Rationale: reading a ~200-line
script costs 2-3K tokens for zero decision value — the report and fix hints
carry everything needed to self-correct.

**Made explicit (round 4, user order):** the contract was inference-only until
round 4 — without an explicit instruction, agents will likely read script
source and consume the limited context window. SKILL.md's Scripts section now
states the rule verbatim and carries ten sample commands; operating-principles
Context economy carries the full rule with the run-log defect hook.

**Round 5 (user order):** bundled `rubric_full_time`, `rubric_part_time_gig`,
and `ideal_job` into `assets/` (flat) — the skill ships working defaults for
cloners instead of pointing at absent personal files; sources.json defaults
are now repo-relative; preflight.py verifies the three as bundled assets
(install-integrity check); wiki originals preserved untouched as history.
Reference fix: jd-analysis.md and matches-and-plan.md now state that every
source key resolves via the preflight table or sources.json, closing the
referential dead end found in the round-4 discussion. Privacy ledger: the
bundled files carry personal bands (salary targets, NSW location, part-time
hour caps) — publication explicitly ordered by the user.

**Round 6 (user order):** source keys may now hold a list of files;
`experience_records` became an array (jobkit pieces + the prepared STAR
stories file). preflight.py flattens lists into indexed entries
(`experience_records[1]`), gates each file individually, and --set/--waive
accept indexed addressing (`--set experience_records[1] <path>`); bare --set
or --waive on a list key dies with the index hint. matches-and-plan.md and
jd-analysis.md state the multi-file semantics; README documents the array
convention.

**Round 7 (user order, live-run findings):** run 18, the first live run
under the skill, skipped init by inference, read step_1 material during
step_0 (jd-analysis, rubric, CV master, precedent files, web searches), and
answered "Yes - step_0 done" with the run folder missing. Fixes: the
checkpoint protocol forbids inferred deviations and requires unmet
conditions named in the same breath as any status answer; step_0's on_fail
routes apparent-wrong instructions to the user. step_0 now lists its allowed
reads and bans read-ahead; Context economy repeats the ban. Structural
call, user option (a): every scored JD gets its run folder at init, even
when the job never promotes.

**Round 8 (user order):** read caps sanctioned — jd-analysis allows one
precedent scoring file, tail only, and caps web search at five results.
The step_0 checkpoint now requires the agent to restate the run rules in
its own words (naming the run-18 violations) before approval. Wiki scoring
notes stay the raw feed; init copies the JD into the run folder (user
confirmed). SKILL.md back at the 150-line cap after the restate line was
fused into the existing checkpoint line.

## 5. Canonical step map

| id | type | focus | rules remap |
|---|---|---|---|
| step_0 | context | preflight sources, init run folder | old step_0 unchanged |
| step_1 | analysis | JD understanding, rubric scoring, **promotion gate** | old step_1 (scoring part) |
| step_2 | planning | matches.md lists + gaps, hidden questions, evidence ranking, **rubric-validated paragraph plan** | old step_1 (matches/question part) |
| step_3 | drafting | cover letter v1, judged + rubric-scored | old step_2 |
| step_4 | rewriting | unslop + better-cover-letter-writing → v2, conditional delta judge | old step_3 |
| step_audit | verification | full verify matrix + independent judge + evidence cross-check | new |
| step_retro | learning loop | run-log → proposed rules, batch approval | new |
| step_5/6/7 | — | RESERVED for the resume-and-prep companion (plan extraction, resume, prep) | old steps 4/5/6 |

All seven active steps mandatory (no optional steps in v1). Rule `applies_to` YAML
values shift mechanically per the remap column (metadata only, prose untouched);
`rules/README.md` step-map table updated to match.

## 6. SKILL.md design — ≤150 lines

Budget strategy: SKILL.md carries **zero domain content** — only orchestration.

- Frontmatter + 6-line overview (what the skill does, run-folder pattern, scope note
  pointing resume/prep to the future companion).
- 3-line portability note: sources by key, `sources.json`, preflight gate.
- 5-line scripts usage block (four CLI signatures, one line each).
- 7 step sections × ~11 lines: YAML header (`id, type, depends_on, expectStatus,
  on_fail, rules[]` — locked format), 1-line Purpose, 3-4 numbered procedure lines,
  1-line checkpoint. All detail lives in references/, named per-step.

Anti-drift enforcement so a reference cannot be skipped:

1. Every step's Procedure line 1 is an imperative "Read `references/<file>.md`" —
   the SKILL.md itself never contains enough domain content to skip it.
2. `verify_artifacts.py` checks outputs against section names that exist **only in
   references/ and assets/** — unread reference ⇒ structurally non-conforming
   output ⇒ verify fails ⇒ `progress.py --approve` refuses.
3. `progress.py --status` prints the next step **with its reference file** — the
   resume-from-interruption path re-issues the JIT pointer mechanically.

## 7. Build order

1. Read all 19 rule files + companion skill files; distill `banned-terms.json`
   (workflow don'ts + unslop vocabulary + simonw pattern catalog, severity split).
2. Write `assets/` (sources.json, banned-terms.json, 5 templates).
3. Write `scripts/` (4) — each with `--help`, exit codes, self-describing errors.
4. Smoke-test scripts against a scratch run folder.
5. Write `references/` (7 files) — content distilled from workflow.md, self-contained,
   no reference to workflow.md or session-handoff. Paragraph rubric lives in its own
   file, loaded at step_2 planning and reused at step_3/4 assessment.
6. Write SKILL.md (≤150 lines).
7. Move `session-handoff.md` → `.local/`; add `.gitignore` (`.local/`).
8. Rule activation: flip 19 × `status: proposed → active` + `last_validated: 2026-09-16`;
   remap `applies_to` per §5; update rules/README step map; fix its stale gitignore
   bullet; open CHANGELOG.md (retro #1 batch entry).
9. Final audit: validate-metadata, checklist audit, line counts, preflight green,
   verify_artifacts regression on the 08 Peoplebank v2 letter + matches.md — the
   letter must fully pass (em-dash = 0, fail-severity banned terms 0, keyword
   coverage, body word budget); the matches checker must pass all structural and
   list checks on 07 + 08 and correctly FLAG the 10K budget violation on both
   historical files (07 = 11.6K, 08 = 15.0K — real violations, approved-era
   artifacts; the default cap stays 10K per workflow.md and is adjustable via
   sources.json word_budgets — no --max-chars override for matches, letters keep
   --max-words which mirrors the workflow's approved-budget-increase mechanism),
   "review"-severity banned-term hits reported, not blocking; progress.py gate
   test, review-report gate test.

## 8. Self-containment and history

- The skill carries everything it needs in SKILL.md/references/assets — **no
  references to workflow.md or session-handoff as instruction sources**.
- `workflow.md` stays untouched as historical narrative; `session-handoff.md` moves
  to `.local/` (gitignored, never shipped).

## 9. Documented deviations from the generic skills checklist

1. `rules/` kept in place — flat, machine-referenced corpus (round 1, item 16: OK).
2. `rules/README.md` + `CHANGELOG.md` — locked rule-governance design, not human
   onboarding docs.
3. `.local/` added to skill root — excluded via `.gitignore`; historical artifacts only.
4. Personal paths ship as **defaults inside assets/sources.json** (portable config),
   not hardcoded in prose.
5. `README.md` at repo root — GitHub-facing repo doc (user-requested post-build),
   unslop-written, 99 lines incl. skill-folder + output trees (budget raised
   on user request); not skill payload (pi loads SKILL.md, never README).
   `plans/` — build-plan archive (SKILL-PLAN.md + goal context), process record,
   not skill payload.

## 10. Techniques mapping (per plan template)

| Workflow step | Init | Rubric | HITL | Script | JSON artifact | Reflection | Scope | JIT context | Tool use | Bounded | Prog. disclosure | Checkpoint |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| step_0 preflight/init | ✅ | ✅ required files | ✅ waivers | ✅ preflight+init | ✅ progress.json | ❌ | ✅ run folder only | ✅ | ✅ | ✅ | ✅ | ✅ |
| step_1 JD scoring | ❌ | ✅ scoring rubric | ✅ promotion gate | ✅ verify scoring | ✅ | ✅ web-grounding | ✅ | ✅ rubric JIT | ✅ web search | ✅ ≤5,000 chars | ✅ | ✅ |
| step_2 matches+plan | ✅ sources read | ✅ paragraph rubric validates the PLAN | ✅ | ✅ verify matches | ✅ matches.md | ❌ | ✅ | ✅ references JIT | ✅ | ✅ 5-7/5-7/3-5 | ✅ | ✅ |
| step_3 draft | ❌ | ✅ paragraph rubric scores output | ✅ | ✅ verify letter | ✅ | ✅ **Tier 1 fresh-context judge** (full, exhaustive) | ✅ | ✅ craft JIT | ✅ | ✅ word budget, ≤2 re-judge rounds | ✅ | ✅ |
| step_4 writing passes | ❌ | ✅ banned terms = 0 | ✅ feedback-only | ✅ verify letter | ✅ v1 preserved | ✅ **conditional delta judge** (substantive changes only) | ✅ targeted rewrites | ✅ passes JIT | ✅ | ✅ ≤2 re-judge rounds | ✅ | ✅ |
| step_audit | ❌ | ✅ full matrix | ✅ | ✅ verify all | ✅ | ✅ **Tier 2 peer judge**, delta-based + cross-check | ✅ | ✅ | ✅ | ✅ ≤2 re-judge rounds | ✅ | ✅ |
| step_retro | ❌ | ✅ rule format | ✅ batch approval | ❌ | ✅ run-log | ✅ distill | ✅ rules/ only | ✅ | ❌ | ✅ ≤3 runs, ≤10 rules | ✅ | ✅ |

## 11. Acceptance criteria

- SKILL.md ≤ 150 lines; every script < 200 lines; every referenced path exists.
- `preflight.py` exits 0 on the default config; removing one mandatory file → exit 1
  naming it + fix command; `--waive` records a dated approval.
- `verify_artifacts.py` regression: 08 Peoplebank v2 letter passes (0 em dashes,
  0 fail-severity banned terms, keyword coverage, budgets); an injected cliché
  (e.g., "plays a crucial role") is caught.
- `progress.py`: `--approve step_3` rejected while step_2 unapproved; `--approve
  step_3` rejected when review-report.json is missing/unapproved; `--approve
  step_4` accepted after small targeted fixes with no substantive-change flag, and
  rejected after substantive changes without a delta review-report;
  `--status` prints the true position + the JIT reference for the next step.
- A judge run produces a valid review-report.json (verdict, dimensions, judge
  identity, tier, scope); the template validates.
- 0 rule files with `status: proposed`; CHANGELOG.md has the retro #1 entry;
  rules/README step map matches the new canonical ids.
- `session-handoff.md` lives in `.local/`; SKILL.md + references contain no mention
  of workflow.md or session-handoff.
- `wc -l SKILL.md` ≤ 150 is itself a checklist gate at final audit.
- Round-3 patch gate (post-publish): operating-principles.md contains the
  filesystem-scope line ("all file writes go through the skill's scripts"); the
  error-completeness invariant holds — every `bail()`/`die()` path in all four
  scripts carries a `fix:` hint, re-checked on any script edit (§4c).
