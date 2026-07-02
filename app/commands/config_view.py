"""Config visibility + rollback commands — config versions, running config,
and the folder config dumped as replayable `set` commands.

Command keys are chosen to NOT collide with the shell's staged-changes view
(`show config` bare / `pending` / `diff` is intercepted in dispatch.py):

    show config running [<resource>]     running config version / one resource
    show config versions [<id>]          SCM config-version history
    show config format set [<resource>]  folder objects as replayable set lines
    load config version <id> [confirm]   rollback: load a version as candidate

`show config format set` is driven by the per-resource spec table
``_FORMAT_SET_SPECS`` below — adding a resource means adding one table entry
(getter + positional-token builder + keyword fields), never a new function
chain. The address variant map is INVERTED from the auto-generated
``app/settings/field_catalog.py`` so CLI tokens stay in sync with the specs.

SCM endpoints (docs/scm-api/specs/ngfw-config-operations.md):
    GET  /config/operations/v1/config-versions
    GET  /config/operations/v1/config-versions/{version}
    GET  /config/operations/v1/config-versions/running
    POST /config/operations/v1/config-versions:load   body {"version": n}
"""

from __future__ import annotations

from typing import Any, Callable, Optional

from app.commands.base import CommandDef, ExecutionContext, require_scm

# ---------------------------------------------------------------------------
# Value quoting — one rule everywhere: quote anything the shell would split.
# ---------------------------------------------------------------------------


def _q(value: Any) -> str:
    """Return *value* as a CLI token, double-quoted when it contains spaces.

    Embedded double quotes are escaped so the emitted line survives shlex
    tokenizing on replay (e.g. description 'say "hi"').
    """
    text = str(value)
    if text == "" or any(ch.isspace() for ch in text) or '"' in text:
        return '"' + text.replace('"', '\\"') + '"'
    return text


def _join_list(value: Any) -> str:
    """Join a list field into the comma form the set commands accept (tag a,b)."""
    if isinstance(value, (list, tuple)):
        return ",".join(str(item) for item in value)
    return str(value)


# ---------------------------------------------------------------------------
# Variant map — inverted from the generated field catalog (api field → CLI
# token), with a hard fallback so a broken/regenerated catalog never takes
# `show config format set` down.
# ---------------------------------------------------------------------------

_ADDRESS_VARIANT_FALLBACK = {
    "ip_netmask": "ip-netmask",
    "ip_range": "ip-range",
    "ip_wildcard": "ip-wildcard",
    "fqdn": "fqdn",
}


def _address_variant_map() -> dict[str, str]:
    """api payload field → CLI token, inverted from FIELD_CATALOG's address variant."""
    try:
        from app.settings.field_catalog import FIELD_CATALOG

        choices = FIELD_CATALOG["set cngfw addresses"]["payload"]["variant"]["choices"]
        inverted = {api_field: cli_token for cli_token, api_field in choices.items()}
        # Sanity: the catalog must cover the known variants or we fall back.
        if set(inverted) >= set(_ADDRESS_VARIANT_FALLBACK):
            return inverted
    except (ImportError, KeyError, TypeError):
        pass
    return dict(_ADDRESS_VARIANT_FALLBACK)


_ADDRESS_VARIANTS = _address_variant_map()

# EDL recurring block key → the `frequency` token the curated set command takes.
_EDL_FREQUENCY_TOKENS = {
    "hourly": "hourly",
    "daily": "daily",
    "weekly": "weekly",
    "monthly": "monthly",
    "5minute": "5minute",
    "five_minute": "5minute",
}


# ---------------------------------------------------------------------------
# Positional-token builders — one small named function per nested payload
# shape. Each returns the tokens that follow the object name, or None when
# the object has no representable value (it is then skipped).
# ---------------------------------------------------------------------------


def _address_tokens(obj: dict) -> Optional[list[str]]:
    """ip_netmask/ip_range/ip_wildcard/fqdn value → `<cli-type> <value>`."""
    for api_field, cli_token in _ADDRESS_VARIANTS.items():
        value = obj.get(api_field)
        if value:
            return [cli_token, _q(value)]
    return None


