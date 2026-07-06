"""Security commands (security-rules, URL categories, decryption, DoS, profiles).

SCM-backed (configuration): security rules, URL categories, decryption rules,
DoS protection, app-override, profile groups, security profiles.

See docs/commands/ and docs/scm-api/specs/ngfw-security.md for full API reference.
PAN-OS CLI equivalents: show security-policy, show decryption-policy, etc.
"""

from __future__ import annotations

from typing import Any

from app.commands.base import (
    CommandDef,
    ExecutionContext,
    delete_handler,
    require_scm,
    show_handler,
)


# ---------------------------------------------------------------------------
# Command table — merged into COMMANDS by registry.py
#
# Plain list commands use show_handler(<SCMClient method>) from base.py;
# pan.dev: GET /config/security/v1/<resource>?folder=<folder>
#
# NOTE: `test security-policy-match` lives in
# app/commands/packet_tracer.py (simulates the folder rule base).
# ---------------------------------------------------------------------------

COMMANDS: dict[str, CommandDef] = {
    "show security policy": CommandDef(
        description="Show security policy rules in the active folder",
        category="security",
        scope="folder",
        api_handler=show_handler("get_security_policy"),
        ssh_command=None,
        render="security_policy",
        feature_flag="show_security_policy",
    ),
    "show url-categories": CommandDef(
        description="Show custom URL categories in the active folder",
        category="security",
        scope="folder",
        api_handler=show_handler("get_url_categories"),
        ssh_command=None,
        render="url_categories",
        feature_flag="show_url_categories",
    ),
}


_EXTRA_COMMANDS: dict[str, CommandDef] = {
    "show decryption-rules": CommandDef(
        description="Show decryption rules in the active folder",
        category="security",
        scope="folder",
        api_handler=show_handler("get_decryption_rules"),
        ssh_command="show running decryption-policy",
        render="list",
        feature_flag="decryption_policy",
    ),
    "show decryption-profile": CommandDef(
        description="Show decryption profiles in the active folder",
        category="security",
        scope="folder",
        api_handler=show_handler("get_decryption_profiles"),
        ssh_command=None,
        render="list",
        feature_flag="decryption_policy",
    ),
    "show dos-protection-rules": CommandDef(
        description="Show DoS protection rules in the active folder",
        category="security",
        scope="folder",
        api_handler=show_handler("get_dos_protection_rules"),
        ssh_command="show dos-protection rule all",
        render="list",
        feature_flag="dos_protection",
    ),
    "show dos-protection-profile": CommandDef(
        description="Show DoS protection profiles in the active folder",
        category="security",
        scope="folder",
        api_handler=show_handler("get_dos_protection_profiles"),
        ssh_command=None,
        render="list",
        feature_flag="dos_protection",
    ),
    "show app-override-rules": CommandDef(
        description="Show application override rules in the active folder",
        category="security",
        scope="folder",
        api_handler=show_handler("get_app_override_rules"),
        ssh_command=None,
        render="list",
        feature_flag="app_override",
    ),
    "show profile-group": CommandDef(
        description="Show security profile groups in the active folder",
        category="security",
        scope="folder",
        api_handler=show_handler("get_profile_groups"),
        ssh_command=None,
        render="list",
        feature_flag="profile_groups",
    ),
    "show anti-spyware-profile": CommandDef(
        description="Show anti-spyware profiles in the active folder",
        category="security",
        scope="folder",
        api_handler=show_handler("get_anti_spyware_profiles"),
        ssh_command=None,
        render="list",
        feature_flag="security_profiles",
    ),
    "show vulnerability-profile": CommandDef(
        description="Show vulnerability protection profiles in the active folder",
        category="security",
        scope="folder",
        api_handler=show_handler("get_vulnerability_protection_profiles"),
        ssh_command=None,
        render="list",
        feature_flag="security_profiles",
    ),
    "show wildfire-profile": CommandDef(
        description="Show WildFire anti-virus profiles in the active folder",
        category="security",
        scope="folder",
        api_handler=show_handler("get_wildfire_profiles"),
        ssh_command=None,
        render="list",
        feature_flag="security_profiles",
    ),
}

COMMANDS.update(_EXTRA_COMMANDS)


# ---------------------------------------------------------------------------
# Write handlers — security config (configure mode)
# ---------------------------------------------------------------------------

def _set_url_category(ctx: ExecutionContext, args: dict) -> Any:
    """Create a custom URL category.

    Usage: set url-category <name> type url-list list <url1> [<url2> ...]
           set url-category <name> type category-match list <cat1>
    pan.dev: POST /config/security/v1/url-categories
    """
    scm = require_scm(ctx)
    pos = args.get("_positional", [])
    name = pos[0] if pos else (args.get("name") or "")
    if not name:
        raise ValueError("Usage: set url-category <name> type url-list list <url1> [<url2> ...]")
    cat_type = args.get("type", "url-list")
    try:
        list_idx = [p.lower() for p in pos].index("list")
        entries = pos[list_idx + 1:]
    except ValueError:
        entries = []
    if not entries:
        raise ValueError("At least one URL/category entry required after 'list'")
    payload = {"name": name, "folder": ctx.folder, "type": cat_type, "list": entries}
    result  = scm.create_url_category(payload)
    return f"[green]✓[/green] URL category [bold]{name}[/bold] created  (id: {result.get('id', '?')})"


_WRITE_COMMANDS: dict[str, CommandDef] = {
    "delete security-rule": CommandDef(
        description="Delete a security rule — delete security-rule <name>",
        category="security",
        scope="folder",
        api_handler=delete_handler(
            "Security rule", "get_security_policy", "delete_security_rule",
            usage="Usage: delete security-rule <name>",
        ),
        ssh_command=None,
        render="raw",
        feature_flag="delete_security",
    ),
    "set url-category": CommandDef(
        description="Create a custom URL category — set url-category <name> type url-list list <url1>",
        category="security",
        scope="folder",
        api_handler=_set_url_category,
        ssh_command=None,
        render="raw",
        feature_flag="create_url_category",
    ),
    "delete url-category": CommandDef(
        description="Delete a URL category — delete url-category <name>",
        category="security",
        scope="folder",
        api_handler=delete_handler(
            "URL category", "get_url_categories", "delete_url_category",
            usage="Usage: delete url-category <name>",
        ),
        ssh_command=None,
        render="raw",
        feature_flag="delete_security",
    ),
}

COMMANDS.update(_WRITE_COMMANDS)


