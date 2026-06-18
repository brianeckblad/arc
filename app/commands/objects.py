"""Objects commands (addresses, services, tags, EDLs). See docs/commands/ and docs/scm-api/specs/objects.md for details."""

from __future__ import annotations

from typing import Any

from app.commands.base import CommandDef, ExecutionContext, require_scm


# ---------------------------------------------------------------------------
# Handlers
# ---------------------------------------------------------------------------

def _show_address(ctx: ExecutionContext, args: dict) -> Any:
    """List address objects in the active SCM folder.

    pan.dev: GET /config/objects/v1/addresses?folder=<folder>
    """
    scm = require_scm(ctx)
    return scm.get_addresses(folder=ctx.folder)


def _show_address_group(ctx: ExecutionContext, args: dict) -> Any:
    """List address groups in the active SCM folder.

    pan.dev: GET /config/objects/v1/address-groups?folder=<folder>
    """
    scm = require_scm(ctx)
    return scm.get_address_groups(folder=ctx.folder)


def _show_service(ctx: ExecutionContext, args: dict) -> Any:
    """List service objects in the active SCM folder.

    pan.dev: GET /config/objects/v1/services?folder=<folder>
    """
    scm = require_scm(ctx)
    return scm.get_services(folder=ctx.folder)


def _show_tag(ctx: ExecutionContext, args: dict) -> Any:
    """List tags in the active SCM folder.

    pan.dev: GET /config/objects/v1/tags?folder=<folder>
    """
    scm = require_scm(ctx)
    return scm.get_tags(folder=ctx.folder)


def _show_external_dynamic_list(ctx: ExecutionContext, args: dict) -> Any:
    """List external dynamic lists (EDLs) in the active SCM folder.

    pan.dev: GET /config/objects/v1/external-dynamic-lists?folder=<folder>
    """
    scm = require_scm(ctx)
    return scm.get_external_dynamic_lists(folder=ctx.folder)


# ---------------------------------------------------------------------------
# Command table — merged into COMMANDS by registry.py
# ---------------------------------------------------------------------------

COMMANDS: dict[str, CommandDef] = {
    "show address": CommandDef(
        description="Show address objects in the active folder",
        category="objects",
        scope="folder",
        api_handler=_show_address,
        ssh_command=None,
        render="address_objects",
        feature_flag="show_address",
    ),
    "show address-group": CommandDef(
        description="Show address groups in the active folder",
        category="objects",
        scope="folder",
        api_handler=_show_address_group,
        ssh_command=None,
        render="address_groups",
        feature_flag="show_address_group",
    ),
    "show service": CommandDef(
        description="Show service objects in the active folder",
        category="objects",
        scope="folder",
        api_handler=_show_service,
        ssh_command=None,
        render="services",
        feature_flag="show_service",
    ),
    "show tag": CommandDef(
        description="Show tags in the active folder",
        category="objects",
        scope="folder",
        api_handler=_show_tag,
        ssh_command=None,
        render="tags",
        feature_flag="show_tag",
    ),
    "show external-dynamic-list": CommandDef(
        description="Show external dynamic lists (EDLs) in the active folder",
        category="objects",
        scope="folder",
        api_handler=_show_external_dynamic_list,
        ssh_command=None,
        render="edl_list",
        feature_flag="show_external_dynamic_list",
    ),
}


# ---------------------------------------------------------------------------
# Additional handlers — unimplemented objects commands
# ---------------------------------------------------------------------------

def _show_service_groups(ctx: ExecutionContext, args: dict) -> Any:
    """pan.dev: GET /config/objects/v1/service-groups?folder=<folder>"""
    scm = require_scm(ctx)
    return scm.get_service_groups(folder=ctx.folder)


def _show_application_groups(ctx: ExecutionContext, args: dict) -> Any:
    """pan.dev: GET /config/objects/v1/application-groups?folder=<folder>"""
    scm = require_scm(ctx)
    return scm.get_application_groups(folder=ctx.folder)


def _show_application_filters(ctx: ExecutionContext, args: dict) -> Any:
    """pan.dev: GET /config/objects/v1/application-filters?folder=<folder>"""
    scm = require_scm(ctx)
    return scm.get_application_filters(folder=ctx.folder)


def _show_schedules(ctx: ExecutionContext, args: dict) -> Any:
    """pan.dev: GET /config/objects/v1/schedules?folder=<folder>"""
    scm = require_scm(ctx)
    return scm.get_schedules(folder=ctx.folder)


