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
    ),
    "show address-group": CommandDef(
        description="Show address groups in the active folder",
        category="objects",
        scope="folder",
        api_handler=_show_address_group,
        ssh_command=None,
        render="address_groups",
    ),
    "show service": CommandDef(
        description="Show service objects in the active folder",
        category="objects",
        scope="folder",
        api_handler=_show_service,
        ssh_command=None,
        render="services",
    ),
    "show tag": CommandDef(
        description="Show tags in the active folder",
        category="objects",
        scope="folder",
        api_handler=_show_tag,
        ssh_command=None,
        render="tags",
    ),
    "show external-dynamic-list": CommandDef(
        description="Show external dynamic lists (EDLs) in the active folder",
        category="objects",
        scope="folder",
        api_handler=_show_external_dynamic_list,
        ssh_command=None,
        render="edl_list",
    ),
}

