#!/usr/bin/env python3
"""Regenerate the settings/features/ glossary from ARC's command and API catalogs.

Flags are split into small per-domain files so each is consumable on its own:
  settings/features/scm-<spec>.json    one per pulled OpenAPI spec (adnsr, cloudngfw-objects, ...)
  settings/features/panos-ops.json     PAN-OS operational command families
  settings/features/panos-config.json  PAN-OS config tree (break-glass)
  settings/features/curated.json       hand-written command flags
A legacy single settings/features.json is absorbed (values preserved) and removed.

Feature flags must not be a hand-maintained shortlist.  The generated resource
catalog is derived from the pulled pan.dev OpenAPI specs; this script turns every
catalog operation plus every explicit ``CommandDef.feature_flag`` into a JSON flag
entry.  All generated defaults are ``false`` (fail closed) until an operator or
feature owner intentionally enables one.
"""

from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

FEATURES_FILE = REPO_ROOT / "settings" / "features.json"   # legacy single file
FEATURES_DIR = REPO_ROOT / "settings" / "features"

_ACTION_BY_METHOD = {
    "GET": "show",
    "POST": "create",
    "PUT": "update",
    "PATCH": "update",
    "DELETE": "delete",
}

_ACTION_ORDER = ("show", "create", "update", "delete", "other")

_ACTION_LABEL = {
    "show": "show/read",
    "create": "set/create",
    "update": "update",
    "delete": "delete",
    "other": "other",
}

_ACRONYM_LABELS = {
    "adnsr": "Advanced DNS Security Resolver (ADNSR)",
    "cdug": "Cloud Dynamic User Groups (CDUG)",
    "ciedss": "Cloud Identity Engine Directory Sync Service (CIE-DSS)",
    "cngfw": "Cloud NGFW (cngfw)",
    "iam": "Identity and Access Management (IAM)",
    "ngts": "Next-Generation Trust Security (NGTS)",
    "sase": "Secure Access Service Edge (SASE)",
}

_CATEGORY_LABELS = {
    "adnsr": "Advanced DNS Security Resolver (ADNSR)",
    "auth": "Authentication",
    "cdug": "Cloud Dynamic User Groups (CDUG)",
    "ciedss": "Cloud Identity Engine Directory Sync Service (CIE-DSS)",
    "cloudngfw": "Cloud NGFW",
    "device": "NGFW device settings",
    "device-onboarding": "Device onboarding",
    "iam": "Identity and Access Management (IAM)",
    "identity": "Identity services",
    "incidents": "SCM incidents",
    "network": "NGFW network configuration",
    "ngfw-operations": "NGFW live operations",
    "ngts": "Next-Generation Trust Security",
    "objects": "NGFW objects",
    "operations": "SCM config operations",
    "posture": "Posture management",
    "sase": "Secure Access Service Edge (SASE)",
    "security": "NGFW security services",
    "setup": "SCM setup",
    "subscription": "SCM subscriptions/licensing",
    "tenancy": "Tenant Service Groups / tenancy",
}


def _load_catalog() -> list[dict]:
    from app.commands.resource_catalog import CATALOG

    return list(CATALOG)


def _explicit_flags() -> set[str]:
    from app.commands.registry import COMMANDS

    return {cmd.feature_flag for cmd in COMMANDS.values() if cmd.feature_flag}


def _explicit_flag_descriptions() -> dict[str, list[str]]:
    """Return flag → human descriptions from explicit registered commands."""
    from app.commands.registry import COMMANDS

    descriptions: dict[str, list[str]] = defaultdict(list)
    for command, command_def in COMMANDS.items():
        if command_def.feature_flag:
            descriptions[command_def.feature_flag].append(f"{command} — {command_def.description}")
    return {flag: sorted(lines) for flag, lines in descriptions.items()}


def _load_existing_states() -> dict[str, object]:
    """Preserve persisted states from the glossary dir AND the legacy file."""
    states: dict[str, object] = {}
    paths = []
    if FEATURES_FILE.exists():
        paths.append(FEATURES_FILE)
    if FEATURES_DIR.is_dir():
        paths.extend(sorted(FEATURES_DIR.glob("*.json")))
    for path in paths:
        try:
            raw = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        if isinstance(raw, dict):
            states.update({k: v for k, v in raw.items() if not k.startswith("_")})
    return states


