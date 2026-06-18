"""ARC runtime feature flags.

Controls which commands are visible and executable. This lets you add a new
command to the registry but keep it hidden from users until it is polished.

Precedence (last wins):
  1. FeatureFlags defaults below  (ship state — what's on for everyone)
  2. config/features.json         (local dev overrides — git-ignored)
  3. ARC_FEATURE_<NAME>=1/0       (environment variable — CI / one-shot)

When a flag is OFF for a command:
  - The command is hidden from ? help output
  - Running it prints "Feature '<x>' is not enabled" + how to enable
  - The CommandDef still exists in the registry (for smoke tests / scaffolding)

Adding a new feature:
  1. Add flag to FeatureFlags below with default=False
  2. Set feature_flag='your_flag' on the CommandDef
  3. Enable locally: add {"your_flag": true} to config/features.json
  4. When ready to ship: flip default to True in FeatureFlags

Agent notes:
  - Read this file when asked "what features are available / enabled"
  - Run `python -c "from app.features import load_features; print(load_features())"` to
    check the current active state including local overrides
"""

from __future__ import annotations

import json
import logging
import os
from dataclasses import asdict, dataclass, field
from pathlib import Path

logger = logging.getLogger(__name__)

_PROJECT_ROOT    = Path(__file__).resolve().parent.parent
_FEATURES_FILE   = _PROJECT_ROOT / "config" / "features.json"
_FEATURES_EXAMPLE = _PROJECT_ROOT / "config" / "features.example.json"


@dataclass
class FeatureFlags:
    """Every flag here gates one or more CommandDef entries.

    Default=True   → shipped and on for all users
    Default=False  → in development; enable locally via config/features.json

    Object families already shipped and their address subtypes:

    ADDRESS OBJECTS:
      show_address / show_address_group
      Subtypes: ip-netmask (10.1.0.0/24), ip-range (10.1.0.1-10.1.0.10),
                ip-wildcard (10.1.0.0/255.0.255.0), fqdn (*.example.com)

    SERVICE OBJECTS:
      show_service
      Subtypes: tcp, udp, application-default, any-port, port-range

    Use `help features` or `feature show` inside ARC for the full flag reference.
    """

    # =========================================================================
    # SHIPPED COMMANDS — default True (on for all users).
    # Set to False in config/features.json to hide a command from the CLI.
    # =========================================================================

    # ── Objects ─────────────────────────────────────────────────────────────
    show_address:               bool = True    # show address
    show_address_group:         bool = True    # show address-group
    show_service:               bool = True    # show service
    show_tag:                   bool = True    # show tag
    show_external_dynamic_list: bool = True    # show external-dynamic-list

    # ── Security ─────────────────────────────────────────────────────────────
    show_security_policy:       bool = True    # show security policy
    show_url_categories:        bool = True    # show url-categories
    test_security_policy_match: bool = True    # test security-policy-match

    # ── Network ──────────────────────────────────────────────────────────────
    show_interface:             bool = True    # show interface / show interface all
    show_zone:                  bool = True    # show zone
    show_routing:               bool = True    # show routing route / routing summary
    show_high_availability:     bool = True    # show high-availability all / state

    # ── Setup / Inventory ────────────────────────────────────────────────────
    show_devices:               bool = True    # show devices / show device / show device snippets
    show_snippets:              bool = True    # show snippets / show snippet / show snippets global
    show_jobs:                  bool = True    # show jobs all / show jobs id

    # ── Operations (live device — SSH / --remote) ────────────────────────────
    show_system_info:           bool = True    # show system info
    show_system_resources:      bool = True    # show system resources
    show_system_disk_space:     bool = True    # show system disk-space
    show_log_system:            bool = True    # show log system
    show_log_traffic:           bool = True    # show log traffic
    ping:                       bool = True    # ping host
    request_system_software:    bool = True    # request system software check

    # ── Config operations ────────────────────────────────────────────────────
    commit:                     bool = True    # commit (configure mode)

    # =========================================================================
    # WRITE OPERATIONS — configure mode required, default False.
    # These gate `set` (create/modify) and `delete` commands.
    # Enable individually via config/features.json.
    #
    # Naming: create_<resource>  /  delete_<resource>
    #   True  = command visible and executable in configure mode
    #   False = command hidden; running it prints "feature not enabled"
    # =========================================================================

    # ── Update operations (objects domain) ──────────────────────────────────
    # PUT requires the full object; ARC does GET→merge→PUT automatically.
    update_objects:         bool = False   # update address/service/tag/address-group/edl/service-group
    create_address:         bool = False   # set address <name> ip-netmask/fqdn/ip-range <value>
    create_address_group:   bool = False   # set address-group <name> static <members>
    create_service:         bool = False   # set service <name> tcp/udp port <n>
    create_service_group:   bool = False   # set service-group <name> members <list>
    create_tag:             bool = False   # set tag <name> [color <color>]
    create_edl:             bool = False   # set external-dynamic-list <name> type <t> url <u>
    delete_objects:         bool = False   # delete address/service/tag/address-group/etc.

    # ── Security — create/delete ─────────────────────────────────────────────
    create_security_rule:   bool = False   # set security-rule <name>
    create_url_category:    bool = False   # set url-category <name> type <t> list <urls>
    delete_security:        bool = False   # delete security-rule/url-category

    # ── Network — create/delete ──────────────────────────────────────────────
    create_zone:            bool = False   # set zone <name> [type layer3]  ← placeholder, no handler yet
    create_nat_rule:        bool = False   # set nat-rule <name>             ← placeholder, no handler yet
    delete_network:         bool = False   # delete zone/interface/route     ← placeholder, no handler yet

    # ── Update (future domains) ──────────────────────────────────────────────
    update_security:        bool = False   # update security-rule/url-category ← placeholder, no handler yet
    update_network:         bool = False   # update nat-rule/zone               ← placeholder, no handler yet

    # =========================================================================
    # UNIMPLEMENTED / IN-DEVELOPMENT — default False.
    # Enable locally via config/features.json when working on a command.
    # =========================================================================

    # ── Network (unimplemented SCM config) ────────────────────────────────────
    nat_rules:           bool = False   # show nat-rules (SCM: /config/network/v1/nat-rules)
    pbf_rules:           bool = False   # show pbf-rules (SCM: /config/network/v1/pbf-rules)
    ipsec_vpn:           bool = False   # show ike-gateway / ipsec-tunnel (SCM config)
                                        # + show vpn ike-sa / vpn tunnel (SSH live state)
    bgp_routing:         bool = False   # show bgp-routing-profile (SCM)
                                        # + show routing bgp peer/summary (SSH live)
    sdwan:               bool = False   # show sdwan-rules (SCM: /config/network/v1/sdwan-rules)
    dhcp:                bool = False   # show dhcp (SCM: /config/network/v1/dhcp-interfaces)
    dns_proxy:           bool = False   # show dns-proxy (SCM: /config/network/v1/dns-proxies)
    qos:                 bool = False   # show qos-profile (SCM: /config/network/v1/qos-profiles)
    logical_routers:     bool = False   # show logical-router (placeholder, no handler yet)
    vpn_auto:            bool = False   # show auto-vpn (placeholder, no handler yet)

    # ── Security (unimplemented) ──────────────────────────────────────────────
    decryption_policy:   bool = False   # show decryption-rules / decryption-profile
    dos_protection:      bool = False   # show dos-protection-rules / dos-protection-profile
    app_override:        bool = False   # show app-override-rules
    profile_groups:      bool = False   # show profile-group
    url_admin_override:  bool = False   # show url-admin-override (placeholder, no handler yet)
    security_profiles:   bool = False   # show anti-spyware / vulnerability / wildfire / dns-security profiles

    # ── Identity (unimplemented) ──────────────────────────────────────────────
    authentication:      bool = False   # show authentication-profile / authentication-rule
                                        # + show radius-server / ldap-server / mfa-server
    certificates:        bool = False   # show certificate-profile / tls-service-profile
    local_users:         bool = False   # show local-user / local-user-group
                                        # + show user ip-user-mapping (SSH live)

    # ── Objects (unimplemented) ───────────────────────────────────────────────
    app_groups:          bool = False   # show application-group / application-filter
    service_groups:      bool = False   # show service-group
    schedules:           bool = False   # show schedule
    regions:             bool = False   # show region
    hip:                 bool = False   # show hip-object / hip-profile (GlobalProtect)
    log_profiles:        bool = False   # show log-forwarding-profile

    # ── Device Settings (unimplemented — placeholder) ────────────────────────
    device_settings:     bool = False   # show general-settings / management-interface / session-settings

    # ── Live device only — SSH --remote required ──────────────────────────────
    show_arp:            bool = False   # show arp (PAN-OS: show arp all)
    show_sessions:       bool = False   # show session all / info / id
    show_routing_live:   bool = False   # show routing protocol bgp peer/summary (placeholder, no handler yet)
    traceroute:          bool = False   # traceroute host <ip>
    test_nat:            bool = False   # test nat-policy-match
    test_url:            bool = False   # test url <url>
    request_system_reboot: bool = False # request system reboot / shutdown (with confirmation)

    # ── Operations (placeholder — no handler yet) ─────────────────────────────
    onboarding:          bool = False   # device onboarding APIs (placeholder)