def _show_regions(ctx: ExecutionContext, args: dict) -> Any:
    """pan.dev: GET /config/objects/v1/regions  (global — no folder filter)"""
    scm = require_scm(ctx)
    return scm.get_regions()


def _show_hip_objects(ctx: ExecutionContext, args: dict) -> Any:
    """pan.dev: GET /config/objects/v1/hip-objects?folder=<folder>"""
    scm = require_scm(ctx)
    return scm.get_hip_objects(folder=ctx.folder)


def _show_hip_profiles(ctx: ExecutionContext, args: dict) -> Any:
    """pan.dev: GET /config/objects/v1/hip-profiles?folder=<folder>"""
    scm = require_scm(ctx)
    return scm.get_hip_profiles(folder=ctx.folder)


def _show_log_forwarding_profiles(ctx: ExecutionContext, args: dict) -> Any:
    """pan.dev: GET /config/objects/v1/log-forwarding-profiles?folder=<folder>"""
    scm = require_scm(ctx)
    return scm.get_log_forwarding_profiles(folder=ctx.folder)


_EXTRA_COMMANDS: dict[str, CommandDef] = {
    "show service-group": CommandDef(
        description="Show service groups in the active folder",
        category="objects",
        scope="folder",
        api_handler=_show_service_groups,
        ssh_command="show objects service-group",
        render="list",
        feature_flag="service_groups",
    ),
    "show application-group": CommandDef(
        description="Show application groups in the active folder",
        category="objects",
        scope="folder",
        api_handler=_show_application_groups,
        ssh_command="show objects application-group",
        render="list",
        feature_flag="app_groups",
    ),
    "show application-filter": CommandDef(
        description="Show application filters in the active folder",
        category="objects",
        scope="folder",
        api_handler=_show_application_filters,
        ssh_command=None,
        render="list",
        feature_flag="app_groups",
    ),
    "show schedule": CommandDef(
        description="Show schedules in the active folder",
        category="objects",
        scope="folder",
        api_handler=_show_schedules,
        ssh_command=None,
        render="list",
        feature_flag="schedules",
    ),
    "show region": CommandDef(
        description="Show regions (TSG-wide, no folder filter)",
        category="objects",
        scope="global",
        api_handler=_show_regions,
        ssh_command=None,
        render="list",
        feature_flag="regions",
    ),
    "show hip-object": CommandDef(
        description="Show GlobalProtect HIP objects in the active folder",
        category="objects",
        scope="folder",
        api_handler=_show_hip_objects,
        ssh_command=None,
        render="list",
        feature_flag="hip",
    ),
    "show hip-profile": CommandDef(
        description="Show GlobalProtect HIP profiles in the active folder",
        category="objects",
        scope="folder",
        api_handler=_show_hip_profiles,
        ssh_command=None,
        render="list",
        feature_flag="hip",
    ),
    "show log-forwarding-profile": CommandDef(
        description="Show log forwarding profiles in the active folder",
        category="objects",
        scope="folder",
        api_handler=_show_log_forwarding_profiles,
        ssh_command=None,
        render="list",
        feature_flag="log_profiles",
    ),
}

COMMANDS.update(_EXTRA_COMMANDS)


# ---------------------------------------------------------------------------
# Write handlers — configure mode, all POST/DELETE via SCM API
# ---------------------------------------------------------------------------

