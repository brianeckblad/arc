"""Output formatter — renders API/SSH data as rich tables and panels."""

from __future__ import annotations

from typing import Any

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich import box


console = Console()


# ---------------------------------------------------------------------------
# Generic helpers
# ---------------------------------------------------------------------------

def _kv_table(data: dict, title: str = "") -> Table:
    t = Table(box=box.ROUNDED, show_header=False, title=title, min_width=50)
    t.add_column("Key", style="bold cyan", no_wrap=True)
    t.add_column("Value", style="white")
    for k, v in data.items():
        t.add_row(str(k).replace("-", " ").title(), str(v) if v is not None else "")
    return t


def _list_table(rows: list[dict], title: str = "") -> Table:
    if not rows:
        return Table(title=title, box=box.ROUNDED)
    t = Table(box=box.ROUNDED, title=title, show_header=True, header_style="bold cyan")
    cols = list(rows[0].keys())
    for c in cols:
        t.add_column(c.replace("-", " ").title(), overflow="fold")
    for row in rows:
        t.add_row(*[str(row.get(c) or "") for c in cols])
    return t


# ---------------------------------------------------------------------------
# Command-specific renderers
# ---------------------------------------------------------------------------

def format_system_info(data: dict) -> Table:
    # Trim uninteresting keys
    interesting = [
        "hostname", "ip-address", "public-ip-address", "serial",
        "model", "family", "sw-version", "app-version", "av-version",
        "threat-version", "wildfire-version", "uptime",
        "multi-vsys", "operational-mode",
    ]
    cleaned = {k: v for k, v in data.items() if v and k in interesting}
    if not cleaned:
        cleaned = {k: v for k, v in data.items() if v}
    return _kv_table(cleaned, title="System Info")


def format_devices(devices: list[dict]) -> Table:
    """Render the SCM device list.

    Field names sourced from GET /config/setup/v1/devices (api.strata.paloaltonetworks.com).
    Key fields: is_connected (bool), software_version, serial_number, ip_address,
                ha_state, uptime, model, folder.
    """
    t = Table(box=box.ROUNDED, title=f"Managed Devices ({len(devices)})", header_style="bold cyan")
    t.add_column("",          width=2, no_wrap=True)   # connected indicator
    t.add_column("Hostname",  style="bold", no_wrap=True)
    t.add_column("Serial",    no_wrap=True)
    t.add_column("Model",     no_wrap=True)
    t.add_column("SW Version",no_wrap=True)
    t.add_column("IP Address",no_wrap=True)
    t.add_column("HA",        no_wrap=True)
    t.add_column("Uptime",    no_wrap=True)
    t.add_column("Folder",    style="dim", no_wrap=True)

    for d in devices:
        is_connected = d.get("is_connected")
        if is_connected is True:
            indicator = "[green]●[/green]"
        elif is_connected is False:
            indicator = "[red]●[/red]"
        else:
            # Field absent — derive from connected_since / last_disconnect_time
            has_connected_since  = bool(d.get("connected_since"))
            has_last_disconnect  = bool(d.get("last_disconnect_time"))
            if has_connected_since and not has_last_disconnect:
                indicator = "[green]●[/green]"
            else:
                indicator = "[dim]●[/dim]"

        hostname = d.get("hostname") or d.get("display_name") or d.get("name") or ""
        # Serial: API returns it as both 'serial_number' and 'name' (name == serial)
        serial   = d.get("serial_number") or d.get("serial") or d.get("name") or ""
        model    = d.get("model") or ""
        sw_ver   = d.get("software_version") or d.get("sw_version") or d.get("installed_software_version") or ""
        ip       = d.get("ip_address") or d.get("ip-address") or ""
        if ip == "unknown":
            ip = ""

        ha_state = d.get("ha_state") or ""
        if ha_state in ("unknown", ""):
            ha_state = ""

        uptime = d.get("uptime") or ""
        # Shorten "118 days, 17:37:33" → "118d 17:37"
        if uptime and "days," in uptime:
            parts = uptime.split(",")
            day_part = parts[0].strip()   # "118 days"
            time_part = parts[1].strip() if len(parts) > 1 else ""
            # drop seconds from time_part
            time_parts = time_part.split(":")
            time_short = ":".join(time_parts[:2]) if len(time_parts) >= 2 else time_part
            day_num = day_part.split()[0]
            uptime = f"{day_num}d {time_short}"

        folder = d.get("folder") or ""

        t.add_row(indicator, hostname, serial, model, sw_ver, ip, ha_state, uptime, folder)

    return t


def format_interfaces(interfaces: list[dict]) -> Table:
    t = Table(box=box.ROUNDED, title="Interfaces", header_style="bold cyan")
    t.add_column("Name", style="bold")
    t.add_column("State")
    t.add_column("IP Address")
    t.add_column("Speed")
    t.add_column("Zone")
    for iface in interfaces:
        state = iface.get("state", "")
        state_str = f"[green]{state}[/green]" if state == "up" else f"[red]{state}[/red]" if state else ""
        t.add_row(
            iface.get("name", ""),
            state_str,
            iface.get("ip") or iface.get("ip-address") or "",
            iface.get("speed", ""),
            iface.get("zone", ""),
        )
    return t


