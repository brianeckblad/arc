"""Network commands (interfaces, zones, routing, HA, NAT, VPN, SD-WAN).

SCM-backed (configuration): interfaces, zones, routing, HA, NAT rules, PBF,
IKE gateways, IPsec tunnels, BGP profiles, DNS proxy, QoS, SD-WAN.

Live device only (SSH / --remote): ARP table, session table, VPN tunnel state,
BGP peer state, routing tables.

See docs/commands/ and docs/scm-api/specs/ngfw-network.md for full API reference.
PAN-OS CLI hierarchy: https://docs.paloaltonetworks.com/ngfw/pan-os-cli-quick-start/cli-command-hierarchy/pan-os-11-2-cli-ops-command-hierarchy
"""

from __future__ import annotations

import shlex
from typing import Any

from app.commands.base import (
    CommandDef,
    ExecutionContext,
    delete_handler,
    require_device,
    require_scm,
    show_handler,
)
from app.commands.objects import _check_concurrent_modification


# ---------------------------------------------------------------------------
# NAT rule update handler
# ---------------------------------------------------------------------------

def _update_nat_rule(ctx: ExecutionContext, args: dict) -> Any:
    """Update an existing NAT rule (GET→merge→PUT).

    Modifies one or more fields of a named NAT rule while preserving all other fields.

    Syntax:
      update nat-rule <name> from <zone> [<zone2> ...]
      update nat-rule <name> to <zone>
      update nat-rule <name> source <addr> [<addr2> ...]
      update nat-rule <name> destination <addr>
      update nat-rule <name> service <svc>
      update nat-rule <name> description <text>
      update nat-rule <name> disabled true|false

    Examples:
      update nat-rule Outbound-PAT source 192.168.1.0/24
      update nat-rule Outbound-PAT description "Updated for new subnet"
      update nat-rule Outbound-PAT disabled false

    pan.dev: PUT /config/network/v1/nat-rules/{id}
    """
    scm = require_scm(ctx)
    pos = args.get("_positional", [])
    name = pos[0] if pos else (args.get("name") or "")
    if not name or len(pos) < 2:
        raise ValueError(
            "Usage: update nat-rule <name> <field> <value>\n"
            "  Fields: from | to | source | destination | service | description | disabled\n"
            "  e.g. update nat-rule Outbound-PAT source 192.168.1.0/24\n"
            "       update nat-rule Outbound-PAT description 'Updated rule'"
        )

    # 1. GET current rule
    items = scm.get_nat_rules(folder=ctx.folder)
    obj = scm.find_by_name(items, name)
    if not obj:
        raise ValueError(
            f"NAT rule '{name}' not found in folder '{ctx.folder}'.\n"
            "  Run [bold]show nat-rules[/bold] to see available rules."
        )
    obj = dict(obj)  # shallow copy — prevent mutation of cached response on retry
    rule_id = obj.pop("id")

    # 2. Apply the requested field change
    field = pos[1].lower()
    values = pos[2:]

    # NAT rule list fields (can have multiple values)
    _LIST_FIELDS = {"from", "source", "tag"}
    # NAT rule single-value zone/address fields
    _SINGLE_FIELDS = {"to", "destination", "service"}

    if field in _LIST_FIELDS:
        if not values:
            raise ValueError(f"Provide at least one value for '{field}'")
        obj[field] = list(values)

    elif field in _SINGLE_FIELDS:
        val = values[0] if values else ""
        if not val:
            raise ValueError(f"Provide a value for '{field}'")
        # NAT 'to' and 'destination' are stored as single strings in SCM NAT rules,
        # not as lists (unlike security rules which use zone lists).
        obj[field] = val

    elif field == "description":
        obj["description"] = " ".join(values)

    elif field == "disabled":
        flag = (values[0].lower() if values else "true")
        if flag not in ("true", "false", "yes", "no", "1", "0"):
            raise ValueError(f"'disabled' expects true or false, got: {flag!r}")
        obj["disabled"] = flag in ("true", "yes", "1")

    else:
        raise ValueError(
            f"Unknown field: {field!r}\n"
            "  Valid fields: from | to | source | destination | service | description | disabled"
        )

    # 3. PUT — re-fetch to detect concurrent modifications before overwriting.
    fresh_items = scm.get_nat_rules(folder=ctx.folder)
    _check_concurrent_modification(obj, scm.find_by_name(fresh_items, name), name)
    scm.update_nat_rule(rule_id, obj)
    return (
        f"[green]✓[/green] NAT rule [bold]{name}[/bold] updated "
        f"([bold]{field}[/bold] = {' '.join(str(v) for v in values) or '(cleared)'})"
    )


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
    return f"show interface {shlex.quote(name)}" if name else "show interface all"


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
        feature_flag="show_interface",
    ),
    "show interface": CommandDef(
        description="Show a specific interface — show interface <name>",
        category="network",
        scope="folder",
        api_handler=_show_interface,
        ssh_command=_ssh_interface,
        render="interfaces",
        feature_flag="show_interface",
    ),
    "show routing route": CommandDef(
        description="Show static routes in the active folder",
        category="network",
        scope="folder",
        api_handler=show_handler("get_static_routes"),
        ssh_command="show routing route",
        render="routes",
        feature_flag="show_routing",
    ),
    "show routing summary": CommandDef(
        description="Show virtual routers / routing profiles in the active folder",
        category="network",
        scope="folder",
        api_handler=show_handler("get_routing_profiles"),
        ssh_command="show routing summary",
        render="dict",
        feature_flag="show_routing",
    ),
    "show zone": CommandDef(
        description="Show security zones in the active folder",
        category="network",
        scope="folder",
        api_handler=show_handler("get_zones"),
        ssh_command="show zone",
        render="zones",
        feature_flag="show_zone",
    ),
    "show high-availability all": CommandDef(
        description="Show full HA configuration from the active folder",
        category="network",
        scope="folder",
        api_handler=show_handler("get_ha_config"),
        ssh_command="show high-availability all",
        render="ha",
        feature_flag="show_high_availability",
    ),
    "show high-availability state": CommandDef(
        description="Show HA state summary from the active folder",
        category="network",
        scope="folder",
        api_handler=_show_ha_state,
        ssh_command="show high-availability state",
        render="ha",
        feature_flag="show_high_availability",
    ),
}


