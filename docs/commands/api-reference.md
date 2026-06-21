# ARC Command → SCM API Reference

Generated from each command's doc front-matter (`api:` field) and the live
registry. Regenerate with `python dev/generate_command_docs.py` (runs on `docsupdate`).

## Adnsr

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `delete adnsr bad-domains` | global | `delete_adnsr_bad_domains` | DELETE https://api.strata.paloaltonetworks.com/adns-resolver/v1/misconfigured-domains/{misconfigured-domain-id} |
| `delete adnsr ca-certs` | global | `delete_adnsr_ca_certs` | DELETE https://api.strata.paloaltonetworks.com/adns-resolver/v1/ca-certs/{ca-cert-id} |
| `delete adnsr conn-sources` | global | `delete_adnsr_conn_sources` | DELETE https://api.strata.paloaltonetworks.com/adns-resolver/v1/connection-sources/{connection-source-id} |
| `delete adnsr conn-sources subnets` | global | `delete_adnsr_conn_sources_subnets` | DELETE https://api.strata.paloaltonetworks.com/adns-resolver/v1/connection-sources/{connection-source-id}/subnets/{subnet-id} |
| `delete adnsr custom-fqdns` | global | `delete_adnsr_custom_fqdns` | DELETE https://api.strata.paloaltonetworks.com/adns-resolver/v1/custom-fqdns/{custom-fqdn-id} |
| `delete adnsr edls` | global | `delete_adnsr_edls` | DELETE https://api.strata.paloaltonetworks.com/adns-resolver/v1/edls/{edl-id} |
| `delete adnsr internal-domains` | global | `delete_adnsr_internal_domains` | DELETE https://api.strata.paloaltonetworks.com/adns-resolver/v1/internal-domains/{internal-domain-id} |
| `delete adnsr profiles` | global | `delete_adnsr_profiles` | DELETE https://api.strata.paloaltonetworks.com/adns-resolver/v1/profiles/{profile-id} |
| `set adnsr bad-domains` | global | `create_adnsr_bad_domains` | POST https://api.strata.paloaltonetworks.com/adns-resolver/v1/misconfigured-domains |
| `set adnsr ca-certs upload` | global | `create_adnsr_ca_certs_upload` | POST https://api.strata.paloaltonetworks.com/adns-resolver/v1/ca-certs:upload |
| `set adnsr conn-sources` | global | `create_adnsr_conn_sources` | POST https://api.strata.paloaltonetworks.com/adns-resolver/v1/connection-sources |
| `set adnsr conn-sources subnets` | global | `create_adnsr_conn_sources_subnets` | POST https://api.strata.paloaltonetworks.com/adns-resolver/v1/connection-sources/{connection-source-id}/subnets |
| `set adnsr conn-sources subnets verify` | global | `create_adnsr_conn_sources_subnets_verify` | POST https://api.strata.paloaltonetworks.com/adns-resolver/v1/connection-sources/{connection-source-id}/subnets/{subnet-id}:verify-update |
| `set adnsr custom-fqdns` | global | `create_adnsr_custom_fqdns` | POST https://api.strata.paloaltonetworks.com/adns-resolver/v1/custom-fqdns |
| `set adnsr edls` | global | `create_adnsr_edls` | POST https://api.strata.paloaltonetworks.com/adns-resolver/v1/edls |
| `set adnsr internal-domains` | global | `create_adnsr_internal_domains` | POST https://api.strata.paloaltonetworks.com/adns-resolver/v1/internal-domains |
| `set adnsr profiles` | global | `create_adnsr_profiles` | POST https://api.strata.paloaltonetworks.com/adns-resolver/v1/profiles |
| `show adnsr bad-domains` | global | `show_adnsr_bad_domains` | GET https://api.strata.paloaltonetworks.com/adns-resolver/v1/misconfigured-domains |
| `show adnsr bad-domains id` | global | `show_adnsr_bad_domains_id` | GET https://api.strata.paloaltonetworks.com/adns-resolver/v1/misconfigured-domains/{misconfigured-domain-id} |
| `show adnsr ca-certs` | global | `show_adnsr_ca_certs` | GET https://api.strata.paloaltonetworks.com/adns-resolver/v1/ca-certs |
| `show adnsr ca-certs download id` | global | `show_adnsr_ca_certs_download_id` | GET https://api.strata.paloaltonetworks.com/adns-resolver/v1/ca-certs/{ca-cert-id}/download |
| `show adnsr ca-certs id` | global | `show_adnsr_ca_certs_id` | GET https://api.strata.paloaltonetworks.com/adns-resolver/v1/ca-certs/{ca-cert-id} |
| `show adnsr conn-sources` | global | `show_adnsr_conn_sources` | GET https://api.strata.paloaltonetworks.com/adns-resolver/v1/connection-sources |
| `show adnsr conn-sources id` | global | `show_adnsr_conn_sources_id` | GET https://api.strata.paloaltonetworks.com/adns-resolver/v1/connection-sources/{connection-source-id} |
| `show adnsr conn-sources subnets` | global | `show_adnsr_conn_sources_subnets` | GET https://api.strata.paloaltonetworks.com/adns-resolver/v1/connection-sources/subnets |
| `show adnsr conn-sources subnets id` | global | `show_adnsr_conn_sources_subnets_id` | GET https://api.strata.paloaltonetworks.com/adns-resolver/v1/connection-sources/{connection-source-id}/subnets/{subnet-id} |
| `show adnsr custom-fqdns` | global | `show_adnsr_custom_fqdns` | GET https://api.strata.paloaltonetworks.com/adns-resolver/v1/custom-fqdns |
| `show adnsr custom-fqdns id` | global | `show_adnsr_custom_fqdns_id` | GET https://api.strata.paloaltonetworks.com/adns-resolver/v1/custom-fqdns/{custom-fqdn-id} |
| `show adnsr edls` | global | `show_adnsr_edls` | GET https://api.strata.paloaltonetworks.com/adns-resolver/v1/edls |
| `show adnsr edls id` | global | `show_adnsr_edls_id` | GET https://api.strata.paloaltonetworks.com/adns-resolver/v1/edls/{edl-id} |
| `show adnsr internal-domains` | global | `show_adnsr_internal_domains` | GET https://api.strata.paloaltonetworks.com/adns-resolver/v1/internal-domains |
| `show adnsr internal-domains id` | global | `show_adnsr_internal_domains_id` | GET https://api.strata.paloaltonetworks.com/adns-resolver/v1/internal-domains/{internal-domain-id} |
| `show adnsr profiles` | global | `show_adnsr_profiles` | GET https://api.strata.paloaltonetworks.com/adns-resolver/v1/profiles |
| `show adnsr profiles categories` | global | `show_adnsr_profiles_categories` | GET https://api.strata.paloaltonetworks.com/adns-resolver/v1/profiles/categories |
| `show adnsr profiles id` | global | `show_adnsr_profiles_id` | GET https://api.strata.paloaltonetworks.com/adns-resolver/v1/profiles/{profile-id} |
| `show adnsr resolver-info` | global | `show_adnsr_resolver_info` | GET https://api.strata.paloaltonetworks.com/adns-resolver/v1/resolver-info |
| `update adnsr bad-domains` | global | `update_adnsr_bad_domains` | PUT https://api.strata.paloaltonetworks.com/adns-resolver/v1/misconfigured-domains/{misconfigured-domain-id} |
| `update adnsr conn-sources` | global | `update_adnsr_conn_sources` | PUT https://api.strata.paloaltonetworks.com/adns-resolver/v1/connection-sources/{connection-source-id} |
| `update adnsr custom-fqdns` | global | `update_adnsr_custom_fqdns` | PUT https://api.strata.paloaltonetworks.com/adns-resolver/v1/custom-fqdns/{custom-fqdn-id} |
| `update adnsr edls` | global | `update_adnsr_edls` | PUT https://api.strata.paloaltonetworks.com/adns-resolver/v1/edls/{edl-id} |
| `update adnsr internal-domains` | global | `update_adnsr_internal_domains` | PUT https://api.strata.paloaltonetworks.com/adns-resolver/v1/internal-domains/{internal-domain-id} |
| `update adnsr profiles` | global | `update_adnsr_profiles` | PUT https://api.strata.paloaltonetworks.com/adns-resolver/v1/profiles/{profile-id} |

## Auth

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `set oauth2 access-token` | global | `create_oauth2_access_token` | POST https://auth.apps.paloaltonetworks.com/auth/v1/oauth2/access_token |
| `set oauth2 userinfo` | global | `create_oauth2_userinfo` | POST https://auth.apps.paloaltonetworks.com/auth/v1/oauth2/userinfo |
| `show oauth2 userinfo` | global | `show_oauth2_userinfo` | GET https://auth.apps.paloaltonetworks.com/auth/v1/oauth2/userinfo |

## Cdug

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `delete cdug cloud-dug-definition group` | global | `delete_cdug_cloud_dug_definition_group` | DELETE /directory-sync/v1/cloud-dug-definition/group |
| `set cdug cloud-dug-definition` | global | `create_cdug_cloud_dug_definition` | POST /directory-sync/v1/cloud-dug-definition |
| `show cdug cloud-dug-definition category` | global | `show_cdug_cloud_dug_definition_category` | GET /directory-sync/v1/cloud-dug-definition/category |
| `show cdug cloud-dug-definition group` | global | `show_cdug_cloud_dug_definition_group` | GET /directory-sync/v1/cloud-dug-definition/group |
| `show cdug user-attr-values` | global | `show_cdug_user_attr_values` | GET /directory-sync/v1/user-attr-values |
| `update cdug cloud-dug-definition group` | global | `update_cdug_cloud_dug_definition_group` | PUT /directory-sync/v1/cloud-dug-definition/group |

## Ciedss

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `set ciedss cache-groups` | global | `create_ciedss_cache_groups` | POST https://api.sase.paloaltonetworks.com/cie/directory-sync/v1/cache-groups |
| `set ciedss cache-users` | global | `create_ciedss_cache_users` | POST https://api.sase.paloaltonetworks.com/cie/directory-sync/v1/cache-users |
| `set ciedss connection update-secret` | global | `create_ciedss_connection_update_secret` | POST https://api.sase.paloaltonetworks.com/cie/directory-sync/v1/connection/update-secret |
| `show ciedss domains` | global | `show_ciedss_domains` | GET https://api.sase.paloaltonetworks.com/cie/directory-sync/v1/domains |

