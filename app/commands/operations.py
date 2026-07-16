"""Operations commands (jobs, commit, system info, logs). See docs/commands/ and docs/scm-api/specs/operations*.md for details."""

from __future__ import annotations

import shlex
import threading
from datetime import datetime, timezone
from typing import Any

from app.commands.base import CommandDef, ExecutionContext, require_device, require_scm, show_handler


# ---------------------------------------------------------------------------
# SCM API handlers
# ---------------------------------------------------------------------------

def _show_system_info(ctx: ExecutionContext, args: dict) -> Any:
    """Show what SCM knows about the selected device.

    Returns the full device record from SCM — model, serial number, software
    version, IP address, connection status, folder, snippets, etc.

    This is configuration/inventory data stored in SCM, not live operational
    state.  For live system info use 'show system info --remote'.

    pan.dev: GET /config/setup/v1/devices  (filtered to the active device)
    """
    device = require_device(ctx)
    scm    = require_scm(ctx)

    serial   = device.get("serial_number") or device.get("name") or ""
    hostname = device.get("hostname") or ""

    devices = scm.get_devices()
    match = next(
        (d for d in devices
         if d.get("serial_number") == serial
         or d.get("name") == serial
         or (hostname and d.get("hostname", "").lower() == hostname.lower())),
        device,   # fall back to the cached device record we already have
    )
    return {"_render": "device_detail", "device": match}


def _show_jobs_id(ctx: ExecutionContext, args: dict) -> list[dict]:
    """Fetch a single SCM job by ID — TSG-wide, no folder scope."""
    job_id = str(args.get("id", "")).strip()
    if not job_id:
        raise RuntimeError("Usage: show jobs id <job-id>")
    scm = require_scm(ctx)
    job = scm.get_job(job_id)
    if job is None:
        raise RuntimeError(f"Job {job_id!r} not found or access denied")
    return [job]


def _commit(ctx: ExecutionContext, args: dict) -> Any:
    """Push the candidate configuration to managed devices.

    Creates an SCM push job.  The returned job record includes the job ID
    so the operator can track progress with 'show jobs id <n>'.

    pan.dev: POST /config/setup/v1/config-versions/candidate:push
    """
    scm         = require_scm(ctx)
    description = args.get("description", "")

    # Scope the push to the active folder when one is set.
    folders = [ctx.folder] if ctx.folder and ctx.folder.lower() != "shared" else None

    job = scm.push_config(folders=folders, description=description)
    job_id = job.get("id") or job.get("job_id") or ""
    if job_id:
        return [job]   # render as jobs table so job ID is prominently shown
    return job


# ---------------------------------------------------------------------------
# Live-device operational handlers (SCM has no API — use --remote)
# ---------------------------------------------------------------------------

def _live_only(command: str) -> Any:
    """Return a clear message explaining why this command needs --remote."""
    return (
        f"'{command}' shows live device state — SCM does not store this data.\n"
        f"  → Run: [bold]{command} --remote[/bold]  to fetch it from the device via SSH.\n"
        f"  → Or:  [bold]remote <device>[/bold]  to open an interactive SSH session."
    )


def _clear_session_all(ctx: ExecutionContext, args: dict) -> str:
    """Clear all sessions on the device — use --remote.

    CAUTION: This terminates ALL active sessions on the target firewall.
    Use with care in production environments.
    """
    device = require_device(ctx)
    name = device.get("hostname") or device.get("name") or "device"
    return (
        "[yellow]⚠  clear session all terminates ALL active sessions on the device.[/yellow]\n"
        f"  Run:  clear session all --remote  on [bold]{name}[/bold] to execute.\n"
        "  [dim]To clear a specific session: clear session id <n> --remote[/dim]"
    )


def _clear_session_id(ctx: ExecutionContext, args: dict) -> str:
    """Clear a specific session by ID — use --remote.

    Usage: clear session id <session-id>
    """
    device = require_device(ctx)
    name = device.get("hostname") or device.get("name") or "device"
    session_id = (args.get("id") or args.get("_positional", [None])[0] or "").strip()
    if not session_id:
        raise ValueError(
            "Usage: clear session id <session-id>  (use --remote)\n"
            "  Find session IDs with: show session all --remote"
        )
    return (
        f"  Run:  clear session id {session_id} --remote  on [bold]{name}[/bold] to execute."
    )


