#!/usr/bin/env python3
"""Regenerate settings/features.json from ARC's command and API catalogs.

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

FEATURES_FILE = REPO_ROOT / "settings" / "features.json"

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
    """Preserve existing persisted states; new flags still default to false."""
    if not FEATURES_FILE.exists():
        return {}
    try:
        raw = json.loads(FEATURES_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}
    return {key: value for key, value in raw.items() if not key.startswith("_")}


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


def build_features() -> dict[str, object]:
    """Build a described, feature-first map with new flags defaulting to false."""
    catalog = _load_catalog()
    explicit = _explicit_flags()
    explicit_descriptions = _explicit_flag_descriptions()
    existing_states = _load_existing_states()

    features: dict[str, object] = {
        "_README": (
            "Generated by dev/generate_feature_flags.py from pulled OpenAPI specs "
            "and CommandDef.feature_flag values. Values are true | \"dev\" | false. "
            "New generated defaults are false: hidden and blocked until intentionally enabled. "
            "After editing, restart ARC. Inside ARC: feature show, feature enable|disable|dev <flag>."
        ),
        "_ORDER": "Grouped by category, then feature/resource. Flags under each feature are ordered: show, set/create, update, delete.",
        "_GLOSSARY": {
            "adnsr": "Advanced DNS Security Resolver",
            "cdug": "Cloud Dynamic User Groups",
            "ciedss": "Cloud Identity Engine Directory Sync Service",
            "cngfw": "Cloud NGFW",
            "iam": "Identity and Access Management",
            "ngts": "Next-Generation Trust Security",
            "sase": "Secure Access Service Edge",
        },
    }

    groups: dict[tuple[str, str], dict[str, object]] = {}
    emitted: set[str] = set()
    catalog_flags: set[str] = set()

    for entry in catalog:
        feature_flag = str(entry["feature_flag"])
        catalog_flags.add(feature_flag)
        action = _ACTION_BY_METHOD.get(str(entry.get("method", "")), "other")
        command = str(entry.get("command", ""))
        resource = _feature_resource(_resource_from_command(command))
        category = str(entry.get("category", "other"))
        group_key = (category, resource)
        group = groups.setdefault(
            group_key,
            {
                "category": category,
                "resource": resource,
                "specs": set(),
                "actions": defaultdict(dict),
            },
        )
        group["specs"].add(str(entry.get("spec", "unknown")))  # type: ignore[union-attr]
        action_flags = group["actions"][action]  # type: ignore[index]
        action_flags[feature_flag] = _short_summary(str(entry.get("summary", "")), command)

    remaining = sorted(explicit - catalog_flags)
    if remaining:
        for flag in remaining:
            action, resource = _resource_from_flag(flag)
            resource = _feature_resource(resource)
            group_key = ("explicit", resource)
            descriptions = explicit_descriptions.get(flag, [flag])
            group = groups.setdefault(
                group_key,
                {
                    "category": "explicit",
                    "resource": resource,
                    "specs": {"explicit-command"},
                    "actions": defaultdict(dict),
                },
            )
            action_flags = group["actions"][action]  # type: ignore[index]
            action_flags[flag] = _short_summary("; ".join(descriptions), flag)

    current_category = ""
    for category, resource in sorted(
        groups,
        key=lambda key: (_CATEGORY_LABELS.get(key[0], key[0]).lower(), _display_resource(key[1]).lower()),
    ):
        group = groups[(category, resource)]
        category_label = _CATEGORY_LABELS.get(category, category.replace("-", " ").title())
        if category != current_category:
            features[_comment_key("section", category)] = f"===== {category_label} ====="
            current_category = category

        actions = group["actions"]  # type: ignore[assignment]
        features[_comment_key(category, resource)] = (
            f"{category_label}: {_resource_flag_name(resource)}"
        )
        for action in _ACTION_ORDER:
            action_flags = actions.get(action, {})
            if not action_flags:
                continue
            for flag in sorted(action_flags):
                features[flag] = existing_states.get(flag, False)
                emitted.add(flag)

    remaining = sorted(explicit - emitted)
    if remaining:
        features["_section_EXPLICIT_UNGROUPED"] = "===== Explicit command flags not matched to generated features ====="
        for flag in remaining:
            features[flag] = existing_states.get(flag, False)

    return features


def render(features: dict[str, object]) -> str:
    return json.dumps(features, indent=2) + "\n"


def main() -> int:
    check_only = "--check" in sys.argv[1:]
    features = build_features()
    rendered = render(features)
    current = FEATURES_FILE.read_text(encoding="utf-8") if FEATURES_FILE.exists() else ""

    if check_only:
        if current != rendered:
            print("settings/features.json is STALE — run: python dev/generate_feature_flags.py")
            return 1
        count = sum(1 for key in features if not key.startswith("_"))
        print(f"feature flags current — {count} flag(s)")
        return 0

    FEATURES_FILE.write_text(rendered, encoding="utf-8")
    count = sum(1 for key in features if not key.startswith("_"))
    print(f"Wrote settings/features.json — {count} feature flag(s), new flags default false")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