# ---------------------------------------------------------------------------
# Handlers — live device state (SSH / --remote only)
# ---------------------------------------------------------------------------

def _show_arp(ctx: ExecutionContext, args: dict) -> Any:
    """Live ARP table from device — use --remote.  Not stored in SCM."""
    device = require_device(ctx)
    name = device.get("hostname") or device.get("name") or "device"
    return f"ARP table is live device state.  Run:  show arp all --remote  to query {name}."


def _show_sessions(ctx: ExecutionContext, args: dict) -> Any:
    """Live session table from device — use --remote.  Not stored in SCM."""
    device = require_device(ctx)
    name = device.get("hostname") or device.get("name") or "device"
    return f"Session table is live device state.  Run:  show session all --remote  to query {name}."


def _show_vpn_tunnel(ctx: ExecutionContext, args: dict) -> Any:
    """Live VPN tunnel state — use --remote.  Tunnel config is in SCM; live state is on device."""
    device = require_device(ctx)
    name = device.get("hostname") or device.get("name") or "device"
    return f"VPN tunnel state is live.  Run:  show vpn tunnel --remote  to query {name}.  " \
           f"For VPN config, use:  show ipsec-tunnel  (SCM-backed)."


def _show_vpn_ike_sa(ctx: ExecutionContext, args: dict) -> Any:
    """Live IKE security association state — use --remote."""
    device = require_device(ctx)
    name = device.get("hostname") or device.get("name") or "device"
    return f"IKE SA is live device state.  Run:  show vpn ike-sa --remote  to query {name}.  " \
           f"For IKE config, use:  show ike-gateway  (SCM-backed)."


def _show_routing_bgp(ctx: ExecutionContext, args: dict) -> Any:
    """Live BGP routing state — use --remote.  BGP profiles (config) are in SCM."""
    device = require_device(ctx)
    name = device.get("hostname") or device.get("name") or "device"
    return f"Live BGP state requires a device.  Run:  show routing protocol bgp summary --remote  on {name}.  " \
           f"For BGP profile config, use:  show bgp-profile  (SCM-backed)."


