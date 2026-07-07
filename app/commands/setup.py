"""Setup commands (devices, snippets, folders). See docs/commands/ and docs/scm-api/specs/setup.md for details."""

from __future__ import annotations

from typing import Any

from rich.console import Console as _console_cls

from app.commands.base import CommandDef, ExecutionContext, require_scm, show_handler

_setup_console = _console_cls()


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _snippet_names_for_folder(scm, folder_name: str) -> set[str]:
    """Return the set of snippet names attached to *folder_name*.

    The authoritative source is the folder record's 'snippets' field
    (a list of snippet name strings), NOT a 'folders' field on the
    snippet object — that field is absent on list responses.

    Falls back to an empty set on any API error so callers degrade gracefully.
    """
    try:
        folders = scm.get_folders_full()
        for folder in folders:
            if folder.get("name", "").lower() == folder_name.lower():
                raw = folder.get("snippets") or []
                # The field may be a list of strings or a list of {name:} dicts
                names: set[str] = set()
                for item in raw:
                    if isinstance(item, str):
                        names.add(item)
                    elif isinstance(item, dict):
                        n = item.get("name") or item.get("id") or ""
                        if n:
                            names.add(n)
                return names
    except Exception:
        pass
    return set()


# ---------------------------------------------------------------------------
# Handlers
# ---------------------------------------------------------------------------

def _show_device_detail(ctx: ExecutionContext, args: dict) -> Any:
    """Show detail for a named device — show device <hostname|serial>.

    Falls back to the current cd context when no name is given.
    pan.dev: GET /config/setup/v1/devices  (filtered client-side by name/serial)
    """
    scm = require_scm(ctx)
    target = args.get("name") or args.get("_positional", [None])[0] or ""

    if not target:
        # No name given — use device context set by `cd`
        if ctx.device:
            devices = scm.get_devices()
            serial   = ctx.device.get("serial_number") or ctx.device.get("name") or ""
            hostname = ctx.device.get("hostname") or ""
            match = next(
                (d for d in devices
                 if d.get("hostname", "").lower() == hostname.lower()
                 or d.get("serial_number") == serial
                 or d.get("name") == serial),
                None,
            )
            return {"_render": "device_detail", "device": match or ctx.device}
        raise RuntimeError(
            "Usage: show device <hostname>  — or use 'cd <device>' first"
        )

    devices = scm.get_devices()
    match = next(
        (d for d in devices
         if d.get("hostname", "").lower() == target.lower()
         or d.get("serial_number", "").lower() == target.lower()
         or d.get("name", "").lower() == target.lower()),
        None,
    )
    if not match:
        raise RuntimeError(
            f"Device {target!r} not found in SCM.\n"
            "  Run [bold]show devices[/bold] to see all managed devices, "
            "or [bold]tsg <id>[/bold] to check a different tenant."
        )
    return {"_render": "device_detail", "device": match}


def _show_device_snippets(ctx: ExecutionContext, args: dict) -> Any:
    """Show snippets attached to a named device — show device <name> snippets.

    pan.dev: GET /config/setup/v1/devices  +  GET /config/setup/v1/snippets/{id}
    """
    scm = require_scm(ctx)
    target = args.get("name") or args.get("_positional", [None])[0] or ""

    if not target:
        if ctx.device:
            target = ctx.device.get("hostname") or ctx.device.get("name") or ""
        else:
            raise RuntimeError(
                "Usage: show device <hostname> snippets  — or use 'cd <device>' first"
            )

    devices = scm.get_devices()
    device = next(
        (d for d in devices
         if d.get("hostname", "").lower() == target.lower()
         or d.get("serial_number", "").lower() == target.lower()
         or d.get("name", "").lower() == target.lower()),
        None,
    )
    if not device:
        raise RuntimeError(
            f"Device {target!r} not found in SCM.\n"
            "  Run [bold]show devices[/bold] to see all managed devices."
        )

    snippet_names: list[str] = device.get("snippets") or []
    if not snippet_names:
        return {"_render": "device_snippets", "device_name": target, "snippets": []}

    all_snippets = scm.get_snippets()
    by_name = {s.get("name"): s for s in all_snippets}
    matched: list[dict] = []
    for name in snippet_names:
        s = by_name.get(name)
        if s and s.get("id"):
            try:
                detail = scm.get_snippet_detail(s["id"])
                matched.append(detail)
            except Exception:
                matched.append(s)
        elif s:
            matched.append(s)
        else:
            matched.append({"name": name})

    return {
        "_render": "device_snippets",
        "device_name": device.get("hostname") or target,
        "snippets": matched,
    }


