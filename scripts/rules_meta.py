"""Shared rule metadata for the rule-digest and check-loop scripts.

Single source of truth for: (a) frontmatter facts from rules/*.md,
(b) step lists from SKILL.md, (c) the evidence kind each rule's check
file demands (verbatim quote vs written confirmation), (d) which
artifact each step's loop quotes from. Imported by build_digests.py,
check_rules.py, and verify_artifacts.py so the three never drift
apart. Stdlib only.
"""

import re
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
RULES_DIR = SKILL_ROOT / "rules"
SKILL_FILE = SKILL_ROOT / "SKILL.md"

# Every rule of every step gets a check file in the per-rule loop
# (check_rules.py). Two evidence kinds, demanded by rule type:
#   content rules (check/style/judgment) at artifact steps -> `quote`:
#     a span copied verbatim from the step's artifact (script-verified).
#   process rules (protocol/architecture), and content rules at steps
#     without an artifact -> `confirmation`: a written statement of how
#     the rule is honored (script-verified non-empty, no filler).
CONTENT_TYPES = {"check", "style", "judgment"}
PROCESS_TYPES = {"protocol", "architecture"}

# Step id -> run-folder artifact its loop rules are checked against.
# Steps without an entry run no loop (no content artifact to quote).
STEP_ARTIFACTS = {
    "step_1": "scoring.md",
    "step_2": "matches.md",
    "step_3": "cover-letter-draft.md",
    "step_4": "cover-letter-draft-v2.md",
}


def norm(rule_id: str) -> str:
    """Canonical key: underscores (frontmatter ids use them; SKILL.md
    lists and filenames use hyphens)."""
    return rule_id.strip().strip("`").replace("-", "_")


def display(key: str) -> str:
    """Display form: hyphens (matches SKILL.md lists and filenames)."""
    return key.replace("_", "-")


def _scalar(fm: str, key: str) -> str:
    m = re.search(rf"^{key}:\s*(.+)$", fm, re.M)
    return m.group(1).strip().strip('"') if m else ""


def _prose_expect(text: str) -> str:
    """Full ## Rule prose, whitespace-collapsed — fallback when frontmatter
    lacks `expect` (13 of 19 files keep it in prose only). Accuracy over
    brevity: the digest is agent-facing raw text, not rendered markdown."""
    m = re.search(r"^##\s+Rule\s*\n(.+?)\n##\s", text, re.M | re.S)
    if not m:
        return ""
    return re.sub(r"\s+", " ", m.group(1)).strip().replace("|", "/")


def load_rules() -> dict[str, dict]:
    """{underscored id -> meta} for every rules/rule-*.md file."""
    rules: dict[str, dict] = {}
    for f in sorted(RULES_DIR.glob("rule-*.md")):
        text = f.read_text()
        m = re.match(r"^---\n(.*?)\n---", text, re.S)
        if not m:
            raise SystemExit(f"rules_meta: {f.name} has no frontmatter")
        fm = m.group(1)
        rid = norm(_scalar(fm, "id") or f.stem)
        om = re.search(r'^\s+action:\s*"(.*)"', fm, re.M)
        rules[rid] = {
            "id": rid,
            "file": f,
            "type": _scalar(fm, "type"),
            "expect": _scalar(fm, "expect") or _prose_expect(text),
            "on_fail": om.group(1) if om else "",
            "applies_to": [
                norm(s)
                for s in re.findall(r"[\w-]+", _applies_to(fm))
            ],
        }
    return rules


def _applies_to(fm: str) -> str:
    m = re.search(r"^applies_to:\s*\[(.*)\]", fm, re.M)
    return m.group(1) if m else ""


def load_steps() -> list[dict]:
    """Ordered step list parsed from SKILL.md's yaml blocks:
    [{id, rules: [underscored keys]}] in declaration order."""
    steps: list[dict] = []
    for m in re.finditer(r"```yaml\s*\n(\{.*?\})\s*\n```", SKILL_FILE.read_text(), re.S):
        block = m.group(1)
        sid = re.search(r"id:\s*(\w+)", block)
        rls = re.search(r"rules:\s*\[([^\]]*)\]", block)
        if not sid or not rls:
            continue
        steps.append(
            {
                "id": sid.group(1),
                "rules": [norm(r) for r in re.findall(r"[\w-]+", rls.group(1))],
            }
        )
    if not steps:
        raise SystemExit("rules_meta: no step yaml blocks found in SKILL.md")
    return steps


def loop_rules(step_id: str, rules: dict[str, dict] | None = None,
               steps: list[dict] | None = None) -> list[dict]:
    """ALL rules of a step, in SKILL.md list order — every one gets a
    check file in the writer's loop."""
    rules = rules or load_rules()
    steps = steps or load_steps()
    step = next((s for s in steps if s["id"] == step_id), None)
    if not step:
        return []
    return [rules[r] for r in step["rules"] if r in rules]


def quote_rules(step_id: str, rules: dict[str, dict] | None = None,
                steps: list[dict] | None = None) -> list[dict]:
    """Content-type rules of a step — the ones whose evidence is a
    verbatim quote from the artifact. The judge's rules_audit covers
    exactly these (a process rule cannot be quoted from the artifact)."""
    return [m for m in loop_rules(step_id, rules, steps)
            if m["type"] in CONTENT_TYPES]


def needs_quote(meta: dict, step_id: str) -> bool:
    """True when the gate demands a verbatim artifact quote for this
    rule: a content rule at a step that has an artifact."""
    return meta["type"] in CONTENT_TYPES and step_id in STEP_ARTIFACTS