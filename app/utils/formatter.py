"""Output formatter — renders API/SSH data as rich tables and panels."""

from __future__ import annotations

from typing import Any, Callable

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

def _inheritance_note(obj: dict) -> str:
    """Return a dim 'inherited from X' note when obj lives in a parent folder.

    Returns empty string when the object is owned at the active folder level.
    The ``_active_folder`` key is injected by show_handler() at runtime.
    """
    active = obj.get("_active_folder", "")
    obj_folder = obj.get("folder", "")
    if active and obj_folder and obj_folder.lower() != active.lower():
        return f"[dim]↑ {obj_folder}[/dim]"
    return ""


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


def _simple_table(
    rows: list[dict],
    title: str,
    columns: list[tuple[str, str, dict]],
    value_fn=None,
) -> Table:
    """Build a fixed-column ROUNDED table from a list of dicts.

    ``columns`` is a list of ``(key, header, column-kwargs)`` tuples.
    ``value_fn(row, key)`` overrides the default cell value ``row.get(key, "")``.
    """
    t = Table(box=box.ROUNDED, title=title, header_style="bold cyan")
    for _key, header, kwargs in columns:
        t.add_column(header, **kwargs)
    for row in rows:
        if value_fn is not None:
            t.add_row(*[value_fn(row, key) for key, _h, _kw in columns])
        else:
            t.add_row(*[row.get(key, "") for key, _h, _kw in columns])
    return t


def _style_action(action: str, red_fallback: bool = False) -> str:
    """Colour a rule action: green for allow, red for deny.

    With ``red_fallback`` any non-allow value (including empty) is red;
    otherwise unrecognised actions are returned unstyled.
    """
    if action == "allow":
        return f"[green]{action}[/green]"
    if action == "deny" or red_fallback:
        return f"[red]{action}[/red]"
    return action


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
    def _cell(iface: dict, key: str) -> str:
        if key == "ip":
            # IP: may be in nested layer3 block (SCM) or flat ip-address (SSH)
            layer3 = iface.get("layer3") or {}
            layer3_entries = layer3.get("ip") or [{}]
            layer3_ip = layer3_entries[0].get("addr") or layer3_entries[0].get("name", "")
            return iface.get("ip") or iface.get("ip-address") or layer3_ip
        if key == "state":
            state = iface.get("state", "") or iface.get("comment", "") or ""
            if state == "up":
                return "[green]up[/green]"
            if state in ("down", "disabled"):
                return "[red]down[/red]"
            return state
        return iface.get(key, "")

    return _simple_table(interfaces, "Interfaces", [
        ("name",  "Name",            {"style": "bold", "no_wrap": True}),
        ("type",  "Type",            {"no_wrap": True}),
        ("ip",    "IP / Layer3",     {"overflow": "fold"}),
        ("zone",  "Zone",            {"no_wrap": True}),
        ("state", "State / Comment", {"overflow": "fold"}),
    ], value_fn=_cell)


def format_routes(routes: list[dict]) -> Table:
    return _simple_table(routes, "Routing Table", [
        ("destination", "Destination", {"overflow": "fold"}),
        ("nexthop",     "Next Hop",    {"overflow": "fold"}),
        ("interface",   "Interface",   {"overflow": "fold"}),
        ("metric",      "Metric",      {"overflow": "fold"}),
        ("flags",       "Flags",       {"overflow": "fold"}),
        ("age",         "Age",         {"overflow": "fold"}),
    ])


def format_security_policy(rules: list[dict]) -> Table:
    def _cell(r: dict, key: str) -> str:
        if key == "name":
            return r.get("name", "")
        if key == "action":
            return _style_action(r.get("action", ""), red_fallback=True)
        return ", ".join(r.get(key, []))

    return _simple_table(rules, "Security Policy", [
        ("name",        "Name",        {"style": "bold"}),
        ("from",        "From Zone",   {}),
        ("to",          "To Zone",     {}),
        ("source",      "Source",      {}),
        ("destination", "Dest",        {}),
        ("application", "Application", {}),
        ("action",      "Action",      {}),
    ], value_fn=_cell)


def format_jobs(jobs: list[dict]) -> Table:
    def _cell(j: dict, key: str) -> str:
        if key == "status":
            status = j.get("status", "")
            return f"[green]{status}[/green]" if status == "FIN" else f"[yellow]{status}[/yellow]"
        if key == "result":
            result = j.get("result", "")
            return f"[green]{result}[/green]" if result == "OK" else f"[red]{result}[/red]" if result else ""
        return j.get(key, "")

    return _simple_table(jobs, "Jobs", [
        ("id",       "ID",       {}),
        ("type",     "Type",     {}),
        ("status",   "Status",   {}),
        ("result",   "Result",   {}),
        ("progress", "Progress", {}),
        ("user",     "User",     {}),
        ("details",  "Details",  {}),
    ], value_fn=_cell)


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
    def _cell(a: dict, key: str) -> str:
        if key == "value":
            return a.get("ip-netmask") or a.get("ip_netmask") or a.get("ip-range") or a.get("fqdn") or ""
        if key == "_source":
            return _inheritance_note(a)
        return a.get(key, "")

    return _simple_table(addresses, "Address Objects", [
        ("name",        "Name",        {"style": "bold"}),
        ("value",       "IP / FQDN",   {}),
        ("description", "Description", {}),
        ("_source",     "Source",      {}),
    ], value_fn=_cell)


