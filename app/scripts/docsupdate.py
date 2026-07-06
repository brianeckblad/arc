#!/usr/bin/env python3
"""Update ARC's local SCM API reference from pan.dev.

This is the engine behind the `docsupdate` agent trigger.  It pulls the
authoritative Palo Alto Networks Strata Cloud Manager (SCM) documentation for
the **NGFW Configuration** components directly from the public pan.dev GitHub
repository, then regenerates ARC's local reference set under ``docs/scm-api/``.

Everything pan.dev documents at https://pan.app/scripts/scm/docs/home/ is mirrored:

* **OpenAPI specs** (``docs/scm-api/specs/``) — one per NGFW config domain.
  For each: ``<category>.yaml`` (raw spec) and ``<category>.md`` (a consolidated,
  terminal-friendly endpoint listing).
* **Guide docs** (``docs/scm-api/guides/``) — every conceptual SCM doc under
  ``products/scm/docs/``.  Curated names stay stable; any new doc pan.dev adds
  is auto-discovered and mirrored with a slugged name.

Resilience (pan.dev renames files often):

* The list of source paths lives in an editable registry, **app/scripts/scm-sources.json**,
  not hard-coded here.  Edit that file when you know a new path.
* When a path 404s, the tool searches the live pan.dev GitHub tree for the most
  likely replacement (by domain + filename similarity), updates the registry
  with the new path, records the move under ``relocations``, and retries.  So a
  weekly/monthly rename self-heals instead of failing with "file not found".

Change tracking (for the docs-agent code-update workflow):

* Before overwriting specs, the previous endpoint set is captured.  After the
  pull, ``docs/scm-api/CHANGES.md`` reports added/removed endpoints per domain so
  an agent can update affected ARC API calls.  See ``app/scripts/DOCS_AGENT.md``.

Also writes:

* ``docs/scm-api/index.md``    — index of specs + guides with the pull date.
* ``docs/scm-api/MANIFEST.md`` — source URL + ``servers[0].url`` per spec.

Design notes (read before editing):

* Raw downloads use only the Python standard library (``urllib``).
* Markdown/manifest/diff generation needs PyYAML (dev extra):
  ``uv pip install -e '.[dev]'``.  Without it, raw specs + guides still save.

Usage::

    python app/scripts/docsupdate.py                # refresh specs + guides (+ self-heal)
    python app/scripts/docsupdate.py --check         # report drift/relocations, write nothing
    python app/scripts/docsupdate.py --list-remote   # print live SCM spec paths
    python app/scripts/docsupdate.py --no-mirror     # curated guides only (skip "pull all")
    python app/scripts/docsupdate.py --self-test     # offline tests for discovery + diff
"""

from __future__ import annotations

import argparse
import datetime as _dt
import difflib
import json
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any, Optional, cast

# ── Constants ────────────────────────────────────────────────────────────────

DEV_DIR = Path(__file__).resolve().parent
ROOT = DEV_DIR.parent
SOURCES_FILE = DEV_DIR / "scm-sources.json"

HTTP_TIMEOUT = 30  # seconds — every network call is bounded
HTTP_METHODS = ("get", "post", "put", "patch", "delete", "head", "options")

# Output layout: ARC's local SCM reference set lives in docs/ so it ships with
# the app.  specs/ holds OpenAPI references; guides/ holds conceptual pan.dev docs.
OUTPUT_DIR = ROOT / "docs" / "scm-api"
SPECS_DIR = OUTPUT_DIR / "specs"
GUIDES_DIR = OUTPUT_DIR / "guides"
CHANGES_FILE = OUTPUT_DIR / "CHANGES.md"