def format_routes(routes: list[dict]) -> Table:
    t = Table(box=box.ROUNDED, title="Routing Table", header_style="bold cyan")
    for col in ["Destination", "Next Hop", "Interface", "Metric", "Flags", "Age"]:
        t.add_column(col, overflow="fold")
    for r in routes:
        t.add_row(
            r.get("destination", ""),
            r.get("nexthop", ""),
            r.get("interface", ""),
            r.get("metric", ""),
            r.get("flags", ""),
            r.get("age", ""),
        )
    return t


def format_security_policy(rules: list[dict]) -> Table:
    t = Table(box=box.ROUNDED, title="Security Policy", header_style="bold cyan")
    t.add_column("Name", style="bold")
    t.add_column("From Zone")
    t.add_column("To Zone")
    t.add_column("Source")
    t.add_column("Dest")
    t.add_column("Application")
    t.add_column("Action")
    for r in rules:
        action = r.get("action", "")
        action_str = f"[green]{action}[/green]" if action == "allow" else f"[red]{action}[/red]"
        t.add_row(
            r.get("name", ""),
            ", ".join(r.get("from", [])),
            ", ".join(r.get("to", [])),
            ", ".join(r.get("source", [])),
            ", ".join(r.get("destination", [])),
            ", ".join(r.get("application", [])),
            action_str,
        )
    return t


def format_jobs(jobs: list[dict]) -> Table:
    t = Table(box=box.ROUNDED, title="Jobs", header_style="bold cyan")
    for col in ["ID", "Type", "Status", "Result", "Progress", "User", "Details"]:
        t.add_column(col)
    for j in jobs:
        status = j.get("status", "")
        result = j.get("result", "")
        status_str = f"[green]{status}[/green]" if status == "FIN" else f"[yellow]{status}[/yellow]"
        result_str = f"[green]{result}[/green]" if result == "OK" else f"[red]{result}[/red]" if result else ""
        t.add_row(
            j.get("id", ""),
            j.get("type", ""),
            status_str,
            result_str,
            j.get("progress", ""),
            j.get("user", ""),
            j.get("details", ""),
        )
    return t


def format_logs(logs: list[dict], log_type: str = "system") -> Table:
    t = Table(box=box.ROUNDED, title=f"Log ({log_type})", header_style="bold cyan")
    priority_cols = ["time", "receive_time", "eventid", "severity", "subtype", "type",
                     "description", "object", "module", "src", "dst"]
    if not logs:
        return t
    all_cols = list(logs[0].keys())
    shown = [c for c in priority_cols if c in all_cols]
    remaining = [c for c in all_cols if c not in shown]
    cols = shown + remaining[:3]  # cap at reasonable width
    for c in cols:
        t.add_column(c.replace("_", " ").title(), overflow="fold", no_wrap=(c == "time"))
    for row in logs:
        t.add_row(*[str(row.get(c) or "") for c in cols])
    return t


def format_address_objects(addresses: list[dict]) -> Table:
    t = Table(box=box.ROUNDED, title="Address Objects", header_style="bold cyan")
    t.add_column("Name", style="bold")
    t.add_column("IP / FQDN")
    t.add_column("Description")
    for a in addresses:
        value = a.get("ip-netmask") or a.get("ip_netmask") or a.get("ip-range") or a.get("fqdn") or ""
        t.add_row(a.get("name", ""), value, a.get("description", ""))
    return t


def format_address_groups(groups: list[dict]) -> Table:
    t = Table(box=box.ROUNDED, title="Address Groups", header_style="bold cyan")
    t.add_column("Name", style="bold")
    t.add_column("Members")
    t.add_column("Dynamic Filter")
    t.add_column("Description")
    for g in groups:
        members = g.get("members", [])
        if isinstance(members, list):
            members_str = ", ".join(members)
        else:
            members_str = str(members)
        t.add_row(
            g.get("name", ""),
            members_str,
            g.get("dynamic") or g.get("filter") or "",
            g.get("description", ""),
        )
    return t


def format_services(services: list[dict]) -> Table:
    t = Table(box=box.ROUNDED, title="Services", header_style="bold cyan")
    t.add_column("Name", style="bold")
    t.add_column("Protocol")
    t.add_column("Port")
    t.add_column("Description")
    for s in services:
        proto = s.get("protocol", "")
        if isinstance(proto, dict):
            proto = list(proto.keys())[0] if proto else ""
        port = s.get("port", "")
        if not port and isinstance(s.get("protocol"), dict):
            for _p, _v in (s["protocol"].items()):
                if isinstance(_v, dict):
                    port = _v.get("port", "")
        t.add_row(s.get("name", ""), str(proto), str(port), s.get("description", ""))
    return t


