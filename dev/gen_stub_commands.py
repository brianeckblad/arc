#!/usr/bin/env python3
"""Generate stub commands + docs for every SCM API resource.

Run: python dev/gen_stub_commands.py

What it does:
  1. Reads the master API resource table below
  2. For each resource with POST → creates docs/commands/set-<resource>.md
     and adds a stub CommandDef entry (feature_flag disabled by default)
  3. For each resource with DELETE → creates docs/commands/delete-<resource>.md
  4. For resources with GET not yet in ARC → creates docs/commands/show-<resource>.md
  5. Prints a summary of what was created

The doc stubs include:
  - Correct API endpoint path
  - Known schema variants (oneOf/anyOf types from the OpenAPI spec)
  - Feature flag to enable
  - Usage examples

This script is IDEMPOTENT — it will not overwrite existing files.
To regenerate a specific file, delete it first then re-run.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT      = Path(__file__).resolve().parent.parent
DOCS_CMDS = ROOT / "docs" / "commands"

# ---------------------------------------------------------------------------
# Known schema variants for each resource (from oneOf/anyOf in OpenAPI specs)
# Sourced from: dev/extract_variants.py
# Format: resource_name → list of (variant_title, required_fields, example, description)
# ---------------------------------------------------------------------------
SCHEMA_VARIANTS: dict[str, list[dict]] = {
    "address": [
        {"title": "ip_netmask",  "field": "ip_netmask",  "example": "192.168.80.0/24",    "desc": "IP address with optional CIDR prefix (e.g. 10.1.0.0/24 or 10.1.2.3/32)"},
        {"title": "ip_range",    "field": "ip_range",    "example": "10.0.0.1-10.0.0.4",  "desc": "Inclusive IP address range (start-end)"},
        {"title": "ip_wildcard", "field": "ip_wildcard", "example": "10.20.1.0/0.0.248.255","desc": "IP with wildcard mask (0=any, 1=exact match)"},
        {"title": "fqdn",        "field": "fqdn",        "example": "some.example.com",    "desc": "Fully qualified domain name (1-255 chars)"},
    ],
    "address-group": [
        {"title": "static",  "field": "static",          "example": "web1 web2",           "desc": "Explicit list of address object names"},
        {"title": "dynamic", "field": "dynamic.filter",  "example": "'Production and DMZ'","desc": "Tag expression evaluated at policy match time"},
    ],
    "service": [
        {"title": "tcp",  "field": "protocol.tcp.port",  "example": "443",         "desc": "TCP destination port — single, range (8080-8090), or list (80,443)"},
        {"title": "udp",  "field": "protocol.udp.port",  "example": "53",          "desc": "UDP destination port — single, range, or list"},
    ],
    "external-dynamic-list": [
        {"title": "ip",     "field": "type.ip.url",     "example": "https://feed.example.com/ips.txt",     "desc": "IP/CIDR list (one per line)"},
        {"title": "domain", "field": "type.domain.url", "example": "https://feed.example.com/domains.txt", "desc": "Domain name list (one per line)"},
        {"title": "url",    "field": "type.url.url",    "example": "https://openphish.com/feed.txt",       "desc": "URL prefix list (one per line)"},
        {"title": "imsi",   "field": "type.imsi.url",   "example": "https://feed.example.com/imsi.txt",    "desc": "IMSI list (mobile subscriber identifiers)"},
        {"title": "imei",   "field": "type.imei.url",   "example": "https://feed.example.com/imei.txt",    "desc": "IMEI list (mobile equipment identifiers)"},
    ],
    "nat-rule": [
        {"title": "destination_translation",         "field": "destination_translation",         "example": "(translated_address, translated_port)", "desc": "Static destination NAT translation"},
        {"title": "dynamic_destination_translation", "field": "dynamic_destination_translation", "example": "(distribution)",                         "desc": "Dynamic destination NAT with load balancing"},
    ],
    "ethernet-interface": [
        {"title": "layer3",          "field": "layer3",          "example": "(ip, mtu, zone)", "desc": "Layer 3 interface with IP address"},
        {"title": "layer2",          "field": "layer2",          "example": "(vlan)",          "desc": "Layer 2 (switching) interface"},
        {"title": "aggregate_group", "field": "aggregate_group", "example": "ae1",             "desc": "Member of an aggregate (LACP) interface"},
        {"title": "tap",             "field": "tap",             "example": "()",              "desc": "Passive tap interface (read-only capture)"},
    ],
    "aggregate-interface": [
        {"title": "layer3", "field": "layer3", "example": "(ip, mtu, zone)", "desc": "Layer 3 aggregate interface"},
        {"title": "layer2", "field": "layer2", "example": "(vlan)",          "desc": "Layer 2 aggregate interface"},
    ],
    "dhcp-interface": [
        {"title": "server", "field": "server", "example": "(ip_pool, subnet, gateway)", "desc": "DHCP server on this interface"},
        {"title": "relay",  "field": "relay",  "example": "(servers)",                  "desc": "DHCP relay to an external server"},
    ],
    "ipsec-crypto-profile": [
        {"title": "esp", "field": "esp", "example": "(encryption, authentication)", "desc": "ESP (Encapsulating Security Payload) — most common"},
        {"title": "ah",  "field": "ah",  "example": "(authentication)",             "desc": "AH (Authentication Header) — no encryption"},
    ],
}


# ---------------------------------------------------------------------------
# Master API resource table
# ---------------------------------------------------------------------------

RESOURCES = [
    # resource, domain, url_suffix, methods, flag, show, set, delete, notes
    ("address",                 "objects",  "/config/objects/v1/addresses",              "LRCUD", "create_address",        "show address",                   "set address",                   "delete address",                   "ip-netmask | ip-range | ip-wildcard | fqdn"),
    ("address-group",           "objects",  "/config/objects/v1/address-groups",          "LRCUD", "create_address_group",  "show address-group",             "set address-group",             "delete address-group",             "static member list or dynamic tag filter"),
    ("service",                 "objects",  "/config/objects/v1/services",               "LRCUD", "create_service",        "show service",                   "set service",                   "delete service",                   "tcp or udp with port/port-range"),
    ("service-group",           "objects",  "/config/objects/v1/service-groups",          "LRCUD", "create_service_group",  "show service-group",             "set service-group",             "delete service-group",             "named list of service objects"),
    ("tag",                     "objects",  "/config/objects/v1/tags",                   "LRCUD", "create_tag",            "show tag",                       "set tag",                       "delete tag",                       "40 color options, optional comments"),
    ("external-dynamic-list",   "objects",  "/config/objects/v1/external-dynamic-lists", "LRCUD", "create_edl",            "show external-dynamic-list",     "set external-dynamic-list",     "delete external-dynamic-list",     "ip | domain | url | imsi | imei"),
    ("application-group",       "objects",  "/config/objects/v1/application-groups",     "LRCUD", "app_groups",            "show application-group",         "",                              "",                                 "group of predefined applications"),
    ("application-filter",      "objects",  "/config/objects/v1/application-filters",    "LRCUD", "app_groups",            "show application-filter",        "",                              "",                                 "filter based on app attributes"),
    ("schedule",                "objects",  "/config/objects/v1/schedules",              "LRCUD", "schedules",             "show schedule",                  "",                              "",                                 "recurring or non-recurring time windows"),
    ("region",                  "objects",  "/config/objects/v1/regions",               "LRCUD", "regions",               "show region",                    "",                              "",                                 "geographic region definitions"),
    ("hip-object",              "objects",  "/config/objects/v1/hip-objects",            "LRCUD", "hip",                   "show hip-object",                "",                              "",                                 "GlobalProtect host information profile object"),
    ("hip-profile",             "objects",  "/config/objects/v1/hip-profiles",           "LRCUD", "hip",                   "show hip-profile",               "",                              "",                                 "GlobalProtect HIP profile (combines HIP objects)"),
    ("log-forwarding-profile",  "objects",  "/config/objects/v1/log-forwarding-profiles","LRCUD", "log_profiles",          "show log-forwarding-profile",    "",                              "",                                 "log forwarding destinations (syslog, HTTP, panorama)"),
    ("syslog-server-profile",   "objects",  "/config/objects/v1/syslog-server-profiles", "LRCUD", "log_profiles",          "",                               "",                              "",                                 "syslog server configuration for log forwarding"),
    ("http-server-profile",     "objects",  "/config/objects/v1/http-server-profiles",   "LRCUD", "log_profiles",          "",                               "",                              "",                                 "HTTP server profile for log forwarding"),
    ("dynamic-user-group",      "objects",  "/config/objects/v1/dynamic-user-groups",    "LRCUD", "local_users",           "",                               "",                              "",                                 "dynamic group of users matching a filter"),

    ("security-rule",           "security", "/config/security/v1/security-rules",        "LRCUD", "create_security_rule",  "show security policy",           "",                              "delete security-rule",             "allow|deny|drop with zone/address/app/service"),
    ("url-category",            "security", "/config/security/v1/url-categories",        "LRCUD", "create_url_category",   "show url-categories",            "set url-category",              "delete url-category",              "custom URL categories for URL filtering policy"),
    ("decryption-rule",         "security", "/config/security/v1/decryption-rules",      "LRCUD", "decryption_policy",     "show decryption-rules",          "",                              "",                                 "SSL/TLS decryption policy rules"),
    ("decryption-profile",      "security", "/config/security/v1/decryption-profiles",   "LRCUD", "decryption_policy",     "show decryption-profile",        "",                              "",                                 "SSL/TLS decryption settings profile"),
    ("dos-protection-rule",     "security", "/config/security/v1/dos-protection-rules",  "LRCUD", "dos_protection",        "show dos-protection-rules",      "",                              "",                                 "DoS protection policy rules"),
    ("dos-protection-profile",  "security", "/config/security/v1/dos-protection-profiles","LRCUD","dos_protection",        "show dos-protection-profile",    "",                              "",                                 "DoS protection threshold settings"),
    ("app-override-rule",       "security", "/config/security/v1/app-override-rules",    "LRCUD", "app_override",          "show app-override-rules",        "",                              "",                                 "override application identification"),
    ("profile-group",           "security", "/config/security/v1/profile-groups",        "LRCUD", "profile_groups",        "show profile-group",             "",                              "",                                 "bundle security profiles into one group"),
    ("anti-spyware-profile",    "security", "/config/security/v1/anti-spyware-profiles", "LRCUD", "security_profiles",     "show anti-spyware-profile",      "",                              "",                                 "spyware/C2 detection settings"),
    ("vulnerability-profile",   "security", "/config/security/v1/vulnerability-protection-profiles","LRCUD","security_profiles","show vulnerability-profile","",                              "",                                 "vulnerability exploit protection"),
    ("wildfire-profile",        "security", "/config/security/v1/wildfire-anti-virus-profiles","LRCUD","security_profiles","show wildfire-profile",         "",                              "",                                 "WildFire malware analysis settings"),
    ("dns-security-profile",    "security", "/config/security/v1/dns-security-profiles", "LRCUD", "security_profiles",     "",                               "",                              "",                                 "DNS sinkholing and threat prevention"),
    ("data-filtering-profile",  "security", "/config/security/v1/data-filtering-profiles","LRCUD","security_profiles",    "",                               "",                              "",                                 "data loss prevention (DLP) profile"),
    ("file-blocking-profile",   "security", "/config/security/v1/file-blocking-profiles","LRCUD","security_profiles",     "",                               "",                              "",                                 "file type blocking profile"),
    ("url-access-profile",      "security", "/config/security/v1/url-access-profiles",   "LRCUD", "security_profiles",     "",                               "",                              "",                                 "URL filtering access profile"),
    ("url-admin-override",      "security", "/config/security/v1/url-admin-override",    "LCD",   "url_admin_override",    "",                               "",                              "",                                 "admin password for overriding URL filtering"),
    ("decryption-exclusion",    "security", "/config/security/v1/decryption-exclusions",  "LRCUD", "decryption_policy",     "",                               "",                              "",                                 "hosts excluded from SSL decryption"),
    ("http-header-profile",     "security", "/config/security/v1/http-header-profiles",  "LRCUD", "security_profiles",     "",                               "",                              "",                                 "HTTP header insertion profiles"),

    ("zone",                    "network",  "/config/network/v1/zones",                  "LRCUD", "create_zone",           "show zone",                      "",                              "",                                 "layer3 | layer2 | virtual-wire | tap | tunnel"),
    ("nat-rule",                "network",  "/config/network/v1/nat-rules",              "LRCUD", "create_nat_rule",       "show nat-rules",                 "",                              "",                                 "source/destination NAT translations"),
    ("pbf-rule",                "network",  "/config/network/v1/pbf-rules",              "LRCUD", "pbf_rules",             "show pbf-rules",                 "",                              "",                                 "policy-based forwarding rules"),
    ("ike-gateway",             "network",  "/config/network/v1/ike-gateways",           "LRCUD", "ipsec_vpn",             "show ike-gateway",               "",                              "",                                 "IKE phase-1 gateway configuration"),
    ("ipsec-tunnel",            "network",  "/config/network/v1/ipsec-tunnels",          "LRCUD", "ipsec_vpn",             "show ipsec-tunnel",              "",                              "",                                 "IPsec phase-2 tunnel configuration"),
    ("ethernet-interface",      "network",  "/config/network/v1/ethernet-interfaces",    "LRCUD", "show_interface",        "show interface",                 "",                              "",                                 "layer3 | layer2 | aggregate_group | tap"),
    ("aggregate-interface",     "network",  "/config/network/v1/aggregate-interfaces",   "LRCUD", "show_interface",        "show interface all",             "",                              "",                                 "layer3 | layer2 LACP aggregate interface"),
    ("loopback-interface",      "network",  "/config/network/v1/loopback-interfaces",    "LRCUD", "show_interface",        "show interface all",             "",                              "",                                 "loopback interface"),
    ("tunnel-interface",        "network",  "/config/network/v1/tunnel-interfaces",      "LRCUD", "ipsec_vpn",             "",                               "",                              "",                                 "IPsec/GRE tunnel interface"),
    ("vlan-interface",          "network",  "/config/network/v1/vlan-interfaces",        "LRCUD", "show_interface",        "",                               "",                              "",                                 "VLAN layer3 sub-interface (static or DHCP)"),
    ("dns-proxy",               "network",  "/config/network/v1/dns-proxies",            "LRCUD", "dns_proxy",             "show dns-proxy",                 "",                              "",                                 "DNS proxy configuration"),
    ("dhcp-interface",          "network",  "/config/network/v1/dhcp-interfaces",        "LRCUD", "dhcp",                  "",                               "",                              "",                                 "DHCP server or relay on an interface"),
    ("sdwan-rule",              "network",  "/config/network/v1/sdwan-rules",            "LRCUD", "sdwan",                 "show sdwan-rules",               "",                              "",                                 "SD-WAN path selection rules"),
    ("qos-profile",             "network",  "/config/network/v1/qos-profiles",           "LRCUD", "qos",                   "show qos-profile",               "",                              "",                                 "QoS bandwidth and priority profile"),
    ("bgp-profile",             "network",  "/config/network/v1/bgp-address-family-profiles","LRCUD","bgp_routing",        "show bgp-profile",               "",                              "",                                 "BGP address-family profile (SCM config)"),
    ("static-route",            "network",  "/config/network/v1/routing/static-routes",  "LRCUD", "show_routing",          "show routing route",             "",                              "",                                 "static routing table entries"),
    ("virtual-router",          "network",  "/config/network/v1/virtual-routers",        "LRCUD", "show_routing",          "show routing summary",           "",                              "",                                 "virtual router (routing domain)"),

    ("authentication-profile",  "identity", "/config/identity/v1/authentication-profiles","LRCUD","authentication",        "show authentication-profile",    "",                              "",                                 "LDAP, RADIUS, SAML, or local auth profile"),
    ("authentication-rule",     "identity", "/config/identity/v1/authentication-rules",  "LRCUD", "authentication",        "show authentication-rules",      "",                              "",                                 "authentication policy rules"),
    ("certificate-profile",     "identity", "/config/identity/v1/certificate-profiles",  "LRCUD", "certificates",          "show certificate-profile",       "",                              "",                                 "certificate verification profile"),
    ("tls-service-profile",     "identity", "/config/identity/v1/tls-service-profiles",  "LRCUD", "certificates",          "show tls-service-profile",       "",                              "",                                 "TLS protocol versions and cipher suites"),
    ("local-user",              "identity", "/config/identity/v1/local-users",           "LRCUD", "local_users",           "show local-user",                "",                              "",                                 "local firewall user account"),
    ("local-user-group",        "identity", "/config/identity/v1/local-user-groups",     "LRCUD", "local_users",           "show local-user-group",          "",                              "",                                 "group of local user accounts"),
    ("radius-server",           "identity", "/config/identity/v1/radius-server-profiles","LRCUD", "authentication",        "show radius-server",             "",                              "",                                 "RADIUS server configuration"),
    ("mfa-server",              "identity", "/config/identity/v1/mfa-servers",           "LRCUD", "authentication",        "show mfa-server",                "",                              "",                                 "multi-factor authentication server"),

    ("folder",                  "setup",    "/config/setup/v1/folders",                  "LRCUD", "show_devices",          "cd folder",                      "set folder",                    "",                                 "SCM folder — use 'set folder <name>' in configure mode"),
    ("snippet",                 "setup",    "/config/setup/v1/snippets",                 "LCU",   "show_snippets",         "show snippet",                   "",                              "",                                 "configuration snippet (reusable config block)"),
]


def slug(resource: str) -> str:
    return resource.replace("/", "-").lower()


def doc_verb_file(verb: str, resource: str) -> Path:
    return DOCS_CMDS / f"{verb}-{slug(resource)}.md"


def has_method(methods: str, letter: str) -> bool:
    return letter in methods


def _variant_section(resource: str) -> str:
    """Build a variants section for the doc if we have schema info."""
    variants = SCHEMA_VARIANTS.get(resource)
    if not variants:
        return ""
    lines = [
        "",
        "## Type variants (oneOf — exactly one required)",
        "",
        "| Variant | Field | Example | Description |",
        "|---------|-------|---------|-------------|",
    ]
    for v in variants:
        lines.append(f"| `{v['title']}` | `{v['field']}` | `{v['example']}` | {v['desc']} |")
    lines.append("")
    return "\n".join(lines)


def write_set_doc(resource: str, domain: str, url: str, flag: str, notes: str) -> bool:
    path = doc_verb_file("set", resource)
    if path.exists():
        return False
    variant_md = _variant_section(resource)
    path.write_text(f"""# set {resource}