# Built-in defaults used to seed app/scripts/scm-sources.json on first run if it is
# missing.  After that, the JSON file is the source of truth (and is auto-updated
# when pan.dev relocates a file).
DEFAULT_SOURCES: dict[str, Any] = {
    "repo": "PaloAltoNetworks/pan.dev",
    "branch": "master",
    "settings": {
        "specs_root": "openapi-specs/scm",
        "guides_root": "products/scm/docs",
        "mirror_all_specs": True,
        "mirror_all_guides": True,
        "discovery_min_score": 0.55,
    },
    "specs": {
        "adnsr": "openapi-specs/scm/config/adnsr/adnsr.yaml",
        "cdug": "openapi-specs/scm/config/cdug/cdug.yaml",
        "ciedss": "openapi-specs/scm/config/ciedss/CIE-DSS-R2.yaml",
        "cloudngfw-identity": "openapi-specs/scm/config/cloudngfw/identity/identity-services-march.yaml",
        "cloudngfw-objects": "openapi-specs/scm/config/cloudngfw/objects/objects-june.yaml",
        "cloudngfw-operations": "openapi-specs/scm/config/cloudngfw/operations/config-operations-march.yaml",
        "cloudngfw-security": "openapi-specs/scm/config/cloudngfw/security/security-services.yaml",
        "cloudngfw-setup": "openapi-specs/scm/config/cloudngfw/setup/config-setup-feb-v1.yaml",
        "cloudngfw-device-onboarding": "openapi-specs/scm/config/cloudngfw/setup/device-onboarding/device-onboarding-updated.yaml",
        "incidents": "openapi-specs/scm/config/incidents/Unified_SCM_Incident.yaml",
        "ngfw-objects": "openapi-specs/scm/config/ngfw/objects/objects_v1.3_feb.yaml",
        "ngfw-security": "openapi-specs/scm/config/ngfw/security/security-services-R2-2026.yaml",
        "ngfw-setup": "openapi-specs/scm/config/ngfw/setup/config-setup-feb-v1.yaml",
        "ngfw-network": "openapi-specs/scm/config/ngfw/network/network-services-R2-2026.yaml",
        "ngfw-config-operations": "openapi-specs/scm/config/ngfw/operations/config-operations-march.yaml",
        "ngfw-operations": "openapi-specs/scm/config/ngfw-operations/operations-R2-2026.yaml",
        "ngfw-device": "openapi-specs/scm/config/ngfw/device/device-settings_April.yaml",
        "ngfw-identity": "openapi-specs/scm/config/ngfw/identity/identity-services-march.yaml",
        "ngfw-device-onboarding": "openapi-specs/scm/config/ngfw/setup/device-onboarding/device-onboarding-updated.yaml",
        "ngts-tlsprotect": "openapi-specs/scm/config/ngts/tlsprotect-cloud.json",
        "posture-management": "openapi-specs/scm/config/posture-management/Posture APIs-updated.yaml",
        "sase-deployment": "openapi-specs/scm/config/sase/deployment/deployment-services-march.yaml",
        "sase-identity": "openapi-specs/scm/config/sase/identity/identity-services-march.yaml",
        "sase-mobileagent": "openapi-specs/scm/config/sase/mobileagent/mobile-agent-feb-v1.yaml",
        "sase-network-configurations": "openapi-specs/scm/config/sase/network configurations/network-services-R2-2026.yaml",
        "sase-network": "openapi-specs/scm/config/sase/network/network-services.yaml",
        "sase-objects": "openapi-specs/scm/config/sase/objects/objects-june.yaml",
        "sase-operations": "openapi-specs/scm/config/sase/operations/config-operations-march.yaml",
        "sase-security": "openapi-specs/scm/config/sase/security/security-services-R2-2026.yaml",
        "sase-setup": "openapi-specs/scm/config/sase/setup/config-setup-feb-v1.yaml",
        "sase-device-onboarding": "openapi-specs/scm/config/sase/setup/device-onboarding/device-onboarding-updated.yaml",
        "auth": "openapi-specs/scm/auth/AuthService.yaml",
        "iam-access-policies": "openapi-specs/scm/iam/AccessPolicies.yaml",
        "iam-custom-roles": "openapi-specs/scm/iam/CustomRoles.yaml",
        "iam-permission-sets": "openapi-specs/scm/iam/PermissionSets.yaml",
        "iam-permissions": "openapi-specs/scm/iam/Permissions.yaml",
        "iam-roles": "openapi-specs/scm/iam/Roles.yaml",
        "tenancy": "openapi-specs/scm/tenancy/TenantServiceGroup.yaml",
        "iam-service-accounts": "openapi-specs/scm/iam/ServiceAccounts.yaml",
        "iam-user-accounts": "openapi-specs/scm/iam/UserAccounts.yaml",
        "subscription-instance": "openapi-specs/scm/subscription/Instance.yaml",
        "subscription-licenses": "openapi-specs/scm/subscription/Licenses.yaml",
    },
    "spec_domains": {
        "adnsr": "adnsr",
        "cdug": "cdug",
        "ciedss": "ciedss",
        "cloudngfw-identity": "identity",
        "cloudngfw-objects": "objects",
        "cloudngfw-operations": "operations",
        "cloudngfw-security": "security",
        "cloudngfw-setup": "setup",
        "cloudngfw-device-onboarding": "device-onboarding",
        "incidents": "incidents",
        "ngfw-objects": "objects",
        "ngfw-security": "security",
        "ngfw-setup": "setup",
        "ngfw-network": "network",
        "ngfw-config-operations": "operations",
        "ngfw-operations": "ngfw-operations",
        "ngfw-device": "device",
        "ngfw-identity": "identity",
        "ngfw-device-onboarding": "device-onboarding",
        "ngts-tlsprotect": "ngts",
        "posture-management": "posture-management",
        "sase-deployment": "deployment",
        "sase-identity": "identity",
        "sase-mobileagent": "mobileagent",
        "sase-network-configurations": "network",
        "sase-network": "network",
        "sase-objects": "objects",
        "sase-operations": "operations",
        "sase-security": "security",
        "sase-setup": "setup",
        "sase-device-onboarding": "device-onboarding",
        "auth": "auth",
        "iam-access-policies": "iam",
        "iam-custom-roles": "iam",
        "iam-permission-sets": "iam",
        "iam-permissions": "iam",
        "iam-roles": "iam",
        "tenancy": "tenancy",
        "iam-service-accounts": "iam",
        "iam-user-accounts": "iam",
        "subscription-instance": "subscription",
        "subscription-licenses": "subscription",
    },
    "guides": {
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
    },
    "relocations": [],
}


# ── Source registry (app/scripts/scm-sources.json) ───────────────────────────────────


def load_sources() -> dict[str, Any]:
    """Return the source registry, seeding app/scripts/scm-sources.json if it is missing.

    The JSON file is the editable, auto-updated source of truth.  Any keys it
    omits fall back to DEFAULT_SOURCES so an older/partial file still works.
    """
    if not SOURCES_FILE.exists():
        save_sources(json.loads(json.dumps(DEFAULT_SOURCES)))
        return json.loads(json.dumps(DEFAULT_SOURCES))

    try:
        data = json.loads(SOURCES_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        print(f"  ⚠ could not read {SOURCES_FILE.name} ({exc}); using built-in defaults")
        return json.loads(json.dumps(DEFAULT_SOURCES))

    changed = False

    # Backfill any missing top-level keys from defaults.
    for key, default in DEFAULT_SOURCES.items():
        if key not in data:
            data[key] = default
            changed = True
    data.setdefault("settings", {})
    for key, default in DEFAULT_SOURCES["settings"].items():
        if key not in data["settings"]:
            data["settings"][key] = default
            changed = True
    for section in ("specs", "spec_domains", "guides"):
        data.setdefault(section, {})
        for key, default in DEFAULT_SOURCES[section].items():
            if key not in data[section]:
                data[section][key] = default
                changed = True
    if changed:
        save_sources(data)
    return data


def save_sources(sources: dict[str, Any]) -> None:
    """Persist the source registry back to app/scripts/scm-sources.json."""
    sources.setdefault(
        "_comment",
        "Editable registry of SCM doc sources for app/scripts/docsupdate.py. "
        "Auto-updated when pan.dev moves files (see 'relocations').",
    )
    SOURCES_FILE.write_text(json.dumps(sources, indent=2) + "\n", encoding="utf-8")


def _raw_base(sources: dict[str, Any]) -> str:
    return f"https://raw.githubusercontent.com/{sources['repo']}/{sources['branch']}"


def _raw_url(sources: dict[str, Any], path: str) -> str:
    """Return a raw GitHub URL, escaping spaces and other path characters."""
    return f"{_raw_base(sources)}/{urllib.parse.quote(path, safe='/')}"


def _tree_api(sources: dict[str, Any]) -> str:
    return f"https://api.github.com/repos/{sources['repo']}/git/trees/{sources['branch']}?recursive=1"


# ── Network helpers ──────────────────────────────────────────────────────────


def _fetch_bytes(url: str) -> bytes:
    """Download a URL and return its raw bytes, with an explicit timeout.

    Raises ``urllib.error.URLError`` / ``HTTPError`` on failure so the caller
    can report which spec or guide could not be retrieved.
    """
    request = urllib.request.Request(url, headers={"User-Agent": "arc-docsupdate"})
    with urllib.request.urlopen(request, timeout=HTTP_TIMEOUT) as response:
        return response.read()


# Cache the full repo tree so we only fetch it once per run.
_TREE_CACHE: dict[str, list[str]] = {}


def fetch_tree(sources: dict[str, Any]) -> list[str]:
    """Return every file path in the pan.dev repo tree (cached, best-effort).

    Returns an empty list if the GitHub tree API is unreachable or rate-limited
    so callers degrade gracefully (discovery is skipped, downloads still try).
    """
    cache_key = f"{sources['repo']}@{sources['branch']}"
    if cache_key in _TREE_CACHE:
        return _TREE_CACHE[cache_key]
    try:
        tree = json.loads(_fetch_bytes(_tree_api(sources)).decode("utf-8"))
        paths = [item["path"] for item in tree.get("tree", []) if item.get("type") == "blob"]
    except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError) as exc:
        print(f"  ⚠ could not fetch repo tree for discovery: {exc}")
        paths = []
    _TREE_CACHE[cache_key] = paths
    return paths


