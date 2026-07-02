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

from app.commands.base import CommandDef, ExecutionContext, require_device, show_handler


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
}