def _show_traceroute(ctx: ExecutionContext, args: dict) -> Any:
    """Traceroute from device — use --remote."""
    host = args.get("host", "")
    device = require_device(ctx)
    name = device.get("hostname") or device.get("name") or "device"
    if not host:
        return f"Usage: traceroute host <ip>  (must use --remote on {name})"
    return f"Traceroute to {host} requires live device.  Run:  traceroute host {host} --remote  on {name}."


def _ssh_traceroute(args: dict) -> str:
    host = shlex.quote(args.get("host", "8.8.8.8"))
    return f"traceroute host {host}"


def _test_nat_policy_match(ctx: ExecutionContext, args: dict) -> Any:
    """Test NAT policy match — use --remote.  PAN-OS: test nat-policy-match"""
    src = args.get("source", "")
    dst = args.get("destination", "")
    device = require_device(ctx)
    name = device.get("hostname") or device.get("name") or "device"
    if not src or not dst:
        return "Usage: test nat-policy-match source <ip> destination <ip>  (use --remote)"
    return f"NAT policy match test requires live device.  Run with --remote on {name}."


def _ssh_test_nat(args: dict) -> str:
    src   = shlex.quote(args.get("source", ""))
    dst   = shlex.quote(args.get("destination", ""))
    raw_dport = args.get("destination-port", "")
    proto = shlex.quote(args.get("protocol", "6"))
    cmd   = f"test nat-policy-match source {src} destination {dst} protocol {proto}"
    if raw_dport:
        cmd += f" destination-port {shlex.quote(raw_dport)}"
    return cmd


def _test_url(ctx: ExecutionContext, args: dict) -> Any:
    """Test URL categorization — use --remote.  PAN-OS: test url <url>"""
    device = require_device(ctx)
    name   = device.get("hostname") or device.get("name") or "device"
    url    = args.get("_positional", [""])[0] if args.get("_positional") else ""
    if not url:
        return "Usage: test url <url>  (use --remote)"
    return f"URL test requires live device.  Run:  test url {url} --remote  on {name}."


def _ssh_test_url(args: dict) -> str:
    raw_url = args.get("_positional", ["https://example.com"])[0] if args.get("_positional") else "https://example.com"
    return f"test url {shlex.quote(raw_url)}"


# ---------------------------------------------------------------------------
# Extended COMMANDS — unimplemented commands added here
# ---------------------------------------------------------------------------