def list_remote_specs(sources: dict[str, Any]) -> list[str]:
    """Return every SCM OpenAPI spec path currently published on pan.dev."""
    specs_root = sources["settings"]["specs_root"]
    return sorted(
        p for p in fetch_tree(sources)
        if p.startswith(specs_root + "/") and (p.endswith(".yaml") or p.endswith(".json"))
    )


def _slug_token(text: str) -> str:
    """Normalize a source-path token into a stable registry key segment."""
    token = text.rsplit(".", 1)[0].lower().replace("_", "-").replace(" ", "-")
    token = "".join(ch if ch.isalnum() or ch == "-" else "-" for ch in token)
    while "--" in token:
        token = token.replace("--", "-")
    return token.strip("-") or "spec"


def _spec_key_for_path(path: str, specs_root: str, existing_keys: set[str]) -> str:
    """Return a compact, stable key for a newly discovered OpenAPI spec path."""
    rel = path[len(specs_root) + 1:] if path.startswith(specs_root + "/") else path
    parts = rel.split("/")
    basename = _slug_token(parts[-1])

    if parts[:1] == ["config"] and len(parts) >= 3:
        product = _slug_token(parts[1])
        domain = _slug_token(parts[2])
        if product == "ngfw-operations":
            base_key = "ngfw-operations"
        elif domain == "setup" and len(parts) >= 4 and _slug_token(parts[3]) == "device-onboarding":
            base_key = f"{product}-device-onboarding"
        else:
            base_key = f"{product}-{domain}"
    elif parts[:1] == ["auth"]:
        base_key = "auth"
    elif parts[:1] == ["tenancy"]:
        base_key = "tenancy"
    elif parts[:1] in (["iam"], ["subscription"]):
        base_key = f"{_slug_token(parts[0])}-{basename}"
    else:
        base_key = basename

    candidate = base_key
    suffix = basename
    if candidate in existing_keys:
        candidate = f"{base_key}-{suffix}"
    index = 2
    while candidate in existing_keys:
        candidate = f"{base_key}-{suffix}-{index}"
        index += 1
    return candidate


def _domain_for_spec_path(path: str, specs_root: str) -> str:
    """Return a discovery hint/domain label for a spec path."""
    rel = path[len(specs_root) + 1:] if path.startswith(specs_root + "/") else path
    parts = rel.split("/")
    if parts[:1] == ["config"] and len(parts) >= 3:
        if _slug_token(parts[1]) == "ngfw-operations":
            return "ngfw-operations"
        if _slug_token(parts[2]) == "setup" and len(parts) >= 4:
            return _slug_token(parts[3])
        return _slug_token(parts[2])
    if parts:
        return _slug_token(parts[0])
    return "scm"


def discover_all_specs(sources: dict[str, Any]) -> dict[str, str]:
    """Add any remote SCM OpenAPI specs missing from the source registry.

    Existing entries remain stable so generated filenames do not churn.  New
    pan.dev spec files are assigned deterministic keys and included in this run.
    """
    settings = cast(dict[str, Any], sources["settings"])
    specs_root = str(settings["specs_root"])
    specs_map = cast(dict[str, str], sources.setdefault("specs", {}))
    domains_map = cast(dict[str, str], sources.setdefault("spec_domains", {}))
    known_paths = {str(value) for value in specs_map.values()}
    existing_keys = {str(key) for key in specs_map}
    discovered: dict[str, str] = {}
    for remote_path in list_remote_specs(sources):
        path = str(remote_path)
        if path in known_paths:
            continue
        key = str(_spec_key_for_path(path, specs_root, existing_keys))
        existing_keys.add(key)
        specs_map[key] = path
        domains_map[key] = _domain_for_spec_path(path, specs_root)
        discovered[key] = path
    return discovered


# ── Auto-discovery of relocated files ────────────────────────────────────────


def discover_path(
    old_path: str,
    tree: list[str],
    root: str,
    ext: str,
    domain_hint: Optional[str],
    min_score: float,
) -> Optional[str]:
    """Find the most likely current location of a moved file in *tree*.

    Scoring blends filename similarity with directory/domain hints:
      - SequenceMatcher ratio on the basename (primary signal)
      - +0.40 when the *domain_hint* folder appears in the candidate path
      - +0.20 when the candidate shares the original parent directory
    Returns the best candidate at or above *min_score*, else ``None``.
    """
    if not tree:
        return None

    old_base = old_path.rsplit("/", 1)[-1]
    old_parent = old_path.rsplit("/", 1)[0] if "/" in old_path else ""

    candidates = [p for p in tree if p.startswith(root + "/") and p.endswith(ext)]
    best: Optional[str] = None
    best_score = 0.0
    for cand in candidates:
        cand_base = cand.rsplit("/", 1)[-1]
        score = difflib.SequenceMatcher(None, old_base, cand_base).ratio()
        if domain_hint and f"/{domain_hint}/" in f"/{cand}":
            score += 0.40
        if old_parent and cand.rsplit("/", 1)[0] == old_parent:
            score += 0.20
        if score > best_score:
            best_score, best = score, cand

    return best if best_score >= min_score else None