Create a **{resource}** object in the active SCM folder.

**Source:** `POST {url}`  
**Feature flag:** `{flag}` — enable with `feature enable {flag}`  
**Schema notes:** {notes}
{variant_md}
## Usage

```text
configure
set {resource} <name> [<type> <value>] [description <text>] [tag <name>]
```

For full schema details run: `help set-{resource}` or see `docs/scm-api/specs/ngfw-{domain}.yaml`

## Example

```text
arc:global > configure
arc:global # feature enable {flag}
arc:global # set {resource} <name> ...
  ✓ {resource.title()} <name> created (id: ...)
```

## Related commands

- `show {resource}` — list {resource} objects
- `delete {resource} <name>` — remove a {resource} object
- `help api-reference` — full API to command mapping
""")
    return True


def write_delete_doc(resource: str, domain: str, url: str, flag: str) -> bool:
    path = doc_verb_file("delete", resource)
    if path.exists():
        return False
    path.write_text(f"""# delete {resource}

Delete a **{resource}** object by name from the active SCM folder.

**Source:** `DELETE {url}/{{id}}`  
**Feature flag:** `delete_objects` or `{flag}`

## Usage

```text
configure
delete {resource} <name>
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete {resource} MyObject
  ✓ {resource.title()} MyObject deleted.
```

