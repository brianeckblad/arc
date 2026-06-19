"""Packet Tracer — Cisco-ASA-style security policy simulation.

ARC fetches the security rule base for the **active folder** from SCM and
evaluates a synthetic packet against the rules top-down, reporting which rule
the packet would hit and the resulting action — without needing a live device.

This works wherever you are in the tree: the rules evaluated are those of the
currently-selected folder (``cd folder <name>``).

Two command names map here (same handler):
  packet-tracer ...                 (Cisco-ASA style name)
  test security-policy-match ...    (PAN-OS operational style name)

Both accept PAN-OS-style keyword arguments:
  from <zone> to <zone> source <ip> destination <ip>
  [application <app>] [destination-port <n>] [protocol <n>] [source-user <user>]

Example:
  packet-tracer from trust to untrust source 10.0.0.5 destination 8.8.8.8 \
                application dns destination-port 53 protocol 17

Matching is intentionally honest about its limits (see MVP NOTES below) so the
output never implies more certainty than the data supports.
"""

from __future__ import annotations

from typing import Any

from app.commands.base import CommandDef, ExecutionContext, require_scm

# ── MVP NOTES ────────────────────────────────────────────────────────────────
# Implemented now (folder rule base, in order):
#   - disabled rules skipped
#   - from / to zone match  (value, 'any', or empty = any)
#   - source / destination match  (literal value, 'any', or empty = any) with
#     negate_source / negate_destination honoured
#   - application match  (value, 'any', or empty = any)
#   - first matching rule wins; action reported (allow / deny / drop / reset*)
#   - no match → PAN-OS default: intrazone-allow when from==to, else interzone-deny
# Documented future enhancements (do not silently fake these):
#   - resolve address objects / groups to CIDRs and do subnet containment
#   - resolve service objects to ports and do strict port/protocol matching
#   - application-default service semantics, app dependencies, URL category


_ANY = {"any", ""}


def _field(rule: dict, key: str) -> list[str]:
    """Return a rule field as a lowercased string list (handles str or list)."""
    val = rule.get(key)
    if val is None:
        return []
    if isinstance(val, str):
        val = [val]
    return [str(v).lower() for v in val]


def _zone_ok(pkt_zone: str, rule_zones: list[str]) -> bool:
    if not pkt_zone:
        return True  # unspecified packet zone → don't constrain
    if not rule_zones or "any" in rule_zones:
        return True
    return pkt_zone.lower() in rule_zones


def _addr_ok(pkt_ip: str, rule_addrs: list[str], negate: bool) -> bool:
    if not pkt_ip:
        return True
    if not rule_addrs or "any" in rule_addrs:
        base = True
    else:
        # MVP: literal value match only (object/CIDR resolution is future work).
        base = pkt_ip.lower() in rule_addrs
    return (not base) if negate else base


def _app_ok(pkt_app: str, rule_apps: list[str]) -> bool:
    if not pkt_app:
        return True
    if not rule_apps or "any" in rule_apps:
        return True
    return pkt_app.lower() in rule_apps


def _evaluate(packet: dict, rules: list[dict]) -> tuple[dict | None, int]:
    """Return (matching_rule, index) or (None, -1) for the first matching rule."""
    for idx, rule in enumerate(rules):
        if rule.get("disabled") in (True, "yes", "true"):
            continue
        if not _zone_ok(packet["from"], _field(rule, "from")):
            continue
        if not _zone_ok(packet["to"], _field(rule, "to")):
            continue
        if not _addr_ok(packet["source"], _field(rule, "source"),
                        bool(rule.get("negate_source"))):
            continue
        if not _addr_ok(packet["destination"], _field(rule, "destination"),
                        bool(rule.get("negate_destination"))):
            continue
        if not _app_ok(packet["application"], _field(rule, "application")):
            continue
        return rule, idx
    return None, -1


