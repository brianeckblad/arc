"""Operations commands (jobs, commit, system info, logs). See docs/commands/ and docs/scm-api/specs/operations*.md for details."""

from __future__ import annotations

from typing import Any

from app.commands.base import CommandDef, ExecutionContext, require_device, require_scm


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


def _show_jobs_all(ctx: ExecutionContext, args: dict) -> list[dict]:
    """Fetch all SCM jobs — TSG-wide, no folder scope required."""
    scm = require_scm(ctx)
    return scm.get_jobs()


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


def _pending_show_system_resources(ctx: ExecutionContext, args: dict) -> str:
    return _live_only("show system resources")


def _pending_show_system_disk_space(ctx: ExecutionContext, args: dict) -> str:
    return _live_only("show system disk-space")


def _pending_request_software_check(ctx: ExecutionContext, args: dict) -> str:
    return _live_only("request system software check")


def _pending_show_log_system(ctx: ExecutionContext, args: dict) -> str:
    return _live_only("show log system")


def _pending_show_log_traffic(ctx: ExecutionContext, args: dict) -> str:
    return _live_only("show log traffic")


def _pending_ping(ctx: ExecutionContext, args: dict) -> str:
    if not args.get("host"):
        raise RuntimeError("Usage: ping host <ip>")
    return _live_only("ping host")


# ---------------------------------------------------------------------------
# SSH command builders (used when --remote is appended)
# ---------------------------------------------------------------------------

def _ssh_jobs_id(args: dict) -> str:
    return f"show jobs id {args.get('id', '')}"


def _ssh_ping(args: dict) -> str:
    host  = args.get("host", "")
    count = args.get("count", "5")
    return f"ping host {host} count {count}"


def _ssh_commit(args: dict) -> str:
    desc = args.get("description", "")
    return f'commit description "{desc}"' if desc else "commit"


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
    ),
    "show jobs all": CommandDef(
        description="Show all SCM jobs (TSG-wide)",
        category="operations",
        scope="global",
        api_handler=_show_jobs_all,
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
    "show log system": CommandDef(
        description="Show live system log — use --remote for live device data",
        category="operations",
        scope="device",
        api_handler=_pending_show_log_system,
        ssh_command="show log system",
        render="raw",
        feature_flag="show_log_system",
    ),
    "show log traffic": CommandDef(
        description="Show live traffic log — use --remote for live device data",
        category="operations",
        scope="device",
        api_handler=_pending_show_log_traffic,
        ssh_command="show log traffic",
        render="raw",
        feature_flag="show_log_traffic",
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
        description="Push candidate config to managed devices — commit [description <text>]",
        category="operations",
        scope="folder",
        api_handler=_commit,
        ssh_command=_ssh_commit,
        render="jobs",
        feature_flag="commit",
    ),
}

