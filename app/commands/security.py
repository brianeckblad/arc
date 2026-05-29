"""Security commands — SCM /config/security/v1 endpoint group.

Covers: security-rules, URL categories, decryption profiles, DNS security profiles.
pan.dev spec: openapi-specs/scm/config/ngfw/security/security-services-R2-2026.yaml
Base URL:     https://api.strata.paloaltonetworks.com/config/security/v1

Commands in this module:
  show security policy              — list security rules (pre-rules) in active folder
  show url-categories               — list custom URL categories
  test security-policy-match        — test whether traffic matches a rule (SSH only)
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
    ),
    "show url-categories": CommandDef(
        description="Show custom URL categories in the active folder",
        category="security",
        scope="folder",
        api_handler=_show_url_categories,
        ssh_command=None,
        render="url_categories",
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
    ),
}

