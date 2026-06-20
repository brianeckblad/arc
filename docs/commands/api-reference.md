# ARC Command → SCM API Reference

Generated from each command's doc front-matter (`api:` field) and the live
registry. Regenerate with `python dev/generate_command_docs.py` (runs on `docsupdate`).

## Diagnostics

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `packet-tracer` | folder | `packet_tracer` | (client-side simulation of the folder rule base) |
| `test security-policy-match` | folder | `packet_tracer` | (client-side simulation of the folder rule base) |

## Identity

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `show authentication-portals` | folder | — | — |
| `show authentication-profile` | folder | `authentication` | GET /config/identity/v1/authentication-profiles |
| `show authentication-rules` | folder | `authentication` | GET /config/identity/v1/authentication-rules |
| `show authentication-sequences` | folder | — | — |
| `show certificate-profile` | folder | `certificates` | GET /config/identity/v1/certificate-profiles |
| `show certificates` | folder | — | — |
| `show kerberos-server-profiles` | folder | — | — |
| `show ldap-server-profiles` | folder | — | — |
| `show local-user` | folder | `local_users` | GET /config/identity/v1/local-users |
| `show local-user-group` | folder | `local_users` | GET /config/identity/v1/local-user-groups |
| `show mfa-server` | folder | `authentication` | GET /config/identity/v1/mfa-servers |
| `show ocsp-responders` | folder | — | — |
| `show radius-server` | folder | `authentication` | GET /config/identity/v1/radius-server-profiles |
| `show saml-server-profiles` | folder | — | — |
| `show scep-profiles` | folder | — | — |
| `show tacacs-server-profiles` | folder | — | — |
| `show tls-service-profile` | folder | `certificates` | GET /config/identity/v1/tls-service-profiles |
| `show trusted-certificate-authorities` | folder | — | — |
| `show user ip-user-mapping` | device | `local_users` | (live device state — SSH via --remote) |

## Network

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `show aggregate-interfaces` | folder | — | — |
| `show arp` | device | `show_arp` | (live device state — SSH via --remote) |
| `show auto-vpn-clusters` | folder | — | — |
| `show auto-vpn-monitor` | folder | — | — |
| `show auto-vpn-settings` | folder | — | — |
| `show bgp-auth-profiles` | folder | — | — |
| `show bgp-filtering-profiles` | folder | — | — |
| `show bgp-profile` | folder | `bgp_routing` | GET /config/network/v1/bgp-address-family-profiles |
| `show bgp-redistribution-profiles` | folder | — | — |
| `show bgp-route-map-redistributions` | folder | — | — |
| `show bgp-route-maps` | folder | — | — |
| `show config-match-list` | folder | — | — |
| `show dhcp-interfaces` | folder | — | — |
| `show dns-proxy` | folder | `dns_proxy` | GET /config/network/v1/dns-proxies |
| `show globalprotect-match-list` | folder | — | — |
| `show high-availability all` | folder | `show_high_availability` | GET /config/network/v1/ha |
| `show high-availability state` | folder | `show_high_availability` | GET /config/network/v1/ha |
| `show hipmatch-match-list` | folder | — | — |
| `show ike-crypto-profiles` | folder | — | — |
| `show ike-gateway` | folder | `ipsec_vpn` | GET /config/network/v1/ike-gateways |
| `show interface` | folder | `show_interface` | GET /config/network/v1/ethernet-interfaces |
| `show interface all` | folder | `show_interface` | GET /config/network/v1/ethernet-interfaces |
| `show interface-management-profiles` | folder | — | — |
| `show ipsec-crypto-profiles` | folder | — | — |
| `show ipsec-tunnel` | folder | `ipsec_vpn` | GET /config/network/v1/ipsec-tunnels |
| `show iptag-match-list` | folder | — | — |
| `show layer2-subinterfaces` | folder | — | — |
| `show layer3-subinterfaces` | folder | — | — |
| `show link-tags` | folder | — | — |
| `show lldp-profiles` | folder | — | — |
| `show logical-routers` | folder | — | — |
| `show loopback-interfaces` | folder | — | — |
| `show nat-rules` | folder | `nat_rules` | GET /config/network/v1/nat-rules |
| `show network_packet_broker_profiles` | folder | — | — |
| `show network_packet_broker_rules` | folder | — | — |
| `show ospf-auth-profiles` | folder | — | — |
| `show pbf-rules` | folder | `pbf_rules` | GET /config/network/v1/pbf-rules |
| `show qos-policy-rules` | folder | — | — |
| `show qos-profile` | folder | `qos` | GET /config/network/v1/qos-profiles |
| `show remote-networks-license-info` | folder | — | — |
| `show route-access-lists` | folder | — | — |
| `show route-community-lists` | folder | — | — |
| `show route-path-access-lists` | folder | — | — |
| `show route-prefix-lists` | folder | — | — |
| `show routing bgp` | device | `bgp_routing` | (live device state — SSH via --remote) |
| `show routing route` | folder | `show_routing` | GET /config/network/v1/routing/static-routes |
| `show routing summary` | folder | `show_routing` | GET /config/network/v1/virtual-routers |
| `show sdwan-error-correction-profiles` | folder | — | — |
| `show sdwan-path-quality-profiles` | folder | — | — |
| `show sdwan-rules` | folder | `sdwan` | GET /config/network/v1/sdwan-rules |
| `show sdwan-saas-quality-profiles` | folder | — | — |
| `show sdwan-traffic-distribution-profiles` | folder | — | — |
| `show session all` | device | `show_sessions` | (live device state — SSH via --remote) |
| `show system-match-list` | folder | — | — |
| `show tunnel-interfaces` | folder | — | — |
| `show userid-match-list` | folder | — | — |
| `show vlan-interfaces` | folder | — | — |
| `show vpn ike-sa` | device | `ipsec_vpn` | (live device state — SSH via --remote) |
| `show vpn tunnel` | device | `ipsec_vpn` | (live device state — SSH via --remote) |
| `show zone` | folder | `show_zone` | GET /config/network/v1/zones |
| `show zone-protection-profiles` | folder | — | — |
| `test nat-policy-match` | device | `test_nat` | (live device state — SSH via --remote) |
| `test url` | device | `test_url` | (live device state — SSH via --remote) |
| `traceroute host` | device | `traceroute` | (live device state — SSH via --remote) |