def _packet_tracer(ctx: ExecutionContext, args: dict) -> Any:
    """Simulate a packet against the active folder's security rule base."""
    scm = require_scm(ctx)

    packet = {
        "from":        (args.get("from") or "").strip(),
        "to":          (args.get("to") or "").strip(),
        "source":      (args.get("source") or "").strip(),
        "destination": (args.get("destination") or "").strip(),
        "application": (args.get("application") or "").strip(),
        "port":        (args.get("destination-port") or "").strip(),
        "protocol":    (args.get("protocol") or "").strip(),
        "user":        (args.get("source-user") or "").strip(),
    }

    if not packet["source"] or not packet["destination"]:
        raise RuntimeError(
            "Usage: packet-tracer from <zone> to <zone> source <ip> destination <ip> "
            "[application <app>] [destination-port <n>] [protocol <n>]\n"
            "  At minimum, source and destination are required."
        )

    rules = scm.get_security_policy(folder=ctx.folder)

    # Build the ASA-style report.
    lines: list[str] = []
    lines.append(f"[bold]Packet Tracer[/bold]  [dim]— folder: {ctx.folder}[/dim]")
    inp = (
        f"from={packet['from'] or 'any'} to={packet['to'] or 'any'} "
        f"src={packet['source']} dst={packet['destination']} "
        f"app={packet['application'] or 'any'} "
        f"port={packet['port'] or 'any'}/{packet['protocol'] or 'any'}"
    )
    lines.append(f"  [dim]Input:[/dim] {inp}")
    lines.append(f"  [dim]Rules evaluated: {len(rules)}[/dim]")
    lines.append("  " + "─" * 60)

    matched, idx = _evaluate(packet, rules)

    if matched:
        action = str(matched.get("action", "")).lower()
        verdict = {
            "allow": "[green]ALLOW[/green]",
            "deny":  "[red]DENY[/red]",
            "drop":  "[red]DROP[/red]",
            "reset-client": "[red]RESET[/red]",
            "reset-server": "[red]RESET[/red]",
            "reset-both":   "[red]RESET[/red]",
        }.get(action, f"[yellow]{action or 'unknown'}[/yellow]")
        lines.append("  [bold]Phase 1: SECURITY POLICY LOOKUP[/bold]")
        lines.append(f"    Matched rule : [bold]{matched.get('name', '?')}[/bold]  (#{idx + 1} of {len(rules)})")
        lines.append(f"    Action       : {verdict}")
        lines.append(f"    From → To    : {', '.join(_field(matched, 'from')) or 'any'} → "
                     f"{', '.join(_field(matched, 'to')) or 'any'}")
        lines.append(f"    Application  : {', '.join(_field(matched, 'application')) or 'any'}")
        svc = ', '.join(_field(matched, 'service')) or 'any'
        lines.append(f"    Service      : {svc}")
        lines.append("  " + "─" * 60)
        lines.append(f"  [bold]RESULT:[/bold] {verdict} — matched [bold]{matched.get('name', '?')}[/bold]")
    else:
        # PAN-OS implicit defaults at the bottom of every rule base.
        same_zone = packet["from"] and packet["from"].lower() == packet["to"].lower()
        if same_zone:
            lines.append("  [bold]RESULT:[/bold] [green]ALLOW[/green] — no explicit rule; "
                         "implicit intrazone-default (allow)")
        else:
            lines.append("  [bold]RESULT:[/bold] [red]DENY[/red] — no explicit rule; "
                         "implicit interzone-default (deny)")

    lines.append("  [dim]Note: matching uses literal zone/address/app values from the "
                 "folder rule base.[/dim]")
    lines.append("  [dim]Address-object/service resolution to CIDRs & ports is a planned "
                 "enhancement.[/dim]")
    return "\n".join(lines)


def _ssh_packet_tracer(args: dict) -> str:
    """PAN-OS operational command for --remote execution on a live device."""
    parts = ["test", "security-policy-match"]
    for key in ("from", "to", "source", "destination", "application",
                "destination-port", "protocol", "source-user"):
        val = args.get(key)
        if val:
            parts += [key, str(val)]
    return " ".join(parts)


# ---------------------------------------------------------------------------
# Command table — merged into COMMANDS by registry.py
# ---------------------------------------------------------------------------

COMMANDS: dict[str, CommandDef] = {
    "packet-tracer": CommandDef(
        description=(
            "Trace a packet through the folder's security rule base — "
            "packet-tracer from <zone> to <zone> source <ip> destination <ip> "
            "[application <app>] [destination-port <n>] [protocol <n>]"
        ),
        category="diagnostics",
        scope="folder",
        api_handler=_packet_tracer,
        ssh_command=_ssh_packet_tracer,
        render="raw",
        feature_flag="test_security_policy_match",
    ),
    "test security-policy-match": CommandDef(
        description=(
            "Test which security rule a packet matches (alias of packet-tracer) — "
            "test security-policy-match source <ip> destination <ip> "
            "[from <zone>] [to <zone>] [application <app>] [destination-port <n>]"
        ),
        category="diagnostics",
        scope="folder",
        api_handler=_packet_tracer,
        ssh_command=_ssh_packet_tracer,
        render="raw",
        feature_flag="test_security_policy_match",
    ),
}