def _set_address(ctx: ExecutionContext, args: dict) -> Any:
    """Create an address object in the active SCM folder.

    Usage:
      set address <name> ip-netmask <value>   e.g.  10.1.0.0/24
      set address <name> ip-range <value>     e.g.  10.1.0.1-10.1.0.10
      set address <name> fqdn <value>         e.g.  *.example.com
      set address <name> ip-wildcard <value>  e.g.  10.1.0.0/255.0.255.0

    pan.dev: POST /config/objects/v1/addresses
    """
    scm  = require_scm(ctx)
    name = (args.get("name") or "").strip()
    pos  = args.get("_positional", [])

    if not name:
        raise ValueError("Usage: set address <name> ip-netmask|fqdn|ip-range|ip-wildcard <value>")

    # Address type comes from the remaining positional tokens: <type> <value>
    # Handled by the dispatcher: set address myobj ip-netmask 10.0.0.0/8
    # After matching "set address", args["name"] = first positional = name
    # remaining positionals contain [type, value]
    addr_type = pos[1].lower() if len(pos) > 1 else ""
    addr_val  = pos[2] if len(pos) > 2 else ""

    _TYPE_MAP = {
        "ip-netmask": "ip_netmask",
        "ip-range":   "ip_range",
        "fqdn":       "fqdn",
        "ip-wildcard": "ip_wildcard",
    }
    if addr_type not in _TYPE_MAP:
        raise ValueError(
            f"Unknown address type {addr_type!r}.  "
            "Use: ip-netmask | ip-range | fqdn | ip-wildcard"
        )
    if not addr_val:
        raise ValueError(f"Missing value for address type {addr_type}")

    payload = {
        "name":   name,
        "folder": ctx.folder,
        _TYPE_MAP[addr_type]: addr_val,
    }
    result = scm.create_address(payload)
    return f"[green]✓[/green] Address [bold]{name}[/bold] created  (id: {result.get('id', '?')})"


def _delete_address(ctx: ExecutionContext, args: dict) -> Any:
    """Delete an address object by name from the active SCM folder.

    Usage: delete address <name>
    pan.dev: DELETE /config/objects/v1/addresses/{id}
    """
    scm  = require_scm(ctx)
    name = (args.get("name") or "").strip()
    if not name:
        raise ValueError("Usage: delete address <name>")
    items = scm.get_addresses(folder=ctx.folder)
    obj_id = scm._find_id_by_name(items, name)
    if not obj_id:
        raise ValueError(f"Address '{name}' not found in folder '{ctx.folder}'")
    scm.delete_address(obj_id)
    return f"[green]✓[/green] Address [bold]{name}[/bold] deleted."


def _set_service(ctx: ExecutionContext, args: dict) -> Any:
    """Create a service object.

    Usage:
      set service <name> tcp port <n|range>    e.g.  set service HTTP tcp port 80
      set service <name> udp port <n|range>    e.g.  set service DNS udp port 53

    pan.dev: POST /config/objects/v1/services
    """
    scm  = require_scm(ctx)
    pos  = args.get("_positional", [])
    name = pos[0] if pos else (args.get("name") or "")
    proto = pos[1].lower() if len(pos) > 1 else ""
    port  = pos[3] if len(pos) > 3 else (args.get("port") or "")

    if not name or proto not in ("tcp", "udp") or not port:
        raise ValueError(
            "Usage: set service <name> tcp|udp port <n|range>\n"
            "  e.g. set service HTTP tcp port 80\n"
            "       set service DNS  udp port 53"
        )
    payload = {
        "name":   name,
        "folder": ctx.folder,
        "protocol": {proto: {"port": str(port)}},
    }
    result = scm.create_service(payload)
    return f"[green]✓[/green] Service [bold]{name}[/bold] ({proto}/{port}) created  (id: {result.get('id', '?')})"


def _delete_service(ctx: ExecutionContext, args: dict) -> Any:
    """Delete a service object by name.

    Usage: delete service <name>
    """
    scm  = require_scm(ctx)
    name = (args.get("name") or "").strip()
    if not name:
        raise ValueError("Usage: delete service <name>")
    items  = scm.get_services(folder=ctx.folder)
    obj_id = scm._find_id_by_name(items, name)
    if not obj_id:
        raise ValueError(f"Service '{name}' not found in folder '{ctx.folder}'")
    scm.delete_service(obj_id)
    return f"[green]✓[/green] Service [bold]{name}[/bold] deleted."


def _set_tag(ctx: ExecutionContext, args: dict) -> Any:
    """Create a tag.

    Usage: set tag <name> [color <color>]
      e.g. set tag Production
           set tag Production color red
    pan.dev: POST /config/objects/v1/tags
    """
    scm  = require_scm(ctx)
    pos  = args.get("_positional", [])
    name = pos[0] if pos else (args.get("name") or "")
    if not name:
        raise ValueError("Usage: set tag <name> [color <color>]")
    payload: dict = {"name": name, "folder": ctx.folder}
    color = args.get("color") or (pos[2] if len(pos) > 2 and pos[1].lower() == "color" else "")
    if color:
        payload["color"] = color
    result = scm.create_tag(payload)
    return f"[green]✓[/green] Tag [bold]{name}[/bold] created  (id: {result.get('id', '?')})"