def format_address_groups(groups: list[dict]) -> Table:
    def _cell(g: dict, key: str) -> str:
        if key == "members":
            members = g.get("members", [])
            return ", ".join(members) if isinstance(members, list) else str(members)
        if key == "dynamic":
            return g.get("dynamic") or g.get("filter") or ""
        if key == "_source":
            return _inheritance_note(g)
        return g.get(key, "")

    return _simple_table(groups, "Address Groups", [
        ("name",        "Name",           {"style": "bold"}),
        ("members",     "Members",        {}),
        ("dynamic",     "Dynamic Filter", {}),
        ("description", "Description",    {}),
        ("_source",     "Source",         {}),
    ], value_fn=_cell)


def format_services(services: list[dict]) -> Table:
    # NB: the SCM object API shape ({tcp: {destination_port: ...}}) is handled
    # separately by _snippet_services_table; this renderer expects the flat
    # SSH/op shape with 'port' nested under the protocol dict.
    def _cell(s: dict, key: str) -> str:
        if key == "protocol":
            proto = s.get("protocol", "")
            if isinstance(proto, dict):
                proto = list(proto.keys())[0] if proto else ""
            return str(proto)
        if key == "port":
            port = s.get("port", "")
            if not port and isinstance(s.get("protocol"), dict):
                for _p, _v in (s["protocol"].items()):
                    if isinstance(_v, dict):
                        port = _v.get("port", "")
            return str(port)
        return s.get(key, "")

    return _simple_table(services, "Services", [
        ("name",        "Name",        {"style": "bold"}),
        ("protocol",    "Protocol",    {}),
        ("port",        "Port",        {}),
        ("description", "Description", {}),
    ], value_fn=_cell)


def format_tags(tags: list[dict]) -> Table:
    def _cell(t: dict, key: str) -> str:
        if key == "_source":
            return _inheritance_note(t)
        return t.get(key, "")
    return _simple_table(tags, "Tags", [
        ("name",     "Name",     {"style": "bold"}),
        ("color",    "Color",    {}),
        ("comments", "Comments", {}),
        ("_source",  "Source",   {}),
    ], value_fn=_cell)


def format_edl_list(edls: list[dict]) -> Table:
    """Render external dynamic lists."""
    def _parse_type(e: dict) -> tuple[str, str, str]:
        """Extract (type, source, repeat) from the nested EDL type dict."""
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
        return str(edl_type), source, str(repeat)

    def _cell(e: dict, key: str) -> str:
        if key in ("type", "source", "repeat"):
            edl_type, source, repeat = _parse_type(e)
            return {"type": edl_type, "source": source, "repeat": repeat}[key]
        if key == "description":
            return e.get("description", "") or ""
        if key == "_source":
            return _inheritance_note(e)
        return e.get(key, "")

    return _simple_table(edls, "External Dynamic Lists", [
        ("name",        "Name",         {"style": "bold"}),
        ("type",        "Type",         {"no_wrap": True}),
        ("source",      "URL / Source", {"overflow": "fold"}),
        ("repeat",      "Repeat",       {"no_wrap": True}),
        ("description", "Description",  {"overflow": "fold"}),
        ("_source",     "Source",       {}),
    ], value_fn=_cell)