## Cloudngfw

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `delete cngfw address-groups` | global | `delete_cngfw_address_groups` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/address-groups/{id} |
| `delete cngfw addresses` | global | `delete_cngfw_addresses` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/addresses/{id} |
| `delete cngfw adv-device-objs` | global | `delete_cngfw_adv_device_objs` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/advanced-device-objects |
| `delete cngfw anti-spyware-profiles` | global | `delete_cngfw_anti_spyware_profiles` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/anti-spyware-profiles/{id} |
| `delete cngfw anti-spyware-signatures` | global | `delete_cngfw_anti_spyware_signatures` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/anti-spyware-signatures/{id} |
| `delete cngfw app-override-rules` | global | `delete_cngfw_app_override_rules` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/app-override-rules/{id} |
| `delete cngfw application-filters` | global | `delete_cngfw_application_filters` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/application-filters/{id} |
| `delete cngfw application-groups` | global | `delete_cngfw_application_groups` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/application-groups/{id} |
| `delete cngfw applications` | global | `delete_cngfw_applications` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/applications/{id} |
| `delete cngfw authentication-portals` | global | `delete_cngfw_authentication_portals` | DELETE https://api.strata.paloaltonetworks.com/config/identity/v1/authentication-portals/{id} |
| `delete cngfw authentication-profiles` | global | `delete_cngfw_authentication_profiles` | DELETE https://api.strata.paloaltonetworks.com/config/identity/v1/authentication-profiles/{id} |
| `delete cngfw authentication-rules` | global | `delete_cngfw_authentication_rules` | DELETE https://api.strata.paloaltonetworks.com/config/identity/v1/authentication-rules/{id} |
| `delete cngfw authentication-sequences` | global | `delete_cngfw_authentication_sequences` | DELETE https://api.strata.paloaltonetworks.com/config/identity/v1/authentication-sequences/{id} |
| `delete cngfw auto-tag-actions` | global | `delete_cngfw_auto_tag_actions` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/auto-tag-actions |
| `delete cngfw certificate-profiles` | global | `delete_cngfw_certificate_profiles` | DELETE https://api.strata.paloaltonetworks.com/config/identity/v1/certificate-profiles/{id} |
| `delete cngfw certs` | global | `delete_cngfw_certs` | DELETE https://api.strata.paloaltonetworks.com/config/identity/v1/certificates/{id} |
| `delete cngfw config-versions candidate` | global | `delete_cngfw_config_versions_candidate` | DELETE https://api.strata.paloaltonetworks.com/config/operations/v1/config-versions/candidate |
| `delete cngfw data-filtering-profiles` | global | `delete_cngfw_data_filtering_profiles` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/data-filtering-profiles/{id} |
| `delete cngfw data-objects` | global | `delete_cngfw_data_objects` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/data-objects/{id} |
| `delete cngfw decryption-exclusions` | global | `delete_cngfw_decryption_exclusions` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/decryption-exclusions/{id} |
| `delete cngfw decryption-profiles` | global | `delete_cngfw_decryption_profiles` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/decryption-profiles/{id} |
| `delete cngfw decryption-rules` | global | `delete_cngfw_decryption_rules` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/decryption-rules/{id} |
| `delete cngfw device-contexts` | global | `delete_cngfw_device_contexts` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/device-context-segments |
| `delete cngfw dns-security-profiles` | global | `delete_cngfw_dns_security_profiles` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/dns-security-profiles/{id} |
| `delete cngfw dos-protection-profiles` | global | `delete_cngfw_dos_protection_profiles` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/dos-protection-profiles/{id} |
| `delete cngfw dos-protection-rules` | global | `delete_cngfw_dos_protection_rules` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/dos-protection-rules/{id} |
| `delete cngfw dynamic-user-groups` | global | `delete_cngfw_dynamic_user_groups` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/dynamic-user-groups/{id} |
| `delete cngfw external-dynamic-lists` | global | `delete_cngfw_external_dynamic_lists` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/external-dynamic-lists/{id} |
| `delete cngfw file-blocking-profiles` | global | `delete_cngfw_file_blocking_profiles` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/file-blocking-profiles/{id} |
| `delete cngfw folders` | global | `delete_cngfw_folders` | DELETE https://api.strata.paloaltonetworks.com/config/setup/v1/folders/{id} |
| `delete cngfw hip-objects` | global | `delete_cngfw_hip_objects` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/hip-objects/{id} |
| `delete cngfw hip-profiles` | global | `delete_cngfw_hip_profiles` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/hip-profiles/{id} |
| `delete cngfw http-header-profiles` | global | `delete_cngfw_http_header_profiles` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/http-header-profiles/{id} |
| `delete cngfw http-server-profiles` | global | `delete_cngfw_http_server_profiles` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/http-server-profiles/{id} |
| `delete cngfw kerberos-server-profiles` | global | `delete_cngfw_kerberos_server_profiles` | DELETE https://api.strata.paloaltonetworks.com/config/identity/v1/kerberos-server-profiles/{id} |
| `delete cngfw labels` | global | `delete_cngfw_labels` | DELETE https://api.strata.paloaltonetworks.com/config/setup/v1/labels/{id} |
| `delete cngfw ldap-server-profiles` | global | `delete_cngfw_ldap_server_profiles` | DELETE https://api.strata.paloaltonetworks.com/config/identity/v1/ldap-server-profiles/{id} |
| `delete cngfw local-user-groups` | global | `delete_cngfw_local_user_groups` | DELETE https://api.strata.paloaltonetworks.com/config/identity/v1/local-user-groups/{id} |
| `delete cngfw local-users` | global | `delete_cngfw_local_users` | DELETE https://api.strata.paloaltonetworks.com/config/identity/v1/local-users/{id} |
| `delete cngfw log-forwarding-profiles` | global | `delete_cngfw_log_forwarding_profiles` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/log-forwarding-profiles/{id} |
| `delete cngfw mfa-servers` | global | `delete_cngfw_mfa_servers` | DELETE https://api.strata.paloaltonetworks.com/config/identity/v1/mfa-servers/{id} |
| `delete cngfw objects adv-device-objs` | global | `delete_cngfw_adv_device_objs` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/advanced-device-objects/{id} |
| `delete cngfw objects device-contexts` | global | `delete_cngfw_device_contexts` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/device-context-segments/{id} |
| `delete cngfw ocsp-responders` | global | `delete_cngfw_ocsp_responders` | DELETE https://api.strata.paloaltonetworks.com/config/identity/v1/ocsp-responders/{id} |
| `delete cngfw onboarding-rules` | global | `delete_cngfw_onboarding_rules` | DELETE https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1/onboarding-rules/{id} |
| `delete cngfw profile-groups` | global | `delete_cngfw_profile_groups` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/profile-groups/{id} |
| `delete cngfw properties` | global | `delete_cngfw_properties` | DELETE https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1/properties/{id} |
| `delete cngfw quarantined-devices` | global | `delete_cngfw_quarantined_devices` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/quarantined-devices |
| `delete cngfw radius-server-profiles` | global | `delete_cngfw_radius_server_profiles` | DELETE https://api.strata.paloaltonetworks.com/config/identity/v1/radius-server-profiles/{id} |
| `delete cngfw regions` | global | `delete_cngfw_regions` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/regions/{id} |
| `delete cngfw saml-server-profiles` | global | `delete_cngfw_saml_server_profiles` | DELETE https://api.strata.paloaltonetworks.com/config/identity/v1/saml-server-profiles/{id} |
| `delete cngfw scep-profiles` | global | `delete_cngfw_scep_profiles` | DELETE https://api.strata.paloaltonetworks.com/config/identity/v1/scep-profiles/{id} |
| `delete cngfw schedules` | global | `delete_cngfw_schedules` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/schedules/{id} |
| `delete cngfw security-rules` | global | `delete_cngfw_security_rules` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/security-rules/{id} |
| `delete cngfw service-groups` | global | `delete_cngfw_service_groups` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/service-groups/{id} |
| `delete cngfw services` | global | `delete_cngfw_services` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/services/{id} |
| `delete cngfw site-groups` | global | `delete_cngfw_site_groups` | DELETE https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1/site-groups/{id} |
| `delete cngfw sites` | global | `delete_cngfw_sites` | DELETE https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1/sites/{id} |
| `delete cngfw snippet-categories` | global | `delete_cngfw_snippet_categories` | DELETE https://api.strata.paloaltonetworks.com/config/setup/v1/snippet-categories/{id} |
| `delete cngfw snippets` | global | `delete_cngfw_snippets` | DELETE https://api.strata.paloaltonetworks.com/config/setup/v1/snippets/{id} |
| `delete cngfw ssl-decryption-settings` | global | `delete_cngfw_ssl_decryption_settings` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/ssl-decryption-settings |
| `delete cngfw subscribed-tenants` | global | `delete_cngfw_subscribed_tenants` | DELETE https://api.strata.paloaltonetworks.com/config/setup/v1/subscribed-tenants |
| `delete cngfw syslog-server-profiles` | global | `delete_cngfw_syslog_server_profiles` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/syslog-server-profiles/{id} |
| `delete cngfw tacacs-server-profiles` | global | `delete_cngfw_tacacs_server_profiles` | DELETE https://api.strata.paloaltonetworks.com/config/identity/v1/tacacs-server-profiles/{id} |
| `delete cngfw tags` | global | `delete_cngfw_tags` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/tags/{id} |
| `delete cngfw tls-service-profiles` | global | `delete_cngfw_tls_service_profiles` | DELETE https://api.strata.paloaltonetworks.com/config/identity/v1/tls-service-profiles/{id} |
| `delete cngfw trusts` | global | `delete_cngfw_trusts` | DELETE https://api.strata.paloaltonetworks.com/config/setup/v1/trusts |
| `delete cngfw url-access-profiles` | global | `delete_cngfw_url_access_profiles` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/url-access-profiles/{id} |
| `delete cngfw url-admin-override` | global | `delete_cngfw_url_admin_override` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/url-admin-override/{id} |
| `delete cngfw url-categories` | global | `delete_cngfw_url_categories` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/url-categories/{id} |
| `delete cngfw variables` | global | `delete_cngfw_variables` | DELETE https://api.strata.paloaltonetworks.com/config/setup/v1/variables/{id} |
| `delete cngfw vuln-profiles` | global | `delete_cngfw_vuln_profiles` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/vulnerability-protection-profiles/{id} |
| `delete cngfw vuln-signatures` | global | `delete_cngfw_vuln_signatures` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/vulnerability-protection-signatures/{id} |
| `delete cngfw wildfire-profiles` | global | `delete_cngfw_wildfire_profiles` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/wildfire-anti-virus-profiles/{id} |
| `set cngfw address-groups` | global | `create_cngfw_address_groups` | POST https://api.strata.paloaltonetworks.com/config/objects/v1/address-groups |
| `set cngfw addresses` | global | `create_cngfw_addresses` | POST https://api.strata.paloaltonetworks.com/config/objects/v1/addresses |
| `set cngfw adv-device-objs` | global | `create_cngfw_adv_device_objs` | POST https://api.strata.paloaltonetworks.com/config/objects/v1/advanced-device-objects |
| `set cngfw anti-spyware-profiles` | global | `create_cngfw_anti_spyware_profiles` | POST https://api.strata.paloaltonetworks.com/config/security/v1/anti-spyware-profiles |
| `set cngfw anti-spyware-signatures` | global | `create_cngfw_anti_spyware_signatures` | POST https://api.strata.paloaltonetworks.com/config/security/v1/anti-spyware-signatures |
| `set cngfw app-override-rules` | global | `create_cngfw_app_override_rules` | POST https://api.strata.paloaltonetworks.com/config/security/v1/app-override-rules |
| `set cngfw app-override-rules move` | global | `create_cngfw_app_override_rules_move` | POST https://api.strata.paloaltonetworks.com/config/security/v1/app-override-rules/{id}:move |
| `set cngfw application-filters` | global | `create_cngfw_application_filters` | POST https://api.strata.paloaltonetworks.com/config/objects/v1/application-filters |
| `set cngfw application-groups` | global | `create_cngfw_application_groups` | POST https://api.strata.paloaltonetworks.com/config/objects/v1/application-groups |
| `set cngfw applications` | global | `create_cngfw_applications` | POST https://api.strata.paloaltonetworks.com/config/objects/v1/applications |
| `set cngfw authentication-portals` | global | `create_cngfw_authentication_portals` | POST https://api.strata.paloaltonetworks.com/config/identity/v1/authentication-portals |
| `set cngfw authentication-profiles` | global | `create_cngfw_authentication_profiles` | POST https://api.strata.paloaltonetworks.com/config/identity/v1/authentication-profiles |
| `set cngfw authentication-rules` | global | `create_cngfw_authentication_rules` | POST https://api.strata.paloaltonetworks.com/config/identity/v1/authentication-rules |
| `set cngfw authentication-rules move` | global | `create_cngfw_authentication_rules_move` | POST https://api.strata.paloaltonetworks.com/config/identity/v1/authentication-rules/{id}:move |
| `set cngfw authentication-sequences` | global | `create_cngfw_authentication_sequences` | POST https://api.strata.paloaltonetworks.com/config/identity/v1/authentication-sequences |
| `set cngfw auto-tag-actions` | global | `create_cngfw_auto_tag_actions` | POST https://api.strata.paloaltonetworks.com/config/objects/v1/auto-tag-actions |
| `set cngfw certificate-profiles` | global | `create_cngfw_certificate_profiles` | POST https://api.strata.paloaltonetworks.com/config/identity/v1/certificate-profiles |
| `set cngfw certs` | global | `create_cngfw_certs` | POST https://api.strata.paloaltonetworks.com/config/identity/v1/certificates |
| `set cngfw certs export` | global | `create_cngfw_certs_export` | POST https://api.strata.paloaltonetworks.com/config/identity/v1/certificates/{id}:export |
| `set cngfw certs import` | global | `create_cngfw_certs_import` | POST https://api.strata.paloaltonetworks.com/config/identity/v1/certificates:import |
| `set cngfw config-versions candidate push` | global | `create_cngfw_config_versions_candidate_push` | POST https://api.strata.paloaltonetworks.com/config/operations/v1/config-versions/candidate:push |
| `set cngfw config-versions load` | global | `create_cngfw_config_versions_load` | POST https://api.strata.paloaltonetworks.com/config/operations/v1/config-versions:load |
| `set cngfw data-filtering-profiles` | global | `create_cngfw_data_filtering_profiles` | POST https://api.strata.paloaltonetworks.com/config/security/v1/data-filtering-profiles |
| `set cngfw data-objects` | global | `create_cngfw_data_objects` | POST https://api.strata.paloaltonetworks.com/config/security/v1/data-objects |
| `set cngfw decryption-exclusions` | global | `create_cngfw_decryption_exclusions` | POST https://api.strata.paloaltonetworks.com/config/security/v1/decryption-exclusions |
| `set cngfw decryption-profiles` | global | `create_cngfw_decryption_profiles` | POST https://api.strata.paloaltonetworks.com/config/security/v1/decryption-profiles |
| `set cngfw decryption-rules` | global | `create_cngfw_decryption_rules` | POST https://api.strata.paloaltonetworks.com/config/security/v1/decryption-rules |
| `set cngfw decryption-rules move` | global | `create_cngfw_decryption_rules_move` | POST https://api.strata.paloaltonetworks.com/config/security/v1/decryption-rules/{id}:move |
| `set cngfw device-contexts` | global | `create_cngfw_device_contexts` | POST https://api.strata.paloaltonetworks.com/config/objects/v1/device-context-segments |
| `set cngfw dns-security-profiles` | global | `create_cngfw_dns_security_profiles` | POST https://api.strata.paloaltonetworks.com/config/security/v1/dns-security-profiles |
| `set cngfw dos-protection-profiles` | global | `create_cngfw_dos_protection_profiles` | POST https://api.strata.paloaltonetworks.com/config/security/v1/dos-protection-profiles |
| `set cngfw dos-protection-rules` | global | `create_cngfw_dos_protection_rules` | POST https://api.strata.paloaltonetworks.com/config/security/v1/dos-protection-rules |
| `set cngfw dynamic-user-groups` | global | `create_cngfw_dynamic_user_groups` | POST https://api.strata.paloaltonetworks.com/config/objects/v1/dynamic-user-groups |
| `set cngfw external-dynamic-lists` | global | `create_cngfw_external_dynamic_lists` | POST https://api.strata.paloaltonetworks.com/config/objects/v1/external-dynamic-lists |
| `set cngfw file-blocking-profiles` | global | `create_cngfw_file_blocking_profiles` | POST https://api.strata.paloaltonetworks.com/config/security/v1/file-blocking-profiles |
| `set cngfw folders` | global | `create_cngfw_folders` | POST https://api.strata.paloaltonetworks.com/config/setup/v1/folders |
| `set cngfw hip-objects` | global | `create_cngfw_hip_objects` | POST https://api.strata.paloaltonetworks.com/config/objects/v1/hip-objects |
| `set cngfw hip-profiles` | global | `create_cngfw_hip_profiles` | POST https://api.strata.paloaltonetworks.com/config/objects/v1/hip-profiles |
| `set cngfw http-header-profiles` | global | `create_cngfw_http_header_profiles` | POST https://api.strata.paloaltonetworks.com/config/security/v1/http-header-profiles |
| `set cngfw http-server-profiles` | global | `create_cngfw_http_server_profiles` | POST https://api.strata.paloaltonetworks.com/config/objects/v1/http-server-profiles |
| `set cngfw kerberos-server-profiles` | global | `create_cngfw_kerberos_server_profiles` | POST https://api.strata.paloaltonetworks.com/config/identity/v1/kerberos-server-profiles |
| `set cngfw labels` | global | `create_cngfw_labels` | POST https://api.strata.paloaltonetworks.com/config/setup/v1/labels |
| `set cngfw ldap-server-profiles` | global | `create_cngfw_ldap_server_profiles` | POST https://api.strata.paloaltonetworks.com/config/identity/v1/ldap-server-profiles |
| `set cngfw local-user-groups` | global | `create_cngfw_local_user_groups` | POST https://api.strata.paloaltonetworks.com/config/identity/v1/local-user-groups |
| `set cngfw local-users` | global | `create_cngfw_local_users` | POST https://api.strata.paloaltonetworks.com/config/identity/v1/local-users |
| `set cngfw log-forwarding-profiles` | global | `create_cngfw_log_forwarding_profiles` | POST https://api.strata.paloaltonetworks.com/config/objects/v1/log-forwarding-profiles |
| `set cngfw mfa-servers` | global | `create_cngfw_mfa_servers` | POST https://api.strata.paloaltonetworks.com/config/identity/v1/mfa-servers |
| `set cngfw ocsp-responders` | global | `create_cngfw_ocsp_responders` | POST https://api.strata.paloaltonetworks.com/config/identity/v1/ocsp-responders |
| `set cngfw onboarding-rules` | global | `create_cngfw_onboarding_rules` | POST https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1/onboarding-rules |
| `set cngfw onboarding-rules move` | global | `create_cngfw_onboarding_rules_move` | POST https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1/onboarding-rules/{id}:move |
| `set cngfw profile-groups` | global | `create_cngfw_profile_groups` | POST https://api.strata.paloaltonetworks.com/config/security/v1/profile-groups |
| `set cngfw properties` | global | `create_cngfw_properties` | POST https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1/properties |
| `set cngfw quarantined-devices` | global | `create_cngfw_quarantined_devices` | POST https://api.strata.paloaltonetworks.com/config/objects/v1/quarantined-devices |
| `set cngfw radius-server-profiles` | global | `create_cngfw_radius_server_profiles` | POST https://api.strata.paloaltonetworks.com/config/identity/v1/radius-server-profiles |
| `set cngfw regions` | global | `create_cngfw_regions` | POST https://api.strata.paloaltonetworks.com/config/objects/v1/regions |
| `set cngfw saml-server-profiles` | global | `create_cngfw_saml_server_profiles` | POST https://api.strata.paloaltonetworks.com/config/identity/v1/saml-server-profiles |
| `set cngfw scep-profiles` | global | `create_cngfw_scep_profiles` | POST https://api.strata.paloaltonetworks.com/config/identity/v1/scep-profiles |
| `set cngfw schedules` | global | `create_cngfw_schedules` | POST https://api.strata.paloaltonetworks.com/config/objects/v1/schedules |
| `set cngfw security-rules` | global | `create_cngfw_security_rules` | POST https://api.strata.paloaltonetworks.com/config/security/v1/security-rules |
| `set cngfw security-rules move` | global | `create_cngfw_security_rules_move` | POST https://api.strata.paloaltonetworks.com/config/security/v1/security-rules/{id}:move |
| `set cngfw service-groups` | global | `create_cngfw_service_groups` | POST https://api.strata.paloaltonetworks.com/config/objects/v1/service-groups |
| `set cngfw services` | global | `create_cngfw_services` | POST https://api.strata.paloaltonetworks.com/config/objects/v1/services |
| `set cngfw shared-snippets load` | global | `create_cngfw_shared_snippets_load` | POST https://api.strata.paloaltonetworks.com/config/setup/v1/shared-snippets:load |
| `set cngfw site-groups` | global | `create_cngfw_site_groups` | POST https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1/site-groups |
| `set cngfw sites` | global | `create_cngfw_sites` | POST https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1/sites |
| `set cngfw snippet-audit-logs` | global | `create_cngfw_snippet_audit_logs` | POST https://api.strata.paloaltonetworks.com/config/setup/v1/snippet-audit-logs |
| `set cngfw snippet-snapshots` | global | `create_cngfw_snippet_snapshots` | POST https://api.strata.paloaltonetworks.com/config/setup/v1/snippet-snapshots |
| `set cngfw snippet-snapshots compare` | global | `create_cngfw_snippet_snapshots_compare` | POST https://api.strata.paloaltonetworks.com/config/setup/v1/snippet-snapshots:compare |
| `set cngfw snippet-snapshots convert` | global | `create_cngfw_snippet_snapshots_convert` | POST https://api.strata.paloaltonetworks.com/config/setup/v1/snippet-snapshots:convert |
| `set cngfw snippet-snapshots diff` | global | `create_cngfw_snippet_snapshots_diff` | POST https://api.strata.paloaltonetworks.com/config/setup/v1/snippet-snapshots:diff |
| `set cngfw snippet-snapshots load` | global | `create_cngfw_snippet_snapshots_load` | POST https://api.strata.paloaltonetworks.com/config/setup/v1/snippet-snapshots:load |
| `set cngfw snippet-snapshots publish` | global | `create_cngfw_snippet_snapshots_publish` | POST https://api.strata.paloaltonetworks.com/config/setup/v1/snippet-snapshots:publish |
| `set cngfw snippet-snapshots updates` | global | `create_cngfw_snippet_snapshots_updates` | POST https://api.strata.paloaltonetworks.com/config/setup/v1/snippet-snapshots:updates |
| `set cngfw snippets` | global | `create_cngfw_snippets` | POST https://api.strata.paloaltonetworks.com/config/setup/v1/snippets |
| `set cngfw ssl-decryption-settings` | global | `create_cngfw_ssl_decryption_settings` | POST https://api.strata.paloaltonetworks.com/config/security/v1/ssl-decryption-settings |
| `set cngfw subscribed-tenants` | global | `create_cngfw_subscribed_tenants` | POST https://api.strata.paloaltonetworks.com/config/setup/v1/subscribed-tenants |
| `set cngfw syslog-server-profiles` | global | `create_cngfw_syslog_server_profiles` | POST https://api.strata.paloaltonetworks.com/config/objects/v1/syslog-server-profiles |
| `set cngfw tacacs-server-profiles` | global | `create_cngfw_tacacs_server_profiles` | POST https://api.strata.paloaltonetworks.com/config/identity/v1/tacacs-server-profiles |
| `set cngfw tags` | global | `create_cngfw_tags` | POST https://api.strata.paloaltonetworks.com/config/objects/v1/tags |
| `set cngfw tls-service-profiles` | global | `create_cngfw_tls_service_profiles` | POST https://api.strata.paloaltonetworks.com/config/identity/v1/tls-service-profiles |
| `set cngfw trust-validations` | global | `create_cngfw_trust_validations` | POST https://api.strata.paloaltonetworks.com/config/setup/v1/trust-validations |
| `set cngfw trusts` | global | `create_cngfw_trusts` | POST https://api.strata.paloaltonetworks.com/config/setup/v1/trusts |
| `set cngfw url-access-profiles` | global | `create_cngfw_url_access_profiles` | POST https://api.strata.paloaltonetworks.com/config/security/v1/url-access-profiles |
| `set cngfw url-admin-override` | global | `create_cngfw_url_admin_override` | POST https://api.strata.paloaltonetworks.com/config/security/v1/url-admin-override |
| `set cngfw url-categories` | global | `create_cngfw_url_categories` | POST https://api.strata.paloaltonetworks.com/config/security/v1/url-categories |
| `set cngfw variables` | global | `create_cngfw_variables` | POST https://api.strata.paloaltonetworks.com/config/setup/v1/variables |
| `set cngfw vuln-profiles` | global | `create_cngfw_vuln_profiles` | POST https://api.strata.paloaltonetworks.com/config/security/v1/vulnerability-protection-profiles |
| `set cngfw vuln-signatures` | global | `create_cngfw_vuln_signatures` | POST https://api.strata.paloaltonetworks.com/config/security/v1/vulnerability-protection-signatures |
| `set cngfw wildfire-profiles` | global | `create_cngfw_wildfire_profiles` | POST https://api.strata.paloaltonetworks.com/config/security/v1/wildfire-anti-virus-profiles |
| `show cngfw address-groups` | global | `show_cngfw_address_groups` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/address-groups |
| `show cngfw address-groups id` | global | `show_cngfw_address_groups_id` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/address-groups/{id} |
| `show cngfw addresses` | global | `show_cngfw_addresses` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/addresses |
| `show cngfw addresses id` | global | `show_cngfw_addresses_id` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/addresses/{id} |
| `show cngfw adv-device-objs` | global | `show_cngfw_adv_device_objs` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/advanced-device-objects |
| `show cngfw adv-device-objs id` | global | `show_cngfw_adv_device_objs_id` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/advanced-device-objects/{id} |
| `show cngfw anti-spyware-profiles` | global | `show_cngfw_anti_spyware_profiles` | GET https://api.strata.paloaltonetworks.com/config/security/v1/anti-spyware-profiles |
| `show cngfw anti-spyware-profiles id` | global | `show_cngfw_anti_spyware_profiles_id` | GET https://api.strata.paloaltonetworks.com/config/security/v1/anti-spyware-profiles/{id} |
| `show cngfw anti-spyware-signatures` | global | `show_cngfw_anti_spyware_signatures` | GET https://api.strata.paloaltonetworks.com/config/security/v1/anti-spyware-signatures |
| `show cngfw anti-spyware-signatures id` | global | `show_cngfw_anti_spyware_signatures_id` | GET https://api.strata.paloaltonetworks.com/config/security/v1/anti-spyware-signatures/{id} |
| `show cngfw app-override-rules` | global | `show_cngfw_app_override_rules` | GET https://api.strata.paloaltonetworks.com/config/security/v1/app-override-rules |
| `show cngfw app-override-rules id` | global | `show_cngfw_app_override_rules_id` | GET https://api.strata.paloaltonetworks.com/config/security/v1/app-override-rules/{id} |
| `show cngfw application-filters` | global | `show_cngfw_application_filters` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/application-filters |
| `show cngfw application-filters id` | global | `show_cngfw_application_filters_id` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/application-filters/{id} |
| `show cngfw application-groups` | global | `show_cngfw_application_groups` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/application-groups |
| `show cngfw application-groups id` | global | `show_cngfw_application_groups_id` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/application-groups/{id} |
| `show cngfw applications` | global | `show_cngfw_applications` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/applications |
| `show cngfw applications id` | global | `show_cngfw_applications_id` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/applications/{id} |
| `show cngfw authentication-portals` | global | `show_cngfw_authentication_portals` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/authentication-portals |
| `show cngfw authentication-portals id` | global | `show_cngfw_authentication_portals_id` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/authentication-portals/{id} |
| `show cngfw authentication-profiles` | global | `show_cngfw_authentication_profiles` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/authentication-profiles |
| `show cngfw authentication-profiles id` | global | `show_cngfw_authentication_profiles_id` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/authentication-profiles/{id} |
| `show cngfw authentication-rules` | global | `show_cngfw_authentication_rules` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/authentication-rules |
| `show cngfw authentication-rules id` | global | `show_cngfw_authentication_rules_id` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/authentication-rules/{id} |
| `show cngfw authentication-sequences` | global | `show_cngfw_authentication_sequences` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/authentication-sequences |
| `show cngfw authentication-sequences id` | global | `show_cngfw_authentication_sequences_id` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/authentication-sequences/{id} |
| `show cngfw auto-tag-actions` | global | `show_cngfw_auto_tag_actions` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/auto-tag-actions |
| `show cngfw certificate-profiles` | global | `show_cngfw_certificate_profiles` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/certificate-profiles |
| `show cngfw certificate-profiles id` | global | `show_cngfw_certificate_profiles_id` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/certificate-profiles/{id} |
| `show cngfw certs` | global | `show_cngfw_certs` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/certificates |
| `show cngfw certs id` | global | `show_cngfw_certs_id` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/certificates/{id} |
| `show cngfw config-versions` | global | `show_cngfw_config_versions` | GET https://api.strata.paloaltonetworks.com/config/operations/v1/config-versions |
| `show cngfw config-versions id` | global | `show_cngfw_config_versions_id` | GET https://api.strata.paloaltonetworks.com/config/operations/v1/config-versions/{version} |
| `show cngfw config-versions running` | global | `show_cngfw_config_versions_running` | GET https://api.strata.paloaltonetworks.com/config/operations/v1/config-versions/running |
| `show cngfw data-filtering-profiles` | global | `show_cngfw_data_filtering_profiles` | GET https://api.strata.paloaltonetworks.com/config/security/v1/data-filtering-profiles |
| `show cngfw data-filtering-profiles id` | global | `show_cngfw_data_filtering_profiles_id` | GET https://api.strata.paloaltonetworks.com/config/security/v1/data-filtering-profiles/{id} |
| `show cngfw data-objects` | global | `show_cngfw_data_objects` | GET https://api.strata.paloaltonetworks.com/config/security/v1/data-objects |
| `show cngfw data-objects id` | global | `show_cngfw_data_objects_id` | GET https://api.strata.paloaltonetworks.com/config/security/v1/data-objects/{id} |
| `show cngfw decryption-exclusions` | global | `show_cngfw_decryption_exclusions` | GET https://api.strata.paloaltonetworks.com/config/security/v1/decryption-exclusions |
| `show cngfw decryption-exclusions id` | global | `show_cngfw_decryption_exclusions_id` | GET https://api.strata.paloaltonetworks.com/config/security/v1/decryption-exclusions/{id} |
| `show cngfw decryption-profiles` | global | `show_cngfw_decryption_profiles` | GET https://api.strata.paloaltonetworks.com/config/security/v1/decryption-profiles |
| `show cngfw decryption-profiles id` | global | `show_cngfw_decryption_profiles_id` | GET https://api.strata.paloaltonetworks.com/config/security/v1/decryption-profiles/{id} |
| `show cngfw decryption-rules` | global | `show_cngfw_decryption_rules` | GET https://api.strata.paloaltonetworks.com/config/security/v1/decryption-rules |
| `show cngfw decryption-rules id` | global | `show_cngfw_decryption_rules_id` | GET https://api.strata.paloaltonetworks.com/config/security/v1/decryption-rules/{id} |
| `show cngfw device-contexts` | global | `show_cngfw_device_contexts` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/device-context-segments |
| `show cngfw device-contexts id` | global | `show_cngfw_device_contexts_id` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/device-context-segments/{id} |
| `show cngfw devices` | global | `show_cngfw_devices` | GET https://api.strata.paloaltonetworks.com/config/setup/v1/devices |
| `show cngfw devices id` | global | `show_cngfw_devices_id` | GET https://api.strata.paloaltonetworks.com/config/setup/v1/devices/{id} |
| `show cngfw dns-security-profiles` | global | `show_cngfw_dns_security_profiles` | GET https://api.strata.paloaltonetworks.com/config/security/v1/dns-security-profiles |
| `show cngfw dns-security-profiles id` | global | `show_cngfw_dns_security_profiles_id` | GET https://api.strata.paloaltonetworks.com/config/security/v1/dns-security-profiles/{id} |
| `show cngfw dos-protection-profiles` | global | `show_cngfw_dos_protection_profiles` | GET https://api.strata.paloaltonetworks.com/config/security/v1/dos-protection-profiles |
| `show cngfw dos-protection-profiles id` | global | `show_cngfw_dos_protection_profiles_id` | GET https://api.strata.paloaltonetworks.com/config/security/v1/dos-protection-profiles/{id} |
| `show cngfw dos-protection-rules` | global | `show_cngfw_dos_protection_rules` | GET https://api.strata.paloaltonetworks.com/config/security/v1/dos-protection-rules |
| `show cngfw dos-protection-rules id` | global | `show_cngfw_dos_protection_rules_id` | GET https://api.strata.paloaltonetworks.com/config/security/v1/dos-protection-rules/{id} |
| `show cngfw dynamic-user-groups` | global | `show_cngfw_dynamic_user_groups` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/dynamic-user-groups |
| `show cngfw dynamic-user-groups id` | global | `show_cngfw_dynamic_user_groups_id` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/dynamic-user-groups/{id} |
| `show cngfw external-dynamic-lists` | global | `show_cngfw_external_dynamic_lists` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/external-dynamic-lists |
| `show cngfw external-dynamic-lists id` | global | `show_cngfw_external_dynamic_lists_id` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/external-dynamic-lists/{id} |
| `show cngfw file-blocking-profiles` | global | `show_cngfw_file_blocking_profiles` | GET https://api.strata.paloaltonetworks.com/config/security/v1/file-blocking-profiles |
| `show cngfw file-blocking-profiles id` | global | `show_cngfw_file_blocking_profiles_id` | GET https://api.strata.paloaltonetworks.com/config/security/v1/file-blocking-profiles/{id} |
| `show cngfw folders` | global | `show_cngfw_folders` | GET https://api.strata.paloaltonetworks.com/config/setup/v1/folders |
| `show cngfw folders id` | global | `show_cngfw_folders_id` | GET https://api.strata.paloaltonetworks.com/config/setup/v1/folders/{id} |
| `show cngfw hip-objects` | global | `show_cngfw_hip_objects` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/hip-objects |
| `show cngfw hip-objects id` | global | `show_cngfw_hip_objects_id` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/hip-objects/{id} |
| `show cngfw hip-profiles` | global | `show_cngfw_hip_profiles` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/hip-profiles |
| `show cngfw hip-profiles id` | global | `show_cngfw_hip_profiles_id` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/hip-profiles/{id} |
| `show cngfw http-header-profiles` | global | `show_cngfw_http_header_profiles` | GET https://api.strata.paloaltonetworks.com/config/security/v1/http-header-profiles |
| `show cngfw http-header-profiles id` | global | `show_cngfw_http_header_profiles_id` | GET https://api.strata.paloaltonetworks.com/config/security/v1/http-header-profiles/{id} |
| `show cngfw http-server-profiles` | global | `show_cngfw_http_server_profiles` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/http-server-profiles |
| `show cngfw http-server-profiles id` | global | `show_cngfw_http_server_profiles_id` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/http-server-profiles/{id} |
| `show cngfw jobs` | global | `show_cngfw_jobs` | GET https://api.strata.paloaltonetworks.com/config/operations/v1/jobs |
| `show cngfw jobs id` | global | `show_cngfw_jobs_id` | GET https://api.strata.paloaltonetworks.com/config/operations/v1/jobs/{id} |
| `show cngfw kerberos-server-profiles` | global | `show_cngfw_kerberos_server_profiles` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/kerberos-server-profiles |
| `show cngfw kerberos-server-profiles id` | global | `show_cngfw_kerberos_server_profiles_id` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/kerberos-server-profiles/{id} |
| `show cngfw labels` | global | `show_cngfw_labels` | GET https://api.strata.paloaltonetworks.com/config/setup/v1/labels |
| `show cngfw labels id` | global | `show_cngfw_labels_id` | GET https://api.strata.paloaltonetworks.com/config/setup/v1/labels/{id} |
| `show cngfw ldap-server-profiles` | global | `show_cngfw_ldap_server_profiles` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/ldap-server-profiles |
| `show cngfw ldap-server-profiles id` | global | `show_cngfw_ldap_server_profiles_id` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/ldap-server-profiles/{id} |
| `show cngfw local-user-groups` | global | `show_cngfw_local_user_groups` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/local-user-groups |
| `show cngfw local-user-groups id` | global | `show_cngfw_local_user_groups_id` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/local-user-groups/{id} |
| `show cngfw local-users` | global | `show_cngfw_local_users` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/local-users |
| `show cngfw local-users id` | global | `show_cngfw_local_users_id` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/local-users/{id} |
| `show cngfw log-forwarding-profiles` | global | `show_cngfw_log_forwarding_profiles` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/log-forwarding-profiles |
| `show cngfw log-forwarding-profiles id` | global | `show_cngfw_log_forwarding_profiles_id` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/log-forwarding-profiles/{id} |
| `show cngfw mfa-servers` | global | `show_cngfw_mfa_servers` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/mfa-servers |
| `show cngfw mfa-servers id` | global | `show_cngfw_mfa_servers_id` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/mfa-servers/{id} |
| `show cngfw ocsp-responders` | global | `show_cngfw_ocsp_responders` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/ocsp-responders |
| `show cngfw ocsp-responders id` | global | `show_cngfw_ocsp_responders_id` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/ocsp-responders/{id} |
| `show cngfw onboarding-rules` | global | `show_cngfw_onboarding_rules` | GET https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1/onboarding-rules |
| `show cngfw onboarding-rules id` | global | `show_cngfw_onboarding_rules_id` | GET https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1/onboarding-rules/{id} |
| `show cngfw profile-groups` | global | `show_cngfw_profile_groups` | GET https://api.strata.paloaltonetworks.com/config/security/v1/profile-groups |
| `show cngfw profile-groups id` | global | `show_cngfw_profile_groups_id` | GET https://api.strata.paloaltonetworks.com/config/security/v1/profile-groups/{id} |
| `show cngfw properties` | global | `show_cngfw_properties` | GET https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1/properties |
| `show cngfw properties id` | global | `show_cngfw_properties_id` | GET https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1/properties/{id} |
| `show cngfw quarantined-devices` | global | `show_cngfw_quarantined_devices` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/quarantined-devices |
| `show cngfw radius-server-profiles` | global | `show_cngfw_radius_server_profiles` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/radius-server-profiles |
| `show cngfw radius-server-profiles id` | global | `show_cngfw_radius_server_profiles_id` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/radius-server-profiles/{id} |
| `show cngfw regions` | global | `show_cngfw_regions` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/regions |
| `show cngfw regions id` | global | `show_cngfw_regions_id` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/regions/{id} |
| `show cngfw saas-tenant-restrictions` | global | `show_cngfw_saas_tenant_restrictions` | GET https://api.strata.paloaltonetworks.com/config/security/v1/saas-tenant-restrictions |
| `show cngfw saml-server-profiles` | global | `show_cngfw_saml_server_profiles` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/saml-server-profiles |
| `show cngfw saml-server-profiles id` | global | `show_cngfw_saml_server_profiles_id` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/saml-server-profiles/{id} |
| `show cngfw scep-profiles` | global | `show_cngfw_scep_profiles` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/scep-profiles |
| `show cngfw scep-profiles id` | global | `show_cngfw_scep_profiles_id` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/scep-profiles/{id} |
| `show cngfw schedules` | global | `show_cngfw_schedules` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/schedules |
| `show cngfw schedules id` | global | `show_cngfw_schedules_id` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/schedules/{id} |
| `show cngfw security-rules` | global | `show_cngfw_security_rules` | GET https://api.strata.paloaltonetworks.com/config/security/v1/security-rules |
| `show cngfw security-rules id` | global | `show_cngfw_security_rules_id` | GET https://api.strata.paloaltonetworks.com/config/security/v1/security-rules/{id} |
| `show cngfw service-groups` | global | `show_cngfw_service_groups` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/service-groups |
| `show cngfw service-groups id` | global | `show_cngfw_service_groups_id` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/service-groups/{id} |
| `show cngfw services` | global | `show_cngfw_services` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/services |
| `show cngfw services id` | global | `show_cngfw_services_id` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/services/{id} |
| `show cngfw shared-snippets` | global | `show_cngfw_shared_snippets` | GET https://api.strata.paloaltonetworks.com/config/setup/v1/shared-snippets |
| `show cngfw site-groups` | global | `show_cngfw_site_groups` | GET https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1/site-groups |
| `show cngfw site-groups id` | global | `show_cngfw_site_groups_id` | GET https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1/site-groups/{id} |
| `show cngfw sites` | global | `show_cngfw_sites` | GET https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1/sites |
| `show cngfw sites id` | global | `show_cngfw_sites_id` | GET https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1/sites/{id} |
| `show cngfw snippet-audit-logs id` | global | `show_cngfw_snippet_audit_logs_id` | GET https://api.strata.paloaltonetworks.com/config/setup/v1/snippet-audit-logs/{id} |
| `show cngfw snippet-categories` | global | `show_cngfw_snippet_categories` | GET https://api.strata.paloaltonetworks.com/config/setup/v1/snippet-categories |
| `show cngfw snippet-categories id` | global | `show_cngfw_snippet_categories_id` | GET https://api.strata.paloaltonetworks.com/config/setup/v1/snippet-categories/{id} |
| `show cngfw snippets` | global | `show_cngfw_snippets` | GET https://api.strata.paloaltonetworks.com/config/setup/v1/snippets |
| `show cngfw snippets id` | global | `show_cngfw_snippets_id` | GET https://api.strata.paloaltonetworks.com/config/setup/v1/snippets/{id} |
| `show cngfw ssl-decryption-settings` | global | `show_cngfw_ssl_decryption_settings` | GET https://api.strata.paloaltonetworks.com/config/security/v1/ssl-decryption-settings |
| `show cngfw subscribed-tenants id` | global | `show_cngfw_subscribed_tenants_id` | GET https://api.strata.paloaltonetworks.com/config/setup/v1/subscribed-tenants/{id} |
| `show cngfw syslog-server-profiles` | global | `show_cngfw_syslog_server_profiles` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/syslog-server-profiles |
| `show cngfw syslog-server-profiles id` | global | `show_cngfw_syslog_server_profiles_id` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/syslog-server-profiles/{id} |
| `show cngfw tacacs-server-profiles` | global | `show_cngfw_tacacs_server_profiles` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/tacacs-server-profiles |
| `show cngfw tacacs-server-profiles id` | global | `show_cngfw_tacacs_server_profiles_id` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/tacacs-server-profiles/{id} |
| `show cngfw tags` | global | `show_cngfw_tags` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/tags |
| `show cngfw tags id` | global | `show_cngfw_tags_id` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/tags/{id} |
| `show cngfw tls-service-profiles` | global | `show_cngfw_tls_service_profiles` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/tls-service-profiles |
| `show cngfw tls-service-profiles id` | global | `show_cngfw_tls_service_profiles_id` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/tls-service-profiles/{id} |
| `show cngfw trusted-cas` | global | `show_cngfw_trusted_cas` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/trusted-certificate-authorities |
| `show cngfw trusted-tenant-overview` | global | `show_cngfw_trusted_tenant_overview` | GET https://api.strata.paloaltonetworks.com/config/setup/v1/trusted-tenant-overview |
| `show cngfw trusted-tenants` | global | `show_cngfw_trusted_tenants` | GET https://api.strata.paloaltonetworks.com/config/setup/v1/trusted-tenants |
| `show cngfw url-access-profiles` | global | `show_cngfw_url_access_profiles` | GET https://api.strata.paloaltonetworks.com/config/security/v1/url-access-profiles |
| `show cngfw url-access-profiles id` | global | `show_cngfw_url_access_profiles_id` | GET https://api.strata.paloaltonetworks.com/config/security/v1/url-access-profiles/{id} |
| `show cngfw url-admin-override` | global | `show_cngfw_url_admin_override` | GET https://api.strata.paloaltonetworks.com/config/security/v1/url-admin-override |
| `show cngfw url-categories` | global | `show_cngfw_url_categories` | GET https://api.strata.paloaltonetworks.com/config/security/v1/url-categories |
| `show cngfw url-categories id` | global | `show_cngfw_url_categories_id` | GET https://api.strata.paloaltonetworks.com/config/security/v1/url-categories/{id} |
| `show cngfw url-filtering-categories` | global | `show_cngfw_url_filtering_categories` | GET https://api.strata.paloaltonetworks.com/config/security/v1/url-filtering-categories |
| `show cngfw variables` | global | `show_cngfw_variables` | GET https://api.strata.paloaltonetworks.com/config/setup/v1/variables |
| `show cngfw variables id` | global | `show_cngfw_variables_id` | GET https://api.strata.paloaltonetworks.com/config/setup/v1/variables/{id} |
| `show cngfw vuln-profiles` | global | `show_cngfw_vuln_profiles` | GET https://api.strata.paloaltonetworks.com/config/security/v1/vulnerability-protection-profiles |
| `show cngfw vuln-profiles id` | global | `show_cngfw_vuln_profiles_id` | GET https://api.strata.paloaltonetworks.com/config/security/v1/vulnerability-protection-profiles/{id} |
| `show cngfw vuln-signatures` | global | `show_cngfw_vuln_signatures` | GET https://api.strata.paloaltonetworks.com/config/security/v1/vulnerability-protection-signatures |
| `show cngfw vuln-signatures id` | global | `show_cngfw_vuln_signatures_id` | GET https://api.strata.paloaltonetworks.com/config/security/v1/vulnerability-protection-signatures/{id} |
| `show cngfw wildfire-profiles` | global | `show_cngfw_wildfire_profiles` | GET https://api.strata.paloaltonetworks.com/config/security/v1/wildfire-anti-virus-profiles |
| `show cngfw wildfire-profiles id` | global | `show_cngfw_wildfire_profiles_id` | GET https://api.strata.paloaltonetworks.com/config/security/v1/wildfire-anti-virus-profiles/{id} |
| `update cngfw address-groups` | global | `update_cngfw_address_groups` | PUT https://api.strata.paloaltonetworks.com/config/objects/v1/address-groups/{id} |
| `update cngfw addresses` | global | `update_cngfw_addresses` | PUT https://api.strata.paloaltonetworks.com/config/objects/v1/addresses/{id} |
| `update cngfw adv-device-objs` | global | `update_cngfw_adv_device_objs` | PUT https://api.strata.paloaltonetworks.com/config/objects/v1/advanced-device-objects |
| `update cngfw anti-spyware-profiles` | global | `update_cngfw_anti_spyware_profiles` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/anti-spyware-profiles/{id} |
| `update cngfw anti-spyware-signatures` | global | `update_cngfw_anti_spyware_signatures` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/anti-spyware-signatures/{id} |
| `update cngfw app-override-rules` | global | `update_cngfw_app_override_rules` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/app-override-rules/{id} |
| `update cngfw application-filters` | global | `update_cngfw_application_filters` | PUT https://api.strata.paloaltonetworks.com/config/objects/v1/application-filters/{id} |
| `update cngfw application-groups` | global | `update_cngfw_application_groups` | PUT https://api.strata.paloaltonetworks.com/config/objects/v1/application-groups/{id} |
| `update cngfw applications` | global | `update_cngfw_applications` | PUT https://api.strata.paloaltonetworks.com/config/objects/v1/applications/{id} |
| `update cngfw authentication-portals` | global | `update_cngfw_authentication_portals` | PUT https://api.strata.paloaltonetworks.com/config/identity/v1/authentication-portals/{id} |
| `update cngfw authentication-profiles` | global | `update_cngfw_authentication_profiles` | PUT https://api.strata.paloaltonetworks.com/config/identity/v1/authentication-profiles/{id} |
| `update cngfw authentication-rules` | global | `update_cngfw_authentication_rules` | PUT https://api.strata.paloaltonetworks.com/config/identity/v1/authentication-rules/{id} |
| `update cngfw authentication-sequences` | global | `update_cngfw_authentication_sequences` | PUT https://api.strata.paloaltonetworks.com/config/identity/v1/authentication-sequences/{id} |
| `update cngfw auto-tag-actions` | global | `update_cngfw_auto_tag_actions` | PUT https://api.strata.paloaltonetworks.com/config/objects/v1/auto-tag-actions |
| `update cngfw certificate-profiles` | global | `update_cngfw_certificate_profiles` | PUT https://api.strata.paloaltonetworks.com/config/identity/v1/certificate-profiles/{id} |
| `update cngfw data-filtering-profiles` | global | `update_cngfw_data_filtering_profiles` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/data-filtering-profiles/{id} |
| `update cngfw data-objects` | global | `update_cngfw_data_objects` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/data-objects/{id} |
| `update cngfw decryption-exclusions` | global | `update_cngfw_decryption_exclusions` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/decryption-exclusions/{id} |
| `update cngfw decryption-profiles` | global | `update_cngfw_decryption_profiles` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/decryption-profiles/{id} |
| `update cngfw decryption-rules` | global | `update_cngfw_decryption_rules` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/decryption-rules/{id} |
| `update cngfw device-contexts` | global | `update_cngfw_device_contexts` | PUT https://api.strata.paloaltonetworks.com/config/objects/v1/device-context-segments/{id} |
| `update cngfw devices` | global | `update_cngfw_devices` | PUT https://api.strata.paloaltonetworks.com/config/setup/v1/devices/{id} |
| `update cngfw dns-security-profiles` | global | `update_cngfw_dns_security_profiles` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/dns-security-profiles/{id} |
| `update cngfw dos-protection-profiles` | global | `update_cngfw_dos_protection_profiles` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/dos-protection-profiles/{id} |
| `update cngfw dos-protection-rules` | global | `update_cngfw_dos_protection_rules` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/dos-protection-rules/{id} |
| `update cngfw dynamic-user-groups` | global | `update_cngfw_dynamic_user_groups` | PUT https://api.strata.paloaltonetworks.com/config/objects/v1/dynamic-user-groups/{id} |
| `update cngfw external-dynamic-lists` | global | `update_cngfw_external_dynamic_lists` | PUT https://api.strata.paloaltonetworks.com/config/objects/v1/external-dynamic-lists/{id} |
| `update cngfw file-blocking-profiles` | global | `update_cngfw_file_blocking_profiles` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/file-blocking-profiles/{id} |
| `update cngfw folders` | global | `update_cngfw_folders` | PUT https://api.strata.paloaltonetworks.com/config/setup/v1/folders/{id} |
| `update cngfw hip-objects` | global | `update_cngfw_hip_objects` | PUT https://api.strata.paloaltonetworks.com/config/objects/v1/hip-objects/{id} |
| `update cngfw hip-profiles` | global | `update_cngfw_hip_profiles` | PUT https://api.strata.paloaltonetworks.com/config/objects/v1/hip-profiles/{id} |
| `update cngfw http-header-profiles` | global | `update_cngfw_http_header_profiles` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/http-header-profiles/{id} |
| `update cngfw http-server-profiles` | global | `update_cngfw_http_server_profiles` | PUT https://api.strata.paloaltonetworks.com/config/objects/v1/http-server-profiles/{id} |
| `update cngfw kerberos-server-profiles` | global | `update_cngfw_kerberos_server_profiles` | PUT https://api.strata.paloaltonetworks.com/config/identity/v1/kerberos-server-profiles/{id} |
| `update cngfw labels` | global | `update_cngfw_labels` | PUT https://api.strata.paloaltonetworks.com/config/setup/v1/labels/{id} |
| `update cngfw ldap-server-profiles` | global | `update_cngfw_ldap_server_profiles` | PUT https://api.strata.paloaltonetworks.com/config/identity/v1/ldap-server-profiles/{id} |
| `update cngfw local-user-groups` | global | `update_cngfw_local_user_groups` | PUT https://api.strata.paloaltonetworks.com/config/identity/v1/local-user-groups/{id} |
| `update cngfw local-users` | global | `update_cngfw_local_users` | PUT https://api.strata.paloaltonetworks.com/config/identity/v1/local-users/{id} |
| `update cngfw log-forwarding-profiles` | global | `update_cngfw_log_forwarding_profiles` | PUT https://api.strata.paloaltonetworks.com/config/objects/v1/log-forwarding-profiles/{id} |
| `update cngfw mfa-servers` | global | `update_cngfw_mfa_servers` | PUT https://api.strata.paloaltonetworks.com/config/identity/v1/mfa-servers/{id} |
| `update cngfw objects adv-device-objs` | global | `update_cngfw_adv_device_objs` | PUT https://api.strata.paloaltonetworks.com/config/objects/v1/advanced-device-objects/{id} |
| `update cngfw ocsp-responders` | global | `update_cngfw_ocsp_responders` | PUT https://api.strata.paloaltonetworks.com/config/identity/v1/ocsp-responders/{id} |
| `update cngfw onboarding-rules` | global | `update_cngfw_onboarding_rules` | PUT https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1/onboarding-rules/{id} |
| `update cngfw profile-groups` | global | `update_cngfw_profile_groups` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/profile-groups/{id} |
| `update cngfw properties` | global | `update_cngfw_properties` | PUT https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1/properties/{id} |
| `update cngfw radius-server-profiles` | global | `update_cngfw_radius_server_profiles` | PUT https://api.strata.paloaltonetworks.com/config/identity/v1/radius-server-profiles/{id} |
| `update cngfw regions` | global | `update_cngfw_regions` | PUT https://api.strata.paloaltonetworks.com/config/objects/v1/regions/{id} |
| `update cngfw saas-tenant-restrictions` | global | `update_cngfw_saas_tenant_restrictions` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/saas-tenant-restrictions |
| `update cngfw saml-server-profiles` | global | `update_cngfw_saml_server_profiles` | PUT https://api.strata.paloaltonetworks.com/config/identity/v1/saml-server-profiles/{id} |
| `update cngfw scep-profiles` | global | `update_cngfw_scep_profiles` | PUT https://api.strata.paloaltonetworks.com/config/identity/v1/scep-profiles/{id} |
| `update cngfw schedules` | global | `update_cngfw_schedules` | PUT https://api.strata.paloaltonetworks.com/config/objects/v1/schedules/{id} |
| `update cngfw security-rules` | global | `update_cngfw_security_rules` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/security-rules/{id} |
| `update cngfw service-groups` | global | `update_cngfw_service_groups` | PUT https://api.strata.paloaltonetworks.com/config/objects/v1/service-groups/{id} |
| `update cngfw services` | global | `update_cngfw_services` | PUT https://api.strata.paloaltonetworks.com/config/objects/v1/services/{id} |
| `update cngfw shared-snippets` | global | `update_cngfw_shared_snippets` | PUT https://api.strata.paloaltonetworks.com/config/setup/v1/shared-snippets |
| `update cngfw site-groups` | global | `update_cngfw_site_groups` | PUT https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1/site-groups/{id} |
| `update cngfw sites` | global | `update_cngfw_sites` | PUT https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1/sites/{id} |
| `update cngfw snippets` | global | `update_cngfw_snippets` | PUT https://api.strata.paloaltonetworks.com/config/setup/v1/snippets/{id} |
| `update cngfw ssl-decryption-settings` | global | `update_cngfw_ssl_decryption_settings` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/ssl-decryption-settings |
| `update cngfw subscribed-tenants` | global | `update_cngfw_subscribed_tenants` | PUT https://api.strata.paloaltonetworks.com/config/setup/v1/subscribed-tenants |
| `update cngfw syslog-server-profiles` | global | `update_cngfw_syslog_server_profiles` | PUT https://api.strata.paloaltonetworks.com/config/objects/v1/syslog-server-profiles/{id} |
| `update cngfw tacacs-server-profiles` | global | `update_cngfw_tacacs_server_profiles` | PUT https://api.strata.paloaltonetworks.com/config/identity/v1/tacacs-server-profiles/{id} |
| `update cngfw tags` | global | `update_cngfw_tags` | PUT https://api.strata.paloaltonetworks.com/config/objects/v1/tags/{id} |
| `update cngfw tls-service-profiles` | global | `update_cngfw_tls_service_profiles` | PUT https://api.strata.paloaltonetworks.com/config/identity/v1/tls-service-profiles/{id} |
| `update cngfw url-access-profiles` | global | `update_cngfw_url_access_profiles` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/url-access-profiles/{id} |
| `update cngfw url-categories` | global | `update_cngfw_url_categories` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/url-categories/{id} |
| `update cngfw variables` | global | `update_cngfw_variables` | PUT https://api.strata.paloaltonetworks.com/config/setup/v1/variables/{id} |
| `update cngfw vuln-profiles` | global | `update_cngfw_vuln_profiles` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/vulnerability-protection-profiles/{id} |
| `update cngfw vuln-signatures` | global | `update_cngfw_vuln_signatures` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/vulnerability-protection-signatures/{id} |
| `update cngfw wildfire-profiles` | global | `update_cngfw_wildfire_profiles` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/wildfire-anti-virus-profiles/{id} |

