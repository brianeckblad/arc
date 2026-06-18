"""Shared types and helpers for ARC command modules.

Every command module imports from here — this is the only place
CommandDef, ExecutionContext, and the shared utility functions live.
No handler logic goes here; only definitions shared across modules.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Callable, Literal, Optional

if TYPE_CHECKING:
    from app.api.client import SCMClient
    from app.config import ArcConfig
    from app.ssh.manager import SSHManager


@dataclass
class ExecutionContext:
    """Passed to every api_handler so it can access state and clients."""

    scm: Optional["SCMClient"] = None
    ssh: Optional["SSHManager"] = None
    config: Optional["ArcConfig"] = None
    device: Optional[dict] = None
    folder: str = "Shared"
    tsg_id: str = ""

    @property
    def target(self) -> Optional[str]:
        """Selected device serial, when known."""
        return self.device.get("serial") if self.device else None

    @property
    def device_host(self) -> Optional[str]:
        """IP / hostname of the selected device for SSH."""
        if not self.device:
            return None
        return self.device.get("ip_address") or self.device.get("hostname") or None


# Command scope — controls what context is required and what gets injected.
#
#   "folder"  — scoped to the active SCM folder (ctx.folder).  These are
#               config/policy commands; the active folder is always passed
#               as the ?folder= query parameter.  Default for most commands.
#
#   "device"  — requires an active device context (cd <device>).  These are
#               operational commands that must run on a specific device.
#               ARC enforces the requirement before calling the handler.
#
#   "global"  — no context filtering.  The command always sees everything
#               regardless of active folder or device (e.g. show snippets global,
#               show devices).
CommandScope = Literal["folder", "device", "global"]


@dataclass
class CommandDef:
    """Descriptor for a single ARC command entry.

    Fields:
        description:  One-line description shown in help output.
        category:     Grouping key used in help (e.g. 'setup', 'objects', 'security').
        scope:        Context requirement — 'folder' (default), 'device', or 'global'.
                      See CommandScope above.
        api_handler:  Called when the command runs in API (SCM) mode.
                      Signature: (ctx: ExecutionContext, args: dict) -> Any
        ssh_command:  Static string or callable that returns the PAN-OS SSH command.
                      Callable signature: (args: dict) -> str
                      None means API-only (config / SCM object commands).
        render:       Key into ArcShell._render() dispatch table.
        feature_flag: Name of a FeatureFlags field that gates this command.
                      Empty string (default) means always enabled.
                      When the flag is False the command is hidden from ? and blocked.
                      Example: feature_flag='nat_rules'
    """

    description: str
    category: str
    scope: CommandScope = "folder"
    api_handler: Optional[Callable] = None
    ssh_command: str | Callable[[dict], str] | None = None
    render: str = ""
    feature_flag: str = ""   # gate behind app/features.py FeatureFlags field


# ---------------------------------------------------------------------------
# Shared guard helpers — imported by every command module
# ---------------------------------------------------------------------------

def require_scm(ctx: ExecutionContext) -> "SCMClient":
    """Return the SCM client or raise a clear RuntimeError if it is not configured."""
    if not ctx.scm:
        raise RuntimeError(
            "SCM is not configured. Set SCM_BEARER_TOKEN, or set "
            "SCM_CLIENT_ID / SCM_CLIENT_SECRET / SCM_TSG_ID and restart."
        )
    return ctx.scm


def require_device(ctx: ExecutionContext) -> dict:
    """Return the active device or raise a clear RuntimeError.

    Used by device-scoped command handlers that need ctx.device to be set.
    """
    if not ctx.device:
        raise RuntimeError(
            "This command requires a device context. "
            "Use [bold]cd <device>[/bold] first, or run with [bold]--remote <device>[/bold]."
        )
    return ctx.device


def translation_pending(command: str) -> str:
    """Return a standard 'not yet implemented' message for SSH-only commands."""
    return (
        f"SCM API translation for '{command}' is not implemented yet. "
        f"Use '{command} --remote' for a one-time SSH run, or use "
        "'remote <device>' / 'connect' for SSH passthrough mode."
    )

