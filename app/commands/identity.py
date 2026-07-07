"""Identity commands (auth profiles, certificates, local users, server profiles).

All commands target SCM /config/identity/v1.  See docs/commands/ and
docs/scm-api/specs/ngfw-identity.md for full API reference.

PAN-OS CLI equivalents (show mode):
  show authentication-profile <name>    → authentication-profiles
  show certificate-profile <name>       → certificate-profiles
  show local-user <name>                → local-users
  show radius-server <name>             → radius-server-profiles
  show user ip-user-mapping             → SSH live state (--remote only)
"""

from __future__ import annotations

from typing import Any

from app.commands.base import CommandDef, ExecutionContext, require_device, require_scm, show_handler


# ---------------------------------------------------------------------------
# Handlers — SCM config commands are built with show_handler() from base.py;
# pan.dev: GET /config/identity/v1/<resource>?folder=<folder>
#
# Handler below — live device only (SSH / --remote)
# ---------------------------------------------------------------------------

def _show_user_ip_mapping(ctx: ExecutionContext, args: dict) -> Any:
    """Live user-to-IP mapping (device state — use --remote).

    This is a runtime table maintained by the firewall; it does not exist in SCM.
    Run with --remote to query a live device.
    """
    device = require_device(ctx)
    hostname = device.get("hostname") or device.get("name") or "device"
    return (
        "User-IP mapping is live device state — not stored in SCM.\n"
        f"  Run:  show user ip-user-mapping all --remote   to query {hostname}."
    )


def _set_local_user(ctx: ExecutionContext, args: dict) -> Any:
    """Create a local user in the active folder.

    Usage:
      set local-user <name> password <password>  [description <text>]  [disabled]
      set local-user <name> password <password>  email <addr>

    Examples:
      set local-user jsmith password Secr3t!  email jsmith@example.com
      set local-user svc-vpn password P@ssw0rd  description "VPN service account"
    """
    scm = require_scm(ctx)
    pos = args.get("_positional", [])
    name = pos[0] if pos else (args.get("name") or "")
    if not name:
        raise ValueError(
            "Usage: set local-user <name> password <password>  [email <addr>]  [description <text>]"
        )
    pos_lower = [p.lower() for p in pos]
    password = ""
    if "password" in pos_lower:
        pw_idx = pos_lower.index("password")
        password = pos[pw_idx + 1] if pw_idx + 1 < len(pos) else ""
    if not password:
        raise ValueError("Password is required: set local-user <name> password <password>")

    payload: dict = {"name": name, "folder": ctx.folder, "password": password}
    if "email" in pos_lower:
        em_idx = pos_lower.index("email")
        payload["email"] = pos[em_idx + 1] if em_idx + 1 < len(pos) else ""
    if args.get("description"):
        payload["description"] = args["description"]
    if "disabled" in pos_lower:
        payload["disabled"] = True

    result = scm.create_local_user(payload)
    return (
        f"[green]✓[/green] Local user [bold]{name}[/bold] created\n"
        f"  folder: {ctx.folder}  id: {(result or {}).get('id', '?')}"
    )


def _delete_local_user(ctx: ExecutionContext, args: dict) -> Any:
    """Delete a local user.  Usage: delete local-user <name>"""
    scm = require_scm(ctx)
    name = (args.get("name") or "").strip()
    if not name:
        raise ValueError("Usage: delete local-user <name>")
    items = scm.get_local_users(folder=ctx.folder)
    user_id = scm.find_id_by_name(items, name)
    if not user_id:
        raise ValueError(
            f"Local user '{name}' not found in folder '{ctx.folder}'.  "
            "Run [bold]show local-user[/bold] to see available users."
        )
    scm.delete_local_user(user_id)
    return f"[green]✓[/green] Local user [bold]{name}[/bold] deleted from folder {ctx.folder}."


def _set_authentication_profile(ctx: ExecutionContext, args: dict) -> Any:
    """Create a minimal authentication profile.

    Usage:
      set authentication-profile <name> type <ldap|radius|saml|kerberos|local-db>
        [description <text>]

    Examples:
      set authentication-profile Corp-LDAP    type ldap    description "Corporate LDAP"
      set authentication-profile Corp-Radius  type radius
    """
    scm = require_scm(ctx)
    pos = args.get("_positional", [])
    name = pos[0] if pos else (args.get("name") or "")
    pos_lower = [p.lower() for p in pos]
    auth_type = ""
    if "type" in pos_lower:
        t_idx = pos_lower.index("type")
        auth_type = pos[t_idx + 1].lower() if t_idx + 1 < len(pos) else ""
    if not name or not auth_type:
        raise ValueError(
            "Usage: set authentication-profile <name> type <ldap|radius|saml|kerberos|local-db>"
        )
    valid_types = {"ldap", "radius", "saml", "kerberos", "local-db"}
    if auth_type not in valid_types:
        raise ValueError(
            f"Unknown auth type: {auth_type!r}\n"
            f"  Valid types: {', '.join(sorted(valid_types))}"
        )
    payload: dict = {"name": name, "folder": ctx.folder, "method": {auth_type: {}}}
    if args.get("description"):
        payload["description"] = args["description"]

    result = scm.create_authentication_profile(payload)
    return (
        f"[green]✓[/green] Authentication profile [bold]{name}[/bold] (type: {auth_type}) created\n"
        f"  folder: {ctx.folder}  id: {(result or {}).get('id', '?')}\n"
        "  [dim]Use the SCM UI or direct API to configure advanced settings.[/dim]"
    )