def _show_snippets(ctx: ExecutionContext, args: dict) -> Any:
    """List snippets scoped to the current context.

    If a positional arg is given (e.g. ``show snippets my-snippet``),
    redirect to detail — same result as ``show snippet my-snippet``.

    Scope when no name given:
      1. Device context  → device.snippets[] merged with active folder snippets
      2. Non-Shared folder → folder record's snippets[] list
      3. Shared root → all snippets

    Use 'show snippets global' to always bypass filtering.
    """
    # "show snippets <name>" → treat as "show snippet <name>"
    if args.get("_positional"):
        return _show_snippet_detail(ctx, args)

    scm = require_scm(ctx)
    all_snippets = scm.get_snippets()
    by_name = {s.get("name"): s for s in all_snippets}

    # 1. Device context — merge device-level + folder-level snippet names.
    if ctx.device:
        device_name = ctx.device.get("hostname") or ctx.device.get("name", "")
        device_names: set[str] = set(ctx.device.get("snippets") or [])

        folder_names: set[str] = set()
        if ctx.folder and ctx.folder.lower() != "shared":
            folder_names = _snippet_names_for_folder(scm, ctx.folder)

        merged = device_names | folder_names
        matched = [by_name[n] for n in merged if n in by_name]
        missing = [{"name": n} for n in merged if n not in by_name]

        scope = f"device: {device_name}"
        if folder_names:
            scope += f"  +  folder: {ctx.folder}"
        elif ctx.folder and ctx.folder.lower() != "shared":
            # Folder had no snippets; still mention it for clarity
            scope += f"  (folder: {ctx.folder} — no snippets attached)"

        return {
            "_render": "snippets_scoped",
            "snippets": matched + missing,
            "scope": scope,
            "hint": (
                "show snippets global → all snippets  |  "
                "show device snippets → device-only with full detail"
            ),
        }

    # 2. Folder context other than Shared.
    if ctx.folder and ctx.folder.lower() != "shared":
        folder_snippet_names = _snippet_names_for_folder(scm, ctx.folder)
        matched = [by_name[n] for n in folder_snippet_names if n in by_name]
        missing = [{"name": n} for n in folder_snippet_names if n not in by_name]
        return {
            "_render": "snippets_scoped",
            "snippets": matched + missing,
            "scope": f"folder: {ctx.folder}",
            "hint": "show snippets global → all snippets  |  folder .. → back to Shared",
        }

    # 3. Shared root — return all snippets.
    return {
        "_render": "snippets_scoped",
        "snippets": all_snippets,
        "scope": "Shared (all snippets)",
        "hint": "folder <name> → switch to a folder to see folder-scoped snippets",
    }


def _show_snippets_global(ctx: ExecutionContext, args: dict) -> Any:
    """List ALL snippets regardless of device or folder context.

    pan.dev: GET /config/setup/v1/snippets
    """
    scm = require_scm(ctx)
    all_snippets = scm.get_snippets()
    return {
        "_render": "snippets_scoped",
        "snippets": all_snippets,
        "scope": "global (all snippets)",
        "hint": "show snippets → context-scoped list",
    }


def _show_snippet_detail(ctx: ExecutionContext, args: dict) -> Any:
    """Show detail for a named snippet.

    ``show snippet <name>``         — metadata + variables (fast)
    ``show snippet <name> details`` — metadata + variables + all configured
                                      objects/rules inside the snippet

    pan.dev:
      GET /config/setup/v1/snippets/{id}
      GET /config/objects/v1/addresses?snippet=<name>  (and others, for details)
    """
    scm = require_scm(ctx)
    positional = args.get("_positional", [])
    target = positional[0] if positional else ""
    want_details = len(positional) > 1 and positional[1].lower() == "details"

    if not target:
        raise RuntimeError("Usage: show snippet <name>  |  show snippet <name> details")

    all_snippets = scm.get_snippets()
    match = next(
        (s for s in all_snippets if s.get("name", "").lower() == target.lower()), None
    )
    if not match:
        raise RuntimeError(f"Snippet not found: {target!r}")

    # Fetch the metadata/variables detail record.
    snippet = scm.get_snippet_detail(match["id"]) if match.get("id") else match

    if not want_details:
        return snippet

    # Full detail: fetch all configured objects scoped to this snippet.
    snippet_name = snippet.get("name") or target
    objects = scm.get_snippet_objects(snippet_name)
    return {
        "_render": "snippet_detail_full",
        "snippet": snippet,
        "objects": objects,
    }


# ---------------------------------------------------------------------------
# Snippet write handlers
# ---------------------------------------------------------------------------