def load_features() -> FeatureFlags:
    """Load feature flags, applying local config and env-var overrides.

    Returns a FeatureFlags instance with effective values.
    """
    flags = FeatureFlags()  # start from code defaults

    # Layer 2: config/features.json overrides
    if _FEATURES_FILE.exists():
        try:
            overrides = json.loads(_FEATURES_FILE.read_text(encoding="utf-8"))
            for key, val in overrides.items():
                if hasattr(flags, key) and isinstance(val, bool):
                    setattr(flags, key, val)
                elif hasattr(flags, key):
                    logger.warning("features.json: '%s' value must be true/false, got %r", key, val)
                else:
                    logger.warning("features.json: unknown flag '%s' — ignored", key)
        except (json.JSONDecodeError, OSError) as exc:
            logger.warning("Could not read config/features.json: %s", exc)

    # Layer 3: environment variable overrides
    # ARC_FEATURE_NAT_RULES=1 → nat_rules=True
    for flag_name in asdict(flags):
        env_key = f"ARC_FEATURE_{flag_name.upper()}"
        env_val = os.environ.get(env_key)
        if env_val is not None:
            setattr(flags, flag_name, env_val.strip() not in ("0", "false", "no", ""))

    return flags


def is_enabled(flags: FeatureFlags, flag_name: str) -> bool:
    """Return True when *flag_name* is enabled in *flags*.

    An empty *flag_name* (the default on CommandDef) always returns True —
    commands without a flag are never gated.
    """
    if not flag_name:
        return True
    return bool(getattr(flags, flag_name, False))


def _write_example() -> None:
    """Write config/features.example.json from current flag defaults.

    Called by gen_api_index and scaffold when adding a new flagged command.
    """
    flags = FeatureFlags()
    example: dict[str, bool] = {}
    for k, v in asdict(flags).items():
        example[k] = v

    _FEATURES_EXAMPLE.parent.mkdir(parents=True, exist_ok=True)
    _FEATURES_EXAMPLE.write_text(
        json.dumps(example, indent=2) + "\n", encoding="utf-8"
    )

