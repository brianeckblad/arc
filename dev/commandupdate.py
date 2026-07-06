#!/usr/bin/env python3
"""Update contextual ? help specs for all enabled ARC commands.

This is the engine behind both the LLM trigger word ``commandupdate`` and
the in-shell ``dev command-structure update`` command.  Run either way to get
the same result.

  python dev/commandupdate.py             # update all commands missing a spec
  python dev/commandupdate.py --check     # dry-run: report what would be added
  python dev/commandupdate.py "set tag"   # update one specific command

Output is written to ``settings/command-structure-generated.json`` (tier 1g).
The hand-curated ``settings/command-structure.json`` is never modified.

**When to run:**
  After enabling a new feature flag (``feature enable <flag>``), run this so
  the newly visible command gets full field-by-field ``?`` help immediately.
  You can also run it any time to fill gaps shown by ``command-structure list``.

**Tier priority (highest first):**
  1  hand-curated   settings/command-structure.json
  1g cli-generated  settings/command-structure-generated.json  ← written here
  2  openapi-spec   app/settings/field_catalog.py
  3  usage-parsed   runtime fallback, not persisted

Running this script promotes tier-3 / NO-SPEC commands to tier 1g.
To get richer metadata (named choices, hints), edit the hand-curated file.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from app.paths import COMMAND_STRUCTURE_GENERATED_JSON
from app.commands.registry import COMMANDS
from app.settings.features import load_features, is_enabled, feature_state
from app.settings.command_structure import (
    load_command_structure,
    _parse_usage_spec,
    invalidate_cache,
)


def _cs_tier(key: str, struct: dict, field_catalog_keys: set) -> str:
    """Return the tier code for a command key."""
    from app.paths import COMMAND_STRUCTURE_JSON
    # Tier 1: hand-curated JSON
    try:
        raw = json.loads(COMMAND_STRUCTURE_JSON.read_text(encoding="utf-8"))
        if key in raw or (not " " in key and f"set {key}" in raw):
            return "1"
        # Also covers auto-derived update/delete
        set_version = key.replace("update ", "set ", 1).replace("delete ", "set ", 1)
        if set_version in raw or f"set {set_version}" in raw:
            return "1"
    except Exception:
        pass
    # Tier 1g: cli-generated JSON
    if COMMAND_STRUCTURE_GENERATED_JSON.exists():
        try:
            gen = json.loads(COMMAND_STRUCTURE_GENERATED_JSON.read_text(encoding="utf-8"))
            if key in gen:
                return "1g"
        except Exception:
            pass
    # Tier 2: field_catalog
    if key in field_catalog_keys:
        return "2"
    # Tier 3: usage-string parseable
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
        help="Overwrite existing tier-1g entries (default: skip already-generated).",
    )
    parser.add_argument(
        "--all-tiers", action="store_true",
        help="Include commands already at tier 1, 2, or 1g (normally skipped).",
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

    # Load existing generated entries
    existing: dict = {}
    if COMMAND_STRUCTURE_GENERATED_JSON.exists():
        try:
            existing = json.loads(COMMAND_STRUCTURE_GENERATED_JSON.read_text(encoding="utf-8"))
        except Exception:
            existing = {}

    added, skipped, failed = [], [], []

    for key in candidates:
        tier = _cs_tier(key, struct, fc_keys)

        if not args.all_tiers and tier == "1":
            skipped.append((key, "tier 1 (hand-curated — not overwritten)"))
            continue
        if not args.force and tier == "1g":
            skipped.append((key, "tier 1g (already generated — use --force to overwrite)"))
            continue
        if not args.all_tiers and tier == "2":
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

        existing[key] = spec
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
        # Only show skip info when targeting a specific command
        for k, reason in skipped:
            print(f"\nSkipped: {k}  [{reason}]")

    if not args.check and added:
        COMMAND_STRUCTURE_GENERATED_JSON.write_text(
            json.dumps(existing, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        print(
            f"\nWrote {len(existing)} total entries to "
            f"settings/command-structure-generated.json"
        )
        print(
            "\nContextual ? help is now active for the updated commands.\n"
            "To get richer field metadata (choices, hints), copy the entry to\n"
            "settings/command-structure.json and edit the field metadata in\n"
            "app/settings/command_structure.py (_FIELD_LIBRARY)."
        )
    elif args.check:
        print("\n[dry run — nothing written]")

    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