def _record_relocation(sources: dict[str, Any], kind: str, key: str, old: str, new: str, when: str) -> None:
    """Append a relocation record so history is auditable in scm-sources.json."""
    sources.setdefault("relocations", []).append(
        {"kind": kind, "key": key, "from": old, "to": new, "date": when}
    )


def _fetch_with_discovery(
    sources: dict[str, Any],
    kind: str,
    key: str,
    path: str,
    domain_hint: Optional[str],
    root: str,
    ext: str,
    pulled_on: str,
    relocated: list[str],
) -> tuple[Optional[bytes], str]:
    """Fetch *path*; on 404 try to discover its new location and retry.

    Returns ``(raw_bytes_or_None, effective_path)``.  When a relocation is
    found, the registry dict (and *relocated* log) are updated in place; the
    caller persists the registry after the run.
    """
    url = _raw_url(sources, path)
    try:
        return _fetch_bytes(url), path
    except urllib.error.HTTPError as exc:
        if exc.code != 404:
            raise
    except urllib.error.URLError:
        raise

    # 404 — attempt rediscovery against the live tree.
    min_score = float(sources["settings"].get("discovery_min_score", 0.55))
    tree = fetch_tree(sources)
    new_path = discover_path(path, tree, root, ext, domain_hint, min_score)
    if not new_path or new_path == path:
        return None, path

    print(f"    > relocation: {path}\n                  ->  {new_path}")
    try:
        raw = _fetch_bytes(_raw_url(sources, new_path))
    except (urllib.error.URLError, urllib.error.HTTPError) as exc:
        print(f"    ✗ discovered path also failed: {exc}")
        return None, path

    # Update the registry in place.
    sources[kind][key] = new_path
    _record_relocation(sources, kind, key, path, new_path, pulled_on)
    relocated.append(f"{kind}:{key}  {path} -> {new_path}")
    return raw, new_path


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


def _endpoint_signatures(spec: dict[str, Any]) -> set[str]:
    """Return the set of ``METHOD /path`` signatures defined in a spec."""
    sigs: set[str] = set()
    for path, operations in (spec.get("paths") or {}).items():
        if not isinstance(operations, dict):
            continue
        for method, operation in operations.items():
            if method.lower() in HTTP_METHODS and isinstance(operation, dict):
                sigs.add(f"{method.upper()} {path}")
    return sigs


def _resolve_ref(spec: dict[str, Any], ref: str) -> dict[str, Any]:
    """Resolve a local ``#/components/...`` JSON pointer within *spec*."""
    node: Any = spec
    for part in ref.lstrip("#/").split("/"):
        if not isinstance(node, dict):
            return {}
        node = node.get(part, {})
    return node if isinstance(node, dict) else {}


def _deref(spec: dict[str, Any], schema: Any) -> dict[str, Any]:
    """Return *schema* with a single top-level ``$ref`` resolved (one hop)."""
    if isinstance(schema, dict) and "$ref" in schema:
        return _resolve_ref(spec, schema["$ref"])
    return schema if isinstance(schema, dict) else {}


def _branch_label(spec: dict[str, Any], branch: dict[str, Any]) -> str:
    """Best short label for one oneOf/anyOf leaf branch (the type-variant name).

    SCM variant branches (e.g. an interface's layer2 vs layer3) are usually a
    one-key object — that key is the variant name we want to surface.
    """
    branch = _deref(spec, branch)
    title = str(branch.get("title") or "").strip()
    if title:
        return title
    props = list((branch.get("properties") or {}).keys())
    required = branch.get("required") or []
    common = {"id", "name", "folder", "snippet", "device", "description", "comment", "tag"}
    distinctive = [p for p in props if p not in common]
    if distinctive:
        return "+".join(distinctive[:2])
    if required:
        return "+".join(str(r) for r in required[:2])
    return props[0] if props else ""


def _collect_variants(spec: dict[str, Any], schema: Any, depth: int = 0) -> list[str]:
    """Recursively collect oneOf/anyOf leaf-variant labels from a schema.

    SCM nests choices (e.g. ``anyOf: [oneOf[...], oneOf[...]]``), so we descend
    until each branch is a concrete object and return its distinctive field —
    the actual type name like ``layer2`` / ``layer3`` / ``ha`` / ``tap``.
    """
    if depth > 4:
        return []
    schema = _deref(spec, schema)
    labels: list[str] = []
    nested = schema.get("oneOf") or schema.get("anyOf")
    if isinstance(nested, list):
        for branch in nested:
            deeper = _collect_variants(spec, branch, depth + 1)
            if deeper:
                labels.extend(deeper)
            else:
                label = _branch_label(spec, branch)
                if label:
                    labels.append(label)
    # De-duplicate while preserving order.
    seen: set[str] = set()
    out: list[str] = []
    for label in labels:
        if label not in seen:
            seen.add(label)
            out.append(label)
    return out


def _schema_variants(spec: dict[str, Any], schema: Any) -> list[str]:
    """Return the oneOf/anyOf variant labels for a schema (the type choices)."""
    schema = _deref(spec, schema)
    top = _collect_variants(spec, schema)
    if top:
        return top
    # Variants may live on a property instead of the top schema.
    labels: list[str] = []
    for prop_name, prop in (schema.get("properties") or {}).items():
        prop = prop if isinstance(prop, dict) else {}
        inner = _collect_variants(spec, prop)
        if inner:
            labels.append(f"{prop_name}({'/'.join(inner)})")
    return labels


