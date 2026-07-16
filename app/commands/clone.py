"""Clone command — duplicate a named config object under a new name.

``clone <resource> <source> <new-name>`` reads an existing object (address,
service, group, tag, EDL, …) from the active container (folder or snippet),
strips its server-managed fields, renames it, and creates the copy in the same
container.  The create is STAGED like any other write — ``commit`` applies it.

Generic by design: the core object types are cloned via their SCMClient
create methods; every other resource that exposes a ``show``/``set`` pair with
a collection endpoint is cloned via the generated resource catalog.
"""
from __future__ import annotations

from typing import Any

from app.commands.base import CommandDef, ExecutionContext, require_scm
from app.commands.resource_catalog import CATALOG

# resource token -> (list client method, create client method).  These are the
# common day-to-day clone targets with hand-written CRUD in objects.py.
_CORE: dict[str, tuple[str, str]] = {
    "address": ("get_addresses", "create_address"),
    "address-group": ("get_address_groups", "create_address_group"),
    "service": ("get_services", "create_service"),
    "service-group": ("get_service_groups", "create_service_group"),
    "tag": ("get_tags", "create_tag"),
    "external-dynamic-list": ("get_external_dynamic_lists", "create_external_dynamic_list"),
}

# Server-managed / read-only fields that must never be carried into a create.
_STRIP_FIELDS = {"id", "uuid", "@name", "folder", "snippet", "device",
                 "created", "modified", "loc", "_active_folder"}

# Catalog entries keyed by command name for the generic fallback path.
_CATALOG_BY_CMD = {e["command"]: e for e in CATALOG}


def _clean(obj: dict) -> dict:
    """Return a create-ready copy of *obj*: drop server/container fields."""
    return {
        k: v for k, v in obj.items()
        if k not in _STRIP_FIELDS and not str(k).startswith("@")
    }


def _split_args(args: dict) -> tuple[str, str, str]:
    """Parse ``<resource...> <source> <new-name>`` from positional args."""
    pos = list(args.get("_positional") or [])
    if len(pos) < 3:
        raise ValueError(
            "Usage: clone <resource> <source-name> <new-name>\n"
            "  e.g.  clone address web-1 web-2\n"
            "        clone service http-alt http-alt-copy\n"
            "        clone address-group dmz-hosts dmz-hosts-v2\n"
            f"  Cloneable object types: {', '.join(sorted(_CORE))}"
        )
    resource = " ".join(pos[:-2]).strip().lower()
    source, new_name = pos[-2], pos[-1]
    return resource, source, new_name


def _read_source(ctx: ExecutionContext, resource: str, source: str) -> dict:
    """Fetch the full source object dict from the active container.

    Uses the registry's ``show <resource>`` handler so every read benefits from
    the same container scoping (folder / snippet) as normal ``show`` commands.
    """
    from app.commands.registry import COMMANDS  # late import avoids a cycle

    show_key = f"show {resource}"
    show_def = COMMANDS.get(show_key)
    if show_def is None or show_def.api_handler is None:
        raise ValueError(
            f"Don't know how to read '{resource}'. "
            f"Cloneable object types: {', '.join(sorted(_CORE))}."
        )
    items = show_def.api_handler(ctx, {})
    if not isinstance(items, list):
        raise ValueError(f"'{resource}' is not a cloneable list resource.")
    match = next((o for o in items if isinstance(o, dict)
                  and (o.get("name") or "").lower() == source.lower()), None)
    if match is None:
        cparam, cvalue = ctx.container
        raise ValueError(f"No {resource} named '{source}' in {cparam} '{cvalue}'.")
    return match


def _clone_handler(ctx: ExecutionContext, args: dict) -> Any:
    scm = require_scm(ctx)
    resource, source, new_name = _split_args(args)

    src = _read_source(ctx, resource, source)
    payload = _clean(src)
    payload["name"] = new_name
    cparam, cvalue = ctx.container
    payload[cparam] = cvalue

    if source.lower() == new_name.lower():
        raise ValueError("New name must differ from the source name.")

    # Core object types: use the dedicated create method (POST is captured by
    # the staging recorder just like any other set command).
    if resource in _CORE:
        _, create_method = _CORE[resource]
        getattr(scm, create_method)(payload)
    else:
        # Generic fallback: POST the cleaned payload to the resource's
        # collection endpoint from the generated catalog.
        entry = _CATALOG_BY_CMD.get(f"set {resource}")
        if entry is None or entry.get("method") != "POST" or entry.get("path_params"):
            raise ValueError(
                f"Cloning '{resource}' is not supported. "
                f"Cloneable object types: {', '.join(sorted(_CORE))}."
            )
        params = {cparam: cvalue} if "folder" in (entry.get("query_params") or []) else {}
        scm.request_api(entry["base_url"], "POST", entry["path"],
                        params=params, json=payload)

    return (
        f"[green]✓[/green] Cloned {resource} [bold]{source}[/bold] → "
        f"[bold]{new_name}[/bold]  [dim]({cparam}: {cvalue})[/dim]"
    )


COMMANDS: dict[str, CommandDef] = {
    "clone": CommandDef(
        description="Clone a named object under a new name (address, service, group, tag, EDL, …)",
        category="objects",
        scope="folder",
        api_handler=_clone_handler,
        render="raw",
        feature_flag="clone_object",
        usage="clone <resource> <source-name> <new-name>",
    ),
}
