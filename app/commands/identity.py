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

from app.commands.base import CommandDef, ExecutionContext, require_scm, require_device


# ---------------------------------------------------------------------------
# Handlers — SCM config (folder-scoped)
# ---------------------------------------------------------------------------

def _show_authentication_profiles(ctx: ExecutionContext, args: dict) -> Any:
    """List authentication profiles in the active SCM folder.

    pan.dev: GET /config/identity/v1/authentication-profiles?folder=<folder>
    """
    scm = require_scm(ctx)
    return scm.get_authentication_profiles(folder=ctx.folder)


def _show_authentication_rules(ctx: ExecutionContext, args: dict) -> Any:
    """List authentication rules in the active SCM folder.

    pan.dev: GET /config/identity/v1/authentication-rules?folder=<folder>
    """
    scm = require_scm(ctx)
    return scm.get_authentication_rules(folder=ctx.folder)


def _show_certificate_profiles(ctx: ExecutionContext, args: dict) -> Any:
    """List certificate profiles in the active SCM folder.

    pan.dev: GET /config/identity/v1/certificate-profiles?folder=<folder>
    """
    scm = require_scm(ctx)
    return scm.get_certificate_profiles(folder=ctx.folder)


def _show_tls_service_profiles(ctx: ExecutionContext, args: dict) -> Any:
    """List TLS service profiles in the active SCM folder.

    pan.dev: GET /config/identity/v1/tls-service-profiles?folder=<folder>
    """
    scm = require_scm(ctx)
    return scm.get_tls_service_profiles(folder=ctx.folder)


def _show_radius_server_profiles(ctx: ExecutionContext, args: dict) -> Any:
    """List RADIUS server profiles in the active SCM folder.

    pan.dev: GET /config/identity/v1/radius-server-profiles?folder=<folder>
    """
    scm = require_scm(ctx)
    return scm.get_radius_server_profiles(folder=ctx.folder)


def _show_mfa_servers(ctx: ExecutionContext, args: dict) -> Any:
    """List MFA server profiles in the active SCM folder.

    pan.dev: GET /config/identity/v1/mfa-servers?folder=<folder>
    """
    scm = require_scm(ctx)
    return scm.get_mfa_servers(folder=ctx.folder)


def _show_local_users(ctx: ExecutionContext, args: dict) -> Any:
    """List local users in the active SCM folder.

    pan.dev: GET /config/identity/v1/local-users?folder=<folder>
    """
    scm = require_scm(ctx)
    return scm.get_local_users(folder=ctx.folder)


def _show_local_user_groups(ctx: ExecutionContext, args: dict) -> Any:
    """List local user groups in the active SCM folder.

    pan.dev: GET /config/identity/v1/local-user-groups?folder=<folder>
    """
    scm = require_scm(ctx)
    return scm.get_local_user_groups(folder=ctx.folder)


# ---------------------------------------------------------------------------
# Handler — live device only (SSH / --remote)
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
        api_handler=_show_authentication_profiles,
        ssh_command="show authentication-profile",
        render="list",
        feature_flag="authentication",
    ),
    "show authentication-rules": CommandDef(
        description="Show authentication rules in the active folder",
        category="identity",
        scope="folder",
        api_handler=_show_authentication_rules,
        ssh_command="show authentication-rule",
        render="list",
        feature_flag="authentication",
    ),
    "show certificate-profile": CommandDef(
        description="Show certificate profiles in the active folder",
        category="identity",
        scope="folder",
        api_handler=_show_certificate_profiles,
        ssh_command="show certificate-profile",
        render="list",
        feature_flag="certificates",
    ),
    "show tls-service-profile": CommandDef(
        description="Show TLS service profiles in the active folder",
        category="identity",
        scope="folder",
        api_handler=_show_tls_service_profiles,
        ssh_command="show tls-service-profile",
        render="list",
        feature_flag="certificates",
    ),
    "show radius-server": CommandDef(
        description="Show RADIUS server profiles in the active folder",
        category="identity",
        scope="folder",
        api_handler=_show_radius_server_profiles,
        ssh_command="show radius-server",
        render="list",
        feature_flag="authentication",
    ),
    "show mfa-server": CommandDef(
        description="Show MFA server profiles in the active folder",
        category="identity",
        scope="folder",
        api_handler=_show_mfa_servers,
        ssh_command=None,
        render="list",
        feature_flag="authentication",
    ),
    "show local-user": CommandDef(
        description="Show local users in the active folder",
        category="identity",
        scope="folder",
        api_handler=_show_local_users,
        ssh_command="show local-user",
        render="list",
        feature_flag="local_users",
    ),
    "show local-user-group": CommandDef(
        description="Show local user groups in the active folder",
        category="identity",
        scope="folder",
        api_handler=_show_local_user_groups,
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