def _ssh_clear_session_id(args: dict) -> str:
    session_id = shlex.quote(str(args.get("id") or (args.get("_positional") or [""])[0] or ""))
    return f"clear session id {session_id}"


def _pending_show_system_resources(ctx: ExecutionContext, args: dict) -> str:
    return _live_only("show system resources")


def _pending_show_system_disk_space(ctx: ExecutionContext, args: dict) -> str:
    return _live_only("show system disk-space")


def _pending_request_software_check(ctx: ExecutionContext, args: dict) -> str:
    return _live_only("request system software check")


def _pending_ping(ctx: ExecutionContext, args: dict) -> str:
    if not args.get("host"):
        raise RuntimeError("Usage: ping host <ip>")
    return _live_only("ping host")


# ---------------------------------------------------------------------------
# Fleet-wide log queries — Strata Logging Service (SLS, formerly CDL)
#
# `show log traffic|threat|system` query the tenant's SLS instance across ALL
# firewalls that forward logs there.  SLS ingestion lags minutes behind the
# device, so the --remote SSH path is kept for real-time output on one device.
# Client: app/api/sls.py (CDL Query Service v2 — no OpenAPI spec on pan.dev).
# ---------------------------------------------------------------------------

# Module-level stash of the last SLS query's FULL rows (documented behaviour):
# handlers receive an ExecutionContext without shell state, so `show log
# detail <n>` re-reads row n from here.  Rendered tables show a mapped subset;
# this keeps every SLS field for the detail view.  One shell process = one
# operator session, so a module-level list is safe here.  The lock guards
# against future concurrent use (e.g. watch + a second command).
_LAST_ROWS: list[dict] = []
_LAST_QUERY_DESC: str = ""   # e.g. "traffic (last 1h)" — for detail-view titles
_LAST_ROWS_LOCK = threading.Lock()

_LOG_USAGE = (
    "Usage: show log <traffic|threat|system> [src <ip>] [dst <ip>] [port <n>] "
    "[rule <name>] [app <name>] [last <Nm|Nh|Nd>] [limit <n>]"
)

# Only SLS clients are cached — one per SCMConfig object, created on first use.
_SLS_CLIENTS: dict[int, Any] = {}
_SLS_CLIENTS_LOCK = threading.Lock()


def _get_sls(ctx: ExecutionContext):
    """Return a cached SLSClient built from the active SCM credentials."""
    from app.api.sls import SLSClient  # lazy — avoid httpx import at registry load

    cfg = getattr(ctx.config, "scm", None)
    if cfg is None or not cfg.is_configured:
        raise ValueError(
            "SLS queries need SCM credentials. Set SCM_CLIENT_ID / "
            "SCM_CLIENT_SECRET / SCM_TSG_ID (or SCM_BEARER_TOKEN) and restart."
        )
    key = id(cfg)
    with _SLS_CLIENTS_LOCK:
        if key not in _SLS_CLIENTS:
            _SLS_CLIENTS[key] = SLSClient(cfg)
        return _SLS_CLIENTS[key]


def _parse_log_window(value: str) -> int:
    """Parse 'Nm' / 'Nh' / 'Nd' into minutes; raise ValueError on bad input."""
    text = str(value).strip().lower()
    unit = text[-1:] if text[-1:] in ("m", "h", "d") else ""
    digits = text[:-1] if unit else text
    if not digits.isdigit() or int(digits) < 1:
        raise ValueError(
            f"Bad time window {value!r} — use last <Nm|Nh|Nd>, e.g. last 15m, last 2h, last 1d."
        )
    return int(digits) * {"m": 1, "h": 60, "d": 1440}[unit or "m"]


def _parse_log_args(args: dict) -> tuple[dict, int, int]:
    """Parse `show log <type>` keyword pairs from the raw remainder tokens.

    Returns (filters, limit, minutes_back).  Defaults: last 1h, limit 100
    (capped at 1000).  Unknown keywords raise ValueError with the usage line.
    """
    tokens: list[str] = list(args.get("_remainder") or [])
    filters: dict[str, str] = {}
    limit = 100
    minutes_back = 60
    i = 0
    while i < len(tokens):
        key = tokens[i].lower()
        if key not in ("src", "dst", "port", "rule", "app", "last", "limit"):
            raise ValueError(f"Unknown argument {tokens[i]!r}.\n  {_LOG_USAGE}")
        if i + 1 >= len(tokens):
            raise ValueError(f"'{key}' needs a value.\n  {_LOG_USAGE}")
        value = tokens[i + 1]
        if key == "last":
            minutes_back = _parse_log_window(value)
        elif key == "limit":
            if not value.isdigit() or int(value) < 1:
                raise ValueError(f"'limit' must be a positive number, got {value!r}.")
            limit = min(int(value), 1000)
        else:
            filters[key] = value
        i += 2
    return filters, limit, minutes_back


