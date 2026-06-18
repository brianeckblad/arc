# feature — Feature Flags

Control which commands are visible and executable in ARC.  Feature flags allow
commands to be added to the registry while still in development without
affecting users.

## Usage

```text
feature show                   List all feature flags and their current state
feature enable <flag>          Enable a feature for this session
feature disable <flag>         Disable a feature for this session
feature help                   Show this page
```

## How flags work

| Flag state | What happens |
|---|---|
| **enabled** (`True`) | Command appears in `?` help and executes normally |
| **disabled** (`False`) | Command is hidden from `?` help; running it prints "feature not enabled" |

Changes made with `feature enable/disable` apply **immediately** but are
session-only.  To persist across restarts, edit `config/features.json`.

## Persistence

```bash
# Persist one or more flags:
# config/features.json (git-ignored)
{
  "nat_rules": true,
  "bgp_routing": true
}

# Or use an environment variable for a single session:
ARC_FEATURE_NAT_RULES=1 arc
```

## Flag reference

All flags default to `False` unless noted.  A flag is `True` when the command
it gates is **implemented, tested, and ready to use**.

### Network

| Flag | Default | Gates |
|------|---------|-------|
| `nat_rules` | `False` | `show nat-rules`, create/delete NAT rules |
| `ipsec_vpn` | `False` | `show ipsec-tunnels`, IKE gateways |
| `bgp_routing` | `False` | `show bgp peers`, BGP routing profiles |
| `pbf_rules` | `False` | `show pbf-rules` — policy-based forwarding |
| `sdwan` | `False` | `show sdwan-rules`, SD-WAN profiles |
| `dhcp` | `False` | `show dhcp-interfaces` |
| `dns_proxy` | `False` | `show dns-proxies` |
| `qos` | `False` | `show qos-rules`, QoS profiles |
| `logical_routers` | `False` | `show logical-routers` |
| `vpn_auto` | `False` | `show auto-vpn-clusters` |

### Security

| Flag | Default | Gates |
|------|---------|-------|
| `decryption_policy` | `False` | `show decryption-rules`, decryption profiles |
| `dos_protection` | `False` | `show dos-protection-rules`, DoS profiles |
| `app_override` | `False` | `show app-override-rules` |
| `profile_groups` | `False` | `show profile-groups` |
| `url_admin_override` | `False` | `show url-admin-override` |

### Identity

| Flag | Default | Gates |
|------|---------|-------|
| `authentication` | `False` | `show authentication-profiles`, authentication rules |
| `certificates` | `False` | `show certificates`, certificate profiles |
| `local_users` | `False` | `show local-users`, user groups |

### Objects

| Flag | Default | Gates |
|------|---------|-------|
| `app_groups` | `False` | `show application-groups`, application filters |
| `schedules` | `False` | `show schedules` |
| `regions` | `False` | `show regions` |

### Device Settings

| Flag | Default | Gates |
|------|---------|-------|
| `device_settings` | `False` | `show general-settings`, management interface |
| `ha_config` | `True` | `show high-availability all/state` ← already shipped |

### Operations

| Flag | Default | Gates |
|------|---------|-------|
| `onboarding` | `False` | Device onboarding API operations |

## Examples

```text
arc:global > feature show
  Feature Flags — session state

    bgp_routing                   disabled
    ha_config                      enabled
    nat_rules                     disabled
    ...

arc:global > feature enable nat_rules
  nat_rules  →  enabled  (session only — edit config/features.json to persist)

arc:global > show nat-rules
  ... (now shows NAT rules)

arc:global > feature disable nat_rules
  nat_rules  →  disabled  (session only)
```

