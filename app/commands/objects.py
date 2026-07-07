"""Objects commands (addresses, services, tags, EDLs).

Read commands:  app/commands/objects.py → SCM /config/objects/v1
Write commands: set/update/delete for addresses, services, tags, address-groups, EDLs
See docs/commands/ and docs/scm-api/specs/ngfw-objects.yaml for full API reference.
"""

from __future__ import annotations

from typing import Any

from app.commands.base import (
    CommandDef,
    ExecutionContext,
    delete_handler,
    merge_common_fields,
    parse_kv_tail,
    require_scm,
    show_handler,
)


# ---------------------------------------------------------------------------
# Command table — merged into COMMANDS by registry.py
#
# Plain list commands use show_handler(<SCMClient method>) from base.py;
# pan.dev: GET /config/objects/v1/<resource>?folder=<folder>
# ---------------------------------------------------------------------------

COMMANDS: dict[str, CommandDef] = {
    "show address": CommandDef(
        description="Show address objects in the active folder",
        category="objects",
        scope="folder",
        api_handler=show_handler("get_addresses"),
        ssh_command=None,
        render="address_objects",
        feature_flag="show_address",
        usage="show address [<name>]",
    ),
    "show address-group": CommandDef(
        description="Show address groups in the active folder",
        category="objects",
        scope="folder",
        api_handler=show_handler("get_address_groups"),
        ssh_command=None,
        render="address_groups",
        feature_flag="show_address_group",
        usage="show address-group [<name>]",
    ),
    "show service": CommandDef(
        description="Show service objects in the active folder",
        category="objects",
        scope="folder",
        api_handler=show_handler("get_services"),
        ssh_command=None,
        render="services",
        feature_flag="show_service",
        usage="show service [<name>]",
    ),
    "show tag": CommandDef(
        description="Show tags in the active folder",
        category="objects",
        scope="folder",
        api_handler=show_handler("get_tags"),
        ssh_command=None,
        render="tags",
        feature_flag="show_tag",
        usage="show tag [<name>]",
    ),
    "show external-dynamic-list": CommandDef(
        description="Show external dynamic lists (EDLs) in the active folder",
        category="objects",
        scope="folder",
        api_handler=show_handler("get_external_dynamic_lists"),
        ssh_command=None,
        render="edl_list",
        feature_flag="show_external_dynamic_list",
        usage="show external-dynamic-list [<name>]",
    ),
}


_EXTRA_COMMANDS: dict[str, CommandDef] = {
    "show service-group": CommandDef(
        description="Show service groups in the active folder",
        category="objects",
        scope="folder",
        api_handler=show_handler("get_service_groups"),
        ssh_command="show objects service-group",
        render="list",
        feature_flag="service_groups",
    ),
    "show application-group": CommandDef(
        description="Show application groups in the active folder",
        category="objects",
        scope="folder",
        api_handler=show_handler("get_application_groups"),
        ssh_command="show objects application-group",
        render="list",
        feature_flag="app_groups",
    ),
    "show application-filter": CommandDef(
        description="Show application filters in the active folder",
        category="objects",
        scope="folder",
        api_handler=show_handler("get_application_filters"),
        ssh_command=None,
        render="list",
        feature_flag="app_groups",
    ),
    "show schedule": CommandDef(
        description="Show schedules in the active folder",
        category="objects",
        scope="folder",
        api_handler=show_handler("get_schedules"),
        ssh_command=None,
        render="list",
        feature_flag="schedules",
    ),
    "show region": CommandDef(
        description="Show regions (TSG-wide, no folder filter)",
        category="objects",
        scope="global",
        api_handler=show_handler("get_regions", folder_scoped=False),
        ssh_command=None,
        render="list",
        feature_flag="regions",
    ),
    "show hip-object": CommandDef(
        description="Show GlobalProtect HIP objects in the active folder",
        category="objects",
        scope="folder",
        api_handler=show_handler("get_hip_objects"),
        ssh_command=None,
        render="list",
        feature_flag="hip",
    ),
    "show hip-profile": CommandDef(
        description="Show GlobalProtect HIP profiles in the active folder",
        category="objects",
        scope="folder",
        api_handler=show_handler("get_hip_profiles"),
        ssh_command=None,
        render="list",
        feature_flag="hip",
    ),
    "show log-forwarding-profile": CommandDef(
        description="Show log forwarding profiles in the active folder",
        category="objects",
        scope="folder",
        api_handler=show_handler("get_log_forwarding_profiles"),
        ssh_command=None,
        render="list",
        feature_flag="log_profiles",
    ),
}

COMMANDS.update(_EXTRA_COMMANDS)


# ---------------------------------------------------------------------------
# Write handlers — configure mode, all POST/DELETE via SCM API
#
# Argument parsing convention:
#   positional[0]  = object name
#   positional[1]  = subtype keyword (ip-netmask, tcp, static, ...)
#   positional[2]  = primary value
#   positional[3+] = optional keyword-value pairs (description, tag, color...)
# ---------------------------------------------------------------------------

