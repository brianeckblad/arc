"""Command registry — maps PAN-OS-style CLI commands to SCM API handlers and SSH equivalents.

ARC integrates with SCM for API mode. The command vocabulary intentionally
resembles operational firewall commands, and API-mode implementations are SCM
REST translations. Commands that are not translated to SCM yet raise an
explicit message and can be run through SSH with `--remote`, `remote`, or
`connect` when an SSH equivalent exists.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Callable, Optional

if TYPE_CHECKING:
    from app.api.client import SCMClient
    from app.config import ArcConfig
    from app.ssh.manager import SSHManager


@dataclass
class ExecutionContext:
    """Passed to every api_handler so it can access state and clients."""

    scm: Optional["SCMClient"] = None
    ssh: Optional["SSHManager"] = None
    config: Optional["ArcConfig"] = None
    device: Optional[dict] = None
    folder: str = "Shared"
    tsg_id: str = ""

    @property
    def target(self) -> Optional[str]:
        """Selected device serial, when known."""
        return self.device.get("serial") if self.device else None

    @property
    def device_host(self) -> Optional[str]:
        """IP / hostname of the selected device for SSH."""
        if not self.device:
            return None
        return self.device.get("ip_address") or self.device.get("hostname") or None


@dataclass
class CommandDef:
    description: str
    category: str
    api_handler: Optional[Callable] = None
    ssh_command: str | Callable[[dict], str] | None = None
    render: str = ""


def _require_scm(ctx: ExecutionContext) -> "SCMClient":
    if not ctx.scm:
        raise RuntimeError(
            "SCM is not configured. Set SCM_BEARER_TOKEN, or set "
            "SCM_CLIENT_ID / SCM_CLIENT_SECRET / SCM_TSG_ID and restart."
        )
    return ctx.scm


def _translation_pending(command: str) -> str:
    return (
        f"SCM API translation for '{command}' is not implemented yet. "
        f"Use '{command} --remote' for a one-time SSH run, or use "
        "'remote <device>' / 'connect' for SSH passthrough mode."
    )


# ---------- SCM-backed config/object reads ----------

def _show_security_policy(ctx: ExecutionContext, args: dict) -> Any:
    scm = _require_scm(ctx)
    return scm.get_security_policy(folder=ctx.folder)


def _show_address(ctx: ExecutionContext, args: dict) -> Any:
    scm = _require_scm(ctx)
    return scm.get_addresses(folder=ctx.folder)


def _show_address_group(ctx: ExecutionContext, args: dict) -> Any:
    scm = _require_scm(ctx)
    return scm.get_address_groups(folder=ctx.folder)


def _show_service(ctx: ExecutionContext, args: dict) -> Any:
    scm = _require_scm(ctx)
    return scm.get_services(folder=ctx.folder)


def _show_devices(ctx: ExecutionContext, args: dict) -> Any:
    scm = _require_scm(ctx)
    return scm.get_devices(folder=ctx.folder)


# ---------- PAN-OS command translations pending in SCM ----------

def _pending_show_system_info(ctx: ExecutionContext, args: dict) -> str:
    return _translation_pending("show system info")


def _pending_show_system_resources(ctx: ExecutionContext, args: dict) -> str:
    return _translation_pending("show system resources")


def _pending_show_system_disk_space(ctx: ExecutionContext, args: dict) -> str:
    return _translation_pending("show system disk-space")


def _pending_request_software_check(ctx: ExecutionContext, args: dict) -> str:
    return _translation_pending("request system software check")


def _pending_show_jobs_all(ctx: ExecutionContext, args: dict) -> str:
    return _translation_pending("show jobs all")


def _pending_show_jobs_id(ctx: ExecutionContext, args: dict) -> str:
    return _translation_pending("show jobs id")


def _pending_show_interface_all(ctx: ExecutionContext, args: dict) -> str:
    return _translation_pending("show interface all")


def _pending_show_interface(ctx: ExecutionContext, args: dict) -> str:
    return _translation_pending("show interface")


def _pending_show_routing_route(ctx: ExecutionContext, args: dict) -> str:
    return _translation_pending("show routing route")


def _pending_show_routing_summary(ctx: ExecutionContext, args: dict) -> str:
    return _translation_pending("show routing summary")


def _pending_show_zone(ctx: ExecutionContext, args: dict) -> str:
    return _translation_pending("show zone")


def _pending_show_ha_all(ctx: ExecutionContext, args: dict) -> str:
    return _translation_pending("show high-availability all")


def _pending_show_ha_state(ctx: ExecutionContext, args: dict) -> str:
    return _translation_pending("show high-availability state")


def _pending_show_log_system(ctx: ExecutionContext, args: dict) -> str:
    return _translation_pending("show log system")


def _pending_show_log_traffic(ctx: ExecutionContext, args: dict) -> str:
    return _translation_pending("show log traffic")


def _pending_ping(ctx: ExecutionContext, args: dict) -> str:
    if not args.get("host"):
        raise RuntimeError("Usage: ping host <ip>")
    return _translation_pending("ping host")


def _pending_test_security_policy_match(ctx: ExecutionContext, args: dict) -> str:
    if not args.get("source") or not args.get("destination"):
        raise RuntimeError(
            "Usage: test security-policy-match source <ip> destination <ip> "
            "[application <app>] [protocol <n>] [destination-port <n>]"
        )
    return _translation_pending("test security-policy-match")


def _pending_commit(ctx: ExecutionContext, args: dict) -> str:
    return _translation_pending("commit")


# ---------------------------------------------------------------------------
# SSH command builders
# ---------------------------------------------------------------------------

def _ssh_ping(args: dict) -> str:
    host = args.get("host", "")
    count = args.get("count", "5")
    return f"ping host {host} count {count}"


def _ssh_test_spm(args: dict) -> str:
    src = args.get("source", "")
    dst = args.get("destination", "")
    app = args.get("application", "any")
    proto = args.get("protocol", "6")
    dport = args.get("destination-port", "80")
    return (
        f"test security-policy-match source {src} destination {dst} "
        f"application {app} protocol {proto} destination-port {dport}"
    )


def _ssh_commit(args: dict) -> str:
    desc = args.get("description", "")
    return f'commit description "{desc}"' if desc else "commit"


COMMANDS: dict[str, CommandDef] = {
    "show system info": CommandDef(
        description="Show system information (hostname, model, SW version, uptime...)",
        category="system",
        api_handler=_pending_show_system_info,
        ssh_command="show system info",
        render="raw",
    ),
    "show system resources": CommandDef(
        description="Show system CPU / memory resources",
        category="system",
        api_handler=_pending_show_system_resources,
        ssh_command="show system resources",
        render="raw",
    ),
    "show system disk-space": CommandDef(
        description="Show disk space usage",
        category="system",
        api_handler=_pending_show_system_disk_space,
        ssh_command="show system disk-space",
        render="raw",
    ),
    "request system software check": CommandDef(
        description="Check for available software updates",
        category="system",
        api_handler=_pending_request_software_check,
        ssh_command="request system software check",
        render="raw",
    ),
    "show jobs all": CommandDef(
        description="Show all jobs",
        category="system",
        api_handler=_pending_show_jobs_all,
        ssh_command="show jobs all",
        render="raw",
    ),
    "show jobs id": CommandDef(
        description="Show a specific job by ID",
        category="system",
        api_handler=_pending_show_jobs_id,
        ssh_command=lambda args: f"show jobs id {args.get('id', '')}",
        render="raw",
    ),
    "show interface all": CommandDef(
        description="Show all interfaces",
        category="network",
        api_handler=_pending_show_interface_all,
        ssh_command="show interface all",
        render="raw",
    ),
    "show interface": CommandDef(
        description="Show a specific interface — show interface <name>",
        category="network",
        api_handler=_pending_show_interface,
        ssh_command=lambda args: f"show interface {args.get('name', 'all')}",
        render="raw",
    ),
    "show routing route": CommandDef(
        description="Show routing table",
        category="network",
        api_handler=_pending_show_routing_route,
        ssh_command="show routing route",
        render="raw",
    ),
    "show routing summary": CommandDef(
        description="Show routing summary",
        category="network",
        api_handler=_pending_show_routing_summary,
        ssh_command="show routing summary",
        render="raw",
    ),
    "show zone": CommandDef(
        description="Show security zones",
        category="network",
        api_handler=_pending_show_zone,
        ssh_command="show zone",
        render="raw",
    ),
    "show high-availability all": CommandDef(
        description="Show full HA status",
        category="network",
        api_handler=_pending_show_ha_all,
        ssh_command="show high-availability all",
        render="raw",
    ),
    "show high-availability state": CommandDef(
        description="Show HA state",
        category="network",
        api_handler=_pending_show_ha_state,
        ssh_command="show high-availability state",
        render="raw",
    ),
    "show security policy": CommandDef(
        description="Show security policy rules",
        category="policy",
        api_handler=_show_security_policy,
        ssh_command=None,
        render="security_policy",
    ),
    "show address": CommandDef(
        description="Show address objects",
        category="policy",
        api_handler=_show_address,
        ssh_command=None,
        render="address_objects",
    ),
    "show address-group": CommandDef(
        description="Show address groups",
        category="policy",
        api_handler=_show_address_group,
        ssh_command=None,
        render="address_groups",
    ),
    "show service": CommandDef(
        description="Show service objects",
        category="policy",
        api_handler=_show_service,
        ssh_command=None,
        render="services",
    ),
    "show devices": CommandDef(
        description="List all managed devices",
        category="devices",
        api_handler=_show_devices,
        ssh_command=None,
        render="devices",
    ),
    "show log system": CommandDef(
        description="Show system log (last 20 entries)",
        category="logs",
        api_handler=_pending_show_log_system,
        ssh_command="show log system",
        render="raw",
    ),
    "show log traffic": CommandDef(
        description="Show traffic log (last 20 entries)",
        category="logs",
        api_handler=_pending_show_log_traffic,
        ssh_command="show log traffic",
        render="raw",
    ),
    "ping host": CommandDef(
        description="Ping a host — ping host <ip>",
        category="tools",
        api_handler=_pending_ping,
        ssh_command=_ssh_ping,
        render="raw",
    ),
    "test security-policy-match": CommandDef(
        description=(
            "Test security policy match — "
            "test security-policy-match source <ip> destination <ip> "
            "application <app> protocol <n> destination-port <n>"
        ),
        category="tools",
        api_handler=_pending_test_security_policy_match,
        ssh_command=_ssh_test_spm,
        render="raw",
    ),
    "commit": CommandDef(
        description="Commit the candidate configuration — commit [description <text>]",
        category="config",
        api_handler=_pending_commit,
        ssh_command=_ssh_commit,
        render="raw",
    ),
}

SORTED_COMMANDS: list[tuple[str, CommandDef]] = sorted(
    COMMANDS.items(), key=lambda kv: len(kv[0]), reverse=True
)

CATEGORIES: dict[str, list[str]] = {}
for _key, _command in COMMANDS.items():
    CATEGORIES.setdefault(_command.category, []).append(_key)


def match_command(tokens: list[str]) -> tuple[Optional[str], CommandDef, dict]:
    """
    Find the longest command prefix that matches *tokens*.

    Returns (matched_key, CommandDef, leftover_args_dict)
    where leftover_args_dict contains positional/named args after the prefix.
    """
    sentence = " ".join(tokens).lower()
    for key, command_def in SORTED_COMMANDS:
        if sentence == key or sentence.startswith(key + " "):
            remainder = tokens[len(key.split()):]
            args = _parse_args(remainder)
            return key, command_def, args
    return None, None, {}  # type: ignore[return-value]


def _parse_args(tokens: list[str]) -> dict:
    result: dict = {}
    i = 0
    positional = []
    while i < len(tokens):
        token = tokens[i]
        if i + 1 < len(tokens) and not tokens[i + 1].startswith("-"):
            result[token.lstrip("-")] = tokens[i + 1]
            i += 2
        else:
            positional.append(token.lstrip("-"))
            i += 1
    if positional:
        result["_positional"] = positional
        result.setdefault("id", positional[0])
        result.setdefault("name", positional[0])
        result.setdefault("host", positional[0])
    return result

