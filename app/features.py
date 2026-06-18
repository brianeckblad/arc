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

    Default=True   → shipped, on for everyone
    Default=False  → in development; enable locally via config/features.json

    Object families already shipped (no flag — always enabled):

    ADDRESS OBJECTS:
      show address               → all types: ip-netmask, ip-range, ip-wildcard, fqdn
      show address-group         → static groups and dynamic (tag-based) groups
      Subtypes: ip-netmask (10.1.0.0/24), ip-range (10.1.0.1-10.1.0.10),
                ip-wildcard (10.1.0.0/255.0.255.0), fqdn (*.example.com)

    SERVICE OBJECTS:
      show service               → tcp/udp port-based services
      Subtypes: tcp, udp, application-default, any-port, port-range

    TAGS:
      show tag                   → all tags (used for dynamic address groups)

    EDLs:
      show external-dynamic-list → ip, domain, url, imsi, imei types

    Use `help features` inside ARC for the full flag reference with enabled/disabled status.
    """

    # ── Implemented & shipped (always on) ──────────────────────────────
    # Core show commands — addresses, services, zones, routes, etc.
    # These have no flag (feature_flag="" on CommandDef) so they can never
    # be accidentally disabled.

    # ── Network ─────────────────────────────────────────────────────────
    # Set to True when the SCM command is implemented and tested.
    nat_rules:           bool = False   # show nat-rules / create / delete
    ipsec_vpn:           bool = False   # show ipsec-tunnels, ike-gateways
    bgp_routing:         bool = False   # show bgp peers, bgp profiles
    pbf_rules:           bool = False   # show pbf-rules
    sdwan:               bool = False   # show sdwan-rules, profiles
    dhcp:                bool = False   # show dhcp-interfaces
    dns_proxy:           bool = False   # show dns-proxies
    qos:                 bool = False   # show qos-rules, qos-profiles
    logical_routers:     bool = False   # show logical-routers
    vpn_auto:            bool = False   # show auto-vpn-clusters

    # ── Security ────────────────────────────────────────────────────────
    decryption_policy:   bool = False   # show decryption-rules / profiles
    dos_protection:      bool = False   # show dos-protection-rules / profiles
    app_override:        bool = False   # show app-override-rules
    profile_groups:      bool = False   # show profile-groups
    url_admin_override:  bool = False   # show url-admin-override

    # ── Identity ────────────────────────────────────────────────────────
    authentication:      bool = False   # show authentication-profiles / rules
    certificates:        bool = False   # show certificates / cert-profiles
    local_users:         bool = False   # show local-users / user-groups

    # ── Objects ─────────────────────────────────────────────────────────
    app_groups:          bool = False   # show application-groups / filters
    schedules:           bool = False   # show schedules
    regions:             bool = False   # show regions

    # ── Device Settings ─────────────────────────────────────────────────
    device_settings:     bool = False   # show general-settings / mgmt-interface
    ha_config:           bool = True    # show high-availability (already shipped)

    # ── Operations ──────────────────────────────────────────────────────
    onboarding:          bool = False   # device onboarding APIs


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