## Objects

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `delete address` | folder | `delete_objects` | DELETE /config/objects/v1/addresses/{id} |
| `delete address-group` | folder | `delete_objects` | DELETE /config/objects/v1/address-groups/{id} |
| `delete external-dynamic-list` | folder | `delete_objects` | DELETE /config/objects/v1/external-dynamic-lists/{id} |
| `delete service` | folder | `delete_objects` | DELETE /config/objects/v1/services/{id} |
| `delete service-group` | folder | `delete_objects` | DELETE /config/objects/v1/service-groups/{id} |
| `delete tag` | folder | `delete_objects` | DELETE /config/objects/v1/tags/{id} |
| `set address` | folder | `create_address` | POST /config/objects/v1/addresses |
| `set address-group` | folder | `create_address_group` | POST /config/objects/v1/address-groups |
| `set external-dynamic-list` | folder | `create_edl` | POST /config/objects/v1/external-dynamic-lists |
| `set service` | folder | `create_service` | POST /config/objects/v1/services |
| `set service-group` | folder | `create_service_group` | POST /config/objects/v1/service-groups |
| `set tag` | folder | `create_tag` | POST /config/objects/v1/tags |
| `show address` | folder | `show_address` | GET /config/objects/v1/addresses |
| `show address-group` | folder | `show_address_group` | GET /config/objects/v1/address-groups |
| `show advanced-device-objects` | folder | — | — |
| `show application-filter` | folder | `app_groups` | GET /config/objects/v1/application-filters |
| `show application-group` | folder | `app_groups` | GET /config/objects/v1/application-groups |
| `show applications` | folder | — | — |
| `show auto-tag-actions` | folder | — | — |
| `show device-context-segments` | folder | — | — |
| `show dynamic-user-groups` | folder | — | — |
| `show external-dynamic-list` | folder | `show_external_dynamic_list` | GET /config/objects/v1/external-dynamic-lists |
| `show hip-object` | folder | `hip` | GET /config/objects/v1/hip-objects |
| `show hip-profile` | folder | `hip` | GET /config/objects/v1/hip-profiles |
| `show http-server-profiles` | folder | — | — |
| `show log-forwarding-profile` | folder | `log_profiles` | GET /config/objects/v1/log-forwarding-profiles |
| `show quarantined-devices` | folder | — | — |
| `show region` | global | `regions` | GET /config/objects/v1/regions |
| `show schedule` | folder | `schedules` | GET /config/objects/v1/schedules |
| `show service` | folder | `show_service` | GET /config/objects/v1/services |
| `show service-group` | folder | `service_groups` | GET /config/objects/v1/service-groups |
| `show syslog-server-profiles` | folder | — | — |
| `show tag` | folder | `show_tag` | GET /config/objects/v1/tags |
| `update address` | folder | `update_objects` | PUT /config/objects/v1/addresses/{id} |
| `update address-group` | folder | `update_objects` | PUT /config/objects/v1/address-groups/{id} |
| `update external-dynamic-list` | folder | `update_objects` | PUT /config/objects/v1/external-dynamic-lists/{id} |
| `update service` | folder | `update_objects` | PUT /config/objects/v1/services/{id} |
| `update service-group` | folder | `update_objects` | PUT /config/objects/v1/service-groups/{id} |
| `update tag` | folder | `update_objects` | PUT /config/objects/v1/tags/{id} |