## Related commands

- `show {resource}` — list objects (confirm the name before deleting)
- `set {resource} <name>` — create a {resource} object
""")
    return True


def write_show_doc(resource: str, domain: str, url: str, flag: str, notes: str) -> bool:
    path = doc_verb_file("show", resource)
    if path.exists():
        return False
    path.write_text(f"""# show {resource}

List **{resource}** objects in the active SCM folder.

**Source:** `GET {url}?folder=<active-folder>`  
**Feature flag:** `{flag}` — enable with `feature enable {flag}`  
**Schema notes:** {notes}

## Usage

```text
show {resource}
```

## Example

```text
arc:global > feature enable {flag}
arc:global > show {resource}
```

## Related commands

- `set {resource} <name>` — create a {resource} object
- `delete {resource} <name>` — remove a {resource} object
- `help api-reference` — full API to command mapping
""")
    return True


def main() -> None:
    created = {"show": 0, "set": 0, "delete": 0}

    sys.path.insert(0, str(ROOT))
    from app.commands.registry import COMMANDS  # noqa: F401

    print("Generating missing command stubs and docs...\n")

    for (resource, domain, url, methods, flag,
         arc_show, arc_set, arc_delete, notes) in RESOURCES:

        if has_method(methods, "L") and not arc_show:
            if write_show_doc(resource, domain, url, flag, notes):
                print(f"  [created] docs/commands/show-{slug(resource)}.md")
                created["show"] += 1

        if has_method(methods, "C"):
            if write_set_doc(resource, domain, url, flag, notes):
                print(f"  [created] docs/commands/set-{slug(resource)}.md")
                created["set"] += 1

        if has_method(methods, "D"):
            if write_delete_doc(resource, domain, url, flag):
                print(f"  [created] docs/commands/delete-{slug(resource)}.md")
                created["delete"] += 1

    print(f"\nDone.  Created: {created['show']} show, {created['set']} set, {created['delete']} delete docs")
    print(f"\nNote: Files that already existed were NOT overwritten.")
    print(f"      To regenerate: delete the file, then re-run this script.")
    print(f"\nNext steps:")
    print(f"  1. Run: python dev/extract_variants.py  (see what oneOf/anyOf types exist)")
    print(f"  2. Edit SCHEMA_VARIANTS in this file to add variant info for more resources")
    print(f"  3. Run: python dev/gen_api_reference.py  (regenerate the summary table)")


if __name__ == "__main__":
    main()

Run: python dev/gen_stub_commands.py

What it does:
  1. Reads the master API resource table below
  2. For each resource with POST → creates docs/commands/set-<resource>.md
     and adds a stub CommandDef entry (feature_flag disabled by default)
  3. For each resource with DELETE → creates docs/commands/delete-<resource>.md
  4. For resources with GET not yet in ARC → creates docs/commands/show-<resource>.md
  5. Prints a summary of what was created

The doc stubs show correct usage, required fields, feature flag to enable,
and the pan.dev API path.  Once a developer enables the flag and implements
the full handler, the stub doc becomes the user's reference.

This script is IDEMPOTENT — it will not overwrite existing files.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT      = Path(__file__).resolve().parent.parent
DOCS_CMDS = ROOT / "docs" / "commands"

# ---------------------------------------------------------------------------
# Master API resource table
#
# Each entry: (resource_name, api_domain, base_url_suffix, methods, feature_flag,
#              arc_show_cmd, arc_set_cmd, arc_delete_cmd, notes)
#
# methods: string containing L=List R=GetById C=Create U=Update D=Delete
# arc_*_cmd: existing ARC command string, or "" if not yet implemented
# ---------------------------------------------------------------------------

RESOURCES = [
    # ── Objects ──────────────────────────────────────────────────────────────
    # resource, domain, url_suffix, methods, flag, show, set, delete, notes
    ("address",                 "objects",  "/config/objects/v1/addresses",              "LRCUD", "create_address",        "show address",                   "set address",                   "delete address",                   "ip-netmask | ip-range | ip-wildcard | fqdn"),
    ("address-group",           "objects",  "/config/objects/v1/address-groups",          "LRCUD", "create_address_group",  "show address-group",             "set address-group",             "delete address-group",             "static member list or dynamic tag filter"),
    ("service",                 "objects",  "/config/objects/v1/services",               "LRCUD", "create_service",        "show service",                   "set service",                   "delete service",                   "tcp or udp with port/port-range"),
    ("service-group",           "objects",  "/config/objects/v1/service-groups",          "LRCUD", "create_service_group",  "show service-group",             "set service-group",             "delete service-group",             "named list of service objects"),
    ("tag",                     "objects",  "/config/objects/v1/tags",                   "LRCUD", "create_tag",            "show tag",                       "set tag",                       "delete tag",                       "40 color options, optional comments"),
    ("external-dynamic-list",   "objects",  "/config/objects/v1/external-dynamic-lists", "LRCUD", "create_edl",            "show external-dynamic-list",     "set external-dynamic-list",     "delete external-dynamic-list",     "ip | domain | url | imsi | imei"),
    ("application-group",       "objects",  "/config/objects/v1/application-groups",     "LRCUD", "app_groups",            "show application-group",         "",                              "",                                 "group of predefined applications"),
    ("application-filter",      "objects",  "/config/objects/v1/application-filters",    "LRCUD", "app_groups",            "show application-filter",        "",                              "",                                 "filter based on app attributes"),
    ("schedule",                "objects",  "/config/objects/v1/schedules",              "LRCUD", "schedules",             "show schedule",                  "",                              "",                                 "recurring or non-recurring time windows"),
    ("region",                  "objects",  "/config/objects/v1/regions",               "LRCUD", "regions",               "show region",                    "",                              "",                                 "geographic region definitions"),
    ("hip-object",              "objects",  "/config/objects/v1/hip-objects",            "LRCUD", "hip",                   "show hip-object",                "",                              "",                                 "GlobalProtect host information profile object"),
    ("hip-profile",             "objects",  "/config/objects/v1/hip-profiles",           "LRCUD", "hip",                   "show hip-profile",               "",                              "",                                 "GlobalProtect HIP profile (combines HIP objects)"),
    ("log-forwarding-profile",  "objects",  "/config/objects/v1/log-forwarding-profiles","LRCUD", "log_profiles",          "show log-forwarding-profile",    "",                              "",                                 "log forwarding destinations (syslog, HTTP, panorama)"),
    ("syslog-server-profile",   "objects",  "/config/objects/v1/syslog-server-profiles", "LRCUD", "log_profiles",          "",                               "",                              "",                                 "syslog server configuration for log forwarding"),
    ("http-server-profile",     "objects",  "/config/objects/v1/http-server-profiles",   "LRCUD", "log_profiles",          "",                               "",                              "",                                 "HTTP server profile for log forwarding"),
    ("dynamic-user-group",      "objects",  "/config/objects/v1/dynamic-user-groups",    "LRCUD", "local_users",           "",                               "",                              "",                                 "dynamic group of users matching a filter"),

    # ── Security ─────────────────────────────────────────────────────────────
    ("security-rule",           "security", "/config/security/v1/security-rules",        "LRCUD", "create_security_rule",  "show security policy",           "",                              "delete security-rule",             "allow|deny|drop with zone/address/app/service"),
    ("url-category",            "security", "/config/security/v1/url-categories",        "LRCUD", "create_url_category",   "show url-categories",            "set url-category",              "delete url-category",              "custom URL categories for URL filtering policy"),
    ("decryption-rule",         "security", "/config/security/v1/decryption-rules",      "LRCUD", "decryption_policy",     "show decryption-rules",          "",                              "",                                 "SSL/TLS decryption policy rules"),
    ("decryption-profile",      "security", "/config/security/v1/decryption-profiles",   "LRCUD", "decryption_policy",     "show decryption-profile",        "",                              "",                                 "SSL/TLS decryption settings profile"),
    ("dos-protection-rule",     "security", "/config/security/v1/dos-protection-rules",  "LRCUD", "dos_protection",        "show dos-protection-rules",      "",                              "",                                 "DoS protection policy rules"),
    ("dos-protection-profile",  "security", "/config/security/v1/dos-protection-profiles","LRCUD","dos_protection",        "show dos-protection-profile",    "",                              "",                                 "DoS protection threshold settings"),
    ("app-override-rule",       "security", "/config/security/v1/app-override-rules",    "LRCUD", "app_override",          "show app-override-rules",        "",                              "",                                 "override application identification"),
    ("profile-group",           "security", "/config/security/v1/profile-groups",        "LRCUD", "profile_groups",        "show profile-group",             "",                              "",                                 "bundle security profiles into one group"),
    ("anti-spyware-profile",    "security", "/config/security/v1/anti-spyware-profiles", "LRCUD", "security_profiles",     "show anti-spyware-profile",      "",                              "",                                 "spyware/C2 detection settings"),
    ("vulnerability-profile",   "security", "/config/security/v1/vulnerability-protection-profiles","LRCUD","security_profiles","show vulnerability-profile","",                              "",                                 "vulnerability exploit protection"),
    ("wildfire-profile",        "security", "/config/security/v1/wildfire-anti-virus-profiles","LRCUD","security_profiles","show wildfire-profile",         "",                              "",                                 "WildFire malware analysis settings"),
    ("dns-security-profile",    "security", "/config/security/v1/dns-security-profiles", "LRCUD", "security_profiles",     "",                               "",                              "",                                 "DNS sinkholing and threat prevention"),
    ("data-filtering-profile",  "security", "/config/security/v1/data-filtering-profiles","LRCUD","security_profiles",    "",                               "",                              "",                                 "data loss prevention (DLP) profile"),
    ("file-blocking-profile",   "security", "/config/security/v1/file-blocking-profiles","LRCUD","security_profiles",     "",                               "",                              "",                                 "file type blocking profile"),
    ("url-access-profile",      "security", "/config/security/v1/url-access-profiles",   "LRCUD", "security_profiles",     "",                               "",                              "",                                 "URL filtering access profile"),
    ("url-admin-override",      "security", "/config/security/v1/url-admin-override",    "LCD",   "url_admin_override",    "",                               "",                              "",                                 "admin password for overriding URL filtering"),
    ("decryption-exclusion",    "security", "/config/security/v1/decryption-exclusions",  "LRCUD", "decryption_policy",     "",                               "",                              "",                                 "hosts excluded from SSL decryption"),
    ("http-header-profile",     "security", "/config/security/v1/http-header-profiles",  "LRCUD", "security_profiles",     "",                               "",                              "",                                 "HTTP header insertion profiles"),

    # ── Network ──────────────────────────────────────────────────────────────
    ("zone",                    "network",  "/config/network/v1/zones",                  "LRCUD", "create_zone",           "show zone",                      "",                              "",                                 "layer3 | layer2 | virtual-wire | tap | tunnel"),
    ("nat-rule",                "network",  "/config/network/v1/nat-rules",              "LRCUD", "create_nat_rule",       "show nat-rules",                 "",                              "",                                 "source/destination NAT translations"),
    ("pbf-rule",                "network",  "/config/network/v1/pbf-rules",              "LRCUD", "pbf_rules",             "show pbf-rules",                 "",                              "",                                 "policy-based forwarding rules"),
    ("ike-gateway",             "network",  "/config/network/v1/ike-gateways",           "LRCUD", "ipsec_vpn",             "show ike-gateway",               "",                              "",                                 "IKE phase-1 gateway configuration"),
    ("ipsec-tunnel",            "network",  "/config/network/v1/ipsec-tunnels",          "LRCUD", "ipsec_vpn",             "show ipsec-tunnel",              "",                              "",                                 "IPsec phase-2 tunnel configuration"),
    ("ethernet-interface",      "network",  "/config/network/v1/ethernet-interfaces",    "LRCUD", "show_interface",        "show interface",                 "",                              "",                                 "physical ethernet interface configuration"),
    ("aggregate-interface",     "network",  "/config/network/v1/aggregate-interfaces",   "LRCUD", "show_interface",        "show interface all",             "",                              "",                                 "aggregate (LACP/802.3ad) interface"),
    ("loopback-interface",      "network",  "/config/network/v1/loopback-interfaces",    "LRCUD", "show_interface",        "show interface all",             "",                              "",                                 "loopback interface"),
    ("tunnel-interface",        "network",  "/config/network/v1/tunnel-interfaces",      "LRCUD", "ipsec_vpn",             "",                               "",                              "",                                 "IPsec/GRE tunnel interface"),
    ("vlan-interface",          "network",  "/config/network/v1/vlan-interfaces",        "LRCUD", "show_interface",        "",                               "",                              "",                                 "VLAN (layer 3 sub-interface)"),
    ("dns-proxy",               "network",  "/config/network/v1/dns-proxies",            "LRCUD", "dns_proxy",             "show dns-proxy",                 "",                              "",                                 "DNS proxy configuration"),
    ("dhcp-interface",          "network",  "/config/network/v1/dhcp-interfaces",        "LRCUD", "dhcp",                  "",                               "",                              "",                                 "DHCP server or relay on an interface"),
    ("sdwan-rule",              "network",  "/config/network/v1/sdwan-rules",            "LRCUD", "sdwan",                 "show sdwan-rules",               "",                              "",                                 "SD-WAN path selection rules"),
    ("qos-profile",             "network",  "/config/network/v1/qos-profiles",           "LRCUD", "qos",                   "show qos-profile",               "",                              "",                                 "QoS bandwidth and priority profile"),
    ("bgp-profile",             "network",  "/config/network/v1/bgp-address-family-profiles","LRCUD","bgp_routing",        "show bgp-profile",               "",                              "",                                 "BGP address-family profile (SCM config)"),
    ("static-route",            "network",  "/config/network/v1/routing/static-routes",  "LRCUD", "show_routing",          "show routing route",             "",                              "",                                 "static routing table entries"),
    ("virtual-router",          "network",  "/config/network/v1/virtual-routers",        "LRCUD", "show_routing",          "show routing summary",           "",                              "",                                 "virtual router (routing domain)"),

    # ── Identity ─────────────────────────────────────────────────────────────
    ("authentication-profile",  "identity", "/config/identity/v1/authentication-profiles","LRCUD","authentication",        "show authentication-profile",    "",                              "",                                 "LDAP, RADIUS, SAML, or local auth profile"),
    ("authentication-rule",     "identity", "/config/identity/v1/authentication-rules",  "LRCUD", "authentication",        "show authentication-rules",      "",                              "",                                 "authentication policy rules"),
    ("certificate-profile",     "identity", "/config/identity/v1/certificate-profiles",  "LRCUD", "certificates",          "show certificate-profile",       "",                              "",                                 "certificate verification profile"),
    ("tls-service-profile",     "identity", "/config/identity/v1/tls-service-profiles",  "LRCUD", "certificates",          "show tls-service-profile",       "",                              "",                                 "TLS protocol versions and cipher suites"),
    ("local-user",              "identity", "/config/identity/v1/local-users",           "LRCUD", "local_users",           "show local-user",                "",                              "",                                 "local firewall user account"),
    ("local-user-group",        "identity", "/config/identity/v1/local-user-groups",     "LRCUD", "local_users",           "show local-user-group",          "",                              "",                                 "group of local user accounts"),
    ("radius-server",           "identity", "/config/identity/v1/radius-server-profiles","LRCUD", "authentication",        "show radius-server",             "",                              "",                                 "RADIUS server configuration"),
    ("mfa-server",              "identity", "/config/identity/v1/mfa-servers",           "LRCUD", "authentication",        "show mfa-server",                "",                              "",                                 "multi-factor authentication server"),

    # ── Setup ─────────────────────────────────────────────────────────────────
    ("folder",                  "setup",    "/config/setup/v1/folders",                  "LRCUD", "show_devices",          "cd folder",                      "set folder",                    "",                                 "SCM folder — use 'set folder <name>' in configure mode"),
    ("snippet",                 "setup",    "/config/setup/v1/snippets",                 "LCU",   "show_snippets",         "show snippet",                   "",                              "",                                 "configuration snippet (reusable config block)"),
]


def slug(resource: str) -> str:
    return resource.replace("/", "-").lower()


def doc_verb_file(verb: str, resource: str) -> Path:
    return DOCS_CMDS / f"{verb}-{slug(resource)}.md"


def has_method(methods: str, letter: str) -> bool:
    return letter in methods


def method_list(methods: str) -> list[str]:
    m = []
    if "L" in methods:
        m.append("GET (list)")
    if "R" in methods:
        m.append("GET (by id)")
    if "C" in methods:
        m.append("POST (create)")
    if "U" in methods:
        m.append("PUT (update)")
    if "D" in methods:
        m.append("DELETE")
    return m


def write_set_doc(resource: str, domain: str, url: str, flag: str, notes: str) -> bool:
    path = doc_verb_file("set", resource)
    if path.exists():
        return False
    cmd = f"set {resource}"
    path.write_text(f"""# {cmd}

