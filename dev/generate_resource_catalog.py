#!/usr/bin/env python3
"""Generate app/commands/resource_catalog.py from every pulled SCM OpenAPI spec.

The catalog is ARC's endpoint coverage ledger.  Each GET/POST/PUT/PATCH/DELETE
operation becomes command metadata with a deterministic feature flag:

* GET    → ``show <resource>`` / ``show_<resource>``
* POST   → ``set <resource>`` / ``create_<resource>``
* PUT    → ``update <resource>`` / ``update_<resource>``
* PATCH  → ``update <resource>`` / ``update_<resource>``
* DELETE → ``delete <resource>`` / ``delete_<resource>``

Generated commands are feature-gated and default OFF in ``settings/features.json``.
Explicit hand-written commands still win; this generator skips default NGFW
endpoints already covered by command doc front-matter and prefixes non-default
families (for example ``cloudngfw`` / ``sase`` / ``iam``) to avoid collisions.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

SPECS_DIR = REPO_ROOT / "docs" / "scm-api" / "specs"
COMMAND_DOCS_DIR = REPO_ROOT / "docs" / "commands"
CATALOG_FILE = REPO_ROOT / "app" / "commands" / "resource_catalog.py"
HTTP_METHODS = {"get", "post", "put", "patch", "delete"}

_ACTION_BY_METHOD = {
    "get": "show",
    "post": "set",
    "put": "update",
    "patch": "update",
    "delete": "delete",
}

_FLAG_BY_METHOD = {
    "get": "show",
    "post": "create",
    "put": "update",
    "patch": "update",
    "delete": "delete",
}

_VERSION_TOKEN = re.compile(r"^v\d+(?:\.\d+)?$", re.IGNORECASE)
_PATH_PARAM = re.compile(r"{([^}]+)}")

_ABBREVIATIONS = {
    "advanced-device-objects": "adv-device-objs",
    "approvalrules": "approval",
    "bgp-address-family-profiles": "bgp-af-profiles",
    "bgp-redistribution-profiles": "bgp-redist-profiles",
    "bgp-route-map-redistributions": "bgp-routemap-redist",
    "certificateinstances": "cert-instances",
    "certificates": "certs",
    "connection-sources": "conn-sources",
    "certificateinstancesearch": "cert-instance-search",
    "certificateissuingtemplates": "cert-templates",
    "certificaterequests": "cert-requests",
    "certificaterequestssearch": "cert-request-search",
    "credentialmanagerconfigurations": "credential-configs",
    "device-context-segments": "device-contexts",
    "distributedissuers": "dist-issuers",
    "domainssynchronization": "domains-sync",
    "expirationnotifications": "exp-notifications",
    "expirationreports": "exp-reports",
    "forwarding-profile-regional-and-custom-proxies": "fp-custom-proxies",
    "forwarding-profile-destinations": "fp-destinations",
    "forwarding-profile-source-applications": "fp-source-apps",
    "forwarding-profile-user-locations": "fp-user-locations",
    "globalprotect-match-list": "gp-match-list",
    "interface-management-profiles": "if-mgmt-profiles",
    "intermediatecertificates": "intermediate-certs",
    "inventorymonitoringconfig": "inventory-monitoring",
    "misconfigured-domains": "bad-domains",
    "network-packet-broker-profiles": "npb-profiles",
    "network-packet-broker-rules": "npb-rules",
    "remote-networks-license-info": "rn-license-info",
    "revocations": "revokes",
    "route-path-access-lists": "route-path-acls",
    "sdwan-error-correction-profiles": "sdwan-error-profiles",
    "sdwan-path-quality-profiles": "sdwan-path-profiles",
    "sdwan-saas-quality-profiles": "sdwan-saas-profiles",
    "sdwan-traffic-distribution-profiles": "sdwan-traffic-profiles",
    "tenantconfiguration": "tenant-config",
    "trusted-certificate-authorities": "trusted-cas",
    "vulnerability-protection-profiles": "vuln-profiles",
    "vulnerability-protection-signatures": "vuln-signatures",
    "verify-update": "verify",
    "wildfire-anti-virus-profiles": "wildfire-profiles",
    "zone-protection-profiles": "zone-profiles",
}

_NOISE_BY_SPEC_PREFIX = {
    "adnsr": {"adns-resolver", "config"},
    "cdug": {"directory-sync"},
    "ciedss": {"cie", "directory-sync"},
    "ngts": {"tlsprotect", "outagedetection"},
    "posture": {"posture", "checks"},
}

_DOMAIN_NOISE = {"identity", "network", "objects", "operations", "security", "setup"}


def _load_yaml(path: Path) -> dict:
    import yaml

    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def _category_prefix(spec_key: str) -> str:
    """Return a command prefix for non-default product/API families."""
    if spec_key.startswith("ngfw-") or spec_key in {"auth", "tenancy", "iam-service-accounts"}:
        return ""
    if spec_key.startswith("cloudngfw-"):
        return "cngfw"
    return spec_key.split("-")[0]


def _category(spec_key: str) -> str:
    if spec_key.startswith("ngfw-"):
        return spec_key.removeprefix("ngfw-")
    return spec_key.split("-")[0]


def _normalize_token(token: str) -> str:
    token = token.strip().strip(":").replace("_", "-")
    token = re.sub(r"[^a-zA-Z0-9-]+", "-", token)
    token = re.sub(r"-+", "-", token).strip("-")
    token = token.lower()
    return _ABBREVIATIONS.get(token, token)


def _resource_tokens(spec_key: str, path: str, method: str) -> list[str]:
    """Build readable command tokens from an OpenAPI path."""
    raw_parts = [part for part in path.strip("/").split("/") if part]

    # Drop leading product/version path prefixes for APIs whose server URL does
    # not include them, e.g. /iam/v1/service_accounts -> service-accounts.
    while raw_parts and (raw_parts[0] in {"auth", "iam", "tenancy", "subscription"}):
        raw_parts.pop(0)
        if raw_parts and _VERSION_TOKEN.match(raw_parts[0]):
            raw_parts.pop(0)
    if raw_parts and _VERSION_TOKEN.match(raw_parts[0]):
        raw_parts.pop(0)

    tokens: list[str] = []
    path_has_params = False
    noise = set()
    for prefix, noise_tokens in _NOISE_BY_SPEC_PREFIX.items():
        if spec_key.startswith(prefix):
            noise.update(noise_tokens)

    for part in raw_parts:
        base, sep, action = part.partition(":")
        if _PATH_PARAM.fullmatch(base):
            path_has_params = True
        elif base != "operations" and not _VERSION_TOKEN.match(base):
            normalized = _normalize_token(base)
            if normalized and normalized not in noise:
                tokens.append(normalized)
        if sep and action:
            normalized_action = _normalize_token(action)
            if normalized_action:
                tokens.append(normalized_action)

    # /{id}/operations/reset style paths should expose the operation name, not
    # the literal implementation bucket "operations".
    if "operations" in raw_parts:
        tail = _normalize_token(raw_parts[-1].split(":")[-1])
        if tail and tail not in tokens and not _PATH_PARAM.fullmatch(raw_parts[-1]):
            tokens.append(tail)

    if spec_key.startswith(("cloudngfw-", "sase-")) and tokens and tokens[0] in _DOMAIN_NOISE:
        tokens.pop(0)

    if method == "get" and path_has_params:
        tokens.append("id")
    return tokens or ["root"]


def _path_params(path: str) -> list[str]:
    return _PATH_PARAM.findall(path)


def _query_params(spec: dict, path_item: dict, operation: dict) -> list[str]:
    params = []
    for entry in list(path_item.get("parameters") or []) + list(operation.get("parameters") or []):
        if not isinstance(entry, dict) or "$ref" in entry:
            continue
        if entry.get("in") == "query" and entry.get("name"):
            params.append(str(entry["name"]))
    return sorted(set(params))


def _covered_default_signatures() -> set[str]:
    """Method/path signatures already covered by explicit default NGFW commands."""
    from app.settings.command_help import parse_front_matter

    covered: set[str] = set()
    for doc in COMMAND_DOCS_DIR.glob("*.md"):
        text = doc.read_text(encoding="utf-8")
        if not text.startswith("---"):
            continue
        meta, _ = parse_front_matter(text)
        api = str(meta.get("api", ""))
        if "/config/" not in api:
            continue
        parts = api.split()
        if len(parts) < 2:
            continue
        method = parts[0].lower()
        path = parts[-1].rstrip("/")
        # Drop known base prefixes so it matches spec-local paths.
        for prefix in (
            "/config/objects/v1",
            "/config/security/v1",
            "/config/setup/v1",
            "/config/network/v1",
            "/config/identity/v1",
            "/config/device/v1",
            "/config/operations/v1",
            "/operations/v1",
        ):
            if path.startswith(prefix):
                path = path[len(prefix):] or "/"
                break
        covered.add(f"{method.upper()} {path}")
    return covered


def _build_catalog() -> list[dict]:
    """Return generated operation entries from every pulled OpenAPI spec."""
    covered = _covered_default_signatures()
    entries: list[dict] = []
    seen_commands: set[str] = set()
    seen_operations: set[tuple[str, str, str]] = set()
    for spec_path in sorted(SPECS_DIR.glob("*.yaml")):
        spec_key = spec_path.stem
        spec = _load_yaml(spec_path)
        base_url = (spec.get("servers") or [{}])[0].get("url", "")
        prefix = _category_prefix(spec_key)
        category = _category(spec_key)
        for path, path_item in (spec.get("paths") or {}).items():
            if not isinstance(path_item, dict):
                continue
            for method, operation in path_item.items():
                method = method.lower()
                if method not in HTTP_METHODS or not isinstance(operation, dict):
                    continue
                operation_signature = (method, base_url, path)
                if operation_signature in seen_operations:
                    continue
                seen_operations.add(operation_signature)
                if spec_key.startswith("ngfw-") and f"{method.upper()} {path.rstrip('/')}" in covered:
                    continue
                tokens = _resource_tokens(spec_key, path, method)
                command_tokens = [prefix] + tokens if prefix else tokens
                command = f"{_ACTION_BY_METHOD[method]} {' '.join(command_tokens)}"
                if command in seen_commands:
                    # Usually a path-param variant of an existing command
                    # (e.g. DELETE /x?name= vs DELETE /x/{id}): follow the
                    # same "… id" convention GET variants use, falling back
                    # to a spec-key prefix only if that is taken too.
                    id_variant = f"{command} id" if _path_params(path) else ""
                    if id_variant and id_variant not in seen_commands:
                        command = id_variant
                    else:
                        command = f"{_ACTION_BY_METHOD[method]} {spec_key.replace('cloudngfw', 'cngfw').replace('-', ' ')} {' '.join(tokens)}"
                seen_commands.add(command)
                resource_flag = "_".join(command_tokens)
                feature_flag = f"{_FLAG_BY_METHOD[method]}_{resource_flag}".replace("-", "_")
                entries.append({
                    "command": command,
                    "method": method.upper(),
                    "base_url": base_url,
                    "path": path,
                    "path_params": _path_params(path),
                    "query_params": _query_params(spec, path_item, operation),
                    "feature_flag": feature_flag,
                    "category": category,
                    "spec": spec_key,
                    "summary": str(operation.get("summary") or "").strip(),
                })
    return sorted(entries, key=lambda e: e["command"])


def _render(entries: list[dict]) -> str:
    lines = [
        '"""Auto-generated NGFW resource catalog — DO NOT EDIT BY HAND.',
        "",
        "Generated by ``dev/generate_resource_catalog.py`` from the pulled SCM OpenAPI specs.",
        "Each entry becomes a feature-gated generated command via ``app/commands/generated.py``.",
        "Regenerate with:",
        "    python dev/generate_resource_catalog.py   (runs automatically on docsupdate)",
        '"""',
        "",
        "from __future__ import annotations",
        "",
        "CATALOG: list[dict] = [",
    ]
    for e in entries:
        lines.append(f"    {e!r},")
    lines.append("]")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    check_only = "--check" in sys.argv[1:]
    try:
        entries = _build_catalog()
    except ModuleNotFoundError:
        print("[warn] PyYAML not installed — cannot regenerate resource catalog "
              "(run: uv pip install -e '.[dev]')", file=sys.stderr)
        return 0  # don't fail the pull; catalog just stays as-is

    rendered = _render(entries)
    current = CATALOG_FILE.read_text(encoding="utf-8") if CATALOG_FILE.exists() else ""

    if check_only:
        if rendered != current:
            print("app/commands/resource_catalog.py is STALE — new uncovered SCM "
                  "endpoints found. Run: python dev/generate_resource_catalog.py")
            return 1
        print(f"resource catalog current — {len(entries)} auto-generated show command(s)")
        return 0

    CATALOG_FILE.write_text(rendered, encoding="utf-8")
    print(f"Wrote app/commands/resource_catalog.py — {len(entries)} generated endpoint command(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