def _slug(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")
    return slug or "feature"


def _resource_from_command(command: str) -> str:
    _verb, _space, resource = command.partition(" ")
    return resource.strip() or command.strip()


def _resource_from_flag(flag: str) -> tuple[str, str]:
    """Return (action, resource) for an explicit flag not present in the catalog."""
    for action in ("show", "create", "update", "delete"):
        prefix = f"{action}_"
        if flag.startswith(prefix):
            return action, flag[len(prefix):].replace("_", "-")
    return "other", flag.replace("_", "-")


def _display_resource(resource: str) -> str:
    """Return a readable resource name without product-prefix noise."""
    parts = resource.split()
    if parts and parts[0] in _ACRONYM_LABELS:
        parts = parts[1:]
    return " ".join(parts).replace("-", " ").strip().title() or resource.replace("-", " ").title()


def _feature_resource(resource: str) -> str:
    """Normalize command resource tokens into the feature users expect to edit.

    Examples:
      ``adnsr bad-domains id`` -> ``bad-domains``
      ``cngfw addresses``      -> ``addresses``
    """
    parts = resource.split()
    if parts and parts[0] in _ACRONYM_LABELS:
        parts = parts[1:]
    if parts and parts[-1] == "id":
        parts = parts[:-1]
    return " ".join(parts) or resource


def _resource_flag_name(resource: str) -> str:
    """Return the compact resource name shown in features.json comments."""
    return _feature_resource(resource).replace("-", " ").replace(" ", "_")


def _short_summary(text: str, fallback: str) -> str:
    summary = " ".join((text or fallback).split())
    return summary[:157] + "..." if len(summary) > 160 else summary


def _comment_key(*parts: str) -> str:
    """Return a readable ignored JSON key (leading underscore)."""
    return "_" + "_".join(_slug(part) for part in parts if part)


def _action_summary(action: str, flag_summaries: dict[str, str]) -> str:
    """Summarize one action in a compact way for the feature comment."""
    summaries = sorted(set(flag_summaries.values()))
    shown = ", ".join(summaries[:2])
    if len(summaries) > 2:
        shown += f", +{len(summaries) - 2} more"
    return f"{_ACTION_LABEL[action]}: {shown}"


# Curated (hand-written) command flags live in the same glossary file as
# their spec siblings, so e.g. show_address sits next to the generated
# ngfw-objects flags. Device-scoped curated commands are live-device (SSH)
# operations -> they belong with the PAN-OS op families.
_CURATED_CATEGORY_FILES = {
    "objects": "scm-ngfw-objects",
    "security": "scm-ngfw-security",
    "network": "scm-ngfw-network",
    "identity": "scm-ngfw-identity",
    "setup": "scm-ngfw-setup",
    "operations": "scm-ngfw-setup",      # jobs/commit live in the setup spec
    "diagnostics": "scm-ngfw-security",  # packet-tracer simulates the rule base
}


def _explicit_flag_meta() -> dict[str, tuple[str, str]]:
    """flag -> majority (category, scope) across the commands it gates."""
    from collections import Counter

    from app.commands.registry import COMMANDS

    per_flag: dict[str, Counter] = defaultdict(Counter)
    for command_def in COMMANDS.values():
        if command_def.feature_flag:
            per_flag[command_def.feature_flag][(command_def.category, command_def.scope)] += 1
    return {flag: counts.most_common(1)[0][0] for flag, counts in per_flag.items()}


def _carry_state(flag: str, existing: dict[str, object]) -> object:
    """Preserve state across the per-action -> per-resource read/write rename.

    A new ``<resource>_read`` flag inherits ON/dev if any old ``show_<resource>``
    flag had it; ``<resource>_write`` inherits from the old create/update/delete
    flags. Exact-name matches (curated, panos, unrenamed) pass straight through.
    """
    if flag in existing:
        return existing[flag]
    old_names: list[str] = []
    if flag.endswith("_read"):
        base = flag[: -len("_read")]
        old_names = [f"show_{base}", f"show_{base}_id"]
    elif flag.endswith("_write"):
        base = flag[: -len("_write")]
        old_names = [f"create_{base}", f"update_{base}", f"delete_{base}", f"delete_{base}_id"]
    values = [existing[name] for name in old_names if name in existing]
    if any(value is True for value in values):
        return True
    if any(str(value).lower() == "dev" for value in values):
        return "dev"
    return False


def _flag_file(flag: str, catalog_flag_specs: dict[str, str],
               explicit_meta: dict[str, tuple[str, str]]) -> str:
    """Return the glossary file stem that owns *flag*."""
    if flag in catalog_flag_specs:
        return f"scm-{catalog_flag_specs[flag]}"
    if flag.startswith("panos_config"):
        return "panos-config"
    if flag.startswith("panos_"):
        return "panos-ops"
    meta = explicit_meta.get(flag)
    if meta:
        category, scope = meta
        if scope == "device":
            return "panos-ops"  # curated live-device command (SSH/--remote)
        mapped = _CURATED_CATEGORY_FILES.get(category)
        if mapped:
            return mapped
    return "curated"


def _file_readme(stem: str) -> str:
    kind = {
        "panos-ops": "PAN-OS operational command families plus curated live-device commands (ping, logs, system state - SSH/--remote). ",
        "panos-config": "PAN-OS device-local config tree — BREAK-GLASS recovery only. "
                        "config_recovery stays on; enable others only when SCM is unreachable. ",
        "curated": "Fallback for flags with no derivable domain (normally empty). ",
    }.get(stem, f"Generated SCM command flags for the {stem.removeprefix('scm-')} spec. ")
    return (
        kind + "Values: true | \"dev\" | false (new flags default false — fail closed). "
        "Regenerated by dev/generate_feature_flags.py (values preserved). "
        "Inside ARC: feature show | feature find <text> | feature enable|disable|dev <flag>."
    )


def build_feature_files() -> dict[str, dict[str, object]]:
    """Build {file_stem: ordered flag map} — one small file per domain."""
    catalog = _load_catalog()
    explicit = _explicit_flags()
    explicit_descriptions = _explicit_flag_descriptions()
    existing_states = _load_existing_states()

    catalog_flag_specs: dict[str, str] = {
        str(entry["feature_flag"]): str(entry.get("spec", "unknown")) for entry in catalog
    }
    explicit_meta = _explicit_flag_meta()

    groups: dict[tuple[str, str], dict[str, object]] = {}
    catalog_flags: set[str] = set()

    for entry in catalog:
        feature_flag = str(entry["feature_flag"])
        catalog_flags.add(feature_flag)
        action = _ACTION_BY_METHOD.get(str(entry.get("method", "")), "other")
        command = str(entry.get("command", ""))
        resource = _feature_resource(_resource_from_command(command))
        category = str(entry.get("category", "other"))
        group = groups.setdefault(
            (category, resource),
            {"category": category, "resource": resource, "specs": set(),
             "actions": defaultdict(dict)},
        )
        group["specs"].add(str(entry.get("spec", "unknown")))  # type: ignore[union-attr]
        group["actions"][action][feature_flag] = _short_summary(  # type: ignore[index]
            str(entry.get("summary", "")), command)

    for flag in sorted(explicit - catalog_flags):
        action, resource = _resource_from_flag(flag)
        resource = _feature_resource(resource)
        descriptions = explicit_descriptions.get(flag, [flag])
        group = groups.setdefault(
            ("explicit", resource),
            {"category": "explicit", "resource": resource,
             "specs": {"explicit-command"}, "actions": defaultdict(dict)},
        )
        group["actions"][action][flag] = _short_summary("; ".join(descriptions), flag)  # type: ignore[index]

    files: dict[str, dict[str, object]] = {}
    emitted: set[str] = set()

    def _file_map(stem: str) -> dict[str, object]:
        if stem not in files:
            files[stem] = {"_README": _file_readme(stem)}
        return files[stem]

    for category, resource in sorted(
        groups,
        key=lambda key: (_CATEGORY_LABELS.get(key[0], key[0]).lower(),
                         _display_resource(key[1]).lower()),
    ):
        group = groups[(category, resource)]
        category_label = _CATEGORY_LABELS.get(category, category.replace("-", " ").title())
        actions = group["actions"]  # type: ignore[assignment]
        # A group's flags may span files (explicit groups mixing panos + curated);
        # emit each flag into its owning file, with the group comment per file.
        by_file: dict[str, list[tuple[str, str]]] = {}
        for action in _ACTION_ORDER:
            for flag in sorted(actions.get(action, {})):
                by_file.setdefault(_flag_file(flag, catalog_flag_specs, explicit_meta), []).append((action, flag))
        for stem, action_flags in by_file.items():
            target = _file_map(stem)
            target[_comment_key(category, resource)] = (
                f"{category_label}: {_resource_flag_name(resource)}"
            )
            for _action, flag in action_flags:
                target[flag] = _carry_state(flag, existing_states)
                emitted.add(flag)

    for flag in sorted(explicit - emitted):
        target = _file_map(_flag_file(flag, catalog_flag_specs, explicit_meta))
        target[flag] = _carry_state(flag, existing_states)

    return files


def render(features: dict[str, object]) -> str:
    return json.dumps(features, indent=2) + "\n"


def main() -> int:
    check_only = "--check" in sys.argv[1:]
    files = build_feature_files()

    expected = {f"{stem}.json": render(payload) for stem, payload in files.items()}
    stale: list[str] = []
    if FEATURES_DIR.is_dir():
        for path in FEATURES_DIR.glob("*.json"):
            if path.name not in expected and path.name != "local.json":
                stale.append(path.name)

    if check_only:
        drift = list(stale)
        if FEATURES_FILE.exists():
            drift.append("settings/features.json (legacy — should be absorbed)")
        for name, rendered in expected.items():
            path = FEATURES_DIR / name
            if not path.exists() or path.read_text(encoding="utf-8") != rendered:
                drift.append(name)
        if drift:
            print("settings/features/ is STALE — run: python dev/generate_feature_flags.py")
            for name in drift[:10]:
                print(f"  drift: {name}")
            return 1
        total = sum(1 for payload in files.values() for k in payload if not k.startswith("_"))
        print(f"feature flags current — {total} flag(s) across {len(files)} file(s)")
        return 0

    FEATURES_DIR.mkdir(parents=True, exist_ok=True)
    for name, rendered in expected.items():
        (FEATURES_DIR / name).write_text(rendered, encoding="utf-8")
    for name in stale:
        (FEATURES_DIR / name).unlink()
        print(f"removed stale {name}")
    if FEATURES_FILE.exists():
        FEATURES_FILE.unlink()
        print("absorbed + removed legacy settings/features.json")
    total = sum(1 for payload in files.values() for k in payload if not k.startswith("_"))
    print(f"Wrote settings/features/ — {total} feature flag(s) across {len(files)} file(s), new flags default false")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

