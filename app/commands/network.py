"""Network commands (interfaces, zones, routing, HA). See docs/commands/ and docs/scm-api/specs/network.md for details."""

from __future__ import annotations

from typing import Any

from app.commands.base import CommandDef, ExecutionContext, require_scm


# ---------------------------------------------------------------------------
# Handlers
# ---------------------------------------------------------------------------

def _show_interface_all(ctx: ExecutionContext, args: dict) -> Any:
    """List all interfaces (ethernet, aggregate, loopback) in the active folder.

    Merges all three interface types so the output mirrors 'show interface all'
    on a live device.

    pan.dev: GET /config/network/v1/ethernet?folder=<folder>
             GET /config/network/v1/aggregate-ethernet?folder=<folder>
             GET /config/network/v1/loopback-interfaces?folder=<folder>
    """
    scm = require_scm(ctx)
    eth  = scm.get_interfaces(folder=ctx.folder)
    agg  = scm.get_aggregate_interfaces(folder=ctx.folder)
    loop = scm.get_loopback_interfaces(folder=ctx.folder)

    for iface in eth:
        iface.setdefault("type", "ethernet")
    for iface in agg:
        iface.setdefault("type", "aggregate")
    for iface in loop:
        iface.setdefault("type", "loopback")

    return eth + agg + loop


def _show_interface(ctx: ExecutionContext, args: dict) -> Any:
    """Show a specific interface by name.

    Falls back to listing all if no name is given.

    pan.dev: GET /config/network/v1/ethernet?folder=<folder>
    """
    name = args.get("name", "").strip()
    if not name:
        return _show_interface_all(ctx, args)

    scm = require_scm(ctx)
    eth  = scm.get_interfaces(folder=ctx.folder)
    agg  = scm.get_aggregate_interfaces(folder=ctx.folder)
    loop = scm.get_loopback_interfaces(folder=ctx.folder)
    all_ifaces = eth + agg + loop

    match = next(
        (i for i in all_ifaces if i.get("name", "").lower() == name.lower()),
        None,
    )
    if not match:
        raise RuntimeError(
            f"Interface {name!r} not found in folder {ctx.folder!r}. "
            "Use 'show interface all' to list available interfaces."
        )
    return [match]


def _show_routing_route(ctx: ExecutionContext, args: dict) -> Any:
    """List static routes configured in the active SCM folder.

    pan.dev: GET /config/network/v1/routing/static-routes?folder=<folder>
    """
    scm = require_scm(ctx)
    return scm.get_static_routes(folder=ctx.folder)


def _show_routing_summary(ctx: ExecutionContext, args: dict) -> Any:
    """List virtual routers (routing profiles) in the active SCM folder.

    pan.dev: GET /config/network/v1/virtual-routers?folder=<folder>
    """
    scm = require_scm(ctx)
    profiles = scm.get_routing_profiles(folder=ctx.folder)
    # format as generic list-of-dicts; 'dict' render handles it
    return profiles


def _show_zone(ctx: ExecutionContext, args: dict) -> Any:
    """List security zones configured in the active SCM folder.

    pan.dev: GET /config/network/v1/zones?folder=<folder>
    """
    scm = require_scm(ctx)
    return scm.get_zones(folder=ctx.folder)


def _show_ha_all(ctx: ExecutionContext, args: dict) -> Any:
    """Show full HA configuration from the active SCM folder.

    pan.dev: GET /config/network/v1/ha?folder=<folder>
    """
    scm = require_scm(ctx)
    return scm.get_ha_config(folder=ctx.folder)


def _show_ha_state(ctx: ExecutionContext, args: dict) -> Any:
    """Show HA state summary — first HA entry as a key/value panel.

    pan.dev: GET /config/network/v1/ha?folder=<folder>
    """
    scm = require_scm(ctx)
    entries = scm.get_ha_config(folder=ctx.folder)
    if entries and isinstance(entries[0], dict):
        return entries[0]
    return {}


# ---------------------------------------------------------------------------
# SSH command builders (used when --remote is appended)
# ---------------------------------------------------------------------------

def _ssh_interface(args: dict) -> str:
    name = args.get("name", "")
    return f"show interface {name}" if name else "show interface all"


# ---------------------------------------------------------------------------
# Command table — merged into COMMANDS by registry.py
# ---------------------------------------------------------------------------

COMMANDS: dict[str, CommandDef] = {
    "show interface all": CommandDef(
        description="Show all interfaces in the active folder",
        category="network",
        scope="folder",
        api_handler=_show_interface_all,
        ssh_command="show interface all",
        render="interfaces",
    ),
    "show interface": CommandDef(
        description="Show a specific interface — show interface <name>",
        category="network",
        scope="folder",
        api_handler=_show_interface,
        ssh_command=_ssh_interface,
        render="interfaces",
    ),
    "show routing route": CommandDef(
        description="Show static routes in the active folder",
        category="network",
        scope="folder",
        api_handler=_show_routing_route,
        ssh_command="show routing route",
        render="routes",
    ),
    "show routing summary": CommandDef(
        description="Show virtual routers / routing profiles in the active folder",
        category="network",
        scope="folder",
        api_handler=_show_routing_summary,
        ssh_command="show routing summary",
        render="dict",
    ),
    "show zone": CommandDef(
        description="Show security zones in the active folder",
        category="network",
        scope="folder",
        api_handler=_show_zone,
        ssh_command="show zone",
        render="zones",
    ),
    "show high-availability all": CommandDef(
        description="Show full HA configuration from the active folder",
        category="network",
        scope="folder",
        api_handler=_show_ha_all,
        ssh_command="show high-availability all",
        render="ha",
    ),
    "show high-availability state": CommandDef(
        description="Show HA state summary from the active folder",
        category="network",
        scope="folder",
        api_handler=_show_ha_state,
        ssh_command="show high-availability state",
        render="ha",
    ),
}