def _delete_authentication_profile(ctx: ExecutionContext, args: dict) -> Any:
    """Delete an authentication profile.  Usage: delete authentication-profile <name>"""
    scm = require_scm(ctx)
    name = (args.get("name") or "").strip()
    if not name:
        raise ValueError("Usage: delete authentication-profile <name>")
    items = scm.get_authentication_profiles(folder=ctx.folder)
    prof_id = scm.find_id_by_name(items, name)
    if not prof_id:
        raise ValueError(
            f"Authentication profile '{name}' not found in folder '{ctx.folder}'.  "
            "Run [bold]show authentication-profile[/bold] to see available profiles."
        )
    scm.delete_authentication_profile(prof_id)
    return f"[green]✓[/green] Authentication profile [bold]{name}[/bold] deleted from folder {ctx.folder}."


# ---------------------------------------------------------------------------
# Command table — merged into COMMANDS by registry.py
# ---------------------------------------------------------------------------

COMMANDS: dict[str, CommandDef] = {
    "show authentication-profile": CommandDef(
        description="Show authentication profiles in the active folder",
        category="identity",
        scope="folder",
        api_handler=show_handler("get_authentication_profiles"),
        ssh_command="show authentication-profile",
        render="list",
        feature_flag="authentication",
    ),
    "show authentication-rules": CommandDef(
        description="Show authentication rules in the active folder",
        category="identity",
        scope="folder",
        api_handler=show_handler("get_authentication_rules"),
        ssh_command="show authentication-rule",
        render="list",
        feature_flag="authentication",
    ),
    "show certificate-profile": CommandDef(
        description="Show certificate profiles in the active folder",
        category="identity",
        scope="folder",
        api_handler=show_handler("get_certificate_profiles"),
        ssh_command="show certificate-profile",
        render="list",
        feature_flag="certificates",
    ),
    "show tls-service-profile": CommandDef(
        description="Show TLS service profiles in the active folder",
        category="identity",
        scope="folder",
        api_handler=show_handler("get_tls_service_profiles"),
        ssh_command="show tls-service-profile",
        render="list",
        feature_flag="certificates",
    ),
    "show radius-server": CommandDef(
        description="Show RADIUS server profiles in the active folder",
        category="identity",
        scope="folder",
        api_handler=show_handler("get_radius_server_profiles"),
        ssh_command="show radius-server",
        render="list",
        feature_flag="authentication",
    ),
    "show mfa-server": CommandDef(
        description="Show MFA server profiles in the active folder",
        category="identity",
        scope="folder",
        api_handler=show_handler("get_mfa_servers"),
        ssh_command=None,
        render="list",
        feature_flag="authentication",
    ),
    "show local-user": CommandDef(
        description="Show local users in the active folder",
        category="identity",
        scope="folder",
        api_handler=show_handler("get_local_users"),
        ssh_command="show local-user",
        render="list",
        feature_flag="local_users",
    ),
    "show local-user-group": CommandDef(
        description="Show local user groups in the active folder",
        category="identity",
        scope="folder",
        api_handler=show_handler("get_local_user_groups"),
        ssh_command="show local-user-group",
        render="list",
        feature_flag="local_users",
    ),
    "show user ip-user-mapping": CommandDef(
        description="Show live user-to-IP mapping from device — use --remote",
        category="identity",
        scope="device",
        api_handler=_show_user_ip_mapping,
        ssh_command="show user ip-user-mapping all",
        render="raw",
        feature_flag="local_users",
    ),
    "set local-user": CommandDef(
        description="Create a local user — set local-user <name> password <pw>",
        category="identity",
        scope="folder",
        api_handler=_set_local_user,
        ssh_command=None,
        render="raw",
        feature_flag="local_users",
        usage="set local-user <name> password <password>  [email <addr>]  [description <text>]",
    ),
    "delete local-user": CommandDef(
        description="Delete a local user — delete local-user <name>",
        category="identity",
        scope="folder",
        api_handler=_delete_local_user,
        ssh_command=None,
        render="raw",
        feature_flag="local_users",
        usage="delete local-user <name>",
    ),
    "set authentication-profile": CommandDef(
        description="Create an authentication profile — set authentication-profile <name> type <type>",
        category="identity",
        scope="folder",
        api_handler=_set_authentication_profile,
        ssh_command=None,
        render="raw",
        feature_flag="authentication",
        usage="set authentication-profile <name> type <ldap|radius|saml|kerberos|local-db>",
    ),
    "delete authentication-profile": CommandDef(
        description="Delete an authentication profile — delete authentication-profile <name>",
        category="identity",
        scope="folder",
        api_handler=_delete_authentication_profile,
        ssh_command=None,
        render="raw",
        feature_flag="authentication",
        usage="delete authentication-profile <name>",
    ),
}