_TAG_COLORS = {
    "red", "green", "blue", "yellow", "copper", "orange", "purple", "gray",
    "light-green", "cyan", "light-gray", "blue-gray", "lime", "black", "gold",
    "brown", "olive", "maroon", "red-orange", "yellow-orange", "forest-green",
    "turquoise-blue", "azure-blue", "cerulean-blue", "midnight-blue", "medium-blue",
    "cobalt-blue", "violet-blue", "blue-violet", "medium-violet", "medium-rose",
    "lavender", "orchid", "thistle", "peach", "salmon", "magenta", "red-violet",
    "mahogany", "burnt-sienna", "chestnut",
}

_ADDR_TYPE_MAP = {
    "ip-netmask":  "ip_netmask",
    "ip-range":    "ip_range",
    "ip-wildcard": "ip_wildcard",
    "fqdn":        "fqdn",
}



def _set_address(ctx: ExecutionContext, args: dict) -> Any:
    """Create an address object in the active SCM folder.

    Syntax (Palo Alto style):
      set address <name> ip-netmask  <cidr>           e.g. 10.1.0.0/24 or 10.1.2.3/32
      set address <name> ip-range    <start>-<end>    e.g. 10.1.0.1-10.1.0.254
      set address <name> ip-wildcard <ip>/<mask>      e.g. 10.0.0.0/255.255.0.0
      set address <name> fqdn        <domain-or-glob> e.g. *.example.com

    Optional (append after the type/value):
      description <text>    — object description
      tag         <name>    — associate a tag (append multiple times)

    Address subtypes:
      ip-netmask   single host (/32) or subnet (CIDR notation)
      ip-range     inclusive IP range with hyphen separator
      ip-wildcard  wildcard mask with slash separator (opposite of CIDR)
      fqdn         fully qualified domain name or wildcard glob

    Examples:
      set address WebServer   ip-netmask  10.1.2.3/32
      set address DMZ-Subnet  ip-netmask  10.1.0.0/24  description "DMZ network"
      set address Corp-Range  ip-range    10.0.0.1-10.0.0.254
      set address NetWild     ip-wildcard 10.0.0.0/255.255.0.0
      set address API-Server  fqdn        api.example.com  tag Production

    pan.dev: POST /config/objects/v1/addresses
    """
    scm = require_scm(ctx)
    pos = args.get("_positional", [])
    name = pos[0] if pos else (args.get("name") or "")
    if not name:
        raise ValueError(
            "Usage: set address <name> ip-netmask|ip-range|ip-wildcard|fqdn <value>\n"
            "  e.g.  set address WebServer ip-netmask 10.1.2.3/32\n"
            "        set address DMZ-Net   ip-netmask 10.1.0.0/24  description 'DMZ'\n"
            "        set address CDN       ip-wildcard 104.16.0.0/255.240.0.0\n"
            "        set address BadHosts  fqdn        *.malware.example.com"
        )
    addr_type = pos[1].lower() if len(pos) > 1 else ""
    addr_val  = pos[2] if len(pos) > 2 else ""
    if addr_type not in _ADDR_TYPE_MAP:
        raise ValueError(
            f"Unknown address type: {addr_type!r}\n"
            "  Valid types:  ip-netmask | ip-range | ip-wildcard | fqdn\n"
            "  ip-netmask   10.1.0.0/24  or  10.1.2.3/32\n"
            "  ip-range     10.1.0.1-10.1.0.254\n"
            "  ip-wildcard  10.0.0.0/255.255.0.0\n"
            "  fqdn         *.example.com  or  host.example.com"
        )
    if not addr_val:
        raise ValueError(f"Missing value after {addr_type!r}")
    kv = parse_kv_tail(pos, 3)
    payload: dict = {"name": name, "folder": ctx.folder, _ADDR_TYPE_MAP[addr_type]: addr_val}
    if args.get("description") or kv.get("description"):
        payload["description"] = args.get("description") or kv["description"]
    tags = []
    if args.get("tag"):
        tags.append(args["tag"])
    if kv.get("tag"):
        tags.append(kv["tag"])
    if tags:
        payload["tag"] = tags
    result = scm.create_address(payload)
    return (
        f"[green]✓[/green] Address [bold]{name}[/bold] ({addr_type}: {addr_val}) created\n"
        f"  folder: {ctx.folder}  id: {result.get('id', '?')}"
    )


def _delete_address(ctx: ExecutionContext, args: dict) -> Any:
    """Delete an address object.  Usage: delete address <name>"""
    scm = require_scm(ctx)
    name = (args.get("name") or "").strip()
    if not name:
        raise ValueError("Usage: delete address <name>")
    items  = scm.get_addresses(folder=ctx.folder)
    obj_id = scm._find_id_by_name(items, name)
    if not obj_id:
        raise ValueError(f"Address '{name}' not found in folder '{ctx.folder}'")
    scm.delete_address(obj_id)
    return f"[green]✓[/green] Address [bold]{name}[/bold] deleted from folder {ctx.folder}."


