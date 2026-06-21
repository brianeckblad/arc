#!/usr/bin/env python3
"""Generate / refresh per-command help docs with YAML front-matter.

`docs/commands/<slug>.md` is the **single source of truth** for each command's
help.  The top of every registered command's doc is a YAML front-matter block::

    ---
    command: show address
    description: Show address objects in the active folder
    usage: show address
    feature_flag: show_address
    category: objects
    scope: folder
    api: GET /config/objects/v1/addresses
    ---
    # show address
    ...full help page...

The inline `?` / `<command> ?` help reads `description` + `usage` from the
front-matter; `help <command>` renders the body.

What this script does (idempotent):
  * ensures every registered command's doc has front-matter (adds it, preserving
    the existing body; never clobbers a human-edited block);
  * regenerates `docs/commands/index.md` (the catalog);
  * regenerates `docs/commands/api-reference.md` from the front-matter + registry.

Run:
    python dev/generate_command_docs.py             # ensure front-matter + regenerate
    python dev/generate_command_docs.py --check      # report gaps, write nothing (exit 1)

This runs automatically as part of `docsupdate` (dev/docsupdate.py).
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from app.commands.registry import CATEGORIES, COMMANDS  # noqa: E402
from app.docs import slugify  # noqa: E402
from app.paths import COMMAND_DOCS_DIR  # noqa: E402
from app.settings import command_help  # noqa: E402
from app.settings.command_help import parse_front_matter  # noqa: E402


def _seed_help() -> dict[str, tuple[str, str]]:
    """Return {command: (description, usage)} to seed front-matter on first run.

    Prefers the legacy ``settings/commands.yaml`` (so the curated descriptions and
    usage lines we built migrate into the docs), falling back to nothing.  After
    migration this file is removed and the docs are the source of truth.
    """
    legacy = REPO_ROOT / "settings" / "commands.yaml"
    if not legacy.exists():
        return {}
    try:
        import yaml

        parsed = yaml.safe_load(legacy.read_text(encoding="utf-8")) or {}
    except Exception:  # noqa: BLE001
        return {}
    seed: dict[str, tuple[str, str]] = {}
    for category, entries in parsed.items() if isinstance(parsed, dict) else []:
        if str(category).startswith("_") or not isinstance(entries, dict):
            continue
        for command, entry in entries.items():
            if isinstance(entry, str):
                seed[str(command)] = (entry.strip(), "")
            elif isinstance(entry, dict):
                seed[str(command)] = (
                    str(entry.get("description", "")).strip(),
                    str(entry.get("usage", "")).strip(),
                )
    return seed


_SEED = _seed_help()

# ---------------------------------------------------------------------------
# Command → SCM API endpoint map.
#
# Rescued from the old hand-maintained RESOURCES table so the endpoint data
# survives in the front-matter (the single source).  Only commands that map to a
# concrete REST endpoint appear here; the rest are derived at runtime:
#   * packet-tracer / test security-policy-match → client-side simulation
#   * live operational `show`/`ping`/`traceroute`/`request` → SSH via --remote
# ---------------------------------------------------------------------------
_API: dict[str, str] = {
    # objects
    "show address": "GET /config/objects/v1/addresses",
    "set address": "POST /config/objects/v1/addresses",
    "update address": "PUT /config/objects/v1/addresses/{id}",
    "delete address": "DELETE /config/objects/v1/addresses/{id}",
    "show address-group": "GET /config/objects/v1/address-groups",
    "set address-group": "POST /config/objects/v1/address-groups",
    "update address-group": "PUT /config/objects/v1/address-groups/{id}",
    "delete address-group": "DELETE /config/objects/v1/address-groups/{id}",
    "show service": "GET /config/objects/v1/services",
    "set service": "POST /config/objects/v1/services",
    "update service": "PUT /config/objects/v1/services/{id}",
    "delete service": "DELETE /config/objects/v1/services/{id}",
    "show service-group": "GET /config/objects/v1/service-groups",
    "set service-group": "POST /config/objects/v1/service-groups",
    "update service-group": "PUT /config/objects/v1/service-groups/{id}",
    "delete service-group": "DELETE /config/objects/v1/service-groups/{id}",
    "show tag": "GET /config/objects/v1/tags",
    "set tag": "POST /config/objects/v1/tags",
    "update tag": "PUT /config/objects/v1/tags/{id}",
    "delete tag": "DELETE /config/objects/v1/tags/{id}",
    "show external-dynamic-list": "GET /config/objects/v1/external-dynamic-lists",
    "set external-dynamic-list": "POST /config/objects/v1/external-dynamic-lists",
    "update external-dynamic-list": "PUT /config/objects/v1/external-dynamic-lists/{id}",
    "delete external-dynamic-list": "DELETE /config/objects/v1/external-dynamic-lists/{id}",
    "show application-group": "GET /config/objects/v1/application-groups",
    "show application-filter": "GET /config/objects/v1/application-filters",
    "show schedule": "GET /config/objects/v1/schedules",
    "show region": "GET /config/objects/v1/regions",
    "show hip-object": "GET /config/objects/v1/hip-objects",
    "show hip-profile": "GET /config/objects/v1/hip-profiles",
    "show log-forwarding-profile": "GET /config/objects/v1/log-forwarding-profiles",
    # security
    "show security policy": "GET /config/security/v1/security-rules",
    "delete security-rule": "DELETE /config/security/v1/security-rules/{id}",
    "show url-categories": "GET /config/security/v1/url-categories",
    "set url-category": "POST /config/security/v1/url-categories",
    "delete url-category": "DELETE /config/security/v1/url-categories/{id}",
    "show decryption-rules": "GET /config/security/v1/decryption-rules",
    "show decryption-profile": "GET /config/security/v1/decryption-profiles",
    "show dos-protection-rules": "GET /config/security/v1/dos-protection-rules",
    "show dos-protection-profile": "GET /config/security/v1/dos-protection-profiles",
    "show app-override-rules": "GET /config/security/v1/app-override-rules",
    "show profile-group": "GET /config/security/v1/profile-groups",
    "show anti-spyware-profile": "GET /config/security/v1/anti-spyware-profiles",
    "show vulnerability-profile": "GET /config/security/v1/vulnerability-protection-profiles",
    "show wildfire-profile": "GET /config/security/v1/wildfire-anti-virus-profiles",
    # network
    "show zone": "GET /config/network/v1/zones",
    "show nat-rules": "GET /config/network/v1/nat-rules",
    "show pbf-rules": "GET /config/network/v1/pbf-rules",
    "show ike-gateway": "GET /config/network/v1/ike-gateways",
    "show ipsec-tunnel": "GET /config/network/v1/ipsec-tunnels",
    "show interface": "GET /config/network/v1/ethernet-interfaces",
    "show interface all": "GET /config/network/v1/ethernet-interfaces",
    "show dns-proxy": "GET /config/network/v1/dns-proxies",
    "show sdwan-rules": "GET /config/network/v1/sdwan-rules",
    "show qos-profile": "GET /config/network/v1/qos-profiles",
    "show bgp-profile": "GET /config/network/v1/bgp-address-family-profiles",
    "show routing route": "GET /config/network/v1/routing/static-routes",
    "show routing summary": "GET /config/network/v1/virtual-routers",
    "show high-availability all": "GET /config/network/v1/ha",
    "show high-availability state": "GET /config/network/v1/ha",
    # identity
    "show authentication-profile": "GET /config/identity/v1/authentication-profiles",
    "show authentication-rules": "GET /config/identity/v1/authentication-rules",
    "show certificate-profile": "GET /config/identity/v1/certificate-profiles",
    "show tls-service-profile": "GET /config/identity/v1/tls-service-profiles",
    "show local-user": "GET /config/identity/v1/local-users",
    "show local-user-group": "GET /config/identity/v1/local-user-groups",
    "show radius-server": "GET /config/identity/v1/radius-server-profiles",
    "show mfa-server": "GET /config/identity/v1/mfa-servers",
    # setup / operations
    "show devices": "GET /config/setup/v1/devices",
    "show device": "GET /config/setup/v1/devices/{id}",
    "show device snippets": "GET /config/setup/v1/devices/{id}",
    "show snippet": "GET /config/setup/v1/snippets",
    "show snippets": "GET /config/setup/v1/snippets",
    "show snippets global": "GET /config/setup/v1/snippets",
    "show jobs all": "GET /config/setup/v1/jobs",
    "show jobs id": "GET /config/setup/v1/jobs/{id}",
    "show system info": "GET /config/setup/v1/devices/{id}",
    "commit": "POST /config/setup/v1/config-versions/candidate:push",
}


def _generated_api_map() -> dict[str, str]:
    """Return API notes for commands created from the generated endpoint catalog."""
    try:
        from app.commands.resource_catalog import CATALOG
    except Exception:  # noqa: BLE001 — stale/missing catalog should not block docs
        return {}
    out: dict[str, str] = {}
    for entry in CATALOG:
        command = str(entry.get("command", ""))
        method = str(entry.get("method", ""))
        base_url = str(entry.get("base_url", "")).rstrip("/")
        path = str(entry.get("path", ""))
        if command and method and path:
            out[command] = f"{method} {base_url}{path}"
    return out


def _generated_commands() -> set[str]:
    """Return command keys created from the generated endpoint catalog."""
    try:
        from app.commands.resource_catalog import CATALOG
    except Exception:  # noqa: BLE001 — stale/missing catalog should not block docs
        return set()
    return {str(entry.get("command", "")) for entry in CATALOG if entry.get("command")}


def _generated_usage_map() -> dict[str, str]:
    """Return command → usage for generated endpoint commands.

    This intentionally duplicates the lightweight usage convention from
    app.commands.generated so docs/front-matter can be refreshed even when the
    live registry has already loaded stale front-matter overrides.
    """
    try:
        from app.commands.resource_catalog import CATALOG
    except Exception:  # noqa: BLE001 — stale/missing catalog should not block docs
        return {}
    usage: dict[str, str] = {}
    for entry in CATALOG:
        command = str(entry.get("command", ""))
        if not command:
            continue
        path_params = " ".join(f"{name} <value>" for name in entry.get("path_params") or [])
        if command.startswith(("set ", "update ")):
            parts = [command]
            if path_params:
                parts.append(path_params)
            parts.append("json|file <payload-or-path>")
            usage[command] = " ".join(parts)
        elif command.startswith("delete ") and path_params:
            usage[command] = f"{command} {path_params}"
        else:
            usage[command] = command
    return usage


def _api_for(key: str) -> str:
    """Return a human-readable API note for a command."""
    if key in _API:
        return _API[key]
    generated = _generated_api_map()
    if key in generated:
        return generated[key]
    if key in ("packet-tracer", "test security-policy-match"):
        return "(client-side simulation of the folder rule base)"
    cmd = COMMANDS[key]
    if cmd.scope == "device" or (cmd.ssh_command is not None and key not in _API):
        return "(live device state — SSH via --remote)"
    return ""


def _front_matter(key: str) -> str:
    """Build the YAML front-matter block for a command from the live registry."""
    cmd = COMMANDS[key]
    seed_desc, seed_usage = _SEED.get(key, ("", ""))
    generated_usage = _generated_usage_map().get(key, "")
    description = seed_desc or cmd.description
    usage = generated_usage or seed_usage or cmd.usage
    lines = ["---", f"command: {_dq(key)}", f"description: {_dq(description)}"]
    if usage:
        lines.append(f"usage: {_dq(usage)}")
    if cmd.feature_flag:
        lines.append(f"feature_flag: {cmd.feature_flag}")
    lines.append(f"category: {cmd.category}")
    lines.append(f"scope: {cmd.scope}")
    api = _api_for(key)
    if api:
        lines.append(f"api: {_dq(api)}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def _dq(text: str) -> str:
    """Double-quote a YAML scalar, escaping backslashes and quotes."""
    return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'


def _doc_path(key: str) -> Path:
    return COMMAND_DOCS_DIR / f"{slugify(key)}.md"


def _has_front_matter(key: str) -> bool:
    path = _doc_path(key)
    if not path.exists():
        return False
    meta, _ = parse_front_matter(path.read_text(encoding="utf-8"))
    return bool(meta.get("command"))


def ensure_front_matter() -> list[str]:
    """Add front-matter to any registered command doc that lacks it.

    Preserves the existing Markdown body.  Returns the commands that were
    updated.  Never overwrites an existing front-matter block (human-owned).
    """
    updated: list[str] = []
    generated = _generated_commands()
    for key in COMMANDS:
        path = _doc_path(key)
        body = path.read_text(encoding="utf-8") if path.exists() else f"# {key}\n"
        meta, stripped_body = parse_front_matter(body)
        new_front_matter = _front_matter(key)
        if meta.get("command") and key not in generated:
            continue  # human-owned front-matter — leave it alone
        existing_front_matter = body[: body.find("---", 3) + 3] + "\n" if body.startswith("---") else ""
        if meta.get("command") and existing_front_matter == new_front_matter:
            continue
        path.write_text(new_front_matter + "\n" + stripped_body, encoding="utf-8")
        updated.append(key)
    return updated


def regenerate_index() -> None:
    """Rewrite docs/commands/index.md (the catalog) from the live registry."""
    lines = [
        "# Command Reference",
        "",
        "Use `help <command>` to open detailed docs for a command.",
        "",
    ]
    for key in sorted(COMMANDS):
        lines.append(f"- `{key}` — {COMMANDS[key].description}")
    lines.append("")
    (COMMAND_DOCS_DIR / "index.md").write_text("\n".join(lines), encoding="utf-8")


def regenerate_api_reference() -> None:
    """Rewrite docs/commands/api-reference.md from front-matter + the registry.

    Replaces the old hand-maintained RESOURCES table: the command→endpoint map
    now lives in each command's doc front-matter (``api:``), surfaced here.
    """
    lines = [
        "# ARC Command → SCM API Reference",
        "",
        "Generated from each command's doc front-matter (`api:` field) and the live",
        "registry. Regenerate with `python dev/generate_command_docs.py` (runs on `docsupdate`).",
        "",
    ]
    for category in sorted(CATEGORIES):
        lines += [f"## {category.title()}", "",
                  "| Command | Scope | Feature flag | SCM API |",
                  "|---|---|---|---|"]
        for key in sorted(CATEGORIES[category]):
            cmd = COMMANDS[key]
            flag = f"`{cmd.feature_flag}`" if cmd.feature_flag else "—"
            api = _api_for(key) or "—"
            lines.append(f"| `{key}` | {cmd.scope} | {flag} | {api} |")
        lines.append("")
    (COMMAND_DOCS_DIR / "api-reference.md").write_text("\n".join(lines), encoding="utf-8")


def _missing_front_matter() -> list[str]:
    return sorted(k for k in COMMANDS if not _has_front_matter(k))


def main() -> int:
    check_only = "--check" in sys.argv[1:]

    if check_only:
        missing = _missing_front_matter()
        for key in missing:
            print(f"  missing front-matter: docs/commands/{slugify(key)}.md")
        if missing:
            print(f"\n{len(missing)} command doc(s) missing front-matter — "
                  "run: python dev/generate_command_docs.py")
            return 1
        print(f"All {len(COMMANDS)} command docs have help front-matter")
        return 0

    updated = ensure_front_matter()
    # Re-read the freshly written front-matter so the index/API reference reflect
    # the migrated descriptions rather than the pre-migration code defaults.
    command_help.invalidate_cache()
    command_help.apply_overrides(COMMANDS)
    regenerate_index()
    regenerate_api_reference()
    print(f"Command docs: {len(COMMANDS)} total, {len(updated)} front-matter block(s) added")
    print("Regenerated: docs/commands/index.md, docs/commands/api-reference.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