def _delete_tag(ctx: ExecutionContext, args: dict) -> Any:
    """Delete a tag by name.  Usage: delete tag <name>"""
    scm  = require_scm(ctx)
    name = (args.get("name") or "").strip()
    if not name:
        raise ValueError("Usage: delete tag <name>")
    items  = scm.get_tags(folder=ctx.folder)
    obj_id = scm._find_id_by_name(items, name)
    if not obj_id:
        raise ValueError(f"Tag '{name}' not found in folder '{ctx.folder}'")
    scm.delete_tag(obj_id)
    return f"[green]✓[/green] Tag [bold]{name}[/bold] deleted."


def _set_address_group(ctx: ExecutionContext, args: dict) -> Any:
    """Create a static address group.

    Usage: set address-group <name> static <member1> [<member2> ...]
      e.g. set address-group DMZ-Servers static web-server db-server
    pan.dev: POST /config/objects/v1/address-groups
    """
    scm = require_scm(ctx)
    pos = args.get("_positional", [])
    name = pos[0] if pos else (args.get("name") or "")
    if not name:
        raise ValueError("Usage: set address-group <name> static <member1> [<member2> ...]")
    # Members: everything after "static"
    try:
        static_idx = [p.lower() for p in pos].index("static")
        members = pos[static_idx + 1:]
    except ValueError:
        members = []
    if not members:
        raise ValueError("At least one member is required: set address-group <name> static <member>")
    payload = {"name": name, "folder": ctx.folder, "static": members}
    result  = scm.create_address_group(payload)
    return f"[green]✓[/green] Address group [bold]{name}[/bold] created  (id: {result.get('id', '?')})"


def _delete_address_group(ctx: ExecutionContext, args: dict) -> Any:
    """Delete an address group.  Usage: delete address-group <name>"""
    scm  = require_scm(ctx)
    name = (args.get("name") or "").strip()
    if not name:
        raise ValueError("Usage: delete address-group <name>")
    items  = scm.get_address_groups(folder=ctx.folder)
    obj_id = scm._find_id_by_name(items, name)
    if not obj_id:
        raise ValueError(f"Address group '{name}' not found in folder '{ctx.folder}'")
    scm.delete_address_group(obj_id)
    return f"[green]✓[/green] Address group [bold]{name}[/bold] deleted."


_WRITE_COMMANDS: dict[str, CommandDef] = {
    "set address": CommandDef(
        description="Create an address object — set address <name> ip-netmask|fqdn|ip-range <value>",
        category="objects",
        scope="folder",
        api_handler=_set_address,
        ssh_command=None,
        render="raw",
        feature_flag="create_address",
    ),
    "delete address": CommandDef(
        description="Delete an address object — delete address <name>",
        category="objects",
        scope="folder",
        api_handler=_delete_address,
        ssh_command=None,
        render="raw",
        feature_flag="delete_objects",
    ),
    "set address-group": CommandDef(
        description="Create a static address group — set address-group <name> static <member1> ...",
        category="objects",
        scope="folder",
        api_handler=_set_address_group,
        ssh_command=None,
        render="raw",
        feature_flag="create_address_group",
    ),
    "delete address-group": CommandDef(
        description="Delete an address group — delete address-group <name>",
        category="objects",
        scope="folder",
        api_handler=_delete_address_group,
        ssh_command=None,
        render="raw",
        feature_flag="delete_objects",
    ),
    "set service": CommandDef(
        description="Create a service object — set service <name> tcp|udp port <n>",
        category="objects",
        scope="folder",
        api_handler=_set_service,
        ssh_command=None,
        render="raw",
        feature_flag="create_service",
    ),
    "delete service": CommandDef(
        description="Delete a service object — delete service <name>",
        category="objects",
        scope="folder",
        api_handler=_delete_service,
        ssh_command=None,
        render="raw",
        feature_flag="delete_objects",
    ),
    "set tag": CommandDef(
        description="Create a tag — set tag <name> [color <color>]",
        category="objects",
        scope="folder",
        api_handler=_set_tag,
        ssh_command=None,
        render="raw",
        feature_flag="create_tag",
    ),
    "delete tag": CommandDef(
        description="Delete a tag — delete tag <name>",
        category="objects",
        scope="folder",
        api_handler=_delete_tag,
        ssh_command=None,
        render="raw",
        feature_flag="delete_objects",
    ),
}

COMMANDS.update(_WRITE_COMMANDS)