def _set_snippet(ctx: ExecutionContext, args: dict) -> Any:
    """Create a new SCM snippet (named configuration container).

    Snippets are reusable configuration packages that can be attached to
    folders or devices to apply a standard config baseline.

    Usage:
      set snippet <name>                          Create an empty snippet
      set snippet <name> description <text>       Create with description
      set snippet <name> type predefined|custom   Set snippet type

    Examples:
      set snippet BaselineConfig description "Standard NGFW baseline"
      set snippet VPN-Template type custom

    pan.dev: POST /config/setup/v1/snippets
    """
    scm = require_scm(ctx)
    pos = args.get("_positional", [])
    name = pos[0] if pos else (args.get("name") or "")
    if not name:
        raise ValueError(
            "Usage: set snippet <name>  [description <text>]  [type predefined|custom]\n"
            "  e.g. set snippet BaselineConfig description 'Standard NGFW baseline'"
        )
    payload: dict = {"name": name}
    pos_lower = [p.lower() for p in pos]
    if "description" in pos_lower:
        d_idx = pos_lower.index("description")
        payload["description"] = " ".join(pos[d_idx + 1:]) or args.get("description", "")
    elif args.get("description"):
        payload["description"] = args["description"]
    if "type" in pos_lower:
        t_idx = pos_lower.index("type")
        snip_type = pos[t_idx + 1] if t_idx + 1 < len(pos) else ""
        if snip_type.lower() not in ("predefined", "custom"):
            raise ValueError(f"Invalid snippet type: {snip_type!r}  (valid: predefined | custom)")
        payload["type"] = snip_type.lower()

    result = scm.create_snippet(payload)
    return (
        f"[green]✓[/green] Snippet [bold]{name}[/bold] created\n"
        f"  id: {(result or {}).get('id', '?')}\n"
        "  [dim]Use the SCM portal to attach configuration objects to this snippet.[/dim]"
    )


def _delete_snippet(ctx: ExecutionContext, args: dict) -> Any:
    """Delete an SCM snippet.

    Usage: delete snippet <name>

    WARNING: Deleting a snippet removes it from all folders and devices it is
    attached to. Configuration managed by the snippet will be removed from those
    devices on the next commit.
    """
    scm = require_scm(ctx)
    name = (args.get("name") or "").strip()
    if not name:
        raise ValueError(
            "Usage: delete snippet <name>\n"
            "  Run [bold]show snippets global[/bold] to see all snippets."
        )
    snippets = scm.get_snippets()
    snip_id = scm.find_id_by_name(snippets, name)
    if not snip_id:
        raise ValueError(
            f"Snippet '{name}' not found.\n"
            "  Run [bold]show snippets global[/bold] to see all snippets."
        )
    # Confirm — snippet deletion can affect many devices
    _setup_console.print(
        f"[yellow]⚠  Deleting snippet [bold]{name}[/bold] will remove it from all attached\n"
        "   folders and devices. Config managed by this snippet will be withdrawn\n"
        "   on the next commit.[/yellow]"
    )
    scm.delete_snippet(snip_id)
    return f"[green]✓[/green] Snippet [bold]{name}[/bold] deleted."


# ---------------------------------------------------------------------------
# Command table — merged into COMMANDS by registry.py
# ---------------------------------------------------------------------------

COMMANDS: dict[str, CommandDef] = {
    "show devices": CommandDef(
        description="List all SCM-managed devices",
        category="setup",
        scope="global",
        api_handler=show_handler("get_devices", folder_scoped=False),
        ssh_command=None,
        render="devices",
        feature_flag="show_devices",
    ),
    "show device snippets": CommandDef(
        description="Show snippets attached to a device — show device <hostname> snippets",
        category="setup",
        scope="global",
        api_handler=_show_device_snippets,
        ssh_command=None,
        render="device_snippets",
        feature_flag="show_devices",
    ),
    "show device": CommandDef(
        description="Show detail for a device — show device <hostname>  (or 'show device' when cd'd in)",
        category="setup",
        scope="global",
        api_handler=_show_device_detail,
        ssh_command=None,
        render="device_detail",
        feature_flag="show_devices",
    ),
    "show snippets global": CommandDef(
        description="List ALL snippets regardless of device or folder context",
        category="setup",
        scope="global",
        api_handler=_show_snippets_global,
        ssh_command=None,
        render="snippets_scoped",
        feature_flag="show_snippets",
    ),
    "show snippets": CommandDef(
        description=(
            "List snippets for the current context  "
            "[dim](device → device snippets | folder → folder snippets | Shared → all)[/dim]"
        ),
        category="setup",
        scope="folder",
        api_handler=_show_snippets,
        ssh_command=None,
        render="snippets_scoped",
        feature_flag="show_snippets",
    ),
    "show snippet": CommandDef(
        description="Show full detail for a snippet — show snippet <name>",
        category="setup",
        scope="global",
        api_handler=_show_snippet_detail,
        ssh_command=None,
        render="snippet_detail",
        feature_flag="show_snippets",
    ),
    "set snippet": CommandDef(
        description="Create a new SCM snippet — set snippet <name> [description <text>]",
        category="setup",
        scope="global",
        api_handler=_set_snippet,
        ssh_command=None,
        render="raw",
        feature_flag="show_snippets",
        usage="set snippet <name>  [description <text>]  [type predefined|custom]",
    ),
    "delete snippet": CommandDef(
        description="Delete an SCM snippet — delete snippet <name>  (WARNING: removes from all attached devices)",
        category="setup",
        scope="global",
        api_handler=_delete_snippet,
        ssh_command=None,
        render="raw",
        feature_flag="show_snippets",
        usage="delete snippet <name>",
    ),
}
