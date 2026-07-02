"""Network commands (interfaces, zones, routing, HA, NAT, VPN, SD-WAN).

SCM-backed (configuration): interfaces, zones, routing, HA, NAT rules, PBF,
IKE gateways, IPsec tunnels, BGP profiles, DNS proxy, QoS, SD-WAN.

Live device only (SSH / --remote): ARP table, session table, VPN tunnel state,
BGP peer state, routing tables.

See docs/commands/ and docs/scm-api/specs/ngfw-network.md for full API reference.
PAN-OS CLI hierarchy: https://docs.paloaltonetworks.com/ngfw/pan-os-cli-quick-start/cli-command-hierarchy/pan-os-11-2-cli-ops-command-hierarchy
"""

from __future__ import annotations

from typing import Any

from app.commands.base import (
    CommandDef,
    ExecutionContext,
    require_device,
    require_scm,
    show_handler,
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
    host = args.get("host", "8.8.8.8")
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
    src   = args.get("source", "")
    dst   = args.get("destination", "")
    dport = args.get("destination-port", "")
    proto = args.get("protocol", "6")
    cmd   = f"test nat-policy-match source {src} destination {dst} protocol {proto}"
    if dport:
        cmd += f" destination-port {dport}"
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
    url = args.get("_positional", ["http://example.com"])[0] if args.get("_positional") else "http://example.com"
    return f"test url {url}"


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

