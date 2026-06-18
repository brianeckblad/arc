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
    require_scm,
    translation_pending,
)


# ---------------------------------------------------------------------------
# Handlers
# ---------------------------------------------------------------------------

def _show_security_policy(ctx: ExecutionContext, args: dict) -> Any:
    """List security rules (pre-position) in the active SCM folder.

    pan.dev: GET /config/security/v1/security-rules?folder=<folder>&position=pre
    """
    scm = require_scm(ctx)
    return scm.get_security_policy(folder=ctx.folder)


def _show_url_categories(ctx: ExecutionContext, args: dict) -> Any:
    """List custom URL categories in the active SCM folder.

    pan.dev: GET /config/security/v1/url-categories?folder=<folder>
    """
    scm = require_scm(ctx)
    return scm.get_url_categories(folder=ctx.folder)


def _pending_test_security_policy_match(ctx: ExecutionContext, args: dict) -> str:
    if not args.get("source") or not args.get("destination"):
        raise RuntimeError(
            "Usage: test security-policy-match source <ip> destination <ip> "
            "[application <app>] [protocol <n>] [destination-port <n>]"
        )
    return translation_pending("test security-policy-match")


# ---------------------------------------------------------------------------
# SSH command builders
# ---------------------------------------------------------------------------

def _ssh_test_spm(args: dict) -> str:
    src   = args.get("source", "")
    dst   = args.get("destination", "")
    app   = args.get("application", "any")
    proto = args.get("protocol", "6")
    dport = args.get("destination-port", "80")
    return (
        f"test security-policy-match source {src} destination {dst} "
        f"application {app} protocol {proto} destination-port {dport}"
    )


# ---------------------------------------------------------------------------
# Command table — merged into COMMANDS by registry.py
# ---------------------------------------------------------------------------

COMMANDS: dict[str, CommandDef] = {
    "show security policy": CommandDef(
        description="Show security policy rules in the active folder",
        category="security",
        scope="folder",
        api_handler=_show_security_policy,
        ssh_command=None,
        render="security_policy",
        feature_flag="show_security_policy",
    ),
    "show url-categories": CommandDef(
        description="Show custom URL categories in the active folder",
        category="security",
        scope="folder",
        api_handler=_show_url_categories,
        ssh_command=None,
        render="url_categories",
        feature_flag="show_url_categories",
    ),
    "test security-policy-match": CommandDef(
        description=(
            "Test security policy match — "
            "test security-policy-match source <ip> destination <ip> "
            "application <app> protocol <n> destination-port <n>"
        ),
        category="security",
        scope="device",
        api_handler=_pending_test_security_policy_match,
        ssh_command=_ssh_test_spm,
        render="raw",
        feature_flag="test_security_policy_match",
    ),
}


# ---------------------------------------------------------------------------
# Additional handlers — unimplemented security commands
# ---------------------------------------------------------------------------

def _show_decryption_rules(ctx: ExecutionContext, args: dict) -> Any:
    """pan.dev: GET /config/security/v1/decryption-rules?folder=<folder>"""
    scm = require_scm(ctx)
    return scm.get_decryption_rules(folder=ctx.folder)


def _show_decryption_profiles(ctx: ExecutionContext, args: dict) -> Any:
    """pan.dev: GET /config/security/v1/decryption-profiles?folder=<folder>"""
    scm = require_scm(ctx)
    return scm.get_decryption_profiles(folder=ctx.folder)


def _show_dos_protection_rules(ctx: ExecutionContext, args: dict) -> Any:
    """pan.dev: GET /config/security/v1/dos-protection-rules?folder=<folder>"""
    scm = require_scm(ctx)
    return scm.get_dos_protection_rules(folder=ctx.folder)


def _show_dos_protection_profiles(ctx: ExecutionContext, args: dict) -> Any:
    """pan.dev: GET /config/security/v1/dos-protection-profiles?folder=<folder>"""
    scm = require_scm(ctx)
    return scm.get_dos_protection_profiles(folder=ctx.folder)


def _show_app_override_rules(ctx: ExecutionContext, args: dict) -> Any:
    """pan.dev: GET /config/security/v1/app-override-rules?folder=<folder>"""
    scm = require_scm(ctx)
    return scm.get_app_override_rules(folder=ctx.folder)


def _show_profile_groups(ctx: ExecutionContext, args: dict) -> Any:
    """pan.dev: GET /config/security/v1/profile-groups?folder=<folder>"""
    scm = require_scm(ctx)
    return scm.get_profile_groups(folder=ctx.folder)


def _show_anti_spyware_profiles(ctx: ExecutionContext, args: dict) -> Any:
    """pan.dev: GET /config/security/v1/anti-spyware-profiles?folder=<folder>"""
    scm = require_scm(ctx)
    return scm.get_anti_spyware_profiles(folder=ctx.folder)