def format_zones(zones: list[dict]) -> Table:
    t = Table(box=box.ROUNDED, title="Zones", header_style="bold cyan")
    t.add_column("Name", style="bold")
    t.add_column("Type")
    t.add_column("Interfaces")
    for z in zones:
        ifaces = z.get("interfaces", [])
        ifaces_str = ", ".join(ifaces) if isinstance(ifaces, list) else str(ifaces)
        t.add_row(z.get("name", ""), z.get("type", ""), ifaces_str)
    return t


def format_snippets(snippets: list[dict], device_filter: str = "") -> Table:
    """Render a list of SCM snippets.

    If device_filter is set, the title reflects that the list is scoped
    to a specific device.
    """
    title = f"Snippets — {device_filter}" if device_filter else f"Snippets ({len(snippets)})"
    t = Table(box=box.ROUNDED, title=title, header_style="bold cyan")
    t.add_column("Name", style="bold", no_wrap=True)
    t.add_column("Type",    no_wrap=True)
    t.add_column("Prefix",  no_wrap=True)
    t.add_column("Shared",  no_wrap=True)
    t.add_column("Folders attached", overflow="fold")
    for s in snippets:
        folders = s.get("folders", [])
        folder_names = ", ".join(f.get("name", "") for f in folders) if isinstance(folders, list) else ""
        t.add_row(
            s.get("name", ""),
            s.get("type", "") or "",
            "yes" if s.get("enable_prefix") else "no",
            s.get("shared_in", "") or "",
            folder_names,
        )
    return t


def format_snippet_detail(snippet: dict) -> Table:
    """Render full detail for a single snippet (key-value pairs)."""
    flat: dict[str, str] = {}
    flat["Name"]       = snippet.get("name", "")
    flat["ID"]         = snippet.get("id", "")
    flat["Type"]       = snippet.get("type", "") or ""
    flat["Prefix"]     = "enabled" if snippet.get("enable_prefix") else "disabled"
    flat["Shared in"]  = snippet.get("shared_in", "") or ""
    flat["Description"] = snippet.get("description", "") or ""
    folders = snippet.get("folders", [])
    if isinstance(folders, list):
        flat["Attached folders"] = ", ".join(f.get("name", "") for f in folders) or "(none)"
    return _kv_table(flat, title=f"Snippet: {snippet.get('name', '')}")


def format_device_detail(device: dict) -> Table:
    """Render full detail for a single device (key-value pairs)."""
    fields = [
        ("Hostname",          device.get("hostname") or device.get("display_name") or ""),
        ("Serial",            device.get("serial_number") or device.get("name") or ""),
        ("Model",             device.get("model") or ""),
        ("Software Version",  device.get("software_version") or ""),
        ("App Version",       device.get("app_version") or ""),
        ("IP Address",        device.get("ip_address") or ""),
        ("Connected",         "yes" if device.get("is_connected") else "no"),
        ("Connected Since",   device.get("connected_since") or ""),
        ("Uptime",            device.get("uptime") or ""),
        ("HA State",          device.get("ha_state") or ""),
        ("HA Peer Serial",    device.get("ha_peer_serial") or ""),
        ("Folder",            device.get("folder") or ""),
        ("Snippets",          ", ".join(device.get("snippets") or []) or "(none)"),
        ("Cert Status",       device.get("dev_cert_detail") or ""),
        ("Log DB Version",    device.get("log_db_version") or ""),
    ]
    t = Table(box=box.ROUNDED, show_header=False,
              title=f"Device: {device.get('hostname') or device.get('name')}")
    t.add_column("Field", style="bold cyan", no_wrap=True)
    t.add_column("Value", style="white")
    for k, v in fields:
        if v:
            t.add_row(k, str(v))
    return t
    return _kv_table(
        {k: str(v) for k, v in _flatten(data).items()},
        title=title,
    )


def format_raw(text: str, title: str = "") -> Panel:
    return Panel(Text(text), title=title or "Output", border_style="cyan")


def format_dict(data: dict, title: str = "") -> Table:
    return _kv_table({k: str(v) for k, v in _flatten(data).items()}, title=title)


# ---------------------------------------------------------------------------
# Util
# ---------------------------------------------------------------------------

def _flatten(d: Any, prefix: str = "") -> dict:
    """Recursively flatten a nested dict into dot-separated key/value pairs."""
    result = {}
    if isinstance(d, dict):
        for k, v in d.items():
            full_key = f"{prefix}.{k}" if prefix else k
            if isinstance(v, (dict, list)):
                result.update(_flatten(v, full_key))
            else:
                result[full_key] = v
    elif isinstance(d, list):
        for i, item in enumerate(d):
            result.update(_flatten(item, f"{prefix}[{i}]"))
    else:
        result[prefix] = d
    return result