def _operation_parameters(spec: dict[str, Any], operation: dict[str, Any]) -> tuple[list[str], list[str]]:
    """Return (container_scopes, other_query_params) for an operation.

    container_scopes is the subset of {folder, snippet, device} the endpoint
    accepts — the SCM config container the object lives in.
    """
    containers: list[str] = []
    others: list[str] = []
    for prm in operation.get("parameters") or []:
        if isinstance(prm, dict) and "$ref" in prm:
            prm = _resolve_ref(spec, prm["$ref"])
        if not isinstance(prm, dict):
            continue
        name = prm.get("name")
        if not name:
            continue
        if name in ("folder", "snippet", "device"):
            containers.append(str(name))
        elif prm.get("in") == "query":
            others.append(str(name))
    return containers, others


def _request_body_summary(spec: dict[str, Any], operation: dict[str, Any]) -> tuple[list[str], list[str], str]:
    """Return (required_fields, variant_labels, schema_name) for a request body."""
    content = (operation.get("requestBody") or {}).get("content") or {}
    for _ctype, media in content.items():
        schema = (media or {}).get("schema") or {}
        name = schema.get("$ref", "").split("/")[-1] if isinstance(schema, dict) else ""
        resolved = _deref(spec, schema)
        required = [str(r) for r in (resolved.get("required") or [])]
        return required, _schema_variants(spec, schema), name
    return [], [], ""