def _sls_value(row: dict, *names: str) -> Any:
    """First non-empty field among *names*; unwraps SLS {'value': …} records."""
    for name in names:
        value = row.get(name)
        if isinstance(value, dict):
            value = value.get("value")
        if value not in (None, ""):
            return value
    return ""


def _sls_time(row: dict) -> str:
    """Render time_generated (epoch seconds or ISO string) as readable UTC."""
    raw = row.get("time_generated") or row.get("log_time") or row.get("receive_time")
    if isinstance(raw, (int, float)):
        try:
            return datetime.fromtimestamp(raw, tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")
        except (OverflowError, OSError, ValueError):
            return str(raw)
    return str(raw or "")


def _map_sls_row(log_type: str, row: dict) -> dict:
    """Map SLS field names onto the columns fmt.format_logs renders.

    Key order matters: format_logs shows its priority columns (time, severity,
    subtype, description, src, dst, …) plus the first three non-priority keys —
    so app/action/rule are inserted right after dst to land in the table.
    The FULL record stays in _LAST_ROWS for `show log detail <n>`.
    """
    if log_type == "system":
        return {
            "time":        _sls_time(row),
            "severity":    _sls_value(row, "severity", "vendor_severity"),
            "subtype":     _sls_value(row, "sub_type", "subtype"),
            "description": _sls_value(row, "description", "opaque", "message"),
            "object":      _sls_value(row, "object"),
            "module":      _sls_value(row, "module"),
        }
    mapped: dict = {"time": _sls_time(row)}
    if log_type == "threat":
        mapped["severity"] = _sls_value(row, "severity", "vendor_severity")
        mapped["description"] = _sls_value(row, "threat_name", "threat_id", "description")
    mapped.update({
        "src":    _sls_value(row, "source_ip", "src", "src_ip"),
        "dst":    _sls_value(row, "dest_ip", "dst", "dst_ip"),
        "app":    _sls_value(row, "app", "application"),
        "action": _sls_value(row, "action"),
        "rule":   _sls_value(row, "rule_matched", "rule"),
        "port":   _sls_value(row, "dest_port", "dport"),
        "device": _sls_value(row, "device_name", "log_source_name", "serial_number"),
    })
    return mapped


def _show_log_sls(log_type: str):
    """Build the api_handler for one SLS-backed `show log <type>` command."""
    def handler(ctx: ExecutionContext, args: dict) -> Any:
        filters, limit, minutes_back = _parse_log_args(args)
        client = _get_sls(ctx)
        rows = client.query_logs(log_type, filters, limit=limit, minutes_back=minutes_back)

        global _LAST_QUERY_DESC
        with _LAST_ROWS_LOCK:
            _LAST_ROWS[:] = rows
            _LAST_QUERY_DESC = f"{log_type} (last {minutes_back}m)"

        if not rows:
            return (
                f"No {log_type} logs in SLS for the last {minutes_back}m"
                + (f" matching {filters}" if filters else "")
                + ".\n  SLS ingestion lags minutes behind the devices — for "
                  f"real-time output on one device run: show log {log_type} --remote\n"
                  f"  To widen the window: show log {log_type} last 24h"
            )
        mapped = [_map_sls_row(log_type, row) for row in rows]
        # (log_type, rows) tuple → fmt.format_logs(rows, log_type=…) titles the
        # table; the short type string IS the contract (not a descriptive title).
        # Full records: `show log detail <n>`; text filtering: `| match <text>`.
        return log_type, mapped

    handler.__name__ = f"_show_log_{log_type}_sls"
    handler.__doc__ = (
        f"Query {log_type} logs fleet-wide via the Strata Logging Service.\n\n"
        "SLS is fleet-wide but ingestion lags minutes behind; use --remote "
        "for real-time on one device.  Full record: show log detail <n>."
    )
    return handler


def _show_log_detail(ctx: ExecutionContext, args: dict) -> Any:
    """Show the FULL SLS record for row <n> of the last log query.

    Reads from the module-level _LAST_ROWS stash populated by the
    `show log traffic|threat|system` handlers (see comment above).
    """
    with _LAST_ROWS_LOCK:
        rows_snapshot = list(_LAST_ROWS)
        desc_snapshot = _LAST_QUERY_DESC
    if not rows_snapshot:
        raise ValueError(
            "No log rows to detail — run a query first, e.g. "
            "show log traffic last 1h, then: show log detail <n>"
        )
    raw = str(args.get("id", "") or "").strip()
    if not raw.isdigit() or not (1 <= int(raw) <= len(rows_snapshot)):
        raise ValueError(
            f"Usage: show log detail <n>   (1–{len(rows_snapshot)} from the last "
            f"{desc_snapshot or 'log'} query)"
        )
    return rows_snapshot[int(raw) - 1]


# ---------------------------------------------------------------------------
# SSH command builders (used when --remote is appended)
# ---------------------------------------------------------------------------

def _ssh_jobs_id(args: dict) -> str:
    job_id = shlex.quote(str(args.get("id", "")))
    return f"show jobs id {job_id}"


def _ssh_ping(args: dict) -> str:
    host  = shlex.quote(args.get("host", ""))
    count = shlex.quote(str(args.get("count", "5")))
    return f"ping host {host} count {count}"


def _ssh_commit(args: dict) -> str:
    desc = args.get("description", "")
    # Quote the description to prevent injection via special characters.
    return f"commit description {shlex.quote(desc)}" if desc else "commit"


# ---------------------------------------------------------------------------
# Command table — merged into COMMANDS by registry.py
# ---------------------------------------------------------------------------

COMMANDS: dict[str, CommandDef] = {
    "show system info": CommandDef(
        description="Show device info from SCM (model, serial, SW version, IP, status…)",
        category="operations",
        scope="device",
        api_handler=_show_system_info,
        ssh_command="show system info",
        render="device_detail",
        feature_flag="show_system_info",
    ),
    "show system resources": CommandDef(
        description="Show live CPU / memory — use --remote for live device data",
        category="operations",
        scope="device",
        api_handler=_pending_show_system_resources,
        ssh_command="show system resources",
        render="raw",
        feature_flag="show_system_resources",
    ),
    "show system disk-space": CommandDef(
        description="Show live disk usage — use --remote for live device data",
        category="operations",
        scope="device",
        api_handler=_pending_show_system_disk_space,
        ssh_command="show system disk-space",
        render="raw",
        feature_flag="show_system_disk_space",
    ),
    "request system software check": CommandDef(
        description="Check available software updates — use --remote for live data",
        category="operations",
        scope="device",
        api_handler=_pending_request_software_check,
        ssh_command="request system software check",
        render="raw",
        feature_flag="request_system_software",
        usage="request system software check",
    ),
    "show jobs all": CommandDef(
        description="Show all SCM jobs (TSG-wide)",
        category="operations",
        scope="global",
        api_handler=show_handler("get_jobs", folder_scoped=False),
        ssh_command="show jobs all",
        render="jobs",
        feature_flag="show_jobs",
    ),
    "show jobs id": CommandDef(
        description="Show a specific job by ID — show jobs id <n>",
        category="operations",
        scope="global",
        api_handler=_show_jobs_id,
        ssh_command=_ssh_jobs_id,
        render="jobs",
        feature_flag="show_jobs",
    ),
    # Fleet-wide SLS log queries.  SLS is fleet-wide but ingestion lags
    # minutes behind; --remote (kept below) gives real-time on one device.
    "show log system": CommandDef(
        description="Fleet-wide system log via SLS (lags minutes) — --remote for real-time on one device",
        usage="show log system [last <Nm|Nh|Nd>] [limit <n>]",
        category="operations",
        scope="global",
        api_handler=_show_log_sls("system"),
        ssh_command="show log system",
        render="logs",
        feature_flag="sls_logs",
    ),
    "show log traffic": CommandDef(
        description="Fleet-wide traffic log via SLS (lags minutes) — --remote for real-time on one device",
        usage="show log traffic [src <ip>] [dst <ip>] [port <n>] [rule <name>] [app <name>] [last <Nm|Nh|Nd>] [limit <n>]",
        category="operations",
        scope="global",
        api_handler=_show_log_sls("traffic"),
        ssh_command="show log traffic",
        render="logs",
        feature_flag="sls_logs",
    ),
    "show log threat": CommandDef(
        description="Fleet-wide threat log via SLS (lags minutes) — --remote for real-time on one device",
        usage="show log threat [src <ip>] [dst <ip>] [port <n>] [rule <name>] [app <name>] [last <Nm|Nh|Nd>] [limit <n>]",
        category="operations",
        scope="global",
        api_handler=_show_log_sls("threat"),
        ssh_command="show log threat",
        render="logs",
        feature_flag="sls_logs",
    ),
    "show log detail": CommandDef(
        description="Show the full SLS record for row <n> of the last log query (1 = top row)",
        usage="show log detail <n>",
        category="operations",
        scope="global",
        api_handler=_show_log_detail,
        ssh_command=None,   # API-only — detail reads the last SLS result set
        render="dict",
        feature_flag="sls_logs",
    ),
    "ping host": CommandDef(
        description="Ping a host from the device — ping host <ip>  (use --remote)",
        category="operations",
        scope="device",
        api_handler=_pending_ping,
        ssh_command=_ssh_ping,
        render="raw",
        feature_flag="ping",
    ),
    "commit": CommandDef(
        description="Apply staged changes and push to devices — commit [watch] [description <text>]",
        category="operations",
        scope="folder",
        # In configure mode the shell intercepts `commit` and runs the staged-
        # change replay + push (ConfigureMixin._cmd_commit_staged); this handler
        # covers `commit --remote` (SSH) and any direct API use.
        api_handler=_commit,
        ssh_command=_ssh_commit,
        render="jobs",
        # Intentionally NOT feature-gated: an operator in configure mode must
        # always be able to commit (or abandon) their staged changes.
    ),
}


# ---------------------------------------------------------------------------
# Additional handlers — system request operations (SSH / --remote)
# ---------------------------------------------------------------------------

def _request_system_reboot(ctx: ExecutionContext, args: dict) -> Any:
    """Request a system reboot — use --remote.  Requires active device context.

    SAFETY: This will reboot the physical firewall.  Always confirm before executing.
    """
    from app.commands.base import require_device
    device = require_device(ctx)
    name   = device.get("hostname") or device.get("name") or "device"
    return (
        f"[bold red]SAFETY CHECK[/bold red]: This will reboot {name}.\n"
        f"  Run:  request system reboot --remote  to execute on {name}.\n"
        f"  The device will be unavailable for ~2-5 minutes."
    )


def _request_system_shutdown(ctx: ExecutionContext, args: dict) -> Any:
    """Request a system shutdown — use --remote.  Requires active device context."""
    from app.commands.base import require_device
    device = require_device(ctx)
    name   = device.get("hostname") or device.get("name") or "device"
    return (
        f"[bold red]SAFETY CHECK[/bold red]: This will shut down {name}.\n"
        f"  Run:  request system shutdown --remote  to execute on {name}.\n"
        f"  The device will be offline until manually powered on."
    )


_EXTRA_COMMANDS: dict[str, CommandDef] = {
    "request system reboot": CommandDef(
        description="Reboot a managed device — use --remote  (CAUTION: device will restart)",
        category="operations",
        scope="device",
        api_handler=_request_system_reboot,
        ssh_command="request system reboot",
        render="raw",
        feature_flag="request_system_reboot",
        usage="request system reboot",
    ),
    "request system shutdown": CommandDef(
        description="Shut down a managed device — use --remote  (CAUTION: device will go offline)",
        category="operations",
        scope="device",
        api_handler=_request_system_shutdown,
        ssh_command="request system shutdown",
        render="raw",
        feature_flag="request_system_reboot",
        usage="request system shutdown",
    ),
    "clear session all": CommandDef(
        description="Clear all active sessions on the device — use --remote  (CAUTION: terminates all sessions)",
        category="operations",
        scope="device",
        api_handler=_clear_session_all,
        ssh_command="clear session all",
        render="raw",
        feature_flag="show_session",
        usage="clear session all",
    ),
    "clear session id": CommandDef(
        description="Clear a specific session by ID — use --remote",
        category="operations",
        scope="device",
        api_handler=_clear_session_id,
        ssh_command=_ssh_clear_session_id,
        render="raw",
        feature_flag="show_session",
        usage="clear session id <session-id>",
    ),
}

COMMANDS.update(_EXTRA_COMMANDS)