def format_zones(zones: list[dict]) -> Table:
    def _cell(z: dict, key: str) -> str:
        if key == "interfaces":
            ifaces = z.get("interfaces", [])
            return ", ".join(ifaces) if isinstance(ifaces, list) else str(ifaces)
        return z.get(key, "")

    return _simple_table(zones, "Zones", [
        ("name",       "Name",       {"style": "bold"}),
        ("type",       "Type",       {}),
        ("interfaces", "Interfaces", {}),
    ], value_fn=_cell)


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

    def _cell(s: dict, key: str) -> str:
        if key == "enable_prefix":
            return "yes" if s.get("enable_prefix") else "no"
        if key == "folders":
            folders = s.get("folders", [])
            return ", ".join(f.get("name", "") for f in folders) if isinstance(folders, list) else ""
        return s.get(key, "") or ""

    return _simple_table(snippets, title, [
        ("name",          "Name",             {"style": "bold", "no_wrap": True}),
        ("type",          "Type",             {"no_wrap": True}),
        ("enable_prefix", "Prefix",           {"no_wrap": True}),
        ("shared_in",     "Shared",           {"no_wrap": True}),
        ("folders",       "Folders attached", {"overflow": "fold"}),
    ], value_fn=_cell)


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
    flat: dict[str, str] = {
        "Name": name,
        "ID": snippet.get("id", "") or "",
        "Type": snippet.get("type", "") or "",
        "Prefix": "enabled" if snippet.get("enable_prefix") else "disabled",
        "Shared in": snippet.get("shared_in", "") or "",
        "Description": snippet.get("description", "") or "",
    }

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
    flat: dict[str, str] = {
        "Name": name,
        "ID": snippet.get("id", "") or "",
        "Type": snippet.get("type", "") or "",
        "Prefix": "enabled" if snippet.get("enable_prefix") else "disabled",
        "Shared in": snippet.get("shared_in", "") or "",
        "Description": snippet.get("description", "") or "",
    }

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
    _KNOWN_RENDERERS: dict[str, Callable[[list[dict], str], Table]] = {
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
    def _addr(a: dict) -> tuple[str, str]:
        for key in ("ip_netmask", "ip_range", "ip_wildcard", "fqdn"):
            if a.get(key):
                return key.replace("_", "-"), str(a[key])
        return "", ""

    def _cell(a: dict, key: str) -> str:
        if key == "type":
            return _addr(a)[0]
        if key == "value":
            return _addr(a)[1]
        return a.get(key, "") or ""

    return _simple_table(items, f"{title} ({len(items)})", [
        ("name",        "Name",        {"style": "bold", "no_wrap": True}),
        ("type",        "Type",        {"no_wrap": True}),
        ("value",       "Value",       {"overflow": "fold"}),
        ("description", "Description", {"overflow": "fold"}),
    ], value_fn=_cell)


def _snippet_address_groups_table(items: list[dict], title: str) -> Table:
    def _cell(g: dict, key: str) -> str:
        if g.get("static"):
            kind = "static"
            members = ", ".join(g["static"]) if isinstance(g["static"], list) else str(g["static"])
        elif g.get("dynamic"):
            kind = "dynamic"
            members = str(g["dynamic"].get("filter", ""))
        else:
            kind, members = "", ""
        if key == "type":
            return kind
        if key == "members":
            return members
        return g.get(key, "")

    return _simple_table(items, f"{title} ({len(items)})", [
        ("name",    "Name",    {"style": "bold", "no_wrap": True}),
        ("type",    "Type",    {"no_wrap": True}),
        ("members", "Members", {"overflow": "fold"}),
    ], value_fn=_cell)


def _snippet_services_table(items: list[dict], title: str) -> Table:
    # NB: intentionally distinct from format_services — SCM objects carry
    # {tcp|udp: {destination_port: ...}}, not the flat 'port' key.
    def _proto(s: dict) -> tuple[str, str]:
        proto = s.get("protocol", {})
        if isinstance(proto, dict):
            if "tcp" in proto:
                return "tcp", str(proto["tcp"].get("destination_port", ""))
            if "udp" in proto:
                return "udp", str(proto["udp"].get("destination_port", ""))
            return "", ""
        return str(proto), ""

    def _cell(s: dict, key: str) -> str:
        if key == "protocol":
            return _proto(s)[0]
        if key == "port":
            return _proto(s)[1]
        return s.get(key, "") or ""

    return _simple_table(items, f"{title} ({len(items)})", [
        ("name",        "Name",        {"style": "bold", "no_wrap": True}),
        ("protocol",    "Protocol",    {"no_wrap": True}),
        ("port",        "Port",        {"no_wrap": True}),
        ("description", "Description", {"overflow": "fold"}),
    ], value_fn=_cell)


def _snippet_security_rules_table(items: list[dict], title: str) -> Table:
    def _join(val):
        if isinstance(val, list):
            return ", ".join(str(v) for v in val)
        return str(val) if val else ""

    def _cell(r: dict, key: str) -> str:
        if key == "name":
            return r.get("name", "")
        if key == "action":
            return _style_action(r.get("action", ""))
        return _join(r.get(key, []))

    return _simple_table(items, f"{title} ({len(items)})", [
        ("name",        "Name",        {"style": "bold", "no_wrap": True}),
        ("from",        "From",        {"no_wrap": True}),
        ("source",      "Source",      {"overflow": "fold"}),
        ("to",          "To",          {"no_wrap": True}),
        ("destination", "Destination", {"overflow": "fold"}),
        ("application", "Application", {"overflow": "fold"}),
        ("action",      "Action",      {"no_wrap": True, "style": "bold"}),
    ], value_fn=_cell)


def _snippet_tags_table(items: list[dict], title: str) -> Table:
    def _cell(tag: dict, key: str) -> str:
        return tag.get(key, "") or ""

    return _simple_table(items, f"{title} ({len(items)})", [
        ("name",     "Name",     {"style": "bold", "no_wrap": True}),
        ("color",    "Color",    {"no_wrap": True}),
        ("comments", "Comments", {"overflow": "fold"}),
    ], value_fn=_cell)


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
