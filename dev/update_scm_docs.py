#!/usr/bin/env python3
"""Update ARC's local SCM API reference from pan.dev.

This is the engine behind the `docsupdate` agent trigger.  It pulls the
authoritative Palo Alto Networks Strata Cloud Manager (SCM) documentation for
the **NGFW Configuration** components directly from the public pan.dev GitHub
repository, then regenerates ARC's local reference set under ``docs/scm-api/``.

Two kinds of content are pulled:

* **OpenAPI specs** (``docs/scm-api/specs/``) — one per NGFW config domain.
  For each: ``<category>.yaml`` (raw spec) and ``<category>.md`` (a consolidated,
  terminal-friendly endpoint listing: method + path, summary, operation id,
  tags, response codes).
* **Guide docs** (``docs/scm-api/guides/``) — the conceptual SCM documentation
  from https://pan.dev/scm/docs/ (getting started, access tokens, service
  accounts, roles, scope, platform configuration, …) copied as-is.

It also writes:

* ``docs/scm-api/index.md``    — index of specs + guides with the pull date.
* ``docs/scm-api/MANIFEST.md`` — source URL, version, and ``servers[0].url``
  base URL for every spec.  This is the source of truth the agent gateway map
  mirrors.

Design notes (read before editing):

* Raw downloads use only the Python standard library (``urllib``) so the
  archive always refreshes even if optional parsing tools are missing.
* Markdown/manifest generation needs PyYAML.  Install dev extras first:
  ``uv pip install -e '.[dev]'`` (or ``pip install pyyaml``).  If PyYAML is
  missing, raw specs + guides are still saved and the script prints a hint.
* Spec file names on pan.dev carry dated suffixes (e.g.
  ``security-services-R2-2026.yaml``).  ``SPECS`` below pins the current file
  for each category — update an entry when pan.dev publishes a renamed spec.
  Run with ``--list-remote`` to see the live spec tree.

Usage::

    python dev/update_scm_docs.py               # refresh specs + guides
    python dev/update_scm_docs.py --list-remote  # print live SCM spec paths
    python dev/update_scm_docs.py --check        # report drift, write nothing
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

# ── Constants ────────────────────────────────────────────────────────────────

REPO = "PaloAltoNetworks/pan.dev"
RAW_BASE = f"https://raw.githubusercontent.com/{REPO}/master"
TREE_API = f"https://api.github.com/repos/{REPO}/git/trees/master?recursive=1"
SPEC_PREFIX = "openapi-specs/scm/"
HTTP_TIMEOUT = 30  # seconds — every network call is bounded

# Output layout: ARC's local SCM reference set lives in docs/ so it ships with
# the app (not in a scratch folder).  specs/ holds OpenAPI references; guides/
# holds the conceptual pan.dev docs.
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "docs" / "scm-api"
SPECS_DIR = OUTPUT_DIR / "specs"
GUIDES_DIR = OUTPUT_DIR / "guides"

# Category → pan.dev spec path (relative to the repo root).
#
# These are the NGFW configuration domains ARC speaks to.  Each maps one ARC
# command module to one SCM API domain (see the command-module layout in the
# agent instructions).  Update a value here when pan.dev renames a spec file;
# `--list-remote` prints the current tree to copy from.
SPECS: dict[str, str] = {
    "ngfw-objects": "openapi-specs/scm/config/ngfw/objects/objects_v1.3_feb.yaml",
    "ngfw-security": "openapi-specs/scm/config/ngfw/security/security-services-R2-2026.yaml",
    "ngfw-setup": "openapi-specs/scm/config/ngfw/setup/config-setup-feb-v1.yaml",
    "ngfw-network": "openapi-specs/scm/config/ngfw/network/network-services-R2-2026.yaml",
    "ngfw-operations": "openapi-specs/scm/config/ngfw/operations/config-operations-march.yaml",
    "ngfw-operations-config": "openapi-specs/scm/config/ngfw-operations/operations-R2-2026.yaml",
    "ngfw-device": "openapi-specs/scm/config/ngfw/device/device-settings_April.yaml",
    "ngfw-identity": "openapi-specs/scm/config/ngfw/identity/identity-services-march.yaml",
    "ngfw-device-onboarding": (
        "openapi-specs/scm/config/ngfw/setup/device-onboarding/device-onboarding-updated.yaml"
    ),
    # Supporting gateways ARC also calls (auth, tenancy, service accounts).
    "auth": "openapi-specs/scm/auth/AuthService.yaml",
    "tenancy": "openapi-specs/scm/tenancy/TenantServiceGroup.yaml",
    "iam-service-accounts": "openapi-specs/scm/iam/ServiceAccounts.yaml",
}

# Guide name → pan.dev conceptual doc path (relative to the repo root).
# These are the prose docs behind https://pan.dev/scm/docs/ — the "NGFW
# Configuration components of SCM" overview, auth, roles, and platform setup.
GUIDES: dict[str, str] = {
    "home": "products/scm/docs/home.md",
    "getstarted": "products/scm/docs/getstarted.md",
    "api-call": "products/scm/docs/api-call.md",
    "api-best-practices": "products/scm/docs/api-best-practices.md",
    "access-tokens": "products/scm/docs/access-tokens.md",
    "scope": "products/scm/docs/scope.md",
    "service-accounts": "products/scm/docs/service-accounts.md",
    "user-accounts": "products/scm/docs/user-accounts.md",
    "roles-overview": "products/scm/docs/roles-overview.md",
    "roles-assign": "products/scm/docs/roles-assign.md",
    "all-roles": "products/scm/docs/all-roles.md",
    "tenant-service-groups": "products/scm/docs/tenant-service-groups.md",
    "platform-configuration": "products/scm/docs/configuration/platform-configuration.md",
    "release-notes": "products/scm/docs/release-notes/release-notes.md",
    "changelog": "products/scm/docs/release-notes/changelog.md",
}

HTTP_METHODS = ("get", "post", "put", "patch", "delete", "head", "options")


# ── Network helpers ──────────────────────────────────────────────────────────


def _fetch_bytes(url: str) -> bytes:
    """Download a URL and return its raw bytes, with an explicit timeout.

    Raises ``urllib.error.URLError`` / ``HTTPError`` on failure so the caller
    can report which spec or guide could not be retrieved.
    """
    request = urllib.request.Request(url, headers={"User-Agent": "arc-docsupdate"})
    with urllib.request.urlopen(request, timeout=HTTP_TIMEOUT) as response:
        return response.read()


def list_remote_specs() -> list[str]:
    """Return every SCM OpenAPI spec path currently published on pan.dev."""
    tree = json.loads(_fetch_bytes(TREE_API).decode("utf-8"))
    return sorted(
        item["path"]
        for item in tree.get("tree", [])
        if item["path"].startswith(SPEC_PREFIX)
        and (item["path"].endswith(".yaml") or item["path"].endswith(".json"))
    )


# ── Spec → markdown rendering ────────────────────────────────────────────────


def _load_yaml(raw: bytes) -> dict[str, Any]:
    """Parse spec bytes into a dict.  Requires PyYAML (dev extra)."""
    import yaml  # Deferred: optional dev dependency, only needed for rendering

    return yaml.safe_load(raw)


def _spec_base_url(spec: dict[str, Any]) -> str:
    """Return ``servers[0].url`` — the gateway base URL for this spec."""
    servers = spec.get("servers") or []
    if servers and isinstance(servers[0], dict):
        return str(servers[0].get("url", "")).strip()
    return ""


def _render_markdown(category: str, spec_path: str, spec: dict[str, Any]) -> tuple[str, int]:
    """Render a consolidated endpoint listing for one spec.

    Returns ``(markdown_text, endpoint_count)``.  The format mirrors the
    existing ARC reference pages: a header block followed by one section per
    HTTP operation with summary, operation id, tags, and response codes.
    """
    info = spec.get("info") or {}
    title = str(info.get("title") or category).strip()
    version = str(info.get("version") or "unknown").strip()
    paths = spec.get("paths") or {}

    lines: list[str] = [
        f"# {title}",
        "",
        f"**Version:** {version}  ",
        f"**Source:** `{spec_path}`  ",
        f"**Base URL:** `{_spec_base_url(spec) or 'n/a'}`  ",
    ]
    # Placeholder endpoint count line — replaced once we know the total.
    count_line_index = len(lines)
    lines.append("**Endpoints:** 0  ")
    lines.append(f"**GitHub:** https://github.com/{REPO}/blob/master/{spec_path}")
    lines.extend(["", "---", "", "## Endpoints", ""])

    endpoint_count = 0
    for path, operations in paths.items():
        if not isinstance(operations, dict):
            continue
        for method, operation in operations.items():
            if method.lower() not in HTTP_METHODS or not isinstance(operation, dict):
                continue
            endpoint_count += 1
            summary = str(operation.get("summary") or "").strip()
            operation_id = str(operation.get("operationId") or "").strip()
            tags = ", ".join(operation.get("tags") or [])
            responses = ", ".join(sorted((operation.get("responses") or {}).keys()))

            lines.append(f"### `{method.upper()} {path}`")
            lines.append("")
            if summary:
                lines.append(f"**Summary:** {summary}  ")
            if operation_id:
                lines.append(f"**Operation ID:** `{operation_id}`  ")
            if tags:
                lines.append(f"**Tags:** {tags}  ")
            if responses:
                lines.append(f"**Response codes:** {responses}")
            lines.append("")

    lines[count_line_index] = f"**Endpoints:** {endpoint_count}  "
    return "\n".join(lines).rstrip() + "\n", endpoint_count


# ── Index + manifest ─────────────────────────────────────────────────────────


def _write_index(counts: dict[str, int], guides_pulled: list[str], pulled_on: str) -> None:
    """Write ``index.md`` listing every spec and guide with the pull date."""
    lines = [
        "# SCM NGFW API Reference",
        "",
        "> Pulled from https://pan.dev/scm/docs/home/ and the pan.dev GitHub",
        f"> OpenAPI specs on {pulled_on}.",
        "> Regenerate with: `python dev/update_scm_docs.py` (the `docsupdate` trigger).",
        "",
        "This reference set ships with ARC but is excluded from the browsable",
        "docs portal (`arc cliup` bundle) because it is developer/agent material.",
        "",
        "---",
        "",
        "## API specs (`specs/`)",
        "",
        "Consolidated OpenAPI endpoint listings per NGFW config domain. See",
        "[`MANIFEST.md`](MANIFEST.md) for each spec's base URL.",
        "",
    ]
    for category in SPECS:
        count = counts.get(category)
        suffix = f" — {count} endpoints" if count is not None else " — (raw only)"
        lines.append(f"- **[specs/{category}.md](specs/{category}.md)**{suffix}")
    lines.extend(["", "## Guides (`guides/`)", "", "Conceptual SCM documentation from pan.dev.", ""])
    for guide in GUIDES:
        marker = "" if guide in guides_pulled else " — (unavailable)"
        lines.append(f"- **[guides/{guide}.md](guides/{guide}.md)**{marker}")
    lines.append("")
    (OUTPUT_DIR / "index.md").write_text("\n".join(lines), encoding="utf-8")


def _write_manifest(base_urls: dict[str, str], pulled_on: str) -> None:
    """Write ``MANIFEST.md`` — source URL + base URL for every spec.

    This is the source of truth the agent-instruction gateway map mirrors.
    """
    lines = [
        "# SCM API Manifest",
        "",
        f"Pulled on {pulled_on} from `{REPO}` (master).",
        "",
        "| Category | Base URL (`servers[0].url`) | Spec |",
        "|----------|------------------------------|------|",
    ]
    for category, spec_path in SPECS.items():
        base = base_urls.get(category, "n/a")
        lines.append(f"| `{category}` | `{base or 'n/a'}` | `{spec_path}` |")
    lines.append("")
    (OUTPUT_DIR / "MANIFEST.md").write_text("\n".join(lines), encoding="utf-8")


# ── Orchestration ────────────────────────────────────────────────────────────


def _download_guides(check_only: bool, failures: list[str]) -> list[str]:
    """Download the conceptual pan.dev guide docs.  Returns names pulled OK."""
    pulled: list[str] = []
    for name, doc_path in GUIDES.items():
        url = f"{RAW_BASE}/{doc_path}"
        print(f"  ↓ guide:{name:<22} {doc_path}")
        try:
            raw = _fetch_bytes(url)
        except (urllib.error.URLError, urllib.error.HTTPError) as exc:
            failures.append(f"guide {name}: {exc}")
            print(f"    ✗ download failed: {exc}")
            continue
        if check_only:
            existing = GUIDES_DIR / f"{name}.md"
            status = "changed" if (not existing.exists() or existing.read_bytes() != raw) else "current"
            print(f"    • {status}")
            pulled.append(name)
            continue
        (GUIDES_DIR / f"{name}.md").write_bytes(raw)
        pulled.append(name)
    return pulled


def update(check_only: bool = False) -> int:
    """Download specs + guides and regenerate the reference set.  Returns exit code."""
    for directory in (OUTPUT_DIR, SPECS_DIR, GUIDES_DIR):
        directory.mkdir(parents=True, exist_ok=True)
    pulled_on = _dt.date.today().isoformat()

    # Detect PyYAML up front so we can warn but still archive the raw specs.
    try:
        import yaml  # noqa: F401  (presence check only)

        can_render = True
    except ModuleNotFoundError:
        can_render = False

    counts: dict[str, int] = {}
    base_urls: dict[str, str] = {}
    failures: list[str] = []

    for category, spec_path in SPECS.items():
        url = f"{RAW_BASE}/{spec_path}"
        print(f"  ↓ spec:{category:<23} {spec_path}")
        try:
            raw = _fetch_bytes(url)
        except (urllib.error.URLError, urllib.error.HTTPError) as exc:
            failures.append(f"{category}: {exc}")
            print(f"    ✗ download failed: {exc}")
            continue

        if check_only:
            existing = SPECS_DIR / f"{category}.yaml"
            status = "changed" if (not existing.exists() or existing.read_bytes() != raw) else "current"
            print(f"    • {status}")
            continue

        (SPECS_DIR / f"{category}.yaml").write_bytes(raw)

        if not can_render:
            continue

        try:
            spec = _load_yaml(raw)
            markdown, count = _render_markdown(category, spec_path, spec)
            (SPECS_DIR / f"{category}.md").write_text(markdown, encoding="utf-8")
            counts[category] = count
            base_urls[category] = _spec_base_url(spec)
            print(f"    ✓ {count} endpoints")
        except Exception as exc:  # noqa: BLE001 — surface any render failure clearly
            failures.append(f"{category}: render error: {exc}")
            print(f"    ✗ render failed: {exc}")

    guides_pulled = _download_guides(check_only, failures)

    if check_only:
        return 1 if failures else 0

    if can_render and counts:
        _write_index(counts, guides_pulled, pulled_on)
        _write_manifest(base_urls, pulled_on)
        print(f"\n  ✓ index.md and MANIFEST.md written ({pulled_on})")
    elif not can_render:
        print(
            "\n  ⚠ PyYAML not installed — raw .yaml specs + guides saved, but"
            "\n    markdown/index were not regenerated. Install dev extras and re-run:"
            "\n      uv pip install -e '.[dev]'   (or: pip install pyyaml)"
        )

    if failures:
        print("\n  Some downloads failed:")
        for item in failures:
            print(f"    - {item}")
        return 1

    print(f"\n  Reference set updated under {OUTPUT_DIR}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Update ARC's SCM NGFW API reference from pan.dev.")
    parser.add_argument(
        "--list-remote",
        action="store_true",
        help="Print every SCM OpenAPI spec path currently on pan.dev and exit.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Report which local specs/guides differ from pan.dev without writing files.",
    )
    args = parser.parse_args(argv)

    if args.list_remote:
        try:
            for path in list_remote_specs():
                print(path)
        except (urllib.error.URLError, urllib.error.HTTPError) as exc:
            print(f"Failed to list remote specs: {exc}", file=sys.stderr)
            return 1
        return 0

    print("Updating SCM NGFW API reference from pan.dev…\n")
    return update(check_only=args.check)


if __name__ == "__main__":
    raise SystemExit(main())