def _address_group_tokens(obj: dict) -> Optional[list[str]]:
    """static members → `static m1 m2`; dynamic filter → `dynamic filter "<expr>"`."""
    static_members = obj.get("static")
    if isinstance(static_members, list) and static_members:
        return ["static"] + [_q(member) for member in static_members]
    dynamic = obj.get("dynamic")
    if isinstance(dynamic, dict) and dynamic.get("filter"):
        return ["dynamic", "filter", _q(dynamic["filter"])]
    return None


def _service_tokens(obj: dict) -> Optional[list[str]]:
    """protocol.tcp/udp {port, source_port} → `tcp port <p> [source-port <sp>]`."""
    protocol = obj.get("protocol")
    if not isinstance(protocol, dict):
        return None
    for proto in ("tcp", "udp"):
        block = protocol.get(proto)
        if isinstance(block, dict) and block.get("port"):
            tokens = [proto, "port", _q(block["port"])]
            if block.get("source_port"):
                tokens += ["source-port", _q(block["source_port"])]
            return tokens
    return None


def _service_group_tokens(obj: dict) -> Optional[list[str]]:
    """members list → `members svc1 svc2 …`."""
    members = obj.get("members")
    if isinstance(members, list) and members:
        return ["members"] + [_q(member) for member in members]
    return None


def _tag_tokens(obj: dict) -> Optional[list[str]]:
    """Tags carry no positional value — color/comments are keyword fields."""
    return []


def _edl_tokens(obj: dict) -> Optional[list[str]]:
    """type.{ip|domain|url|imsi|imei} {url, recurring} → `type <t> url <u> [frequency <f>]`."""
    type_block = obj.get("type")
    if not isinstance(type_block, dict):
        return None
    for edl_type, spec in type_block.items():
        if not isinstance(spec, dict) or not spec.get("url"):
            continue
        tokens = ["type", edl_type, "url", _q(spec["url"])]
        recurring = spec.get("recurring")
        if isinstance(recurring, dict) and recurring:
            frequency = _EDL_FREQUENCY_TOKENS.get(next(iter(recurring)).lower())
            if frequency:
                tokens += ["frequency", frequency]
        return tokens
    return None


# ---------------------------------------------------------------------------
# Per-resource spec table — THE place to add format-set support for a new
# resource. Fields:
#   getter      SCMClient list method (folder-scoped)
#   set_key     the curated set-command key the emitted line replays through
#   positional  callable(obj) -> tokens after the name (None → skip object)
#   keywords    ordered (cli_keyword, api_field) pairs appended when present;
#               list-valued api fields are comma-joined (tag a,b)
# ---------------------------------------------------------------------------

_FORMAT_SET_SPECS: dict[str, dict] = {
    "address": {
        "getter": "get_addresses",
        "set_key": "set address",
        "positional": _address_tokens,
        "keywords": (("description", "description"), ("tag", "tag")),
    },
    "address-group": {
        "getter": "get_address_groups",
        "set_key": "set address-group",
        "positional": _address_group_tokens,
        "keywords": (("description", "description"), ("tag", "tag")),
    },
    "service": {
        "getter": "get_services",
        "set_key": "set service",
        "positional": _service_tokens,
        "keywords": (("description", "description"), ("tag", "tag")),
    },
    "service-group": {
        "getter": "get_service_groups",
        "set_key": "set service-group",
        "positional": _service_group_tokens,
        "keywords": (("description", "description"), ("tag", "tag")),
    },
    "tag": {
        "getter": "get_tags",
        "set_key": "set tag",
        "positional": _tag_tokens,
        "keywords": (("color", "color"), ("comments", "comments")),
    },
    "external-dynamic-list": {
        "getter": "get_external_dynamic_lists",
        "set_key": "set external-dynamic-list",
        "positional": _edl_tokens,
        "keywords": (("description", "description"), ("tag", "tag")),
    },
}

# Accept common spellings for the resource argument (plural, API path names).
_RESOURCE_ALIASES: dict[str, str] = {}
for _resource in _FORMAT_SET_SPECS:
    _RESOURCE_ALIASES[_resource] = _resource
    _RESOURCE_ALIASES[_resource + "s"] = _resource
_RESOURCE_ALIASES["addresses"] = "address"
_RESOURCE_ALIASES["edl"] = "external-dynamic-list"
_RESOURCE_ALIASES["edls"] = "external-dynamic-list"


