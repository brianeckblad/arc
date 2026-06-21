"""Output formatter — renders API/SSH data as rich tables and panels."""

from __future__ import annotations

from typing import Any

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.tree import Tree
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


def format_devices(devices: list[dict], folder: str = "Shared") -> Table:
    """Render the SCM device list, scoped to ``folder``.

    Field names sourced from GET /config/setup/v1/devices (api.strata.paloaltonetworks.com).
    The endpoint has no folder parameter; it returns every device visible to the
    token's TSG scope regardless of which folder is currently active.
    Key fields: is_connected (bool), software_version, serial_number, ip_address,
                ha_state, uptime, model, folder.

    ``folder`` controls the table title:
      "Shared" (root) → "All Managed Devices — TSG-wide (N)"
      Any other value → "Devices in <folder> (N)"
    """
    if folder and folder != "Shared":
        title = f"Devices in {folder} ({len(devices)})"
    else:
        title = f"All Managed Devices — TSG-wide ({len(devices)})"
    t = Table(box=box.ROUNDED, title=title, header_style="bold cyan")
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


def format_folder_tree(
    folders: list[dict],
    devices: list[dict],
    root_folder: str = "",
) -> Tree:
    """Render the SCM folder hierarchy as a tree, with devices shown in their folder.

    Each folder node shows:
      - The folder name (green)
      - Connected device hostnames in that folder, with a count (if any)

    Folder parent relationships come from each folder record's ``parent`` field
    (a string — the parent folder's name).  Folders whose parent is absent or
    not in the known folder list are treated as roots.

    ``root_folder`` — when provided, renders only the sub-tree rooted at that
    folder instead of the full TSG-wide hierarchy.  The root folder itself
    becomes the top-level tree node; all of its descendants are shown beneath
    it.  Pass ``""`` (default) for the full tree.

    pan.dev: GET /config/setup/v1/folders  (carries 'parent' field)
    pan.dev: GET /config/setup/v1/devices  (carries 'folder' field)
    """
    # Map folder name → list of device hostnames directly in that folder.
    folder_devices: dict[str, list[str]] = {}
    for d in devices:
        fname    = d.get("folder") or "Shared"
        hostname = d.get("hostname") or d.get("display_name") or d.get("name") or ""
        if hostname:
            folder_devices.setdefault(fname, []).append(hostname)

    # Build parent → [children] mapping and a lookup dict.
    children:       dict[str, list[str]] = {}
    folder_by_name: dict[str, dict]      = {}
    for f in folders:
        fname  = f.get("name", "")
        parent = f.get("parent", "") or ""
        if not fname:
            continue
        folder_by_name[fname] = f
        children.setdefault(parent, [])
        if fname not in children[parent]:
            children[parent].append(fname)

    # Sort children lists for consistent, alphabetical display.
    for key in children:
        children[key].sort()

    def _folder_label(folder_name: str, bold: bool = False) -> str:
        """Return a Rich-markup label for a folder node, including direct devices."""
        devs      = folder_devices.get(folder_name, [])
        dev_count = len(devs)
        name_style = "bold green" if bold else "green"
        if devs:
            dev_str = ", ".join(devs)
            return (
                f"[{name_style}]{folder_name}[/{name_style}]  "
                f"[dim]{dev_count} device{'s' if dev_count != 1 else ''}:[/dim] "
                f"[cyan]{dev_str}[/cyan]"
            )
        return f"[{name_style}]{folder_name}[/{name_style}]"

    def _add_node(branch: Tree, folder_name: str) -> None:
        """Recursively add a folder and all its descendants to ``branch``."""
        node = branch.add(_folder_label(folder_name))
        for child in children.get(folder_name, []):
            _add_node(node, child)

    # ------------------------------------------------------------------
    # Scoped mode: render only the sub-tree rooted at root_folder
    # ------------------------------------------------------------------
    if root_folder and root_folder in folder_by_name:
        tree = Tree(_folder_label(root_folder, bold=True))
        for child in children.get(root_folder, []):
            _add_node(tree, child)
        return tree

    # ------------------------------------------------------------------
    # Full mode: render the entire TSG-wide hierarchy
    # ------------------------------------------------------------------
    all_names = set(folder_by_name)
    roots = sorted(
        name for name, f in folder_by_name.items()
        if not (f.get("parent") or "") or (f.get("parent") or "") not in all_names
    )

    tree = Tree("[bold cyan]Folder Structure[/bold cyan]", hide_root=True)
    for root in roots:
        _add_node(tree, root)

    return tree