Create a **{resource}** object in the active SCM folder.

## Feature flag

This command requires the **`{flag}`** feature flag to be enabled:

```bash
# Enable for this session:
arc> feature enable {flag}

# Enable permanently (config/features.json — git-ignored):
{{"  \\"{flag}\\": true"}}
```

## Syntax

```text
configure
set {resource} <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST {url}
```

{notes and f'''Resource notes: {notes}''' or ''}

## Supported methods

{chr(10).join(f'- {m}' for m in ["GET (list)", "POST (create)", "PUT (update)", "DELETE"])}

## Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `name` | Yes | Object name (must be unique in folder) |
| `folder` | Yes | Set automatically from active folder context |
| `description` | No | Human-readable description |
| `tag` | No | One or more tag names to associate |

> **Full schema:** See `docs/scm-api/specs/ngfw-{domain}.md` for all fields.

## Example

```text
arc:global > configure
arc:global # feature enable {flag}
arc:global # set {resource} MyObject ...
  ✓ {resource.title()} MyObject created (id: ...)
```

## Related commands

- `show {resource}` — list {resource} objects in the active folder
- `delete {resource} <name>` — remove a {resource} object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
""")
    return True


def write_delete_doc(resource: str, domain: str, url: str, flag: str) -> bool:
    path = doc_verb_file("delete", resource)
    if path.exists():
        return False
    cmd = f"delete {resource}"
    path.write_text(f"""# {cmd}