def _set_address_group(ctx: ExecutionContext, args: dict) -> Any:
    """Create a static or dynamic address group in the active folder.

    Static group — explicit member list:
      set address-group <name> static <member1> [<member2> ...]

    Dynamic group — tag-based filter evaluated at runtime:
      set address-group <name> dynamic filter <expression>
        expression examples:
          'Production'                  single tag
          'Production and DMZ'          AND
          'Production or Staging'       OR
          'Production and not Staging'  compound

    Optional:  description <text>   tag <name>

    Examples:
      set address-group WebServers  static  web1 web2 web3
      set address-group ProdHosts   dynamic filter 'Production'
      set address-group AllEnvs     dynamic filter 'Production or Staging'  description "All envs"

    pan.dev: POST /config/objects/v1/address-groups
    """
    scm = require_scm(ctx)
    pos = args.get("_positional", [])
    name = pos[0] if pos else (args.get("name") or "")
    if not name:
        raise ValueError(
            "Usage:\n"
            "  set address-group <name> static  <member1> [...]\n"
            "  set address-group <name> dynamic filter '<expression>'"
        )
    mode = pos[1].lower() if len(pos) > 1 else ""
    payload: dict = {"name": name, "folder": ctx.folder}
    if mode == "static":
        _KW = {"description", "tag"}
        members, kv_start = [], len(pos)
        for i, tok in enumerate(pos[2:], 2):
            if tok.lower() in _KW:
                kv_start = i; break
            members.append(tok)
        if not members:
            raise ValueError("Static group needs at least one member.\n  e.g. set address-group Servers static web1 db1")
        payload["static"] = members
        kv = parse_kv_tail(pos, kv_start)
    elif mode == "dynamic":
        if len(pos) < 3 or pos[2].lower() != "filter":
            raise ValueError("Usage: set address-group <name> dynamic filter '<expression>'")
        expr = pos[3] if len(pos) > 3 else ""
        if not expr:
            raise ValueError("Missing filter expression after 'filter'")
        payload["dynamic"] = {"filter": expr}
        kv = parse_kv_tail(pos, 4)
    else:
        raise ValueError(f"Unknown group type {mode!r} — use 'static' or 'dynamic'")
    if args.get("description") or kv.get("description"):
        payload["description"] = args.get("description") or kv["description"]
    tags = [t for t in [args.get("tag"), kv.get("tag")] if t]
    if tags:
        payload["tag"] = tags
    result = scm.create_address_group(payload)
    return (
        f"[green]✓[/green] Address group [bold]{name}[/bold] ({mode}) created\n"
        f"  folder: {ctx.folder}  id: {result.get('id', '?')}"
    )


def _set_service(ctx: ExecutionContext, args: dict) -> Any:
    """Create a TCP or UDP service object in the active folder.

    Syntax:
      set service <name> tcp port <dst-port>
      set service <name> udp port <dst-port>
      set service <name> tcp port <dst-port> source-port <src-port>
      set service <name> udp port <dst-port> source-port <src-port>

    Port formats:
      single     80
      range      8080-8090
      list       80,443,8080   (comma-separated, no spaces)

    Optional:  description <text>   tag <name>

    Examples:
      set service HTTP      tcp port 80
      set service HTTPS     tcp port 443
      set service DNS       udp port 53
      set service HTTP-ALT  tcp port 8080-8090  description "Alt HTTP"
      set service RPC-UDP   udp port 111  source-port 1024-65535
      set service APP       tcp port 8443  tag Production  description "App TLS"

    pan.dev: POST /config/objects/v1/services
    """
    scm = require_scm(ctx)
    pos = args.get("_positional", [])
    name  = pos[0] if pos else (args.get("name") or "")
    proto = pos[1].lower() if len(pos) > 1 else ""
    if not name or proto not in ("tcp", "udp"):
        raise ValueError(
            "Usage: set service <name> tcp|udp port <n>\n"
            "  e.g. set service HTTP tcp port 80\n"
            "       set service DNS  udp port 53\n"
            "       set service Range tcp port 8080-8090  source-port 1024-65535"
        )
    pos_lower = [p.lower() for p in pos]
    try:
        port_idx = pos_lower.index("port")
        dst_port = pos[port_idx + 1] if port_idx + 1 < len(pos) else ""
    except ValueError:
        dst_port = ""
    if not dst_port:
        raise ValueError(f"Missing 'port' keyword.  e.g. set service HTTP tcp port 80")
    proto_block: dict = {"port": dst_port}
    try:
        sp_idx = pos_lower.index("source-port")
        src_port = pos[sp_idx + 1] if sp_idx + 1 < len(pos) else ""
        if src_port:
            proto_block["source_port"] = src_port
    except ValueError:
        pass
    # Description / tag from remaining tokens
    kv_tokens = [p for p in pos[2:] if p.lower() not in ("port", "source-port", dst_port, proto_block.get("source_port", ""))]
    kv: dict[str, str] = {}
    i = 0
    while i + 1 < len(kv_tokens):
        kv[kv_tokens[i].lower()] = kv_tokens[i + 1]; i += 2
    payload: dict = {"name": name, "folder": ctx.folder, "protocol": {proto: proto_block}}
    if args.get("description") or kv.get("description"):
        payload["description"] = args.get("description") or kv["description"]
    tags = [t for t in [args.get("tag"), kv.get("tag")] if t]
    if tags:
        payload["tag"] = tags
    result = scm.create_service(payload)
    src_info = f"  source-port: {proto_block['source_port']}" if "source_port" in proto_block else ""
    return (
        f"[green]✓[/green] Service [bold]{name}[/bold] ({proto}/{dst_port}{src_info}) created\n"
        f"  folder: {ctx.folder}  id: {result.get('id', '?')}"
    )