def _render_markdown(category: str, spec_path: str, spec: dict[str, Any], repo: str) -> tuple[str, int]:
    """Render a consolidated endpoint listing for one spec.

    Returns ``(markdown_text, endpoint_count)``.
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
    count_line_index = len(lines)
    lines.append("**Endpoints:** 0  ")
    lines.append(f"**GitHub:** https://github.com/{repo}/blob/master/{spec_path}")
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

            # Deep detail: the SCM container the object lives in (folder / snippet
            # / device) and any other query params — so the reference reflects
            # that config can be scoped to a snippet or device, not just a folder.
            containers, query_params = _operation_parameters(spec, operation)

            # Deep detail: request-body required fields + oneOf/anyOf type
            # variants (e.g. an interface's layer2 vs layer3), the structure the
            # flat endpoint list used to discard.
            required, variants, schema_name = _request_body_summary(spec, operation)
            _CONTAINERS = ("folder", "snippet", "device")
            # SCM encodes the container choice as a oneOf in the body too — pull
            # those out so they show as the container scope, not a type variant.
            body_containers = [c for c in _CONTAINERS if c in variants]
            type_variants = [v for v in variants if v not in _CONTAINERS]
            scope = containers or body_containers

            if scope:
                where = "" if containers else " (in request body)"
                lines.append(f"**Container scope:** {' | '.join(scope)}{where}  ")
            if query_params:
                lines.append(f"**Query params:** {', '.join(query_params)}  ")
            if schema_name:
                lines.append(f"**Body schema:** `{schema_name}`  ")
            if required:
                lines.append(f"**Required fields:** {', '.join(f'`{r}`' for r in required)}  ")
            if type_variants:
                lines.append(f"**Type variants (oneOf/anyOf):** {' | '.join(f'`{v}`' for v in type_variants)}  ")

            if responses:
                lines.append(f"**Response codes:** {responses}")
            lines.append("")

    lines[count_line_index] = f"**Endpoints:** {endpoint_count}  "
    return "\n".join(lines).rstrip() + "\n", endpoint_count


# ── Change report (CHANGES.md) ───────────────────────────────────────────────


def _build_changes_markdown(
    changes: dict[str, tuple[set[str], set[str]]],
    relocated: list[str],
    pulled_on: str,
) -> tuple[str, bool]:
    """Build CHANGES.md content from per-category (added, removed) signature sets.

    Returns ``(markdown, had_changes)``.
    """
    lines = [
        "# SCM API Change Report",
        "",
        f"> Generated by `app/scripts/docsupdate.py` on {pulled_on}.",
        "> Read by the docs-agent (see `app/scripts/DOCS_AGENT.md`) to update affected ARC API calls.",
        "",
    ]

    had_changes = False

    if relocated:
        had_changes = True
        lines.extend(["## Relocated source files", ""])
        for item in relocated:
            lines.append(f"- {item}")
        lines.append("")

    any_endpoint_change = any(added or removed for added, removed in changes.values())
    if any_endpoint_change:
        had_changes = True
        lines.extend(["## Endpoint changes by domain", ""])
        for category in sorted(changes):
            added, removed = changes[category]
            if not added and not removed:
                continue
            lines.append(f"### `{category}`")
            lines.append("")
            if added:
                lines.append(f"**Added ({len(added)}):**")
                for sig in sorted(added):
                    lines.append(f"- `{sig}`")
                lines.append("")
            if removed:
                lines.append(f"**Removed ({len(removed)}):**  <- check ARC handlers/`client.py` for these")
                for sig in sorted(removed):
                    lines.append(f"- `{sig}`")
                lines.append("")

    if not had_changes:
        lines.extend(["No endpoint or source-location changes since the last pull.", ""])

    return "\n".join(lines).rstrip() + "\n", had_changes


# ── Index + manifest ─────────────────────────────────────────────────────────


def _write_index(sources: dict[str, Any], counts: dict[str, int], guides_pulled: list[str], pulled_on: str) -> None:
    """Write ``index.md`` listing every spec and guide with the pull date."""
    lines = [
        "# SCM NGFW API Reference",
        "",
        "> Pulled from https://pan.app/scripts/scm/docs/home/ and the pan.dev GitHub",
        f"> OpenAPI specs on {pulled_on}.",
        "> Regenerate with: `python app/scripts/docsupdate.py` (the `docsupdate` trigger).",
        "",
        "This reference set ships with ARC but is excluded from the browsable",
        "docs portal (`arc cliup` bundle) because it is developer/agent material.",
        "",
        "See [`CHANGES.md`](CHANGES.md) for what changed in the last pull.",
        "",
        "---",
        "",
        "## API specs (`specs/`)",
        "",
        "Consolidated OpenAPI endpoint listings per NGFW config domain. See",
        "[`MANIFEST.md`](MANIFEST.md) for each spec's base URL.",
        "",
    ]
    for category in sources["specs"]:
        count = counts.get(category)
        suffix = f" — {count} endpoints" if count is not None else " — (raw only)"
        lines.append(f"- **[specs/{category}.md](specs/{category}.md)**{suffix}")
    lines.extend(["", "## Guides (`guides/`)", "", "Conceptual SCM documentation from pan.dev.", ""])
    for guide in sorted(guides_pulled):
        lines.append(f"- **[guides/{guide}.md](guides/{guide}.md)**")
    lines.append("")
    (OUTPUT_DIR / "index.md").write_text("\n".join(lines), encoding="utf-8")


def _write_manifest(sources: dict[str, Any], base_urls: dict[str, str], pulled_on: str) -> None:
    """Write ``MANIFEST.md`` — source URL + base URL for every spec.

    This is the source of truth the agent-instruction gateway map mirrors.
    """
    lines = [
        "# SCM API Manifest",
        "",
        f"Pulled on {pulled_on} from `{sources['repo']}` ({sources['branch']}).",
        "",
        "| Category | Base URL (`servers[0].url`) | Spec |",
        "|----------|------------------------------|------|",
    ]
    for category, spec_path in sources["specs"].items():
        base = base_urls.get(category, "n/a")
        lines.append(f"| `{category}` | `{base or 'n/a'}` | `{spec_path}` |")
    lines.append("")
    (OUTPUT_DIR / "MANIFEST.md").write_text("\n".join(lines), encoding="utf-8")


# ── Guide discovery ──────────────────────────────────────────────────────────


def _slug_for_guide(path: str, guides_root: str) -> str:
    """Turn a guide path into a stable file-name slug.

    ``products/scm/docs/configuration/platform-configuration.md``
        -> ``configuration__platform-configuration``
    """
    rel = path[len(guides_root) + 1:] if path.startswith(guides_root + "/") else path
    if rel.endswith(".md"):
        rel = rel[:-3]
    return rel.replace("/", "__")


def discover_all_guides(sources: dict[str, Any], already: set[str]) -> dict[str, str]:
    """Return {slug: path} for every guide doc not already covered.

    Mirrors *all* markdown under the guides root so new pan.dev docs appear
    automatically.  Skips paths already pulled by curated names.
    """
    guides_root = sources["settings"]["guides_root"]
    extra: dict[str, str] = {}
    for path in fetch_tree(sources):
        if not path.startswith(guides_root + "/") or not path.endswith(".md"):
            continue
        if path in already:
            continue
        extra[_slug_for_guide(path, guides_root)] = path
    return extra


# ── Orchestration ────────────────────────────────────────────────────────────


def _capture_old_signatures(sources: dict[str, Any], can_render: bool) -> dict[str, set[str]]:
    """Parse existing local specs to capture endpoint signatures before overwrite."""
    old: dict[str, set[str]] = {}
    if not can_render:
        return old
    for category in sources["specs"]:
        existing = SPECS_DIR / f"{category}.yaml"
        if not existing.exists():
            old[category] = set()
            continue
        try:
            old[category] = _endpoint_signatures(_load_yaml(existing.read_bytes()))
        except Exception:  # noqa: BLE001 — a malformed old file just means "no baseline"
            old[category] = set()
    return old


def _download_guides(
    sources: dict[str, Any],
    guide_map: dict[str, str],
    check_only: bool,
    failures: list[str],
    relocated: list[str],
    pulled_on: str,
) -> list[str]:
    """Download guide docs (curated + discovered).  Returns names pulled OK."""
    pulled_names: list[str] = []
    settings = cast(dict[str, Any], sources["settings"])

    for name, doc_path in guide_map.items():
        print(f"  ↓ guide:{name:<28} {doc_path}")
        raw, _eff_path = _fetch_with_discovery(
            sources, "guides", name, doc_path,
            domain_hint=None, root=str(settings["guides_root"]), ext=".md",
            pulled_on=pulled_on, relocated=relocated,
        )
        if raw is None:
            failures.append(f"guide {name}: not found (even after discovery)")
            print("    ✗ not found")
            continue
        if check_only:
            existing = GUIDES_DIR / f"{name}.md"
            status = "changed" if (not existing.exists() or existing.read_bytes() != raw) else "current"
            print(f"    • {status}")
            pulled_names.append(name)
            continue
        (GUIDES_DIR / f"{name}.md").write_bytes(raw)
        pulled_names.append(name)
    return pulled_names


def update(check_only: bool = False, mirror_all: Optional[bool] = None) -> int:
    """Download specs + guides and regenerate the reference set.  Returns exit code."""
    for directory in (OUTPUT_DIR, SPECS_DIR, GUIDES_DIR):
        directory.mkdir(parents=True, exist_ok=True)
    pulled_on = _dt.date.today().isoformat()

    sources = load_sources()
    mirror_all_specs = bool(sources["settings"].get("mirror_all_specs", True))
    if mirror_all is None:
        mirror_all = bool(sources["settings"].get("mirror_all_guides", True))

    discovered_specs: dict[str, str] = {}
    if mirror_all_specs:
        discovered_specs = discover_all_specs(sources)
        if discovered_specs:
            print(f"  + {len(discovered_specs)} additional OpenAPI spec(s) discovered under {sources['settings']['specs_root']}/")
            for key, path in sorted(discovered_specs.items()):
                print(f"    + spec:{key:<23} {path}")
            if not check_only:
                save_sources(sources)

    try:
        import yaml  # noqa: F401  (presence check only)
        can_render = True
    except ModuleNotFoundError:
        can_render = False

    counts: dict[str, int] = {}
    base_urls: dict[str, str] = {}
    failures: list[str] = []
    relocated: list[str] = []
    specs_root = sources["settings"]["specs_root"]

    # Capture the previous endpoint sets so we can diff after the pull.
    old_signatures = _capture_old_signatures(sources, can_render)
    new_signatures: dict[str, set[str]] = {}

    for category, spec_path in list(sources["specs"].items()):
        domain_hint = sources.get("spec_domains", {}).get(category)
        print(f"  ↓ spec:{category:<23} {spec_path}")
        raw, eff_path = _fetch_with_discovery(
            sources, "specs", category, spec_path,
            domain_hint=domain_hint,
            root=specs_root,
            ext=".json" if spec_path.endswith(".json") else ".yaml",
            pulled_on=pulled_on, relocated=relocated,
        )
        if raw is None:
            failures.append(f"{category}: not found (even after discovery)")
            print("    ✗ not found")
            continue

        if not check_only:
            (SPECS_DIR / f"{category}.yaml").write_bytes(raw)

        if not can_render:
            continue
        try:
            spec = _load_yaml(raw)
            new_signatures[category] = _endpoint_signatures(spec)
            markdown, count = _render_markdown(category, eff_path, spec, sources["repo"])
            if not check_only:
                (SPECS_DIR / f"{category}.md").write_text(markdown, encoding="utf-8")
            counts[category] = count
            base_urls[category] = _spec_base_url(spec)
            print(f"    ✓ {count} endpoints")
        except Exception as exc:  # noqa: BLE001 — surface any render failure clearly
            failures.append(f"{category}: render error: {exc}")
            print(f"    ✗ render failed: {exc}")

    # Guides: curated set first, then mirror everything else under the root.
    guide_map = dict(sources["guides"])
    if mirror_all:
        extra = discover_all_guides(sources, already=set(sources["guides"].values()))
        if extra:
            print(f"  + {len(extra)} additional guide doc(s) discovered under {sources['settings']['guides_root']}/")
        guide_map.update(extra)

    guides_pulled = _download_guides(
        sources, guide_map, check_only, failures, relocated, pulled_on
    )

    # Build the change report from old vs new endpoint signatures.
    changes: dict[str, tuple[set[str], set[str]]] = {}
    for category in new_signatures:
        old = old_signatures.get(category, set())
        new = new_signatures[category]
        changes[category] = (new - old, old - new)
    changes_md, had_changes = _build_changes_markdown(changes, relocated, pulled_on)

    if check_only:
        print("\n  ── check summary ──")
        if discovered_specs:
            print("  New OpenAPI specs discovered (run without --check to save/pull):")
            for key, path in sorted(discovered_specs.items()):
                print(f"    - {key}: {path}")
        if relocated:
            print("  Relocations detected (run without --check to apply):")
            for item in relocated:
                print(f"    - {item}")
        if had_changes:
            print("  Endpoint or location changes detected.")
        else:
            print("  No changes detected.")
        return 1 if failures else 0

    # Persist relocations back to the registry so future runs use new paths.
    if relocated:
        save_sources(sources)
        print(f"\n  ✓ {len(relocated)} relocation(s) saved to {SOURCES_FILE.name}")

    if can_render and counts:
        _write_index(sources, counts, guides_pulled, pulled_on)
        _write_manifest(sources, base_urls, pulled_on)
        CHANGES_FILE.write_text(changes_md, encoding="utf-8")
        print(f"\n  ✓ index.md, MANIFEST.md, CHANGES.md written ({pulled_on})")
    elif not can_render:
        print(
            "\n  ⚠ PyYAML not installed — raw .yaml specs + guides saved, but"
            "\n    markdown/index/changes were not regenerated. Install dev extras:"
            "\n      uv pip install -e '.[dev]'   (or: pip install pyyaml)"
        )

    if failures:
        print("\n  Some downloads failed:")
        for item in failures:
            print(f"    - {item}")
        return 1

    print(f"\n  Reference set updated under {OUTPUT_DIR}")
    if had_changes:
        print("  ⚠ Changes detected — see docs/scm-api/CHANGES.md (docs-agent: update affected API calls).")
    return 0


# ── Offline self-test (no network) ───────────────────────────────────────────


def _self_test() -> int:
    """Exercise discovery + diff logic offline so the engine stays trustworthy."""
    passed = 0
    failed = 0

    def check(name: str, cond: bool) -> None:
        nonlocal passed, failed
        if cond:
            passed += 1
            print(f"  ✓ {name}")
        else:
            failed += 1
            print(f"  ✗ {name}")

    # Synthetic tree mimicking a pan.dev rename (date suffix changed).
    tree = [
        "openapi-specs/scm/config/ngfw/network/network-services-R3-2026.yaml",
        "openapi-specs/scm/config/ngfw/security/security-services-R3-2026.yaml",
        "openapi-specs/scm/config/ngfw/objects/objects_v1.4_aug.yaml",
        "products/scm/docs/home.md",
        "products/scm/docs/getstarted.md",
        "products/scm/docs/new-guide.md",
        "products/scm/docs/configuration/platform-configuration.md",
    ]

    # 1. Relocated network spec is found via domain + filename similarity.
    found = discover_path(
        "openapi-specs/scm/config/ngfw/network/network-services-R2-2026.yaml",
        tree, "openapi-specs/scm", ".yaml", "network", 0.55,
    )
    check("discover_path finds renamed network spec",
          found == "openapi-specs/scm/config/ngfw/network/network-services-R3-2026.yaml")

    # 2. Objects spec with a very different name still matches via domain hint.
    found_obj = discover_path(
        "openapi-specs/scm/config/ngfw/objects/objects_v1.3_feb.yaml",
        tree, "openapi-specs/scm", ".yaml", "objects", 0.55,
    )
    check("discover_path finds renamed objects spec via domain hint",
          found_obj == "openapi-specs/scm/config/ngfw/objects/objects_v1.4_aug.yaml")

    # 3. A path with no plausible match returns None.
    none_match = discover_path(
        "openapi-specs/scm/config/ngfw/zzz/does-not-exist.yaml",
        tree, "openapi-specs/scm", ".yaml", "zzz", 0.95,
    )
    check("discover_path returns None when nothing matches", none_match is None)

    # 4. Empty tree -> None (degrade gracefully when GitHub is unreachable).
    check("discover_path returns None on empty tree",
          discover_path("a/b.yaml", [], "a", ".yaml", None, 0.5) is None)

    # 5. Endpoint signature diff detects add + remove.
    old_spec = {"paths": {"/a": {"get": {}}, "/b": {"get": {}}}}
    new_spec = {"paths": {"/a": {"get": {}}, "/c": {"post": {}}}}
    old_sigs = _endpoint_signatures(old_spec)
    new_sigs = _endpoint_signatures(new_spec)
    check("signature diff detects added endpoint", (new_sigs - old_sigs) == {"POST /c"})
    check("signature diff detects removed endpoint", (old_sigs - new_sigs) == {"GET /b"})

    # 6. Guide slug builder handles nested paths.
    slug = _slug_for_guide("products/scm/docs/configuration/platform-configuration.md", "products/scm/docs")
    check("guide slug flattens nested path", slug == "configuration__platform-configuration")

    # 7. discover_all_guides surfaces a brand-new doc not in the curated set.
    sources = json.loads(json.dumps(DEFAULT_SOURCES))
    _TREE_CACHE[f"{sources['repo']}@{sources['branch']}"] = tree
    extra = discover_all_guides(sources, already=set(sources["guides"].values()))
    check("discover_all_guides surfaces new doc", "new-guide" in extra)
    _TREE_CACHE.clear()

    # 8. CHANGES.md reports relocations + endpoint changes.
    md, had = _build_changes_markdown(
        {"ngfw-network": ({"POST /c"}, {"GET /b"})},
        ["specs:ngfw-network  old.yaml -> new.yaml"],
        "2026-06-17",
    )
    check("changes md flags had_changes", had is True)
    check("changes md lists added endpoint", "`POST /c`" in md)
    check("changes md lists removed endpoint", "`GET /b`" in md)

    print(f"\n  self-test: {passed} passed, {failed} failed")
    return 0 if failed == 0 else 1


# ── CLI ──────────────────────────────────────────────────────────────────────


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
        help="Report drift/relocations/endpoint changes without writing files.",
    )
    parser.add_argument(
        "--no-mirror",
        action="store_true",
        help="Pull only the curated guide set (skip mirroring every doc under the guides root).",
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="Run offline tests for discovery + diff logic (no network) and exit.",
    )
    args = parser.parse_args(argv)

    if args.self_test:
        return _self_test()

    if args.list_remote:
        try:
            for path in list_remote_specs(load_sources()):
                print(path)
        except (urllib.error.URLError, urllib.error.HTTPError) as exc:
            print(f"Failed to list remote specs: {exc}", file=sys.stderr)
            return 1
        return 0

    print("Updating SCM NGFW API reference from pan.dev…\n")
    mirror_all = False if args.no_mirror else None
    result = update(check_only=args.check, mirror_all=mirror_all)

    # After a successful update, regenerate generated catalogs/docs derived from
    # the freshly pulled specs.
    if result == 0 and not args.check:
        # Regenerate the auto-coverage resource catalog FIRST: turn every new
        # pulled spec operation into feature-gated generated command metadata.
        print("\nRegenerating NGFW resource catalog (app/commands/resource_catalog.py)…")
        try:
            subprocess.run(
                [sys.executable, str(DEV_DIR / "generate_resource_catalog.py")],
                check=True,
            )
        except (subprocess.CalledProcessError, OSError) as exc:
            print(f"[warn] resource-catalog regeneration failed: {exc}", file=sys.stderr)

        # Regenerate the CLI field catalog: request-body schemas become field
        # syntax + prompt-time validation for flat generated `set` commands.
        print("\nRegenerating CLI field catalog (app/settings/field_catalog.py)…")
        try:
            subprocess.run(
                [sys.executable, str(DEV_DIR / "generate_field_library.py")],
                check=True,
            )
        except (subprocess.CalledProcessError, OSError) as exc:
            print(f"[warn] field-catalog regeneration failed: {exc}", file=sys.stderr)

        # Pull the PAN-OS CLI hierarchy pages (app/scripts/panos_sources.json — add new
        # version URLs there) and regenerate the PAN-OS command catalog.
        print("\nUpdating PAN-OS CLI hierarchy mirrors (docs/panos-cli/)…")
        try:
            subprocess.run(
                [sys.executable, str(DEV_DIR / "panosupdate.py")],
                check=True,
            )
        except (subprocess.CalledProcessError, OSError) as exc:
            print(f"[warn] PAN-OS docs pull failed: {exc}", file=sys.stderr)

        print("\nRegenerating PAN-OS command catalog (app/commands/panos_catalog.py)…")
        try:
            subprocess.run(
                [sys.executable, str(DEV_DIR / "generate_panos_catalog.py")],
                check=True,
            )
        except (subprocess.CalledProcessError, OSError) as exc:
            print(f"[warn] PAN-OS catalog regeneration failed: {exc}", file=sys.stderr)

        # Regenerate feature flags from the generated endpoint catalog plus every
        # explicit CommandDef.feature_flag.  New API surface defaults OFF so ARC
        # fails closed until features are intentionally enabled.
        print("\nRegenerating feature flags (settings/features.json)…")
        try:
            subprocess.run(
                [sys.executable, str(DEV_DIR / "generate_feature_flags.py")],
                check=True,
            )
        except (subprocess.CalledProcessError, OSError) as exc:
            print(f"[warn] feature-flag regeneration failed: {exc}", file=sys.stderr)

        # Regenerate per-command help docs: ensure every command's
        # docs/commands/<slug>.md has help front-matter, and rebuild the command
        # index + API reference.  This keeps the `?`/`help` text and the
        # API→command map in sync with the registry after a spec pull.
        print("\nRegenerating command help docs (docs/commands/)…")
        try:
            subprocess.run(
                [sys.executable, str(DEV_DIR / "generate_command_docs.py")],
                check=True,
            )
        except (subprocess.CalledProcessError, OSError) as exc:
            print(f"[warn] command-doc regeneration failed: {exc}", file=sys.stderr)

        # Regenerate the compact API index last so the ARC Command column sees
        # the freshly generated command docs/front-matter.
        print("\nRegenerating compact API index (app/scripts/API_INDEX.md)…")
        try:
            subprocess.run(
                [sys.executable, str(DEV_DIR / "generate_api_index.py")],
                check=True,
            )
        except (subprocess.CalledProcessError, OSError) as exc:
            print(f"[warn] API index regeneration failed: {exc}", file=sys.stderr)

        # Self-verify: a broken catalog/registry should fail HERE, not at the
        # next arc startup.  Sections 1-3 = syntax + imports + registry.
        print("\nVerifying registry (app/scripts/smoke_test.py --only 1,2,3)…")
        try:
            subprocess.run(
                [sys.executable, str(DEV_DIR / "smoke_test.py"), "--only", "1,2,3", "--quiet"],
                check=True,
            )
            print("Registry OK.")
        except (subprocess.CalledProcessError, OSError) as exc:
            print(f"[warn] smoke verification failed — fix before committing: {exc}", file=sys.stderr)
            result = 1

    return result


if __name__ == "__main__":
    raise SystemExit(main())