## Operations

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `commit` | folder | `commit` | POST /config/setup/v1/config-versions/candidate:push |
| `ping host` | device | `ping` | (live device state — SSH via --remote) |
| `request system reboot` | device | `request_system_reboot` | (live device state — SSH via --remote) |
| `request system shutdown` | device | `request_system_reboot` | (live device state — SSH via --remote) |
| `request system software check` | device | `request_system_software` | (live device state — SSH via --remote) |
| `show jobs all` | global | `show_jobs` | GET /config/setup/v1/jobs |
| `show jobs id` | global | `show_jobs` | GET /config/setup/v1/jobs/{id} |
| `show log system` | device | `show_log_system` | (live device state — SSH via --remote) |
| `show log traffic` | device | `show_log_traffic` | (live device state — SSH via --remote) |
| `show system disk-space` | device | `show_system_disk_space` | (live device state — SSH via --remote) |
| `show system info` | device | `show_system_info` | GET /config/setup/v1/devices/{id} |
| `show system resources` | device | `show_system_resources` | (live device state — SSH via --remote) |

## Security

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `delete security-rule` | folder | `delete_security` | DELETE /config/security/v1/security-rules/{id} |
| `delete url-category` | folder | `delete_security` | DELETE /config/security/v1/url-categories/{id} |
| `set url-category` | folder | `create_url_category` | POST /config/security/v1/url-categories |
| `show anti-spyware-profile` | folder | `security_profiles` | GET /config/security/v1/anti-spyware-profiles |
| `show anti-spyware-signatures` | folder | — | — |
| `show app-override-rules` | folder | `app_override` | GET /config/security/v1/app-override-rules |
| `show data-filtering-profiles` | folder | — | — |
| `show data-objects` | folder | — | — |
| `show decryption-exclusions` | folder | — | — |
| `show decryption-profile` | folder | `decryption_policy` | GET /config/security/v1/decryption-profiles |
| `show decryption-rules` | folder | `decryption_policy` | GET /config/security/v1/decryption-rules |
| `show dns-security-profiles` | folder | — | — |
| `show dos-protection-profile` | folder | `dos_protection` | GET /config/security/v1/dos-protection-profiles |
| `show dos-protection-rules` | folder | `dos_protection` | GET /config/security/v1/dos-protection-rules |
| `show file-blocking-profiles` | folder | — | — |
| `show http-header-profiles` | folder | — | — |
| `show profile-group` | folder | `profile_groups` | GET /config/security/v1/profile-groups |
| `show saas-tenant-restrictions` | folder | — | — |
| `show security policy` | folder | `show_security_policy` | GET /config/security/v1/security-rules |
| `show ssl-decryption-settings` | folder | — | — |
| `show url-access-profiles` | folder | — | — |
| `show url-admin-override` | folder | — | — |
| `show url-categories` | folder | `show_url_categories` | GET /config/security/v1/url-categories |
| `show url-filtering-categories` | folder | — | — |
| `show vulnerability-profile` | folder | `security_profiles` | GET /config/security/v1/vulnerability-protection-profiles |
| `show vulnerability-protection-signatures` | folder | — | — |
| `show wildfire-profile` | folder | `security_profiles` | GET /config/security/v1/wildfire-anti-virus-profiles |

## Setup

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `show device` | global | `show_devices` | GET /config/setup/v1/devices/{id} |
| `show device snippets` | global | `show_devices` | GET /config/setup/v1/devices/{id} |
| `show devices` | global | `show_devices` | GET /config/setup/v1/devices |
| `show snippet` | global | `show_snippets` | GET /config/setup/v1/snippets |
| `show snippets` | folder | `show_snippets` | GET /config/setup/v1/snippets |
| `show snippets global` | global | `show_snippets` | GET /config/setup/v1/snippets |