def _folder_flat_list(folders: list[dict]) -> list[tuple[int, str, str]]:
    """Return a depth-ordered flat list of (depth, name, path) tuples.

    Useful for numbered selection menus — preserves tree order so that
    indented display matches the flat index numbers.
    """
    children:       dict[str, list[str]] = {}
    folder_by_name: dict[str, dict]      = {}
    for f in folders:
        fname  = f.get("name", "")
        parent = f.get("parent", "") or ""
        if not fname:
            continue
        folder_by_name[fname] = f
        children.setdefault(parent, [])
        if fname not in children[parent]:
            children[parent].append(fname)

    for key in children:
        children[key].sort()

    all_names = set(folder_by_name)
    roots = sorted(
        name for name, f in folder_by_name.items()
        if not (f.get("parent") or "") or (f.get("parent") or "") not in all_names
    )

    flat: list[tuple[int, str, str]] = []

    def _flatten(fname: str, depth: int, path: str) -> None:
        full_path = f"{path}/{fname}" if path else fname
        flat.append((depth, fname, full_path))
        for child in children.get(fname, []):
            _flatten(child, depth + 1, full_path)

    for root in roots:
        _flatten(root, 0, "")

    return flat


def format_interfaces(interfaces: list[dict]) -> Table:
    """Render a list of interfaces from SCM or SSH.

    SCM network API returns configuration fields (name, type, ip, zone, comment).
    SSH operational output returns state fields (state, speed, etc.).
    Both are handled by showing whatever fields are present.
    """
    t = Table(box=box.ROUNDED, title="Interfaces", header_style="bold cyan")
    t.add_column("Name", style="bold", no_wrap=True)
    t.add_column("Type", no_wrap=True)
    t.add_column("IP / Layer3", overflow="fold")
    t.add_column("Zone", no_wrap=True)
    t.add_column("State / Comment", overflow="fold")
    for iface in interfaces:
        # IP: may be in nested layer3 block (SCM) or flat ip-address (SSH)
        ip = (
            iface.get("ip") or
            iface.get("ip-address") or
            iface.get("layer3", {}).get("ip", [{}])[0].get("addr", "") if iface.get("layer3") else "" or
            ""
        )
        state = iface.get("state", "") or iface.get("comment", "") or ""
        if state == "up":
            state = "[green]up[/green]"
        elif state in ("down", "disabled"):
            state = "[red]down[/red]"
        t.add_row(
            iface.get("name", ""),
            iface.get("type", ""),
            ip,
            iface.get("zone", ""),
            state,
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


def format_tags(tags: list[dict]) -> Table:
    t = Table(box=box.ROUNDED, title="Tags", header_style="bold cyan")
    t.add_column("Name", style="bold")
    t.add_column("Color")
    t.add_column("Comments")
    for tag in tags:
        t.add_row(tag.get("name", ""), tag.get("color", ""), tag.get("comments", ""))
    return t


def format_edl_list(edls: list[dict]) -> Table:
    """Render external dynamic lists."""
    t = Table(box=box.ROUNDED, title="External Dynamic Lists", header_style="bold cyan")
    t.add_column("Name",        style="bold")
    t.add_column("Type",        no_wrap=True)
    t.add_column("URL / Source", overflow="fold")
    t.add_column("Repeat",      no_wrap=True)
    t.add_column("Description", overflow="fold")
    for e in edls:
        edl_type = e.get("type", "")
        source = ""
        repeat = ""
        if isinstance(edl_type, dict):
            for kind, cfg in edl_type.items():
                edl_type = kind
                if isinstance(cfg, dict):
                    source = cfg.get("url", "") or cfg.get("source", "")
                    repeat = cfg.get("recurring", "") or ""
                    if isinstance(repeat, dict):
                        repeat = next(iter(repeat.keys()), "")
                break
        t.add_row(
            e.get("name", ""),
            str(edl_type),
            source,
            str(repeat),
            e.get("description", "") or "",
        )
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


def format_ha(data: Any, title: str = "High Availability") -> Table:
    """Render HA configuration as a flat key/value table.

    Accepts either a single dict (from show high-availability state) or a
    list of dicts (from show high-availability all).  Lists are flattened into
    separate sections separated by a blank row.
    """
    if isinstance(data, list):
        if not data:
            t = Table(box=box.ROUNDED, title=title, show_header=False)
            t.add_column("Info")
            t.add_row("[dim]No HA configuration found in this folder.[/dim]")
            return t
        # Multiple HA entries — flatten the first for now; most deployments have one.
        return _kv_table(_flatten(data[0]), title=title)
    if isinstance(data, dict):
        if not data:
            t = Table(box=box.ROUNDED, title=title, show_header=False)
            t.add_column("Info")
            t.add_row("[dim]No HA configuration found in this folder.[/dim]")
            return t
        return _kv_table(_flatten(data), title=title)
    t = Table(box=box.ROUNDED, title=title, show_header=False)
    t.add_column("Info")
    t.add_row(str(data))
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


def format_snippets_scoped(data: dict) -> list:
    """Render a context-scoped snippet list with a scope header and hint footer.

    The snippet list API does not populate folder references on list items,
    so the table only shows fields that are reliably present: name, shared_in,
    description.  The "Folders attached" column is omitted here — it is only
    meaningful in the detail view (show snippet <name>).
    """
    from rich.text import Text

    snippets: list[dict] = data.get("snippets", [])
    scope: str = data.get("scope", "")
    hint: str = data.get("hint", "")

    renderables: list = []

    # Scope header
    renderables.append(Text.from_markup(
        f"[bold cyan]Snippets[/bold cyan]  [dim]({scope})[/dim]"
    ))

    if snippets:
        t = Table(box=box.ROUNDED, header_style="bold cyan",
                  title=f"{len(snippets)} snippet(s)")
        t.add_column("Name",        style="bold", no_wrap=True)
        t.add_column("Shared in",   no_wrap=True)
        t.add_column("Prefix",      no_wrap=True)
        t.add_column("Description", overflow="fold")
        for s in snippets:
            t.add_row(
                s.get("name", ""),
                s.get("shared_in", "") or "",
                "yes" if s.get("enable_prefix") else "no",
                s.get("description", "") or "",
            )
        renderables.append(t)
    else:
        renderables.append(Text.from_markup("[dim]No snippets in this context.[/dim]"))

    if hint:
        renderables.append(Text.from_markup(f"[dim]  {hint}[/dim]"))

    return renderables


def format_snippet_detail(snippet: dict) -> list:
    """Render metadata + variables for a single snippet.

    Returns a list of Rich renderables.
    Called by 'show snippet <name>' (no details flag).
    """
    name = snippet.get("name", "")
    renderables: list = []

    # --- Header: identity and metadata ---
    flat: dict[str, str] = {}
    flat["Name"]        = name
    flat["ID"]          = snippet.get("id", "") or ""
    flat["Type"]        = snippet.get("type", "") or ""
    flat["Prefix"]      = "enabled" if snippet.get("enable_prefix") else "disabled"
    flat["Shared in"]   = snippet.get("shared_in", "") or ""
    flat["Description"] = snippet.get("description", "") or ""

    labels = snippet.get("labels", [])
    if labels:
        flat["Labels"] = ", ".join(str(l) for l in labels) if isinstance(labels, list) else str(labels)

    folders = snippet.get("folders", [])
    if isinstance(folders, list) and folders:
        folder_labels = []
        for f in folders:
            if isinstance(f, dict):
                label = f.get("name") or f.get("id") or ""
            else:
                label = str(f)
            if label:
                folder_labels.append(label)
        flat["Attached folders"] = ", ".join(folder_labels) if folder_labels else "(none)"
    else:
        flat["Attached folders"] = "(none)"

    renderables.append(_kv_table(flat, title=f"Snippet: {name}"))

    # --- Variables ---
    _append_variables(renderables, snippet.get("variables", []))

    from rich.text import Text
    renderables.append(Text.from_markup(
        "[dim]  Tip: [bold]show snippet " + name + " details[/bold] "
        "→ also shows configured addresses, rules, services, and tags[/dim]"
    ))

    return renderables


def format_snippet_detail_full(data: dict) -> list:
    """Render full snippet detail: metadata + variables + all configured objects.

    Called by 'show snippet <name> details'.
    data keys:
        snippet  — dict from GET /config/setup/v1/snippets/{id}
        objects  — dict[label, list[dict]] from get_snippet_objects()
    """
    from rich.text import Text

    snippet: dict = data.get("snippet", {})
    objects: dict[str, list] = data.get("objects", {})
    name = snippet.get("name", "")
    renderables: list = []

    # --- Header ---
    flat: dict[str, str] = {}
    flat["Name"]        = name
    flat["ID"]          = snippet.get("id", "") or ""
    flat["Type"]        = snippet.get("type", "") or ""
    flat["Prefix"]      = "enabled" if snippet.get("enable_prefix") else "disabled"
    flat["Shared in"]   = snippet.get("shared_in", "") or ""
    flat["Description"] = snippet.get("description", "") or ""

    labels = snippet.get("labels", [])
    if labels:
        flat["Labels"] = ", ".join(str(l) for l in labels) if isinstance(labels, list) else str(labels)

    folders = snippet.get("folders", [])
    if isinstance(folders, list) and folders:
        folder_labels = []
        for f in folders:
            label = (f.get("name") or f.get("id") or "") if isinstance(f, dict) else str(f)
            if label:
                folder_labels.append(label)
        flat["Attached folders"] = ", ".join(folder_labels) if folder_labels else "(none)"
    else:
        flat["Attached folders"] = "(none)"

    renderables.append(_kv_table(flat, title=f"Snippet: {name}"))

    # --- Variables ---
    _append_variables(renderables, snippet.get("variables", []))

    # --- Configured objects ---
    if not objects:
        renderables.append(Text.from_markup(
            "[dim]  No configured objects found in this snippet "
            "(addresses, rules, services, tags, etc.)[/dim]"
        ))
        return renderables

    renderables.append(Text.from_markup(
        f"\n[bold cyan]Configured Objects[/bold cyan]  "
        f"[dim]({sum(len(v) for v in objects.values())} item(s) across "
        f"{len(objects)} type(s))[/dim]"
    ))

    # Render each object type as a dedicated table.
    # Known types get purpose-built renderers; everything else gets a generic table.
    _KNOWN_RENDERERS: dict[str, callable] = {
        "Addresses":        _snippet_addresses_table,
        "Address Groups":   _snippet_address_groups_table,
        "Services":         _snippet_services_table,
        "Security Rules":   _snippet_security_rules_table,
        "Tags":             _snippet_tags_table,
    }
    for label, items in objects.items():
        renderer = _KNOWN_RENDERERS.get(label)
        if renderer:
            renderables.append(renderer(items, label))
        else:
            renderables.append(_generic_objects_table(items, label))

    return renderables


# ---------------------------------------------------------------------------
# Snippet object section renderers (used by format_snippet_detail_full)
# ---------------------------------------------------------------------------

def _append_variables(renderables: list, variables: list) -> None:
    """Append a variables table to renderables if any variables exist."""
    if not variables or not isinstance(variables, list):
        return
    vt = Table(box=box.ROUNDED, title="Variables", header_style="bold cyan")
    vt.add_column("Name",        style="bold", no_wrap=True)
    vt.add_column("Type",        no_wrap=True)
    vt.add_column("Default",     overflow="fold")
    vt.add_column("Description", overflow="fold")
    for v in variables:
        if isinstance(v, dict):
            vt.add_row(
                v.get("name", ""),
                v.get("type", "") or "",
                str(v.get("default", "")) if v.get("default") is not None else "",
                v.get("description", "") or "",
            )
    renderables.append(vt)


def _snippet_addresses_table(items: list[dict], title: str) -> Table:
    t = Table(box=box.ROUNDED, title=f"{title} ({len(items)})", header_style="bold cyan")
    t.add_column("Name",        style="bold", no_wrap=True)
    t.add_column("Type",        no_wrap=True)
    t.add_column("Value",       overflow="fold")
    t.add_column("Description", overflow="fold")
    for a in items:
        addr_type = ""
        value = ""
        for key in ("ip_netmask", "ip_range", "ip_wildcard", "fqdn"):
            if a.get(key):
                addr_type = key.replace("_", "-")
                value = str(a[key])
                break
        t.add_row(a.get("name", ""), addr_type, value, a.get("description", "") or "")
    return t


def _snippet_address_groups_table(items: list[dict], title: str) -> Table:
    t = Table(box=box.ROUNDED, title=f"{title} ({len(items)})", header_style="bold cyan")
    t.add_column("Name",    style="bold", no_wrap=True)
    t.add_column("Type",    no_wrap=True)
    t.add_column("Members", overflow="fold")
    for g in items:
        if g.get("static"):
            members = ", ".join(g["static"]) if isinstance(g["static"], list) else str(g["static"])
            t.add_row(g.get("name", ""), "static", members)
        elif g.get("dynamic"):
            t.add_row(g.get("name", ""), "dynamic", str(g["dynamic"].get("filter", "")))
        else:
            t.add_row(g.get("name", ""), "", "")
    return t


def _snippet_services_table(items: list[dict], title: str) -> Table:
    t = Table(box=box.ROUNDED, title=f"{title} ({len(items)})", header_style="bold cyan")
    t.add_column("Name",     style="bold", no_wrap=True)
    t.add_column("Protocol", no_wrap=True)
    t.add_column("Port",     no_wrap=True)
    t.add_column("Description", overflow="fold")
    for s in items:
        proto = s.get("protocol", {})
        if isinstance(proto, dict):
            if "tcp" in proto:
                p, port = "tcp", str(proto["tcp"].get("destination_port", ""))
            elif "udp" in proto:
                p, port = "udp", str(proto["udp"].get("destination_port", ""))
            else:
                p, port = "", ""
        else:
            p, port = str(proto), ""
        t.add_row(s.get("name", ""), p, port, s.get("description", "") or "")
    return t


def _snippet_security_rules_table(items: list[dict], title: str) -> Table:
    t = Table(box=box.ROUNDED, title=f"{title} ({len(items)})", header_style="bold cyan")
    t.add_column("Name",        style="bold", no_wrap=True)
    t.add_column("From",        no_wrap=True)
    t.add_column("Source",      overflow="fold")
    t.add_column("To",          no_wrap=True)
    t.add_column("Destination", overflow="fold")
    t.add_column("Application", overflow="fold")
    t.add_column("Action",      no_wrap=True, style="bold")
    for r in items:
        def _join(val):
            if isinstance(val, list):
                return ", ".join(str(v) for v in val)
            return str(val) if val else ""
        action = r.get("action", "")
        action_style = "green" if action == "allow" else "red" if action == "deny" else ""
        t.add_row(
            r.get("name", ""),
            _join(r.get("from", [])),
            _join(r.get("source", [])),
            _join(r.get("to", [])),
            _join(r.get("destination", [])),
            _join(r.get("application", [])),
            f"[{action_style}]{action}[/{action_style}]" if action_style else action,
        )
    return t


def _snippet_tags_table(items: list[dict], title: str) -> Table:
    t = Table(box=box.ROUNDED, title=f"{title} ({len(items)})", header_style="bold cyan")
    t.add_column("Name",    style="bold", no_wrap=True)
    t.add_column("Color",   no_wrap=True)
    t.add_column("Comments", overflow="fold")
    for tag in items:
        t.add_row(tag.get("name", ""), tag.get("color", "") or "", tag.get("comments", "") or "")
    return t


def _generic_objects_table(items: list[dict], title: str) -> Table:
    """Fallback renderer for object types without a dedicated renderer."""
    if not items:
        return Table(title=title)
    cols = list(items[0].keys())
    t = Table(box=box.ROUNDED, title=f"{title} ({len(items)})", header_style="bold cyan")
    for c in cols:
        t.add_column(c.replace("_", " ").replace("-", " ").title(), overflow="fold")
    for item in items:
        t.add_row(*[str(item.get(c, "") or "") for c in cols])
    return t


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

