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