def _show_vulnerability_profiles(ctx: ExecutionContext, args: dict) -> Any:
    """pan.dev: GET /config/security/v1/vulnerability-protection-profiles?folder=<folder>"""
    scm = require_scm(ctx)
    return scm.get_vulnerability_protection_profiles(folder=ctx.folder)


def _show_wildfire_profiles(ctx: ExecutionContext, args: dict) -> Any:
    """pan.dev: GET /config/security/v1/wildfire-anti-virus-profiles?folder=<folder>"""
    scm = require_scm(ctx)
    return scm.get_wildfire_profiles(folder=ctx.folder)


_EXTRA_COMMANDS: dict[str, CommandDef] = {
    "show decryption-rules": CommandDef(
        description="Show decryption rules in the active folder",
        category="security",
        scope="folder",
        api_handler=_show_decryption_rules,
        ssh_command="show running decryption-policy",
        render="list",
        feature_flag="decryption_policy",
    ),
    "show decryption-profile": CommandDef(
        description="Show decryption profiles in the active folder",
        category="security",
        scope="folder",
        api_handler=_show_decryption_profiles,
        ssh_command=None,
        render="list",
        feature_flag="decryption_policy",
    ),
    "show dos-protection-rules": CommandDef(
        description="Show DoS protection rules in the active folder",
        category="security",
        scope="folder",
        api_handler=_show_dos_protection_rules,
        ssh_command="show dos-protection rule all",
        render="list",
        feature_flag="dos_protection",
    ),
    "show dos-protection-profile": CommandDef(
        description="Show DoS protection profiles in the active folder",
        category="security",
        scope="folder",
        api_handler=_show_dos_protection_profiles,
        ssh_command=None,
        render="list",
        feature_flag="dos_protection",
    ),
    "show app-override-rules": CommandDef(
        description="Show application override rules in the active folder",
        category="security",
        scope="folder",
        api_handler=_show_app_override_rules,
        ssh_command=None,
        render="list",
        feature_flag="app_override",
    ),
    "show profile-group": CommandDef(
        description="Show security profile groups in the active folder",
        category="security",
        scope="folder",
        api_handler=_show_profile_groups,
        ssh_command=None,
        render="list",
        feature_flag="profile_groups",
    ),
    "show anti-spyware-profile": CommandDef(
        description="Show anti-spyware profiles in the active folder",
        category="security",
        scope="folder",
        api_handler=_show_anti_spyware_profiles,
        ssh_command=None,
        render="list",
        feature_flag="security_profiles",
    ),
    "show vulnerability-profile": CommandDef(
        description="Show vulnerability protection profiles in the active folder",
        category="security",
        scope="folder",
        api_handler=_show_vulnerability_profiles,
        ssh_command=None,
        render="list",
        feature_flag="security_profiles",
    ),
    "show wildfire-profile": CommandDef(
        description="Show WildFire anti-virus profiles in the active folder",
        category="security",
        scope="folder",
        api_handler=_show_wildfire_profiles,
        ssh_command=None,
        render="list",
        feature_flag="security_profiles",
    ),
}

COMMANDS.update(_EXTRA_COMMANDS)


# ---------------------------------------------------------------------------
# Write handlers — security config (configure mode)
# ---------------------------------------------------------------------------

def _delete_security_rule(ctx: ExecutionContext, args: dict) -> Any:
    """Delete a security rule by name.

    Usage: delete security-rule <name>
    pan.dev: DELETE /config/security/v1/security-rules/{id}
    """
    scm  = require_scm(ctx)
    name = (args.get("name") or "").strip()
    if not name:
        raise ValueError("Usage: delete security-rule <name>")
    rules  = scm.get_security_policy(folder=ctx.folder)
    obj_id = scm._find_id_by_name(rules, name)
    if not obj_id:
        raise ValueError(f"Security rule '{name}' not found in folder '{ctx.folder}'")
    scm.delete_security_rule(obj_id)
    return f"[green]✓[/green] Security rule [bold]{name}[/bold] deleted."


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


def _delete_url_category(ctx: ExecutionContext, args: dict) -> Any:
    """Delete a URL category.  Usage: delete url-category <name>"""
    scm  = require_scm(ctx)
    name = (args.get("name") or "").strip()
    if not name:
        raise ValueError("Usage: delete url-category <name>")
    cats   = scm.get_url_categories(folder=ctx.folder)
    obj_id = scm._find_id_by_name(cats, name)
    if not obj_id:
        raise ValueError(f"URL category '{name}' not found in folder '{ctx.folder}'")
    scm.delete_url_category(obj_id)
    return f"[green]✓[/green] URL category [bold]{name}[/bold] deleted."


_WRITE_COMMANDS: dict[str, CommandDef] = {
    "delete security-rule": CommandDef(
        description="Delete a security rule — delete security-rule <name>",
        category="security",
        scope="folder",
        api_handler=_delete_security_rule,
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
        api_handler=_delete_url_category,
        ssh_command=None,
        render="raw",
        feature_flag="delete_security",
    ),
}

COMMANDS.update(_WRITE_COMMANDS)


