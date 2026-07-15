"""Shared types and helpers for ARC command modules.

Every command module imports from here — this is the only place
CommandDef, ExecutionContext, and the shared utility functions live.
No handler logic goes here; only definitions shared across modules.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Callable, Literal, Optional

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


# Command scope — controls what context is required AND the execution plane.
#
#   "folder"  — scoped to the active SCM folder (ctx.folder).  These are
#               config/policy commands; the active folder is always passed
#               as the ?folder= query parameter.  Default for most commands.
#               Runs via the SCM API (bearer token, no device auth).
#
#   "device"  — requires an active device context (cd <device>).  Operational
#               commands that TARGET a device but run via the SCM ops-job proxy
#               (over the device's management tunnel — no SSH, no 2FA).
#
#   "remote"  — requires an active device context AND can only run by SSHing to
#               the device (no SCM path).  Expect the device's auth (TACACS+/2FA).
#               This is the explicit 2FA surface; expanding the SCM proxy moves
#               commands from "remote" to "device".
#
#   "global"  — no context filtering.  The command always sees everything
#               regardless of active folder or device (e.g. show snippets global,
#               show devices).  Runs via the SCM API.
#
# Both "device" and "remote" require `cd <device>`; they differ only in the
# execution plane (SCM ops-job proxy vs SSH).  The generators derive scope
# automatically (see app/commands/generated.py + panos_generated.py).
CommandScope = Literal["folder", "device", "remote", "global"]


@dataclass
class CommandDef:
    """Descriptor for a single ARC command entry.

    Fields:
        description:  One-line description shown in help output.
        usage:        Optional syntax line shown by ``<command> ?`` — how to
                      invoke the command, including its arguments/options.
                      Empty (default) → ``?`` falls back to the command name.
                      Overridable per command in docs/commands/<slug>.md front-matter.
        category:     Grouping key used in help (e.g. 'setup', 'objects', 'security').
        scope:        Context requirement — 'folder' (default), 'device', or 'global'.
                      See CommandScope above.
        api_handler:  Called when the command runs in API (SCM) mode.
                      Signature: (ctx: ExecutionContext, args: dict) -> Any
        ssh_command:  Static string or callable that returns the PAN-OS SSH command.
                      Callable signature: (args: dict) -> str
                      None means API-only (config / SCM object commands).
        render:       Key into ArcShell._render() dispatch table.
        feature_flag: Name of a flag in the settings/features/ glossary that gates this command.
                      Empty string (default) means always enabled.
                      When the flag is false (or absent) the command is hidden from
                      ? help and blocked at runtime.  Example: feature_flag='nat_rules'
    """

    description: str
    category: str
    scope: CommandScope = "folder"
    api_handler: Optional[Callable] = None
    ssh_command: str | Callable[[dict], str] | None = None
    render: str = ""
    feature_flag: str = ""   # key in the settings/features/ glossary that gates this command
    usage: str = ""          # syntax line shown by `<command> ?` (see docs/commands front-matter)


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


# ---------------------------------------------------------------------------
# Handler factories — build the common read/delete handlers declaratively.
#
# Most 'show <resource>' handlers are a single SCM list call, and most
# 'delete <resource>' handlers are the same find-by-name-then-DELETE
# sequence.  These factories replace that copy-paste boilerplate; handlers
# with any extra logic (client-side filtering, payload building, multiple
# calls) stay hand-written in their command module.
# ---------------------------------------------------------------------------

def show_handler(scm_method: str, *, folder_scoped: bool = True) -> Callable:
    """Return a read handler that calls a single SCMClient list method.

    Accepts an optional ``args["name"]`` to filter the list to a single object
    by name — so ``show address web-server`` shows just that address.
    Tab completion offers live names from the API.

    **Folder inheritance**: SCM returns objects from the active folder AND
    inherited from parent folders. Each object carries a ``folder`` field
    showing where it is defined. The active folder is injected into the result
    as ``_active_folder`` so formatters can annotate inherited objects.

    e.g.  api_handler=show_handler("get_addresses")
          api_handler=show_handler("get_regions", folder_scoped=False)
    """
    def handler(ctx: ExecutionContext, args: dict):
        scm = require_scm(ctx)
        method = getattr(scm, scm_method)
        if folder_scoped:
            results = method(folder=ctx.folder)
        else:
            results = method()
        # Inject active folder so formatters can mark inherited objects
        active_folder = ctx.folder if folder_scoped else None
        if isinstance(results, list) and active_folder:
            for obj in results:
                if isinstance(obj, dict):
                    obj["_active_folder"] = active_folder
        # Optional name filter: `show address web-server` → show just that one
        name_filter = (args.get("name") or (args.get("_positional") or [None])[0] if args else None)
        if name_filter and isinstance(results, list):
            matched = [r for r in results if isinstance(r, dict)
                       and r.get("name", "").lower() == name_filter.lower()]
            if matched:
                return matched
            # Partial match fallback
            partial = [r for r in results if isinstance(r, dict)
                       and r.get("name", "").lower().startswith(name_filter.lower())]
            if partial:
                return partial
            raise ValueError(f"No object named '{name_filter}' in folder '{ctx.folder}'.")
        return results
    return handler


def delete_handler(resource_label: str, get_method: str, delete_method: str, *, usage: str) -> Callable:
    """Return a delete-by-name handler (list → resolve id → DELETE).

    The handler reads ``args["name"]`` (raising ValueError with *usage* when
    missing), lists the resource via *get_method* in the active folder,
    resolves the object id with ``SCMClient._find_id_by_name``, raises
    ValueError when no object matches, then calls *delete_method* with the id.

    e.g.  api_handler=delete_handler(
              "Tag", "get_tags", "delete_tag",
              usage="Usage: delete tag <name>",
          )
    """
    def handler(ctx: ExecutionContext, args: dict):
        scm = require_scm(ctx)
        name = (args.get("name") or "").strip()
        if not name:
            raise ValueError(usage)
        items  = getattr(scm, get_method)(folder=ctx.folder)
        obj_id = scm._find_id_by_name(items, name)
        if not obj_id:
            raise ValueError(f"{resource_label} '{name}' not found in folder '{ctx.folder}'")
        getattr(scm, delete_method)(obj_id)
        return f"[green]✓[/green] {resource_label} [bold]{name}[/bold] deleted."
    return handler


# ---------------------------------------------------------------------------
# Write-command helpers — used by objects.py, security.py, network.py etc.
# ---------------------------------------------------------------------------

def parse_kv_tail(pos: list[str], start: int) -> dict[str, str]:
    """Parse positional[start:] as alternating key/value pairs.

    e.g. ["description", "My object", "tag", "Production"]
    → {"description": "My object", "tag": "Production"}

    Used by all 'set'/'update' command handlers to extract optional trailing
    keyword-value pairs after the primary type/value arguments.
    """
    result: dict[str, str] = {}
    i = start
    while i + 1 < len(pos):
        result[pos[i].lower().replace("-", "_")] = pos[i + 1]
        i += 2
    return result


def merge_common_fields(obj: dict, args: dict, pos: list[str], pos_start: int) -> None:
    """Apply description and tag changes from parsed args onto an existing object dict.

    Used by update handlers (GET→merge→PUT pattern) to selectively overwrite
    only the fields the user specified.
    """
    kv = parse_kv_tail(pos, pos_start)
    if args.get("description") or kv.get("description"):
        obj["description"] = args.get("description") or kv["description"]
    new_tags = [t for t in [args.get("tag"), kv.get("tag")] if t]
    if new_tags:
        obj["tag"] = new_tags