## Device

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `delete authentication-settings` | global | `delete_authentication_settings` | DELETE https://api.strata.paloaltonetworks.com/config/device/v1/authentication-settings/{id} |
| `delete content-id-settings` | global | `delete_content_id_settings` | DELETE https://api.strata.paloaltonetworks.com/config/device/v1/content-id-settings/{id} |
| `delete device-redistribution-collector` | global | `delete_device_redistribution_collector` | DELETE https://api.strata.paloaltonetworks.com/config/device/v1/device-redistribution-collector/{id} |
| `delete general-settings` | global | `delete_general_settings` | DELETE https://api.strata.paloaltonetworks.com/config/device/v1/general-settings/{id} |
| `delete ha-configurations` | global | `delete_ha_configurations` | DELETE https://api.strata.paloaltonetworks.com/config/device/v1/ha-configurations/{id} |
| `delete management-interface` | global | `delete_management_interface` | DELETE https://api.strata.paloaltonetworks.com/config/device/v1/management-interface/{id} |
| `delete motd-banner-settings` | global | `delete_motd_banner_settings` | DELETE https://api.strata.paloaltonetworks.com/config/device/v1/motd-banner-settings/{id} |
| `delete service-route` | global | `delete_service_route` | DELETE https://api.strata.paloaltonetworks.com/config/device/v1/service-route/{id} |
| `delete service-settings` | global | `delete_service_settings` | DELETE https://api.strata.paloaltonetworks.com/config/device/v1/service-settings/{id} |
| `delete session-settings` | global | `delete_session_settings` | DELETE https://api.strata.paloaltonetworks.com/config/device/v1/session-settings/{id} |
| `delete session-timeouts` | global | `delete_session_timeouts` | DELETE https://api.strata.paloaltonetworks.com/config/device/v1/session-timeouts/{id} |
| `delete tcp-settings` | global | `delete_tcp_settings` | DELETE https://api.strata.paloaltonetworks.com/config/device/v1/tcp-settings/{id} |
| `delete update-schedule` | global | `delete_update_schedule` | DELETE https://api.strata.paloaltonetworks.com/config/device/v1/update-schedule/{id} |
| `delete vpn-settings` | global | `delete_vpn_settings` | DELETE https://api.strata.paloaltonetworks.com/config/device/v1/vpn-settings/{id} |
| `set authentication-settings` | global | `create_authentication_settings` | POST https://api.strata.paloaltonetworks.com/config/device/v1/authentication-settings |
| `set content-id-settings` | global | `create_content_id_settings` | POST https://api.strata.paloaltonetworks.com/config/device/v1/content-id-settings |
| `set device-redistribution-collector` | global | `create_device_redistribution_collector` | POST https://api.strata.paloaltonetworks.com/config/device/v1/device-redistribution-collector |
| `set general-settings` | global | `create_general_settings` | POST https://api.strata.paloaltonetworks.com/config/device/v1/general-settings |
| `set ha-configurations` | global | `create_ha_configurations` | POST https://api.strata.paloaltonetworks.com/config/device/v1/ha-configurations |
| `set management-interface` | global | `create_management_interface` | POST https://api.strata.paloaltonetworks.com/config/device/v1/management-interface |
| `set motd-banner-settings` | global | `create_motd_banner_settings` | POST https://api.strata.paloaltonetworks.com/config/device/v1/motd-banner-settings |
| `set service-route` | global | `create_service_route` | POST https://api.strata.paloaltonetworks.com/config/device/v1/service-route |
| `set service-settings` | global | `create_service_settings` | POST https://api.strata.paloaltonetworks.com/config/device/v1/service-settings |
| `set session-settings` | global | `create_session_settings` | POST https://api.strata.paloaltonetworks.com/config/device/v1/session-settings |
| `set session-timeouts` | global | `create_session_timeouts` | POST https://api.strata.paloaltonetworks.com/config/device/v1/session-timeouts |
| `set tcp-settings` | global | `create_tcp_settings` | POST https://api.strata.paloaltonetworks.com/config/device/v1/tcp-settings |
| `set update-schedule` | global | `create_update_schedule` | POST https://api.strata.paloaltonetworks.com/config/device/v1/update-schedule |
| `set vpn-settings` | global | `create_vpn_settings` | POST https://api.strata.paloaltonetworks.com/config/device/v1/vpn-settings |
| `show authentication-settings` | global | `show_authentication_settings` | GET https://api.strata.paloaltonetworks.com/config/device/v1/authentication-settings |
| `show authentication-settings id` | global | `show_authentication_settings_id` | GET https://api.strata.paloaltonetworks.com/config/device/v1/authentication-settings/{id} |
| `show content-id-settings` | global | `show_content_id_settings` | GET https://api.strata.paloaltonetworks.com/config/device/v1/content-id-settings |
| `show content-id-settings id` | global | `show_content_id_settings_id` | GET https://api.strata.paloaltonetworks.com/config/device/v1/content-id-settings/{id} |
| `show device-redistribution-collector` | global | `show_device_redistribution_collector` | GET https://api.strata.paloaltonetworks.com/config/device/v1/device-redistribution-collector |
| `show device-redistribution-collector id` | global | `show_device_redistribution_collector_id` | GET https://api.strata.paloaltonetworks.com/config/device/v1/device-redistribution-collector/{id} |
| `show general-settings` | global | `show_general_settings` | GET https://api.strata.paloaltonetworks.com/config/device/v1/general-settings |
| `show general-settings id` | global | `show_general_settings_id` | GET https://api.strata.paloaltonetworks.com/config/device/v1/general-settings/{id} |
| `show ha-configurations` | global | `show_ha_configurations` | GET https://api.strata.paloaltonetworks.com/config/device/v1/ha-configurations |
| `show ha-configurations id` | global | `show_ha_configurations_id` | GET https://api.strata.paloaltonetworks.com/config/device/v1/ha-configurations/{id} |
| `show ha-devices` | global | `show_ha_devices` | GET https://api.strata.paloaltonetworks.com/config/device/v1/ha-devices |
| `show management-interface` | global | `show_management_interface` | GET https://api.strata.paloaltonetworks.com/config/device/v1/management-interface |
| `show management-interface id` | global | `show_management_interface_id` | GET https://api.strata.paloaltonetworks.com/config/device/v1/management-interface/{id} |
| `show motd-banner-settings` | global | `show_motd_banner_settings` | GET https://api.strata.paloaltonetworks.com/config/device/v1/motd-banner-settings |
| `show motd-banner-settings id` | global | `show_motd_banner_settings_id` | GET https://api.strata.paloaltonetworks.com/config/device/v1/motd-banner-settings/{id} |
| `show service-route` | global | `show_service_route` | GET https://api.strata.paloaltonetworks.com/config/device/v1/service-route |
| `show service-route id` | global | `show_service_route_id` | GET https://api.strata.paloaltonetworks.com/config/device/v1/service-route/{id} |
| `show service-settings` | global | `show_service_settings` | GET https://api.strata.paloaltonetworks.com/config/device/v1/service-settings |
| `show service-settings id` | global | `show_service_settings_id` | GET https://api.strata.paloaltonetworks.com/config/device/v1/service-settings/{id} |
| `show session-settings` | global | `show_session_settings` | GET https://api.strata.paloaltonetworks.com/config/device/v1/session-settings |
| `show session-settings id` | global | `show_session_settings_id` | GET https://api.strata.paloaltonetworks.com/config/device/v1/session-settings/{id} |
| `show session-timeouts` | global | `show_session_timeouts` | GET https://api.strata.paloaltonetworks.com/config/device/v1/session-timeouts |
| `show session-timeouts id` | global | `show_session_timeouts_id` | GET https://api.strata.paloaltonetworks.com/config/device/v1/session-timeouts/{id} |
| `show tcp-settings` | global | `show_tcp_settings` | GET https://api.strata.paloaltonetworks.com/config/device/v1/tcp-settings |
| `show tcp-settings id` | global | `show_tcp_settings_id` | GET https://api.strata.paloaltonetworks.com/config/device/v1/tcp-settings/{id} |
| `show update-schedule` | global | `show_update_schedule` | GET https://api.strata.paloaltonetworks.com/config/device/v1/update-schedule |
| `show update-schedule id` | global | `show_update_schedule_id` | GET https://api.strata.paloaltonetworks.com/config/device/v1/update-schedule/{id} |
| `show vpn-settings` | global | `show_vpn_settings` | GET https://api.strata.paloaltonetworks.com/config/device/v1/vpn-settings |
| `show vpn-settings id` | global | `show_vpn_settings_id` | GET https://api.strata.paloaltonetworks.com/config/device/v1/vpn-settings/{id} |
| `update authentication-settings` | global | `update_authentication_settings` | PUT https://api.strata.paloaltonetworks.com/config/device/v1/authentication-settings/{id} |
| `update content-id-settings` | global | `update_content_id_settings` | PUT https://api.strata.paloaltonetworks.com/config/device/v1/content-id-settings/{id} |
| `update device-redistribution-collector` | global | `update_device_redistribution_collector` | PUT https://api.strata.paloaltonetworks.com/config/device/v1/device-redistribution-collector/{id} |
| `update general-settings` | global | `update_general_settings` | PUT https://api.strata.paloaltonetworks.com/config/device/v1/general-settings/{id} |
| `update ha-configurations` | global | `update_ha_configurations` | PUT https://api.strata.paloaltonetworks.com/config/device/v1/ha-configurations/{id} |
| `update management-interface` | global | `update_management_interface` | PUT https://api.strata.paloaltonetworks.com/config/device/v1/management-interface/{id} |
| `update motd-banner-settings` | global | `update_motd_banner_settings` | PUT https://api.strata.paloaltonetworks.com/config/device/v1/motd-banner-settings/{id} |
| `update service-route` | global | `update_service_route` | PUT https://api.strata.paloaltonetworks.com/config/device/v1/service-route/{id} |
| `update service-settings` | global | `update_service_settings` | PUT https://api.strata.paloaltonetworks.com/config/device/v1/service-settings/{id} |
| `update session-settings` | global | `update_session_settings` | PUT https://api.strata.paloaltonetworks.com/config/device/v1/session-settings/{id} |
| `update session-timeouts` | global | `update_session_timeouts` | PUT https://api.strata.paloaltonetworks.com/config/device/v1/session-timeouts/{id} |
| `update tcp-settings` | global | `update_tcp_settings` | PUT https://api.strata.paloaltonetworks.com/config/device/v1/tcp-settings/{id} |
| `update update-schedule` | global | `update_update_schedule` | PUT https://api.strata.paloaltonetworks.com/config/device/v1/update-schedule/{id} |
| `update vpn-settings` | global | `update_vpn_settings` | PUT https://api.strata.paloaltonetworks.com/config/device/v1/vpn-settings/{id} |