_EXTRA_COMMANDS: dict[str, CommandDef] = {
    "show nat-rules": CommandDef(
        description="Show NAT rules in the active folder",
        category="network",
        scope="folder",
        api_handler=show_handler("get_nat_rules"),
        ssh_command="show running nat-policy",
        render="list",
        feature_flag="nat_rules",
    ),
    "update nat-rule": CommandDef(
        description="Update a NAT rule — update nat-rule <name> <field> <value>",
        category="network",
        scope="folder",
        api_handler=_update_nat_rule,
        ssh_command=None,
        render="raw",
        feature_flag="nat_rules",
        usage="update nat-rule <name> from|to|source|destination|service|description|disabled <value>",
    ),
    "delete nat-rule": CommandDef(
        description="Delete a NAT rule — delete nat-rule <name>",
        category="network",
        scope="folder",
        api_handler=delete_handler(
            "NAT rule", "get_nat_rules", "delete_nat_rule",
            usage="Usage: delete nat-rule <name>",
        ),
        ssh_command=None,
        render="raw",
        feature_flag="nat_rules",
        usage="delete nat-rule <name>",
    ),
    "show pbf-rules": CommandDef(
        description="Show policy-based forwarding rules in the active folder",
        category="network",
        scope="folder",
        api_handler=show_handler("get_pbf_rules"),
        ssh_command="show pbf rule all",
        render="list",
        feature_flag="pbf_rules",
    ),
    "show ike-gateway": CommandDef(
        description="Show IKE gateway configurations (VPN) in the active folder",
        category="network",
        scope="folder",
        api_handler=show_handler("get_ike_gateways"),
        ssh_command="show vpn ike-sa gateway all",
        render="list",
        feature_flag="ipsec_vpn",
    ),
    "show ipsec-tunnel": CommandDef(
        description="Show IPsec tunnel configurations in the active folder",
        category="network",
        scope="folder",
        api_handler=show_handler("get_ipsec_tunnels"),
        ssh_command="show vpn ipsec-sa",
        render="list",
        feature_flag="ipsec_vpn",
    ),
    "show bgp-profile": CommandDef(
        description="Show BGP routing profiles (configuration) in the active folder",
        category="network",
        scope="folder",
        api_handler=show_handler("get_bgp_routing_profiles"),
        ssh_command="show routing protocol bgp summary",
        render="list",
        feature_flag="bgp_routing",
    ),
    "show dns-proxy": CommandDef(
        description="Show DNS proxy configurations in the active folder",
        category="network",
        scope="folder",
        api_handler=show_handler("get_dns_proxies"),
        ssh_command="show dns-proxy dns-signature statistics",
        render="list",
        feature_flag="dns_proxy",
    ),
    "show qos-profile": CommandDef(
        description="Show QoS profiles in the active folder",
        category="network",
        scope="folder",
        api_handler=show_handler("get_qos_profiles"),
        ssh_command=None,
        render="list",
        feature_flag="qos",
    ),
    "show sdwan-rules": CommandDef(
        description="Show SD-WAN rules in the active folder",
        category="network",
        scope="folder",
        api_handler=show_handler("get_sdwan_rules"),
        ssh_command="show sdwan traffic",
        render="list",
        feature_flag="sdwan",
    ),
    # ── Live device only (SSH / --remote) ────────────────────────────────────
    "show arp": CommandDef(
        description="Show live ARP table from device — use --remote",
        category="network",
        scope="device",
        api_handler=_show_arp,
        ssh_command="show arp all",
        render="raw",
        feature_flag="show_arp",
    ),
    "show session all": CommandDef(
        description="Show live session table from device — use --remote",
        category="network",
        scope="device",
        api_handler=_show_sessions,
        ssh_command="show session all",
        render="raw",
        feature_flag="show_sessions",
    ),
    "show vpn tunnel": CommandDef(
        description="Show live VPN tunnel state from device — use --remote",
        category="network",
        scope="device",
        api_handler=_show_vpn_tunnel,
        ssh_command="show vpn tunnel",
        render="raw",
        feature_flag="ipsec_vpn",
    ),
    "show vpn ike-sa": CommandDef(
        description="Show live IKE security associations from device — use --remote",
        category="network",
        scope="device",
        api_handler=_show_vpn_ike_sa,
        ssh_command="show vpn ike-sa",
        render="raw",
        feature_flag="ipsec_vpn",
    ),
    "show routing bgp": CommandDef(
        description="Show live BGP routing state from device — use --remote",
        category="network",
        scope="device",
        api_handler=_show_routing_bgp,
        ssh_command="show routing protocol bgp peer",
        render="raw",
        feature_flag="bgp_routing",
    ),
    "traceroute host": CommandDef(
        description="Traceroute from device — traceroute host <ip>  (use --remote)",
        category="network",
        scope="device",
        api_handler=_show_traceroute,
        ssh_command=_ssh_traceroute,
        render="raw",
        feature_flag="traceroute",
    ),
    "test nat-policy-match": CommandDef(
        description="Test NAT policy match — source <ip> destination <ip>  (use --remote)",
        category="network",
        scope="device",
        api_handler=_test_nat_policy_match,
        ssh_command=_ssh_test_nat,
        render="raw",
        feature_flag="test_nat",
    ),
    "test url": CommandDef(
        description="Test URL categorization — test url <url>  (use --remote)",
        category="network",
        scope="device",
        api_handler=_test_url,
        ssh_command=_ssh_test_url,
        render="raw",
        feature_flag="test_url",
    ),
}

COMMANDS.update(_EXTRA_COMMANDS)