def _set_service_group(ctx: ExecutionContext, args: dict) -> Any:
    """Create a service group (named collection of service objects).

    Syntax:
      set service-group <name> members <svc1> [<svc2> ...]

    Optional:  tag <name>

    Members must be existing service object names in the same folder.

    Examples:
      set service-group Web-Services  members HTTP HTTPS
      set service-group DB-Ports      members MySQL PostgreSQL Redis  tag Production
      set service-group Mail-Ports    members SMTP SMTPS IMAP IMAPS

    pan.dev: POST /config/objects/v1/service-groups
    """
    scm = require_scm(ctx)
    pos = args.get("_positional", [])
    name = pos[0] if pos else (args.get("name") or "")
    if not name:
        raise ValueError("Usage: set service-group <name> members <svc1> [svc2 ...]")
    pos_lower = [p.lower() for p in pos]
    try:
        mem_idx = pos_lower.index("members")
    except ValueError:
        raise ValueError("Missing 'members' keyword.\n  e.g. set service-group Web members HTTP HTTPS")
    _KW = {"tag", "description"}
    members, kv_start = [], len(pos)
    for i, tok in enumerate(pos[mem_idx + 1:], mem_idx + 1):
        if tok.lower() in _KW:
            kv_start = i; break
        members.append(tok)
    if not members:
        raise ValueError("At least one service member required.")
    kv = parse_kv_tail(pos, kv_start)
    payload: dict = {"name": name, "folder": ctx.folder, "members": members}
    if args.get("description") or kv.get("description"):
        payload["description"] = args.get("description") or kv["description"]
    tags = [t for t in [args.get("tag"), kv.get("tag")] if t]
    if tags:
        payload["tag"] = tags
    result = scm.create_service_group(payload)
    return (
        f"[green]✓[/green] Service group [bold]{name}[/bold] ({len(members)} members: {', '.join(members)}) created\n"
        f"  folder: {ctx.folder}  id: {result.get('id', '?')}"
    )


def _set_tag(ctx: ExecutionContext, args: dict) -> Any:
    """Create a tag in the active folder.

    Syntax:
      set tag <name>
      set tag <name> color <color>
      set tag <name> color <color> comments <text>

    Available colors (40 options):
      red, green, blue, yellow, copper, orange, purple, gray,
      light-green, cyan, light-gray, blue-gray, lime, black, gold,
      brown, olive, maroon, red-orange, yellow-orange, forest-green,
      turquoise-blue, azure-blue, cerulean-blue, midnight-blue, medium-blue,
      cobalt-blue, violet-blue, blue-violet, medium-violet, medium-rose,
      lavender, orchid, thistle, peach, salmon, magenta, red-violet,
      mahogany, burnt-sienna, chestnut

    Examples:
      set tag Production
      set tag Staging      color yellow
      set tag Critical     color red     comments "High-risk objects"
      set tag DMZ          color blue

    pan.dev: POST /config/objects/v1/tags
    """
    scm = require_scm(ctx)
    pos = args.get("_positional", [])
    name = pos[0] if pos else (args.get("name") or "")
    if not name:
        raise ValueError("Usage: set tag <name> [color <color>] [comments <text>]")
    kv = parse_kv_tail(pos, 1)
    payload: dict = {"name": name, "folder": ctx.folder}
    color = args.get("color") or kv.get("color") or ""
    if color:
        norm = color.lower()
        if norm not in _TAG_COLORS:
            close = sorted(c for c in _TAG_COLORS if c.startswith(norm[:3]))[:5]
            hint  = f"  Did you mean: {', '.join(close)}?" if close else ""
            raise ValueError(
                f"Unknown color: {color!r}\n"
                f"  Valid: {', '.join(sorted(_TAG_COLORS))}\n{hint}"
            )
        payload["color"] = norm
    comments = args.get("comments") or kv.get("comments") or ""
    if comments:
        payload["comments"] = comments
    result = scm.create_tag(payload)
    color_info = f" color: {color}" if color else ""
    return (
        f"[green]✓[/green] Tag [bold]{name}[/bold] created{color_info}\n"
        f"  folder: {ctx.folder}  id: {result.get('id', '?')}"
    )