## Diagnostics

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `packet-tracer` | folder | `packet_tracer` | (client-side simulation of the folder rule base) |
| `test security-policy-match` | folder | `packet_tracer` | (client-side simulation of the folder rule base) |

## Iam

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `delete iam access-policies` | global | `delete_iam_access_policies` | DELETE https://api.sase.paloaltonetworks.com/iam/v1/access_policies/{id} |
| `delete iam custom-roles` | global | `delete_iam_custom_roles` | DELETE https://api.sase.paloaltonetworks.com/iam/v1/custom_roles/{name} |
| `delete service-accounts` | global | `delete_service_accounts` | DELETE https://api.sase.paloaltonetworks.com/iam/v1/service_accounts/{id} |
| `set iam access-policies` | global | `create_iam_access_policies` | POST https://api.sase.paloaltonetworks.com/iam/v1/access_policies |
| `set iam custom-roles` | global | `create_iam_custom_roles` | POST https://api.sase.paloaltonetworks.com/iam/v1/custom_roles |
| `set iam sso-users` | global | `create_iam_sso_users` | POST https://api.sase.paloaltonetworks.com/iam/v1/sso_users |
| `set service-accounts` | global | `create_service_accounts` | POST https://api.sase.paloaltonetworks.com/iam/v1/service_accounts |
| `set service-accounts reset` | global | `create_service_accounts_reset` | POST https://api.sase.paloaltonetworks.com/iam/v1/service_accounts/{id}/operations/reset |
| `show iam access-policies` | global | `show_iam_access_policies` | GET https://api.sase.paloaltonetworks.com/iam/v1/access_policies |
| `show iam access-policies id` | global | `show_iam_access_policies_id` | GET https://api.sase.paloaltonetworks.com/iam/v1/access_policies/{id} |
| `show iam custom-roles` | global | `show_iam_custom_roles` | GET https://api.sase.paloaltonetworks.com/iam/v1/custom_roles |
| `show iam custom-roles id` | global | `show_iam_custom_roles_id` | GET https://api.sase.paloaltonetworks.com/iam/v1/custom_roles/{name} |
| `show iam permission-sets` | global | `show_iam_permission_sets` | GET https://api.sase.paloaltonetworks.com/iam/v1/permission_sets |
| `show iam permission-sets id` | global | `show_iam_permission_sets_id` | GET https://api.sase.paloaltonetworks.com/iam/v1/permission_sets/{name} |
| `show iam permissions` | global | `show_iam_permissions` | GET https://api.sase.paloaltonetworks.com/iam/v1/permissions |
| `show iam permissions id` | global | `show_iam_permissions_id` | GET https://api.sase.paloaltonetworks.com/iam/v1/permissions/{name} |
| `show iam roles` | global | `show_iam_roles` | GET https://api.sase.paloaltonetworks.com/iam/v1/roles |
| `show iam roles id` | global | `show_iam_roles_id` | GET https://api.sase.paloaltonetworks.com/iam/v1/roles/{name} |
| `show iam sso-users` | global | `show_iam_sso_users` | GET https://api.sase.paloaltonetworks.com/iam/v1/sso_users |
| `show service-accounts` | global | `show_service_accounts` | GET https://api.sase.paloaltonetworks.com/iam/v1/service_accounts |
| `show service-accounts id` | global | `show_service_accounts_id` | GET https://api.sase.paloaltonetworks.com/iam/v1/service_accounts/{id} |
| `update iam custom-roles` | global | `update_iam_custom_roles` | PUT https://api.sase.paloaltonetworks.com/iam/v1/custom_roles/{name} |
| `update service-accounts` | global | `update_service_accounts` | PUT https://api.sase.paloaltonetworks.com/iam/v1/service_accounts/{id} |

