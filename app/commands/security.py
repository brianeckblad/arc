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
from app.commands.objects import _check_concurrent_modification


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

def _update_security_rule(ctx: ExecutionContext, args: dict) -> Any:
    """Update an existing security rule (GET→merge→PUT).

    Modifies one or more fields of a named security rule while preserving
    all other fields. The same pattern as update address / update service.

    Syntax:
      update security-rule <name> action <allow|deny|drop|reset-client|reset-server|reset-both>
      update security-rule <name> from <zone> [<zone2> ...]
      update security-rule <name> to <zone> [<zone2> ...]
      update security-rule <name> source <addr> [<addr2> ...]
      update security-rule <name> destination <addr> [<addr2> ...]
      update security-rule <name> application <app> [<app2> ...]
      update security-rule <name> service <svc> [<svc2> ...]
      update security-rule <name> description <text>
      update security-rule <name> tag <name>
      update security-rule <name> disabled true|false
      update security-rule <name> profile-group <name>
      update security-rule <name> position <n>   (move to position n in the rule list, 1-based)

    Examples:
      update security-rule Allow-Web action deny
      update security-rule Allow-Web from trust untrust
      update security-rule Allow-Web destination 10.1.0.0/24
      update security-rule Allow-Web application ssl http
      update security-rule Allow-Web description "Updated for Q3 audit"
      update security-rule Allow-Web position 3

    pan.dev: PUT /config/security/v1/security-rules/{id}
    """
    scm = require_scm(ctx)
    pos = args.get("_positional", [])
    name = pos[0] if pos else (args.get("name") or "")
    if not name or len(pos) < 2:
        raise ValueError(
            "Usage: update security-rule <name> <field> <value>\n"
            "  Fields: action | from | to | source | destination | application "
            "| service | description | tag | disabled | profile-group | position\n"
            "  e.g. update security-rule Allow-Web action deny\n"
            "       update security-rule Allow-Web from trust untrust\n"
            "       update security-rule Allow-Web position 3"
        )

    # 1. GET current rule
    items = scm.get_security_policy(folder=ctx.folder)
    obj = scm.find_by_name(items, name)
    if not obj:
        raise ValueError(
            f"Security rule '{name}' not found in folder '{ctx.folder}'.\n"
            "  Run [bold]show security policy[/bold] to see available rules."
        )
    obj = dict(obj)  # shallow copy — prevent mutation of cached API response
    rule_id = obj.pop("id")

    # 2. Apply the requested field change
    field = pos[1].lower()
    values = pos[2:]  # remaining tokens are the new value(s)

    _LIST_FIELDS = {"from", "to", "source", "destination", "application", "service", "tag"}
    _VALID_ACTIONS = {
        "allow", "deny", "drop",
        "reset-client", "reset-server", "reset-both",
    }

    if field == "action":
        action = values[0].lower() if values else ""
        if action not in _VALID_ACTIONS:
            raise ValueError(
                f"Unknown action: {action!r}\n"
                f"  Valid actions: {', '.join(sorted(_VALID_ACTIONS))}"
            )
        obj["action"] = action

    elif field in _LIST_FIELDS:
        if not values:
            raise ValueError(
                f"Provide at least one value for '{field}': "
                f"update security-rule {name} {field} <value> [<value2> ...]"
            )
        # 'tag' is a list field but named 'tag' in the API (may be singular)
        obj[field] = list(values)

    elif field == "description":
        obj["description"] = " ".join(values)

    elif field == "disabled":
        flag = (values[0].lower() if values else "true")
        if flag not in ("true", "false", "yes", "no", "1", "0"):
            raise ValueError(f"'disabled' expects true or false, got: {flag!r}")
        obj["disabled"] = flag in ("true", "yes", "1")

    elif field == "profile-group":
        group = " ".join(values)
        if not group:
            raise ValueError(f"Provide a profile group name: update security-rule {name} profile-group <name>")
        obj["profile_setting"] = {"group": [group]}

    elif field == "position":
        pos_val = values[0] if values else ""
        if not pos_val.isdigit() or int(pos_val) < 1:
            raise ValueError(
                f"Position must be a positive integer (1-based), got: {pos_val!r}\n"
                f"  e.g. update security-rule {name} position 3"
            )
        # Position is applied via a separate MOVE endpoint on the same rule.
        # SCM uses PUT with a 'position_keyword' or direct index; we store it
        # for use in the PUT payload.  Some SCM versions support 'position' field
        # directly on the object; others require a separate call.
        obj["position"] = int(pos_val)

    else:
        raise ValueError(
            f"Unknown field: {field!r}\n"
            "  Valid fields: action | from | to | source | destination | application "
            "| service | description | tag | disabled | profile-group | position"
        )

    # 3. PUT — re-fetch to detect concurrent modifications before overwriting.
    fresh_items = scm.get_security_policy(folder=ctx.folder)
    _check_concurrent_modification(obj, scm.find_by_name(fresh_items, name), name)
    scm.update_security_rule(rule_id, obj)
    return (
        f"[green]✓[/green] Security rule [bold]{name}[/bold] updated "
        f"([bold]{field}[/bold] = {' '.join(str(v) for v in values) or '(cleared)'})"
    )


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
    return f"[green]✓[/green] URL category [bold]{name}[/bold] created  (id: {(result or {}).get('id', '?')})"


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
    "update security-rule": CommandDef(
        description="Update an existing security rule — update security-rule <name> <field> <value>",
        category="security",
        scope="folder",
        api_handler=_update_security_rule,
        ssh_command=None,
        render="raw",
        feature_flag="update_security",
        usage="update security-rule <name> action|from|to|source|destination|application|service|description|tag|disabled|position <value>",
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


