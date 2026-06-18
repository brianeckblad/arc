# ARC Command API Reference

Complete mapping of SCM REST API resources to ARC commands.

| Symbol | Meaning |
|--------|---------|
| `yes`  | Implemented, enabled by default |
| `stub` | Help doc exists; enable feature flag to use |
| `-`    | Not yet in ARC |

Methods: L=List  R=GetById  C=Create  U=Update  D=Delete

---

## Objects

| Resource | Methods | show | set | delete | Feature Flag |
|---|---|---|---|---|---|
| `address` | LRCUD | yes | yes | yes | `create_address` |
| `address-group` | LRCUD | yes | yes | yes | `create_address_group` |
| `service` | LRCUD | yes | yes | yes | `create_service` |
| `service-group` | LRCUD | yes | yes | yes | `create_service_group` |
| `tag` | LRCUD | yes | yes | yes | `create_tag` |
| `external-dynamic-list` | LRCUD | yes | yes | yes | `create_edl` |
| `application-group` | LRCUD | yes | stub | stub | `app_groups` |
| `application-filter` | LRCUD | yes | stub | stub | `app_groups` |
| `schedule` | LRCUD | yes | stub | stub | `schedules` |
| `region` | LRCUD | yes | stub | stub | `regions` |
| `hip-object` | LRCUD | yes | stub | stub | `hip` |
| `hip-profile` | LRCUD | yes | stub | stub | `hip` |
| `log-forwarding-profile` | LRCUD | yes | stub | stub | `log_profiles` |
| `syslog-server-profile` | LRCUD | - | stub | stub | `log_profiles` |
| `http-server-profile` | LRCUD | - | stub | stub | `log_profiles` |
| `dynamic-user-group` | LRCUD | - | stub | stub | `local_users` |

## Security

| Resource | Methods | show | set | delete | Feature Flag |
|---|---|---|---|---|---|
| `security-rule` | LRCUD | yes | stub | yes | `create_security_rule` |
| `url-category` | LRCUD | yes | yes | yes | `create_url_category` |
| `decryption-rule` | LRCUD | yes | stub | stub | `decryption_policy` |
| `decryption-profile` | LRCUD | yes | stub | stub | `decryption_policy` |
| `dos-protection-rule` | LRCUD | yes | stub | stub | `dos_protection` |
| `dos-protection-profile` | LRCUD | yes | stub | stub | `dos_protection` |
| `app-override-rule` | LRCUD | yes | stub | stub | `app_override` |
| `profile-group` | LRCUD | yes | stub | stub | `profile_groups` |
| `anti-spyware-profile` | LRCUD | yes | stub | stub | `security_profiles` |
| `vulnerability-profile` | LRCUD | yes | stub | stub | `security_profiles` |
| `wildfire-profile` | LRCUD | yes | stub | stub | `security_profiles` |
| `dns-security-profile` | LRCUD | - | stub | stub | `security_profiles` |
| `data-filtering-profile` | LRCUD | - | stub | stub | `security_profiles` |
| `file-blocking-profile` | LRCUD | - | stub | stub | `security_profiles` |
| `url-access-profile` | LRCUD | - | stub | stub | `security_profiles` |
| `url-admin-override` | LCD | - | stub | stub | `url_admin_override` |
| `decryption-exclusion` | LRCUD | - | stub | stub | `decryption_policy` |
| `http-header-profile` | LRCUD | - | stub | stub | `security_profiles` |

## Network

| Resource | Methods | show | set | delete | Feature Flag |
|---|---|---|---|---|---|
| `zone` | LRCUD | yes | stub | stub | `create_zone` |
| `nat-rule` | LRCUD | yes | stub | stub | `create_nat_rule` |
| `pbf-rule` | LRCUD | yes | stub | stub | `pbf_rules` |
| `ike-gateway` | LRCUD | yes | stub | stub | `ipsec_vpn` |
| `ipsec-tunnel` | LRCUD | yes | stub | stub | `ipsec_vpn` |
| `ethernet-interface` | LRCUD | yes | stub | stub | `show_interface` |
| `aggregate-interface` | LRCUD | yes | stub | stub | `show_interface` |
| `loopback-interface` | LRCUD | yes | stub | stub | `show_interface` |
| `tunnel-interface` | LRCUD | - | stub | stub | `ipsec_vpn` |
| `vlan-interface` | LRCUD | - | stub | stub | `show_interface` |
| `dns-proxy` | LRCUD | yes | stub | stub | `dns_proxy` |
| `dhcp-interface` | LRCUD | - | stub | stub | `dhcp` |
| `sdwan-rule` | LRCUD | yes | stub | stub | `sdwan` |
| `qos-profile` | LRCUD | yes | stub | stub | `qos` |
| `bgp-profile` | LRCUD | yes | stub | stub | `bgp_routing` |
| `static-route` | LRCUD | yes | stub | stub | `show_routing` |
| `virtual-router` | LRCUD | yes | stub | stub | `show_routing` |

## Identity

| Resource | Methods | show | set | delete | Feature Flag |
|---|---|---|---|---|---|
| `authentication-profile` | LRCUD | yes | stub | stub | `authentication` |
| `authentication-rule` | LRCUD | yes | stub | stub | `authentication` |
| `certificate-profile` | LRCUD | yes | stub | stub | `certificates` |
| `tls-service-profile` | LRCUD | yes | stub | stub | `certificates` |
| `local-user` | LRCUD | yes | stub | stub | `local_users` |
| `local-user-group` | LRCUD | yes | stub | stub | `local_users` |
| `radius-server` | LRCUD | yes | stub | stub | `authentication` |
| `mfa-server` | LRCUD | yes | stub | stub | `authentication` |

## Setup

| Resource | Methods | show | set | delete | Feature Flag |
|---|---|---|---|---|---|
| `folder` | LRCUD | yes | yes | stub | `show_devices` |
| `snippet` | LCU | yes | stub | - | `show_snippets` |

---

## Usage

Inside ARC:
```
help api-reference          # view this table
feature show                # see all feature flags and their status
feature enable <flag>       # enable a command family
help set-<resource>         # view usage for a specific set command
help delete-<resource>      # view usage for a specific delete command
```

## Refresh API docs

```bash
python dev/update_scm_docs.py    # pull latest specs from pan.dev
python dev/gen_stub_commands.py  # regenerate missing stub docs
```