def _set_external_dynamic_list(ctx: ExecutionContext, args: dict) -> Any:
    """Create an External Dynamic List (EDL) in the active folder.

    EDL types:
      ip      — IP/CIDR list (one entry per line)
      domain  — Domain name list
      url     — URL prefix list
      imsi    — IMSI identifiers (mobile subscribers)
      imei    — IMEI identifiers (mobile equipment)

    Syntax:
      set external-dynamic-list <name> type ip     url <fetch-url>
      set external-dynamic-list <name> type domain url <fetch-url>
      set external-dynamic-list <name> type url    url <fetch-url>

    The <fetch-url> is where SCM fetches the list content.

    Optional:
      description <text>
      tag         <name>
      frequency   hourly|daily|weekly|monthly|5minute

    Examples:
      set external-dynamic-list Bad-IPs      type ip     url https://feeds.example.com/ips.txt
      set external-dynamic-list Block-Domains type domain url https://feeds.example.com/domains.txt
      set external-dynamic-list Phish-URLs   type url    url https://openphish.com/feed.txt
      set external-dynamic-list Threat-IPs   type ip     url https://feed.example.com/ips.txt  description "Threat feed"  tag Security  frequency daily

    pan.dev: POST /config/objects/v1/external-dynamic-lists
    """
    scm = require_scm(ctx)
    pos = args.get("_positional", [])
    name = pos[0] if pos else (args.get("name") or "")
    if not name:
        raise ValueError(
            "Usage: set external-dynamic-list <name> type ip|domain|url|imsi|imei url <fetch-url>\n"
            "  e.g. set external-dynamic-list Bad-IPs type ip url https://feed.example.com/ips.txt"
        )
    pos_lower = [p.lower() for p in pos]
    try:
        type_idx = pos_lower.index("type")
        edl_type = pos[type_idx + 1].lower() if type_idx + 1 < len(pos) else ""
    except ValueError:
        edl_type = ""
    _VALID = {"ip", "domain", "url", "imsi", "imei"}
    if edl_type not in _VALID:
        raise ValueError(
            f"Unknown EDL type: {edl_type!r}\n"
            f"  Valid types: {', '.join(sorted(_VALID))}\n"
            "  e.g. set external-dynamic-list Bad-IPs type ip url https://..."
        )
    url_idx = 0
    try:
        url_idx   = pos_lower.index("url")
        fetch_url = pos[url_idx + 1] if url_idx + 1 < len(pos) else ""
    except ValueError:
        fetch_url = ""
    if not fetch_url:
        raise ValueError(f"Missing 'url <fetch-url>' for EDL type '{edl_type}'")
    type_block: dict = {"url": fetch_url}
    # Frequency
    try:
        freq_idx  = pos_lower.index("frequency")
        freq = pos[freq_idx + 1].lower() if freq_idx + 1 < len(pos) else ""
        if freq in ("hourly", "daily", "weekly", "monthly", "5minute"):
            type_block["recurring"] = {freq: {}}
    except ValueError:
        pass
    payload: dict = {"name": name, "folder": ctx.folder, "type": {edl_type: type_block}}
    kv = parse_kv_tail(pos, url_idx + 2) if url_idx + 2 < len(pos) else {}
    if args.get("description") or kv.get("description"):
        payload["description"] = args.get("description") or kv["description"]
    tags = [t for t in [args.get("tag"), kv.get("tag")] if t]
    if tags:
        payload["tag"] = tags
    result = scm.create_external_dynamic_list(payload)
    return (
        f"[green]✓[/green] EDL [bold]{name}[/bold] (type: {edl_type}) created\n"
        f"  url: {fetch_url}  folder: {ctx.folder}  id: {result.get('id', '?')}"
    )


_WRITE_COMMANDS: dict[str, CommandDef] = {
    "set address": CommandDef(
        description="Create address — set address <name> ip-netmask|ip-range|ip-wildcard|fqdn <value>",
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
        description="Create address group — set address-group <name> static <m1> [m2] | dynamic filter '<expr>'",
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
        api_handler=delete_handler(
            "Address group", "get_address_groups", "delete_address_group",
            usage="Usage: delete address-group <name>",
        ),
        ssh_command=None,
        render="raw",
        feature_flag="delete_objects",
    ),
    "set service": CommandDef(
        description="Create service — set service <name> tcp|udp port <n> [source-port <n>]",
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
        api_handler=delete_handler(
            "Service", "get_services", "delete_service",
            usage="Usage: delete service <name>",
        ),
        ssh_command=None,
        render="raw",
        feature_flag="delete_objects",
    ),
    "set service-group": CommandDef(
        description="Create service group — set service-group <name> members <svc1> [svc2 ...]",
        category="objects",
        scope="folder",
        api_handler=_set_service_group,
        ssh_command=None,
        render="raw",
        feature_flag="create_service_group",
    ),
    "delete service-group": CommandDef(
        description="Delete a service group — delete service-group <name>",
        category="objects",
        scope="folder",
        api_handler=delete_handler(
            "Service group", "get_service_groups", "delete_service_group",
            usage="Usage: delete service-group <name>",
        ),
        ssh_command=None,
        render="raw",
        feature_flag="delete_objects",
    ),
    "set tag": CommandDef(
        description="Create tag — set tag <name> [color red|green|blue|...] [comments <text>]",
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
        api_handler=delete_handler(
            "Tag", "get_tags", "delete_tag",
            usage="Usage: delete tag <name>",
        ),
        ssh_command=None,
        render="raw",
        feature_flag="delete_objects",
    ),
    "set external-dynamic-list": CommandDef(
        description="Create EDL — set external-dynamic-list <name> type ip|domain|url url <fetch-url>",
        category="objects",
        scope="folder",
        api_handler=_set_external_dynamic_list,
        ssh_command=None,
        render="raw",
        feature_flag="create_edl",
    ),
    "delete external-dynamic-list": CommandDef(
        description="Delete an EDL — delete external-dynamic-list <name>",
        category="objects",
        scope="folder",
        api_handler=delete_handler(
            "EDL", "get_external_dynamic_lists", "delete_external_dynamic_list",
            usage="Usage: delete external-dynamic-list <name>",
        ),
        ssh_command=None,
        render="raw",
        feature_flag="delete_objects",
    ),
}

