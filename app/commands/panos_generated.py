"""PAN-OS CLI catalog → feature-gated CommandDefs.

``app/scripts/generate_panos_catalog.py`` scrapes the PAN-OS CLI hierarchy docs into
``app/commands/panos_catalog.py``. This module turns those entries into
commands:

- **op commands** (show/clear/request/test/…): always SSH-capable via
  ``--remote`` (lossless passthrough of whatever the operator typed). When the
  entry carries an ``scm`` mapping, the API path runs a live-device operations
  job over SCM's management tunnel — no SSH, no 2FA. Otherwise the API path
  prints clear ``--remote`` / ``connect`` guidance.
- **config commands** (``set`` hierarchy): break-glass recovery for when SCM
  is down. Flagged off/invisible except the curated recovery family; executed
  over a scripted interactive SSH channel with a drift warning
  (see ExecutionMixin._execute_remote).

Merge order in registry.py: OpenAPI-generated < PAN-OS < curated (curated wins).
"""

from __future__ import annotations

import time
from typing import Any, Callable

from app.commands.base import CommandDef, ExecutionContext, require_device, require_scm

try:
    from app.commands.panos_catalog import PANOS_CATALOG
except ImportError:
    PANOS_CATALOG = []

# Poll a live-device operations job for up to this long (they normally finish
# in a few seconds; the API contract allows slower devices).
_OPS_JOB_TIMEOUT_S = 120
_OPS_JOB_POLL_S = 3


def _device_serial(ctx: ExecutionContext) -> str:
    device = require_device(ctx)
    serial = str(device.get("serial_number") or device.get("serial") or "").strip()
    if not serial.isdigit():
        raise ValueError(
            "This command runs over SCM's device tunnel and needs the device "
            "serial — `cd <device>` to a real inventory entry first."
        )
    return serial


def _run_ops_job(ctx: ExecutionContext, op: str, advanced: bool) -> Any:
    """POST the job, poll to completion, return the inline result data."""
    scm = require_scm(ctx)
    serial = _device_serial(ctx)
    job_id = scm.ops_job_start(op, [serial], advanced=advanced)
    deadline = time.monotonic() + _OPS_JOB_TIMEOUT_S
    job: dict = {}
    while time.monotonic() < deadline:
        job = scm.ops_job_status(job_id)
        state = str(job.get("state", "")).lower()
        if state in ("complete", "failed"):
            break
        time.sleep(_OPS_JOB_POLL_S)
    state = str(job.get("state", "")).lower()
    if state == "failed":
        raise ValueError(f"Device operations job {job_id} failed: {job!r}"[:400])
    if state != "complete":
        raise ValueError(
            f"Device operations job {job_id} still {state or 'pending'} after "
            f"{_OPS_JOB_TIMEOUT_S}s — check later or use --remote."
        )
    results = job.get("results") or []
    for result in results:
        if str(result.get("device", "")) == serial:
            details = result.get("details") or {}
            return details.get("result") or details
    return results


def _make_op_api_handler(entry: dict) -> Callable[[ExecutionContext, dict], Any]:
    """API handler: SCM ops-job when mapped, --remote guidance otherwise."""
    scm_map = entry.get("scm") or {}
    command = entry["key"]

    if scm_map.get("job"):
        op = str(scm_map["job"])
        advanced = bool(scm_map.get("advanced"))

        def _api(ctx: ExecutionContext, args: dict) -> Any:
            del args
            return _run_ops_job(ctx, op, advanced)

        _api.__name__ = "_panos_job_" + op.replace("-", "_")
        return _api

    def _guidance(ctx: ExecutionContext, args: dict) -> str:
        del ctx, args
        return (
            f"'{command}' needs live device access — SCM does not serve this data.\n"
            f"  → Run: [bold]{command} --remote[/bold]  (SSH; one 2FA per device per session)\n"
            f"  → Or:  [bold]connect <device>[/bold]  for an interactive session.\n"
            f"  Tip:   [bold]watch 10 {command} --remote[/bold]  re-runs it every 10s."
        )

    _guidance.__name__ = "_panos_live_" + entry["key"].replace(" ", "_").replace("-", "_")
    return _guidance


def _make_config_api_handler(entry: dict) -> Callable[[ExecutionContext, dict], Any]:
    """Config commands never run via API — explain the break-glass path."""
    command = entry["key"]

    def _api(ctx: ExecutionContext, args: dict) -> str:
        del ctx, args
        return (
            f"'{command}' is DEVICE-LOCAL configuration (break-glass recovery).\n"
            f"  → Run: [bold]{command} … --remote[/bold]  to apply it on the device via SSH.\n"
            "  [yellow]Warning:[/yellow] device-local changes drift from SCM and may be "
            "overwritten at the next SCM push. Prefer SCM configure mode when SCM is reachable."
        )

    _api.__name__ = "_panos_cfg_" + entry["key"].replace(" ", "_").replace("-", "_")
    return _api


def _make_ssh_command(entry: dict) -> Callable[[dict], str]:
    """Lossless passthrough: emit the stem + exactly what the operator typed."""
    stem = entry["ssh"]

    def _ssh(args: dict) -> str:
        remainder = [str(t) for t in (args.get("_remainder") or [])]
        return f"{stem} {' '.join(remainder)}".strip()

    _ssh.__name__ = "_panos_ssh_" + entry["key"].replace(" ", "_").replace("-", "_")
    return _ssh


def _description(entry: dict) -> str:
    verb = entry.get("verb", "")
    kind = "device-local config (break-glass)" if entry.get("family", "").startswith("config") \
        else "live device data" if not (entry.get("scm") or {}) else "live device data via SCM"
    tail = entry["key"][len(verb):].strip().replace("-", " ") if verb else entry["key"]
    return f"{verb.title()} {tail} — {kind}".strip()


def _build() -> dict[str, CommandDef]:
    commands: dict[str, CommandDef] = {}
    for entry in PANOS_CATALOG:
        if "panorama" in (entry.get("platforms") or []):
            continue  # SCM-managed firewalls only; catalog keeps them for the future
        if entry.get("version_removed"):
            continue  # tombstoned in the PAN-OS version we target
        family = str(entry.get("family") or "misc")
        is_config = family.startswith("config")
        commands[entry["key"]] = CommandDef(
            description=_description(entry),
            category="panos-config" if is_config else "panos-ops",
            scope="device",
            api_handler=_make_config_api_handler(entry) if is_config else _make_op_api_handler(entry),
            ssh_command=_make_ssh_command(entry),
            render="raw" if not (entry.get("scm") or {}) else "",
            feature_flag=f"panos_{family}",
            usage="\n".join(entry.get("usage") or [entry["key"]]),
        )
    return commands


COMMANDS: dict[str, CommandDef] = _build()