def _resolve_resource(token: str) -> str:
    """Map a user-typed resource word onto a spec-table key (or raise usage)."""
    resource = _RESOURCE_ALIASES.get(token.strip().lower())
    if not resource:
        supported = " | ".join(_FORMAT_SET_SPECS)
        raise ValueError(
            f"Unsupported resource {token!r} for config format set.\n"
            f"  Supported: {supported}"
        )
    return resource


def format_set_lines(resource: str, objects: list[dict]) -> list[str]:
    """Render *objects* of *resource* as replayable `set <resource> …` lines.

    Objects with no representable value (unknown variant shape) are skipped —
    the output must stay 100% replayable, so nothing but set lines is emitted.
    """
    spec = _FORMAT_SET_SPECS[resource]
    build_positional: Callable[[dict], Optional[list[str]]] = spec["positional"]
    lines: list[str] = []
    for obj in objects:
        name = obj.get("name")
        if not name:
            continue
        positional = build_positional(obj)
        if positional is None:
            continue
        tokens = [spec["set_key"], _q(name)] + positional
        for cli_keyword, api_field in spec["keywords"]:
            value = obj.get(api_field)
            if value in (None, "", [], {}):
                continue
            tokens += [cli_keyword, _q(_join_list(value))]
        lines.append(" ".join(tokens))
    return lines


def _defined_in_folder(obj: dict, folder: str) -> bool:
    """True when the object is defined in *folder* itself.

    SCM folder listings include objects inherited from ancestor folders and
    predefined snippets; replaying those into the folder would duplicate
    them, so the dump only includes objects the folder owns. Objects without
    any location marker are kept (fail open — better to show than hide).
    """
    location = obj.get("folder") or obj.get("snippet") or obj.get("device")
    return location is None or location == folder


def _fetch_format_set(ctx: ExecutionContext, resources: list[str]) -> list[str]:
    """Fetch each resource in the active folder and emit its set lines."""
    scm = require_scm(ctx)
    lines: list[str] = []
    for resource in resources:
        getter = getattr(scm, _FORMAT_SET_SPECS[resource]["getter"])
        objects = [o for o in getter(folder=ctx.folder) if _defined_in_folder(o, ctx.folder)]
        lines.extend(format_set_lines(resource, objects))
    return lines


# ---------------------------------------------------------------------------
# Handlers
# ---------------------------------------------------------------------------

_VERSION_TABLE_COLUMNS = ("id", "version", "date", "admin", "scope", "description")


def _show_config_format_set(ctx: ExecutionContext, args: dict) -> Any:
    """Dump the active folder's config as replayable set commands.

    Usage: show config format set [<resource>]
    """
    positional = args.get("_positional", [])
    if positional:
        resources = [_resolve_resource(positional[0])]
    else:
        resources = list(_FORMAT_SET_SPECS)
    lines = _fetch_format_set(ctx, resources)
    if not lines:
        return f"(no {', '.join(resources)} objects defined in folder '{ctx.folder}')"
    # A list of plain strings renders line-by-line (no table, no panel), so
    # `| match` filters and copy/replay work on clean set lines.
    return lines


def _show_config_running(ctx: ExecutionContext, args: dict) -> Any:
    """Show the running config version — or one resource as set commands.

    Usage: show config running [<resource>]

    Bare form: GET /config-versions/running. The endpoint returns config
    VERSION metadata (not raw config content) — it is rendered as-is.
    With a resource: the active folder's objects of that type, in the same
    replayable set-command format as `show config format set`.
    """
    positional = args.get("_positional", [])
    if positional:
        resource = _resolve_resource(positional[0])
        lines = _fetch_format_set(ctx, [resource])
        return lines or f"(no {resource} objects defined in folder '{ctx.folder}')"
    scm = require_scm(ctx)
    running = scm.get_running_config_version()
    # Unwrap a {"data": [...]} envelope so the fallback renderer draws a table.
    if isinstance(running, dict) and isinstance(running.get("data"), list):
        return running["data"]
    return running