COMMANDS.update(_WRITE_COMMANDS)


# ---------------------------------------------------------------------------
# Update handlers — configure mode, GET→merge→PUT via SCM API
#
# Pattern for every update handler:
#   1. GET the current object by name (to get its ID and all current fields)
#   2. Apply only the fields the user specified (leaving others unchanged)
#   3. PUT the merged full object back
#
# This matches PAN-OS semantics: `set address HOST description "new"` only
# changes the description — the IP/type/tags remain as they were.
# ---------------------------------------------------------------------------



def _update_address(ctx: ExecutionContext, args: dict) -> Any:
    """Update an existing address object (GET→merge→PUT).

    Changes only the fields you specify — unspecified fields are unchanged.

    Syntax:
      update address <name> ip-netmask  <new-value>
      update address <name> ip-range    <new-value>
      update address <name> ip-wildcard <new-value>
      update address <name> fqdn        <new-value>
      update address <name> description <text>
      update address <name> tag         <name>

    Changing the address type replaces the old type field entirely.

    Examples:
      update address WebServer   ip-netmask  10.1.2.4/32
      update address DMZ-Subnet  description "Updated DMZ range"
      update address API-Host    fqdn        api2.example.com
      update address OldHost     tag         Decommissioned

    pan.dev: PUT /config/objects/v1/addresses/{id}
    """
    scm = require_scm(ctx)
    pos = args.get("_positional", [])
    name = pos[0] if pos else (args.get("name") or "")
    if not name:
        raise ValueError(
            "Usage: update address <name> <field> <value>\n"
            "  e.g. update address WebServer ip-netmask 10.1.2.4/32\n"
            "       update address WebServer description 'New description'"
        )
    # 1. GET current object
    items = scm.get_addresses(folder=ctx.folder)
    obj = scm._find_by_name(items, name)
    if not obj:
        raise ValueError(f"Address '{name}' not found in folder '{ctx.folder}'.  Run 'show address' to see available addresses.")
    obj_id = obj.pop("id")

    # 2. Apply address-type change if specified
    field_key = pos[1].lower() if len(pos) > 1 else ""
    if field_key in _ADDR_TYPE_MAP:
        new_val = pos[2] if len(pos) > 2 else ""
        if not new_val:
            raise ValueError(f"Missing value for address type '{field_key}'")
        # Clear all other address type fields first
        for f in _ADDR_TYPE_MAP.values():
            obj.pop(f, None)
        obj[_ADDR_TYPE_MAP[field_key]] = new_val
        merge_common_fields(obj, args, pos, 3)
    else:
        # Only description/tag change
        merge_common_fields(obj, args, pos, 1)

    # 3. PUT
    scm.update_address(obj_id, obj)
    changed = field_key or "description/tag"
    return f"[green]✓[/green] Address [bold]{name}[/bold] updated ({changed})"


def _update_address_group(ctx: ExecutionContext, args: dict) -> Any:
    """Update an existing address group (GET→merge→PUT).

    Syntax:
      update address-group <name> static  <member1> [member2 ...]
      update address-group <name> dynamic filter '<expression>'
      update address-group <name> description <text>
      update address-group <name> tag <name>

    Changing static→dynamic or vice versa replaces the group type entirely.

    Examples:
      update address-group WebTier  static  web1 web2 web3 web4
      update address-group ProdGroup dynamic filter 'Production and not Legacy'
      update address-group DBServers description "All database hosts"

    pan.dev: PUT /config/objects/v1/address-groups/{id}
    """
    scm = require_scm(ctx)
    pos = args.get("_positional", [])
    name = pos[0] if pos else (args.get("name") or "")
    if not name:
        raise ValueError("Usage: update address-group <name> static <m1>... | dynamic filter '<expr>'")
    items = scm.get_address_groups(folder=ctx.folder)
    obj = scm._find_by_name(items, name)
    if not obj:
        raise ValueError(f"Address group '{name}' not found in folder '{ctx.folder}'.")
    obj_id = obj.pop("id")

    mode = pos[1].lower() if len(pos) > 1 else ""
    if mode == "static":
        _KW = {"description", "tag"}
        members, kv_start = [], len(pos)
        for i, tok in enumerate(pos[2:], 2):
            if tok.lower() in _KW:
                kv_start = i; break
            members.append(tok)
        if not members:
            raise ValueError("Need at least one member: update address-group <name> static <member>")
        obj.pop("dynamic", None)
        obj["static"] = members
        merge_common_fields(obj, args, pos, kv_start)
    elif mode == "dynamic":
        if len(pos) < 3 or pos[2].lower() != "filter":
            raise ValueError("Usage: update address-group <name> dynamic filter '<expression>'")
        expr = pos[3] if len(pos) > 3 else ""
        if not expr:
            raise ValueError("Missing filter expression")
        obj.pop("static", None)
        obj["dynamic"] = {"filter": expr}
        merge_common_fields(obj, args, pos, 4)
    else:
        merge_common_fields(obj, args, pos, 1)

    scm.update_address_group(obj_id, obj)
    return f"[green]✓[/green] Address group [bold]{name}[/bold] updated"


