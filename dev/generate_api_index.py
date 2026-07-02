#!/usr/bin/env python3
"""Generate a compact API index from the SCM NGFW OpenAPI YAML specs.

Reads every .yaml in docs/scm-api/specs/ and produces dev/API_INDEX.md —
a one-line-per-resource table that replaces reading individual spec files
(5,000+ lines) when looking up an endpoint.

Usage:
    python dev/generate_api_index.py          # writes dev/API_INDEX.md
    python dev/generate_api_index.py --check  # prints without writing
    python dev/generate_api_index.py --cat network  # one spec only

Requires: PyYAML (already in [dev] extras — uv pip install -e '.[dev]')
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT       = Path(__file__).resolve().parent.parent
SPECS_DIR  = ROOT / "docs" / "scm-api" / "specs"
OUT_FILE   = ROOT / "dev" / "API_INDEX.md"
COMMAND_DOCS_DIR = ROOT / "docs" / "commands"

# ---------------------------------------------------------------------------
# Known ARC CLI commands (from app.commands.registry.COMMANDS).
# Refreshed by running: python dev/generate_api_index.py
# Format: resource-path-fragment → arc command name
# ---------------------------------------------------------------------------
_ARC_COMMANDS: dict[str, str] = {
    "addresses":                "show address",
    "address-groups":           "show address-group",
    "services":                 "show service",
    "tags":                     "show tag",
    "external-dynamic-lists":   "show external-dynamic-list",
    "security-rules":           "show security policy",
    "url-categories":           "show url-categories",
    "ethernet-interfaces":      "show interface all / show interface",
    "aggregate-interfaces":     "show interface all",
    "loopback-interfaces":      "show interface all",
    "zones":                    "show zone",
    "ha":                       "show high-availability all / state",
    "static-routes":            "show routing route",
    "virtual-routers":          "show routing summary",
    "devices":                  "show devices / show device",
    "folders":                  "ls folder / folder create",
    "snippets":                 "show snippet / show snippets",
    "jobs":                     "show jobs all / show jobs id",
    "config-versions":          "commit",
}


def _strip_known_prefixes(path: str) -> str:
    for prefix in (
        "/config/objects/v1",
        "/config/security/v1",
        "/config/setup/v1",
        "/config/network/v1",
        "/config/identity/v1",
        "/config/device/v1",
        "/config/setup/device-onboarding/v1",
        "/config/operations/v1",
        "/operations/v1",
        "/auth/v1",
        "/iam/v1",
        "/tenancy/v1",
        "/subscription/v1",
    ):
        if path.startswith(prefix):
            return path[len(prefix):].lstrip("/")
    return path.lstrip("/")


def _resource_key(path_or_url: str) -> str:
    parsed = urlparse(path_or_url)
    path = parsed.path if parsed.scheme else path_or_url
    resource = _strip_known_prefixes(path)
    resource = resource.split("/{")[0]
    resource = resource.split(":")[0]
    parts = [p for p in resource.split("/") if p and p not in {"operations"}]
    if len(parts) >= 2 and parts[1].lower().startswith("v") and parts[1][1:].replace(".", "").isdigit():
        parts = parts[2:]
    return "/".join(parts)


def _registry_commands() -> dict[str, list[str]]:
    """Return resource path → command names, from the live command sources.

    Primary source is the generated endpoint catalog (every generated command
    knows its method + URL). Doc front-matter supplements it for curated
    commands whose docs declare an ``api:`` field — most commands have no doc
    file at all (help is registry-synthesized), so docs alone are NOT a
    reliable mapping source.
    """
    mapping: dict[str, list[str]] = {}

    try:
        from app.commands.resource_catalog import CATALOG
    except Exception:  # noqa: BLE001
        CATALOG = []
    for entry in CATALOG:
        command = str(entry.get("command") or "").strip()
        url = str(entry.get("base_url") or "") + str(entry.get("path") or "")
        key = _resource_key(url)
        if command and key:
            mapping.setdefault(key, []).append(command)

    try:
        from app.settings.command_help import parse_front_matter
    except Exception:  # noqa: BLE001
        return mapping
    for doc in COMMAND_DOCS_DIR.glob("*.md"):
        meta, _body = parse_front_matter(doc.read_text(encoding="utf-8"))
        command = str(meta.get("command") or "").strip()
        api = str(meta.get("api") or "").strip()
        if not command or not api or api.startswith("("):
            continue
        parts = api.split()
        if len(parts) < 2:
            continue
        key = _resource_key(parts[-1])
        if key and command not in mapping.get(key, []):
            mapping.setdefault(key, []).append(command)
    return mapping

# SSH command vocabulary (PAN-OS operational CLI → for --remote execution)
_SSH_MAP: dict[str, str] = {
    "addresses":                "show objects address",
    "address-groups":           "show objects address-group",
    "services":                 "show objects service",
    "tags":                     "show objects tag",
    "security-rules":           "show security policy",
    "url-categories":           "show security url-filtering",
    "ethernet-interfaces":      "show interface <name>",
    "aggregate-interfaces":     "show interface <name>",
    "loopback-interfaces":      "show interface <name>",
    "zones":                    "show zone <name>",
    "nat-rules":                "show running nat-policy",
    "pbf-rules":                "show pbf rule all",
    "static-routes":            "show routing route",
    "virtual-routers":          "show routing summary",
    "bgp-peers":                "show routing protocol bgp peer",
    "bgp-address-family-profiles": "show routing protocol bgp summary",
    "ike-gateways":             "show vpn ike-sa",
    "ipsec-tunnels":            "show vpn ipsec-sa",
    "sdwan-rules":              "show sdwan traffic",
    "dhcp-interfaces":          "show dhcp server lease interface <name>",
    "dns-proxies":              "show dns-proxy dns-signature statistics",
    "logical-routers":          "show routing summary",
    "devices":                  "show system info",
    "jobs":                     "show jobs processed",
}


def _methods_str(methods: set[str]) -> str:
    """Return compact method indicator: C=POST R=GET-id U=PUT D=DELETE L=GET-list."""
    parts = []
    if "list" in methods:    parts.append("L")
    if "get" in methods:     parts.append("R")
    if "post" in methods:    parts.append("C")
    if "put" in methods:     parts.append("U")
    if "delete" in methods:  parts.append("D")
    return "".join(parts) or "?"


def _parse_spec(yaml_path: Path) -> dict:
    """Parse one YAML spec and return a summary dict."""
    try:
        import yaml
    except ImportError:
        print("PyYAML not found. Install with: uv pip install -e '.[dev]'", file=sys.stderr)
        sys.exit(1)

    with open(yaml_path, encoding="utf-8") as f:
        spec = yaml.safe_load(f)

    base_url = ""
    servers = spec.get("servers", [])
    if servers:
        base_url = servers[0].get("url", "")

    title = spec.get("info", {}).get("title", yaml_path.stem)

    # Collect paths → methods, group by resource (strip /{id} and action suffixes)
    resources: dict[str, set[str]] = {}
    for path, path_item in (spec.get("paths") or {}).items():
        # Strip /{id} and :{action} to get the base resource name
        resource = path.lstrip("/")
        resource = resource.split("/{")[0]   # strip /{id} suffix
        resource = resource.split(":")[0]    # strip :action suffix (e.g. :move)

        if resource not in resources:
            resources[resource] = set()

        for method in path_item:
            if method.lower() in ("get", "post", "put", "delete", "patch"):
                # Distinguish list GET vs single-item GET
                if method.lower() == "get":
                    if "/{" in path:
                        resources[resource].add("get")
                    else:
                        resources[resource].add("list")
                else:
                    resources[resource].add(method.lower())

    return {
        "title":     title,
        "base_url":  base_url,
        "yaml_file": yaml_path.name,
        "resources": resources,
    }


def _build_index(specs: list[dict]) -> str:
    """Build the compact markdown index."""
    doc_commands = _registry_commands()
    lines: list[str] = [
        "# ARC API Index — Compact Endpoint Reference",
        "<!--",
        "  Generated by dev/generate_api_index.py — do NOT edit by hand.",
        "  Refresh with: python dev/generate_api_index.py",
        "",
        "  TOKEN-SAVER: Read this instead of docs/scm-api/specs/*.md when looking up an endpoint.",
        "  Full spec files are 1,000-20,000 lines. This index is ~200 lines covering all endpoints.",
        "",
        "  Methods key:  L=List(GET)  R=GetById(GET)  C=Create(POST)  U=Update(PUT)  D=Delete",
        "  ARC col:      ✓ = implemented command  |  — = not yet in ARC registry",
        "  SSH col:      PAN-OS operational CLI equivalent for --remote execution",
        "-->",
        "",
    ]

    for spec in specs:
        base    = spec["base_url"]
        title   = spec["title"]
        yaml_f  = spec["yaml_file"]
        resources = spec["resources"]

        if not resources:
            continue

        lines.append(f"## {title}")
        lines.append(f"**Base:** `{base}`  |  **Spec:** `docs/scm-api/specs/{yaml_f}`")
        lines.append("")
        lines.append(f"{'Resource':<45} {'Methods':<8} {'ARC Command':<42} SSH Command")
        lines.append(f"{'─'*45} {'─'*8} {'─'*42} {'─'*35}")

        for resource, methods in sorted(resources.items()):
            methods_str = _methods_str(methods)

            # Look up ARC implementation from generated command docs first,
            # then fall back to the small hand-written legacy map.
            arc_cmd = "—"
            resource_key = _resource_key(resource)
            if resource_key in doc_commands:
                commands = sorted(set(doc_commands[resource_key]))
                arc_cmd = "✓ " + " / ".join(commands[:3])
                if len(commands) > 3:
                    arc_cmd += f" / +{len(commands) - 3} more"

            for key, cmd in _ARC_COMMANDS.items():
                if arc_cmd == "—" and key in resource:
                    arc_cmd = f"✓ {cmd}"
                    break

            # Look up SSH command
            ssh_cmd = "—"
            for key, cmd in _SSH_MAP.items():
                if key in resource:
                    ssh_cmd = cmd
                    break

            lines.append(
                f"  {resource:<43} {methods_str:<8} {arc_cmd:<42} {ssh_cmd}"
            )

        lines.append("")

    # Keyword vocabulary section
    lines += [
        "---",
        "",
        "## Keyword Vocabulary — Intent → Implementation Recipe",
        "",
        "Use these keywords when requesting features so the agent instantly knows",
        "the module, scope, and pattern without reading AGENTS.md.",
        "",
        "| Keyword | Module | Scope | Guard | Pattern |",
        "|---------|--------|-------|-------|---------|",
        "| `scm command` | any commands/ | `folder` or `global` | `require_scm(ctx)` | api_handler + SSH fallback |",
        "| `config mode` | any | any | `configure_mode` check in `_dispatch()` | write ops only in configure |",
        "| `device command` | operations.py | `device` | `require_device(ctx)` | scope='device', needs `cd <device>` |",
        "| `folder command` | any | `folder` | `ctx.folder` passed to SCM | default for config/policy/objects |",
        "| `global command` | setup.py / operations.py | `global` | none | TSG-wide; no folder filter |",
        "| `ssh command` | operations.py | `device` | `require_device(ctx)` | ssh_command= key; --remote flag |",
        "| `show X` | network/objects/security/setup | `folder` | `require_scm` | GET list endpoint |",
        "| `show X <name>` | same | `folder` | `require_scm` | GET list + filter by name client-side |",
        "| `create X` | same | `folder` | configure mode + `require_scm` | POST endpoint |",
        "| `delete X` | same | `folder` | configure mode + `require_scm` | DELETE endpoint |",
        "| `commit` | operations.py | `global` | configure mode | POST /config-versions/candidate:push |",
        "| `ping` | operations.py | `device` | `require_device` | ssh_command only — live device state |",
        "| `show log` | operations.py | `device` | `require_device` | ssh_command only — live device state |",
        "",
        "---",
        "",
        "## Render Keys (ArcShell._render() dispatch)",
        "",
        "| Key | What it renders | Use for |",
        "|-----|----------------|---------|",
        "| `list` | Rich Table, one row per item, columns from dict keys | any GET-list response |",
        "| `raw` | prints string/dict as-is via Rich | raw SSH output, misc |",
        "| `panel` | Rich Panel with key-value pairs | single-item detail |",
        "| `table` | same as list | alias |",
        "| `tree` | Rich Tree | hierarchical data (folder tree) |",
        "| `jobs` | specialized jobs table | show jobs all/id |",
        "| `policy` | multi-column security policy table | show security policy |",
        "",
        "---",
        "",
        "## Fast Lookup: 'I want to add show X' — 30-second recipe",
        "",
        "1. Find `X` in the resource column above → note the base URL and `Methods` column",
        "2. `python dev/scaffold.py \"show X\" <module>`",
        "3. In the generated handler, call `scm.get_X(folder=ctx.folder)` — add that method to `app/api/client.py` if missing",
        "4. `python dev/smoke_test.py --only 1,2,3`",
        "",
        "**If no SCM endpoint exists** for a live-device concept (arp, bgp neighbors, VPN tunnel status):",
        "- `scope='device'`, `api_handler=` returns a 'use --remote' message, `ssh_command=` is the PAN-OS CLI string",
        "- See the SSH Command column above for the PAN-OS equivalent",
    ]

    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check",  action="store_true", help="Print without writing")
    parser.add_argument("--cat",    default=None, help="Only process specs matching this name fragment")
    args = parser.parse_args()

    yaml_files = sorted(SPECS_DIR.glob("*.yaml"))
    if not yaml_files:
        print(f"No YAML files found in {SPECS_DIR}", file=sys.stderr)
        return 1

    if args.cat:
        yaml_files = [f for f in yaml_files if args.cat.lower() in f.stem.lower()]
        if not yaml_files:
            print(f"No spec files matching '{args.cat}'", file=sys.stderr)
            return 1

    specs = []
    for yaml_path in yaml_files:
        print(f"  parsing {yaml_path.name} ...", file=sys.stderr)
        try:
            specs.append(_parse_spec(yaml_path))
        except Exception as exc:
            print(f"  [skip] {yaml_path.name}: {exc}", file=sys.stderr)

    content = _build_index(specs)

    if args.check:
        print(content)
        return 0

    OUT_FILE.write_text(content, encoding="utf-8")
    lines = content.count("\n")
    print(f"Wrote {OUT_FILE.relative_to(ROOT)}  ({lines} lines)", file=sys.stderr)
    print(f"Replaces ~{len(list(SPECS_DIR.glob('*.md'))) * 300} lines of spec reading", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())

