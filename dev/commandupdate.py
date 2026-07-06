#!/usr/bin/env python3
"""Update contextual ? help specs for all enabled ARC commands.

This is the engine behind both the LLM trigger word ``commandupdate`` and
the in-shell ``dev command-structure update`` command.  Run either way to get
the same result.

  python dev/commandupdate.py             # update all commands missing a spec
  python dev/commandupdate.py --check     # dry-run: report what would be added
  python dev/commandupdate.py "set tag"   # update one specific command
  python dev/commandupdate.py --force     # also refresh existing override:false entries

Output is written to ``settings/command-structure.json`` as override:false entries.
Entries with ``override:true`` are never touched — they are hand-curated.

**When to run:**
  After enabling a new feature flag (``feature enable <flag>``), run this so
  the newly visible command gets full field-by-field ``?`` help immediately.

**To lock a generated entry (prevent commandupdate from overwriting it):**
  Open settings/command-structure.json, find the entry, change override to true,
  then edit the 'args' or switch to 'fields' (string list) for cleaner editing.

**Tier in command-structure list:**
  override:true  → hand-curated (green)
  override:false → cli-generated (cyan)
  field_catalog  → openapi-spec  (blue)
  usage-parsed   → runtime only  (yellow)
  absent         → NO SPEC       (red)
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from app.paths import COMMAND_STRUCTURE_JSON
from app.commands.registry import COMMANDS
from app.settings.features import load_features, is_enabled, feature_state
from app.settings.command_structure import (
    load_command_structure,
    _parse_usage_spec,
    invalidate_cache,
)


def _cs_tier(key: str, struct: dict, field_catalog_keys: set) -> str:
    """Return the tier code for a command key."""
    entry = struct.get(key)
    if entry:
        if entry.get("override", False):
            return "1"   # hand-curated
        return "1g"      # cli-generated (override:false)
    if key in field_catalog_keys:
        return "2"
    cmd_def = COMMANDS.get(key)
    if cmd_def and cmd_def.usage:
        spec = _parse_usage_spec(key, cmd_def.usage)
        if spec:
            return "3"
    return "-"


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__.splitlines()[0],
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "command", nargs="?",
        help="Specific command to update (e.g. 'set tag'). Default: all enabled.",
    )
    parser.add_argument(
        "--check", action="store_true",
        help="Dry-run: report what would be added without writing anything.",
    )
    parser.add_argument(
        "--force", action="store_true",
        help="Also refresh existing override:false (cli-generated) entries.",
    )
    parser.add_argument(
        "--all-tiers", action="store_true",
        help="Include commands at all tiers (normally skips tier 1, 2).",
    )
    args = parser.parse_args()

    features = load_features()
    invalidate_cache()
    struct = load_command_structure()

    try:
        from app.settings.field_catalog import FIELD_CATALOG
        fc_keys = set(FIELD_CATALOG.keys())
    except Exception:
        fc_keys = set()

    # Determine which commands to process
    if args.command:
        candidates = [args.command.strip()]
    else:
        candidates = sorted([
            k for k in COMMANDS
            if COMMANDS[k].feature_flag
            and is_enabled(features, COMMANDS[k].feature_flag, False)
        ])

    # Load the single command-structure.json
    existing: dict = {}
    if COMMAND_STRUCTURE_JSON.exists():
        try:
            existing = json.loads(COMMAND_STRUCTURE_JSON.read_text(encoding="utf-8"))
        except Exception:
            existing = {}

    added, skipped, failed = [], [], []

    for key in candidates:
        tier = _cs_tier(key, struct, fc_keys)

        # Never touch override:true (hand-curated) unless --all-tiers
        if tier == "1" and not args.all_tiers:
            skipped.append((key, "override:true (hand-curated — change override to false to allow updates)"))
            continue
        # Skip already-generated unless --force
        if tier == "1g" and not args.force and not args.all_tiers:
            skipped.append((key, "override:false already generated (use --force to refresh)"))
            continue
        # Skip openapi-spec entries
        if tier == "2" and not args.all_tiers:
            skipped.append((key, "tier 2 (openapi-spec — already covered)"))
            continue

        cmd_def = COMMANDS.get(key)
        if not cmd_def:
            failed.append((key, "not found in COMMANDS registry"))
            continue

        spec = _parse_usage_spec(key, cmd_def.usage or "")
        if not spec:
            failed.append((key, "no parseable usage string — add usage= to CommandDef"))
            continue

        existing[key] = {"override": False, "args": spec}
        added.append((key, spec))

    # Report
    if added:
        print(f"\n{'DRY RUN — ' if args.check else ''}Added/updated {len(added)} command(s):\n")
        for k, spec in added:
            fields = " ".join(a["name"] for a in spec[:8])
            suffix = " …" if len(spec) > 8 else ""
            print(f"  {k:<50} {fields}{suffix}")
    else:
        print("\nNothing new to add.")

    if failed:
        print(f"\nCould not generate specs for {len(failed)} command(s):")
        for k, reason in failed:
            print(f"  {k:<50} [{reason}]")

    if skipped and args.command:
        for k, reason in skipped:
            print(f"\nSkipped: {k}  [{reason}]")

    if not args.check and added:
        COMMAND_STRUCTURE_JSON.write_text(
            json.dumps(existing, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        total_override_true = sum(
            1 for v in existing.values()
            if isinstance(v, dict) and v.get("override", False)
        )
        total_override_false = sum(
            1 for v in existing.values()
            if isinstance(v, dict) and not v.get("override", True)
        )
        print(
            f"\nWrote settings/command-structure.json — "
            f"{total_override_true} hand-curated (override:true), "
            f"{total_override_false} generated (override:false)"
        )
        print(
            "\nContextual ? help is now active for the updated commands.\n"
            "To lock an entry: set override:true in command-structure.json.\n"
            "To get richer metadata (choices, hints): use a 'fields' list and\n"
            "add metadata to app/settings/command_structure.py (_FIELD_LIBRARY)."
        )
    elif args.check:
        print("\n[dry run — nothing written]")

    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