## Identity

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `show authentication-profile` | folder | `authentication` | GET /config/identity/v1/authentication-profiles |
| `show authentication-rules` | folder | `authentication` | GET /config/identity/v1/authentication-rules |
| `show certificate-profile` | folder | `certificates` | GET /config/identity/v1/certificate-profiles |
| `show local-user` | folder | `local_users` | GET /config/identity/v1/local-users |
| `show local-user-group` | folder | `local_users` | GET /config/identity/v1/local-user-groups |
| `show mfa-server` | folder | `authentication` | GET /config/identity/v1/mfa-servers |
| `show radius-server` | folder | `authentication` | GET /config/identity/v1/radius-server-profiles |
| `show tls-service-profile` | folder | `certificates` | GET /config/identity/v1/tls-service-profiles |
| `show user ip-user-mapping` | device | `local_users` | (live device state — SSH via --remote) |

## Incidents

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `set incidents incidents search` | global | `create_incidents_incidents_search` | POST https://api.strata.paloaltonetworks.com/incidents/v1/search |
| `show incidents incidents details id` | global | `show_incidents_incidents_details_id` | GET https://api.strata.paloaltonetworks.com/incidents/v1/details/{incident-id} |

## Network

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `delete aggregate-interfaces` | global | `delete_aggregate_interfaces` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/aggregate-interfaces/{id} |
| `delete auto-vpn-clusters` | global | `delete_auto_vpn_clusters` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/auto-vpn-clusters/{id} |
| `delete bgp-af-profiles` | global | `delete_bgp_af_profiles` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/bgp-address-family-profiles/{id} |
| `delete bgp-auth-profiles` | global | `delete_bgp_auth_profiles` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/bgp-auth-profiles/{id} |
| `delete bgp-filtering-profiles` | global | `delete_bgp_filtering_profiles` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/bgp-filtering-profiles/{id} |
| `delete bgp-redist-profiles` | global | `delete_bgp_redist_profiles` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/bgp-redistribution-profiles/{id} |
| `delete bgp-route-maps` | global | `delete_bgp_route_maps` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/bgp-route-maps/{id} |
| `delete bgp-routemap-redist` | global | `delete_bgp_routemap_redist` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/bgp-route-map-redistributions/{id} |
| `delete config-match-list` | global | `delete_config_match_list` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/config-match-list/{id} |
| `delete dhcp-interfaces` | global | `delete_dhcp_interfaces` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/dhcp-interfaces/{id} |
| `delete dns-proxies` | global | `delete_dns_proxies` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/dns-proxies/{id} |
| `delete ethernet-interfaces` | global | `delete_ethernet_interfaces` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/ethernet-interfaces/{id} |
| `delete gp-match-list` | global | `delete_gp_match_list` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/globalprotect-match-list/{id} |
| `delete hipmatch-match-list` | global | `delete_hipmatch_match_list` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/hipmatch-match-list/{id} |
| `delete if-mgmt-profiles` | global | `delete_if_mgmt_profiles` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/interface-management-profiles/{id} |
| `delete ike-crypto-profiles` | global | `delete_ike_crypto_profiles` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/ike-crypto-profiles/{id} |
| `delete ike-gateways` | global | `delete_ike_gateways` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/ike-gateways/{id} |
| `delete ipsec-crypto-profiles` | global | `delete_ipsec_crypto_profiles` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/ipsec-crypto-profiles/{id} |
| `delete ipsec-tunnels` | global | `delete_ipsec_tunnels` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/ipsec-tunnels/{id} |
| `delete iptag-match-list` | global | `delete_iptag_match_list` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/iptag-match-list/{id} |
| `delete layer2-subinterfaces` | global | `delete_layer2_subinterfaces` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/layer2-subinterfaces/{id} |
| `delete layer3-subinterfaces` | global | `delete_layer3_subinterfaces` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/layer3-subinterfaces/{id} |
| `delete link-tags` | global | `delete_link_tags` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/link-tags/{id} |
| `delete lldp-profiles` | global | `delete_lldp_profiles` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/lldp-profiles/{id} |
| `delete logical-routers` | global | `delete_logical_routers` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/logical-routers/{id} |
| `delete loopback-interfaces` | global | `delete_loopback_interfaces` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/loopback-interfaces/{id} |
| `delete nat-rules` | global | `delete_nat_rules` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/nat-rules/{id} |
| `delete npb-profiles` | global | `delete_npb_profiles` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/network_packet_broker_profiles/{id} |
| `delete npb-rules` | global | `delete_npb_rules` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/network_packet_broker_rules/{id} |
| `delete ospf-auth-profiles` | global | `delete_ospf_auth_profiles` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/ospf-auth-profiles/{id} |
| `delete pbf-rules` | global | `delete_pbf_rules` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/pbf-rules/{id} |
| `delete qos-policy-rules` | global | `delete_qos_policy_rules` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/qos-policy-rules/{id} |
| `delete qos-profiles` | global | `delete_qos_profiles` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/qos-profiles/{id} |
| `delete route-access-lists` | global | `delete_route_access_lists` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/route-access-lists/{id} |
| `delete route-community-lists` | global | `delete_route_community_lists` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/route-community-lists/{id} |
| `delete route-path-acls` | global | `delete_route_path_acls` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/route-path-access-lists/{id} |
| `delete route-prefix-lists` | global | `delete_route_prefix_lists` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/route-prefix-lists/{id} |
| `delete sdwan-error-profiles` | global | `delete_sdwan_error_profiles` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-error-correction-profiles/{id} |
| `delete sdwan-path-profiles` | global | `delete_sdwan_path_profiles` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-path-quality-profiles/{id} |
| `delete sdwan-rules` | global | `delete_sdwan_rules` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-rules/{id} |
| `delete sdwan-saas-profiles` | global | `delete_sdwan_saas_profiles` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-saas-quality-profiles/{id} |
| `delete sdwan-traffic-profiles` | global | `delete_sdwan_traffic_profiles` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-traffic-distribution-profiles/{id} |
| `delete system-match-list` | global | `delete_system_match_list` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/system-match-list/{id} |
| `delete tunnel-interfaces` | global | `delete_tunnel_interfaces` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/tunnel-interfaces/{id} |
| `delete userid-match-list` | global | `delete_userid_match_list` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/userid-match-list/{id} |
| `delete vlan-interfaces` | global | `delete_vlan_interfaces` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/vlan-interfaces/{id} |
| `delete zone-profiles` | global | `delete_zone_profiles` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/zone-protection-profiles/{id} |
| `delete zones` | global | `delete_zones` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/zones/{id} |
| `set aggregate-interfaces` | global | `create_aggregate_interfaces` | POST https://api.strata.paloaltonetworks.com/config/network/v1/aggregate-interfaces |
| `set auto-vpn-clusters` | global | `create_auto_vpn_clusters` | POST https://api.strata.paloaltonetworks.com/config/network/v1/auto-vpn-clusters |
| `set auto-vpn-push` | global | `create_auto_vpn_push` | POST https://api.strata.paloaltonetworks.com/config/network/v1/auto-vpn-push |
| `set bgp-af-profiles` | global | `create_bgp_af_profiles` | POST https://api.strata.paloaltonetworks.com/config/network/v1/bgp-address-family-profiles |
| `set bgp-auth-profiles` | global | `create_bgp_auth_profiles` | POST https://api.strata.paloaltonetworks.com/config/network/v1/bgp-auth-profiles |
| `set bgp-filtering-profiles` | global | `create_bgp_filtering_profiles` | POST https://api.strata.paloaltonetworks.com/config/network/v1/bgp-filtering-profiles |
| `set bgp-redist-profiles` | global | `create_bgp_redist_profiles` | POST https://api.strata.paloaltonetworks.com/config/network/v1/bgp-redistribution-profiles |
| `set bgp-route-maps` | global | `create_bgp_route_maps` | POST https://api.strata.paloaltonetworks.com/config/network/v1/bgp-route-maps |
| `set bgp-routemap-redist` | global | `create_bgp_routemap_redist` | POST https://api.strata.paloaltonetworks.com/config/network/v1/bgp-route-map-redistributions |
| `set config-match-list` | global | `create_config_match_list` | POST https://api.strata.paloaltonetworks.com/config/network/v1/config-match-list |
| `set dhcp-interfaces` | global | `create_dhcp_interfaces` | POST https://api.strata.paloaltonetworks.com/config/network/v1/dhcp-interfaces |
| `set dns-proxies` | global | `create_dns_proxies` | POST https://api.strata.paloaltonetworks.com/config/network/v1/dns-proxies |
| `set ethernet-interfaces` | global | `create_ethernet_interfaces` | POST https://api.strata.paloaltonetworks.com/config/network/v1/ethernet-interfaces |
| `set gp-match-list` | global | `create_gp_match_list` | POST https://api.strata.paloaltonetworks.com/config/network/v1/globalprotect-match-list |
| `set hipmatch-match-list` | global | `create_hipmatch_match_list` | POST https://api.strata.paloaltonetworks.com/config/network/v1/hipmatch-match-list |
| `set if-mgmt-profiles` | global | `create_if_mgmt_profiles` | POST https://api.strata.paloaltonetworks.com/config/network/v1/interface-management-profiles |
| `set ike-crypto-profiles` | global | `create_ike_crypto_profiles` | POST https://api.strata.paloaltonetworks.com/config/network/v1/ike-crypto-profiles |
| `set ike-gateways` | global | `create_ike_gateways` | POST https://api.strata.paloaltonetworks.com/config/network/v1/ike-gateways |
| `set ipsec-crypto-profiles` | global | `create_ipsec_crypto_profiles` | POST https://api.strata.paloaltonetworks.com/config/network/v1/ipsec-crypto-profiles |
| `set ipsec-tunnels` | global | `create_ipsec_tunnels` | POST https://api.strata.paloaltonetworks.com/config/network/v1/ipsec-tunnels |
| `set iptag-match-list` | global | `create_iptag_match_list` | POST https://api.strata.paloaltonetworks.com/config/network/v1/iptag-match-list |
| `set layer2-subinterfaces` | global | `create_layer2_subinterfaces` | POST https://api.strata.paloaltonetworks.com/config/network/v1/layer2-subinterfaces |
| `set layer3-subinterfaces` | global | `create_layer3_subinterfaces` | POST https://api.strata.paloaltonetworks.com/config/network/v1/layer3-subinterfaces |
| `set link-tags` | global | `create_link_tags` | POST https://api.strata.paloaltonetworks.com/config/network/v1/link-tags |
| `set lldp-profiles` | global | `create_lldp_profiles` | POST https://api.strata.paloaltonetworks.com/config/network/v1/lldp-profiles |
| `set logical-routers` | global | `create_logical_routers` | POST https://api.strata.paloaltonetworks.com/config/network/v1/logical-routers |
| `set loopback-interfaces` | global | `create_loopback_interfaces` | POST https://api.strata.paloaltonetworks.com/config/network/v1/loopback-interfaces |
| `set nat-rules` | global | `create_nat_rules` | POST https://api.strata.paloaltonetworks.com/config/network/v1/nat-rules |
| `set npb-profiles` | global | `create_npb_profiles` | POST https://api.strata.paloaltonetworks.com/config/network/v1/network_packet_broker_profiles |
| `set npb-rules` | global | `create_npb_rules` | POST https://api.strata.paloaltonetworks.com/config/network/v1/network_packet_broker_rules |
| `set ospf-auth-profiles` | global | `create_ospf_auth_profiles` | POST https://api.strata.paloaltonetworks.com/config/network/v1/ospf-auth-profiles |
| `set pbf-rules` | global | `create_pbf_rules` | POST https://api.strata.paloaltonetworks.com/config/network/v1/pbf-rules |
| `set qos-policy-rules` | global | `create_qos_policy_rules` | POST https://api.strata.paloaltonetworks.com/config/network/v1/qos-policy-rules |
| `set qos-policy-rules move` | global | `create_qos_policy_rules_move` | POST https://api.strata.paloaltonetworks.com/config/network/v1/qos-policy-rules/{id}:move |
| `set qos-profiles` | global | `create_qos_profiles` | POST https://api.strata.paloaltonetworks.com/config/network/v1/qos-profiles |
| `set route-access-lists` | global | `create_route_access_lists` | POST https://api.strata.paloaltonetworks.com/config/network/v1/route-access-lists |
| `set route-community-lists` | global | `create_route_community_lists` | POST https://api.strata.paloaltonetworks.com/config/network/v1/route-community-lists |
| `set route-path-acls` | global | `create_route_path_acls` | POST https://api.strata.paloaltonetworks.com/config/network/v1/route-path-access-lists |
| `set route-prefix-lists` | global | `create_route_prefix_lists` | POST https://api.strata.paloaltonetworks.com/config/network/v1/route-prefix-lists |
| `set sdwan-error-profiles` | global | `create_sdwan_error_profiles` | POST https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-error-correction-profiles |
| `set sdwan-path-profiles` | global | `create_sdwan_path_profiles` | POST https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-path-quality-profiles |
| `set sdwan-rules` | global | `create_sdwan_rules` | POST https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-rules |
| `set sdwan-saas-profiles` | global | `create_sdwan_saas_profiles` | POST https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-saas-quality-profiles |
| `set sdwan-traffic-profiles` | global | `create_sdwan_traffic_profiles` | POST https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-traffic-distribution-profiles |
| `set system-match-list` | global | `create_system_match_list` | POST https://api.strata.paloaltonetworks.com/config/network/v1/system-match-list |
| `set tunnel-interfaces` | global | `create_tunnel_interfaces` | POST https://api.strata.paloaltonetworks.com/config/network/v1/tunnel-interfaces |
| `set userid-match-list` | global | `create_userid_match_list` | POST https://api.strata.paloaltonetworks.com/config/network/v1/userid-match-list |
| `set vlan-interfaces` | global | `create_vlan_interfaces` | POST https://api.strata.paloaltonetworks.com/config/network/v1/vlan-interfaces |
| `set zone-profiles` | global | `create_zone_profiles` | POST https://api.strata.paloaltonetworks.com/config/network/v1/zone-protection-profiles |
| `set zones` | global | `create_zones` | POST https://api.strata.paloaltonetworks.com/config/network/v1/zones |
| `show aggregate-interfaces` | global | `show_aggregate_interfaces` | GET https://api.strata.paloaltonetworks.com/config/network/v1/aggregate-interfaces |
| `show aggregate-interfaces id` | global | `show_aggregate_interfaces_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/aggregate-interfaces/{id} |
| `show arp` | device | `show_arp` | (live device state — SSH via --remote) |
| `show auto-vpn-clusters` | global | `show_auto_vpn_clusters` | GET https://api.strata.paloaltonetworks.com/config/network/v1/auto-vpn-clusters |
| `show auto-vpn-clusters id` | global | `show_auto_vpn_clusters_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/auto-vpn-clusters/{id} |
| `show auto-vpn-monitor` | global | `show_auto_vpn_monitor` | GET https://api.strata.paloaltonetworks.com/config/network/v1/auto-vpn-monitor |
| `show auto-vpn-settings` | global | `show_auto_vpn_settings` | GET https://api.strata.paloaltonetworks.com/config/network/v1/auto-vpn-settings |
| `show bgp-af-profiles id` | global | `show_bgp_af_profiles_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/bgp-address-family-profiles/{id} |
| `show bgp-auth-profiles` | global | `show_bgp_auth_profiles` | GET https://api.strata.paloaltonetworks.com/config/network/v1/bgp-auth-profiles |
| `show bgp-auth-profiles id` | global | `show_bgp_auth_profiles_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/bgp-auth-profiles/{id} |
| `show bgp-filtering-profiles` | global | `show_bgp_filtering_profiles` | GET https://api.strata.paloaltonetworks.com/config/network/v1/bgp-filtering-profiles |
| `show bgp-filtering-profiles id` | global | `show_bgp_filtering_profiles_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/bgp-filtering-profiles/{id} |
| `show bgp-profile` | folder | `bgp_routing` | GET /config/network/v1/bgp-address-family-profiles |
| `show bgp-redist-profiles` | global | `show_bgp_redist_profiles` | GET https://api.strata.paloaltonetworks.com/config/network/v1/bgp-redistribution-profiles |
| `show bgp-redist-profiles id` | global | `show_bgp_redist_profiles_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/bgp-redistribution-profiles/{id} |
| `show bgp-route-maps` | global | `show_bgp_route_maps` | GET https://api.strata.paloaltonetworks.com/config/network/v1/bgp-route-maps |
| `show bgp-route-maps id` | global | `show_bgp_route_maps_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/bgp-route-maps/{id} |
| `show bgp-routemap-redist` | global | `show_bgp_routemap_redist` | GET https://api.strata.paloaltonetworks.com/config/network/v1/bgp-route-map-redistributions |
| `show bgp-routemap-redist id` | global | `show_bgp_routemap_redist_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/bgp-route-map-redistributions/{id} |
| `show config-match-list` | global | `show_config_match_list` | GET https://api.strata.paloaltonetworks.com/config/network/v1/config-match-list |
| `show config-match-list id` | global | `show_config_match_list_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/config-match-list/{id} |
| `show dhcp-interfaces` | global | `show_dhcp_interfaces` | GET https://api.strata.paloaltonetworks.com/config/network/v1/dhcp-interfaces |
| `show dhcp-interfaces id` | global | `show_dhcp_interfaces_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/dhcp-interfaces/{id} |
| `show dns-proxies id` | global | `show_dns_proxies_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/dns-proxies/{id} |
| `show dns-proxy` | folder | `dns_proxy` | GET /config/network/v1/dns-proxies |
| `show ethernet-interfaces id` | global | `show_ethernet_interfaces_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/ethernet-interfaces/{id} |
| `show gp-match-list` | global | `show_gp_match_list` | GET https://api.strata.paloaltonetworks.com/config/network/v1/globalprotect-match-list |
| `show gp-match-list id` | global | `show_gp_match_list_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/globalprotect-match-list/{id} |
| `show high-availability all` | folder | `show_high_availability` | GET /config/network/v1/ha |
| `show high-availability state` | folder | `show_high_availability` | GET /config/network/v1/ha |
| `show hipmatch-match-list` | global | `show_hipmatch_match_list` | GET https://api.strata.paloaltonetworks.com/config/network/v1/hipmatch-match-list |
| `show hipmatch-match-list id` | global | `show_hipmatch_match_list_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/hipmatch-match-list/{id} |
| `show if-mgmt-profiles` | global | `show_if_mgmt_profiles` | GET https://api.strata.paloaltonetworks.com/config/network/v1/interface-management-profiles |
| `show if-mgmt-profiles id` | global | `show_if_mgmt_profiles_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/interface-management-profiles/{id} |
| `show ike-crypto-profiles` | global | `show_ike_crypto_profiles` | GET https://api.strata.paloaltonetworks.com/config/network/v1/ike-crypto-profiles |
| `show ike-crypto-profiles id` | global | `show_ike_crypto_profiles_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/ike-crypto-profiles/{id} |
| `show ike-gateway` | folder | `ipsec_vpn` | GET /config/network/v1/ike-gateways |
| `show ike-gateways id` | global | `show_ike_gateways_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/ike-gateways/{id} |
| `show interface` | folder | `show_interface` | GET /config/network/v1/ethernet-interfaces |
| `show interface all` | folder | `show_interface` | GET /config/network/v1/ethernet-interfaces |
| `show ipsec-crypto-profiles` | global | `show_ipsec_crypto_profiles` | GET https://api.strata.paloaltonetworks.com/config/network/v1/ipsec-crypto-profiles |
| `show ipsec-crypto-profiles id` | global | `show_ipsec_crypto_profiles_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/ipsec-crypto-profiles/{id} |
| `show ipsec-tunnel` | folder | `ipsec_vpn` | GET /config/network/v1/ipsec-tunnels |
| `show ipsec-tunnels id` | global | `show_ipsec_tunnels_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/ipsec-tunnels/{id} |
| `show iptag-match-list` | global | `show_iptag_match_list` | GET https://api.strata.paloaltonetworks.com/config/network/v1/iptag-match-list |
| `show iptag-match-list id` | global | `show_iptag_match_list_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/iptag-match-list/{id} |
| `show layer2-subinterfaces` | global | `show_layer2_subinterfaces` | GET https://api.strata.paloaltonetworks.com/config/network/v1/layer2-subinterfaces |
| `show layer2-subinterfaces id` | global | `show_layer2_subinterfaces_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/layer2-subinterfaces/{id} |
| `show layer3-subinterfaces` | global | `show_layer3_subinterfaces` | GET https://api.strata.paloaltonetworks.com/config/network/v1/layer3-subinterfaces |
| `show layer3-subinterfaces id` | global | `show_layer3_subinterfaces_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/layer3-subinterfaces/{id} |
| `show link-tags` | global | `show_link_tags` | GET https://api.strata.paloaltonetworks.com/config/network/v1/link-tags |
| `show link-tags id` | global | `show_link_tags_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/link-tags/{id} |
| `show lldp-profiles` | global | `show_lldp_profiles` | GET https://api.strata.paloaltonetworks.com/config/network/v1/lldp-profiles |
| `show lldp-profiles id` | global | `show_lldp_profiles_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/lldp-profiles/{id} |
| `show logical-routers` | global | `show_logical_routers` | GET https://api.strata.paloaltonetworks.com/config/network/v1/logical-routers |
| `show logical-routers id` | global | `show_logical_routers_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/logical-routers/{id} |
| `show loopback-interfaces` | global | `show_loopback_interfaces` | GET https://api.strata.paloaltonetworks.com/config/network/v1/loopback-interfaces |
| `show loopback-interfaces id` | global | `show_loopback_interfaces_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/loopback-interfaces/{id} |
| `show nat-rules` | folder | `nat_rules` | GET /config/network/v1/nat-rules |
| `show nat-rules id` | global | `show_nat_rules_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/nat-rules/{id} |
| `show npb-profiles` | global | `show_npb_profiles` | GET https://api.strata.paloaltonetworks.com/config/network/v1/network_packet_broker_profiles |
| `show npb-profiles id` | global | `show_npb_profiles_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/network_packet_broker_profiles/{id} |
| `show npb-rules` | global | `show_npb_rules` | GET https://api.strata.paloaltonetworks.com/config/network/v1/network_packet_broker_rules |
| `show npb-rules id` | global | `show_npb_rules_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/network_packet_broker_rules/{id} |
| `show ospf-auth-profiles` | global | `show_ospf_auth_profiles` | GET https://api.strata.paloaltonetworks.com/config/network/v1/ospf-auth-profiles |
| `show ospf-auth-profiles id` | global | `show_ospf_auth_profiles_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/ospf-auth-profiles/{id} |
| `show pbf-rules` | folder | `pbf_rules` | GET /config/network/v1/pbf-rules |
| `show pbf-rules id` | global | `show_pbf_rules_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/pbf-rules/{id} |
| `show qos-policy-rules` | global | `show_qos_policy_rules` | GET https://api.strata.paloaltonetworks.com/config/network/v1/qos-policy-rules |
| `show qos-policy-rules id` | global | `show_qos_policy_rules_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/qos-policy-rules/{id} |
| `show qos-profile` | folder | `qos` | GET /config/network/v1/qos-profiles |
| `show qos-profiles id` | global | `show_qos_profiles_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/qos-profiles/{id} |
| `show rn-license-info` | global | `show_rn_license_info` | GET https://api.strata.paloaltonetworks.com/config/network/v1/remote-networks-license-info |
| `show route-access-lists` | global | `show_route_access_lists` | GET https://api.strata.paloaltonetworks.com/config/network/v1/route-access-lists |
| `show route-access-lists id` | global | `show_route_access_lists_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/route-access-lists/{id} |
| `show route-community-lists` | global | `show_route_community_lists` | GET https://api.strata.paloaltonetworks.com/config/network/v1/route-community-lists |
| `show route-community-lists id` | global | `show_route_community_lists_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/route-community-lists/{id} |
| `show route-path-acls` | global | `show_route_path_acls` | GET https://api.strata.paloaltonetworks.com/config/network/v1/route-path-access-lists |
| `show route-path-acls id` | global | `show_route_path_acls_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/route-path-access-lists/{id} |
| `show route-prefix-lists` | global | `show_route_prefix_lists` | GET https://api.strata.paloaltonetworks.com/config/network/v1/route-prefix-lists |
| `show route-prefix-lists id` | global | `show_route_prefix_lists_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/route-prefix-lists/{id} |
| `show routing bgp` | device | `bgp_routing` | (live device state — SSH via --remote) |
| `show routing route` | folder | `show_routing` | GET /config/network/v1/routing/static-routes |
| `show routing summary` | folder | `show_routing` | GET /config/network/v1/virtual-routers |
| `show sdwan-error-profiles` | global | `show_sdwan_error_profiles` | GET https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-error-correction-profiles |
| `show sdwan-error-profiles id` | global | `show_sdwan_error_profiles_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-error-correction-profiles/{id} |
| `show sdwan-path-profiles` | global | `show_sdwan_path_profiles` | GET https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-path-quality-profiles |
| `show sdwan-path-profiles id` | global | `show_sdwan_path_profiles_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-path-quality-profiles/{id} |
| `show sdwan-rules` | folder | `sdwan` | GET /config/network/v1/sdwan-rules |
| `show sdwan-rules id` | global | `show_sdwan_rules_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-rules/{id} |
| `show sdwan-saas-profiles` | global | `show_sdwan_saas_profiles` | GET https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-saas-quality-profiles |
| `show sdwan-saas-profiles id` | global | `show_sdwan_saas_profiles_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-saas-quality-profiles/{id} |
| `show sdwan-traffic-profiles` | global | `show_sdwan_traffic_profiles` | GET https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-traffic-distribution-profiles |
| `show sdwan-traffic-profiles id` | global | `show_sdwan_traffic_profiles_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-traffic-distribution-profiles/{id} |
| `show session all` | device | `show_sessions` | (live device state — SSH via --remote) |
| `show system-match-list` | global | `show_system_match_list` | GET https://api.strata.paloaltonetworks.com/config/network/v1/system-match-list |
| `show system-match-list id` | global | `show_system_match_list_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/system-match-list/{id} |
| `show tunnel-interfaces` | global | `show_tunnel_interfaces` | GET https://api.strata.paloaltonetworks.com/config/network/v1/tunnel-interfaces |
| `show tunnel-interfaces id` | global | `show_tunnel_interfaces_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/tunnel-interfaces/{id} |
| `show userid-match-list` | global | `show_userid_match_list` | GET https://api.strata.paloaltonetworks.com/config/network/v1/userid-match-list |
| `show userid-match-list id` | global | `show_userid_match_list_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/userid-match-list/{id} |
| `show vlan-interfaces` | global | `show_vlan_interfaces` | GET https://api.strata.paloaltonetworks.com/config/network/v1/vlan-interfaces |
| `show vlan-interfaces id` | global | `show_vlan_interfaces_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/vlan-interfaces/{id} |
| `show vpn ike-sa` | device | `ipsec_vpn` | (live device state — SSH via --remote) |
| `show vpn tunnel` | device | `ipsec_vpn` | (live device state — SSH via --remote) |
| `show zone` | folder | `show_zone` | GET /config/network/v1/zones |
| `show zone-profiles` | global | `show_zone_profiles` | GET https://api.strata.paloaltonetworks.com/config/network/v1/zone-protection-profiles |
| `show zone-profiles id` | global | `show_zone_profiles_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/zone-protection-profiles/{id} |
| `show zones id` | global | `show_zones_id` | GET https://api.strata.paloaltonetworks.com/config/network/v1/zones/{id} |
| `test nat-policy-match` | device | `test_nat` | (live device state — SSH via --remote) |
| `test url` | device | `test_url` | (live device state — SSH via --remote) |
| `traceroute host` | device | `traceroute` | (live device state — SSH via --remote) |
| `update aggregate-interfaces` | global | `update_aggregate_interfaces` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/aggregate-interfaces/{id} |
| `update auto-vpn-clusters` | global | `update_auto_vpn_clusters` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/auto-vpn-clusters/{id} |
| `update auto-vpn-settings` | global | `update_auto_vpn_settings` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/auto-vpn-settings |
| `update bgp-af-profiles` | global | `update_bgp_af_profiles` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/bgp-address-family-profiles/{id} |
| `update bgp-auth-profiles` | global | `update_bgp_auth_profiles` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/bgp-auth-profiles/{id} |
| `update bgp-filtering-profiles` | global | `update_bgp_filtering_profiles` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/bgp-filtering-profiles/{id} |
| `update bgp-redist-profiles` | global | `update_bgp_redist_profiles` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/bgp-redistribution-profiles/{id} |
| `update bgp-route-maps` | global | `update_bgp_route_maps` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/bgp-route-maps/{id} |
| `update bgp-routemap-redist` | global | `update_bgp_routemap_redist` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/bgp-route-map-redistributions/{id} |
| `update config-match-list` | global | `update_config_match_list` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/config-match-list/{id} |
| `update dhcp-interfaces` | global | `update_dhcp_interfaces` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/dhcp-interfaces/{id} |
| `update dns-proxies` | global | `update_dns_proxies` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/dns-proxies/{id} |
| `update ethernet-interfaces` | global | `update_ethernet_interfaces` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/ethernet-interfaces/{id} |
| `update gp-match-list` | global | `update_gp_match_list` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/globalprotect-match-list/{id} |
| `update hipmatch-match-list` | global | `update_hipmatch_match_list` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/hipmatch-match-list/{id} |
| `update if-mgmt-profiles` | global | `update_if_mgmt_profiles` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/interface-management-profiles/{id} |
| `update ike-crypto-profiles` | global | `update_ike_crypto_profiles` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/ike-crypto-profiles/{id} |
| `update ike-gateways` | global | `update_ike_gateways` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/ike-gateways/{id} |
| `update ipsec-crypto-profiles` | global | `update_ipsec_crypto_profiles` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/ipsec-crypto-profiles/{id} |
| `update ipsec-tunnels` | global | `update_ipsec_tunnels` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/ipsec-tunnels/{id} |
| `update iptag-match-list` | global | `update_iptag_match_list` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/iptag-match-list/{id} |
| `update layer2-subinterfaces` | global | `update_layer2_subinterfaces` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/layer2-subinterfaces/{id} |
| `update layer3-subinterfaces` | global | `update_layer3_subinterfaces` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/layer3-subinterfaces/{id} |
| `update link-tags` | global | `update_link_tags` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/link-tags/{id} |
| `update lldp-profiles` | global | `update_lldp_profiles` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/lldp-profiles/{id} |
| `update logical-routers` | global | `update_logical_routers` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/logical-routers/{id} |
| `update loopback-interfaces` | global | `update_loopback_interfaces` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/loopback-interfaces/{id} |
| `update nat-rules` | global | `update_nat_rules` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/nat-rules/{id} |
| `update npb-profiles` | global | `update_npb_profiles` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/network_packet_broker_profiles/{id} |
| `update npb-rules` | global | `update_npb_rules` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/network_packet_broker_rules/{id} |
| `update ospf-auth-profiles` | global | `update_ospf_auth_profiles` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/ospf-auth-profiles/{id} |
| `update pbf-rules` | global | `update_pbf_rules` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/pbf-rules/{id} |
| `update qos-policy-rules` | global | `update_qos_policy_rules` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/qos-policy-rules/{id} |
| `update qos-profiles` | global | `update_qos_profiles` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/qos-profiles/{id} |
| `update route-access-lists` | global | `update_route_access_lists` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/route-access-lists/{id} |
| `update route-community-lists` | global | `update_route_community_lists` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/route-community-lists/{id} |
| `update route-path-acls` | global | `update_route_path_acls` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/route-path-access-lists/{id} |
| `update route-prefix-lists` | global | `update_route_prefix_lists` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/route-prefix-lists/{id} |
| `update sdwan-error-profiles` | global | `update_sdwan_error_profiles` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-error-correction-profiles/{id} |
| `update sdwan-path-profiles` | global | `update_sdwan_path_profiles` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-path-quality-profiles/{id} |
| `update sdwan-rules` | global | `update_sdwan_rules` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-rules/{id} |
| `update sdwan-saas-profiles` | global | `update_sdwan_saas_profiles` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-saas-quality-profiles/{id} |
| `update sdwan-traffic-profiles` | global | `update_sdwan_traffic_profiles` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-traffic-distribution-profiles/{id} |
| `update system-match-list` | global | `update_system_match_list` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/system-match-list/{id} |
| `update tunnel-interfaces` | global | `update_tunnel_interfaces` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/tunnel-interfaces/{id} |
| `update userid-match-list` | global | `update_userid_match_list` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/userid-match-list/{id} |
| `update vlan-interfaces` | global | `update_vlan_interfaces` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/vlan-interfaces/{id} |
| `update zone-profiles` | global | `update_zone_profiles` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/zone-protection-profiles/{id} |
| `update zones` | global | `update_zones` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/zones/{id} |

## Ngts

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `delete ngts cert-requests approval` | global | `delete_ngts_cert_requests_approval` | DELETE https://api.strata.paloaltonetworks.com/v1/certificaterequests/approvalrules/{id} |
| `delete ngts cert-templates` | global | `delete_ngts_cert_templates` | DELETE https://api.strata.paloaltonetworks.com/v1/certificateissuingtemplates/{id} |
| `delete ngts certs revokes approval` | global | `delete_ngts_certs_revokes_approval` | DELETE https://api.strata.paloaltonetworks.com/v1/certificates/revocations/approvalrules/{id} |
| `delete ngts credential-configs` | global | `delete_ngts_credential_configs` | DELETE https://api.strata.paloaltonetworks.com/v1/credentialmanagerconfigurations/{id} |
| `delete ngts credentials` | global | `delete_ngts_credentials` | DELETE https://api.strata.paloaltonetworks.com/v1/credentials |
| `delete ngts dist-issuers configurations` | global | `delete_ngts_dist_issuers_configurations` | DELETE https://api.strata.paloaltonetworks.com/v1/distributedissuers/configurations/{id} |
| `delete ngts dist-issuers policies` | global | `delete_ngts_dist_issuers_policies` | DELETE https://api.strata.paloaltonetworks.com/v1/distributedissuers/policies/{id} |
| `delete ngts dist-issuers subcaproviders` | global | `delete_ngts_dist_issuers_subcaproviders` | DELETE https://api.strata.paloaltonetworks.com/v1/distributedissuers/subcaproviders/{id} |
| `delete ngts edgeworkers` | global | `delete_ngts_edgeworkers` | DELETE https://api.strata.paloaltonetworks.com/v1/edgeworkers/{id} |
| `delete ngts integrationservices` | global | `delete_ngts_integrationservices` | DELETE https://api.strata.paloaltonetworks.com/v1/integrationservices/{id} |
| `delete ngts machineidentities` | global | `delete_ngts_machineidentities` | DELETE https://api.strata.paloaltonetworks.com/v1/machineidentities/{id} |
| `delete ngts machines` | global | `delete_ngts_machines` | DELETE https://api.strata.paloaltonetworks.com/v1/machines/{id} |
| `delete ngts plugins` | global | `delete_ngts_plugins` | DELETE https://api.strata.paloaltonetworks.com/v1/plugins/{id} |
| `delete ngts plugins disablements` | global | `delete_ngts_plugins_disablements` | DELETE https://api.strata.paloaltonetworks.com/v1/plugins/{id}/disablements |
| `delete ngts serviceaccounts` | global | `delete_ngts_serviceaccounts` | DELETE https://api.strata.paloaltonetworks.com/v1/serviceaccounts/{id} |
| `delete ngts tags` | global | `delete_ngts_tags` | DELETE https://api.strata.paloaltonetworks.com/v1/tags/{name} |
| `delete ngts tags values` | global | `delete_ngts_tags_values` | DELETE https://api.strata.paloaltonetworks.com/v1/tags/{name}/values/{value} |
| `delete ngts tlsprotect credentials` | global | `delete_ngts_credentials` | DELETE https://api.strata.paloaltonetworks.com/v1/credentials/{id} |
| `set ngts activitylogsearch` | global | `create_ngts_activitylogsearch` | POST https://api.strata.paloaltonetworks.com/v1/activitylogsearch |
| `set ngts activitylogsearch export` | global | `create_ngts_activitylogsearch_export` | POST https://api.strata.paloaltonetworks.com/v1/activitylogsearch/export |
| `set ngts autorenewal trigger` | global | `create_ngts_autorenewal_trigger` | POST https://api.strata.paloaltonetworks.com/v1/autorenewal/trigger |
| `set ngts cert-instance-search` | global | `create_ngts_cert_instance_search` | POST https://api.strata.paloaltonetworks.com/outagedetection/v1/certificateinstancesearch |
| `set ngts cert-instances validation` | global | `create_ngts_cert_instances_validation` | POST https://api.strata.paloaltonetworks.com/outagedetection/v1/certificateinstances/validation |
| `set ngts cert-request-search` | global | `create_ngts_cert_request_search` | POST https://api.strata.paloaltonetworks.com/outagedetection/v1/certificaterequestssearch |
| `set ngts cert-requests` | global | `create_ngts_cert_requests` | POST https://api.strata.paloaltonetworks.com/outagedetection/v1/certificaterequests |
| `set ngts cert-requests approval` | global | `create_ngts_cert_requests_approval` | POST https://api.strata.paloaltonetworks.com/v1/certificaterequests/{id}/approval/{decision} |
| `set ngts cert-requests approval bulk` | global | `create_ngts_cert_requests_approval_bulk` | POST https://api.strata.paloaltonetworks.com/v1/certificaterequests/approval/bulk/{decision} |
| `set ngts cert-requests resubmission` | global | `create_ngts_cert_requests_resubmission` | POST https://api.strata.paloaltonetworks.com/outagedetection/v1/certificaterequests/{id}/resubmission |
| `set ngts cert-requests validation` | global | `create_ngts_cert_requests_validation` | POST https://api.strata.paloaltonetworks.com/outagedetection/v1/certificaterequests/validation |
| `set ngts cert-templates` | global | `create_ngts_cert_templates` | POST https://api.strata.paloaltonetworks.com/v1/certificateissuingtemplates |
| `set ngts cert-templates domains-sync` | global | `create_ngts_cert_templates_domains_sync` | POST https://api.strata.paloaltonetworks.com/v1/certificateissuingtemplates/domainssynchronization |
| `set ngts certificatesearch` | global | `create_ngts_certificatesearch` | POST https://api.strata.paloaltonetworks.com/outagedetection/v1/certificatesearch |
| `set ngts certs` | global | `create_ngts_certs` | POST https://api.strata.paloaltonetworks.com/outagedetection/v1/certificates |
| `set ngts certs deletion` | global | `create_ngts_certs_deletion` | POST https://api.strata.paloaltonetworks.com/outagedetection/v1/certificates/deletion |
| `set ngts certs imports` | global | `create_ngts_certs_imports` | POST https://api.strata.paloaltonetworks.com/v1/certificates/imports |
| `set ngts certs recovery` | global | `create_ngts_certs_recovery` | POST https://api.strata.paloaltonetworks.com/outagedetection/v1/certificates/recovery |
| `set ngts certs retirement` | global | `create_ngts_certs_retirement` | POST https://api.strata.paloaltonetworks.com/outagedetection/v1/certificates/retirement |
| `set ngts certs revokes approval` | global | `create_ngts_certs_revokes_approval` | POST https://api.strata.paloaltonetworks.com/v1/certificates/revocations/approvalrules |
| `set ngts certs validation` | global | `create_ngts_certs_validation` | POST https://api.strata.paloaltonetworks.com/outagedetection/v1/certificates/validation |
| `set ngts credential-configs` | global | `create_ngts_credential_configs` | POST https://api.strata.paloaltonetworks.com/v1/credentialmanagerconfigurations |
| `set ngts credential-configs test` | global | `create_ngts_credential_configs_test` | POST https://api.strata.paloaltonetworks.com/v1/credentialmanagerconfigurations/test |
| `set ngts credentials` | global | `create_ngts_credentials` | POST https://api.strata.paloaltonetworks.com/v1/credentials |
| `set ngts credentials test` | global | `create_ngts_credentials_test` | POST https://api.strata.paloaltonetworks.com/v1/credentials/test |
| `set ngts dist-issuers configurations` | global | `create_ngts_dist_issuers_configurations` | POST https://api.strata.paloaltonetworks.com/v1/distributedissuers/configurations |
| `set ngts dist-issuers policies` | global | `create_ngts_dist_issuers_policies` | POST https://api.strata.paloaltonetworks.com/v1/distributedissuers/policies |
| `set ngts dist-issuers subcaproviders` | global | `create_ngts_dist_issuers_subcaproviders` | POST https://api.strata.paloaltonetworks.com/v1/distributedissuers/subcaproviders |
| `set ngts edgeinstances update` | global | `create_ngts_edgeinstances_update` | POST https://api.strata.paloaltonetworks.com/v1/edgeinstances/{id}/update |
| `set ngts edgeworkers` | global | `create_ngts_edgeworkers` | POST https://api.strata.paloaltonetworks.com/v1/edgeworkers |
| `set ngts edgeworkers pair` | global | `create_ngts_edgeworkers_pair` | POST https://api.strata.paloaltonetworks.com/v1/edgeworkers/{id}/pair |
| `set ngts exp-reports trigger` | global | `create_ngts_exp_reports_trigger` | POST https://api.strata.paloaltonetworks.com/v1/expirationreports/trigger |
| `set ngts integrationservices` | global | `create_ngts_integrationservices` | POST https://api.strata.paloaltonetworks.com/v1/integrationservices |
| `set ngts machineidentities` | global | `create_ngts_machineidentities` | POST https://api.strata.paloaltonetworks.com/v1/machineidentities |
| `set ngts machineidentities workflows` | global | `create_ngts_machineidentities_workflows` | POST https://api.strata.paloaltonetworks.com/v1/machineidentities/{id}/workflows |
| `set ngts machineidentitysearch` | global | `create_ngts_machineidentitysearch` | POST https://api.strata.paloaltonetworks.com/v1/machineidentitysearch |
| `set ngts machines` | global | `create_ngts_machines` | POST https://api.strata.paloaltonetworks.com/v1/machines |
| `set ngts machines batchprovisionings abort` | global | `create_ngts_machines_batchprovisionings_abort` | POST https://api.strata.paloaltonetworks.com/v1/machines/{id}/batchprovisionings/abort |
| `set ngts machines discovery abort` | global | `create_ngts_machines_discovery_abort` | POST https://api.strata.paloaltonetworks.com/v1/machines/{id}/discovery/abort |
| `set ngts machines workflows` | global | `create_ngts_machines_workflows` | POST https://api.strata.paloaltonetworks.com/v1/machines/{id}/workflows |
| `set ngts machinesearch` | global | `create_ngts_machinesearch` | POST https://api.strata.paloaltonetworks.com/v1/machinesearch |
| `set ngts pairingcodes satellite` | global | `create_ngts_pairingcodes_satellite` | POST https://api.strata.paloaltonetworks.com/v1/pairingcodes/satellite |
| `set ngts plugins` | global | `create_ngts_plugins` | POST https://api.strata.paloaltonetworks.com/v1/plugins |
| `set ngts plugins disablements` | global | `create_ngts_plugins_disablements` | POST https://api.strata.paloaltonetworks.com/v1/plugins/{id}/disablements |
| `set ngts recoverycodes satellite` | global | `create_ngts_recoverycodes_satellite` | POST https://api.strata.paloaltonetworks.com/v1/recoverycodes/satellite |
| `set ngts serviceaccounts` | global | `create_ngts_serviceaccounts` | POST https://api.strata.paloaltonetworks.com/v1/serviceaccounts |
| `set ngts tags` | global | `create_ngts_tags` | POST https://api.strata.paloaltonetworks.com/v1/tags |
| `set ngts tags creation` | global | `create_ngts_tags_creation` | POST https://api.strata.paloaltonetworks.com/v1/tags/creation |
| `set ngts tags deletion` | global | `create_ngts_tags_deletion` | POST https://api.strata.paloaltonetworks.com/v1/tags/deletion |
| `set ngts tags values` | global | `create_ngts_tags_values` | POST https://api.strata.paloaltonetworks.com/v1/tags/{name}/values |
| `set ngts tagsassignment aggregates` | global | `create_ngts_tagsassignment_aggregates` | POST https://api.strata.paloaltonetworks.com/v1/tagsassignment/aggregates |
| `set ngts tlsprotect cert-requests approval` | global | `create_ngts_cert_requests_approval` | POST https://api.strata.paloaltonetworks.com/v1/certificaterequests/approvalrules |
| `set ngts tlsprotect credential-configs test` | global | `create_ngts_credential_configs_test` | POST https://api.strata.paloaltonetworks.com/v1/credentialmanagerconfigurations/{id}/test |
| `show ngts activitytypes` | global | `show_ngts_activitytypes` | GET https://api.strata.paloaltonetworks.com/v1/activitytypes |
| `show ngts autorenewal status` | global | `show_ngts_autorenewal_status` | GET https://api.strata.paloaltonetworks.com/v1/autorenewal/status |
| `show ngts autorenewal tenant-config` | global | `show_ngts_autorenewal_tenant_config` | GET https://api.strata.paloaltonetworks.com/v1/autorenewal/tenantconfiguration |
| `show ngts cert-instances` | global | `show_ngts_cert_instances` | GET https://api.strata.paloaltonetworks.com/outagedetection/v1/certificateinstances |
| `show ngts cert-instances id` | global | `show_ngts_cert_instances_id` | GET https://api.strata.paloaltonetworks.com/outagedetection/v1/certificateinstances/{id} |
| `show ngts cert-requests` | global | `show_ngts_cert_requests` | GET https://api.strata.paloaltonetworks.com/outagedetection/v1/certificaterequests |
| `show ngts cert-requests approval` | global | `show_ngts_cert_requests_approval` | GET https://api.strata.paloaltonetworks.com/v1/certificaterequests/approvalrules |
| `show ngts cert-requests approval id` | global | `show_ngts_cert_requests_approval_id` | GET https://api.strata.paloaltonetworks.com/v1/certificaterequests/approvalrules/{id} |
| `show ngts cert-requests approvalrequests id` | global | `show_ngts_cert_requests_approvalrequests_id` | GET https://api.strata.paloaltonetworks.com/v1/certificaterequests/approvalrequests/{entityId} |
| `show ngts cert-requests id` | global | `show_ngts_cert_requests_id` | GET https://api.strata.paloaltonetworks.com/outagedetection/v1/certificaterequests/{id} |
| `show ngts cert-templates` | global | `show_ngts_cert_templates` | GET https://api.strata.paloaltonetworks.com/v1/certificateissuingtemplates |
| `show ngts cert-templates id` | global | `show_ngts_cert_templates_id` | GET https://api.strata.paloaltonetworks.com/v1/certificateissuingtemplates/{id} |
| `show ngts certs` | global | `show_ngts_certs` | GET https://api.strata.paloaltonetworks.com/outagedetection/v1/certificates |
| `show ngts certs contents id` | global | `show_ngts_certs_contents_id` | GET https://api.strata.paloaltonetworks.com/outagedetection/v1/certificates/{id}/contents |
| `show ngts certs id` | global | `show_ngts_certs_id` | GET https://api.strata.paloaltonetworks.com/outagedetection/v1/certificates/{id} |
| `show ngts certs imports id` | global | `show_ngts_certs_imports_id` | GET https://api.strata.paloaltonetworks.com/v1/certificates/imports/{id} |
| `show ngts certs revokes approval` | global | `show_ngts_certs_revokes_approval` | GET https://api.strata.paloaltonetworks.com/v1/certificates/revocations/approvalrules |
| `show ngts certs revokes approval id` | global | `show_ngts_certs_revokes_approval_id` | GET https://api.strata.paloaltonetworks.com/v1/certificates/revocations/approvalrules/{id} |
| `show ngts credential-configs` | global | `show_ngts_credential_configs` | GET https://api.strata.paloaltonetworks.com/v1/credentialmanagerconfigurations |
| `show ngts credential-configs id` | global | `show_ngts_credential_configs_id` | GET https://api.strata.paloaltonetworks.com/v1/credentialmanagerconfigurations/{id} |
| `show ngts credentials` | global | `show_ngts_credentials` | GET https://api.strata.paloaltonetworks.com/v1/credentials |
| `show ngts credentials id` | global | `show_ngts_credentials_id` | GET https://api.strata.paloaltonetworks.com/v1/credentials/{id} |
| `show ngts dist-issuers configurations` | global | `show_ngts_dist_issuers_configurations` | GET https://api.strata.paloaltonetworks.com/v1/distributedissuers/configurations |
| `show ngts dist-issuers configurations id` | global | `show_ngts_dist_issuers_configurations_id` | GET https://api.strata.paloaltonetworks.com/v1/distributedissuers/configurations/{id} |
| `show ngts dist-issuers intermediate-certs` | global | `show_ngts_dist_issuers_intermediate_certs` | GET https://api.strata.paloaltonetworks.com/v1/distributedissuers/intermediatecertificates |
| `show ngts dist-issuers policies` | global | `show_ngts_dist_issuers_policies` | GET https://api.strata.paloaltonetworks.com/v1/distributedissuers/policies |
| `show ngts dist-issuers policies id` | global | `show_ngts_dist_issuers_policies_id` | GET https://api.strata.paloaltonetworks.com/v1/distributedissuers/policies/{id} |
| `show ngts dist-issuers subcaproviders` | global | `show_ngts_dist_issuers_subcaproviders` | GET https://api.strata.paloaltonetworks.com/v1/distributedissuers/subcaproviders |
| `show ngts dist-issuers subcaproviders id` | global | `show_ngts_dist_issuers_subcaproviders_id` | GET https://api.strata.paloaltonetworks.com/v1/distributedissuers/subcaproviders/{id} |
| `show ngts edgeencryptionkeys` | global | `show_ngts_edgeencryptionkeys` | GET https://api.strata.paloaltonetworks.com/v1/edgeencryptionkeys |
| `show ngts edgeencryptionkeys id` | global | `show_ngts_edgeencryptionkeys_id` | GET https://api.strata.paloaltonetworks.com/v1/edgeencryptionkeys/{id} |
| `show ngts edgeinstances` | global | `show_ngts_edgeinstances` | GET https://api.strata.paloaltonetworks.com/v1/edgeinstances |
| `show ngts edgeinstances id` | global | `show_ngts_edgeinstances_id` | GET https://api.strata.paloaltonetworks.com/v1/edgeinstances/{id} |
| `show ngts edgeworkers` | global | `show_ngts_edgeworkers` | GET https://api.strata.paloaltonetworks.com/v1/edgeworkers |
| `show ngts exp-notifications tenant-config` | global | `show_ngts_exp_notifications_tenant_config` | GET https://api.strata.paloaltonetworks.com/v1/expirationnotifications/tenantconfiguration |
| `show ngts exp-reports tenant-config` | global | `show_ngts_exp_reports_tenant_config` | GET https://api.strata.paloaltonetworks.com/v1/expirationreports/tenantconfiguration |
| `show ngts integrationservices` | global | `show_ngts_integrationservices` | GET https://api.strata.paloaltonetworks.com/v1/integrationservices |
| `show ngts integrationservices id` | global | `show_ngts_integrationservices_id` | GET https://api.strata.paloaltonetworks.com/v1/integrationservices/{id} |
| `show ngts inventory-monitoring id` | global | `show_ngts_inventory_monitoring_id` | GET https://api.strata.paloaltonetworks.com/outagedetection/v1/inventorymonitoringconfig/{type} |
| `show ngts machineidentities` | global | `show_ngts_machineidentities` | GET https://api.strata.paloaltonetworks.com/v1/machineidentities |
| `show ngts machineidentities id` | global | `show_ngts_machineidentities_id` | GET https://api.strata.paloaltonetworks.com/v1/machineidentities/{id} |
| `show ngts machines` | global | `show_ngts_machines` | GET https://api.strata.paloaltonetworks.com/v1/machines |
| `show ngts machines discovery id` | global | `show_ngts_machines_discovery_id` | GET https://api.strata.paloaltonetworks.com/v1/machines/{id}/discovery |
| `show ngts machines id` | global | `show_ngts_machines_id` | GET https://api.strata.paloaltonetworks.com/v1/machines/{id} |
| `show ngts machinetypes` | global | `show_ngts_machinetypes` | GET https://api.strata.paloaltonetworks.com/v1/machinetypes |
| `show ngts plugins` | global | `show_ngts_plugins` | GET https://api.strata.paloaltonetworks.com/v1/plugins |
| `show ngts plugins disablements` | global | `show_ngts_plugins_disablements` | GET https://api.strata.paloaltonetworks.com/v1/plugins/disablements |
| `show ngts plugins id` | global | `show_ngts_plugins_id` | GET https://api.strata.paloaltonetworks.com/v1/plugins/{id} |
| `show ngts serviceaccounts` | global | `show_ngts_serviceaccounts` | GET https://api.strata.paloaltonetworks.com/v1/serviceaccounts |
| `show ngts serviceaccounts id` | global | `show_ngts_serviceaccounts_id` | GET https://api.strata.paloaltonetworks.com/v1/serviceaccounts/{id} |
| `show ngts serviceaccounts scopes` | global | `show_ngts_serviceaccounts_scopes` | GET https://api.strata.paloaltonetworks.com/v1/serviceaccounts/scopes |
| `show ngts tags` | global | `show_ngts_tags` | GET https://api.strata.paloaltonetworks.com/v1/tags |
| `show ngts tags id` | global | `show_ngts_tags_id` | GET https://api.strata.paloaltonetworks.com/v1/tags/{name} |
| `show ngts tags values` | global | `show_ngts_tags_values` | GET https://api.strata.paloaltonetworks.com/v1/tags/values |
| `show ngts tags values id` | global | `show_ngts_tags_values_id` | GET https://api.strata.paloaltonetworks.com/v1/tags/{name}/values |
| `show ngts updatesconfig` | global | `show_ngts_updatesconfig` | GET https://api.strata.paloaltonetworks.com/v1/updatesconfig |
| `update ngts autorenewal tenant-config` | global | `update_ngts_autorenewal_tenant_config` | PUT https://api.strata.paloaltonetworks.com/v1/autorenewal/tenantconfiguration |
| `update ngts cert-requests approval` | global | `update_ngts_cert_requests_approval` | PUT https://api.strata.paloaltonetworks.com/v1/certificaterequests/approvalrules/{id} |
| `update ngts cert-templates` | global | `update_ngts_cert_templates` | PUT https://api.strata.paloaltonetworks.com/v1/certificateissuingtemplates/{id} |
| `update ngts certs revokes approval` | global | `update_ngts_certs_revokes_approval` | PUT https://api.strata.paloaltonetworks.com/v1/certificates/revocations/approvalrules/{id} |
| `update ngts credential-configs` | global | `update_ngts_credential_configs` | PUT https://api.strata.paloaltonetworks.com/v1/credentialmanagerconfigurations |
| `update ngts credentials` | global | `update_ngts_credentials` | PUT https://api.strata.paloaltonetworks.com/v1/credentials |
| `update ngts dist-issuers configurations` | global | `update_ngts_dist_issuers_configurations` | PATCH https://api.strata.paloaltonetworks.com/v1/distributedissuers/configurations/{id} |
| `update ngts dist-issuers policies` | global | `update_ngts_dist_issuers_policies` | PATCH https://api.strata.paloaltonetworks.com/v1/distributedissuers/policies/{id} |
| `update ngts dist-issuers subcaproviders` | global | `update_ngts_dist_issuers_subcaproviders` | PATCH https://api.strata.paloaltonetworks.com/v1/distributedissuers/subcaproviders/{id} |
| `update ngts edgeinstances` | global | `update_ngts_edgeinstances` | PUT https://api.strata.paloaltonetworks.com/v1/edgeinstances/{id} |
| `update ngts exp-notifications tenant-config` | global | `update_ngts_exp_notifications_tenant_config` | PUT https://api.strata.paloaltonetworks.com/v1/expirationnotifications/tenantconfiguration |
| `update ngts exp-reports tenant-config` | global | `update_ngts_exp_reports_tenant_config` | PUT https://api.strata.paloaltonetworks.com/v1/expirationreports/tenantconfiguration |
| `update ngts integrationservices` | global | `update_ngts_integrationservices` | PATCH https://api.strata.paloaltonetworks.com/v1/integrationservices/{id} |
| `update ngts inventory-monitoring` | global | `update_ngts_inventory_monitoring` | PUT https://api.strata.paloaltonetworks.com/outagedetection/v1/inventorymonitoringconfig/{type} |
| `update ngts inventory-monitoring scheduler` | global | `update_ngts_inventory_monitoring_scheduler` | PUT https://api.strata.paloaltonetworks.com/outagedetection/v1/inventorymonitoringconfig/{type}/scheduler |
| `update ngts machineidentities` | global | `update_ngts_machineidentities` | PATCH https://api.strata.paloaltonetworks.com/v1/machineidentities/{id} |
| `update ngts machines` | global | `update_ngts_machines` | PATCH https://api.strata.paloaltonetworks.com/v1/machines/{id} |
| `update ngts plugins` | global | `update_ngts_plugins` | PATCH https://api.strata.paloaltonetworks.com/v1/plugins/{id} |
| `update ngts serviceaccounts` | global | `update_ngts_serviceaccounts` | PATCH https://api.strata.paloaltonetworks.com/v1/serviceaccounts/{id} |
| `update ngts serviceaccounts credentials` | global | `update_ngts_serviceaccounts_credentials` | PUT https://api.strata.paloaltonetworks.com/v1/serviceaccounts/{id}/credentials |
| `update ngts serviceaccounts ocitoken` | global | `update_ngts_serviceaccounts_ocitoken` | PUT https://api.strata.paloaltonetworks.com/v1/serviceaccounts/{id}/ocitoken |
| `update ngts tagsassignment` | global | `update_ngts_tagsassignment` | PATCH https://api.strata.paloaltonetworks.com/v1/tagsassignment |
| `update ngts updatesconfig` | global | `update_ngts_updatesconfig` | PATCH https://api.strata.paloaltonetworks.com/v1/updatesconfig |

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
| `show application-filter` | folder | `app_groups` | GET /config/objects/v1/application-filters |
| `show application-group` | folder | `app_groups` | GET /config/objects/v1/application-groups |
| `show external-dynamic-list` | folder | `show_external_dynamic_list` | GET /config/objects/v1/external-dynamic-lists |
| `show hip-object` | folder | `hip` | GET /config/objects/v1/hip-objects |
| `show hip-profile` | folder | `hip` | GET /config/objects/v1/hip-profiles |
| `show log-forwarding-profile` | folder | `log_profiles` | GET /config/objects/v1/log-forwarding-profiles |
| `show region` | global | `regions` | GET /config/objects/v1/regions |
| `show schedule` | folder | `schedules` | GET /config/objects/v1/schedules |
| `show service` | folder | `show_service` | GET /config/objects/v1/services |
| `show service-group` | folder | `service_groups` | GET /config/objects/v1/service-groups |
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
| `set jobs bgp-policy-export` | global | `create_jobs_bgp_policy_export` | POST https://api.strata.paloaltonetworks.com/operations/v1/jobs/bgp-policy-export |
| `set jobs device-interfaces` | global | `create_jobs_device_interfaces` | POST https://api.strata.paloaltonetworks.com/operations/v1/jobs/device-interfaces |
| `set jobs device-rules` | global | `create_jobs_device_rules` | POST https://api.strata.paloaltonetworks.com/operations/v1/jobs/device-rules |
| `set jobs dns-proxy` | global | `create_jobs_dns_proxy` | POST https://api.strata.paloaltonetworks.com/operations/v1/jobs/dns-proxy |
| `set jobs fib-table` | global | `create_jobs_fib_table` | POST https://api.strata.paloaltonetworks.com/operations/v1/jobs/fib-table |
| `set jobs logging-service-forwarding-status` | global | `create_jobs_logging_service_forwarding_status` | POST https://api.strata.paloaltonetworks.com/operations/v1/jobs/logging-service-forwarding-status |
| `set jobs route-table` | global | `create_jobs_route_table` | POST https://api.strata.paloaltonetworks.com/operations/v1/jobs/route-table |
| `show device jobs id` | global | `show_device_jobs_id` | GET https://api.strata.paloaltonetworks.com/operations/v1/device/jobs/{id} |
| `show jobs all` | global | `show_jobs` | GET /config/setup/v1/jobs |
| `show jobs id` | global | `show_jobs` | GET /config/setup/v1/jobs/{id} |
| `show local-config download` | global | `show_local_config_download` | GET https://api.strata.paloaltonetworks.com/operations/v1/local-config/download |
| `show local-config versions` | global | `show_local_config_versions` | GET https://api.strata.paloaltonetworks.com/operations/v1/local-config/versions |
| `show log system` | device | `show_log_system` | (live device state — SSH via --remote) |
| `show log traffic` | device | `show_log_traffic` | (live device state — SSH via --remote) |
| `show system disk-space` | device | `show_system_disk_space` | (live device state — SSH via --remote) |
| `show system info` | device | `show_system_info` | GET /config/setup/v1/devices/{id} |
| `show system resources` | device | `show_system_resources` | (live device state — SSH via --remote) |

## Posture

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `delete posture root` | global | `delete_posture_root` | DELETE https://api.strata.paloaltonetworks.com/posture/checks/v1/{id} |
| `set posture batch-delete` | global | `create_posture_batch_delete` | POST https://api.strata.paloaltonetworks.com/posture/checks/v1/batch-delete |
| `set posture batch-upsert` | global | `create_posture_batch_upsert` | POST https://api.strata.paloaltonetworks.com/posture/checks/v1/batch-upsert |
| `set posture clone` | global | `create_posture_clone` | POST https://api.strata.paloaltonetworks.com/posture/checks/v1/{id}:clone |
| `set posture reports config-file-upload` | global | `create_posture_reports_config_file_upload` | POST https://api.strata.paloaltonetworks.com/posture/checks/v1/reports/config-file-upload |
| `set posture root` | global | `create_posture_root` | POST https://api.strata.paloaltonetworks.com/posture/checks/v1 |
| `show posture id` | global | `show_posture_id` | GET https://api.strata.paloaltonetworks.com/posture/checks/v1/{id} |
| `show posture reports bpa-result id` | global | `show_posture_reports_bpa_result_id` | GET https://api.strata.paloaltonetworks.com/posture/checks/v1/reports/{id}/bpa-result |
| `show posture root` | global | `show_posture_root` | GET https://api.strata.paloaltonetworks.com/posture/checks/v1 |
| `update posture root` | global | `update_posture_root` | PUT https://api.strata.paloaltonetworks.com/posture/checks/v1/{id} |

## Sase

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `delete sase agent-profiles` | global | `delete_sase_agent_profiles` | DELETE https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/agent-profiles |
| `delete sase authentication-settings` | global | `delete_sase_authentication_settings` | DELETE https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/authentication-settings |
| `delete sase bandwidth-allocations` | global | `delete_sase_bandwidth_allocations` | DELETE https://api.strata.paloaltonetworks.com/config/deployment/v1/bandwidth-allocations |
| `delete sase forwarding-profiles` | global | `delete_sase_forwarding_profiles` | DELETE https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profiles/{id} |
| `delete sase fp-custom-proxies` | global | `delete_sase_fp_custom_proxies` | DELETE https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profile-regional-and-custom-proxies/{id} |
| `delete sase fp-destinations` | global | `delete_sase_fp_destinations` | DELETE https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profile-destinations/{id} |
| `delete sase fp-source-apps` | global | `delete_sase_fp_source_apps` | DELETE https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profile-source-applications/{id} |
| `delete sase fp-user-locations` | global | `delete_sase_fp_user_locations` | DELETE https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profile-user-locations/{id} |
| `delete sase infrastructure-settings` | global | `delete_sase_infrastructure_settings` | DELETE https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/infrastructure-settings |
| `delete sase internal-dns-servers` | global | `delete_sase_internal_dns_servers` | DELETE https://api.strata.paloaltonetworks.com/config/deployment/v1/internal-dns-servers/{id} |
| `delete sase remote-networks` | global | `delete_sase_remote_networks` | DELETE https://api.strata.paloaltonetworks.com/config/deployment/v1/remote-networks/{id} |
| `delete sase service-connection-groups` | global | `delete_sase_service_connection_groups` | DELETE https://api.strata.paloaltonetworks.com/config/deployment/v1/service-connection-groups/{id} |
| `delete sase service-connections` | global | `delete_sase_service_connections` | DELETE https://api.strata.paloaltonetworks.com/config/deployment/v1/service-connections/{id} |
| `delete sase sites` | global | `delete_sase_sites` | DELETE https://api.strata.paloaltonetworks.com/config/deployment/v1/sites/{id} |
| `delete sase traffic-steering-rules` | global | `delete_sase_traffic_steering_rules` | DELETE https://api.strata.paloaltonetworks.com/config/deployment/v1/traffic-steering-rules/{id} |
| `delete sase tunnel-profiles` | global | `delete_sase_tunnel_profiles` | DELETE https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/tunnel-profiles |
| `set sase agent-profiles` | global | `create_sase_agent_profiles` | POST https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/agent-profiles |
| `set sase authentication-settings` | global | `create_sase_authentication_settings` | POST https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/authentication-settings |
| `set sase authentication-settings move` | global | `create_sase_authentication_settings_move` | POST https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/authentication-settings/{name}:move |
| `set sase bandwidth-allocations` | global | `create_sase_bandwidth_allocations` | POST https://api.strata.paloaltonetworks.com/config/deployment/v1/bandwidth-allocations |
| `set sase enable` | global | `create_sase_enable` | POST https://api.strata.paloaltonetworks.com/config/deployment/v1/enable |
| `set sase forwarding-profiles` | global | `create_sase_forwarding_profiles` | POST https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profiles |
| `set sase fp-custom-proxies` | global | `create_sase_fp_custom_proxies` | POST https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profile-regional-and-custom-proxies |
| `set sase fp-destinations` | global | `create_sase_fp_destinations` | POST https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profile-destinations |
| `set sase fp-source-apps` | global | `create_sase_fp_source_apps` | POST https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profile-source-applications |
| `set sase fp-user-locations` | global | `create_sase_fp_user_locations` | POST https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profile-user-locations |
| `set sase infrastructure-settings` | global | `create_sase_infrastructure_settings` | POST https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/infrastructure-settings |
| `set sase internal-dns-servers` | global | `create_sase_internal_dns_servers` | POST https://api.strata.paloaltonetworks.com/config/deployment/v1/internal-dns-servers |
| `set sase mobileagent enable` | global | `create_sase_enable` | POST https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/enable |
| `set sase remote-networks` | global | `create_sase_remote_networks` | POST https://api.strata.paloaltonetworks.com/config/deployment/v1/remote-networks |
| `set sase service-connection-groups` | global | `create_sase_service_connection_groups` | POST https://api.strata.paloaltonetworks.com/config/deployment/v1/service-connection-groups |
| `set sase service-connections` | global | `create_sase_service_connections` | POST https://api.strata.paloaltonetworks.com/config/deployment/v1/service-connections |
| `set sase sites` | global | `create_sase_sites` | POST https://api.strata.paloaltonetworks.com/config/deployment/v1/sites |
| `set sase traffic-steering-rules` | global | `create_sase_traffic_steering_rules` | POST https://api.strata.paloaltonetworks.com/config/deployment/v1/traffic-steering-rules |
| `set sase tunnel-profiles` | global | `create_sase_tunnel_profiles` | POST https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/tunnel-profiles |
| `show sase agent-profiles` | global | `show_sase_agent_profiles` | GET https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/agent-profiles |
| `show sase agent-versions` | global | `show_sase_agent_versions` | GET https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/agent-versions |
| `show sase authentication-settings` | global | `show_sase_authentication_settings` | GET https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/authentication-settings |
| `show sase bandwidth-allocations` | global | `show_sase_bandwidth_allocations` | GET https://api.strata.paloaltonetworks.com/config/deployment/v1/bandwidth-allocations |
| `show sase bgp-routing` | global | `show_sase_bgp_routing` | GET https://api.strata.paloaltonetworks.com/config/deployment/v1/bgp-routing |
| `show sase enable` | global | `show_sase_enable` | GET https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/enable |
| `show sase forwarding-profiles` | global | `show_sase_forwarding_profiles` | GET https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profiles |
| `show sase forwarding-profiles id` | global | `show_sase_forwarding_profiles_id` | GET https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profiles/{id} |
| `show sase fp-custom-proxies` | global | `show_sase_fp_custom_proxies` | GET https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profile-regional-and-custom-proxies |
| `show sase fp-custom-proxies id` | global | `show_sase_fp_custom_proxies_id` | GET https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profile-regional-and-custom-proxies/{id} |
| `show sase fp-destinations` | global | `show_sase_fp_destinations` | GET https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profile-destinations |
| `show sase fp-destinations id` | global | `show_sase_fp_destinations_id` | GET https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profile-destinations/{id} |
| `show sase fp-source-apps` | global | `show_sase_fp_source_apps` | GET https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profile-source-applications |
| `show sase fp-source-apps id` | global | `show_sase_fp_source_apps_id` | GET https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profile-source-applications/{id} |
| `show sase fp-user-locations` | global | `show_sase_fp_user_locations` | GET https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profile-user-locations |
| `show sase fp-user-locations id` | global | `show_sase_fp_user_locations_id` | GET https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profile-user-locations/{id} |
| `show sase global-settings` | global | `show_sase_global_settings` | GET https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/global-settings |
| `show sase infrastructure-settings` | global | `show_sase_infrastructure_settings` | GET https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/infrastructure-settings |
| `show sase internal-dns-servers` | global | `show_sase_internal_dns_servers` | GET https://api.strata.paloaltonetworks.com/config/deployment/v1/internal-dns-servers |
| `show sase internal-dns-servers id` | global | `show_sase_internal_dns_servers_id` | GET https://api.strata.paloaltonetworks.com/config/deployment/v1/internal-dns-servers/{id} |
| `show sase locations` | global | `show_sase_locations` | GET https://api.strata.paloaltonetworks.com/config/deployment/v1/locations |
| `show sase mobileagent locations` | global | `show_sase_locations` | GET https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/locations |
| `show sase remote-networks` | global | `show_sase_remote_networks` | GET https://api.strata.paloaltonetworks.com/config/deployment/v1/remote-networks |
| `show sase remote-networks id` | global | `show_sase_remote_networks_id` | GET https://api.strata.paloaltonetworks.com/config/deployment/v1/remote-networks/{id} |
| `show sase service-connection-groups` | global | `show_sase_service_connection_groups` | GET https://api.strata.paloaltonetworks.com/config/deployment/v1/service-connection-groups |
| `show sase service-connection-groups id` | global | `show_sase_service_connection_groups_id` | GET https://api.strata.paloaltonetworks.com/config/deployment/v1/service-connection-groups/{id} |
| `show sase service-connections` | global | `show_sase_service_connections` | GET https://api.strata.paloaltonetworks.com/config/deployment/v1/service-connections |
| `show sase service-connections id` | global | `show_sase_service_connections_id` | GET https://api.strata.paloaltonetworks.com/config/deployment/v1/service-connections/{id} |
| `show sase shared-infrastructure-settings` | global | `show_sase_shared_infrastructure_settings` | GET https://api.strata.paloaltonetworks.com/config/deployment/v1/shared-infrastructure-settings |
| `show sase sites` | global | `show_sase_sites` | GET https://api.strata.paloaltonetworks.com/config/deployment/v1/sites |
| `show sase sites id` | global | `show_sase_sites_id` | GET https://api.strata.paloaltonetworks.com/config/deployment/v1/sites/{id} |
| `show sase traffic-steering-rules` | global | `show_sase_traffic_steering_rules` | GET https://api.strata.paloaltonetworks.com/config/deployment/v1/traffic-steering-rules |
| `show sase traffic-steering-rules id` | global | `show_sase_traffic_steering_rules_id` | GET https://api.strata.paloaltonetworks.com/config/deployment/v1/traffic-steering-rules/{id} |
| `show sase tunnel-profiles` | global | `show_sase_tunnel_profiles` | GET https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/tunnel-profiles |
| `update sase agent-profiles` | global | `update_sase_agent_profiles` | PUT https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/agent-profiles |
| `update sase authentication-settings` | global | `update_sase_authentication_settings` | PUT https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/authentication-settings |
| `update sase bandwidth-allocations` | global | `update_sase_bandwidth_allocations` | PUT https://api.strata.paloaltonetworks.com/config/deployment/v1/bandwidth-allocations |
| `update sase bgp-routing` | global | `update_sase_bgp_routing` | PUT https://api.strata.paloaltonetworks.com/config/deployment/v1/bgp-routing |
| `update sase forwarding-profiles` | global | `update_sase_forwarding_profiles` | PUT https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profiles/{id} |
| `update sase fp-custom-proxies` | global | `update_sase_fp_custom_proxies` | PUT https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profile-regional-and-custom-proxies/{id} |
| `update sase fp-destinations` | global | `update_sase_fp_destinations` | PUT https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profile-destinations/{id} |
| `update sase fp-source-apps` | global | `update_sase_fp_source_apps` | PUT https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profile-source-applications/{id} |
| `update sase fp-user-locations` | global | `update_sase_fp_user_locations` | PUT https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profile-user-locations/{id} |
| `update sase global-settings` | global | `update_sase_global_settings` | PUT https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/global-settings |
| `update sase infrastructure-settings` | global | `update_sase_infrastructure_settings` | PUT https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/infrastructure-settings |
| `update sase internal-dns-servers` | global | `update_sase_internal_dns_servers` | PUT https://api.strata.paloaltonetworks.com/config/deployment/v1/internal-dns-servers/{id} |
| `update sase locations` | global | `update_sase_locations` | PUT https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/locations |
| `update sase remote-networks` | global | `update_sase_remote_networks` | PUT https://api.strata.paloaltonetworks.com/config/deployment/v1/remote-networks/{id} |
| `update sase service-connection-groups` | global | `update_sase_service_connection_groups` | PUT https://api.strata.paloaltonetworks.com/config/deployment/v1/service-connection-groups/{id} |
| `update sase service-connections` | global | `update_sase_service_connections` | PUT https://api.strata.paloaltonetworks.com/config/deployment/v1/service-connections/{id} |
| `update sase shared-infrastructure-settings` | global | `update_sase_shared_infrastructure_settings` | PUT https://api.strata.paloaltonetworks.com/config/deployment/v1/shared-infrastructure-settings |
| `update sase sites` | global | `update_sase_sites` | PUT https://api.strata.paloaltonetworks.com/config/deployment/v1/sites/{id} |
| `update sase traffic-steering-rules` | global | `update_sase_traffic_steering_rules` | PUT https://api.strata.paloaltonetworks.com/config/deployment/v1/traffic-steering-rules/{id} |
| `update sase tunnel-profiles` | global | `update_sase_tunnel_profiles` | PUT https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/tunnel-profiles |

## Security

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `delete security-rule` | folder | `delete_security` | DELETE /config/security/v1/security-rules/{id} |
| `delete url-category` | folder | `delete_security` | DELETE /config/security/v1/url-categories/{id} |
| `set url-category` | folder | `create_url_category` | POST /config/security/v1/url-categories |
| `show anti-spyware-profile` | folder | `security_profiles` | GET /config/security/v1/anti-spyware-profiles |
| `show app-override-rules` | folder | `app_override` | GET /config/security/v1/app-override-rules |
| `show decryption-profile` | folder | `decryption_policy` | GET /config/security/v1/decryption-profiles |
| `show decryption-rules` | folder | `decryption_policy` | GET /config/security/v1/decryption-rules |
| `show dos-protection-profile` | folder | `dos_protection` | GET /config/security/v1/dos-protection-profiles |
| `show dos-protection-rules` | folder | `dos_protection` | GET /config/security/v1/dos-protection-rules |
| `show profile-group` | folder | `profile_groups` | GET /config/security/v1/profile-groups |
| `show security policy` | folder | `show_security_policy` | GET /config/security/v1/security-rules |
| `show url-categories` | folder | `show_url_categories` | GET /config/security/v1/url-categories |
| `show vulnerability-profile` | folder | `security_profiles` | GET /config/security/v1/vulnerability-protection-profiles |
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

## Subscription

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `set subscription instances` | global | `create_subscription_instances` | POST https://api.sase.paloaltonetworks.com/subscription/v1/instances |
| `show subscription instances` | global | `show_subscription_instances` | GET https://api.sase.paloaltonetworks.com/subscription/v1/instances |
| `show subscription licenses` | global | `show_subscription_licenses` | GET https://api.sase.paloaltonetworks.com/subscription/v1/licenses |

## Tenancy

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `delete tenant-service-groups` | global | `delete_tenant_service_groups` | DELETE https://api.sase.paloaltonetworks.com/tenancy/v1/tenant_service_groups/{tsg_id} |
| `set tenant-service-groups` | global | `create_tenant_service_groups` | POST https://api.sase.paloaltonetworks.com/tenancy/v1/tenant_service_groups |
| `set tenant-service-groups list-ancestors` | global | `create_tenant_service_groups_list_ancestors` | POST https://api.sase.paloaltonetworks.com/tenancy/v1/tenant_service_groups/{tsg_id}/operations/list_ancestors |
| `set tenant-service-groups list-children` | global | `create_tenant_service_groups_list_children` | POST https://api.sase.paloaltonetworks.com/tenancy/v1/tenant_service_groups/{tsg_id}/operations/list_children |
| `show tenant-service-groups` | global | `show_tenant_service_groups` | GET https://api.sase.paloaltonetworks.com/tenancy/v1/tenant_service_groups |
| `show tenant-service-groups id` | global | `show_tenant_service_groups_id` | GET https://api.sase.paloaltonetworks.com/tenancy/v1/tenant_service_groups/{tsg_id} |
| `update tenant-service-groups` | global | `update_tenant_service_groups` | PUT https://api.sase.paloaltonetworks.com/tenancy/v1/tenant_service_groups/{tsg_id} |
