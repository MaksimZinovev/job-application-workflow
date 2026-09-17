#!/usr/bin/env python3
"""Preflight gate for the job-application skill.

Loads assets/sources.json (the only place paths live), expands and
existence-checks every configured source plus the skill's bundled assets,
and blocks the workflow while a mandatory source is unresolved.

Usage:
  preflight.py [--config <sources.json>] [--set <key> <path>]
               [--waive <key> --note "..."]

stdout  resolved-path table (key | required | status | resolved path)
stderr  failure details for missing mandatory sources; warnings for
        missing optional sources
exit    0 all mandatory resolved (waivers count) · 1 mandatory missing
        · 2 usage/config error
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import NoReturn

SKILL_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CONFIG = SKILL_ROOT / "assets" / "sources.json"
BUNDLED_ASSETS = [
    "sources.json",
    "banned-terms.json",
    "scoring-template.md",
    "matches-template.md",
    "review-report-template.json",
    "progress-template.md",
    "run-log-template.md",
    "scoring-rubric-full-time.md",
    "scoring-rubric-part-time-gig.md",
    "ideal-job-2026.md",
]


def die(msg: str, hint: str = "", code: int = 2) -> NoReturn:
    print(f"preflight: {msg}", file=sys.stderr)
    if hint:
        print(f"  fix: {hint}", file=sys.stderr)
    sys.exit(code)


def load_config(path: str | None) -> tuple[Path, dict]:
    p = Path(path).expanduser() if path else DEFAULT_CONFIG
    if not p.exists():
        die(f"config not found: {p}", "pass --config <sources.json> or create assets/sources.json")
    try:
        return p, json.loads(p.read_text())
    except json.JSONDecodeError as e:
        die(f"config is not valid JSON: {p} ({e})", "fix the JSON syntax")


def resolve_path(raw: str) -> Path:
    p = Path(raw).expanduser()
    return p if p.is_absolute() else (SKILL_ROOT / p).resolve()


def iter_sources(cfg: dict):
    """Flatten config entries; a key may hold one source or a list of them."""
    for req in ("mandatory", "optional"):
        for key, entry in cfg.get("sources", {}).get(req, {}).items():
            if isinstance(entry, list):
                for i, item in enumerate(entry):
                    yield req, f"{key}[{i}]", item
            else:
                yield req, key, entry


def check(cfg: dict) -> tuple[list[dict], list[dict]]:
    """Return (table rows, missing mandatory entries). Waived = resolved."""
    waived = cfg.get("waived", {})
    rows, missing = [], []
    for req, key, entry in iter_sources(cfg):
        rp = resolve_path(entry.get("path", ""))
        status = "OK" if rp.exists() else "MISSING"
        if status == "MISSING" and key in waived:
            status = "WAIVED" if req == "mandatory" else "WAIVED-OPTIONAL"
        elif status == "MISSING" and req == "optional":
            status = "OPTIONAL-MISSING"
        if status == "MISSING" and req == "mandatory":
            missing.append({"key": key, "path": str(rp), "function": entry.get("function", "")})
        rows.append({"key": key, "required": req, "status": status, "path": str(rp),
                     "function": entry.get("function", "")})
    return rows, missing


def check_bundled() -> list[str]:
    return [name for name in BUNDLED_ASSETS if not (SKILL_ROOT / "assets" / name).exists()]


def print_table(rows: list[dict]) -> None:
    w = max(len(r["key"]) for r in rows) if rows else 3
    print(f"{'key':<{w}}  {'required':<9}  {'status':<17}  resolved path")
    for r in rows:
        print(f"{r['key']:<{w}}  {r['required']:<9}  {r['status']:<17}  {r['path']}")


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Resolve and gate every configured source before a run starts.",
        epilog="stdout: table · stderr: failures/warnings · exit 0 ok / 1 blocked / 2 usage")
    ap.add_argument("--config", help="path to an alternative sources.json")
    ap.add_argument("--set", nargs=2, metavar=("KEY", "PATH"),
                    help="record a corrected path for a source key, then re-check")
    ap.add_argument("--waive", metavar="KEY",
                    help="record an explicit, dated user waiver for a missing mandatory source")
    ap.add_argument("--note", default="", help="reason for --waive (required; recorded in sources.json)")
    a = ap.parse_args()

    cfg_path, cfg = load_config(a.config)

    if a.set:
        key, path = a.set
        m = re.fullmatch(r"([^\[\]]+?)(?:\[(\d+)\])?", key)
        base, idx = m.group(1), m.group(2)
        hit = False
        for group in ("mandatory", "optional"):
            bucket = cfg.get("sources", {}).get(group, {})
            if base not in bucket:
                continue
            hit = True
            entry = bucket[base]
            if isinstance(entry, list):
                if idx is None:
                    die(f"'{base}' holds a list of sources",
                        f"use --set {base}[<index>] <path>, or edit assets/sources.json to add/remove entries")
                if not 0 <= int(idx) < len(entry):
                    die(f"index {idx} out of range for '{base}' ({len(entry)} entries)",
                        "see assets/sources.json")
                entry[int(idx)]["path"] = path
                cfg.setdefault("waived", {}).pop(f"{base}[{idx}]", None)
            else:
                if idx is not None:
                    die(f"'{base}' is a single source, not a list", f"use --set {base} <path>")
                entry["path"] = path
                cfg.setdefault("waived", {}).pop(base, None)
        if not hit:
            die(f"unknown source key: {base}", "see keys in assets/sources.json")
        cfg_path.write_text(json.dumps(cfg, indent=2) + "\n")
        print(f"set {key} -> {path}")

    if a.waive:
        key = a.waive
        m = re.fullmatch(r"([^\[\]]+?)(?:\[(\d+)\])?", key)
        base, idx = m.group(1), m.group(2)
        hit = False
        for group in ("mandatory", "optional"):
            bucket = cfg.get("sources", {}).get(group, {})
            if base not in bucket:
                continue
            hit = True
            if isinstance(bucket[base], list) and idx is None:
                die(f"'{base}' holds a list of sources",
                    f"waive a specific entry: --waive {base}[<index>] --note \"<why>\"")
            if not isinstance(bucket[base], list) and idx is not None:
                die(f"'{base}' is a single source, not a list", f"waive with --waive {base} --note \"<why>\"")
        if not hit:
            die(f"unknown source key: {base}", "see keys in assets/sources.json")
        if not a.note.strip():
            die(f"waiver for {key} needs an explicit --note", "approval is never silent")
        cfg.setdefault("waived", {})[key] = {"note": a.note.strip(), "date": date.today().isoformat()}
        cfg_path.write_text(json.dumps(cfg, indent=2) + "\n")
        print(f"waived {key} (dated {cfg['waived'][key]['date']}): {a.note.strip()}")

    rows, missing = check(cfg)
    for name in check_bundled():
        print(f"WARNING bundled skill asset missing: assets/{name}", file=sys.stderr)
    print_table(rows)

    for m in missing:
        print(
            f"BLOCKED mandatory source missing: {m['key']}\n"
            f"  path:     {m['path']}\n"
            f"  function: {m['function']}\n"
            f"  fix:      preflight.py --set {m['key']} <path>   (or edit {cfg_path})\n"
            f"  waiver:   preflight.py --waive {m['key']} --note \"<why this is acceptable>\"",
            file=sys.stderr)
    if missing:
        sys.exit(1)

    for r in rows:
        if r["status"] == "OPTIONAL-MISSING":
            print(f"WARNING optional source missing: {r['key']} — flag it at the interview "
                  f"tool; affected steps adapt (degraded mode where the reference says so)",
                  file=sys.stderr)
    print("preflight: OK — all mandatory sources resolved")


if __name__ == "__main__":
    main()