def _update_service(ctx: ExecutionContext, args: dict) -> Any:
    """Update an existing service object (GET→merge→PUT).

    Syntax:
      update service <name> tcp port <n>  [source-port <n>]
      update service <name> udp port <n>  [source-port <n>]
      update service <name> description <text>
      update service <name> tag <name>

    Examples:
      update service HTTP    tcp port 8080
      update service HTTPS   tcp port 443  source-port 1024-65535
      update service DNS     description "DNS resolver service"

    pan.dev: PUT /config/objects/v1/services/{id}
    """
    scm = require_scm(ctx)
    pos = args.get("_positional", [])
    name = pos[0] if pos else (args.get("name") or "")
    if not name:
        raise ValueError("Usage: update service <name> tcp|udp port <n>")
    items = scm.get_services(folder=ctx.folder)
    obj = scm._find_by_name(items, name)
    if not obj:
        raise ValueError(f"Service '{name}' not found in folder '{ctx.folder}'.")
    obj_id = obj.pop("id")

    proto = pos[1].lower() if len(pos) > 1 else ""
    pos_lower = [p.lower() for p in pos]
    if proto in ("tcp", "udp"):
        try:
            port_idx = pos_lower.index("port")
            dst_port = pos[port_idx + 1] if port_idx + 1 < len(pos) else ""
        except ValueError:
            dst_port = ""
        if not dst_port:
            raise ValueError(f"Missing port value: update service {name} {proto} port <n>")
        proto_block: dict = {"port": dst_port}
        try:
            sp_idx = pos_lower.index("source-port")
            src = pos[sp_idx + 1] if sp_idx + 1 < len(pos) else ""
            if src:
                proto_block["source_port"] = src
        except ValueError:
            pass
        obj["protocol"] = {proto: proto_block}
    merge_common_fields(obj, args, pos, 1 if proto not in ("tcp", "udp") else 4)

    scm.update_service(obj_id, obj)
    return f"[green]✓[/green] Service [bold]{name}[/bold] updated"


def _update_service_group(ctx: ExecutionContext, args: dict) -> Any:
    """Update a service group's member list.

    Syntax:
      update service-group <name> members <svc1> [svc2 ...]
      update service-group <name> description <text>

    Examples:
      update service-group Web-Services  members HTTP HTTPS HTTP-ALT
      update service-group DB-Ports      description "Database access ports"

    pan.dev: PUT /config/objects/v1/service-groups/{id}
    """
    scm = require_scm(ctx)
    pos = args.get("_positional", [])
    name = pos[0] if pos else (args.get("name") or "")
    if not name:
        raise ValueError("Usage: update service-group <name> members <svc1> [svc2...]")
    items = scm.get_service_groups(folder=ctx.folder)
    obj = scm._find_by_name(items, name)
    if not obj:
        raise ValueError(f"Service group '{name}' not found in folder '{ctx.folder}'.")
    obj_id = obj.pop("id")

    pos_lower = [p.lower() for p in pos]
    if "members" in pos_lower:
        mem_idx = pos_lower.index("members")
        _KW = {"tag", "description"}
        members, kv_start = [], len(pos)
        for i, tok in enumerate(pos[mem_idx + 1:], mem_idx + 1):
            if tok.lower() in _KW:
                kv_start = i; break
            members.append(tok)
        if members:
            obj["members"] = members
        merge_common_fields(obj, args, pos, kv_start)
    else:
        merge_common_fields(obj, args, pos, 1)

    scm.update_service_group(obj_id, obj)
    return f"[green]✓[/green] Service group [bold]{name}[/bold] updated"