def _show_config_versions(ctx: ExecutionContext, args: dict) -> Any:
    """List SCM config versions, or show one version's full record.

    Usage: show config versions [<id>]
    """
    positional = args.get("_positional", [])
    if positional:
        version = positional[0]
        if not version.isdigit():
            raise ValueError("Usage: show config versions [<id>]  — <id> is numeric, e.g. show config versions 123")
        return require_scm(ctx).get_config_version(version)
    rows = require_scm(ctx).get_config_versions()
    projected = [
        {column: row[column] for column in _VERSION_TABLE_COLUMNS if column in row}
        for row in rows
        if isinstance(row, dict)
    ]
    # Honest fallback: if the API shape ever drifts from the spec's
    # config-version schema, show whatever it returned instead of {}.
    if any(projected):
        return projected
    return rows


def _load_config_version(ctx: ExecutionContext, args: dict) -> Any:
    """Rollback: load a config version as the tenant's candidate config.

    Usage: load config version <id> [confirm]

    Without the trailing `confirm` token this only PREVIEWS the rollback
    (fetching the version's metadata). With `confirm` it POSTs
    /config-versions:load — which executes in SCM immediately (load is not a
    staged write) — and reminds the operator to `commit` to push to devices.
    """
    scm = require_scm(ctx)
    positional = args.get("_positional", [])
    version = positional[0] if positional else ""
    if not version.isdigit():
        raise ValueError(
            "Usage: load config version <id> [confirm]\n"
            "  Find version ids with: show config versions"
        )
    confirmed = len(positional) > 1 and positional[1].lower() == "confirm"

    # Fetch the version record first — validates the id (404 → friendly
    # error upstream) and lets the operator see what they are loading.
    record = scm.get_config_version(version)
    detail_lines = []
    if isinstance(record, dict):
        for field in ("version", "date", "admin", "scope", "description"):
            if record.get(field):
                detail_lines.append(f"  {field:<12} {record[field]}")
    detail = "\n".join(detail_lines) or "  (no metadata returned)"

    if not confirmed:
        return (
            f"ROLLBACK PREVIEW — config version {version}\n"
            f"{detail}\n\n"
            f"This will load version {version} as the tenant's CANDIDATE configuration,\n"
            "replacing any uncommitted changes (including ones made in the SCM UI).\n"
            "The load runs in SCM immediately — it is NOT staged — but nothing\n"
            "reaches devices until you commit.\n\n"
            f"To proceed:  load config version {version} confirm\n"
            "Then:        commit"
        )

    scm.load_config_version(int(version))
    return (
        f"✓ Config version {version} loaded as the candidate configuration.\n"
        f"{detail}\n\n"
        "The candidate now matches this version (executed in SCM — not staged).\n"
        "Review:  show config versions   |   show config running\n"
        "Push to devices:  commit"
    )


# ---------------------------------------------------------------------------
# Command table
# ---------------------------------------------------------------------------

_RESOURCE_USAGE = "|".join(_FORMAT_SET_SPECS)

COMMANDS: dict[str, CommandDef] = {
    "show config running": CommandDef(
        description="Show the running config version, or one resource as set commands",
        category="operations",
        scope="folder",
        api_handler=_show_config_running,
        ssh_command="show config running",
        render="",  # dict → key/value, list[str] → plain replayable lines
        feature_flag="config_view",
        usage=f"show config running [{_RESOURCE_USAGE}]",
    ),
    "show config versions": CommandDef(
        description="List SCM config versions (id, date, admin) or one version by id",
        category="operations",
        scope="global",
        api_handler=_show_config_versions,
        ssh_command=None,
        render="",  # list[dict] → table, dict → key/value
        feature_flag="config_view",
        usage="show config versions [<id>]",
    ),
    "show config format set": CommandDef(
        description="Dump folder config as replayable set commands",
        category="operations",
        scope="folder",
        api_handler=_show_config_format_set,
        ssh_command=None,
        render="",  # list[str] → plain lines so `| match` pipes naturally
        feature_flag="config_view",
        usage=f"show config format set [{_RESOURCE_USAGE}]",
    ),
    "load config version": CommandDef(
        description="Rollback: load a config version as the candidate (preview without confirm)",
        category="operations",
        scope="global",
        api_handler=_load_config_version,
        ssh_command=None,
        render="raw",
        feature_flag="config_rollback",
        usage="load config version <id> [confirm]",
    ),
}
