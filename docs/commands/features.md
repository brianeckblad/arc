# feature — Feature Flags

Control which commands are visible and executable in ARC.  Feature flags allow
commands to be hidden, disabled, or worked on individually without affecting the rest of the CLI.

Every command — including all shipped commands — has a feature flag.
Flags for shipped commands default to `True`; flags for unimplemented commands default to `False`.

## Usage

```text
feature show                   List all flags grouped by shipped / in-development
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
# config/features.json (git-ignored) — one entry per flag to override
{
  "nat_rules": true,
  "show_address": false
}

# Or use an environment variable for a single session:
ARC_FEATURE_NAT_RULES=1 arc
ARC_FEATURE_SHOW_ADDRESS=0 arc
```

## Shipped commands — default `True`

These flags are `True` by default.  Set to `false` to hide a command you don't need.

### Objects
| Flag | Commands controlled |
|------|---------------------|
| `show_address` | `show address` |
| `show_address_group` | `show address-group` |
| `show_service` | `show service` |
| `show_tag` | `show tag` |
| `show_external_dynamic_list` | `show external-dynamic-list` |

### Security
| Flag | Commands controlled |
|------|---------------------|
| `show_security_policy` | `show security policy` |
| `show_url_categories` | `show url-categories` |
| `test_security_policy_match` | `test security-policy-match` |

### Network
| Flag | Commands controlled |
|------|---------------------|
| `show_interface` | `show interface`, `show interface all` |
| `show_zone` | `show zone` |
| `show_routing` | `show routing route`, `show routing summary` |
| `show_high_availability` | `show high-availability all`, `show high-availability state` |

### Setup / Inventory
| Flag | Commands controlled |
|------|---------------------|
| `show_devices` | `show devices`, `show device`, `show device snippets` |
| `show_snippets` | `show snippets`, `show snippet`, `show snippets global` |
| `show_jobs` | `show jobs all`, `show jobs id` |

### Operations (live device — SSH / --remote)
| Flag | Commands controlled |
|------|---------------------|
| `show_system_info` | `show system info` |
| `show_system_resources` | `show system resources` |
| `show_system_disk_space` | `show system disk-space` |
| `show_log_system` | `show log system` |
| `show_log_traffic` | `show log traffic` |
| `ping` | `ping host` |
| `request_system_software` | `request system software check` |

### Config operations
| Flag | Commands controlled |
|------|---------------------|
| `commit` | `commit` (configure mode) |

---

## Unimplemented / in-development — default `False`

These flags are `False` by default.  Enable them locally while building a new command.

### Network (unimplemented)
| Flag | Planned commands |
|------|-----------------|
| `nat_rules` | `show nat-rules`, create/delete NAT rules |
| `ipsec_vpn` | `show ipsec-tunnels`, IKE gateways |
| `bgp_routing` | `show bgp peers`, BGP routing profiles |
| `pbf_rules` | `show pbf-rules` |
| `sdwan` | `show sdwan-rules`, SD-WAN profiles |
| `dhcp` | `show dhcp-interfaces` |
| `dns_proxy` | `show dns-proxies` |
| `qos` | `show qos-rules`, QoS profiles |
| `logical_routers` | `show logical-routers` |
| `vpn_auto` | `show auto-vpn-clusters` |

### Security (unimplemented)
| Flag | Planned commands |
|------|-----------------|
| `decryption_policy` | `show decryption-rules`, decryption profiles |
| `dos_protection` | `show dos-protection-rules`, DoS profiles |
| `app_override` | `show app-override-rules` |
| `profile_groups` | `show profile-groups` |
| `url_admin_override` | `show url-admin-override` |

### Identity (unimplemented)
| Flag | Planned commands |
|------|-----------------|
| `authentication` | `show authentication-profiles`, authentication rules |
| `certificates` | `show certificates`, certificate profiles |
| `local_users` | `show local-users`, user groups |

### Objects (unimplemented)
| Flag | Planned commands |
|------|-----------------|
| `app_groups` | `show application-groups`, application filters |
| `service_groups` | `show service-groups` |
| `schedules` | `show schedules` |
| `regions` | `show regions` |

### Device Settings (unimplemented)
| Flag | Planned commands |
|------|-----------------|
| `device_settings` | `show general-settings`, management interface |

### Operations (unimplemented)
| Flag | Planned commands |
|------|-----------------|
| `onboarding` | Device onboarding API operations |

---

## Examples

```text
arc:global > feature show
  Shipped commands (default: enabled)
    show_address                         on   show address
    show_address_group                   on   show address-group
    show_high_availability               on   show high-availability all, ...
    ...

  Unimplemented / in-development (default: disabled)
    bgp_routing                         off   —
    nat_rules                           off   —
    ...

arc:global > feature disable show_snippets
  show_snippets  →  disabled  (session only)

arc:global > show ?
  # show snippet, show snippets, show snippets global no longer appear

arc:global > feature enable nat_rules
  nat_rules  →  enabled  (session only — edit config/features.json to persist)
```