def _update_tag(ctx: ExecutionContext, args: dict) -> Any:
    """Update an existing tag (color, comments).

    Syntax:
      update tag <name> color <color>
      update tag <name> comments <text>
      update tag <name> color <color> comments <text>

    Examples:
      update tag Production  color  green
      update tag Staging     color  yellow  comments "Pre-production environment"
      update tag Critical    comments "High priority — review before change"

    pan.dev: PUT /config/objects/v1/tags/{id}
    """
    scm = require_scm(ctx)
    pos = args.get("_positional", [])
    name = pos[0] if pos else (args.get("name") or "")
    if not name:
        raise ValueError("Usage: update tag <name> color <color> [comments <text>]")
    items = scm.get_tags(folder=ctx.folder)
    obj = scm._find_by_name(items, name)
    if not obj:
        raise ValueError(f"Tag '{name}' not found in folder '{ctx.folder}'.")
    obj_id = obj.pop("id")

    kv = parse_kv_tail(pos, 1)
    color = args.get("color") or kv.get("color") or ""
    if color:
        norm = color.lower()
        if norm not in _TAG_COLORS:
            raise ValueError(f"Unknown color: {color!r}. Valid: {', '.join(sorted(_TAG_COLORS))}")
        obj["color"] = norm
    comments = args.get("comments") or kv.get("comments") or ""
    if comments:
        obj["comments"] = comments

    scm.update_tag(obj_id, obj)
    return f"[green]✓[/green] Tag [bold]{name}[/bold] updated"


def _update_external_dynamic_list(ctx: ExecutionContext, args: dict) -> Any:
    """Update an existing EDL (URL, description, or frequency).

    Syntax:
      update external-dynamic-list <name> url <new-fetch-url>
      update external-dynamic-list <name> description <text>
      update external-dynamic-list <name> frequency hourly|daily|weekly|monthly|5minute
      update external-dynamic-list <name> url <url> frequency <freq>

    Examples:
      update external-dynamic-list Threat-IPs  url https://new-feed.example.com/ips.txt
      update external-dynamic-list Bad-Domains frequency daily
      update external-dynamic-list Phish-URLs  description "Updated phishing feed"

    pan.dev: PUT /config/objects/v1/external-dynamic-lists/{id}
    """
    scm = require_scm(ctx)
    pos = args.get("_positional", [])
    name = pos[0] if pos else (args.get("name") or "")
    if not name:
        raise ValueError("Usage: update external-dynamic-list <name> url <url> | description <text> | frequency <freq>")
    items = scm.get_external_dynamic_lists(folder=ctx.folder)
    obj = scm._find_by_name(items, name)
    if not obj:
        raise ValueError(f"EDL '{name}' not found in folder '{ctx.folder}'.")
    obj_id = obj.pop("id")

    pos_lower = [p.lower() for p in pos]
    # Update fetch URL
    try:
        url_idx = pos_lower.index("url")
        new_url = pos[url_idx + 1] if url_idx + 1 < len(pos) else ""
        if new_url:
            # Navigate into the nested type block and update the url
            for type_key in ("ip", "domain", "url", "imsi", "imei"):
                if type_key in obj.get("type", {}):
                    obj["type"][type_key]["url"] = new_url
                    break
    except ValueError:
        pass
    # Update frequency
    try:
        freq_idx = pos_lower.index("frequency")
        freq = pos[freq_idx + 1].lower() if freq_idx + 1 < len(pos) else ""
        if freq in ("hourly", "daily", "weekly", "monthly", "5minute"):
            for type_key in ("ip", "domain", "url", "imsi", "imei"):
                if type_key in obj.get("type", {}):
                    obj["type"][type_key]["recurring"] = {freq: {}}
                    break
    except ValueError:
        pass
    kv = parse_kv_tail(pos, 1)
    if args.get("description") or kv.get("description"):
        obj["description"] = args.get("description") or kv["description"]

    scm.update_external_dynamic_list(obj_id, obj)
    return f"[green]✓[/green] EDL [bold]{name}[/bold] updated"


_UPDATE_COMMANDS: dict[str, CommandDef] = {
    "update address": CommandDef(
        description="Update address — update address <name> ip-netmask|fqdn|ip-range|ip-wildcard|description|tag <value>",
        category="objects",
        scope="folder",
        api_handler=_update_address,
        ssh_command=None,
        render="raw",
        feature_flag="update_objects",
    ),
    "update address-group": CommandDef(
        description="Update address group — update address-group <name> static <m1>... | dynamic filter '<expr>'",
        category="objects",
        scope="folder",
        api_handler=_update_address_group,
        ssh_command=None,
        render="raw",
        feature_flag="update_objects",
    ),
    "update service": CommandDef(
        description="Update service — update service <name> tcp|udp port <n> [source-port <n>]",
        category="objects",
        scope="folder",
        api_handler=_update_service,
        ssh_command=None,
        render="raw",
        feature_flag="update_objects",
    ),
    "update service-group": CommandDef(
        description="Update service group members — update service-group <name> members <svc1> [svc2...]",
        category="objects",
        scope="folder",
        api_handler=_update_service_group,
        ssh_command=None,
        render="raw",
        feature_flag="update_objects",
    ),
    "update tag": CommandDef(
        description="Update tag color/comments — update tag <name> color <color> [comments <text>]",
        category="objects",
        scope="folder",
        api_handler=_update_tag,
        ssh_command=None,
        render="raw",
        feature_flag="update_objects",
    ),
    "update external-dynamic-list": CommandDef(
        description="Update EDL url/frequency — update external-dynamic-list <name> url <url>",
        category="objects",
        scope="folder",
        api_handler=_update_external_dynamic_list,
        ssh_command=None,
        render="raw",
        feature_flag="update_objects",
    ),
}

COMMANDS.update(_UPDATE_COMMANDS)