Delete a **{resource}** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`{flag}`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete {resource} <name>
```

## API

```
DELETE {url}/{{id}}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete {resource} MyObject
  ✓ {resource.title()} MyObject deleted.
```

## Related commands

- `show {resource}` — list {resource} objects (to confirm name)
- `set {resource} <name>` — create a {resource} object

---
*Generated stub.*
""")
    return True


def write_show_doc(resource: str, domain: str, url: str, flag: str, notes: str) -> bool:
    path = doc_verb_file("show", resource)
    if path.exists():
        return False
    cmd = f"show {resource}"
    path.write_text(f"""# {cmd}

List **{resource}** objects in the active SCM folder.

## Feature flag

This command requires **`{flag}`** to be enabled:

```bash
arc> feature enable {flag}
```

## Syntax

```text
show {resource}
show {resource} --remote    # live device state via SSH
```

## API

```
GET {url}?folder=<active-folder>
```

{notes and f'''Notes: {notes}''' or ''}

## Output

Returns a table of {resource} objects with key fields.

## Example

```text
arc:global > feature enable {flag}
arc:global > show {resource}
  Name           ...
  ─────────────  ...
  my-object      ...
```

## Related commands

- `set {resource} <name>` — create a {resource} object
- `delete {resource} <name>` — remove a {resource} object
- `help features` — manage feature flags

---
*Generated stub.*
""")
    return True


def main() -> None:
    created = {"show": 0, "set": 0, "delete": 0}

    # Load existing arc commands to know what's already there
    sys.path.insert(0, str(ROOT))
    from app.commands.registry import COMMANDS  # noqa: F401

    existing_show   = {k for k in COMMANDS if k.startswith("show")}
    existing_set    = {k for k in COMMANDS if k.startswith("set")}
    existing_delete = {k for k in COMMANDS if k.startswith("delete")}

    print("Generating missing command stubs and docs...\n")

    for (resource, domain, url, methods, flag,
         arc_show, arc_set, arc_delete, notes) in RESOURCES:

        # show docs
        if has_method(methods, "L") and not arc_show:
            if write_show_doc(resource, domain, url, flag, notes):
                print(f"  [created] docs/commands/show-{slug(resource)}.md")
                created["show"] += 1

        # set docs
        if has_method(methods, "C"):
            if write_set_doc(resource, domain, url, flag, notes):
                print(f"  [created] docs/commands/set-{slug(resource)}.md")
                created["set"] += 1

        # delete docs
        if has_method(methods, "D"):
            if write_delete_doc(resource, domain, url, flag):
                print(f"  [created] docs/commands/delete-{slug(resource)}.md")
                created["delete"] += 1

    print(f"\nDone.  Created: {created['show']} show, {created['set']} set, {created['delete']} delete docs")
    print(f"Existing docs (not overwritten): already present in docs/commands/")
    print(f"\nNext steps:")
    print(f"  1. Review generated stubs in docs/commands/")
    print(f"  2. Enable flags in config/features.json to test")
    print(f"  3. Implement handlers in app/commands/<module>.py")
    print(f"  4. Run: python dev/smoke_test.py --only 1,2,3")


if __name__ == "__main__":
    main()

