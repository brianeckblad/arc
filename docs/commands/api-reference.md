# ARC Command → SCM API Reference

Generated from each command's doc front-matter (`api:` field) and the live
registry. Regenerate with `python dev/generate_command_docs.py` (runs on `docsupdate`).

## Adnsr

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `delete adnsr bad-domains` | global | `adnsr_bad_domains_write` | DELETE https://api.strata.paloaltonetworks.com/adns-resolver/v1/misconfigured-domains/{misconfigured-domain-id} |
| `delete adnsr ca-certs` | global | `adnsr_ca_certs_write` | DELETE https://api.strata.paloaltonetworks.com/adns-resolver/v1/ca-certs/{ca-cert-id} |
| `delete adnsr conn-sources` | global | `adnsr_conn_sources_write` | DELETE https://api.strata.paloaltonetworks.com/adns-resolver/v1/connection-sources/{connection-source-id} |
| `delete adnsr conn-sources subnets` | global | `adnsr_conn_sources_subnets_write` | DELETE https://api.strata.paloaltonetworks.com/adns-resolver/v1/connection-sources/{connection-source-id}/subnets/{subnet-id} |
| `delete adnsr custom-fqdns` | global | `adnsr_custom_fqdns_write` | DELETE https://api.strata.paloaltonetworks.com/adns-resolver/v1/custom-fqdns/{custom-fqdn-id} |
| `delete adnsr edls` | global | `adnsr_edls_write` | DELETE https://api.strata.paloaltonetworks.com/adns-resolver/v1/edls/{edl-id} |
| `delete adnsr internal-domains` | global | `adnsr_internal_domains_write` | DELETE https://api.strata.paloaltonetworks.com/adns-resolver/v1/internal-domains/{internal-domain-id} |
| `delete adnsr profiles` | global | `adnsr_profiles_write` | DELETE https://api.strata.paloaltonetworks.com/adns-resolver/v1/profiles/{profile-id} |
| `set adnsr bad-domains` | global | `adnsr_bad_domains_write` | POST https://api.strata.paloaltonetworks.com/adns-resolver/v1/misconfigured-domains |
| `set adnsr ca-certs upload` | global | `adnsr_ca_certs_upload_write` | POST https://api.strata.paloaltonetworks.com/adns-resolver/v1/ca-certs:upload |
| `set adnsr conn-sources` | global | `adnsr_conn_sources_write` | POST https://api.strata.paloaltonetworks.com/adns-resolver/v1/connection-sources |
| `set adnsr conn-sources subnets` | global | `adnsr_conn_sources_subnets_write` | POST https://api.strata.paloaltonetworks.com/adns-resolver/v1/connection-sources/{connection-source-id}/subnets |
| `set adnsr conn-sources subnets verify` | global | `adnsr_conn_sources_subnets_verify_write` | POST https://api.strata.paloaltonetworks.com/adns-resolver/v1/connection-sources/{connection-source-id}/subnets/{subnet-id}:verify-update |
| `set adnsr custom-fqdns` | global | `adnsr_custom_fqdns_write` | POST https://api.strata.paloaltonetworks.com/adns-resolver/v1/custom-fqdns |
| `set adnsr edls` | global | `adnsr_edls_write` | POST https://api.strata.paloaltonetworks.com/adns-resolver/v1/edls |
| `set adnsr internal-domains` | global | `adnsr_internal_domains_write` | POST https://api.strata.paloaltonetworks.com/adns-resolver/v1/internal-domains |
| `set adnsr profiles` | global | `adnsr_profiles_write` | POST https://api.strata.paloaltonetworks.com/adns-resolver/v1/profiles |
| `show adnsr bad-domains` | global | `adnsr_bad_domains_read` | GET https://api.strata.paloaltonetworks.com/adns-resolver/v1/misconfigured-domains |
| `show adnsr bad-domains id` | global | `adnsr_bad_domains_read` | GET https://api.strata.paloaltonetworks.com/adns-resolver/v1/misconfigured-domains/{misconfigured-domain-id} |
| `show adnsr ca-certs` | global | `adnsr_ca_certs_read` | GET https://api.strata.paloaltonetworks.com/adns-resolver/v1/ca-certs |
| `show adnsr ca-certs download id` | global | `adnsr_ca_certs_download_read` | GET https://api.strata.paloaltonetworks.com/adns-resolver/v1/ca-certs/{ca-cert-id}/download |
| `show adnsr ca-certs id` | global | `adnsr_ca_certs_read` | GET https://api.strata.paloaltonetworks.com/adns-resolver/v1/ca-certs/{ca-cert-id} |
| `show adnsr conn-sources` | global | `adnsr_conn_sources_read` | GET https://api.strata.paloaltonetworks.com/adns-resolver/v1/connection-sources |
| `show adnsr conn-sources id` | global | `adnsr_conn_sources_read` | GET https://api.strata.paloaltonetworks.com/adns-resolver/v1/connection-sources/{connection-source-id} |
| `show adnsr conn-sources subnets` | global | `adnsr_conn_sources_subnets_read` | GET https://api.strata.paloaltonetworks.com/adns-resolver/v1/connection-sources/subnets |
| `show adnsr conn-sources subnets id` | global | `adnsr_conn_sources_subnets_read` | GET https://api.strata.paloaltonetworks.com/adns-resolver/v1/connection-sources/{connection-source-id}/subnets/{subnet-id} |
| `show adnsr conn-sources subnets id id` | global | `adnsr_conn_sources_subnets_read` | GET https://api.strata.paloaltonetworks.com/adns-resolver/v1/connection-sources/{connection-source-id}/subnets |
| `show adnsr custom-fqdns` | global | `adnsr_custom_fqdns_read` | GET https://api.strata.paloaltonetworks.com/adns-resolver/v1/custom-fqdns |
| `show adnsr custom-fqdns id` | global | `adnsr_custom_fqdns_read` | GET https://api.strata.paloaltonetworks.com/adns-resolver/v1/custom-fqdns/{custom-fqdn-id} |
| `show adnsr edls` | global | `adnsr_edls_read` | GET https://api.strata.paloaltonetworks.com/adns-resolver/v1/edls |
| `show adnsr edls id` | global | `adnsr_edls_read` | GET https://api.strata.paloaltonetworks.com/adns-resolver/v1/edls/{edl-id} |
| `show adnsr internal-domains` | global | `adnsr_internal_domains_read` | GET https://api.strata.paloaltonetworks.com/adns-resolver/v1/internal-domains |
| `show adnsr internal-domains id` | global | `adnsr_internal_domains_read` | GET https://api.strata.paloaltonetworks.com/adns-resolver/v1/internal-domains/{internal-domain-id} |
| `show adnsr profiles` | global | `adnsr_profiles_read` | GET https://api.strata.paloaltonetworks.com/adns-resolver/v1/profiles |
| `show adnsr profiles categories` | global | `adnsr_profiles_categories_read` | GET https://api.strata.paloaltonetworks.com/adns-resolver/v1/profiles/categories |
| `show adnsr profiles id` | global | `adnsr_profiles_read` | GET https://api.strata.paloaltonetworks.com/adns-resolver/v1/profiles/{profile-id} |
| `show adnsr resolver-info` | global | `adnsr_resolver_info_read` | GET https://api.strata.paloaltonetworks.com/adns-resolver/v1/resolver-info |
| `update adnsr bad-domains` | global | `adnsr_bad_domains_write` | PUT https://api.strata.paloaltonetworks.com/adns-resolver/v1/misconfigured-domains/{misconfigured-domain-id} |
| `update adnsr conn-sources` | global | `adnsr_conn_sources_write` | PUT https://api.strata.paloaltonetworks.com/adns-resolver/v1/connection-sources/{connection-source-id} |
| `update adnsr custom-fqdns` | global | `adnsr_custom_fqdns_write` | PUT https://api.strata.paloaltonetworks.com/adns-resolver/v1/custom-fqdns/{custom-fqdn-id} |
| `update adnsr edls` | global | `adnsr_edls_write` | PUT https://api.strata.paloaltonetworks.com/adns-resolver/v1/edls/{edl-id} |
| `update adnsr internal-domains` | global | `adnsr_internal_domains_write` | PUT https://api.strata.paloaltonetworks.com/adns-resolver/v1/internal-domains/{internal-domain-id} |
| `update adnsr profiles` | global | `adnsr_profiles_write` | PUT https://api.strata.paloaltonetworks.com/adns-resolver/v1/profiles/{profile-id} |

## Auth

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `set oauth2 access-token` | global | `oauth2_access_token_write` | POST https://auth.apps.paloaltonetworks.com/auth/v1/oauth2/access_token |
| `set oauth2 userinfo` | global | `oauth2_userinfo_write` | POST https://auth.apps.paloaltonetworks.com/auth/v1/oauth2/userinfo |
| `show oauth2 userinfo` | global | `oauth2_userinfo_read` | GET https://auth.apps.paloaltonetworks.com/auth/v1/oauth2/userinfo |

## Cdug

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `delete cdug cloud-dug-definition group` | global | `cdug_cloud_dug_definition_group_write` | DELETE /directory-sync/v1/cloud-dug-definition/group |
| `set cdug cloud-dug-definition` | global | `cdug_cloud_dug_definition_write` | POST /directory-sync/v1/cloud-dug-definition |
| `show cdug cloud-dug-definition category` | global | `cdug_cloud_dug_definition_category_read` | GET /directory-sync/v1/cloud-dug-definition/category |
| `show cdug cloud-dug-definition group` | global | `cdug_cloud_dug_definition_group_read` | GET /directory-sync/v1/cloud-dug-definition/group |
| `show cdug user-attr-values` | global | `cdug_user_attr_values_read` | GET /directory-sync/v1/user-attr-values |
| `update cdug cloud-dug-definition group` | global | `cdug_cloud_dug_definition_group_write` | PUT /directory-sync/v1/cloud-dug-definition/group |

## Ciedss

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `set ciedss cache-groups` | global | `ciedss_cache_groups_write` | POST https://api.sase.paloaltonetworks.com/cie/directory-sync/v1/cache-groups |
| `set ciedss cache-users` | global | `ciedss_cache_users_write` | POST https://api.sase.paloaltonetworks.com/cie/directory-sync/v1/cache-users |
| `set ciedss connection update-secret` | global | `ciedss_connection_update_secret_write` | POST https://api.sase.paloaltonetworks.com/cie/directory-sync/v1/connection/update-secret |
| `show ciedss domains` | global | `ciedss_domains_read` | GET https://api.sase.paloaltonetworks.com/cie/directory-sync/v1/domains |

## Cloudngfw

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `delete cngfw address-groups` | global | `cngfw_address_groups_write` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/address-groups/{id} |
| `delete cngfw addresses` | global | `cngfw_addresses_write` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/addresses/{id} |
| `delete cngfw adv-device-objs` | global | `cngfw_adv_device_objs_write` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/advanced-device-objects |
| `delete cngfw adv-device-objs id` | global | `cngfw_adv_device_objs_write` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/advanced-device-objects/{id} |
| `delete cngfw anti-spyware-profiles` | global | `cngfw_anti_spyware_profiles_write` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/anti-spyware-profiles/{id} |
| `delete cngfw anti-spyware-signatures` | global | `cngfw_anti_spyware_signatures_write` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/anti-spyware-signatures/{id} |
| `delete cngfw app-override-rules` | global | `cngfw_app_override_rules_write` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/app-override-rules/{id} |
| `delete cngfw application-filters` | global | `cngfw_application_filters_write` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/application-filters/{id} |
| `delete cngfw application-groups` | global | `cngfw_application_groups_write` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/application-groups/{id} |
| `delete cngfw applications` | global | `cngfw_applications_write` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/applications/{id} |
| `delete cngfw authentication-portals` | global | `cngfw_authentication_portals_write` | DELETE https://api.strata.paloaltonetworks.com/config/identity/v1/authentication-portals/{id} |
| `delete cngfw authentication-profiles` | global | `cngfw_authentication_profiles_write` | DELETE https://api.strata.paloaltonetworks.com/config/identity/v1/authentication-profiles/{id} |
| `delete cngfw authentication-rules` | global | `cngfw_authentication_rules_write` | DELETE https://api.strata.paloaltonetworks.com/config/identity/v1/authentication-rules/{id} |
| `delete cngfw authentication-sequences` | global | `cngfw_authentication_sequences_write` | DELETE https://api.strata.paloaltonetworks.com/config/identity/v1/authentication-sequences/{id} |
| `delete cngfw auto-tag-actions` | global | `cngfw_auto_tag_actions_write` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/auto-tag-actions |
| `delete cngfw certificate-profiles` | global | `cngfw_certificate_profiles_write` | DELETE https://api.strata.paloaltonetworks.com/config/identity/v1/certificate-profiles/{id} |
| `delete cngfw certs` | global | `cngfw_certs_write` | DELETE https://api.strata.paloaltonetworks.com/config/identity/v1/certificates/{id} |
| `delete cngfw config-versions candidate` | global | `cngfw_config_versions_candidate_write` | DELETE https://api.strata.paloaltonetworks.com/config/operations/v1/config-versions/candidate |
| `delete cngfw data-filtering-profiles` | global | `cngfw_data_filtering_profiles_write` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/data-filtering-profiles/{id} |
| `delete cngfw data-objects` | global | `cngfw_data_objects_write` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/data-objects/{id} |
| `delete cngfw decryption-exclusions` | global | `cngfw_decryption_exclusions_write` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/decryption-exclusions/{id} |
| `delete cngfw decryption-profiles` | global | `cngfw_decryption_profiles_write` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/decryption-profiles/{id} |
| `delete cngfw decryption-rules` | global | `cngfw_decryption_rules_write` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/decryption-rules/{id} |
| `delete cngfw device-contexts` | global | `cngfw_device_contexts_write` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/device-context-segments |
| `delete cngfw device-contexts id` | global | `cngfw_device_contexts_write` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/device-context-segments/{id} |
| `delete cngfw dns-security-profiles` | global | `cngfw_dns_security_profiles_write` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/dns-security-profiles/{id} |
| `delete cngfw dos-protection-profiles` | global | `cngfw_dos_protection_profiles_write` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/dos-protection-profiles/{id} |
| `delete cngfw dos-protection-rules` | global | `cngfw_dos_protection_rules_write` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/dos-protection-rules/{id} |
| `delete cngfw dynamic-user-groups` | global | `cngfw_dynamic_user_groups_write` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/dynamic-user-groups/{id} |
| `delete cngfw external-dynamic-lists` | global | `cngfw_external_dynamic_lists_write` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/external-dynamic-lists/{id} |
| `delete cngfw file-blocking-profiles` | global | `cngfw_file_blocking_profiles_write` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/file-blocking-profiles/{id} |
| `delete cngfw folders` | global | `cngfw_folders_write` | DELETE https://api.strata.paloaltonetworks.com/config/setup/v1/folders/{id} |
| `delete cngfw hip-objects` | global | `cngfw_hip_objects_write` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/hip-objects/{id} |
| `delete cngfw hip-profiles` | global | `cngfw_hip_profiles_write` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/hip-profiles/{id} |
| `delete cngfw http-header-profiles` | global | `cngfw_http_header_profiles_write` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/http-header-profiles/{id} |
| `delete cngfw http-server-profiles` | global | `cngfw_http_server_profiles_write` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/http-server-profiles/{id} |
| `delete cngfw kerberos-server-profiles` | global | `cngfw_kerberos_server_profiles_write` | DELETE https://api.strata.paloaltonetworks.com/config/identity/v1/kerberos-server-profiles/{id} |
| `delete cngfw labels` | global | `cngfw_labels_write` | DELETE https://api.strata.paloaltonetworks.com/config/setup/v1/labels/{id} |
| `delete cngfw ldap-server-profiles` | global | `cngfw_ldap_server_profiles_write` | DELETE https://api.strata.paloaltonetworks.com/config/identity/v1/ldap-server-profiles/{id} |
| `delete cngfw local-user-groups` | global | `cngfw_local_user_groups_write` | DELETE https://api.strata.paloaltonetworks.com/config/identity/v1/local-user-groups/{id} |
| `delete cngfw local-users` | global | `cngfw_local_users_write` | DELETE https://api.strata.paloaltonetworks.com/config/identity/v1/local-users/{id} |
| `delete cngfw log-forwarding-profiles` | global | `cngfw_log_forwarding_profiles_write` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/log-forwarding-profiles/{id} |
| `delete cngfw mfa-servers` | global | `cngfw_mfa_servers_write` | DELETE https://api.strata.paloaltonetworks.com/config/identity/v1/mfa-servers/{id} |
| `delete cngfw ocsp-responders` | global | `cngfw_ocsp_responders_write` | DELETE https://api.strata.paloaltonetworks.com/config/identity/v1/ocsp-responders/{id} |
| `delete cngfw onboarding-rules` | global | `cngfw_onboarding_rules_write` | DELETE https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1/onboarding-rules/{id} |
| `delete cngfw profile-groups` | global | `cngfw_profile_groups_write` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/profile-groups/{id} |
| `delete cngfw properties` | global | `cngfw_properties_write` | DELETE https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1/properties/{id} |
| `delete cngfw quarantined-devices` | global | `cngfw_quarantined_devices_write` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/quarantined-devices |
| `delete cngfw radius-server-profiles` | global | `cngfw_radius_server_profiles_write` | DELETE https://api.strata.paloaltonetworks.com/config/identity/v1/radius-server-profiles/{id} |
| `delete cngfw regions` | global | `cngfw_regions_write` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/regions/{id} |
| `delete cngfw saml-server-profiles` | global | `cngfw_saml_server_profiles_write` | DELETE https://api.strata.paloaltonetworks.com/config/identity/v1/saml-server-profiles/{id} |
| `delete cngfw scep-profiles` | global | `cngfw_scep_profiles_write` | DELETE https://api.strata.paloaltonetworks.com/config/identity/v1/scep-profiles/{id} |
| `delete cngfw schedules` | global | `cngfw_schedules_write` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/schedules/{id} |
| `delete cngfw security-rules` | global | `cngfw_security_rules_write` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/security-rules/{id} |
| `delete cngfw service-groups` | global | `cngfw_service_groups_write` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/service-groups/{id} |
| `delete cngfw services` | global | `cngfw_services_write` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/services/{id} |
| `delete cngfw site-groups` | global | `cngfw_site_groups_write` | DELETE https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1/site-groups/{id} |
| `delete cngfw sites` | global | `cngfw_sites_write` | DELETE https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1/sites/{id} |
| `delete cngfw snippet-categories` | global | `cngfw_snippet_categories_write` | DELETE https://api.strata.paloaltonetworks.com/config/setup/v1/snippet-categories/{id} |
| `delete cngfw snippets` | global | `cngfw_snippets_write` | DELETE https://api.strata.paloaltonetworks.com/config/setup/v1/snippets/{id} |
| `delete cngfw ssl-decryption-settings` | global | `cngfw_ssl_decryption_settings_write` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/ssl-decryption-settings |
| `delete cngfw subscribed-tenants` | global | `cngfw_subscribed_tenants_write` | DELETE https://api.strata.paloaltonetworks.com/config/setup/v1/subscribed-tenants |
| `delete cngfw syslog-server-profiles` | global | `cngfw_syslog_server_profiles_write` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/syslog-server-profiles/{id} |
| `delete cngfw tacacs-server-profiles` | global | `cngfw_tacacs_server_profiles_write` | DELETE https://api.strata.paloaltonetworks.com/config/identity/v1/tacacs-server-profiles/{id} |
| `delete cngfw tags` | global | `cngfw_tags_write` | DELETE https://api.strata.paloaltonetworks.com/config/objects/v1/tags/{id} |
| `delete cngfw tls-service-profiles` | global | `cngfw_tls_service_profiles_write` | DELETE https://api.strata.paloaltonetworks.com/config/identity/v1/tls-service-profiles/{id} |
| `delete cngfw trusts` | global | `cngfw_trusts_write` | DELETE https://api.strata.paloaltonetworks.com/config/setup/v1/trusts |
| `delete cngfw url-access-profiles` | global | `cngfw_url_access_profiles_write` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/url-access-profiles/{id} |
| `delete cngfw url-admin-override` | global | `cngfw_url_admin_override_write` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/url-admin-override/{id} |
| `delete cngfw url-categories` | global | `cngfw_url_categories_write` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/url-categories/{id} |
| `delete cngfw variables` | global | `cngfw_variables_write` | DELETE https://api.strata.paloaltonetworks.com/config/setup/v1/variables/{id} |
| `delete cngfw vuln-profiles` | global | `cngfw_vuln_profiles_write` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/vulnerability-protection-profiles/{id} |
| `delete cngfw vuln-signatures` | global | `cngfw_vuln_signatures_write` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/vulnerability-protection-signatures/{id} |
| `delete cngfw wildfire-profiles` | global | `cngfw_wildfire_profiles_write` | DELETE https://api.strata.paloaltonetworks.com/config/security/v1/wildfire-anti-virus-profiles/{id} |
| `set cngfw address-groups` | global | `cngfw_address_groups_write` | POST https://api.strata.paloaltonetworks.com/config/objects/v1/address-groups |
| `set cngfw addresses` | global | `cngfw_addresses_write` | POST https://api.strata.paloaltonetworks.com/config/objects/v1/addresses |
| `set cngfw adv-device-objs` | global | `cngfw_adv_device_objs_write` | POST https://api.strata.paloaltonetworks.com/config/objects/v1/advanced-device-objects |
| `set cngfw anti-spyware-profiles` | global | `cngfw_anti_spyware_profiles_write` | POST https://api.strata.paloaltonetworks.com/config/security/v1/anti-spyware-profiles |
| `set cngfw anti-spyware-signatures` | global | `cngfw_anti_spyware_signatures_write` | POST https://api.strata.paloaltonetworks.com/config/security/v1/anti-spyware-signatures |
| `set cngfw app-override-rules` | global | `cngfw_app_override_rules_write` | POST https://api.strata.paloaltonetworks.com/config/security/v1/app-override-rules |
| `set cngfw app-override-rules move` | global | `cngfw_app_override_rules_move_write` | POST https://api.strata.paloaltonetworks.com/config/security/v1/app-override-rules/{id}:move |
| `set cngfw application-filters` | global | `cngfw_application_filters_write` | POST https://api.strata.paloaltonetworks.com/config/objects/v1/application-filters |
| `set cngfw application-groups` | global | `cngfw_application_groups_write` | POST https://api.strata.paloaltonetworks.com/config/objects/v1/application-groups |
| `set cngfw applications` | global | `cngfw_applications_write` | POST https://api.strata.paloaltonetworks.com/config/objects/v1/applications |
| `set cngfw authentication-portals` | global | `cngfw_authentication_portals_write` | POST https://api.strata.paloaltonetworks.com/config/identity/v1/authentication-portals |
| `set cngfw authentication-profiles` | global | `cngfw_authentication_profiles_write` | POST https://api.strata.paloaltonetworks.com/config/identity/v1/authentication-profiles |
| `set cngfw authentication-rules` | global | `cngfw_authentication_rules_write` | POST https://api.strata.paloaltonetworks.com/config/identity/v1/authentication-rules |
| `set cngfw authentication-rules move` | global | `cngfw_authentication_rules_move_write` | POST https://api.strata.paloaltonetworks.com/config/identity/v1/authentication-rules/{id}:move |
| `set cngfw authentication-sequences` | global | `cngfw_authentication_sequences_write` | POST https://api.strata.paloaltonetworks.com/config/identity/v1/authentication-sequences |
| `set cngfw auto-tag-actions` | global | `cngfw_auto_tag_actions_write` | POST https://api.strata.paloaltonetworks.com/config/objects/v1/auto-tag-actions |
| `set cngfw certificate-profiles` | global | `cngfw_certificate_profiles_write` | POST https://api.strata.paloaltonetworks.com/config/identity/v1/certificate-profiles |
| `set cngfw certs` | global | `cngfw_certs_write` | POST https://api.strata.paloaltonetworks.com/config/identity/v1/certificates |
| `set cngfw certs export` | global | `cngfw_certs_export_write` | POST https://api.strata.paloaltonetworks.com/config/identity/v1/certificates/{id}:export |
| `set cngfw certs import` | global | `cngfw_certs_import_write` | POST https://api.strata.paloaltonetworks.com/config/identity/v1/certificates:import |
| `set cngfw config-versions candidate push` | global | `cngfw_config_versions_candidate_push_write` | POST https://api.strata.paloaltonetworks.com/config/operations/v1/config-versions/candidate:push |
| `set cngfw config-versions load` | global | `cngfw_config_versions_load_write` | POST https://api.strata.paloaltonetworks.com/config/operations/v1/config-versions:load |
| `set cngfw data-filtering-profiles` | global | `cngfw_data_filtering_profiles_write` | POST https://api.strata.paloaltonetworks.com/config/security/v1/data-filtering-profiles |
| `set cngfw data-objects` | global | `cngfw_data_objects_write` | POST https://api.strata.paloaltonetworks.com/config/security/v1/data-objects |
| `set cngfw decryption-exclusions` | global | `cngfw_decryption_exclusions_write` | POST https://api.strata.paloaltonetworks.com/config/security/v1/decryption-exclusions |
| `set cngfw decryption-profiles` | global | `cngfw_decryption_profiles_write` | POST https://api.strata.paloaltonetworks.com/config/security/v1/decryption-profiles |
| `set cngfw decryption-rules` | global | `cngfw_decryption_rules_write` | POST https://api.strata.paloaltonetworks.com/config/security/v1/decryption-rules |
| `set cngfw decryption-rules move` | global | `cngfw_decryption_rules_move_write` | POST https://api.strata.paloaltonetworks.com/config/security/v1/decryption-rules/{id}:move |
| `set cngfw device-contexts` | global | `cngfw_device_contexts_write` | POST https://api.strata.paloaltonetworks.com/config/objects/v1/device-context-segments |
| `set cngfw dns-security-profiles` | global | `cngfw_dns_security_profiles_write` | POST https://api.strata.paloaltonetworks.com/config/security/v1/dns-security-profiles |
| `set cngfw dos-protection-profiles` | global | `cngfw_dos_protection_profiles_write` | POST https://api.strata.paloaltonetworks.com/config/security/v1/dos-protection-profiles |
| `set cngfw dos-protection-rules` | global | `cngfw_dos_protection_rules_write` | POST https://api.strata.paloaltonetworks.com/config/security/v1/dos-protection-rules |
| `set cngfw dynamic-user-groups` | global | `cngfw_dynamic_user_groups_write` | POST https://api.strata.paloaltonetworks.com/config/objects/v1/dynamic-user-groups |
| `set cngfw external-dynamic-lists` | global | `cngfw_external_dynamic_lists_write` | POST https://api.strata.paloaltonetworks.com/config/objects/v1/external-dynamic-lists |
| `set cngfw file-blocking-profiles` | global | `cngfw_file_blocking_profiles_write` | POST https://api.strata.paloaltonetworks.com/config/security/v1/file-blocking-profiles |
| `set cngfw folders` | global | `cngfw_folders_write` | POST https://api.strata.paloaltonetworks.com/config/setup/v1/folders |
| `set cngfw hip-objects` | global | `cngfw_hip_objects_write` | POST https://api.strata.paloaltonetworks.com/config/objects/v1/hip-objects |
| `set cngfw hip-profiles` | global | `cngfw_hip_profiles_write` | POST https://api.strata.paloaltonetworks.com/config/objects/v1/hip-profiles |
| `set cngfw http-header-profiles` | global | `cngfw_http_header_profiles_write` | POST https://api.strata.paloaltonetworks.com/config/security/v1/http-header-profiles |
| `set cngfw http-server-profiles` | global | `cngfw_http_server_profiles_write` | POST https://api.strata.paloaltonetworks.com/config/objects/v1/http-server-profiles |
| `set cngfw kerberos-server-profiles` | global | `cngfw_kerberos_server_profiles_write` | POST https://api.strata.paloaltonetworks.com/config/identity/v1/kerberos-server-profiles |
| `set cngfw labels` | global | `cngfw_labels_write` | POST https://api.strata.paloaltonetworks.com/config/setup/v1/labels |
| `set cngfw ldap-server-profiles` | global | `cngfw_ldap_server_profiles_write` | POST https://api.strata.paloaltonetworks.com/config/identity/v1/ldap-server-profiles |
| `set cngfw local-user-groups` | global | `cngfw_local_user_groups_write` | POST https://api.strata.paloaltonetworks.com/config/identity/v1/local-user-groups |
| `set cngfw local-users` | global | `cngfw_local_users_write` | POST https://api.strata.paloaltonetworks.com/config/identity/v1/local-users |
| `set cngfw log-forwarding-profiles` | global | `cngfw_log_forwarding_profiles_write` | POST https://api.strata.paloaltonetworks.com/config/objects/v1/log-forwarding-profiles |
| `set cngfw mfa-servers` | global | `cngfw_mfa_servers_write` | POST https://api.strata.paloaltonetworks.com/config/identity/v1/mfa-servers |
| `set cngfw ocsp-responders` | global | `cngfw_ocsp_responders_write` | POST https://api.strata.paloaltonetworks.com/config/identity/v1/ocsp-responders |
| `set cngfw onboarding-rules` | global | `cngfw_onboarding_rules_write` | POST https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1/onboarding-rules |
| `set cngfw onboarding-rules move` | global | `cngfw_onboarding_rules_move_write` | POST https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1/onboarding-rules/{id}:move |
| `set cngfw profile-groups` | global | `cngfw_profile_groups_write` | POST https://api.strata.paloaltonetworks.com/config/security/v1/profile-groups |
| `set cngfw properties` | global | `cngfw_properties_write` | POST https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1/properties |
| `set cngfw quarantined-devices` | global | `cngfw_quarantined_devices_write` | POST https://api.strata.paloaltonetworks.com/config/objects/v1/quarantined-devices |
| `set cngfw radius-server-profiles` | global | `cngfw_radius_server_profiles_write` | POST https://api.strata.paloaltonetworks.com/config/identity/v1/radius-server-profiles |
| `set cngfw regions` | global | `cngfw_regions_write` | POST https://api.strata.paloaltonetworks.com/config/objects/v1/regions |
| `set cngfw saml-server-profiles` | global | `cngfw_saml_server_profiles_write` | POST https://api.strata.paloaltonetworks.com/config/identity/v1/saml-server-profiles |
| `set cngfw scep-profiles` | global | `cngfw_scep_profiles_write` | POST https://api.strata.paloaltonetworks.com/config/identity/v1/scep-profiles |
| `set cngfw schedules` | global | `cngfw_schedules_write` | POST https://api.strata.paloaltonetworks.com/config/objects/v1/schedules |
| `set cngfw security-rules` | global | `cngfw_security_rules_write` | POST https://api.strata.paloaltonetworks.com/config/security/v1/security-rules |
| `set cngfw security-rules move` | global | `cngfw_security_rules_move_write` | POST https://api.strata.paloaltonetworks.com/config/security/v1/security-rules/{id}:move |
| `set cngfw service-groups` | global | `cngfw_service_groups_write` | POST https://api.strata.paloaltonetworks.com/config/objects/v1/service-groups |
| `set cngfw services` | global | `cngfw_services_write` | POST https://api.strata.paloaltonetworks.com/config/objects/v1/services |
| `set cngfw shared-snippets load` | global | `cngfw_shared_snippets_load_write` | POST https://api.strata.paloaltonetworks.com/config/setup/v1/shared-snippets:load |
| `set cngfw site-groups` | global | `cngfw_site_groups_write` | POST https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1/site-groups |
| `set cngfw sites` | global | `cngfw_sites_write` | POST https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1/sites |
| `set cngfw snippet-audit-logs` | global | `cngfw_snippet_audit_logs_write` | POST https://api.strata.paloaltonetworks.com/config/setup/v1/snippet-audit-logs |
| `set cngfw snippet-snapshots` | global | `cngfw_snippet_snapshots_write` | POST https://api.strata.paloaltonetworks.com/config/setup/v1/snippet-snapshots |
| `set cngfw snippet-snapshots compare` | global | `cngfw_snippet_snapshots_compare_write` | POST https://api.strata.paloaltonetworks.com/config/setup/v1/snippet-snapshots:compare |
| `set cngfw snippet-snapshots convert` | global | `cngfw_snippet_snapshots_convert_write` | POST https://api.strata.paloaltonetworks.com/config/setup/v1/snippet-snapshots:convert |
| `set cngfw snippet-snapshots diff` | global | `cngfw_snippet_snapshots_diff_write` | POST https://api.strata.paloaltonetworks.com/config/setup/v1/snippet-snapshots:diff |
| `set cngfw snippet-snapshots load` | global | `cngfw_snippet_snapshots_load_write` | POST https://api.strata.paloaltonetworks.com/config/setup/v1/snippet-snapshots:load |
| `set cngfw snippet-snapshots publish` | global | `cngfw_snippet_snapshots_publish_write` | POST https://api.strata.paloaltonetworks.com/config/setup/v1/snippet-snapshots:publish |
| `set cngfw snippet-snapshots updates` | global | `cngfw_snippet_snapshots_updates_write` | POST https://api.strata.paloaltonetworks.com/config/setup/v1/snippet-snapshots:updates |
| `set cngfw snippets` | global | `cngfw_snippets_write` | POST https://api.strata.paloaltonetworks.com/config/setup/v1/snippets |
| `set cngfw ssl-decryption-settings` | global | `cngfw_ssl_decryption_settings_write` | POST https://api.strata.paloaltonetworks.com/config/security/v1/ssl-decryption-settings |
| `set cngfw subscribed-tenants` | global | `cngfw_subscribed_tenants_write` | POST https://api.strata.paloaltonetworks.com/config/setup/v1/subscribed-tenants |
| `set cngfw syslog-server-profiles` | global | `cngfw_syslog_server_profiles_write` | POST https://api.strata.paloaltonetworks.com/config/objects/v1/syslog-server-profiles |
| `set cngfw tacacs-server-profiles` | global | `cngfw_tacacs_server_profiles_write` | POST https://api.strata.paloaltonetworks.com/config/identity/v1/tacacs-server-profiles |
| `set cngfw tags` | global | `cngfw_tags_write` | POST https://api.strata.paloaltonetworks.com/config/objects/v1/tags |
| `set cngfw tls-service-profiles` | global | `cngfw_tls_service_profiles_write` | POST https://api.strata.paloaltonetworks.com/config/identity/v1/tls-service-profiles |
| `set cngfw trust-validations` | global | `cngfw_trust_validations_write` | POST https://api.strata.paloaltonetworks.com/config/setup/v1/trust-validations |
| `set cngfw trusts` | global | `cngfw_trusts_write` | POST https://api.strata.paloaltonetworks.com/config/setup/v1/trusts |
| `set cngfw url-access-profiles` | global | `cngfw_url_access_profiles_write` | POST https://api.strata.paloaltonetworks.com/config/security/v1/url-access-profiles |
| `set cngfw url-admin-override` | global | `cngfw_url_admin_override_write` | POST https://api.strata.paloaltonetworks.com/config/security/v1/url-admin-override |
| `set cngfw url-categories` | global | `cngfw_url_categories_write` | POST https://api.strata.paloaltonetworks.com/config/security/v1/url-categories |
| `set cngfw variables` | global | `cngfw_variables_write` | POST https://api.strata.paloaltonetworks.com/config/setup/v1/variables |
| `set cngfw vuln-profiles` | global | `cngfw_vuln_profiles_write` | POST https://api.strata.paloaltonetworks.com/config/security/v1/vulnerability-protection-profiles |
| `set cngfw vuln-signatures` | global | `cngfw_vuln_signatures_write` | POST https://api.strata.paloaltonetworks.com/config/security/v1/vulnerability-protection-signatures |
| `set cngfw wildfire-profiles` | global | `cngfw_wildfire_profiles_write` | POST https://api.strata.paloaltonetworks.com/config/security/v1/wildfire-anti-virus-profiles |
| `show cngfw address-groups` | global | `cngfw_address_groups_read` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/address-groups |
| `show cngfw address-groups id` | global | `cngfw_address_groups_read` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/address-groups/{id} |
| `show cngfw addresses` | global | `cngfw_addresses_read` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/addresses |
| `show cngfw addresses id` | global | `cngfw_addresses_read` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/addresses/{id} |
| `show cngfw adv-device-objs` | global | `cngfw_adv_device_objs_read` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/advanced-device-objects |
| `show cngfw adv-device-objs id` | global | `cngfw_adv_device_objs_read` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/advanced-device-objects/{id} |
| `show cngfw anti-spyware-profiles` | global | `cngfw_anti_spyware_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/anti-spyware-profiles |
| `show cngfw anti-spyware-profiles id` | global | `cngfw_anti_spyware_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/anti-spyware-profiles/{id} |
| `show cngfw anti-spyware-signatures` | global | `cngfw_anti_spyware_signatures_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/anti-spyware-signatures |
| `show cngfw anti-spyware-signatures id` | global | `cngfw_anti_spyware_signatures_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/anti-spyware-signatures/{id} |
| `show cngfw app-override-rules` | global | `cngfw_app_override_rules_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/app-override-rules |
| `show cngfw app-override-rules id` | global | `cngfw_app_override_rules_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/app-override-rules/{id} |
| `show cngfw application-filters` | global | `cngfw_application_filters_read` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/application-filters |
| `show cngfw application-filters id` | global | `cngfw_application_filters_read` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/application-filters/{id} |
| `show cngfw application-groups` | global | `cngfw_application_groups_read` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/application-groups |
| `show cngfw application-groups id` | global | `cngfw_application_groups_read` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/application-groups/{id} |
| `show cngfw applications` | global | `cngfw_applications_read` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/applications |
| `show cngfw applications id` | global | `cngfw_applications_read` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/applications/{id} |
| `show cngfw authentication-portals` | global | `cngfw_authentication_portals_read` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/authentication-portals |
| `show cngfw authentication-portals id` | global | `cngfw_authentication_portals_read` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/authentication-portals/{id} |
| `show cngfw authentication-profiles` | global | `cngfw_authentication_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/authentication-profiles |
| `show cngfw authentication-profiles id` | global | `cngfw_authentication_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/authentication-profiles/{id} |
| `show cngfw authentication-rules` | global | `cngfw_authentication_rules_read` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/authentication-rules |
| `show cngfw authentication-rules id` | global | `cngfw_authentication_rules_read` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/authentication-rules/{id} |
| `show cngfw authentication-sequences` | global | `cngfw_authentication_sequences_read` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/authentication-sequences |
| `show cngfw authentication-sequences id` | global | `cngfw_authentication_sequences_read` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/authentication-sequences/{id} |
| `show cngfw auto-tag-actions` | global | `cngfw_auto_tag_actions_read` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/auto-tag-actions |
| `show cngfw certificate-profiles` | global | `cngfw_certificate_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/certificate-profiles |
| `show cngfw certificate-profiles id` | global | `cngfw_certificate_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/certificate-profiles/{id} |
| `show cngfw certs` | global | `cngfw_certs_read` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/certificates |
| `show cngfw certs id` | global | `cngfw_certs_read` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/certificates/{id} |
| `show cngfw config-versions` | global | `cngfw_config_versions_read` | GET https://api.strata.paloaltonetworks.com/config/operations/v1/config-versions |
| `show cngfw config-versions id` | global | `cngfw_config_versions_read` | GET https://api.strata.paloaltonetworks.com/config/operations/v1/config-versions/{version} |
| `show cngfw config-versions running` | global | `cngfw_config_versions_running_read` | GET https://api.strata.paloaltonetworks.com/config/operations/v1/config-versions/running |
| `show cngfw data-filtering-profiles` | global | `cngfw_data_filtering_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/data-filtering-profiles |
| `show cngfw data-filtering-profiles id` | global | `cngfw_data_filtering_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/data-filtering-profiles/{id} |
| `show cngfw data-objects` | global | `cngfw_data_objects_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/data-objects |
| `show cngfw data-objects id` | global | `cngfw_data_objects_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/data-objects/{id} |
| `show cngfw decryption-exclusions` | global | `cngfw_decryption_exclusions_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/decryption-exclusions |
| `show cngfw decryption-exclusions id` | global | `cngfw_decryption_exclusions_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/decryption-exclusions/{id} |
| `show cngfw decryption-profiles` | global | `cngfw_decryption_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/decryption-profiles |
| `show cngfw decryption-profiles id` | global | `cngfw_decryption_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/decryption-profiles/{id} |
| `show cngfw decryption-rules` | global | `cngfw_decryption_rules_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/decryption-rules |
| `show cngfw decryption-rules id` | global | `cngfw_decryption_rules_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/decryption-rules/{id} |
| `show cngfw device-contexts` | global | `cngfw_device_contexts_read` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/device-context-segments |
| `show cngfw device-contexts id` | global | `cngfw_device_contexts_read` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/device-context-segments/{id} |
| `show cngfw devices` | global | `cngfw_devices_read` | GET https://api.strata.paloaltonetworks.com/config/setup/v1/devices |
| `show cngfw devices id` | global | `cngfw_devices_read` | GET https://api.strata.paloaltonetworks.com/config/setup/v1/devices/{id} |
| `show cngfw dns-security-profiles` | global | `cngfw_dns_security_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/dns-security-profiles |
| `show cngfw dns-security-profiles id` | global | `cngfw_dns_security_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/dns-security-profiles/{id} |
| `show cngfw dos-protection-profiles` | global | `cngfw_dos_protection_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/dos-protection-profiles |
| `show cngfw dos-protection-profiles id` | global | `cngfw_dos_protection_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/dos-protection-profiles/{id} |
| `show cngfw dos-protection-rules` | global | `cngfw_dos_protection_rules_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/dos-protection-rules |
| `show cngfw dos-protection-rules id` | global | `cngfw_dos_protection_rules_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/dos-protection-rules/{id} |
| `show cngfw dynamic-user-groups` | global | `cngfw_dynamic_user_groups_read` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/dynamic-user-groups |
| `show cngfw dynamic-user-groups id` | global | `cngfw_dynamic_user_groups_read` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/dynamic-user-groups/{id} |
| `show cngfw external-dynamic-lists` | global | `cngfw_external_dynamic_lists_read` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/external-dynamic-lists |
| `show cngfw external-dynamic-lists id` | global | `cngfw_external_dynamic_lists_read` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/external-dynamic-lists/{id} |
| `show cngfw file-blocking-profiles` | global | `cngfw_file_blocking_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/file-blocking-profiles |
| `show cngfw file-blocking-profiles id` | global | `cngfw_file_blocking_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/file-blocking-profiles/{id} |
| `show cngfw folders` | global | `cngfw_folders_read` | GET https://api.strata.paloaltonetworks.com/config/setup/v1/folders |
| `show cngfw folders id` | global | `cngfw_folders_read` | GET https://api.strata.paloaltonetworks.com/config/setup/v1/folders/{id} |
| `show cngfw hip-objects` | global | `cngfw_hip_objects_read` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/hip-objects |
| `show cngfw hip-objects id` | global | `cngfw_hip_objects_read` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/hip-objects/{id} |
| `show cngfw hip-profiles` | global | `cngfw_hip_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/hip-profiles |
| `show cngfw hip-profiles id` | global | `cngfw_hip_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/hip-profiles/{id} |
| `show cngfw http-header-profiles` | global | `cngfw_http_header_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/http-header-profiles |
| `show cngfw http-header-profiles id` | global | `cngfw_http_header_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/http-header-profiles/{id} |
| `show cngfw http-server-profiles` | global | `cngfw_http_server_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/http-server-profiles |
| `show cngfw http-server-profiles id` | global | `cngfw_http_server_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/http-server-profiles/{id} |
| `show cngfw jobs` | global | `cngfw_jobs_read` | GET https://api.strata.paloaltonetworks.com/config/operations/v1/jobs |
| `show cngfw jobs id` | global | `cngfw_jobs_read` | GET https://api.strata.paloaltonetworks.com/config/operations/v1/jobs/{id} |
| `show cngfw kerberos-server-profiles` | global | `cngfw_kerberos_server_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/kerberos-server-profiles |
| `show cngfw kerberos-server-profiles id` | global | `cngfw_kerberos_server_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/kerberos-server-profiles/{id} |
| `show cngfw labels` | global | `cngfw_labels_read` | GET https://api.strata.paloaltonetworks.com/config/setup/v1/labels |
| `show cngfw labels id` | global | `cngfw_labels_read` | GET https://api.strata.paloaltonetworks.com/config/setup/v1/labels/{id} |
| `show cngfw ldap-server-profiles` | global | `cngfw_ldap_server_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/ldap-server-profiles |
| `show cngfw ldap-server-profiles id` | global | `cngfw_ldap_server_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/ldap-server-profiles/{id} |
| `show cngfw local-user-groups` | global | `cngfw_local_user_groups_read` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/local-user-groups |
| `show cngfw local-user-groups id` | global | `cngfw_local_user_groups_read` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/local-user-groups/{id} |
| `show cngfw local-users` | global | `cngfw_local_users_read` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/local-users |
| `show cngfw local-users id` | global | `cngfw_local_users_read` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/local-users/{id} |
| `show cngfw log-forwarding-profiles` | global | `cngfw_log_forwarding_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/log-forwarding-profiles |
| `show cngfw log-forwarding-profiles id` | global | `cngfw_log_forwarding_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/log-forwarding-profiles/{id} |
| `show cngfw mfa-servers` | global | `cngfw_mfa_servers_read` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/mfa-servers |
| `show cngfw mfa-servers id` | global | `cngfw_mfa_servers_read` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/mfa-servers/{id} |
| `show cngfw ocsp-responders` | global | `cngfw_ocsp_responders_read` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/ocsp-responders |
| `show cngfw ocsp-responders id` | global | `cngfw_ocsp_responders_read` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/ocsp-responders/{id} |
| `show cngfw onboarding-rules` | global | `cngfw_onboarding_rules_read` | GET https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1/onboarding-rules |
| `show cngfw onboarding-rules id` | global | `cngfw_onboarding_rules_read` | GET https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1/onboarding-rules/{id} |
| `show cngfw profile-groups` | global | `cngfw_profile_groups_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/profile-groups |
| `show cngfw profile-groups id` | global | `cngfw_profile_groups_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/profile-groups/{id} |
| `show cngfw properties` | global | `cngfw_properties_read` | GET https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1/properties |
| `show cngfw properties id` | global | `cngfw_properties_read` | GET https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1/properties/{id} |
| `show cngfw quarantined-devices` | global | `cngfw_quarantined_devices_read` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/quarantined-devices |
| `show cngfw radius-server-profiles` | global | `cngfw_radius_server_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/radius-server-profiles |
| `show cngfw radius-server-profiles id` | global | `cngfw_radius_server_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/radius-server-profiles/{id} |
| `show cngfw regions` | global | `cngfw_regions_read` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/regions |
| `show cngfw regions id` | global | `cngfw_regions_read` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/regions/{id} |
| `show cngfw saas-tenant-restrictions` | global | `cngfw_saas_tenant_restrictions_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/saas-tenant-restrictions |
| `show cngfw saml-server-profiles` | global | `cngfw_saml_server_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/saml-server-profiles |
| `show cngfw saml-server-profiles id` | global | `cngfw_saml_server_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/saml-server-profiles/{id} |
| `show cngfw scep-profiles` | global | `cngfw_scep_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/scep-profiles |
| `show cngfw scep-profiles id` | global | `cngfw_scep_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/scep-profiles/{id} |
| `show cngfw schedules` | global | `cngfw_schedules_read` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/schedules |
| `show cngfw schedules id` | global | `cngfw_schedules_read` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/schedules/{id} |
| `show cngfw security-rules` | global | `cngfw_security_rules_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/security-rules |
| `show cngfw security-rules id` | global | `cngfw_security_rules_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/security-rules/{id} |
| `show cngfw service-groups` | global | `cngfw_service_groups_read` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/service-groups |
| `show cngfw service-groups id` | global | `cngfw_service_groups_read` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/service-groups/{id} |
| `show cngfw services` | global | `cngfw_services_read` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/services |
| `show cngfw services id` | global | `cngfw_services_read` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/services/{id} |
| `show cngfw shared-snippets` | global | `cngfw_shared_snippets_read` | GET https://api.strata.paloaltonetworks.com/config/setup/v1/shared-snippets |
| `show cngfw site-groups` | global | `cngfw_site_groups_read` | GET https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1/site-groups |
| `show cngfw site-groups id` | global | `cngfw_site_groups_read` | GET https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1/site-groups/{id} |
| `show cngfw sites` | global | `cngfw_sites_read` | GET https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1/sites |
| `show cngfw sites id` | global | `cngfw_sites_read` | GET https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1/sites/{id} |
| `show cngfw snippet-audit-logs id` | global | `cngfw_snippet_audit_logs_read` | GET https://api.strata.paloaltonetworks.com/config/setup/v1/snippet-audit-logs/{id} |
| `show cngfw snippet-categories` | global | `cngfw_snippet_categories_read` | GET https://api.strata.paloaltonetworks.com/config/setup/v1/snippet-categories |
| `show cngfw snippet-categories id` | global | `cngfw_snippet_categories_read` | GET https://api.strata.paloaltonetworks.com/config/setup/v1/snippet-categories/{id} |
| `show cngfw snippets` | global | `cngfw_snippets_read` | GET https://api.strata.paloaltonetworks.com/config/setup/v1/snippets |
| `show cngfw snippets id` | global | `cngfw_snippets_read` | GET https://api.strata.paloaltonetworks.com/config/setup/v1/snippets/{id} |
| `show cngfw ssl-decryption-settings` | global | `cngfw_ssl_decryption_settings_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/ssl-decryption-settings |
| `show cngfw subscribed-tenants id` | global | `cngfw_subscribed_tenants_read` | GET https://api.strata.paloaltonetworks.com/config/setup/v1/subscribed-tenants/{id} |
| `show cngfw syslog-server-profiles` | global | `cngfw_syslog_server_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/syslog-server-profiles |
| `show cngfw syslog-server-profiles id` | global | `cngfw_syslog_server_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/syslog-server-profiles/{id} |
| `show cngfw tacacs-server-profiles` | global | `cngfw_tacacs_server_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/tacacs-server-profiles |
| `show cngfw tacacs-server-profiles id` | global | `cngfw_tacacs_server_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/tacacs-server-profiles/{id} |
| `show cngfw tags` | global | `cngfw_tags_read` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/tags |
| `show cngfw tags id` | global | `cngfw_tags_read` | GET https://api.strata.paloaltonetworks.com/config/objects/v1/tags/{id} |
| `show cngfw tls-service-profiles` | global | `cngfw_tls_service_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/tls-service-profiles |
| `show cngfw tls-service-profiles id` | global | `cngfw_tls_service_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/tls-service-profiles/{id} |
| `show cngfw trusted-cas` | global | `cngfw_trusted_cas_read` | GET https://api.strata.paloaltonetworks.com/config/identity/v1/trusted-certificate-authorities |
| `show cngfw trusted-tenant-overview` | global | `cngfw_trusted_tenant_overview_read` | GET https://api.strata.paloaltonetworks.com/config/setup/v1/trusted-tenant-overview |
| `show cngfw trusted-tenants` | global | `cngfw_trusted_tenants_read` | GET https://api.strata.paloaltonetworks.com/config/setup/v1/trusted-tenants |
| `show cngfw url-access-profiles` | global | `cngfw_url_access_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/url-access-profiles |
| `show cngfw url-access-profiles id` | global | `cngfw_url_access_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/url-access-profiles/{id} |
| `show cngfw url-admin-override` | global | `cngfw_url_admin_override_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/url-admin-override |
| `show cngfw url-categories` | global | `cngfw_url_categories_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/url-categories |
| `show cngfw url-categories id` | global | `cngfw_url_categories_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/url-categories/{id} |
| `show cngfw url-filtering-categories` | global | `cngfw_url_filtering_categories_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/url-filtering-categories |
| `show cngfw variables` | global | `cngfw_variables_read` | GET https://api.strata.paloaltonetworks.com/config/setup/v1/variables |
| `show cngfw variables id` | global | `cngfw_variables_read` | GET https://api.strata.paloaltonetworks.com/config/setup/v1/variables/{id} |
| `show cngfw vuln-profiles` | global | `cngfw_vuln_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/vulnerability-protection-profiles |
| `show cngfw vuln-profiles id` | global | `cngfw_vuln_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/vulnerability-protection-profiles/{id} |
| `show cngfw vuln-signatures` | global | `cngfw_vuln_signatures_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/vulnerability-protection-signatures |
| `show cngfw vuln-signatures id` | global | `cngfw_vuln_signatures_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/vulnerability-protection-signatures/{id} |
| `show cngfw wildfire-profiles` | global | `cngfw_wildfire_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/wildfire-anti-virus-profiles |
| `show cngfw wildfire-profiles id` | global | `cngfw_wildfire_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/security/v1/wildfire-anti-virus-profiles/{id} |
| `update cngfw address-groups` | global | `cngfw_address_groups_write` | PUT https://api.strata.paloaltonetworks.com/config/objects/v1/address-groups/{id} |
| `update cngfw addresses` | global | `cngfw_addresses_write` | PUT https://api.strata.paloaltonetworks.com/config/objects/v1/addresses/{id} |
| `update cngfw adv-device-objs` | global | `cngfw_adv_device_objs_write` | PUT https://api.strata.paloaltonetworks.com/config/objects/v1/advanced-device-objects |
| `update cngfw adv-device-objs id` | global | `cngfw_adv_device_objs_write` | PUT https://api.strata.paloaltonetworks.com/config/objects/v1/advanced-device-objects/{id} |
| `update cngfw anti-spyware-profiles` | global | `cngfw_anti_spyware_profiles_write` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/anti-spyware-profiles/{id} |
| `update cngfw anti-spyware-signatures` | global | `cngfw_anti_spyware_signatures_write` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/anti-spyware-signatures/{id} |
| `update cngfw app-override-rules` | global | `cngfw_app_override_rules_write` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/app-override-rules/{id} |
| `update cngfw application-filters` | global | `cngfw_application_filters_write` | PUT https://api.strata.paloaltonetworks.com/config/objects/v1/application-filters/{id} |
| `update cngfw application-groups` | global | `cngfw_application_groups_write` | PUT https://api.strata.paloaltonetworks.com/config/objects/v1/application-groups/{id} |
| `update cngfw applications` | global | `cngfw_applications_write` | PUT https://api.strata.paloaltonetworks.com/config/objects/v1/applications/{id} |
| `update cngfw authentication-portals` | global | `cngfw_authentication_portals_write` | PUT https://api.strata.paloaltonetworks.com/config/identity/v1/authentication-portals/{id} |
| `update cngfw authentication-profiles` | global | `cngfw_authentication_profiles_write` | PUT https://api.strata.paloaltonetworks.com/config/identity/v1/authentication-profiles/{id} |
| `update cngfw authentication-rules` | global | `cngfw_authentication_rules_write` | PUT https://api.strata.paloaltonetworks.com/config/identity/v1/authentication-rules/{id} |
| `update cngfw authentication-sequences` | global | `cngfw_authentication_sequences_write` | PUT https://api.strata.paloaltonetworks.com/config/identity/v1/authentication-sequences/{id} |
| `update cngfw auto-tag-actions` | global | `cngfw_auto_tag_actions_write` | PUT https://api.strata.paloaltonetworks.com/config/objects/v1/auto-tag-actions |
| `update cngfw certificate-profiles` | global | `cngfw_certificate_profiles_write` | PUT https://api.strata.paloaltonetworks.com/config/identity/v1/certificate-profiles/{id} |
| `update cngfw data-filtering-profiles` | global | `cngfw_data_filtering_profiles_write` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/data-filtering-profiles/{id} |
| `update cngfw data-objects` | global | `cngfw_data_objects_write` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/data-objects/{id} |
| `update cngfw decryption-exclusions` | global | `cngfw_decryption_exclusions_write` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/decryption-exclusions/{id} |
| `update cngfw decryption-profiles` | global | `cngfw_decryption_profiles_write` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/decryption-profiles/{id} |
| `update cngfw decryption-rules` | global | `cngfw_decryption_rules_write` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/decryption-rules/{id} |
| `update cngfw device-contexts` | global | `cngfw_device_contexts_write` | PUT https://api.strata.paloaltonetworks.com/config/objects/v1/device-context-segments/{id} |
| `update cngfw devices` | global | `cngfw_devices_write` | PUT https://api.strata.paloaltonetworks.com/config/setup/v1/devices/{id} |
| `update cngfw dns-security-profiles` | global | `cngfw_dns_security_profiles_write` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/dns-security-profiles/{id} |
| `update cngfw dos-protection-profiles` | global | `cngfw_dos_protection_profiles_write` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/dos-protection-profiles/{id} |
| `update cngfw dos-protection-rules` | global | `cngfw_dos_protection_rules_write` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/dos-protection-rules/{id} |
| `update cngfw dynamic-user-groups` | global | `cngfw_dynamic_user_groups_write` | PUT https://api.strata.paloaltonetworks.com/config/objects/v1/dynamic-user-groups/{id} |
| `update cngfw external-dynamic-lists` | global | `cngfw_external_dynamic_lists_write` | PUT https://api.strata.paloaltonetworks.com/config/objects/v1/external-dynamic-lists/{id} |
| `update cngfw file-blocking-profiles` | global | `cngfw_file_blocking_profiles_write` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/file-blocking-profiles/{id} |
| `update cngfw folders` | global | `cngfw_folders_write` | PUT https://api.strata.paloaltonetworks.com/config/setup/v1/folders/{id} |
| `update cngfw hip-objects` | global | `cngfw_hip_objects_write` | PUT https://api.strata.paloaltonetworks.com/config/objects/v1/hip-objects/{id} |
| `update cngfw hip-profiles` | global | `cngfw_hip_profiles_write` | PUT https://api.strata.paloaltonetworks.com/config/objects/v1/hip-profiles/{id} |
| `update cngfw http-header-profiles` | global | `cngfw_http_header_profiles_write` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/http-header-profiles/{id} |
| `update cngfw http-server-profiles` | global | `cngfw_http_server_profiles_write` | PUT https://api.strata.paloaltonetworks.com/config/objects/v1/http-server-profiles/{id} |
| `update cngfw kerberos-server-profiles` | global | `cngfw_kerberos_server_profiles_write` | PUT https://api.strata.paloaltonetworks.com/config/identity/v1/kerberos-server-profiles/{id} |
| `update cngfw labels` | global | `cngfw_labels_write` | PUT https://api.strata.paloaltonetworks.com/config/setup/v1/labels/{id} |
| `update cngfw ldap-server-profiles` | global | `cngfw_ldap_server_profiles_write` | PUT https://api.strata.paloaltonetworks.com/config/identity/v1/ldap-server-profiles/{id} |
| `update cngfw local-user-groups` | global | `cngfw_local_user_groups_write` | PUT https://api.strata.paloaltonetworks.com/config/identity/v1/local-user-groups/{id} |
| `update cngfw local-users` | global | `cngfw_local_users_write` | PUT https://api.strata.paloaltonetworks.com/config/identity/v1/local-users/{id} |
| `update cngfw log-forwarding-profiles` | global | `cngfw_log_forwarding_profiles_write` | PUT https://api.strata.paloaltonetworks.com/config/objects/v1/log-forwarding-profiles/{id} |
| `update cngfw mfa-servers` | global | `cngfw_mfa_servers_write` | PUT https://api.strata.paloaltonetworks.com/config/identity/v1/mfa-servers/{id} |
| `update cngfw ocsp-responders` | global | `cngfw_ocsp_responders_write` | PUT https://api.strata.paloaltonetworks.com/config/identity/v1/ocsp-responders/{id} |
| `update cngfw onboarding-rules` | global | `cngfw_onboarding_rules_write` | PUT https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1/onboarding-rules/{id} |
| `update cngfw profile-groups` | global | `cngfw_profile_groups_write` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/profile-groups/{id} |
| `update cngfw properties` | global | `cngfw_properties_write` | PUT https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1/properties/{id} |
| `update cngfw radius-server-profiles` | global | `cngfw_radius_server_profiles_write` | PUT https://api.strata.paloaltonetworks.com/config/identity/v1/radius-server-profiles/{id} |
| `update cngfw regions` | global | `cngfw_regions_write` | PUT https://api.strata.paloaltonetworks.com/config/objects/v1/regions/{id} |
| `update cngfw saas-tenant-restrictions` | global | `cngfw_saas_tenant_restrictions_write` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/saas-tenant-restrictions |
| `update cngfw saml-server-profiles` | global | `cngfw_saml_server_profiles_write` | PUT https://api.strata.paloaltonetworks.com/config/identity/v1/saml-server-profiles/{id} |
| `update cngfw scep-profiles` | global | `cngfw_scep_profiles_write` | PUT https://api.strata.paloaltonetworks.com/config/identity/v1/scep-profiles/{id} |
| `update cngfw schedules` | global | `cngfw_schedules_write` | PUT https://api.strata.paloaltonetworks.com/config/objects/v1/schedules/{id} |
| `update cngfw security-rules` | global | `cngfw_security_rules_write` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/security-rules/{id} |
| `update cngfw service-groups` | global | `cngfw_service_groups_write` | PUT https://api.strata.paloaltonetworks.com/config/objects/v1/service-groups/{id} |
| `update cngfw services` | global | `cngfw_services_write` | PUT https://api.strata.paloaltonetworks.com/config/objects/v1/services/{id} |
| `update cngfw shared-snippets` | global | `cngfw_shared_snippets_write` | PUT https://api.strata.paloaltonetworks.com/config/setup/v1/shared-snippets |
| `update cngfw site-groups` | global | `cngfw_site_groups_write` | PUT https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1/site-groups/{id} |
| `update cngfw sites` | global | `cngfw_sites_write` | PUT https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1/sites/{id} |
| `update cngfw snippets` | global | `cngfw_snippets_write` | PUT https://api.strata.paloaltonetworks.com/config/setup/v1/snippets/{id} |
| `update cngfw ssl-decryption-settings` | global | `cngfw_ssl_decryption_settings_write` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/ssl-decryption-settings |
| `update cngfw subscribed-tenants` | global | `cngfw_subscribed_tenants_write` | PUT https://api.strata.paloaltonetworks.com/config/setup/v1/subscribed-tenants |
| `update cngfw syslog-server-profiles` | global | `cngfw_syslog_server_profiles_write` | PUT https://api.strata.paloaltonetworks.com/config/objects/v1/syslog-server-profiles/{id} |
| `update cngfw tacacs-server-profiles` | global | `cngfw_tacacs_server_profiles_write` | PUT https://api.strata.paloaltonetworks.com/config/identity/v1/tacacs-server-profiles/{id} |
| `update cngfw tags` | global | `cngfw_tags_write` | PUT https://api.strata.paloaltonetworks.com/config/objects/v1/tags/{id} |
| `update cngfw tls-service-profiles` | global | `cngfw_tls_service_profiles_write` | PUT https://api.strata.paloaltonetworks.com/config/identity/v1/tls-service-profiles/{id} |
| `update cngfw url-access-profiles` | global | `cngfw_url_access_profiles_write` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/url-access-profiles/{id} |
| `update cngfw url-categories` | global | `cngfw_url_categories_write` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/url-categories/{id} |
| `update cngfw variables` | global | `cngfw_variables_write` | PUT https://api.strata.paloaltonetworks.com/config/setup/v1/variables/{id} |
| `update cngfw vuln-profiles` | global | `cngfw_vuln_profiles_write` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/vulnerability-protection-profiles/{id} |
| `update cngfw vuln-signatures` | global | `cngfw_vuln_signatures_write` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/vulnerability-protection-signatures/{id} |
| `update cngfw wildfire-profiles` | global | `cngfw_wildfire_profiles_write` | PUT https://api.strata.paloaltonetworks.com/config/security/v1/wildfire-anti-virus-profiles/{id} |

## Device-Device-Settings

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `delete authentication-settings` | global | `authentication_settings_write` | DELETE https://api.strata.paloaltonetworks.com/config/device/v1/authentication-settings/{id} |
| `delete autoscale` | global | `autoscale_write` | DELETE https://api.strata.paloaltonetworks.com/config/device/v1/autoscale |
| `delete content-cloud-settings` | global | `content_cloud_settings_write` | DELETE https://api.strata.paloaltonetworks.com/config/device/v1/content-cloud-settings/{id} |
| `delete content-id-settings` | global | `content_id_settings_write` | DELETE https://api.strata.paloaltonetworks.com/config/device/v1/content-id-settings/{id} |
| `delete device-context-segment-association` | global | `device_context_segment_association_write` | DELETE https://api.strata.paloaltonetworks.com/config/device/v1/device-context-segment-association |
| `delete device-context-segment-association id` | global | `device_context_segment_association_write` | DELETE https://api.strata.paloaltonetworks.com/config/device/v1/device-context-segment-association/{id} |
| `delete device-redistribution-collector` | global | `device_redistribution_collector_write` | DELETE https://api.strata.paloaltonetworks.com/config/device/v1/device-redistribution-collector/{id} |
| `delete general-settings` | global | `general_settings_write` | DELETE https://api.strata.paloaltonetworks.com/config/device/v1/general-settings/{id} |
| `delete ha-configurations` | global | `ha_configurations_write` | DELETE https://api.strata.paloaltonetworks.com/config/device/v1/ha-configurations |
| `delete management-interface` | global | `management_interface_write` | DELETE https://api.strata.paloaltonetworks.com/config/device/v1/management-interface/{id} |
| `delete motd-banner-settings` | global | `motd_banner_settings_write` | DELETE https://api.strata.paloaltonetworks.com/config/device/v1/motd-banner-settings/{id} |
| `delete service-route` | global | `service_route_write` | DELETE https://api.strata.paloaltonetworks.com/config/device/v1/service-route/{id} |
| `delete service-settings` | global | `service_settings_write` | DELETE https://api.strata.paloaltonetworks.com/config/device/v1/service-settings/{id} |
| `delete session-settings` | global | `session_settings_write` | DELETE https://api.strata.paloaltonetworks.com/config/device/v1/session-settings/{id} |
| `delete session-timeouts` | global | `session_timeouts_write` | DELETE https://api.strata.paloaltonetworks.com/config/device/v1/session-timeouts/{id} |
| `delete tcp-settings` | global | `tcp_settings_write` | DELETE https://api.strata.paloaltonetworks.com/config/device/v1/tcp-settings/{id} |
| `delete update-schedule` | global | `update_schedule_write` | DELETE https://api.strata.paloaltonetworks.com/config/device/v1/update-schedule/{id} |
| `delete vpn-settings` | global | `vpn_settings_write` | DELETE https://api.strata.paloaltonetworks.com/config/device/v1/vpn-settings/{id} |
| `set authentication-settings` | global | `authentication_settings_write` | POST https://api.strata.paloaltonetworks.com/config/device/v1/authentication-settings |
| `set autoscale` | global | `autoscale_write` | POST https://api.strata.paloaltonetworks.com/config/device/v1/autoscale |
| `set content-cloud-settings` | global | `content_cloud_settings_write` | POST https://api.strata.paloaltonetworks.com/config/device/v1/content-cloud-settings |
| `set content-id-settings` | global | `content_id_settings_write` | POST https://api.strata.paloaltonetworks.com/config/device/v1/content-id-settings |
| `set device-context-segment-association` | global | `device_context_segment_association_write` | POST https://api.strata.paloaltonetworks.com/config/device/v1/device-context-segment-association |
| `set device-redistribution-collector` | global | `device_redistribution_collector_write` | POST https://api.strata.paloaltonetworks.com/config/device/v1/device-redistribution-collector |
| `set general-settings` | global | `general_settings_write` | POST https://api.strata.paloaltonetworks.com/config/device/v1/general-settings |
| `set ha-configurations` | global | `ha_configurations_write` | POST https://api.strata.paloaltonetworks.com/config/device/v1/ha-configurations |
| `set management-interface` | global | `management_interface_write` | POST https://api.strata.paloaltonetworks.com/config/device/v1/management-interface |
| `set motd-banner-settings` | global | `motd_banner_settings_write` | POST https://api.strata.paloaltonetworks.com/config/device/v1/motd-banner-settings |
| `set service-route` | global | `service_route_write` | POST https://api.strata.paloaltonetworks.com/config/device/v1/service-route |
| `set service-settings` | global | `service_settings_write` | POST https://api.strata.paloaltonetworks.com/config/device/v1/service-settings |
| `set session-settings` | global | `session_settings_write` | POST https://api.strata.paloaltonetworks.com/config/device/v1/session-settings |
| `set session-timeouts` | global | `session_timeouts_write` | POST https://api.strata.paloaltonetworks.com/config/device/v1/session-timeouts |
| `set tcp-settings` | global | `tcp_settings_write` | POST https://api.strata.paloaltonetworks.com/config/device/v1/tcp-settings |
| `set update-schedule` | global | `update_schedule_write` | POST https://api.strata.paloaltonetworks.com/config/device/v1/update-schedule |
| `set vpn-settings` | global | `vpn_settings_write` | POST https://api.strata.paloaltonetworks.com/config/device/v1/vpn-settings |
| `show authentication-settings` | global | `authentication_settings_read` | GET https://api.strata.paloaltonetworks.com/config/device/v1/authentication-settings |
| `show authentication-settings id` | global | `authentication_settings_read` | GET https://api.strata.paloaltonetworks.com/config/device/v1/authentication-settings/{id} |
| `show autoscale` | global | `autoscale_read` | GET https://api.strata.paloaltonetworks.com/config/device/v1/autoscale |
| `show content-cloud-settings` | global | `content_cloud_settings_read` | GET https://api.strata.paloaltonetworks.com/config/device/v1/content-cloud-settings |
| `show content-cloud-settings id` | global | `content_cloud_settings_read` | GET https://api.strata.paloaltonetworks.com/config/device/v1/content-cloud-settings/{id} |
| `show content-id-settings` | global | `content_id_settings_read` | GET https://api.strata.paloaltonetworks.com/config/device/v1/content-id-settings |
| `show content-id-settings id` | global | `content_id_settings_read` | GET https://api.strata.paloaltonetworks.com/config/device/v1/content-id-settings/{id} |
| `show device-context-segment-association` | global | `device_context_segment_association_read` | GET https://api.strata.paloaltonetworks.com/config/device/v1/device-context-segment-association |
| `show device-context-segment-association id` | global | `device_context_segment_association_read` | GET https://api.strata.paloaltonetworks.com/config/device/v1/device-context-segment-association/{id} |
| `show device-redistribution-collector` | global | `device_redistribution_collector_read` | GET https://api.strata.paloaltonetworks.com/config/device/v1/device-redistribution-collector |
| `show device-redistribution-collector id` | global | `device_redistribution_collector_read` | GET https://api.strata.paloaltonetworks.com/config/device/v1/device-redistribution-collector/{id} |
| `show general-settings` | global | `general_settings_read` | GET https://api.strata.paloaltonetworks.com/config/device/v1/general-settings |
| `show general-settings id` | global | `general_settings_read` | GET https://api.strata.paloaltonetworks.com/config/device/v1/general-settings/{id} |
| `show ha-configurations` | global | `ha_configurations_read` | GET https://api.strata.paloaltonetworks.com/config/device/v1/ha-configurations |
| `show ha-configurations-gateways` | global | `ha_configurations_gateways_read` | GET https://api.strata.paloaltonetworks.com/config/device/v1/ha-configurations-gateways |
| `show ha-configurations-ip-addresses` | global | `ha_configurations_ip_addresses_read` | GET https://api.strata.paloaltonetworks.com/config/device/v1/ha-configurations-ip-addresses |
| `show ha-configurations-netmasks` | global | `ha_configurations_netmasks_read` | GET https://api.strata.paloaltonetworks.com/config/device/v1/ha-configurations-netmasks |
| `show ha-configurations-ports` | global | `ha_configurations_ports_read` | GET https://api.strata.paloaltonetworks.com/config/device/v1/ha-configurations-ports |
| `show ha-devices` | global | `ha_devices_read` | GET https://api.strata.paloaltonetworks.com/config/device/v1/ha-devices |
| `show management-interface` | global | `management_interface_read` | GET https://api.strata.paloaltonetworks.com/config/device/v1/management-interface |
| `show management-interface id` | global | `management_interface_read` | GET https://api.strata.paloaltonetworks.com/config/device/v1/management-interface/{id} |
| `show motd-banner-settings` | global | `motd_banner_settings_read` | GET https://api.strata.paloaltonetworks.com/config/device/v1/motd-banner-settings |
| `show motd-banner-settings id` | global | `motd_banner_settings_read` | GET https://api.strata.paloaltonetworks.com/config/device/v1/motd-banner-settings/{id} |
| `show service-route` | global | `service_route_read` | GET https://api.strata.paloaltonetworks.com/config/device/v1/service-route |
| `show service-route id` | global | `service_route_read` | GET https://api.strata.paloaltonetworks.com/config/device/v1/service-route/{id} |
| `show service-settings` | global | `service_settings_read` | GET https://api.strata.paloaltonetworks.com/config/device/v1/service-settings |
| `show service-settings id` | global | `service_settings_read` | GET https://api.strata.paloaltonetworks.com/config/device/v1/service-settings/{id} |
| `show session-settings` | global | `session_settings_read` | GET https://api.strata.paloaltonetworks.com/config/device/v1/session-settings |
| `show session-settings id` | global | `session_settings_read` | GET https://api.strata.paloaltonetworks.com/config/device/v1/session-settings/{id} |
| `show session-timeouts` | global | `session_timeouts_read` | GET https://api.strata.paloaltonetworks.com/config/device/v1/session-timeouts |
| `show session-timeouts id` | global | `session_timeouts_read` | GET https://api.strata.paloaltonetworks.com/config/device/v1/session-timeouts/{id} |
| `show tcp-settings` | global | `tcp_settings_read` | GET https://api.strata.paloaltonetworks.com/config/device/v1/tcp-settings |
| `show tcp-settings id` | global | `tcp_settings_read` | GET https://api.strata.paloaltonetworks.com/config/device/v1/tcp-settings/{id} |
| `show update-schedule` | global | `update_schedule_read` | GET https://api.strata.paloaltonetworks.com/config/device/v1/update-schedule |
| `show update-schedule id` | global | `update_schedule_read` | GET https://api.strata.paloaltonetworks.com/config/device/v1/update-schedule/{id} |
| `show vpn-settings` | global | `vpn_settings_read` | GET https://api.strata.paloaltonetworks.com/config/device/v1/vpn-settings |
| `show vpn-settings id` | global | `vpn_settings_read` | GET https://api.strata.paloaltonetworks.com/config/device/v1/vpn-settings/{id} |
| `update authentication-settings` | global | `authentication_settings_write` | PUT https://api.strata.paloaltonetworks.com/config/device/v1/authentication-settings/{id} |
| `update autoscale` | global | `autoscale_write` | PUT https://api.strata.paloaltonetworks.com/config/device/v1/autoscale |
| `update content-cloud-settings` | global | `content_cloud_settings_write` | PUT https://api.strata.paloaltonetworks.com/config/device/v1/content-cloud-settings/{id} |
| `update content-id-settings` | global | `content_id_settings_write` | PUT https://api.strata.paloaltonetworks.com/config/device/v1/content-id-settings/{id} |
| `update device-context-segment-association` | global | `device_context_segment_association_write` | PUT https://api.strata.paloaltonetworks.com/config/device/v1/device-context-segment-association/{id} |
| `update device-redistribution-collector` | global | `device_redistribution_collector_write` | PUT https://api.strata.paloaltonetworks.com/config/device/v1/device-redistribution-collector/{id} |
| `update general-settings` | global | `general_settings_write` | PUT https://api.strata.paloaltonetworks.com/config/device/v1/general-settings/{id} |
| `update ha-configurations` | global | `ha_configurations_write` | PUT https://api.strata.paloaltonetworks.com/config/device/v1/ha-configurations |
| `update management-interface` | global | `management_interface_write` | PUT https://api.strata.paloaltonetworks.com/config/device/v1/management-interface/{id} |
| `update motd-banner-settings` | global | `motd_banner_settings_write` | PUT https://api.strata.paloaltonetworks.com/config/device/v1/motd-banner-settings/{id} |
| `update service-route` | global | `service_route_write` | PUT https://api.strata.paloaltonetworks.com/config/device/v1/service-route/{id} |
| `update service-settings` | global | `service_settings_write` | PUT https://api.strata.paloaltonetworks.com/config/device/v1/service-settings/{id} |
| `update session-settings` | global | `session_settings_write` | PUT https://api.strata.paloaltonetworks.com/config/device/v1/session-settings/{id} |
| `update session-timeouts` | global | `session_timeouts_write` | PUT https://api.strata.paloaltonetworks.com/config/device/v1/session-timeouts/{id} |
| `update tcp-settings` | global | `tcp_settings_write` | PUT https://api.strata.paloaltonetworks.com/config/device/v1/tcp-settings/{id} |
| `update update-schedule` | global | `update_schedule_write` | PUT https://api.strata.paloaltonetworks.com/config/device/v1/update-schedule/{id} |
| `update vpn-settings` | global | `vpn_settings_write` | PUT https://api.strata.paloaltonetworks.com/config/device/v1/vpn-settings/{id} |

## Diagnostics

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `packet-tracer` | folder | `packet_tracer` | (client-side simulation of the folder rule base) |
| `test security-policy-match` | folder | `packet_tracer` | (client-side simulation of the folder rule base) |

## Iam

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `delete iam access-policies` | global | `iam_access_policies_write` | DELETE https://api.sase.paloaltonetworks.com/iam/v1/access_policies/{id} |
| `delete iam custom-roles` | global | `iam_custom_roles_write` | DELETE https://api.sase.paloaltonetworks.com/iam/v1/custom_roles/{name} |
| `delete service-accounts` | global | `service_accounts_write` | DELETE https://api.sase.paloaltonetworks.com/iam/v1/service_accounts/{id} |
| `set iam access-policies` | global | `iam_access_policies_write` | POST https://api.sase.paloaltonetworks.com/iam/v1/access_policies |
| `set iam custom-roles` | global | `iam_custom_roles_write` | POST https://api.sase.paloaltonetworks.com/iam/v1/custom_roles |
| `set iam sso-users` | global | `iam_sso_users_write` | POST https://api.sase.paloaltonetworks.com/iam/v1/sso_users |
| `set service-accounts` | global | `service_accounts_write` | POST https://api.sase.paloaltonetworks.com/iam/v1/service_accounts |
| `set service-accounts reset` | global | `service_accounts_reset_write` | POST https://api.sase.paloaltonetworks.com/iam/v1/service_accounts/{id}/operations/reset |
| `show iam access-policies` | global | `iam_access_policies_read` | GET https://api.sase.paloaltonetworks.com/iam/v1/access_policies |
| `show iam access-policies id` | global | `iam_access_policies_read` | GET https://api.sase.paloaltonetworks.com/iam/v1/access_policies/{id} |
| `show iam custom-roles` | global | `iam_custom_roles_read` | GET https://api.sase.paloaltonetworks.com/iam/v1/custom_roles |
| `show iam custom-roles id` | global | `iam_custom_roles_read` | GET https://api.sase.paloaltonetworks.com/iam/v1/custom_roles/{name} |
| `show iam permission-sets` | global | `iam_permission_sets_read` | GET https://api.sase.paloaltonetworks.com/iam/v1/permission_sets |
| `show iam permission-sets id` | global | `iam_permission_sets_read` | GET https://api.sase.paloaltonetworks.com/iam/v1/permission_sets/{name} |
| `show iam permissions` | global | `iam_permissions_read` | GET https://api.sase.paloaltonetworks.com/iam/v1/permissions |
| `show iam permissions id` | global | `iam_permissions_read` | GET https://api.sase.paloaltonetworks.com/iam/v1/permissions/{name} |
| `show iam roles` | global | `iam_roles_read` | GET https://api.sase.paloaltonetworks.com/iam/v1/roles |
| `show iam roles id` | global | `iam_roles_read` | GET https://api.sase.paloaltonetworks.com/iam/v1/roles/{name} |
| `show iam sso-users` | global | `iam_sso_users_read` | GET https://api.sase.paloaltonetworks.com/iam/v1/sso_users |
| `show service-accounts` | global | `service_accounts_read` | GET https://api.sase.paloaltonetworks.com/iam/v1/service_accounts |
| `show service-accounts id` | global | `service_accounts_read` | GET https://api.sase.paloaltonetworks.com/iam/v1/service_accounts/{id} |
| `update iam custom-roles` | global | `iam_custom_roles_write` | PUT https://api.sase.paloaltonetworks.com/iam/v1/custom_roles/{name} |
| `update service-accounts` | global | `service_accounts_write` | PUT https://api.sase.paloaltonetworks.com/iam/v1/service_accounts/{id} |

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
| `set incidents incidents search` | global | `incidents_incidents_search_write` | POST https://api.strata.paloaltonetworks.com/incidents/v1/search |
| `show incidents incidents details id` | global | `incidents_incidents_details_read` | GET https://api.strata.paloaltonetworks.com/incidents/v1/details/{incident-id} |

## Network

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `delete aggregate-interfaces` | global | `aggregate_interfaces_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/aggregate-interfaces/{id} |
| `delete auto-vpn-clusters` | global | `auto_vpn_clusters_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/auto-vpn-clusters/{id} |
| `delete bgp-af-profiles` | global | `bgp_af_profiles_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/bgp-address-family-profiles/{id} |
| `delete bgp-auth-profiles` | global | `bgp_auth_profiles_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/bgp-auth-profiles/{id} |
| `delete bgp-filtering-profiles` | global | `bgp_filtering_profiles_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/bgp-filtering-profiles/{id} |
| `delete bgp-redist-profiles` | global | `bgp_redist_profiles_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/bgp-redistribution-profiles/{id} |
| `delete bgp-route-maps` | global | `bgp_route_maps_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/bgp-route-maps/{id} |
| `delete bgp-routemap-redist` | global | `bgp_routemap_redist_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/bgp-route-map-redistributions/{id} |
| `delete config-match-list` | global | `config_match_list_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/config-match-list/{id} |
| `delete dhcp-interfaces` | global | `dhcp_interfaces_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/dhcp-interfaces/{id} |
| `delete dns-proxies` | global | `dns_proxies_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/dns-proxies/{id} |
| `delete ethernet-interfaces` | global | `ethernet_interfaces_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/ethernet-interfaces/{id} |
| `delete gp-match-list` | global | `gp_match_list_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/globalprotect-match-list/{id} |
| `delete hipmatch-match-list` | global | `hipmatch_match_list_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/hipmatch-match-list/{id} |
| `delete if-mgmt-profiles` | global | `if_mgmt_profiles_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/interface-management-profiles/{id} |
| `delete ike-crypto-profiles` | global | `ike_crypto_profiles_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/ike-crypto-profiles/{id} |
| `delete ike-gateways` | global | `ike_gateways_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/ike-gateways/{id} |
| `delete ipsec-crypto-profiles` | global | `ipsec_crypto_profiles_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/ipsec-crypto-profiles/{id} |
| `delete ipsec-tunnels` | global | `ipsec_tunnels_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/ipsec-tunnels/{id} |
| `delete iptag-match-list` | global | `iptag_match_list_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/iptag-match-list/{id} |
| `delete layer2-subinterfaces` | global | `layer2_subinterfaces_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/layer2-subinterfaces/{id} |
| `delete layer3-subinterfaces` | global | `layer3_subinterfaces_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/layer3-subinterfaces/{id} |
| `delete link-tags` | global | `link_tags_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/link-tags/{id} |
| `delete lldp-profiles` | global | `lldp_profiles_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/lldp-profiles/{id} |
| `delete logical-routers` | global | `logical_routers_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/logical-routers/{id} |
| `delete loopback-interfaces` | global | `loopback_interfaces_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/loopback-interfaces/{id} |
| `delete nat-rules` | global | `nat_rules_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/nat-rules/{id} |
| `delete npb-profiles` | global | `npb_profiles_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/network_packet_broker_profiles/{id} |
| `delete npb-rules` | global | `npb_rules_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/network_packet_broker_rules/{id} |
| `delete ospf-auth-profiles` | global | `ospf_auth_profiles_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/ospf-auth-profiles/{id} |
| `delete pbf-rules` | global | `pbf_rules_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/pbf-rules/{id} |
| `delete qos-policy-rules` | global | `qos_policy_rules_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/qos-policy-rules/{id} |
| `delete qos-profiles` | global | `qos_profiles_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/qos-profiles/{id} |
| `delete route-access-lists` | global | `route_access_lists_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/route-access-lists/{id} |
| `delete route-community-lists` | global | `route_community_lists_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/route-community-lists/{id} |
| `delete route-path-acls` | global | `route_path_acls_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/route-path-access-lists/{id} |
| `delete route-prefix-lists` | global | `route_prefix_lists_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/route-prefix-lists/{id} |
| `delete sdwan-error-profiles` | global | `sdwan_error_profiles_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-error-correction-profiles/{id} |
| `delete sdwan-path-profiles` | global | `sdwan_path_profiles_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-path-quality-profiles/{id} |
| `delete sdwan-rules` | global | `sdwan_rules_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-rules/{id} |
| `delete sdwan-saas-profiles` | global | `sdwan_saas_profiles_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-saas-quality-profiles/{id} |
| `delete sdwan-traffic-profiles` | global | `sdwan_traffic_profiles_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-traffic-distribution-profiles/{id} |
| `delete system-match-list` | global | `system_match_list_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/system-match-list/{id} |
| `delete tunnel-interfaces` | global | `tunnel_interfaces_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/tunnel-interfaces/{id} |
| `delete userid-match-list` | global | `userid_match_list_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/userid-match-list/{id} |
| `delete vlan-interfaces` | global | `vlan_interfaces_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/vlan-interfaces/{id} |
| `delete zone-profiles` | global | `zone_profiles_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/zone-protection-profiles/{id} |
| `delete zones` | global | `zones_write` | DELETE https://api.strata.paloaltonetworks.com/config/network/v1/zones/{id} |
| `set aggregate-interfaces` | global | `aggregate_interfaces_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/aggregate-interfaces |
| `set auto-vpn-clusters` | global | `auto_vpn_clusters_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/auto-vpn-clusters |
| `set auto-vpn-push` | global | `auto_vpn_push_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/auto-vpn-push |
| `set bgp-af-profiles` | global | `bgp_af_profiles_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/bgp-address-family-profiles |
| `set bgp-auth-profiles` | global | `bgp_auth_profiles_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/bgp-auth-profiles |
| `set bgp-filtering-profiles` | global | `bgp_filtering_profiles_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/bgp-filtering-profiles |
| `set bgp-redist-profiles` | global | `bgp_redist_profiles_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/bgp-redistribution-profiles |
| `set bgp-route-maps` | global | `bgp_route_maps_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/bgp-route-maps |
| `set bgp-routemap-redist` | global | `bgp_routemap_redist_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/bgp-route-map-redistributions |
| `set config-match-list` | global | `config_match_list_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/config-match-list |
| `set dhcp-interfaces` | global | `dhcp_interfaces_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/dhcp-interfaces |
| `set dns-proxies` | global | `dns_proxies_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/dns-proxies |
| `set ethernet-interfaces` | global | `ethernet_interfaces_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/ethernet-interfaces |
| `set gp-match-list` | global | `gp_match_list_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/globalprotect-match-list |
| `set hipmatch-match-list` | global | `hipmatch_match_list_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/hipmatch-match-list |
| `set if-mgmt-profiles` | global | `if_mgmt_profiles_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/interface-management-profiles |
| `set ike-crypto-profiles` | global | `ike_crypto_profiles_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/ike-crypto-profiles |
| `set ike-gateways` | global | `ike_gateways_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/ike-gateways |
| `set ipsec-crypto-profiles` | global | `ipsec_crypto_profiles_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/ipsec-crypto-profiles |
| `set ipsec-tunnels` | global | `ipsec_tunnels_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/ipsec-tunnels |
| `set iptag-match-list` | global | `iptag_match_list_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/iptag-match-list |
| `set layer2-subinterfaces` | global | `layer2_subinterfaces_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/layer2-subinterfaces |
| `set layer3-subinterfaces` | global | `layer3_subinterfaces_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/layer3-subinterfaces |
| `set link-tags` | global | `link_tags_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/link-tags |
| `set lldp-profiles` | global | `lldp_profiles_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/lldp-profiles |
| `set logical-routers` | global | `logical_routers_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/logical-routers |
| `set loopback-interfaces` | global | `loopback_interfaces_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/loopback-interfaces |
| `set nat-rules` | global | `nat_rules_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/nat-rules |
| `set npb-profiles` | global | `npb_profiles_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/network_packet_broker_profiles |
| `set npb-rules` | global | `npb_rules_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/network_packet_broker_rules |
| `set ospf-auth-profiles` | global | `ospf_auth_profiles_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/ospf-auth-profiles |
| `set pbf-rules` | global | `pbf_rules_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/pbf-rules |
| `set qos-policy-rules` | global | `qos_policy_rules_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/qos-policy-rules |
| `set qos-policy-rules move` | global | `qos_policy_rules_move_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/qos-policy-rules/{id}:move |
| `set qos-profiles` | global | `qos_profiles_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/qos-profiles |
| `set route-access-lists` | global | `route_access_lists_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/route-access-lists |
| `set route-community-lists` | global | `route_community_lists_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/route-community-lists |
| `set route-path-acls` | global | `route_path_acls_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/route-path-access-lists |
| `set route-prefix-lists` | global | `route_prefix_lists_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/route-prefix-lists |
| `set sdwan-error-profiles` | global | `sdwan_error_profiles_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-error-correction-profiles |
| `set sdwan-path-profiles` | global | `sdwan_path_profiles_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-path-quality-profiles |
| `set sdwan-rules` | global | `sdwan_rules_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-rules |
| `set sdwan-saas-profiles` | global | `sdwan_saas_profiles_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-saas-quality-profiles |
| `set sdwan-traffic-profiles` | global | `sdwan_traffic_profiles_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-traffic-distribution-profiles |
| `set system-match-list` | global | `system_match_list_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/system-match-list |
| `set tunnel-interfaces` | global | `tunnel_interfaces_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/tunnel-interfaces |
| `set userid-match-list` | global | `userid_match_list_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/userid-match-list |
| `set vlan-interfaces` | global | `vlan_interfaces_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/vlan-interfaces |
| `set zone-profiles` | global | `zone_profiles_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/zone-protection-profiles |
| `set zones` | global | `zones_write` | POST https://api.strata.paloaltonetworks.com/config/network/v1/zones |
| `show aggregate-interfaces` | global | `aggregate_interfaces_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/aggregate-interfaces |
| `show aggregate-interfaces id` | global | `aggregate_interfaces_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/aggregate-interfaces/{id} |
| `show arp` | device | `show_arp` | (live device state — SSH via --remote) |
| `show auto-vpn-clusters` | global | `auto_vpn_clusters_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/auto-vpn-clusters |
| `show auto-vpn-clusters id` | global | `auto_vpn_clusters_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/auto-vpn-clusters/{id} |
| `show auto-vpn-monitor` | global | `auto_vpn_monitor_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/auto-vpn-monitor |
| `show auto-vpn-settings` | global | `auto_vpn_settings_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/auto-vpn-settings |
| `show bgp-af-profiles id` | global | `bgp_af_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/bgp-address-family-profiles/{id} |
| `show bgp-auth-profiles` | global | `bgp_auth_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/bgp-auth-profiles |
| `show bgp-auth-profiles id` | global | `bgp_auth_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/bgp-auth-profiles/{id} |
| `show bgp-filtering-profiles` | global | `bgp_filtering_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/bgp-filtering-profiles |
| `show bgp-filtering-profiles id` | global | `bgp_filtering_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/bgp-filtering-profiles/{id} |
| `show bgp-profile` | folder | `bgp_routing` | GET /config/network/v1/bgp-address-family-profiles |
| `show bgp-redist-profiles` | global | `bgp_redist_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/bgp-redistribution-profiles |
| `show bgp-redist-profiles id` | global | `bgp_redist_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/bgp-redistribution-profiles/{id} |
| `show bgp-route-maps` | global | `bgp_route_maps_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/bgp-route-maps |
| `show bgp-route-maps id` | global | `bgp_route_maps_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/bgp-route-maps/{id} |
| `show bgp-routemap-redist` | global | `bgp_routemap_redist_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/bgp-route-map-redistributions |
| `show bgp-routemap-redist id` | global | `bgp_routemap_redist_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/bgp-route-map-redistributions/{id} |
| `show config-match-list` | global | `config_match_list_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/config-match-list |
| `show config-match-list id` | global | `config_match_list_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/config-match-list/{id} |
| `show dhcp-interfaces` | global | `dhcp_interfaces_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/dhcp-interfaces |
| `show dhcp-interfaces id` | global | `dhcp_interfaces_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/dhcp-interfaces/{id} |
| `show dns-proxies id` | global | `dns_proxies_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/dns-proxies/{id} |
| `show dns-proxy` | folder | `dns_proxy` | GET /config/network/v1/dns-proxies |
| `show ethernet-interfaces id` | global | `ethernet_interfaces_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/ethernet-interfaces/{id} |
| `show gp-match-list` | global | `gp_match_list_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/globalprotect-match-list |
| `show gp-match-list id` | global | `gp_match_list_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/globalprotect-match-list/{id} |
| `show high-availability all` | folder | `show_high_availability` | GET /config/network/v1/ha |
| `show high-availability state` | folder | `show_high_availability` | GET /config/network/v1/ha |
| `show hipmatch-match-list` | global | `hipmatch_match_list_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/hipmatch-match-list |
| `show hipmatch-match-list id` | global | `hipmatch_match_list_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/hipmatch-match-list/{id} |
| `show if-mgmt-profiles` | global | `if_mgmt_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/interface-management-profiles |
| `show if-mgmt-profiles id` | global | `if_mgmt_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/interface-management-profiles/{id} |
| `show ike-crypto-profiles` | global | `ike_crypto_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/ike-crypto-profiles |
| `show ike-crypto-profiles id` | global | `ike_crypto_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/ike-crypto-profiles/{id} |
| `show ike-gateway` | folder | `ipsec_vpn` | GET /config/network/v1/ike-gateways |
| `show ike-gateways id` | global | `ike_gateways_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/ike-gateways/{id} |
| `show interface` | folder | `show_interface` | GET /config/network/v1/ethernet-interfaces |
| `show interface all` | folder | `show_interface` | GET /config/network/v1/ethernet-interfaces |
| `show ipsec-crypto-profiles` | global | `ipsec_crypto_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/ipsec-crypto-profiles |
| `show ipsec-crypto-profiles id` | global | `ipsec_crypto_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/ipsec-crypto-profiles/{id} |
| `show ipsec-tunnel` | folder | `ipsec_vpn` | GET /config/network/v1/ipsec-tunnels |
| `show ipsec-tunnels id` | global | `ipsec_tunnels_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/ipsec-tunnels/{id} |
| `show iptag-match-list` | global | `iptag_match_list_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/iptag-match-list |
| `show iptag-match-list id` | global | `iptag_match_list_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/iptag-match-list/{id} |
| `show layer2-subinterfaces` | global | `layer2_subinterfaces_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/layer2-subinterfaces |
| `show layer2-subinterfaces id` | global | `layer2_subinterfaces_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/layer2-subinterfaces/{id} |
| `show layer3-subinterfaces` | global | `layer3_subinterfaces_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/layer3-subinterfaces |
| `show layer3-subinterfaces id` | global | `layer3_subinterfaces_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/layer3-subinterfaces/{id} |
| `show link-tags` | global | `link_tags_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/link-tags |
| `show link-tags id` | global | `link_tags_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/link-tags/{id} |
| `show lldp-profiles` | global | `lldp_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/lldp-profiles |
| `show lldp-profiles id` | global | `lldp_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/lldp-profiles/{id} |
| `show logical-routers` | global | `logical_routers_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/logical-routers |
| `show logical-routers id` | global | `logical_routers_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/logical-routers/{id} |
| `show loopback-interfaces` | global | `loopback_interfaces_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/loopback-interfaces |
| `show loopback-interfaces id` | global | `loopback_interfaces_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/loopback-interfaces/{id} |
| `show nat-rules` | folder | `nat_rules` | GET /config/network/v1/nat-rules |
| `show nat-rules id` | global | `nat_rules_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/nat-rules/{id} |
| `show npb-profiles` | global | `npb_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/network_packet_broker_profiles |
| `show npb-profiles id` | global | `npb_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/network_packet_broker_profiles/{id} |
| `show npb-rules` | global | `npb_rules_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/network_packet_broker_rules |
| `show npb-rules id` | global | `npb_rules_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/network_packet_broker_rules/{id} |
| `show ospf-auth-profiles` | global | `ospf_auth_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/ospf-auth-profiles |
| `show ospf-auth-profiles id` | global | `ospf_auth_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/ospf-auth-profiles/{id} |
| `show pbf-rules` | folder | `pbf_rules` | GET /config/network/v1/pbf-rules |
| `show pbf-rules id` | global | `pbf_rules_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/pbf-rules/{id} |
| `show qos-policy-rules` | global | `qos_policy_rules_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/qos-policy-rules |
| `show qos-policy-rules id` | global | `qos_policy_rules_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/qos-policy-rules/{id} |
| `show qos-profile` | folder | `qos` | GET /config/network/v1/qos-profiles |
| `show qos-profiles id` | global | `qos_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/qos-profiles/{id} |
| `show rn-license-info` | global | `rn_license_info_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/remote-networks-license-info |
| `show route-access-lists` | global | `route_access_lists_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/route-access-lists |
| `show route-access-lists id` | global | `route_access_lists_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/route-access-lists/{id} |
| `show route-community-lists` | global | `route_community_lists_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/route-community-lists |
| `show route-community-lists id` | global | `route_community_lists_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/route-community-lists/{id} |
| `show route-path-acls` | global | `route_path_acls_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/route-path-access-lists |
| `show route-path-acls id` | global | `route_path_acls_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/route-path-access-lists/{id} |
| `show route-prefix-lists` | global | `route_prefix_lists_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/route-prefix-lists |
| `show route-prefix-lists id` | global | `route_prefix_lists_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/route-prefix-lists/{id} |
| `show routing bgp` | device | `bgp_routing` | (live device state — SSH via --remote) |
| `show routing route` | folder | `show_routing` | GET /config/network/v1/routing/static-routes |
| `show routing summary` | folder | `show_routing` | GET /config/network/v1/virtual-routers |
| `show sdwan-error-profiles` | global | `sdwan_error_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-error-correction-profiles |
| `show sdwan-error-profiles id` | global | `sdwan_error_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-error-correction-profiles/{id} |
| `show sdwan-path-profiles` | global | `sdwan_path_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-path-quality-profiles |
| `show sdwan-path-profiles id` | global | `sdwan_path_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-path-quality-profiles/{id} |
| `show sdwan-rules` | folder | `sdwan` | GET /config/network/v1/sdwan-rules |
| `show sdwan-rules id` | global | `sdwan_rules_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-rules/{id} |
| `show sdwan-saas-profiles` | global | `sdwan_saas_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-saas-quality-profiles |
| `show sdwan-saas-profiles id` | global | `sdwan_saas_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-saas-quality-profiles/{id} |
| `show sdwan-traffic-profiles` | global | `sdwan_traffic_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-traffic-distribution-profiles |
| `show sdwan-traffic-profiles id` | global | `sdwan_traffic_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-traffic-distribution-profiles/{id} |
| `show session all` | device | `show_sessions` | (live device state — SSH via --remote) |
| `show system-match-list` | global | `system_match_list_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/system-match-list |
| `show system-match-list id` | global | `system_match_list_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/system-match-list/{id} |
| `show tunnel-interfaces` | global | `tunnel_interfaces_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/tunnel-interfaces |
| `show tunnel-interfaces id` | global | `tunnel_interfaces_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/tunnel-interfaces/{id} |
| `show userid-match-list` | global | `userid_match_list_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/userid-match-list |
| `show userid-match-list id` | global | `userid_match_list_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/userid-match-list/{id} |
| `show vlan-interfaces` | global | `vlan_interfaces_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/vlan-interfaces |
| `show vlan-interfaces id` | global | `vlan_interfaces_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/vlan-interfaces/{id} |
| `show vpn ike-sa` | device | `ipsec_vpn` | (live device state — SSH via --remote) |
| `show vpn tunnel` | device | `ipsec_vpn` | (live device state — SSH via --remote) |
| `show zone` | folder | `show_zone` | GET /config/network/v1/zones |
| `show zone-profiles` | global | `zone_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/zone-protection-profiles |
| `show zone-profiles id` | global | `zone_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/zone-protection-profiles/{id} |
| `show zones id` | global | `zones_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/zones/{id} |
| `test nat-policy-match` | device | `test_nat` | (live device state — SSH via --remote) |
| `test url` | device | `test_url` | (live device state — SSH via --remote) |
| `traceroute host` | device | `traceroute` | (live device state — SSH via --remote) |
| `update aggregate-interfaces` | global | `aggregate_interfaces_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/aggregate-interfaces/{id} |
| `update auto-vpn-clusters` | global | `auto_vpn_clusters_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/auto-vpn-clusters/{id} |
| `update auto-vpn-settings` | global | `auto_vpn_settings_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/auto-vpn-settings |
| `update bgp-af-profiles` | global | `bgp_af_profiles_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/bgp-address-family-profiles/{id} |
| `update bgp-auth-profiles` | global | `bgp_auth_profiles_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/bgp-auth-profiles/{id} |
| `update bgp-filtering-profiles` | global | `bgp_filtering_profiles_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/bgp-filtering-profiles/{id} |
| `update bgp-redist-profiles` | global | `bgp_redist_profiles_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/bgp-redistribution-profiles/{id} |
| `update bgp-route-maps` | global | `bgp_route_maps_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/bgp-route-maps/{id} |
| `update bgp-routemap-redist` | global | `bgp_routemap_redist_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/bgp-route-map-redistributions/{id} |
| `update config-match-list` | global | `config_match_list_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/config-match-list/{id} |
| `update dhcp-interfaces` | global | `dhcp_interfaces_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/dhcp-interfaces/{id} |
| `update dns-proxies` | global | `dns_proxies_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/dns-proxies/{id} |
| `update ethernet-interfaces` | global | `ethernet_interfaces_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/ethernet-interfaces/{id} |
| `update gp-match-list` | global | `gp_match_list_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/globalprotect-match-list/{id} |
| `update hipmatch-match-list` | global | `hipmatch_match_list_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/hipmatch-match-list/{id} |
| `update if-mgmt-profiles` | global | `if_mgmt_profiles_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/interface-management-profiles/{id} |
| `update ike-crypto-profiles` | global | `ike_crypto_profiles_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/ike-crypto-profiles/{id} |
| `update ike-gateways` | global | `ike_gateways_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/ike-gateways/{id} |
| `update ipsec-crypto-profiles` | global | `ipsec_crypto_profiles_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/ipsec-crypto-profiles/{id} |
| `update ipsec-tunnels` | global | `ipsec_tunnels_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/ipsec-tunnels/{id} |
| `update iptag-match-list` | global | `iptag_match_list_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/iptag-match-list/{id} |
| `update layer2-subinterfaces` | global | `layer2_subinterfaces_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/layer2-subinterfaces/{id} |
| `update layer3-subinterfaces` | global | `layer3_subinterfaces_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/layer3-subinterfaces/{id} |
| `update link-tags` | global | `link_tags_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/link-tags/{id} |
| `update lldp-profiles` | global | `lldp_profiles_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/lldp-profiles/{id} |
| `update logical-routers` | global | `logical_routers_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/logical-routers/{id} |
| `update loopback-interfaces` | global | `loopback_interfaces_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/loopback-interfaces/{id} |
| `update nat-rules` | global | `nat_rules_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/nat-rules/{id} |
| `update npb-profiles` | global | `npb_profiles_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/network_packet_broker_profiles/{id} |
| `update npb-rules` | global | `npb_rules_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/network_packet_broker_rules/{id} |
| `update ospf-auth-profiles` | global | `ospf_auth_profiles_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/ospf-auth-profiles/{id} |
| `update pbf-rules` | global | `pbf_rules_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/pbf-rules/{id} |
| `update qos-policy-rules` | global | `qos_policy_rules_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/qos-policy-rules/{id} |
| `update qos-profiles` | global | `qos_profiles_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/qos-profiles/{id} |
| `update route-access-lists` | global | `route_access_lists_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/route-access-lists/{id} |
| `update route-community-lists` | global | `route_community_lists_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/route-community-lists/{id} |
| `update route-path-acls` | global | `route_path_acls_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/route-path-access-lists/{id} |
| `update route-prefix-lists` | global | `route_prefix_lists_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/route-prefix-lists/{id} |
| `update sdwan-error-profiles` | global | `sdwan_error_profiles_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-error-correction-profiles/{id} |
| `update sdwan-path-profiles` | global | `sdwan_path_profiles_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-path-quality-profiles/{id} |
| `update sdwan-rules` | global | `sdwan_rules_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-rules/{id} |
| `update sdwan-saas-profiles` | global | `sdwan_saas_profiles_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-saas-quality-profiles/{id} |
| `update sdwan-traffic-profiles` | global | `sdwan_traffic_profiles_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/sdwan-traffic-distribution-profiles/{id} |
| `update system-match-list` | global | `system_match_list_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/system-match-list/{id} |
| `update tunnel-interfaces` | global | `tunnel_interfaces_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/tunnel-interfaces/{id} |
| `update userid-match-list` | global | `userid_match_list_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/userid-match-list/{id} |
| `update vlan-interfaces` | global | `vlan_interfaces_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/vlan-interfaces/{id} |
| `update zone-profiles` | global | `zone_profiles_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/zone-protection-profiles/{id} |
| `update zones` | global | `zones_write` | PUT https://api.strata.paloaltonetworks.com/config/network/v1/zones/{id} |

## Ngts

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `delete ngts cert-requests approval` | global | `ngts_cert_requests_approval_write` | DELETE https://api.strata.paloaltonetworks.com/ngts/v1/certificaterequests/approvalrules/{id} |
| `delete ngts cert-templates` | global | `ngts_cert_templates_write` | DELETE https://api.strata.paloaltonetworks.com/ngts/v1/certificateissuingtemplates/{id} |
| `delete ngts certs revokes approval` | global | `ngts_certs_revokes_approval_write` | DELETE https://api.strata.paloaltonetworks.com/ngts/v1/certificates/revocations/approvalrules/{id} |
| `delete ngts credential-configs` | global | `ngts_credential_configs_write` | DELETE https://api.strata.paloaltonetworks.com/ngts/v1/credentialmanagerconfigurations/{id} |
| `delete ngts credentials` | global | `ngts_credentials_write` | DELETE https://api.strata.paloaltonetworks.com/ngts/v1/credentials |
| `delete ngts credentials id` | global | `ngts_credentials_write` | DELETE https://api.strata.paloaltonetworks.com/ngts/v1/credentials/{id} |
| `delete ngts dist-issuers configurations` | global | `ngts_dist_issuers_configurations_write` | DELETE https://api.strata.paloaltonetworks.com/ngts/v1/distributedissuers/configurations/{id} |
| `delete ngts dist-issuers policies` | global | `ngts_dist_issuers_policies_write` | DELETE https://api.strata.paloaltonetworks.com/ngts/v1/distributedissuers/policies/{id} |
| `delete ngts dist-issuers subcaproviders` | global | `ngts_dist_issuers_subcaproviders_write` | DELETE https://api.strata.paloaltonetworks.com/ngts/v1/distributedissuers/subcaproviders/{id} |
| `delete ngts edgeworkers` | global | `ngts_edgeworkers_write` | DELETE https://api.strata.paloaltonetworks.com/ngts/v1/edgeworkers/{id} |
| `delete ngts integrationservices` | global | `ngts_integrationservices_write` | DELETE https://api.strata.paloaltonetworks.com/ngts/v1/integrationservices/{id} |
| `delete ngts machineidentities` | global | `ngts_machineidentities_write` | DELETE https://api.strata.paloaltonetworks.com/ngts/v1/machineidentities/{id} |
| `delete ngts machines` | global | `ngts_machines_write` | DELETE https://api.strata.paloaltonetworks.com/ngts/v1/machines/{id} |
| `delete ngts plugins` | global | `ngts_plugins_write` | DELETE https://api.strata.paloaltonetworks.com/ngts/v1/plugins/{id} |
| `delete ngts plugins disablements` | global | `ngts_plugins_disablements_write` | DELETE https://api.strata.paloaltonetworks.com/ngts/v1/plugins/{id}/disablements |
| `delete ngts serviceaccounts` | global | `ngts_serviceaccounts_write` | DELETE https://api.strata.paloaltonetworks.com/ngts/v1/serviceaccounts/{id} |
| `delete ngts tags` | global | `ngts_tags_write` | DELETE https://api.strata.paloaltonetworks.com/ngts/v1/tags/{name} |
| `delete ngts tags values` | global | `ngts_tags_values_write` | DELETE https://api.strata.paloaltonetworks.com/ngts/v1/tags/{name}/values/{value} |
| `set ngts activitylogsearch` | global | `ngts_activitylogsearch_write` | POST https://api.strata.paloaltonetworks.com/ngts/v1/activitylogsearch |
| `set ngts activitylogsearch export` | global | `ngts_activitylogsearch_export_write` | POST https://api.strata.paloaltonetworks.com/ngts/v1/activitylogsearch/export |
| `set ngts autorenewal trigger` | global | `ngts_autorenewal_trigger_write` | POST https://api.strata.paloaltonetworks.com/ngts/v1/autorenewal/trigger |
| `set ngts cert-instance-search` | global | `ngts_cert_instance_search_write` | POST https://api.strata.paloaltonetworks.com/ngts/outagedetection/v1/certificateinstancesearch |
| `set ngts cert-instances validation` | global | `ngts_cert_instances_validation_write` | POST https://api.strata.paloaltonetworks.com/ngts/outagedetection/v1/certificateinstances/validation |
| `set ngts cert-request-search` | global | `ngts_cert_request_search_write` | POST https://api.strata.paloaltonetworks.com/ngts/outagedetection/v1/certificaterequestssearch |
| `set ngts cert-requests` | global | `ngts_cert_requests_write` | POST https://api.strata.paloaltonetworks.com/ngts/outagedetection/v1/certificaterequests |
| `set ngts cert-requests approval` | global | `ngts_cert_requests_approval_write` | POST https://api.strata.paloaltonetworks.com/ngts/v1/certificaterequests/{id}/approval/{decision} |
| `set ngts cert-requests approval bulk` | global | `ngts_cert_requests_approval_bulk_write` | POST https://api.strata.paloaltonetworks.com/ngts/v1/certificaterequests/approval/bulk/{decision} |
| `set ngts cert-requests resubmission` | global | `ngts_cert_requests_resubmission_write` | POST https://api.strata.paloaltonetworks.com/ngts/outagedetection/v1/certificaterequests/{id}/resubmission |
| `set ngts cert-requests validation` | global | `ngts_cert_requests_validation_write` | POST https://api.strata.paloaltonetworks.com/ngts/outagedetection/v1/certificaterequests/validation |
| `set ngts cert-templates` | global | `ngts_cert_templates_write` | POST https://api.strata.paloaltonetworks.com/ngts/v1/certificateissuingtemplates |
| `set ngts cert-templates domains-sync` | global | `ngts_cert_templates_domains_sync_write` | POST https://api.strata.paloaltonetworks.com/ngts/v1/certificateissuingtemplates/domainssynchronization |
| `set ngts certificatesearch` | global | `ngts_certificatesearch_write` | POST https://api.strata.paloaltonetworks.com/ngts/outagedetection/v1/certificatesearch |
| `set ngts certs` | global | `ngts_certs_write` | POST https://api.strata.paloaltonetworks.com/ngts/outagedetection/v1/certificates |
| `set ngts certs deletion` | global | `ngts_certs_deletion_write` | POST https://api.strata.paloaltonetworks.com/ngts/outagedetection/v1/certificates/deletion |
| `set ngts certs imports` | global | `ngts_certs_imports_write` | POST https://api.strata.paloaltonetworks.com/ngts/v1/certificates/imports |
| `set ngts certs recovery` | global | `ngts_certs_recovery_write` | POST https://api.strata.paloaltonetworks.com/ngts/outagedetection/v1/certificates/recovery |
| `set ngts certs retirement` | global | `ngts_certs_retirement_write` | POST https://api.strata.paloaltonetworks.com/ngts/outagedetection/v1/certificates/retirement |
| `set ngts certs revokes approval` | global | `ngts_certs_revokes_approval_write` | POST https://api.strata.paloaltonetworks.com/ngts/v1/certificates/revocations/approvalrules |
| `set ngts certs validation` | global | `ngts_certs_validation_write` | POST https://api.strata.paloaltonetworks.com/ngts/outagedetection/v1/certificates/validation |
| `set ngts credential-configs` | global | `ngts_credential_configs_write` | POST https://api.strata.paloaltonetworks.com/ngts/v1/credentialmanagerconfigurations |
| `set ngts credential-configs test` | global | `ngts_credential_configs_test_write` | POST https://api.strata.paloaltonetworks.com/ngts/v1/credentialmanagerconfigurations/test |
| `set ngts credential-configs test id` | global | `ngts_credential_configs_test_write` | POST https://api.strata.paloaltonetworks.com/ngts/v1/credentialmanagerconfigurations/{id}/test |
| `set ngts credentials` | global | `ngts_credentials_write` | POST https://api.strata.paloaltonetworks.com/ngts/v1/credentials |
| `set ngts credentials test` | global | `ngts_credentials_test_write` | POST https://api.strata.paloaltonetworks.com/ngts/v1/credentials/test |
| `set ngts dist-issuers configurations` | global | `ngts_dist_issuers_configurations_write` | POST https://api.strata.paloaltonetworks.com/ngts/v1/distributedissuers/configurations |
| `set ngts dist-issuers policies` | global | `ngts_dist_issuers_policies_write` | POST https://api.strata.paloaltonetworks.com/ngts/v1/distributedissuers/policies |
| `set ngts dist-issuers subcaproviders` | global | `ngts_dist_issuers_subcaproviders_write` | POST https://api.strata.paloaltonetworks.com/ngts/v1/distributedissuers/subcaproviders |
| `set ngts edgeinstances update` | global | `ngts_edgeinstances_update_write` | POST https://api.strata.paloaltonetworks.com/ngts/v1/edgeinstances/{id}/update |
| `set ngts edgeworkers` | global | `ngts_edgeworkers_write` | POST https://api.strata.paloaltonetworks.com/ngts/v1/edgeworkers |
| `set ngts edgeworkers pair` | global | `ngts_edgeworkers_pair_write` | POST https://api.strata.paloaltonetworks.com/ngts/v1/edgeworkers/{id}/pair |
| `set ngts integrationservices` | global | `ngts_integrationservices_write` | POST https://api.strata.paloaltonetworks.com/ngts/v1/integrationservices |
| `set ngts machineidentities` | global | `ngts_machineidentities_write` | POST https://api.strata.paloaltonetworks.com/ngts/v1/machineidentities |
| `set ngts machineidentities workflows` | global | `ngts_machineidentities_workflows_write` | POST https://api.strata.paloaltonetworks.com/ngts/v1/machineidentities/{id}/workflows |
| `set ngts machineidentitysearch` | global | `ngts_machineidentitysearch_write` | POST https://api.strata.paloaltonetworks.com/ngts/v1/machineidentitysearch |
| `set ngts machines` | global | `ngts_machines_write` | POST https://api.strata.paloaltonetworks.com/ngts/v1/machines |
| `set ngts machines batchprovisionings abort` | global | `ngts_machines_batchprovisionings_abort_write` | POST https://api.strata.paloaltonetworks.com/ngts/v1/machines/{id}/batchprovisionings/abort |
| `set ngts machines discovery abort` | global | `ngts_machines_discovery_abort_write` | POST https://api.strata.paloaltonetworks.com/ngts/v1/machines/{id}/discovery/abort |
| `set ngts machines workflows` | global | `ngts_machines_workflows_write` | POST https://api.strata.paloaltonetworks.com/ngts/v1/machines/{id}/workflows |
| `set ngts machinesearch` | global | `ngts_machinesearch_write` | POST https://api.strata.paloaltonetworks.com/ngts/v1/machinesearch |
| `set ngts pairingcodes satellite` | global | `ngts_pairingcodes_satellite_write` | POST https://api.strata.paloaltonetworks.com/ngts/v1/pairingcodes/satellite |
| `set ngts plugins` | global | `ngts_plugins_write` | POST https://api.strata.paloaltonetworks.com/ngts/v1/plugins |
| `set ngts plugins disablements` | global | `ngts_plugins_disablements_write` | POST https://api.strata.paloaltonetworks.com/ngts/v1/plugins/{id}/disablements |
| `set ngts recoverycodes satellite` | global | `ngts_recoverycodes_satellite_write` | POST https://api.strata.paloaltonetworks.com/ngts/v1/recoverycodes/satellite |
| `set ngts serviceaccounts` | global | `ngts_serviceaccounts_write` | POST https://api.strata.paloaltonetworks.com/ngts/v1/serviceaccounts |
| `set ngts tags` | global | `ngts_tags_write` | POST https://api.strata.paloaltonetworks.com/ngts/v1/tags |
| `set ngts tags creation` | global | `ngts_tags_creation_write` | POST https://api.strata.paloaltonetworks.com/ngts/v1/tags/creation |
| `set ngts tags deletion` | global | `ngts_tags_deletion_write` | POST https://api.strata.paloaltonetworks.com/ngts/v1/tags/deletion |
| `set ngts tags values` | global | `ngts_tags_values_write` | POST https://api.strata.paloaltonetworks.com/ngts/v1/tags/{name}/values |
| `set ngts tagsassignment aggregates` | global | `ngts_tagsassignment_aggregates_write` | POST https://api.strata.paloaltonetworks.com/ngts/v1/tagsassignment/aggregates |
| `set ngts tlsprotect cert-requests approval` | global | `ngts_cert_requests_approval_write` | POST https://api.strata.paloaltonetworks.com/ngts/v1/certificaterequests/approvalrules |
| `show ngts activitytypes` | global | `ngts_activitytypes_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/activitytypes |
| `show ngts autorenewal status` | global | `ngts_autorenewal_status_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/autorenewal/status |
| `show ngts autorenewal tenant-config` | global | `ngts_autorenewal_tenant_config_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/autorenewal/tenantconfiguration |
| `show ngts cert-instances` | global | `ngts_cert_instances_read` | GET https://api.strata.paloaltonetworks.com/ngts/outagedetection/v1/certificateinstances |
| `show ngts cert-instances id` | global | `ngts_cert_instances_read` | GET https://api.strata.paloaltonetworks.com/ngts/outagedetection/v1/certificateinstances/{id} |
| `show ngts cert-requests` | global | `ngts_cert_requests_read` | GET https://api.strata.paloaltonetworks.com/ngts/outagedetection/v1/certificaterequests |
| `show ngts cert-requests approval` | global | `ngts_cert_requests_approval_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/certificaterequests/approvalrules |
| `show ngts cert-requests approval id` | global | `ngts_cert_requests_approval_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/certificaterequests/approvalrules/{id} |
| `show ngts cert-requests approvalrequests id` | global | `ngts_cert_requests_approvalrequests_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/certificaterequests/approvalrequests/{entityId} |
| `show ngts cert-requests id` | global | `ngts_cert_requests_read` | GET https://api.strata.paloaltonetworks.com/ngts/outagedetection/v1/certificaterequests/{id} |
| `show ngts cert-templates` | global | `ngts_cert_templates_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/certificateissuingtemplates |
| `show ngts cert-templates id` | global | `ngts_cert_templates_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/certificateissuingtemplates/{id} |
| `show ngts certs` | global | `ngts_certs_read` | GET https://api.strata.paloaltonetworks.com/ngts/outagedetection/v1/certificates |
| `show ngts certs contents id` | global | `ngts_certs_contents_read` | GET https://api.strata.paloaltonetworks.com/ngts/outagedetection/v1/certificates/{id}/contents |
| `show ngts certs id` | global | `ngts_certs_read` | GET https://api.strata.paloaltonetworks.com/ngts/outagedetection/v1/certificates/{id} |
| `show ngts certs imports id` | global | `ngts_certs_imports_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/certificates/imports/{id} |
| `show ngts certs revokes approval` | global | `ngts_certs_revokes_approval_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/certificates/revocations/approvalrules |
| `show ngts certs revokes approval id` | global | `ngts_certs_revokes_approval_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/certificates/revocations/approvalrules/{id} |
| `show ngts credential-configs` | global | `ngts_credential_configs_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/credentialmanagerconfigurations |
| `show ngts credential-configs id` | global | `ngts_credential_configs_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/credentialmanagerconfigurations/{id} |
| `show ngts credentials` | global | `ngts_credentials_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/credentials |
| `show ngts credentials id` | global | `ngts_credentials_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/credentials/{id} |
| `show ngts dist-issuers configurations` | global | `ngts_dist_issuers_configurations_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/distributedissuers/configurations |
| `show ngts dist-issuers configurations id` | global | `ngts_dist_issuers_configurations_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/distributedissuers/configurations/{id} |
| `show ngts dist-issuers intermediate-certs` | global | `ngts_dist_issuers_intermediate_certs_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/distributedissuers/intermediatecertificates |
| `show ngts dist-issuers policies` | global | `ngts_dist_issuers_policies_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/distributedissuers/policies |
| `show ngts dist-issuers policies id` | global | `ngts_dist_issuers_policies_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/distributedissuers/policies/{id} |
| `show ngts dist-issuers subcaproviders` | global | `ngts_dist_issuers_subcaproviders_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/distributedissuers/subcaproviders |
| `show ngts dist-issuers subcaproviders id` | global | `ngts_dist_issuers_subcaproviders_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/distributedissuers/subcaproviders/{id} |
| `show ngts edgeencryptionkeys` | global | `ngts_edgeencryptionkeys_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/edgeencryptionkeys |
| `show ngts edgeencryptionkeys id` | global | `ngts_edgeencryptionkeys_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/edgeencryptionkeys/{id} |
| `show ngts edgeinstances` | global | `ngts_edgeinstances_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/edgeinstances |
| `show ngts edgeinstances id` | global | `ngts_edgeinstances_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/edgeinstances/{id} |
| `show ngts edgeworkers` | global | `ngts_edgeworkers_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/edgeworkers |
| `show ngts exp-notifications tenant-config` | global | `ngts_exp_notifications_tenant_config_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/expirationnotifications/tenantconfiguration |
| `show ngts integrationservices` | global | `ngts_integrationservices_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/integrationservices |
| `show ngts integrationservices id` | global | `ngts_integrationservices_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/integrationservices/{id} |
| `show ngts inventory-monitoring id` | global | `ngts_inventory_monitoring_read` | GET https://api.strata.paloaltonetworks.com/ngts/outagedetection/v1/inventorymonitoringconfig/{type} |
| `show ngts machineidentities` | global | `ngts_machineidentities_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/machineidentities |
| `show ngts machineidentities id` | global | `ngts_machineidentities_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/machineidentities/{id} |
| `show ngts machines` | global | `ngts_machines_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/machines |
| `show ngts machines discovery id` | global | `ngts_machines_discovery_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/machines/{id}/discovery |
| `show ngts machines id` | global | `ngts_machines_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/machines/{id} |
| `show ngts machinetypes` | global | `ngts_machinetypes_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/machinetypes |
| `show ngts plugins` | global | `ngts_plugins_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/plugins |
| `show ngts plugins disablements` | global | `ngts_plugins_disablements_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/plugins/disablements |
| `show ngts plugins id` | global | `ngts_plugins_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/plugins/{id} |
| `show ngts serviceaccounts` | global | `ngts_serviceaccounts_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/serviceaccounts |
| `show ngts serviceaccounts id` | global | `ngts_serviceaccounts_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/serviceaccounts/{id} |
| `show ngts serviceaccounts scopes` | global | `ngts_serviceaccounts_scopes_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/serviceaccounts/scopes |
| `show ngts tags` | global | `ngts_tags_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/tags |
| `show ngts tags id` | global | `ngts_tags_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/tags/{name} |
| `show ngts tags values` | global | `ngts_tags_values_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/tags/values |
| `show ngts tags values id` | global | `ngts_tags_values_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/tags/{name}/values |
| `show ngts updatesconfig` | global | `ngts_updatesconfig_read` | GET https://api.strata.paloaltonetworks.com/ngts/v1/updatesconfig |
| `update ngts autorenewal tenant-config` | global | `ngts_autorenewal_tenant_config_write` | PUT https://api.strata.paloaltonetworks.com/ngts/v1/autorenewal/tenantconfiguration |
| `update ngts cert-requests approval` | global | `ngts_cert_requests_approval_write` | PUT https://api.strata.paloaltonetworks.com/ngts/v1/certificaterequests/approvalrules/{id} |
| `update ngts cert-templates` | global | `ngts_cert_templates_write` | PUT https://api.strata.paloaltonetworks.com/ngts/v1/certificateissuingtemplates/{id} |
| `update ngts certs revokes approval` | global | `ngts_certs_revokes_approval_write` | PUT https://api.strata.paloaltonetworks.com/ngts/v1/certificates/revocations/approvalrules/{id} |
| `update ngts credential-configs` | global | `ngts_credential_configs_write` | PUT https://api.strata.paloaltonetworks.com/ngts/v1/credentialmanagerconfigurations |
| `update ngts credentials` | global | `ngts_credentials_write` | PUT https://api.strata.paloaltonetworks.com/ngts/v1/credentials |
| `update ngts dist-issuers configurations` | global | `ngts_dist_issuers_configurations_write` | PATCH https://api.strata.paloaltonetworks.com/ngts/v1/distributedissuers/configurations/{id} |
| `update ngts dist-issuers policies` | global | `ngts_dist_issuers_policies_write` | PATCH https://api.strata.paloaltonetworks.com/ngts/v1/distributedissuers/policies/{id} |
| `update ngts dist-issuers subcaproviders` | global | `ngts_dist_issuers_subcaproviders_write` | PATCH https://api.strata.paloaltonetworks.com/ngts/v1/distributedissuers/subcaproviders/{id} |
| `update ngts edgeinstances` | global | `ngts_edgeinstances_write` | PUT https://api.strata.paloaltonetworks.com/ngts/v1/edgeinstances/{id} |
| `update ngts exp-notifications tenant-config` | global | `ngts_exp_notifications_tenant_config_write` | PUT https://api.strata.paloaltonetworks.com/ngts/v1/expirationnotifications/tenantconfiguration |
| `update ngts integrationservices` | global | `ngts_integrationservices_write` | PATCH https://api.strata.paloaltonetworks.com/ngts/v1/integrationservices/{id} |
| `update ngts inventory-monitoring` | global | `ngts_inventory_monitoring_write` | PUT https://api.strata.paloaltonetworks.com/ngts/outagedetection/v1/inventorymonitoringconfig/{type} |
| `update ngts inventory-monitoring scheduler` | global | `ngts_inventory_monitoring_scheduler_write` | PUT https://api.strata.paloaltonetworks.com/ngts/outagedetection/v1/inventorymonitoringconfig/{type}/scheduler |
| `update ngts machineidentities` | global | `ngts_machineidentities_write` | PATCH https://api.strata.paloaltonetworks.com/ngts/v1/machineidentities/{id} |
| `update ngts machines` | global | `ngts_machines_write` | PATCH https://api.strata.paloaltonetworks.com/ngts/v1/machines/{id} |
| `update ngts plugins` | global | `ngts_plugins_write` | PATCH https://api.strata.paloaltonetworks.com/ngts/v1/plugins/{id} |
| `update ngts serviceaccounts` | global | `ngts_serviceaccounts_write` | PATCH https://api.strata.paloaltonetworks.com/ngts/v1/serviceaccounts/{id} |
| `update ngts serviceaccounts credentials` | global | `ngts_serviceaccounts_credentials_write` | PUT https://api.strata.paloaltonetworks.com/ngts/v1/serviceaccounts/{id}/credentials |
| `update ngts serviceaccounts ocitoken` | global | `ngts_serviceaccounts_ocitoken_write` | PUT https://api.strata.paloaltonetworks.com/ngts/v1/serviceaccounts/{id}/ocitoken |
| `update ngts tagsassignment` | global | `ngts_tagsassignment_write` | PATCH https://api.strata.paloaltonetworks.com/ngts/v1/tagsassignment |
| `update ngts updatesconfig` | global | `ngts_updatesconfig_write` | PATCH https://api.strata.paloaltonetworks.com/ngts/v1/updatesconfig |

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
| `commit` | folder | — | POST /config/setup/v1/config-versions/candidate:push |
| `ping host` | device | `ping` | (live device state — SSH via --remote) |
| `request system reboot` | device | `request_system_reboot` | (live device state — SSH via --remote) |
| `request system shutdown` | device | `request_system_reboot` | (live device state — SSH via --remote) |
| `request system software check` | device | `request_system_software` | (live device state — SSH via --remote) |
| `set jobs bgp-policy-export` | global | `jobs_bgp_policy_export_write` | POST https://api.strata.paloaltonetworks.com/operations/v1/jobs/bgp-policy-export |
| `set jobs device-interfaces` | global | `jobs_device_interfaces_write` | POST https://api.strata.paloaltonetworks.com/operations/v1/jobs/device-interfaces |
| `set jobs device-rules` | global | `jobs_device_rules_write` | POST https://api.strata.paloaltonetworks.com/operations/v1/jobs/device-rules |
| `set jobs dns-proxy` | global | `jobs_dns_proxy_write` | POST https://api.strata.paloaltonetworks.com/operations/v1/jobs/dns-proxy |
| `set jobs fib-table` | global | `jobs_fib_table_write` | POST https://api.strata.paloaltonetworks.com/operations/v1/jobs/fib-table |
| `set jobs logging-service-forwarding-status` | global | `jobs_logging_service_forwarding_status_write` | POST https://api.strata.paloaltonetworks.com/operations/v1/jobs/logging-service-forwarding-status |
| `set jobs route-table` | global | `jobs_route_table_write` | POST https://api.strata.paloaltonetworks.com/operations/v1/jobs/route-table |
| `show device jobs id` | global | `device_jobs_read` | GET https://api.strata.paloaltonetworks.com/operations/v1/device/jobs/{id} |
| `show jobs all` | global | `show_jobs` | GET /config/setup/v1/jobs |
| `show jobs id` | global | `show_jobs` | GET /config/setup/v1/jobs/{id} |
| `show local-config download` | global | `local_config_download_read` | GET https://api.strata.paloaltonetworks.com/operations/v1/local-config/download |
| `show local-config versions` | global | `local_config_versions_read` | GET https://api.strata.paloaltonetworks.com/operations/v1/local-config/versions |
| `show log system` | device | `show_log_system` | (live device state — SSH via --remote) |
| `show log traffic` | device | `show_log_traffic` | (live device state — SSH via --remote) |
| `show system disk-space` | device | `show_system_disk_space` | (live device state — SSH via --remote) |
| `show system info` | device | `show_system_info` | GET /config/setup/v1/devices/{id} |
| `show system resources` | device | `show_system_resources` | (live device state — SSH via --remote) |

## Panos-Config

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `check data-access-passwd system` | device | `panos_config_check` | (live device state — SSH via --remote) |
| `check full-commit-required` | device | `panos_config_check` | (live device state — SSH via --remote) |
| `check pending-changes` | device | `panos_config_check` | (live device state — SSH via --remote) |
| `commit description` | device | `panos_config_commit` | (live device state — SSH via --remote) |
| `load config key` | device | `panos_config_load` | (live device state — SSH via --remote) |
| `load device-state` | device | `panos_config_load` | (live device state — SSH via --remote) |
| `save config to` | device | `panos_config_save` | (live device state — SSH via --remote) |
| `save device-state` | device | `panos_config_save` | (live device state — SSH via --remote) |
| `set deviceconfig` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig high-availability` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig high-availability enabled` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig setting autofocus` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig setting autofocus autofocus-url` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig setting autofocus enabled` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig setting autofocus query-timeout` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig setting cloud-userid` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig setting cloud-userid address` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig setting cloud-userid disabled` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig setting cloud-userid segment-assignment` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig setting cloudapp` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig setting cloudapp cloudapp-srvr-addr` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig setting cloudapp cloudapp-srvr-addr address` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig setting cloudapp disable` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig setting custom-logo` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig setting iot` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig setting iot edge` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig setting iot edge address` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig setting management admin-lockout` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig setting management admin-session` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig setting management admin-session max-session-count` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig setting management admin-session max-session-time` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig setting management api` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig setting management api key` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig setting management api key certificate` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig setting management api key lifetime` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig setting management appusage-lifetime` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig setting management audit-tracking` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig setting management audit-tracking op-commands` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig setting management audit-tracking send-syslog` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig setting management audit-tracking ui-actions` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig setting management browse-activity-report-setting` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig setting management browse-activity-report-setting average-browse-time` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig setting management browse-activity-report-setting page-load-threshold` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig setting management common-criteria self-test-schedule` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig setting management common-criteria self-test-schedule crypto start-time` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig setting management common-criteria self-test-schedule software-integrity start-time` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig setting management disable-predefined-correlation-objs` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig setting management disable-predefined-reports` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig setting management hostname-type-in-syslog` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig setting management idle-timeout` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig setting management max-audit-versions` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig setting management max-rows-in-csv-export` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig setting management max-rows-in-pdf-report` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig setting management panorama-ssl-send-retries` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig setting management panorama-tcp-receive-timeout` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig setting management panorama-tcp-send-timeout` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig setting management quota-settings` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig setting management report-expiration-period` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig setting management report-run-time` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig setting management rule-audit-comment-regex` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig setting management secure-conn-client` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig setting management secure-conn-client certificate-type local certificate` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig setting management secure-conn-client certificate-type local certificate-profile` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig setting management secure-conn-client certificate-type scep certificate-profile` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig setting management secure-conn-client certificate-type scep scep-profile` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig setting management secure-conn-server` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig setting management secure-conn-server certificate-profile` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig setting management secure-conn-server enable-secure-user-id-communication` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig setting management secure-conn-server ssl-tls-service-profile` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig setting session offload` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig setting session packet-buffer-protection-use-buffer` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig setting session persistent-dipp-alert-enable` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig setting session-tracking` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig setting session-tracking disable` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig setting session-tracking user-re-authentication` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig setting session-tracking user-re-authentication disable` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig setting ssl-decrypt use-mp-sess-cache` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig system auto-renew-mkey-lifetime` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system device-telemetry` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system device-telemetry device-health-performance` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system device-telemetry product-usage` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system device-telemetry region` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system device-telemetry threat-prevention` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system dns-security-server` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system dns-setting servers` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig system dns-setting servers primary` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig system dns-setting servers secondary` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig system geo-location` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system geo-location latitude` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system geo-location longitude` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system hsm-settings` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system hsm-settings provider` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system hsm-settings provider ciphertrust-manager hsm-server` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system hsm-settings provider ncipher-nshield-connect hsm-server` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system hsm-settings provider ncipher-nshield-connect rfs-address` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system hsm-settings provider safenet-network ha` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system hsm-settings provider safenet-network ha auto-recovery-retry` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system hsm-settings provider safenet-network ha ha-group-name` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system hsm-settings provider safenet-network hsm-server` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system inline-cloud-proxy` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system locale` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system log-link` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system motd-and-banner` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system motd-and-banner message` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system motd-and-banner severity` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system mtu` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system ntp-servers` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system ntp-servers primary-ntp-server authentication-type` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system ntp-servers primary-ntp-server authentication-type symmetric-key algorithm` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system ntp-servers primary-ntp-server authentication-type symmetric-key algorithm md5 authentication-key` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system ntp-servers primary-ntp-server authentication-type symmetric-key algorithm sha1 authentication-key` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system ntp-servers primary-ntp-server authentication-type symmetric-key key-id` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system ntp-servers primary-ntp-server ntp-server-address` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system ntp-servers secondary-ntp-server authentication-type` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system ntp-servers secondary-ntp-server authentication-type symmetric-key algorithm` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system ntp-servers secondary-ntp-server authentication-type symmetric-key algorithm md5 authentication-key` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system ntp-servers secondary-ntp-server authentication-type symmetric-key algorithm sha1 authentication-key` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system ntp-servers secondary-ntp-server authentication-type symmetric-key key-id` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system ntp-servers secondary-ntp-server ntp-server-address` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system panorama local-panorama panorama-server` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig system permitted-ip` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system secure-proxy-port` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system service` | device | `panos_config_recovery` | (live device state — SSH via --remote) |
| `set deviceconfig system snmp-setting` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system snmp-setting access-setting version` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system snmp-setting access-setting version v2c snmp-community-string` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system snmp-setting access-setting version v3 users` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system snmp-setting access-setting version v3 views` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system snmp-setting snmp-system contact` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system snmp-setting snmp-system location` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system snmp-setting snmp-system send-event-specific-traps` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system ssh` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system ssh ha ha-profile` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system ssh mgmt server-profile` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system ssh profiles ha-profiles` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system ssh profiles mgmt-profiles` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system ssh profiles mgmt-profiles server-profiles` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system ssh regenerate-hostkeys ha` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system ssh regenerate-hostkeys ha key-type` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system ssh regenerate-hostkeys ha key-type ecdsa key-length` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system ssh regenerate-hostkeys ha key-type rsa key-length` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system ssh regenerate-hostkeys mgmt` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system ssh regenerate-hostkeys mgmt key-type` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system ssh regenerate-hostkeys mgmt key-type ecdsa key-length` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system ssh regenerate-hostkeys mgmt key-type rsa key-length` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system timezone` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system type` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system type dhcp-client` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system type static` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule anti-virus` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule anti-virus recurring` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule anti-virus recurring daily` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule anti-virus recurring daily action` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule anti-virus recurring daily at` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule anti-virus recurring hourly` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule anti-virus recurring hourly action` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule anti-virus recurring hourly at` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule anti-virus recurring none` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule anti-virus recurring sync-to-peer` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule anti-virus recurring threshold` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule anti-virus recurring weekly` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule anti-virus recurring weekly action` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule anti-virus recurring weekly at` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule anti-virus recurring weekly day-of-week` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule threats` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule threats recurring` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule threats recurring daily` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule threats recurring daily action` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule threats recurring daily at` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule threats recurring daily disable-new-content` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule threats recurring every-30-mins` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule threats recurring every-30-mins action` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule threats recurring every-30-mins at` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule threats recurring every-30-mins disable-new-content` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule threats recurring hourly` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule threats recurring hourly action` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule threats recurring hourly at` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule threats recurring hourly disable-new-content` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule threats recurring new-app-threshold` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule threats recurring none` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule threats recurring sync-to-peer` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule threats recurring threshold` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule threats recurring weekly` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule threats recurring weekly action` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule threats recurring weekly at` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule threats recurring weekly day-of-week` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule threats recurring weekly disable-new-content` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule wf-private` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule wf-private recurring` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule wf-private recurring every-15-mins` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule wf-private recurring every-15-mins action` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule wf-private recurring every-15-mins at` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule wf-private recurring every-30-mins` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule wf-private recurring every-30-mins action` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule wf-private recurring every-30-mins at` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule wf-private recurring every-5-mins` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule wf-private recurring every-5-mins action` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule wf-private recurring every-5-mins at` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule wf-private recurring every-hour` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule wf-private recurring every-hour action` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule wf-private recurring every-hour at` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule wf-private recurring none` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule wf-private recurring sync-to-peer` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule wildfire` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule wildfire recurring` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule wildfire recurring every-15-mins action` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule wildfire recurring every-15-mins at` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule wildfire recurring every-15-mins sync-to-peer` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule wildfire recurring every-30-mins action` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule wildfire recurring every-30-mins at` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule wildfire recurring every-30-mins sync-to-peer` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule wildfire recurring every-hour action` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule wildfire recurring every-hour at` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule wildfire recurring every-hour sync-to-peer` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule wildfire recurring every-min action` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set deviceconfig system update-schedule wildfire recurring every-min sync-to-peer` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `set mgt-config` | device | `panos_config_mgt_config` | (live device state — SSH via --remote) |
| `set mgt-config password-complexity` | device | `panos_config_mgt_config` | (live device state — SSH via --remote) |
| `set mgt-config password-complexity block-username-inclusion` | device | `panos_config_mgt_config` | (live device state — SSH via --remote) |
| `set mgt-config password-complexity enabled` | device | `panos_config_mgt_config` | (live device state — SSH via --remote) |
| `set mgt-config password-complexity minimum-length` | device | `panos_config_mgt_config` | (live device state — SSH via --remote) |
| `set mgt-config password-complexity password-change` | device | `panos_config_mgt_config` | (live device state — SSH via --remote) |
| `set mgt-config password-complexity password-change-on-first-login` | device | `panos_config_mgt_config` | (live device state — SSH via --remote) |
| `set mgt-config password-complexity password-change-period-block` | device | `panos_config_mgt_config` | (live device state — SSH via --remote) |
| `set mgt-config password-complexity password-history-count` | device | `panos_config_mgt_config` | (live device state — SSH via --remote) |
| `set mgt-config password-profile` | device | `panos_config_mgt_config` | (live device state — SSH via --remote) |
| `set shared` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `set shared email-scheduler` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `set shared log-settings` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `set shared pdf-summary-report` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `set shared report-group` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `set shared response-page remote-browser-isolation` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `set shared response-page url-reply` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show application` | device | `panos_config_misc` | (live device state — SSH via --remote) |
| `show application-tag` | device | `panos_config_misc` | (live device state — SSH via --remote) |
| `show authentication-object` | device | `panos_config_misc` | (live device state — SSH via --remote) |
| `show captive-portal` | device | `panos_config_misc` | (live device state — SSH via --remote) |
| `show captive-portal mode` | device | `panos_config_misc` | (live device state — SSH via --remote) |
| `show captive-portal mode redirect session-cookie` | device | `panos_config_misc` | (live device state — SSH via --remote) |
| `show cloud-identity-engine` | device | `panos_config_misc` | (live device state — SSH via --remote) |
| `show device-object` | device | `panos_config_misc` | (live device state — SSH via --remote) |
| `show deviceconfig` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig high-availability` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig high-availability cluster` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig high-availability cluster cluster-members` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig high-availability group` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig high-availability group election-option timers` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig high-availability group mode active-active` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig high-availability group mode active-active network-configuration` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig high-availability group mode active-active network-configuration sync` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig high-availability group mode active-active session-owner-selection` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig high-availability group mode active-active session-owner-selection first-packet session-setup` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig high-availability group mode active-active virtual-address` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig high-availability group mode active-passive` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig high-availability group monitoring link-monitoring` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig high-availability group monitoring link-monitoring link-group` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig high-availability group monitoring path-monitoring` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig high-availability group monitoring path-monitoring path-group` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig high-availability group state-synchronization ha2-keep-alive` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig high-availability interface` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig high-availability interface ha1` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig high-availability interface ha1 encryption` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig setting` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig setting application` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig setting application traceroute` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig setting cloudapp` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig setting cloudapp cloudapp-srvr-addr` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig setting custom-logo` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig setting dhcp-syslog-server` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig setting iot` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig setting iot edge` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig setting logging` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig setting logging enhanced-application-logging disable-application` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig setting logging enhanced-application-logging disable-global` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig setting management` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig setting management api` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig setting management api key` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig setting management common-criteria` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig setting management common-criteria self-test-schedule` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig setting management common-criteria-alarm-generation` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig setting management quota-settings` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig setting management secure-conn-client` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig setting management secure-conn-client certificate-type` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig setting session-tracking` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig setting session-tracking user-re-authentication` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig setting vpn` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig setting vpn ikev2` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig setting wildfire` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig setting wildfire cloud-inline-wf-session-info-select` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig setting wildfire cloud-inline-wildfire` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig setting wildfire cloud-inline-wildfire file-size-limit` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig setting wildfire file-size-limit` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig setting wildfire session-info-select` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system dns-setting` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system dns-setting servers` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system dns-setting servers encrypted-dns` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system dns-setting servers encrypted-dns connection-type` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system hsm-settings` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system hsm-settings provider` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system hsm-settings provider ciphertrust-manager hsm-server` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system hsm-settings provider ncipher-nshield-connect hsm-server` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system hsm-settings provider safenet-network ha` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system hsm-settings provider safenet-network hsm-server` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system ipv6-gw-type` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system ipv6-type` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system log-export-schedule` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system log-link` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system ntp-servers` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system ntp-servers primary-ntp-server authentication-type` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system ntp-servers primary-ntp-server authentication-type symmetric-key algorithm` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system ntp-servers secondary-ntp-server authentication-type` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system ntp-servers secondary-ntp-server authentication-type symmetric-key algorithm` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system panorama` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system permitted-ip` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system route` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system route destination` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system route service` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system snmp-setting` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system snmp-setting access-setting version` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system snmp-setting access-setting version v3 users` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system snmp-setting access-setting version v3 views` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system ssh` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system ssh profiles ha-profiles` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system ssh profiles mgmt-profiles` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system ssh profiles mgmt-profiles server-profiles` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system ssh regenerate-hostkeys ha` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system ssh regenerate-hostkeys ha key-type` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system ssh regenerate-hostkeys mgmt` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system ssh regenerate-hostkeys mgmt key-type` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system type` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system update-schedule` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system update-schedule anti-virus recurring` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system update-schedule app-profile recurring` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system update-schedule global-protect-clientless-vpn recurring` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system update-schedule global-protect-datafile recurring` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system update-schedule threats recurring` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system update-schedule wf-private recurring` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system update-schedule wildfire recurring` | device | `panos_config_deviceconfig` | (live device state — SSH via --remote) |
| `show disable-inspect` | device | `panos_config_misc` | (live device state — SSH via --remote) |
| `show display-name` | device | `panos_config_misc` | (live device state — SSH via --remote) |
| `show dynamic-user-group` | device | `panos_config_misc` | (live device state — SSH via --remote) |
| `show email-scheduler` | device | `panos_config_misc` | (live device state — SSH via --remote) |
| `show external-list` | device | `panos_config_misc` | (live device state — SSH via --remote) |
| `show global-protect global-protect-gateway` | device | `panos_config_misc` | (live device state — SSH via --remote) |
| `show global-protect global-protect-portal` | device | `panos_config_misc` | (live device state — SSH via --remote) |
| `show group-mapping` | device | `panos_config_misc` | (live device state — SSH via --remote) |
| `show import` | device | `panos_config_misc` | (live device state — SSH via --remote) |
| `show iptag-include-exclude-list` | device | `panos_config_misc` | (live device state — SSH via --remote) |
| `show iptag-include-exclude-list include-exclude-network` | device | `panos_config_misc` | (live device state — SSH via --remote) |
| `show ipuser-include-exclude-list` | device | `panos_config_misc` | (live device state — SSH via --remote) |
| `show ipuser-include-exclude-list include-exclude-network` | device | `panos_config_misc` | (live device state — SSH via --remote) |
| `show mgt-config` | device | `panos_config_mgt_config` | (live device state — SSH via --remote) |
| `show mgt-config access-domain` | device | `panos_config_mgt_config` | (live device state — SSH via --remote) |
| `show mgt-config password-complexity` | device | `panos_config_mgt_config` | (live device state — SSH via --remote) |
| `show mgt-config password-complexity password-change` | device | `panos_config_mgt_config` | (live device state — SSH via --remote) |
| `show mgt-config password-profile` | device | `panos_config_mgt_config` | (live device state — SSH via --remote) |
| `show mgt-config users` | device | `panos_config_mgt_config` | (live device state — SSH via --remote) |
| `show network` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network dhcp` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network dhcp interface` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network dns-proxy` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network ike` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network ike crypto-profiles` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network ike crypto-profiles global-protect-app-crypto-profiles` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network ike crypto-profiles ike-crypto-profiles` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network ike crypto-profiles ipsec-crypto-profiles` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network ike gateway` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface aggregate-ethernet` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface ethernet` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface loopback` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface loopback adjust-tcp-mss` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface loopback ip` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface loopback ipv6` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface loopback ipv6 address` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface loopback units` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface sdwan` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface sdwan units` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface tunnel` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface tunnel ip` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface tunnel ipv6` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface tunnel ipv6 address` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface tunnel units` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan adjust-tcp-mss` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan arp` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ddns-config` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ddns-config ddns-vendor-config` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan dhcp-client` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan dhcp-client send-hostname` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ip` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ipv6` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ipv6 address` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ipv6 dhcp-client` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ipv6 dhcp-client neighbor-discovery dns-server` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ipv6 dhcp-client neighbor-discovery dns-server source` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ipv6 dhcp-client neighbor-discovery dns-server source manual server` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ipv6 dhcp-client neighbor-discovery dns-suffix` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ipv6 dhcp-client neighbor-discovery dns-suffix source` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ipv6 dhcp-client neighbor-discovery dns-suffix source manual suffix` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ipv6 dhcp-client neighbor-discovery neighbor` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ipv6 dhcp-client prefix-delegation enable` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ipv6 dhcp-client v6-options enable` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ipv6 inherited` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ipv6 inherited assign-addr` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ipv6 inherited neighbor-discovery` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ipv6 inherited neighbor-discovery dns-server` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ipv6 inherited neighbor-discovery dns-server source` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ipv6 inherited neighbor-discovery dns-server source manual server` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ipv6 inherited neighbor-discovery dns-suffix` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ipv6 inherited neighbor-discovery dns-suffix source` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ipv6 inherited neighbor-discovery dns-suffix source manual suffix` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ipv6 inherited neighbor-discovery neighbor` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ipv6 inherited neighbor-discovery router-advertisement` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ipv6 neighbor-discovery` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ipv6 neighbor-discovery neighbor` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ipv6 neighbor-discovery router-advertisement` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ipv6 neighbor-discovery router-advertisement dns-support` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ipv6 neighbor-discovery router-advertisement dns-support server` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ipv6 neighbor-discovery router-advertisement dns-support suffix` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ipv6 pppoe` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ipv6 pppoe dhcpv6 prefix-delegation` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ipv6 pppoe dhcpv6 prefix-delegation enable` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ipv6 pppoe dhcpv6 v6-options` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ipv6 pppoe dhcpv6 v6-options enable` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ipv6 pppoe neighbor-discovery dns-server` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ipv6 pppoe neighbor-discovery dns-server source` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ipv6 pppoe neighbor-discovery dns-server source manual server` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ipv6 pppoe neighbor-discovery dns-suffix` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ipv6 pppoe neighbor-discovery dns-suffix source` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ipv6 pppoe neighbor-discovery dns-suffix source manual suffix` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ipv6 pppoe neighbor-discovery neighbor` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ndp-proxy` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan ndp-proxy address` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network interface vlan units` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network lldp` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network logical-router` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network macsec` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network macsec crypto-profiles` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network macsec interfaces` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network macsec pre-shared-key-profiles` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network profiles` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network profiles bfd-profile` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network profiles interface-management-profile` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network profiles lldp-profile` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network profiles monitor-profile` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network profiles zone-protection-profile` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network qos` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network qos interface` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network qos profile` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network routing-profile` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network routing-profile bfd` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network routing-profile bgp` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network routing-profile bgp address-family-profile` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network routing-profile bgp auth-profile` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network routing-profile bgp dampening-profile` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network routing-profile bgp filtering-profile` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network routing-profile bgp redistribution-profile` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network routing-profile bgp timer-profile` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network routing-profile filters` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network routing-profile filters access-list` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network routing-profile filters as-path-access-list` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network routing-profile filters community-list` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network routing-profile filters prefix-list` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network routing-profile filters route-maps` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network routing-profile filters route-maps bgp bgp-entry` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network routing-profile filters route-maps redistribution redist-entry` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network routing-profile multicast` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network routing-profile ospf` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network routing-profile ospf auth-profile` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network routing-profile ospf if-timer-profile` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network routing-profile ospf redistribution-profile` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network routing-profile ospf spf-timer-profile` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network routing-profile ospfv3` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network routing-profile ospfv3 auth-profile` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network routing-profile ospfv3 if-timer-profile` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network routing-profile ospfv3 redistribution-profile` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network routing-profile ospfv3 spf-timer-profile` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network routing-profile rip` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network routing-profile rip auth-profile` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network routing-profile rip global-timer-profile` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network routing-profile rip redistribution-profile` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network tunnel` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network tunnel global-protect-gateway` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network tunnel global-protect-site-to-site` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network tunnel gre` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network tunnel ipsec` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network underlay-net` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network underlay-net ip-mapping` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network virtual-router` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network virtual-wire` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show network vlan` | device | `panos_config_network` | (live device state — SSH via --remote) |
| `show pdf-summary-report` | device | `panos_config_misc` | (live device state — SSH via --remote) |
| `show profiles` | device | `panos_config_profiles` | (live device state — SSH via --remote) |
| `show profiles data-filtering` | device | `panos_config_profiles` | (live device state — SSH via --remote) |
| `show profiles data-objects` | device | `panos_config_profiles` | (live device state — SSH via --remote) |
| `show profiles decryption` | device | `panos_config_profiles` | (live device state — SSH via --remote) |
| `show profiles dos-protection` | device | `panos_config_profiles` | (live device state — SSH via --remote) |
| `show profiles file-blocking` | device | `panos_config_profiles` | (live device state — SSH via --remote) |
| `show profiles hip-objects` | device | `panos_config_profiles` | (live device state — SSH via --remote) |
| `show profiles packet-broker` | device | `panos_config_profiles` | (live device state — SSH via --remote) |
| `show profiles sdwan-error-correction` | device | `panos_config_profiles` | (live device state — SSH via --remote) |
| `show profiles sdwan-path-quality` | device | `panos_config_profiles` | (live device state — SSH via --remote) |
| `show profiles sdwan-saas-quality` | device | `panos_config_profiles` | (live device state — SSH via --remote) |
| `show profiles sdwan-traffic-distribution` | device | `panos_config_profiles` | (live device state — SSH via --remote) |
| `show profiles spyware` | device | `panos_config_profiles` | (live device state — SSH via --remote) |
| `show profiles url-filtering` | device | `panos_config_profiles` | (live device state — SSH via --remote) |
| `show profiles virus` | device | `panos_config_profiles` | (live device state — SSH via --remote) |
| `show profiles vulnerability` | device | `panos_config_profiles` | (live device state — SSH via --remote) |
| `show profiles wildfire-analysis` | device | `panos_config_profiles` | (live device state — SSH via --remote) |
| `show redistribution-agent` | device | `panos_config_misc` | (live device state — SSH via --remote) |
| `show redistribution-collector` | device | `panos_config_misc` | (live device state — SSH via --remote) |
| `show redistribution-collector setting` | device | `panos_config_misc` | (live device state — SSH via --remote) |
| `show report-group` | device | `panos_config_misc` | (live device state — SSH via --remote) |
| `show reports` | device | `panos_config_misc` | (live device state — SSH via --remote) |
| `show route` | device | `panos_config_misc` | (live device state — SSH via --remote) |
| `show route service` | device | `panos_config_misc` | (live device state — SSH via --remote) |
| `show rulebase` | device | `panos_config_rulebase` | (live device state — SSH via --remote) |
| `show rulebase application-override rules` | device | `panos_config_rulebase` | (live device state — SSH via --remote) |
| `show rulebase authentication rules` | device | `panos_config_rulebase` | (live device state — SSH via --remote) |
| `show rulebase decryption rules` | device | `panos_config_rulebase` | (live device state — SSH via --remote) |
| `show rulebase default-security-rules rules` | device | `panos_config_rulebase` | (live device state — SSH via --remote) |
| `show rulebase dos rules` | device | `panos_config_rulebase` | (live device state — SSH via --remote) |
| `show rulebase nat rules` | device | `panos_config_rulebase` | (live device state — SSH via --remote) |
| `show rulebase network-packet-broker rules` | device | `panos_config_rulebase` | (live device state — SSH via --remote) |
| `show rulebase pbf rules` | device | `panos_config_rulebase` | (live device state — SSH via --remote) |
| `show rulebase qos rules` | device | `panos_config_rulebase` | (live device state — SSH via --remote) |
| `show rulebase sdwan rules` | device | `panos_config_rulebase` | (live device state — SSH via --remote) |
| `show rulebase security rules` | device | `panos_config_rulebase` | (live device state — SSH via --remote) |
| `show rulebase tunnel-inspect rules` | device | `panos_config_rulebase` | (live device state — SSH via --remote) |
| `show sdwan-interface-profile` | device | `panos_config_misc` | (live device state — SSH via --remote) |
| `show setting` | device | `panos_config_misc` | (live device state — SSH via --remote) |
| `show shared` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared admin-role` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared alg-override` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared alg-override application` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared authentication-profile` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared botnet` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared botnet configuration http` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared botnet configuration other-applications` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared botnet configuration unknown-applications` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared botnet configuration unknown-applications unknown-tcp session-length` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared botnet configuration unknown-applications unknown-udp session-length` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared certificate-profile` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared email-scheduler` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared local-user-database` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared local-user-database user` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared local-user-database user-group` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared log-settings` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared log-settings config` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared log-settings config match-list` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared log-settings email` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared log-settings http` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared log-settings profiles` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared log-settings snmptrap` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared log-settings syslog` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared log-settings system` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared log-settings system match-list` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared override` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared override application` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared pdf-summary-report` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared report-group` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared reports` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared response-page` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared scep` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared server-profile` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared server-profile kerberos` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared server-profile ldap` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared server-profile mfa-server-profile` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared server-profile netflow` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared server-profile radius` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared server-profile saml-idp` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared server-profile scp` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared server-profile tacplus` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared ssl-decrypt` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared ssl-decrypt forward-trust-certificate` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared ssl-decrypt forward-untrust-certificate` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared ssl-decrypt ssl-exclude-cert` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared ssl-tls-service-profile` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show shared user-id-hub` | device | `panos_config_shared` | (live device state — SSH via --remote) |
| `show threats` | device | `panos_config_misc` | (live device state — SSH via --remote) |
| `show threats spyware` | device | `panos_config_misc` | (live device state — SSH via --remote) |
| `show threats vulnerability` | device | `panos_config_misc` | (live device state — SSH via --remote) |
| `show ts-agent` | device | `panos_config_misc` | (live device state — SSH via --remote) |
| `show url-admin-override` | device | `panos_config_misc` | (live device state — SSH via --remote) |
| `show url-admin-override mode` | device | `panos_config_misc` | (live device state — SSH via --remote) |
| `show user-context-segment` | device | `panos_config_misc` | (live device state — SSH via --remote) |
| `show user-context-segment assignments` | device | `panos_config_misc` | (live device state — SSH via --remote) |
| `show user-id-collector` | device | `panos_config_user_id_collector` | (live device state — SSH via --remote) |
| `show user-id-collector include-exclude-network` | device | `panos_config_user_id_collector` | (live device state — SSH via --remote) |
| `show user-id-collector include-exclude-network-sequence` | device | `panos_config_user_id_collector` | (live device state — SSH via --remote) |
| `show user-id-collector server-monitor` | device | `panos_config_user_id_collector` | (live device state — SSH via --remote) |
| `show user-id-collector setting` | device | `panos_config_user_id_collector` | (live device state — SSH via --remote) |
| `show user-id-collector syslog-parse-profile` | device | `panos_config_user_id_collector` | (live device state — SSH via --remote) |
| `show user-id-ssl-auth` | device | `panos_config_misc` | (live device state — SSH via --remote) |
| `show vm-info-source` | device | `panos_config_misc` | (live device state — SSH via --remote) |
| `show x-authenticated-user` | device | `panos_config_misc` | (live device state — SSH via --remote) |
| `validate full` | device | `panos_config_validate` | (live device state — SSH via --remote) |
| `validate partial device-and-network` | device | `panos_config_validate` | (live device state — SSH via --remote) |

## Panos-Ops

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `clear advanced-routing bfd counters session-id` | device | `panos_clear_advanced_routing` | (live device state — SSH via --remote) |
| `clear advanced-routing bfd session-state session-id` | device | `panos_clear_advanced_routing` | (live device state — SSH via --remote) |
| `clear advanced-routing bgp logical-router` | device | `panos_clear_advanced_routing` | (live device state — SSH via --remote) |
| `clear advanced-routing multicast igmp membership logical-router` | device | `panos_clear_advanced_routing` | (live device state — SSH via --remote) |
| `clear advanced-routing multicast igmp statistics logical-router` | device | `panos_clear_advanced_routing` | (live device state — SSH via --remote) |
| `clear advanced-routing multicast mroute logical-router` | device | `panos_clear_advanced_routing` | (live device state — SSH via --remote) |
| `clear advanced-routing multicast msdp sa logical-router` | device | `panos_clear_advanced_routing` | (live device state — SSH via --remote) |
| `clear advanced-routing multicast msdp statistics logical-router` | device | `panos_clear_advanced_routing` | (live device state — SSH via --remote) |
| `clear advanced-routing multicast pim statistics logical-router` | device | `panos_clear_advanced_routing` | (live device state — SSH via --remote) |
| `clear application-signature statistics` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear arp interface` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear audit-comment xpath` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear auto-tag vsys` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear bonjour interface` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear cluster-flow all` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear cluster-flow id` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear cookie-surrogate-cache all` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear cookie-surrogate-cache username` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear counter all` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear counter global filter category` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear counter global name` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear counter interface` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear device-cache-mp all` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear device-cache-mp ip` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear dhcp lease all expired-only` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear dhcp lease interface` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear dns-proxy cache all domain-name` | device | `panos_clear_dns_proxy` | (live device state — SSH via --remote) |
| `clear dns-proxy cache name` | device | `panos_clear_dns_proxy` | (live device state — SSH via --remote) |
| `clear dns-proxy dns-signature cache fqdn` | device | `panos_clear_dns_proxy` | (live device state — SSH via --remote) |
| `clear dns-proxy dns-signature counters` | device | `panos_clear_dns_proxy` | (live device state — SSH via --remote) |
| `clear dns-proxy encrypted-dns` | device | `panos_clear_dns_proxy` | (live device state — SSH via --remote) |
| `clear dns-proxy statistics all` | device | `panos_clear_dns_proxy` | (live device state — SSH via --remote) |
| `clear dns-proxy statistics name` | device | `panos_clear_dns_proxy` | (live device state — SSH via --remote) |
| `clear dos-block-table all filter source-ip` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear dos-block-table drop-counter` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear dos-protection rule` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear dos-protection zone` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear global-protect redirect location` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear global-protect-portal statistics portal` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear high-availability cluster statistics` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear high-availability control-link statistics` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear high-availability transitions` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear job id` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear lacp counters aggregate-ethernet` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear lldp counters all` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear lldp counters interface` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear log` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear logrcvr offline-logpurger` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear mac` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear nat-rule-cache rule` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear neighbor interface` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear neighbor ndp-monitor` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear net-inspection filter` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear pbf return-mac all` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear pbf return-mac name` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear pbf rule all` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear pbf rule name` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear policy-app-usage-data ruleuuid` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear pppoe interface` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear pppoe ipv6 interface` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear query all-by-session` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear query id` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear report all-by-session` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear report cache` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear report id` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear resiliency statistics` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear routing bfd counters session-id` | device | `panos_clear_routing` | (live device state — SSH via --remote) |
| `clear routing bfd session-state session-id` | device | `panos_clear_routing` | (live device state — SSH via --remote) |
| `clear routing bgp virtual-router` | device | `panos_clear_routing` | (live device state — SSH via --remote) |
| `clear routing multicast igmp statistics virtual-router` | device | `panos_clear_routing` | (live device state — SSH via --remote) |
| `clear routing multicast pim statistics virtual-router` | device | `panos_clear_routing` | (live device state — SSH via --remote) |
| `clear rule-hit-count vsys` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear sdwan event` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear sdwan pool unsuccess` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear session all filter nat` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear session id` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear snmpd refresh-timer-period` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear ssl-cert-cn` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear ssl-decrypt exclude-cache server` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear statistics` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear uappid-filtergroup-mapping all` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear uappid-filtergroup-mapping id` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear uappid-policy-cache all` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear uappid-policy-cache id` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear ueip address` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear ueip all` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear uid-cache all` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear uid-cache uid` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear uid-map-cache all` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear uid-map-cache uid` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear url-cache all` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear url-cache url` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear user-cache all type` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear user-cache ip` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear user-cache-mp all type` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear user-cache-mp ip` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear user-policy-cache all` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear user-policy-cache uid` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear vpn flow tunnel-id` | device | `panos_clear_vpn` | (live device state — SSH via --remote) |
| `clear vpn ike-hashurl` | device | `panos_clear_vpn` | (live device state — SSH via --remote) |
| `clear vpn ike-preferred-version gateway` | device | `panos_clear_vpn` | (live device state — SSH via --remote) |
| `clear vpn ike-sa gateway` | device | `panos_clear_vpn` | (live device state — SSH via --remote) |
| `clear vpn ipsec-sa tunnel` | device | `panos_clear_vpn` | (live device state — SSH via --remote) |
| `clear wildfire counters` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear xml-api multiusersystem cloud` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `clear zone-protection zone` | device | `panos_clear_misc` | (live device state — SSH via --remote) |
| `debug advanced-routing` | device | `panos_debug_advanced_routing` | (live device state — SSH via --remote) |
| `debug advanced-routing bgp` | device | `panos_debug_advanced_routing` | (live device state — SSH via --remote) |
| `debug advanced-routing bgp updates in peer-name` | device | `panos_debug_advanced_routing` | (live device state — SSH via --remote) |
| `debug advanced-routing bgp updates out peer-name` | device | `panos_debug_advanced_routing` | (live device state — SSH via --remote) |
| `debug advanced-routing daemon-status logical-router` | device | `panos_debug_advanced_routing` | (live device state — SSH via --remote) |
| `debug advanced-routing fib check` | device | `panos_debug_advanced_routing` | (live device state — SSH via --remote) |
| `debug advanced-routing fib clear logical-router` | device | `panos_debug_advanced_routing` | (live device state — SSH via --remote) |
| `debug advanced-routing fib flush` | device | `panos_debug_advanced_routing` | (live device state — SSH via --remote) |
| `debug advanced-routing fib stats` | device | `panos_debug_advanced_routing` | (live device state — SSH via --remote) |
| `debug advanced-routing fqdn display logical-router` | device | `panos_debug_advanced_routing` | (live device state — SSH via --remote) |
| `debug advanced-routing global off` | device | `panos_debug_advanced_routing` | (live device state — SSH via --remote) |
| `debug advanced-routing global on` | device | `panos_debug_advanced_routing` | (live device state — SSH via --remote) |
| `debug advanced-routing global show` | device | `panos_debug_advanced_routing` | (live device state — SSH via --remote) |
| `debug advanced-routing mpf offload` | device | `panos_debug_advanced_routing` | (live device state — SSH via --remote) |
| `debug advanced-routing mpf stats` | device | `panos_debug_advanced_routing` | (live device state — SSH via --remote) |
| `debug advanced-routing ospfv3 logical-router` | device | `panos_debug_advanced_routing` | (live device state — SSH via --remote) |
| `debug advanced-routing path-monitor id` | device | `panos_debug_advanced_routing` | (live device state — SSH via --remote) |
| `debug advanced-routing pcap` | device | `panos_debug_advanced_routing` | (live device state — SSH via --remote) |
| `debug advanced-routing pcap show` | device | `panos_debug_advanced_routing` | (live device state — SSH via --remote) |
| `debug advanced-routing qtrace disable afi` | device | `panos_debug_advanced_routing` | (live device state — SSH via --remote) |
| `debug advanced-routing qtrace enable afi` | device | `panos_debug_advanced_routing` | (live device state — SSH via --remote) |
| `debug advanced-routing qtrace flush-log` | device | `panos_debug_advanced_routing` | (live device state — SSH via --remote) |
| `debug advanced-routing qtrace show afi` | device | `panos_debug_advanced_routing` | (live device state — SSH via --remote) |
| `debug advanced-routing restart` | device | `panos_debug_advanced_routing` | (live device state — SSH via --remote) |
| `debug advanced-routing zebra events enable` | device | `panos_debug_advanced_routing` | (live device state — SSH via --remote) |
| `debug advanced-routing zebra fpm enable` | device | `panos_debug_advanced_routing` | (live device state — SSH via --remote) |
| `debug advanced-routing zebra kernel msgdump logical-router` | device | `panos_debug_advanced_routing` | (live device state — SSH via --remote) |
| `debug advanced-routing zebra nht detailed` | device | `panos_debug_advanced_routing` | (live device state — SSH via --remote) |
| `debug advanced-routing zebra packet logical-router` | device | `panos_debug_advanced_routing` | (live device state — SSH via --remote) |
| `debug advanced-routing zebra rib detailed` | device | `panos_debug_advanced_routing` | (live device state — SSH via --remote) |
| `debug authentication` | device | `panos_debug_authentication` | (live device state — SSH via --remote) |
| `debug authentication api-key-show key` | device | `panos_debug_authentication` | (live device state — SSH via --remote) |
| `debug authentication connection-debug-off protocol-type` | device | `panos_debug_authentication` | (live device state — SSH via --remote) |
| `debug authentication connection-debug-on protocol-type` | device | `panos_debug_authentication` | (live device state — SSH via --remote) |
| `debug authentication connection-show protocol-type` | device | `panos_debug_authentication` | (live device state — SSH via --remote) |
| `debug authentication on` | device | `panos_debug_authentication` | (live device state — SSH via --remote) |
| `debug authentication set-tacacs-acct-task-q-size qsize` | device | `panos_debug_authentication` | (live device state — SSH via --remote) |
| `debug authentication test-tacacs-acct-server-connection address` | device | `panos_debug_authentication` | (live device state — SSH via --remote) |
| `debug bfd global off` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug bfd global on` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug bfd global show` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug cli` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug cloud-appid ace-server` | device | `panos_debug_cloud_appid` | (live device state — SSH via --remote) |
| `debug cloud-appid cloud-manual-pull` | device | `panos_debug_cloud_appid` | (live device state — SSH via --remote) |
| `debug cloud-appid delete-signature-data app-name` | device | `panos_debug_cloud_appid` | (live device state — SSH via --remote) |
| `debug cloud-appid delete-signature-data appid` | device | `panos_debug_cloud_appid` | (live device state — SSH via --remote) |
| `debug cloud-appid delete-signature-data filter-signature-id` | device | `panos_debug_cloud_appid` | (live device state — SSH via --remote) |
| `debug cloud-appid dump config` | device | `panos_debug_cloud_appid` | (live device state — SSH via --remote) |
| `debug cloud-appid keep-task-file` | device | `panos_debug_cloud_appid` | (live device state — SSH via --remote) |
| `debug cloud-appid reset` | device | `panos_debug_cloud_appid` | (live device state — SSH via --remote) |
| `debug cloud-appid reset signature-dp option` | device | `panos_debug_cloud_appid` | (live device state — SSH via --remote) |
| `debug cloud-appid set config` | device | `panos_debug_cloud_appid` | (live device state — SSH via --remote) |
| `debug cloud-appid unknown-signature-query app-name` | device | `panos_debug_cloud_appid` | (live device state — SSH via --remote) |
| `debug cloud-appid unknown-signature-query appid` | device | `panos_debug_cloud_appid` | (live device state — SSH via --remote) |
| `debug cloud-appid unknown-signature-query filter-sig-id` | device | `panos_debug_cloud_appid` | (live device state — SSH via --remote) |
| `debug cloud-userid clear-cookie type` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug cloud-userid reset-connection` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug cloud-userid reset-counters` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug contentd status` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug cord corr-mgr off` | device | `panos_debug_cord` | (live device state — SSH via --remote) |
| `debug cord corr-mgr on` | device | `panos_debug_cord` | (live device state — SSH via --remote) |
| `debug cord corr-mgr show back-query status` | device | `panos_debug_cord` | (live device state — SSH via --remote) |
| `debug cord corr-mgr show brief` | device | `panos_debug_cord` | (live device state — SSH via --remote) |
| `debug cord corr-mgr show failed` | device | `panos_debug_cord` | (live device state — SSH via --remote) |
| `debug cord corr-mgr show filter search object` | device | `panos_debug_cord` | (live device state — SSH via --remote) |
| `debug cord corr-mgr show instance search category` | device | `panos_debug_cord` | (live device state — SSH via --remote) |
| `debug cord corr-mgr show instance summary` | device | `panos_debug_cord` | (live device state — SSH via --remote) |
| `debug cord corr-mgr show object id` | device | `panos_debug_cord` | (live device state — SSH via --remote) |
| `debug cord corr-mgr show object list` | device | `panos_debug_cord` | (live device state — SSH via --remote) |
| `debug cord corr-mgr stats clear object` | device | `panos_debug_cord` | (live device state — SSH via --remote) |
| `debug cord corr-mgr stats show object` | device | `panos_debug_cord` | (live device state — SSH via --remote) |
| `debug cord delete db` | device | `panos_debug_cord` | (live device state — SSH via --remote) |
| `debug cord delete events objectname` | device | `panos_debug_cord` | (live device state — SSH via --remote) |
| `debug cord delete instances match` | device | `panos_debug_cord` | (live device state — SSH via --remote) |
| `debug cord object-stats clear` | device | `panos_debug_cord` | (live device state — SSH via --remote) |
| `debug cord object-stats set` | device | `panos_debug_cord` | (live device state — SSH via --remote) |
| `debug cord object-stats show` | device | `panos_debug_cord` | (live device state — SSH via --remote) |
| `debug cord object-stats show-setting` | device | `panos_debug_cord` | (live device state — SSH via --remote) |
| `debug cord off` | device | `panos_debug_cord` | (live device state — SSH via --remote) |
| `debug cord on` | device | `panos_debug_cord` | (live device state — SSH via --remote) |
| `debug cord show` | device | `panos_debug_cord` | (live device state — SSH via --remote) |
| `debug cord stats` | device | `panos_debug_cord` | (live device state — SSH via --remote) |
| `debug cryptod clear hsm-key-cache` | device | `panos_debug_cryptod` | (live device state — SSH via --remote) |
| `debug cryptod global off` | device | `panos_debug_cryptod` | (live device state — SSH via --remote) |
| `debug cryptod global on` | device | `panos_debug_cryptod` | (live device state — SSH via --remote) |
| `debug cryptod global show` | device | `panos_debug_cryptod` | (live device state — SSH via --remote) |
| `debug cryptod show counters` | device | `panos_debug_cryptod` | (live device state — SSH via --remote) |
| `debug cryptod show hsm-thread all` | device | `panos_debug_cryptod` | (live device state — SSH via --remote) |
| `debug cryptod show hsm-thread index` | device | `panos_debug_cryptod` | (live device state — SSH via --remote) |
| `debug dataplane appinfo clear` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane cloud-appid lookup filter-sig-id` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane cloud-appid lookup global-id` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane cloud-appid lookup local-id` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane cloud-appid lookup name` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane cloud-appid reset cache all` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane cloud-appid reset cache appid` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane cloud-appid reset cache hash-slot` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane cloud-appid set report-overlap` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane cloud-appid show` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane cloud-appid show app-sig type` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane cloud-appid show cache` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane cloud-appid show database details` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane cloud-appid show detection` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane ctd-agent adns-telemetry debug` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane ctd-agent adns-telemetry debug-log` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane ctd-agent adns-telemetry freeze` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane ctd-agent adns-telemetry set interval-ms` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane ctd-agent adns-telemetry set max-cache-entry` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane ctd-agent adns-telemetry show` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane ctd-agent adns-telemetry stop` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane ctd-agent clear all` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane ctd-agent config` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane ctd-agent device-cert` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane ctd-agent global off` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane ctd-agent global on` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane ctd-agent global show` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane ctd-agent license` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane ctd-agent reset security-client` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane ctd-agent session id` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane ctd-agent set ace-debug` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane ctd-agent set cloud-trace` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane ctd-agent set host` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane ctd-agent set port` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane ctd-agent set source` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane flow-control disable slot` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane flow-control enable slot` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane flush-log` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane fpga hw_aho offload-bytes-threshold` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane fpga hw_aho offload-request-threshold` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane fpga hw_dfa offload-bytes-threshold` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane fpga hw_dfa offload-request-threshold` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane fpga set sw_aho` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane fpga set sw_dfa` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane fpga state` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt abort` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt bcm counters` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt bcm lport shaper get lport` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt bcm show congestion` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt bcm show flow flow_id` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt bcm show port` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt bcm show queue` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt ce10 cip` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt ce10 dfa` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt ce10 dxaui info instance` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt ce10 dxge info instance` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt ce10 dxge stats instance` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt ce10 pbm status instance` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt ce10 rd instance` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt ce10 show` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt ce10 show-all` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 acl dump count` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 csr` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 csr rd addr` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 csr scan regex` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 csr wr_sem_ctrl_ctr_scan_dis value` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 csr wr_sem_fcr_max_upd_thresh_cfg_pkt_ctr value` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 ddr eye intf` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 debug check` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 dphy_reg rd dcfg` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 event dump count` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 event fetch offset` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 flow ctrs` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 flow dump offset` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 flow histo` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 flow lookup saddr` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 flow tbl_size` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 lag dump count` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 lef dump count` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 lif access table` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 lif dump count` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 lif lookup table` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 lif stats clear` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 lif tbl_size` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 mac dump offset` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 mem rd target_mem` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 nexthop dump type` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 nif check_port` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 nif pkt_cap disable intf` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 nif pkt_cap display intf` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 nif pkt_cap enable intf` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 nif pkt_cap help` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 predict dump count` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 qmap dump pt` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 rd offset` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 route dump pt` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 show config` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 show fc clear` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 show intr` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 show latency` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 show stats` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 show stats port port` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 show status` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 tmi check_port` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 tmi pkt_cap disable intf` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 tmi pkt_cap display intf` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 tmi pkt_cap enable intf` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 tmi pkt_cap help` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 traffic info` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 umctl2_reg rd dcfg` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt fe100 vsys dump count` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt nac aho dump instance` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt nac dfa dump instance` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt nac info instance` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt nac show-all` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt nac stats instance` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt oct bgx config bgx` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt oct bgx status bgx` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt oct bootmem` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt oct csr rd reg` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt oct fpa show` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt oct gmx stats port` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt oct ilk` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt oct pip stats port` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt oct pki dump` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt oct pki port_config port` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt oct pki stats` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt oct pko debug port` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt oct pko stats all` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt oct pko stats port` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt oct pko3` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt oct portmap show` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt oct pow debug all` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal pdt pci list` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal vif` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane internal vif route` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane memory dump bootmem delete file` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane memory dump bootmem disable` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane memory dump bootmem enable log_disk_percent` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane memory dump bootmem show` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane memory status` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane mica reset cache` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane mica reset request-meta-cache adns` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane mica reset rtt` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane mica set cache adns` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane mica set cache default` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane mica set cache disable` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane mica set cache enable` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane mica set cache tp` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane mica set cache url` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane mica set inwf-mlav-prefilter` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane mica set mlc2-http-ldl-prefilter` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane mica set mlc2-micaflag-prefilter` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane mica set request-meta-cache adns` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane mica set telemetry adns-interval` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane mica show cache adns` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane mica show cache tp` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane mica show cache url` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane mica show config` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane mica show request-meta-cache adns entries` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane mica show rtt service` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane mmdbg leakiller memory-pool enable` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane mmdbg leakiller memory-pool show` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane mmdbg leakiller swbuf-pool enable` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane mmdbg leakiller swbuf-pool show` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane mmdbg obj-trace ev_num_per_q set` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane mmdbg obj-trace session level` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane mmdbg obj-trace shared-pool-192 level` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane mmdbg obj-trace shared-pool-24 level` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane mmdbg obj-trace stop` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane mmdbg obj-trace symbol lvl` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane mmdbg obj-trace wqe delay-free` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane mmdbg obj-trace wqe extra-trace` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane mmdbg obj-trace wqe leak-dump num` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane mmdbg obj-trace wqe level` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane mmdbg obj-trace wqe trace-type` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane mmdbg pool-debug overflow-check` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane mmdbg pool-debug reuse-check` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane mmdbg status` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane mmdbg watchpoint address s1dp0` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane monitor detail` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane nat static-mapping add from-ip` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane nat static-mapping del from-ip` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane nat static-mapping show` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane nat sync-ippool rule` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane netflow` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane oprofile opcontrol` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane oprofile opreport` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag aggregate-logs log_name` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag clear all` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag clear capture all` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag clear capture snaplen` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag clear capture stage` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag clear capture trigger` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag clear capture username` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag clear filter index` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag clear filter-marked-session all` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag clear filter-marked-session id` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag clear log counter` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag clear log feature` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag clear log feature all` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag clear log feature appid` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag clear log feature base` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag clear log feature cfg` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag clear log feature ctd` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag clear log feature flow` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag clear log feature misc` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag clear log feature module` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag clear log feature ssl` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag clear log feature tcp` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag clear log feature tdb` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag clear log feature tunnel` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag clear log feature url_trie` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag clear log log` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag set capture off` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag set capture on` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag set capture snaplen` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag set capture stage` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag set capture stage clientless-vpn-client file` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag set capture stage clientless-vpn-server file` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag set capture trigger application from` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag set capture username` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag set filter index` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag set filter match ingress-interface` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag set filter off` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag set filter offload` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag set filter on` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag set filter pre-parse-match` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag set filter-marked-session id` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag set log buffer-threshold` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag set log counter` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag set log cpu-threshold` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag set log feature` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag set log feature all` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag set log feature appid` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag set log feature base` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag set log feature cfg` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag set log feature ctd` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag set log feature flow` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag set log feature misc` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag set log feature module` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag set log feature ssl` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag set log feature tcp` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag set log feature tdb` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag set log feature tunnel` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag set log feature url_trie` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag set log log-option throttle` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag set log off` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag set log on` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag set log timeout` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag set tag` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-diag show` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-path-test counter` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane packet-path-test test proc` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane policy cache-usage-threshold` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane policy switch-cache` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane pool check hardware` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane pool check software` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane pool elastic delete profile name` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane pool elastic reset-defaults` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane pool elastic select-profile name` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane pool elastic set mode` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane pool elastic set profile name` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane pool elastic show config` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane pool elastic show profile active` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane pool elastic show profile all` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane pool elastic show profile capacity` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane pool elastic show profile name` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane pool mem file` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane pool memseg name common sz-pct` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane pool reset-max-usage` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane pool set` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane pool set off` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane pool set on name dthreat` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane pool set on name fptcp sessid-cid` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane pool set on name vcheck` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane pool show all top` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane pool show history top` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane pool show in-use top` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane pool statistics` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane pow performance all core` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane pow performance core` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane pow performance filter` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane pow performance rx_tx_ltncy` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane pow status filter worker` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane pow status global-counters pretty` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane pow status high-watermark reset` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane pow status inflightonly reset` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane pow status niconly brief` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane pow status niconly filter worker` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane pow status nonic reset` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane pow status nosleep filter worker` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane process` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane process cmd off` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane process cmd on` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane process cmd show` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane process comm off` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane process comm on` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane process comm profile-cache` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane process comm show` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane process mprelay off` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane process mprelay on` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane process mprelay show` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane process task dynamic-filter` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane process task off` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane process task on` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane process task show` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane pvst sys-id-ext-rewrite` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane reset` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane reset appid cache` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane reset appid statistics` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane reset appid unknown-cache destination` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane reset ctd` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane reset ctd dns-cache host` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane reset ctd feature-forward stats` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane reset ctd url-block-cache lockout` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane reset ctd wf-cache virus-pattern-type` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane reset dns-cache all` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane reset dns-cache fqdn` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane reset dos block-table` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane reset dos classification-table` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane reset dos rule` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane reset dos zone` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane reset ml-block-cache all` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane reset ml-block-cache url` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane reset ssl-decrypt` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane reset ssl-decrypt notify-cache source` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane set` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane set blocked-forward upload` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane set ctd autogen` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane set ctd ldl-model-enable` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane set ctd wildfire max` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane set ip6-mcast-fwd-check` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane set pbf-no-return-mac-learning` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane set pow no-desched` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane set qos-setting qos-param qlimit` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane set ssl-decrypt blk-send-reset` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane set ssl-decrypt ecdhe-aggressive-keying` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show app-filter-policy vsys` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show app-group-policy vsys` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show ctd` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show ctd credential-enforcement domain-credential` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show ctd credential-enforcement group-mapping vsys` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show ctd dns-cache entries host` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show ctd dns-cache stats` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show ctd feature-forward` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show ctd feature-forward forward-info session-id` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show ctd ldl status` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show ctd lscan app-sig type` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show ctd lscan database context prefix` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show ctd lscan database context-list` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show ctd lscan database details` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show ctd lscan sml-scope appid` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show ctd lscan sml-token appid` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show ctd regex-group dump` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show ctd regex-stats dump` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show ctd session` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show ctd threat id` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show ctd wf-cache virus-pattern-type` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show ctd wif service-mapping` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show ctd wildfire max` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show dns-cache print` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show dns-cache query fqdn` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show dns-cache statistics` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show dos block-table` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show dos classification-table` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show dos free-list` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show dos rule` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show dos zone` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show gtp session-qinfo` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show http2` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show http2 session` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show pow no-desched` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show qos-param qos-qlimit-sw` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show ssl-decrypt bitmask-cipher` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show ssl-decrypt bitmask-version` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show ssl-decrypt dns-cache` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show ssl-decrypt session` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show ssl-decrypt ssl-stats` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show uappid-filtergroup-mapping id` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show uappid-in-policy id` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show uappid-policy-cache uappid` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane show unknown-uappid-cache id` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane task-heartbeat` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane tcp state` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane test dump-nw-id-ebl-tble` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane test dump-nw-id-vsys-tble vsysid` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane test nat-policy-add from` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane test nat-policy-del from` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane test nw-id-lookup vsysid` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane test tunnel-tables` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane test uappid-filtergroup-mapping uappid` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane test uappid-policy-cache uappid` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane test url` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane test url-bloom` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug dataplane test url-from-file max-per-sec` | device | `panos_debug_dataplane` | (live device state — SSH via --remote) |
| `debug device-server` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server clear` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump app-containers name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump app-filters vsys` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump app-groups vsys` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump apps vsys` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump com` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump dynamic-address-group vsys` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump fqdn type dnat vsys` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump fqdn type pbf vsys` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump fqdn type policy vsys` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr global` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr high-availability state` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type dns-proxy all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type dns-proxy id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type dns-proxy name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type edl-domain all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type edl-domain id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type edl-domain name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type edl-ip all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type edl-ip id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type edl-ip name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type hip-profile all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type hip-profile id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type hip-profile name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type http-header-insert-header-value-l all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type http-header-insert-header-value-l id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type http-header-insert-header-value-l name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type http-header-insert-header-value-s all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type http-header-insert-header-value-s id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type http-header-insert-header-value-s name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type interface-group all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type interface-group id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type interface-group name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type macl-rule all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type macl-rule id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type macl-rule name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type monitor-tag all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type monitor-tag id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type monitor-tag name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type ospfv3-virtual-link all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type ospfv3-virtual-link id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type ospfv3-virtual-link name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type sdwan-link-tag all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type sdwan-link-tag id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type sdwan-link-tag name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type shared-app-signature all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type shared-app-signature id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type shared-app-signature name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type shared-application-filter all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type shared-application-filter id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type shared-application-filter name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type shared-application-group all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type shared-application-group id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type shared-application-group name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type shared-bgp-aggr-address all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type shared-bgp-aggr-address id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type shared-bgp-aggr-address name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type shared-bgp-peer all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type shared-bgp-peer id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type shared-bgp-peer name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type shared-bgp-peergrp all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type shared-bgp-peergrp id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type shared-bgp-peergrp name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type shared-qos-group all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type shared-qos-group id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type shared-qos-group name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type shared-region all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type shared-region id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type shared-region name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type shared-spyware all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type shared-spyware id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type shared-spyware name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type shared-url-filtering all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type shared-url-filtering id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type shared-url-filtering name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type tci-rule all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type tci-rule id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type tci-rule name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type vsys-app-signature all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type vsys-app-signature id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type vsys-app-signature name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type vsys-application-filter all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type vsys-application-filter id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type vsys-application-filter name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type vsys-application-group all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type vsys-application-group id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type vsys-application-group name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type vsys-region all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type vsys-region id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type vsys-region name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type vsys-spyware all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type vsys-spyware id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type vsys-spyware name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type vsys-url-filtering all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type vsys-url-filtering id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr redis type vsys-url-filtering name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type dns-proxy all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type dns-proxy id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type dns-proxy name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type edl-domain all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type edl-domain id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type edl-domain name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type edl-ip all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type edl-ip id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type edl-ip name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type hip-profile all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type hip-profile id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type hip-profile name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type http-header-insert-header-value-l all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type http-header-insert-header-value-l id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type http-header-insert-header-value-l name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type http-header-insert-header-value-s all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type http-header-insert-header-value-s id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type http-header-insert-header-value-s name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type interface-group all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type interface-group id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type interface-group name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type macl-rule all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type macl-rule id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type macl-rule name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type monitor-tag all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type monitor-tag id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type monitor-tag name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type ospfv3-virtual-link all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type ospfv3-virtual-link id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type ospfv3-virtual-link name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type sdwan-link-tag all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type sdwan-link-tag id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type sdwan-link-tag name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type shared-app-signature all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type shared-app-signature id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type shared-app-signature name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type shared-application-filter all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type shared-application-filter id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type shared-application-filter name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type shared-application-group all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type shared-application-group id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type shared-application-group name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type shared-bgp-aggr-address all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type shared-bgp-aggr-address id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type shared-bgp-aggr-address name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type shared-bgp-peer all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type shared-bgp-peer id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type shared-bgp-peer name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type shared-bgp-peergrp all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type shared-bgp-peergrp id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type shared-bgp-peergrp name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type shared-qos-group all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type shared-qos-group id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type shared-qos-group name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type shared-region all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type shared-region id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type shared-region name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type shared-spyware all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type shared-spyware id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type shared-spyware name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type shared-url-filtering all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type shared-url-filtering id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type shared-url-filtering name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type tci-rule all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type tci-rule id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type tci-rule name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type vsys-app-signature all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type vsys-app-signature id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type vsys-app-signature name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type vsys-application-filter all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type vsys-application-filter id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type vsys-application-filter name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type vsys-application-group all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type vsys-application-group id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type vsys-application-group name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type vsys-region all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type vsys-region id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type vsys-region name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type vsys-spyware all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type vsys-spyware id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type vsys-spyware name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type vsys-url-filtering all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type vsys-url-filtering id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump idmgr type vsys-url-filtering name` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump logging statistics` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump memory` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump ml7-idblob-flatbuf statistics` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump pan-url-db statistics` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump regips ip` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump regips iprange` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump regips summary` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump regips tag` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server dump tag-table tag` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server ldl show status` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server mlav clear-cache` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server mlav revert-model filetype-id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server mlav set-cloud-url default` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server mlav set-cloud-url url` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server off` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server on` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server pan-url-db` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server pan-url-db db-backup back-duration` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server pcap` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server pcap logical-router on logicalrouter` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server pcap virtual-router on virtualrouter` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server reset com statistics` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server reset config` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server reset id-manager type` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server reset logging statistics` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server set all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server set base` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server set config` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server set misc` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server set mlav` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server set tdb` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server set third-party` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server set url` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server set url_trie` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server set wfrt` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server show` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server test admin-override-password` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server test botnet-domain` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server test dynamic-url cloud` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server test idmgr-change-max type` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server test idmgr-change-max type global-router new-max-id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server test idmgr-change-max type shared-custom-url-category new-max-id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server test idmgr-change-max type ssl-rule new-max-id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server test idmgr-change-max type vsys-application new-max-id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server test idmgr-change-max type vsys-custom-url-category new-max-id` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server test idmgr-restore-default-max type` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server test ldl-model path` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server test ml7-blob path` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server test nw_id options` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server test url-category` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server trigger addrobjrefresh` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server unset all` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server unset base` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server unset config` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server unset misc` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server unset mlav` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server unset tdb` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server unset third-party` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server unset url` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server unset url_trie` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-server unset wfrt` | device | `panos_debug_device_server` | (live device state — SSH via --remote) |
| `debug device-telemetry` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug dhcpd cluster` | device | `panos_debug_dhcpd` | (live device state — SSH via --remote) |
| `debug dhcpd downgrade convert-db` | device | `panos_debug_dhcpd` | (live device state — SSH via --remote) |
| `debug dhcpd global off` | device | `panos_debug_dhcpd` | (live device state — SSH via --remote) |
| `debug dhcpd global on` | device | `panos_debug_dhcpd` | (live device state — SSH via --remote) |
| `debug dhcpd global show` | device | `panos_debug_dhcpd` | (live device state — SSH via --remote) |
| `debug dhcpd high-availability ignore-config-sync` | device | `panos_debug_dhcpd` | (live device state — SSH via --remote) |
| `debug dhcpd pcap` | device | `panos_debug_dhcpd` | (live device state — SSH via --remote) |
| `debug dhcpd pcap logical-router on logicalrouter` | device | `panos_debug_dhcpd` | (live device state — SSH via --remote) |
| `debug dhcpd pcap virtual-router on virtualrouter` | device | `panos_debug_dhcpd` | (live device state — SSH via --remote) |
| `debug dhcpd show objects` | device | `panos_debug_dhcpd` | (live device state — SSH via --remote) |
| `debug distributord dump relay` | device | `panos_debug_distributord` | (live device state — SSH via --remote) |
| `debug distributord dump relay-ipc-iotd state` | device | `panos_debug_distributord` | (live device state — SSH via --remote) |
| `debug distributord dump relay-ipc-useridd` | device | `panos_debug_distributord` | (live device state — SSH via --remote) |
| `debug distributord hip-relay hip-report-dedup-cache-size set` | device | `panos_debug_distributord` | (live device state — SSH via --remote) |
| `debug distributord hip-relay hip-report-dedup-cache-size show` | device | `panos_debug_distributord` | (live device state — SSH via --remote) |
| `debug distributord hip-relay hip-report-in-cache-aging-interval set` | device | `panos_debug_distributord` | (live device state — SSH via --remote) |
| `debug distributord hip-relay hip-report-in-cache-aging-interval show` | device | `panos_debug_distributord` | (live device state — SSH via --remote) |
| `debug distributord hip-relay reset-hip-report-dedup-cache` | device | `panos_debug_distributord` | (live device state — SSH via --remote) |
| `debug distributord max-handle-concurrent-clients set` | device | `panos_debug_distributord` | (live device state — SSH via --remote) |
| `debug distributord max-handle-concurrent-clients show` | device | `panos_debug_distributord` | (live device state — SSH via --remote) |
| `debug distributord off` | device | `panos_debug_distributord` | (live device state — SSH via --remote) |
| `debug distributord on` | device | `panos_debug_distributord` | (live device state — SSH via --remote) |
| `debug distributord redis-connection-pool ip-user set` | device | `panos_debug_distributord` | (live device state — SSH via --remote) |
| `debug distributord redis-connection-pool ip-user show` | device | `panos_debug_distributord` | (live device state — SSH via --remote) |
| `debug distributord redis-connection-pool other-data-types enable` | device | `panos_debug_distributord` | (live device state — SSH via --remote) |
| `debug distributord redis-connection-pool other-data-types set` | device | `panos_debug_distributord` | (live device state — SSH via --remote) |
| `debug distributord redis-connection-pool other-data-types show` | device | `panos_debug_distributord` | (live device state — SSH via --remote) |
| `debug distributord relay relay-ipc-iotd set qsize` | device | `panos_debug_distributord` | (live device state — SSH via --remote) |
| `debug distributord relay relay-ipc-iotd set relay-iotd-recv-cache-qsize` | device | `panos_debug_distributord` | (live device state — SSH via --remote) |
| `debug distributord relay relay-ipc-iotd set relay-iotd-recv-read-batch-size` | device | `panos_debug_distributord` | (live device state — SSH via --remote) |
| `debug distributord relay relay-ipc-iotd show` | device | `panos_debug_distributord` | (live device state — SSH via --remote) |
| `debug distributord relay relay-ipc-useridd set qsize` | device | `panos_debug_distributord` | (live device state — SSH via --remote) |
| `debug distributord relay relay-ipc-useridd set relay-useridd-recv-cache-qsize` | device | `panos_debug_distributord` | (live device state — SSH via --remote) |
| `debug distributord relay relay-ipc-useridd set relay-useridd-recv-read-batch-size` | device | `panos_debug_distributord` | (live device state — SSH via --remote) |
| `debug distributord relay relay-ipc-useridd show` | device | `panos_debug_distributord` | (live device state — SSH via --remote) |
| `debug distributord relay relay-mode set-dcom-relay-mode-only` | device | `panos_debug_distributord` | (live device state — SSH via --remote) |
| `debug distributord relay relay-mode show-dcom-relay-mode` | device | `panos_debug_distributord` | (live device state — SSH via --remote) |
| `debug distributord reset redistribution-agent` | device | `panos_debug_distributord` | (live device state — SSH via --remote) |
| `debug distributord reset relay-statistics` | device | `panos_debug_distributord` | (live device state — SSH via --remote) |
| `debug distributord set agent` | device | `panos_debug_distributord` | (live device state — SSH via --remote) |
| `debug distributord set client` | device | `panos_debug_distributord` | (live device state — SSH via --remote) |
| `debug distributord set distribute` | device | `panos_debug_distributord` | (live device state — SSH via --remote) |
| `debug distributord set relay` | device | `panos_debug_distributord` | (live device state — SSH via --remote) |
| `debug distributord show` | device | `panos_debug_distributord` | (live device state — SSH via --remote) |
| `debug distributord test debug-log-category` | device | `panos_debug_distributord` | (live device state — SSH via --remote) |
| `debug distributord unset agent` | device | `panos_debug_distributord` | (live device state — SSH via --remote) |
| `debug distributord unset client` | device | `panos_debug_distributord` | (live device state — SSH via --remote) |
| `debug distributord unset distribute` | device | `panos_debug_distributord` | (live device state — SSH via --remote) |
| `debug distributord unset relay` | device | `panos_debug_distributord` | (live device state — SSH via --remote) |
| `debug dnsproxyd` | device | `panos_debug_dnsproxyd` | (live device state — SSH via --remote) |
| `debug dnsproxyd clear cache-statistics` | device | `panos_debug_dnsproxyd` | (live device state — SSH via --remote) |
| `debug dnsproxyd clear fqdn counters` | device | `panos_debug_dnsproxyd` | (live device state — SSH via --remote) |
| `debug dnsproxyd clear sys-stats` | device | `panos_debug_dnsproxyd` | (live device state — SSH via --remote) |
| `debug dnsproxyd dns-signature allow-list download` | device | `panos_debug_dnsproxyd` | (live device state — SSH via --remote) |
| `debug dnsproxyd dns-signature cache fqdn` | device | `panos_debug_dnsproxyd` | (live device state — SSH via --remote) |
| `debug dnsproxyd dns-signature counters` | device | `panos_debug_dnsproxyd` | (live device state — SSH via --remote) |
| `debug dnsproxyd dns-signature info` | device | `panos_debug_dnsproxyd` | (live device state — SSH via --remote) |
| `debug dnsproxyd dns-signature query bypass-cache` | device | `panos_debug_dnsproxyd` | (live device state — SSH via --remote) |
| `debug dnsproxyd dns-signature query_n bypass-cache` | device | `panos_debug_dnsproxyd` | (live device state — SSH via --remote) |
| `debug dnsproxyd dns-signature response fqdn` | device | `panos_debug_dnsproxyd` | (live device state — SSH via --remote) |
| `debug dnsproxyd dns-signature response_n` | device | `panos_debug_dnsproxyd` | (live device state — SSH via --remote) |
| `debug dnsproxyd dns-signature response_n fqdns` | device | `panos_debug_dnsproxyd` | (live device state — SSH via --remote) |
| `debug dnsproxyd dns-signature response_n match-subdomains` | device | `panos_debug_dnsproxyd` | (live device state — SSH via --remote) |
| `debug dnsproxyd dns-signature threat-info fqdn` | device | `panos_debug_dnsproxyd` | (live device state — SSH via --remote) |
| `debug dnsproxyd dns-signature ut threat-info-api api-query-domain fqdn` | device | `panos_debug_dnsproxyd` | (live device state — SSH via --remote) |
| `debug dnsproxyd fqdn counters delta` | device | `panos_debug_dnsproxyd` | (live device state — SSH via --remote) |
| `debug dnsproxyd fqdn dump brief` | device | `panos_debug_dnsproxyd` | (live device state — SSH via --remote) |
| `debug dnsproxyd global off` | device | `panos_debug_dnsproxyd` | (live device state — SSH via --remote) |
| `debug dnsproxyd global on` | device | `panos_debug_dnsproxyd` | (live device state — SSH via --remote) |
| `debug dnsproxyd global show` | device | `panos_debug_dnsproxyd` | (live device state — SSH via --remote) |
| `debug dnsproxyd show` | device | `panos_debug_dnsproxyd` | (live device state — SSH via --remote) |
| `debug evtmgr` | device | `panos_debug_evtmgr` | (live device state — SSH via --remote) |
| `debug evtmgr ms` | device | `panos_debug_evtmgr` | (live device state — SSH via --remote) |
| `debug evtmgr ms debug-log clfy` | device | `panos_debug_evtmgr` | (live device state — SSH via --remote) |
| `debug evtmgr ms debug-log client` | device | `panos_debug_evtmgr` | (live device state — SSH via --remote) |
| `debug evtmgr ms debug-log msg` | device | `panos_debug_evtmgr` | (live device state — SSH via --remote) |
| `debug evtmgr ms debug-log multicast` | device | `panos_debug_evtmgr` | (live device state — SSH via --remote) |
| `debug evtmgr ms msg-filter msg-class` | device | `panos_debug_evtmgr` | (live device state — SSH via --remote) |
| `debug evtmgr ms show basic` | device | `panos_debug_evtmgr` | (live device state — SSH via --remote) |
| `debug evtmgr ms show client-id` | device | `panos_debug_evtmgr` | (live device state — SSH via --remote) |
| `debug evtmgr ms show detail` | device | `panos_debug_evtmgr` | (live device state — SSH via --remote) |
| `debug evtmgr ms syslog-enabled` | device | `panos_debug_evtmgr` | (live device state — SSH via --remote) |
| `debug external-list delete-file all` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug external-list delete-file type domain name` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug external-list delete-file type ip name` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug external-list delete-file type url name` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug global-protect hip set-dp-query-interval` | device | `panos_debug_global_protect` | (live device state — SSH via --remote) |
| `debug global-protect hip show-dp-query-interval` | device | `panos_debug_global_protect` | (live device state — SSH via --remote) |
| `debug global-protect portal clientlessvpn gzip-encoding` | device | `panos_debug_global_protect` | (live device state — SSH via --remote) |
| `debug global-protect portal clientlessvpn host-match-referer` | device | `panos_debug_global_protect` | (live device state — SSH via --remote) |
| `debug global-protect portal interval` | device | `panos_debug_global_protect` | (live device state — SSH via --remote) |
| `debug global-protect portal off` | device | `panos_debug_global_protect` | (live device state — SSH via --remote) |
| `debug global-protect portal on` | device | `panos_debug_global_protect` | (live device state — SSH via --remote) |
| `debug global-protect portal show` | device | `panos_debug_global_protect` | (live device state — SSH via --remote) |
| `debug gp-broker gpsvc key-value` | device | `panos_debug_gp_broker` | (live device state — SSH via --remote) |
| `debug gp-broker gpsvc reload-template` | device | `panos_debug_gp_broker` | (live device state — SSH via --remote) |
| `debug gp-broker gpsvc reset counter` | device | `panos_debug_gp_broker` | (live device state — SSH via --remote) |
| `debug gp-broker gpsvc reset key-value` | device | `panos_debug_gp_broker` | (live device state — SSH via --remote) |
| `debug gp-broker gpsvc task` | device | `panos_debug_gp_broker` | (live device state — SSH via --remote) |
| `debug gp-broker gpsvc test rpc api-name` | device | `panos_debug_gp_broker` | (live device state — SSH via --remote) |
| `debug gp-broker gpsvc trace add user` | device | `panos_debug_gp_broker` | (live device state — SSH via --remote) |
| `debug gp-broker gpsvc trace clear` | device | `panos_debug_gp_broker` | (live device state — SSH via --remote) |
| `debug gp-broker gpsvc trace delete user` | device | `panos_debug_gp_broker` | (live device state — SSH via --remote) |
| `debug gp-broker gpsvc trace global-log` | device | `panos_debug_gp_broker` | (live device state — SSH via --remote) |
| `debug gp-broker gpsvc trace show` | device | `panos_debug_gp_broker` | (live device state — SSH via --remote) |
| `debug gp-broker off` | device | `panos_debug_gp_broker` | (live device state — SSH via --remote) |
| `debug gp-broker on` | device | `panos_debug_gp_broker` | (live device state — SSH via --remote) |
| `debug gp-broker show` | device | `panos_debug_gp_broker` | (live device state — SSH via --remote) |
| `debug high-availability` | device | `panos_debug_high_availability` | (live device state — SSH via --remote) |
| `debug high-availability flap-interface interface` | device | `panos_debug_high_availability` | (live device state — SSH via --remote) |
| `debug high-availability knob set encrypt-init-hold-time` | device | `panos_debug_high_availability` | (live device state — SSH via --remote) |
| `debug high-availability knob set init-hold-time` | device | `panos_debug_high_availability` | (live device state — SSH via --remote) |
| `debug high-availability knob show` | device | `panos_debug_high_availability` | (live device state — SSH via --remote) |
| `debug high-availability on` | device | `panos_debug_high_availability` | (live device state — SSH via --remote) |
| `debug ifmgr dump-detail-history port` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug ifmgr dump-history port` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug ifmgr dump-portdb` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug ifmgr pstate port` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug ike gateway` | device | `panos_debug_ike` | (live device state — SSH via --remote) |
| `debug ike global off` | device | `panos_debug_ike` | (live device state — SSH via --remote) |
| `debug ike global on` | device | `panos_debug_ike` | (live device state — SSH via --remote) |
| `debug ike global show` | device | `panos_debug_ike` | (live device state — SSH via --remote) |
| `debug ike pcap` | device | `panos_debug_ike` | (live device state — SSH via --remote) |
| `debug ike socket` | device | `panos_debug_ike` | (live device state — SSH via --remote) |
| `debug ike stat` | device | `panos_debug_ike` | (live device state — SSH via --remote) |
| `debug ike stat fqdn name` | device | `panos_debug_ike` | (live device state — SSH via --remote) |
| `debug ike stat ipsec counter` | device | `panos_debug_ike` | (live device state — SSH via --remote) |
| `debug ike stat isakmp counter` | device | `panos_debug_ike` | (live device state — SSH via --remote) |
| `debug ike stat sched filter gwid` | device | `panos_debug_ike` | (live device state — SSH via --remote) |
| `debug ike tunnel` | device | `panos_debug_ike` | (live device state — SSH via --remote) |
| `debug iot clear-all type` | device | `panos_debug_iot` | (live device state — SSH via --remote) |
| `debug iot disable-device-id` | device | `panos_debug_iot` | (live device state — SSH via --remote) |
| `debug iot dump relay` | device | `panos_debug_iot` | (live device state — SSH via --remote) |
| `debug iot dump relay-ipc-distributord state` | device | `panos_debug_iot` | (live device state — SSH via --remote) |
| `debug iot eal cortex-server` | device | `panos_debug_iot` | (live device state — SSH via --remote) |
| `debug iot eal key-value` | device | `panos_debug_iot` | (live device state — SSH via --remote) |
| `debug iot eal on` | device | `panos_debug_iot` | (live device state — SSH via --remote) |
| `debug iot eal reset aggregation-non-ack` | device | `panos_debug_iot` | (live device state — SSH via --remote) |
| `debug iot eal reset aggregation-num` | device | `panos_debug_iot` | (live device state — SSH via --remote) |
| `debug iot eal reset connection` | device | `panos_debug_iot` | (live device state — SSH via --remote) |
| `debug iot eal reset counter` | device | `panos_debug_iot` | (live device state — SSH via --remote) |
| `debug iot eal reset key-value` | device | `panos_debug_iot` | (live device state — SSH via --remote) |
| `debug iot eal sending-format` | device | `panos_debug_iot` | (live device state — SSH via --remote) |
| `debug iot eal test load-dpi` | device | `panos_debug_iot` | (live device state — SSH via --remote) |
| `debug iot eal track` | device | `panos_debug_iot` | (live device state — SSH via --remote) |
| `debug iot eal track filter add subtype` | device | `panos_debug_iot` | (live device state — SSH via --remote) |
| `debug iot eal track filter clear` | device | `panos_debug_iot` | (live device state — SSH via --remote) |
| `debug iot eal track filter show` | device | `panos_debug_iot` | (live device state — SSH via --remote) |
| `debug iot eal validate-dpi` | device | `panos_debug_iot` | (live device state — SSH via --remote) |
| `debug iot global counter` | device | `panos_debug_iot` | (live device state — SSH via --remote) |
| `debug iot global off` | device | `panos_debug_iot` | (live device state — SSH via --remote) |
| `debug iot global on` | device | `panos_debug_iot` | (live device state — SSH via --remote) |
| `debug iot global show` | device | `panos_debug_iot` | (live device state — SSH via --remote) |
| `debug iot icd key-value` | device | `panos_debug_iot` | (live device state — SSH via --remote) |
| `debug iot icd on` | device | `panos_debug_iot` | (live device state — SSH via --remote) |
| `debug iot icd reset connection` | device | `panos_debug_iot` | (live device state — SSH via --remote) |
| `debug iot icd reset cookie` | device | `panos_debug_iot` | (live device state — SSH via --remote) |
| `debug iot icd reset key-value` | device | `panos_debug_iot` | (live device state — SSH via --remote) |
| `debug iot icd set-app-match-workers` | device | `panos_debug_iot` | (live device state — SSH via --remote) |
| `debug iot icd trigger-app-match` | device | `panos_debug_iot` | (live device state — SSH via --remote) |
| `debug iot icd verdict-server` | device | `panos_debug_iot` | (live device state — SSH via --remote) |
| `debug iot memory` | device | `panos_debug_iot` | (live device state — SSH via --remote) |
| `debug iot relay-ipc-distributord set qsize` | device | `panos_debug_iot` | (live device state — SSH via --remote) |
| `debug iot relay-ipc-distributord set relay-distd-recv-cache-qsize` | device | `panos_debug_iot` | (live device state — SSH via --remote) |
| `debug iot relay-ipc-distributord set relay-distd-recv-read-batch-size` | device | `panos_debug_iot` | (live device state — SSH via --remote) |
| `debug iot relay-ipc-distributord show` | device | `panos_debug_iot` | (live device state — SSH via --remote) |
| `debug keymgr gateway id` | device | `panos_debug_keymgr` | (live device state — SSH via --remote) |
| `debug keymgr global off` | device | `panos_debug_keymgr` | (live device state — SSH via --remote) |
| `debug keymgr global on` | device | `panos_debug_keymgr` | (live device state — SSH via --remote) |
| `debug keymgr global show` | device | `panos_debug_keymgr` | (live device state — SSH via --remote) |
| `debug keymgr list-sa` | device | `panos_debug_keymgr` | (live device state — SSH via --remote) |
| `debug keymgr queue` | device | `panos_debug_keymgr` | (live device state — SSH via --remote) |
| `debug keymgr socket` | device | `panos_debug_keymgr` | (live device state — SSH via --remote) |
| `debug keymgr tunnel id` | device | `panos_debug_keymgr` | (live device state — SSH via --remote) |
| `debug l2ctrld global off` | device | `panos_debug_l2ctrld` | (live device state — SSH via --remote) |
| `debug l2ctrld global on` | device | `panos_debug_l2ctrld` | (live device state — SSH via --remote) |
| `debug l2ctrld global show` | device | `panos_debug_l2ctrld` | (live device state — SSH via --remote) |
| `debug l2ctrld lacp off` | device | `panos_debug_l2ctrld` | (live device state — SSH via --remote) |
| `debug l2ctrld lacp on` | device | `panos_debug_l2ctrld` | (live device state — SSH via --remote) |
| `debug l2ctrld lacp set hold-time aggregate-ethernet` | device | `panos_debug_l2ctrld` | (live device state — SSH via --remote) |
| `debug l2ctrld lacp show` | device | `panos_debug_l2ctrld` | (live device state — SSH via --remote) |
| `debug l2ctrld lldp delete neighbor` | device | `panos_debug_l2ctrld` | (live device state — SSH via --remote) |
| `debug l2ctrld lldp off` | device | `panos_debug_l2ctrld` | (live device state — SSH via --remote) |
| `debug l2ctrld lldp on` | device | `panos_debug_l2ctrld` | (live device state — SSH via --remote) |
| `debug l2ctrld lldp pcap` | device | `panos_debug_l2ctrld` | (live device state — SSH via --remote) |
| `debug l2ctrld lldp pcap logical-router on logicalrouter` | device | `panos_debug_l2ctrld` | (live device state — SSH via --remote) |
| `debug l2ctrld lldp pcap virtual-router on virtualrouter` | device | `panos_debug_l2ctrld` | (live device state — SSH via --remote) |
| `debug l2ctrld lldp set stagger-limit` | device | `panos_debug_l2ctrld` | (live device state — SSH via --remote) |
| `debug l2ctrld lldp show` | device | `panos_debug_l2ctrld` | (live device state — SSH via --remote) |
| `debug l3svc captive-portal kerberos-timeout interval` | device | `panos_debug_l3svc` | (live device state — SSH via --remote) |
| `debug l3svc captive-portal kerberos-timeout off` | device | `panos_debug_l3svc` | (live device state — SSH via --remote) |
| `debug l3svc captive-portal kerberos-timeout on` | device | `panos_debug_l3svc` | (live device state — SSH via --remote) |
| `debug l3svc captive-portal kerberos-timeout show` | device | `panos_debug_l3svc` | (live device state — SSH via --remote) |
| `debug l3svc clear` | device | `panos_debug_l3svc` | (live device state — SSH via --remote) |
| `debug l3svc off` | device | `panos_debug_l3svc` | (live device state — SSH via --remote) |
| `debug l3svc on` | device | `panos_debug_l3svc` | (live device state — SSH via --remote) |
| `debug l3svc pcap` | device | `panos_debug_l3svc` | (live device state — SSH via --remote) |
| `debug l3svc pcap logical-router on logicalrouter` | device | `panos_debug_l3svc` | (live device state — SSH via --remote) |
| `debug l3svc pcap virtual-router on virtualrouter` | device | `panos_debug_l3svc` | (live device state — SSH via --remote) |
| `debug l3svc reset user-cache` | device | `panos_debug_l3svc` | (live device state — SSH via --remote) |
| `debug l3svc show user-cache` | device | `panos_debug_l3svc` | (live device state — SSH via --remote) |
| `debug list-admin-history` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug list-blocked-partial-xpaths` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug log-output-need-utf8` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug log-receiver` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver container-page entries` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver container-page off` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver container-page on` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver container-page timeout` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver contmgr status` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver corr-mgr off` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver corr-mgr on` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver corr-mgr show back-query status` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver corr-mgr show brief` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver corr-mgr show failed` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver corr-mgr show filter search object` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver corr-mgr show instance search category` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver corr-mgr show instance summary` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver corr-mgr show object id` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver corr-mgr show object list` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver corr-mgr stats clear object` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver corr-mgr stats show object` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver correlation filters show` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver correlation stats show` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver counters filter delta` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver dag always-include-dag` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver dag disable-dag-logging` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver dag dump dag-id vsysid` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver dag dump id-dag dag-idx` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver dag dump ip-dag ip` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver dag dump rule-dag rule_uuid` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver dag off` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver dag on` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver dag show` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver dpi dump clear` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver dpi dump format` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver dpi dump off` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver dpi dump on` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver dump users all` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver dump users id` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver dumplog off` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver dumplog on count` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver edl disable-edl-logging` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver edl dump edl-id vsysid` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver edl dump id-edl edl-idx` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver edl dump ip-edl ip` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver edl dump rule-edl rule_uuid` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver edl off` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver edl on` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver edl show` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver fwd` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver ip-cache clear node-data vsysid` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver ip-cache clear vsys-data vsysid` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver log-flow counters` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver log-flow trace show` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver log-forwarding per-second-stats` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver log-forwarding status` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver log-forwarding-connections per-second-stats` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver log-forwarding-connections status` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver log-purger debug` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver logdb-writer-stats latest` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver memory info verbose` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver memory per-second-stats` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver memory trim` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver netflow` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver on` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver param-tuning rollup` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver param-tuning syslog-threads show` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver param-tuning syslog-threads size` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver param-tuning task-queue show` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver param-tuning task-queue size` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver per-second-stats off` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver per-second-stats on` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver rawlog_fwd clear hints-all` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver rawlog_fwd off` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver rawlog_fwd on` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver rawlog_fwd set hints-expiration-duration` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver rawlog_fwd set hints-max` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver rawlog_fwd show` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver rawlog_fwd show connmgr verbose` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver rawlog_fwd stats global clear` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver rawlog_fwd stats global show verbose` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver rawlog_fwd stats per-lc` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver rawlog_fwd_trial connmgr` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver rawlog_fwd_trial evtmgr` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver rawlog_fwd_trial stats global show verbose` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug log-receiver telemetry-triggers` | device | `panos_debug_log_receiver` | (live device state — SSH via --remote) |
| `debug logdb-usage` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug logview role` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type edl-domain all` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type edl-domain id` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type edl-domain name` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type edl-ip all` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type edl-ip id` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type edl-ip name` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type hip-profile all` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type hip-profile id` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type hip-profile name` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type interface-group all` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type interface-group id` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type interface-group name` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type macl-rule all` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type macl-rule id` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type macl-rule name` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type ospfv3-virtual-link all` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type ospfv3-virtual-link id` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type ospfv3-virtual-link name` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type sdwan-link-tag all` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type sdwan-link-tag id` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type sdwan-link-tag name` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type shared-app-signature all` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type shared-app-signature id` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type shared-app-signature name` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type shared-bgp-aggr-address all` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type shared-bgp-aggr-address id` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type shared-bgp-aggr-address name` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type shared-bgp-peer all` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type shared-bgp-peer id` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type shared-bgp-peer name` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type shared-bgp-peergrp all` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type shared-bgp-peergrp id` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type shared-bgp-peergrp name` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type shared-qos-group all` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type shared-qos-group id` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type shared-qos-group name` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type shared-region all` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type shared-region id` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type shared-region name` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type shared-spyware all` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type shared-spyware id` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type shared-spyware name` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type shared-url-filtering all` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type shared-url-filtering id` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type shared-url-filtering name` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type tci-rule all` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type tci-rule id` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type tci-rule name` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type vsys-app-signature all` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type vsys-app-signature id` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type vsys-app-signature name` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type vsys-region all` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type vsys-region id` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type vsys-region name` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type vsys-spyware all` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type vsys-spyware id` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type vsys-spyware name` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type vsys-url-filtering all` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type vsys-url-filtering id` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd dump idmgr type vsys-url-filtering name` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug lpmgrd status` | device | `panos_debug_lpmgrd` | (live device state — SSH via --remote) |
| `debug macsec global off` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug macsec global on` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug macsec global show` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug macsec pcap` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug management-interface dhcp client debug` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug management-interface dhcp client log` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug management-server` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server app-config-trigger` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server autofocus` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server client disable` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server client enable` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server configd-mem` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server contmgr status` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server corr-mgr off` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server corr-mgr on` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server corr-mgr show back-query status` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server corr-mgr show brief` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server corr-mgr show failed` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server corr-mgr show filter search object` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server corr-mgr show instance search category` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server corr-mgr show instance summary` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server corr-mgr show object id` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server corr-mgr show object list` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server corr-mgr stats clear object` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server corr-mgr stats show object` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server db-intervals start-time` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server db-rollup` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server device-monitoring enable` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server dg-ctxt vsys` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server disable-cms-conn-check` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server last-candidatecfg-audit diff base-version` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server last-candidatecfg-audit info` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server last-candidatecfg-audit show version` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server log-forwarding-congestion-ctrl set` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server log-forwarding-congestion-ctrl show` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server max-config-size set size` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server max-config-size show` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server memory` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server ml7 anti-virus install` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server ml7 content install` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server ml7 iot install` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server on` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server req-stats` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server rolledup-intervals start-time` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server rule-hit` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server secure-conn set scep-cert-renewal-time` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server secure-conn set scep-cert-retry-on-failure-interval` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server secure-conn show ha config file` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server secure-conn show mgmt config file` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server secure-conn show mgmt detail` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server secure-conn show scep-cert-renewal-time` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server secure-conn show scep-cert-retry-on-failure-interval` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server set` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server set all` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server snmp-memory-map` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server telemetry-triggers correlated-threat-log-limit` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server telemetry-triggers counters` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server telemetry-triggers per-signature-limit` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server telemetry-triggers raw-threat-log-limit` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server telemetry-triggers related-threat-log-limit` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server template dump-config from` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server toggle-ui-notification` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server unified-log` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server unset` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server unset all` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server user bitmap` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server user info name` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-server vld stats cc` | device | `panos_debug_management_server` | (live device state — SSH via --remote) |
| `debug management-websrvr backend off` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug management-websrvr backend on` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug management-websrvr backend show` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug md-service internal-dump` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug md-service off` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug md-service on` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug md-service show` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug mprelay off` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug mprelay on` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug mprelay show` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug net-inspection packet-limit` | device | `panos_debug_net_inspection` | (live device state — SSH via --remote) |
| `debug net-inspection reset` | device | `panos_debug_net_inspection` | (live device state — SSH via --remote) |
| `debug net-inspection show` | device | `panos_debug_net_inspection` | (live device state — SSH via --remote) |
| `debug net-inspection trace` | device | `panos_debug_net_inspection` | (live device state — SSH via --remote) |
| `debug net-inspection trace-limit` | device | `panos_debug_net_inspection` | (live device state — SSH via --remote) |
| `debug netconfig-agent off` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug netconfig-agent on` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug netconfig-agent show` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug object registered-ip` | device | `panos_debug_object` | (live device state — SSH via --remote) |
| `debug object registered-ip clear all source-name` | device | `panos_debug_object` | (live device state — SSH via --remote) |
| `debug object registered-ip redis-entry ip` | device | `panos_debug_object` | (live device state — SSH via --remote) |
| `debug object registered-ip redis-entry iprange` | device | `panos_debug_object` | (live device state — SSH via --remote) |
| `debug object registered-ip show tag-source tag` | device | `panos_debug_object` | (live device state — SSH via --remote) |
| `debug object registered-ip test cuid-upload` | device | `panos_debug_object` | (live device state — SSH via --remote) |
| `debug object registered-ip test download` | device | `panos_debug_object` | (live device state — SSH via --remote) |
| `debug object registered-ip test download-mode` | device | `panos_debug_object` | (live device state — SSH via --remote) |
| `debug object registered-ip test register tag` | device | `panos_debug_object` | (live device state — SSH via --remote) |
| `debug object registered-ip test unregister tag` | device | `panos_debug_object` | (live device state — SSH via --remote) |
| `debug object registered-user clear all tag-source` | device | `panos_debug_object` | (live device state — SSH via --remote) |
| `debug object registered-user show tag-source user` | device | `panos_debug_object` | (live device state — SSH via --remote) |
| `debug object registered-user test cuid-upload` | device | `panos_debug_object` | (live device state — SSH via --remote) |
| `debug object registered-user test register user` | device | `panos_debug_object` | (live device state — SSH via --remote) |
| `debug object registered-user test unregister user` | device | `panos_debug_object` | (live device state — SSH via --remote) |
| `debug online diagnostics get execution-time` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug online diagnostics run` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug pancfg-directory-usage clean config saved` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug pancfg-directory-usage clean dynamic-updates anti-virus update` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug pancfg-directory-usage clean dynamic-updates content update` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug pancfg-directory-usage clean software-images version` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug pppoed global off` | device | `panos_debug_pppoed` | (live device state — SSH via --remote) |
| `debug pppoed global on` | device | `panos_debug_pppoed` | (live device state — SSH via --remote) |
| `debug pppoed global show` | device | `panos_debug_pppoed` | (live device state — SSH via --remote) |
| `debug pppoed pcap` | device | `panos_debug_pppoed` | (live device state — SSH via --remote) |
| `debug pppoed pcap on file_size` | device | `panos_debug_pppoed` | (live device state — SSH via --remote) |
| `debug pppoed show config` | device | `panos_debug_pppoed` | (live device state — SSH via --remote) |
| `debug pppoed show interface` | device | `panos_debug_pppoed` | (live device state — SSH via --remote) |
| `debug predefined-report-default` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug preserve-prenat feature show` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug proxy discard-partial-client-hello enable` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug proxy discard-partial-client-hello show` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug proxy fast-session-delete enable` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug proxy-protocol debug-level` | device | `panos_debug_proxy_protocol` | (live device state — SSH via --remote) |
| `debug proxy-protocol debug-mode normal` | device | `panos_debug_proxy_protocol` | (live device state — SSH via --remote) |
| `debug proxy-protocol debug-mode session-limit` | device | `panos_debug_proxy_protocol` | (live device state — SSH via --remote) |
| `debug proxy-protocol debug-mode trace-limit` | device | `panos_debug_proxy_protocol` | (live device state — SSH via --remote) |
| `debug proxy-protocol feature enabled` | device | `panos_debug_proxy_protocol` | (live device state — SSH via --remote) |
| `debug proxy-protocol feature hostid-subtlv-type` | device | `panos_debug_proxy_protocol` | (live device state — SSH via --remote) |
| `debug proxy-protocol feature show` | device | `panos_debug_proxy_protocol` | (live device state — SSH via --remote) |
| `debug proxy-protocol feature userid-subtlv-type` | device | `panos_debug_proxy_protocol` | (live device state — SSH via --remote) |
| `debug proxy-protocol packet-dump-max-bytes` | device | `panos_debug_proxy_protocol` | (live device state — SSH via --remote) |
| `debug rasmgr delay-nh-update` | device | `panos_debug_rasmgr` | (live device state — SSH via --remote) |
| `debug rasmgr delay-nh-update reset` | device | `panos_debug_rasmgr` | (live device state — SSH via --remote) |
| `debug rasmgr gateway` | device | `panos_debug_rasmgr` | (live device state — SSH via --remote) |
| `debug rasmgr ippool reset-all` | device | `panos_debug_rasmgr` | (live device state — SSH via --remote) |
| `debug rasmgr off` | device | `panos_debug_rasmgr` | (live device state — SSH via --remote) |
| `debug rasmgr on` | device | `panos_debug_rasmgr` | (live device state — SSH via --remote) |
| `debug rasmgr satellite` | device | `panos_debug_rasmgr` | (live device state — SSH via --remote) |
| `debug rasmgr show` | device | `panos_debug_rasmgr` | (live device state — SSH via --remote) |
| `debug rasmgr src-ip-trie gateway-name` | device | `panos_debug_rasmgr` | (live device state — SSH via --remote) |
| `debug rasmgr statistics` | device | `panos_debug_rasmgr` | (live device state — SSH via --remote) |
| `debug rasmgr user` | device | `panos_debug_rasmgr` | (live device state — SSH via --remote) |
| `debug rawlog_fwd enable` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug reportd contmgr status` | device | `panos_debug_reportd` | (live device state — SSH via --remote) |
| `debug reportd corr-mgr off` | device | `panos_debug_reportd` | (live device state — SSH via --remote) |
| `debug reportd corr-mgr on` | device | `panos_debug_reportd` | (live device state — SSH via --remote) |
| `debug reportd corr-mgr show back-query status` | device | `panos_debug_reportd` | (live device state — SSH via --remote) |
| `debug reportd corr-mgr show brief` | device | `panos_debug_reportd` | (live device state — SSH via --remote) |
| `debug reportd corr-mgr show failed` | device | `panos_debug_reportd` | (live device state — SSH via --remote) |
| `debug reportd corr-mgr show filter search object` | device | `panos_debug_reportd` | (live device state — SSH via --remote) |
| `debug reportd corr-mgr show instance search category` | device | `panos_debug_reportd` | (live device state — SSH via --remote) |
| `debug reportd corr-mgr show instance summary` | device | `panos_debug_reportd` | (live device state — SSH via --remote) |
| `debug reportd corr-mgr show object id` | device | `panos_debug_reportd` | (live device state — SSH via --remote) |
| `debug reportd corr-mgr show object list` | device | `panos_debug_reportd` | (live device state — SSH via --remote) |
| `debug reportd corr-mgr stats clear object` | device | `panos_debug_reportd` | (live device state — SSH via --remote) |
| `debug reportd corr-mgr stats show object` | device | `panos_debug_reportd` | (live device state — SSH via --remote) |
| `debug reportd off` | device | `panos_debug_reportd` | (live device state — SSH via --remote) |
| `debug reportd on` | device | `panos_debug_reportd` | (live device state — SSH via --remote) |
| `debug reportd schedule-reports` | device | `panos_debug_reportd` | (live device state — SSH via --remote) |
| `debug reportd send-request-to-7k` | device | `panos_debug_reportd` | (live device state — SSH via --remote) |
| `debug reportd set-timeout` | device | `panos_debug_reportd` | (live device state — SSH via --remote) |
| `debug reportd show` | device | `panos_debug_reportd` | (live device state — SSH via --remote) |
| `debug routing` | device | `panos_debug_routing` | (live device state — SSH via --remote) |
| `debug routing dctrace both enable` | device | `panos_debug_routing` | (live device state — SSH via --remote) |
| `debug routing dctrace ips enable` | device | `panos_debug_routing` | (live device state — SSH via --remote) |
| `debug routing dctrace pd enable` | device | `panos_debug_routing` | (live device state — SSH via --remote) |
| `debug routing dctrace show` | device | `panos_debug_routing` | (live device state — SSH via --remote) |
| `debug routing fib clear virtual-router` | device | `panos_debug_routing` | (live device state — SSH via --remote) |
| `debug routing fib flush` | device | `panos_debug_routing` | (live device state — SSH via --remote) |
| `debug routing fib stats` | device | `panos_debug_routing` | (live device state — SSH via --remote) |
| `debug routing fqdn display virtual-router` | device | `panos_debug_routing` | (live device state — SSH via --remote) |
| `debug routing global off` | device | `panos_debug_routing` | (live device state — SSH via --remote) |
| `debug routing global on` | device | `panos_debug_routing` | (live device state — SSH via --remote) |
| `debug routing global show` | device | `panos_debug_routing` | (live device state — SSH via --remote) |
| `debug routing mib` | device | `panos_debug_routing` | (live device state — SSH via --remote) |
| `debug routing mpf offload` | device | `panos_debug_routing` | (live device state — SSH via --remote) |
| `debug routing mpf stats` | device | `panos_debug_routing` | (live device state — SSH via --remote) |
| `debug routing path-monitor id` | device | `panos_debug_routing` | (live device state — SSH via --remote) |
| `debug routing pcap` | device | `panos_debug_routing` | (live device state — SSH via --remote) |
| `debug routing pcap show` | device | `panos_debug_routing` | (live device state — SSH via --remote) |
| `debug routing qtrace disable afi` | device | `panos_debug_routing` | (live device state — SSH via --remote) |
| `debug routing qtrace enable afi` | device | `panos_debug_routing` | (live device state — SSH via --remote) |
| `debug routing qtrace flush-log` | device | `panos_debug_routing` | (live device state — SSH via --remote) |
| `debug routing qtrace show afi` | device | `panos_debug_routing` | (live device state — SSH via --remote) |
| `debug run-panorama-predefined-report` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug satd dump certificate-pool global` | device | `panos_debug_satd` | (live device state — SSH via --remote) |
| `debug satd dump certificate-pool satellite` | device | `panos_debug_satd` | (live device state — SSH via --remote) |
| `debug satd failed-refresh-timeout satellite name` | device | `panos_debug_satd` | (live device state — SSH via --remote) |
| `debug satd off` | device | `panos_debug_satd` | (live device state — SSH via --remote) |
| `debug satd on` | device | `panos_debug_satd` | (live device state — SSH via --remote) |
| `debug satd show` | device | `panos_debug_satd` | (live device state — SSH via --remote) |
| `debug satd statistics` | device | `panos_debug_satd` | (live device state — SSH via --remote) |
| `debug sdwand clear all` | device | `panos_debug_sdwand` | (live device state — SSH via --remote) |
| `debug sdwand event-log filter delete all` | device | `panos_debug_sdwand` | (live device state — SSH via --remote) |
| `debug sdwand event-log filter delete idx` | device | `panos_debug_sdwand` | (live device state — SSH via --remote) |
| `debug sdwand event-log filter off` | device | `panos_debug_sdwand` | (live device state — SSH via --remote) |
| `debug sdwand event-log filter on` | device | `panos_debug_sdwand` | (live device state — SSH via --remote) |
| `debug sdwand event-log filter set index` | device | `panos_debug_sdwand` | (live device state — SSH via --remote) |
| `debug sdwand event-log filter set match ingress-interface` | device | `panos_debug_sdwand` | (live device state — SSH via --remote) |
| `debug sdwand event-log filter show` | device | `panos_debug_sdwand` | (live device state — SSH via --remote) |
| `debug sdwand feature show` | device | `panos_debug_sdwand` | (live device state — SSH via --remote) |
| `debug sdwand global off` | device | `panos_debug_sdwand` | (live device state — SSH via --remote) |
| `debug sdwand global on` | device | `panos_debug_sdwand` | (live device state — SSH via --remote) |
| `debug sdwand global show` | device | `panos_debug_sdwand` | (live device state — SSH via --remote) |
| `debug sdwand path-monitor disable all` | device | `panos_debug_sdwand` | (live device state — SSH via --remote) |
| `debug sdwand path-monitor disable tunnel-id` | device | `panos_debug_sdwand` | (live device state — SSH via --remote) |
| `debug sdwand path-monitor enable all` | device | `panos_debug_sdwand` | (live device state — SSH via --remote) |
| `debug sdwand path-monitor enable tunnel-id` | device | `panos_debug_sdwand` | (live device state — SSH via --remote) |
| `debug sdwand saas branch interval` | device | `panos_debug_sdwand` | (live device state — SSH via --remote) |
| `debug sdwand saas hub interval` | device | `panos_debug_sdwand` | (live device state — SSH via --remote) |
| `debug set-content-download-retry attempts` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug snmpd async` | device | `panos_debug_snmpd` | (live device state — SSH via --remote) |
| `debug snmpd clear_persistence` | device | `panos_debug_snmpd` | (live device state — SSH via --remote) |
| `debug snmpd off` | device | `panos_debug_snmpd` | (live device state — SSH via --remote) |
| `debug snmpd on debug` | device | `panos_debug_snmpd` | (live device state — SSH via --remote) |
| `debug snmpd sysd-disable-retry` | device | `panos_debug_snmpd` | (live device state — SSH via --remote) |
| `debug snmpd sysd-timeout` | device | `panos_debug_snmpd` | (live device state — SSH via --remote) |
| `debug software` | device | `panos_debug_software` | (live device state — SSH via --remote) |
| `debug software core` | device | `panos_debug_software` | (live device state — SSH via --remote) |
| `debug software disk-usage aggressive-cleaning` | device | `panos_debug_software` | (live device state — SSH via --remote) |
| `debug software disk-usage cleanup threshold` | device | `panos_debug_software` | (live device state — SSH via --remote) |
| `debug software disk-usage dagger-fds-cleaning` | device | `panos_debug_software` | (live device state — SSH via --remote) |
| `debug software disk-usage dangling-fds target-name` | device | `panos_debug_software` | (live device state — SSH via --remote) |
| `debug software fd-limit service` | device | `panos_debug_software` | (live device state — SSH via --remote) |
| `debug software generate-sar-report current-date` | device | `panos_debug_software` | (live device state — SSH via --remote) |
| `debug software kernelcfg thp` | device | `panos_debug_software` | (live device state — SSH via --remote) |
| `debug software kernelcfg zram-swap disable` | device | `panos_debug_software` | (live device state — SSH via --remote) |
| `debug software kernelcfg zram-swap enable` | device | `panos_debug_software` | (live device state — SSH via --remote) |
| `debug software kernelcfg zram-swap modify num-dev` | device | `panos_debug_software` | (live device state — SSH via --remote) |
| `debug software kernelcfg zram-swap show` | device | `panos_debug_software` | (live device state — SSH via --remote) |
| `debug software large-core show-reserved-space` | device | `panos_debug_software` | (live device state — SSH via --remote) |
| `debug software logging-level set feature service` | device | `panos_debug_software` | (live device state — SSH via --remote) |
| `debug software logging-level set level` | device | `panos_debug_software` | (live device state — SSH via --remote) |
| `debug software logging-level show feature service` | device | `panos_debug_software` | (live device state — SSH via --remote) |
| `debug software logging-level show feature-defs service` | device | `panos_debug_software` | (live device state — SSH via --remote) |
| `debug software logging-level show level service` | device | `panos_debug_software` | (live device state — SSH via --remote) |
| `debug software logging-size set ratio` | device | `panos_debug_software` | (live device state — SSH via --remote) |
| `debug software logging-size show ratio service` | device | `panos_debug_software` | (live device state — SSH via --remote) |
| `debug software memsize_tracked` | device | `panos_debug_software` | (live device state — SSH via --remote) |
| `debug software monitor_smaps_threshold percentage` | device | `panos_debug_software` | (live device state — SSH via --remote) |
| `debug software phy-limit service` | device | `panos_debug_software` | (live device state — SSH via --remote) |
| `debug software resource subsystem` | device | `panos_debug_software` | (live device state — SSH via --remote) |
| `debug software restart process` | device | `panos_debug_software` | (live device state — SSH via --remote) |
| `debug software trace` | device | `panos_debug_software` | (live device state — SSH via --remote) |
| `debug software virt-limit service` | device | `panos_debug_software` | (live device state — SSH via --remote) |
| `debug sslmgr clear log` | device | `panos_debug_sslmgr` | (live device state — SSH via --remote) |
| `debug sslmgr delete crl` | device | `panos_debug_sslmgr` | (live device state — SSH via --remote) |
| `debug sslmgr delete ocsp` | device | `panos_debug_sslmgr` | (live device state — SSH via --remote) |
| `debug sslmgr delete ocsp-host` | device | `panos_debug_sslmgr` | (live device state — SSH via --remote) |
| `debug sslmgr off` | device | `panos_debug_sslmgr` | (live device state — SSH via --remote) |
| `debug sslmgr on` | device | `panos_debug_sslmgr` | (live device state — SSH via --remote) |
| `debug sslmgr reset` | device | `panos_debug_sslmgr` | (live device state — SSH via --remote) |
| `debug sslmgr save ocsp` | device | `panos_debug_sslmgr` | (live device state — SSH via --remote) |
| `debug sslmgr set` | device | `panos_debug_sslmgr` | (live device state — SSH via --remote) |
| `debug sslmgr set crl-background-download` | device | `panos_debug_sslmgr` | (live device state — SSH via --remote) |
| `debug sslmgr set crl-recv-speed-limit` | device | `panos_debug_sslmgr` | (live device state — SSH via --remote) |
| `debug sslmgr set disable-scep-auth-cookie` | device | `panos_debug_sslmgr` | (live device state — SSH via --remote) |
| `debug sslmgr set max-crl-file-size` | device | `panos_debug_sslmgr` | (live device state — SSH via --remote) |
| `debug sslmgr set max-inflated-crl-file-size` | device | `panos_debug_sslmgr` | (live device state — SSH via --remote) |
| `debug sslmgr set ocsp-host-failure-threshold` | device | `panos_debug_sslmgr` | (live device state — SSH via --remote) |
| `debug sslmgr set ocsp-next-update-time` | device | `panos_debug_sslmgr` | (live device state — SSH via --remote) |
| `debug sslmgr set parallel-processing` | device | `panos_debug_sslmgr` | (live device state — SSH via --remote) |
| `debug sslmgr show` | device | `panos_debug_sslmgr` | (live device state — SSH via --remote) |
| `debug sslmgr show memory` | device | `panos_debug_sslmgr` | (live device state — SSH via --remote) |
| `debug sslmgr statistics` | device | `panos_debug_sslmgr` | (live device state — SSH via --remote) |
| `debug sslmgr tar-all-crl` | device | `panos_debug_sslmgr` | (live device state — SSH via --remote) |
| `debug sslmgr test gp-client-cert-check cert-file` | device | `panos_debug_sslmgr` | (live device state — SSH via --remote) |
| `debug sslmgr test show-cert-check-jobs` | device | `panos_debug_sslmgr` | (live device state — SSH via --remote) |
| `debug sslmgr view crl` | device | `panos_debug_sslmgr` | (live device state — SSH via --remote) |
| `debug sslmgr view ocsp` | device | `panos_debug_sslmgr` | (live device state — SSH via --remote) |
| `debug sslmgr view ocsp-host` | device | `panos_debug_sslmgr` | (live device state — SSH via --remote) |
| `debug sslmgr view pending-crl-downloads` | device | `panos_debug_sslmgr` | (live device state — SSH via --remote) |
| `debug streaming dump` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug streaming tdb` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug streaming-telemetry set-logging-reporting-timeout` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug streaming-telemetry show-region-list` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug streaming-telemetry show-schedule` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug streaming-telemetry show-schedule-path-list` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug swm` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug swm install image` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug swm refresh content` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug swm show revert-status` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug sysd prefix-query command` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug sysd process-query command` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug sysd summary` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug sysd top` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug syslog-params reset-to-default-settings` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug syslog-params settings time-reopen` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug syslog-params show` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug system` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug system disk-life disk-1` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug system disk-smart-info disk-1` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug system ssh-key-reset` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug tac-login` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug techsupport duts` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug techsupport duts add-search-dir` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug techsupport duts set-byte-threshold` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug tund clear all` | device | `panos_debug_tund` | (live device state — SSH via --remote) |
| `debug tund global off` | device | `panos_debug_tund` | (live device state — SSH via --remote) |
| `debug tund global on` | device | `panos_debug_tund` | (live device state — SSH via --remote) |
| `debug tund global show` | device | `panos_debug_tund` | (live device state — SSH via --remote) |
| `debug tund tunnel id` | device | `panos_debug_tund` | (live device state — SSH via --remote) |
| `debug ui telemetry` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug use-proxy-for-email-server` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug user-id` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id agent` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id agent-getall-rate rate` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id agent-getall-rate show` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id clear cloud-identity-engine type` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id clear domain-map from-disk` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id clear email-cache` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id clear gm-srvc-query` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id clear group` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id clear ip-port-user-dp ip` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id clear log` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id cluster-get-all` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id cluster-peer-ip` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id cluster-state` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id cp-redirect-host-v6 clear` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id cp-redirect-host-v6 show` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id cp-redirect-host-v6 value` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dscd off` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dscd on` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dscd subdomains` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump cloud-identity-engine type` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump com statistics` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump conn-mgr statistics` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump domain-id-table domain all` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump domain-id-table domain name` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump edir-user all` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump edir-user user` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump email-cache all` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump email-cache email` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump hip-mdm-cache start-from` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump hip-profile-database entry start-from` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump hip-profile-database ipmapping` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump hip-profile-database statistics` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump hip-report user` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump idmgr high-availability state` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump idmgr redis type computer all` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump idmgr redis type computer id` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump idmgr redis type computer name` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump idmgr redis type user all` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump idmgr redis type user id` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump idmgr redis type user name` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump idmgr redis type user-group all` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump idmgr redis type user-group id` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump idmgr redis type user-group name` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump idmgr type computer all` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump idmgr type computer id` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump idmgr type computer name` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump idmgr type user all` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump idmgr type user id` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump idmgr type user name` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump idmgr type user-group all` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump idmgr type user-group id` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump idmgr type user-group name` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump memory` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump relay-ipc-distributord` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump ts-agent` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump uid-2-metadata user all` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump uid-2-metadata user id` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump uid-2-primeuid user all` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump uid-2-primeuid user id` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump userprefix-2-uid user all` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump userprefix-2-uid user name` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump vm-monitored-objects all` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump vm-monitored-objects ref-id` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump vm-monitored-objects source-name` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id dump vm-monitored-objects type` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id get` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id kerberos list server-monitor` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id kerberos purge server-monitor` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id kerberos test default` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id kerberos test server-name` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id l3svc-max-retry rate` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id l3svc-max-retry show` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id l3svc-max-write-retry rate` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id l3svc-max-write-retry show` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id measure-handle-messages-duration` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id off` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id on` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id refresh cloud-identity-engine all` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id refresh cloud-identity-engine config-data` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id refresh cloud-identity-engine name` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id refresh dp-uid-gid` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id refresh group-mapping all` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id refresh group-mapping group-mapping-name` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id refresh group-mapping xmlapi-groups` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id refresh user-id agent` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id relay-ipc-distributord set qsize` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id relay-ipc-distributord set relay-distd-recv-cache-qsize` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id relay-ipc-distributord set relay-distd-recv-read-batch-size` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id relay-ipc-distributord show` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id reset` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id reset captive-portal ip-address` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id reset cloud-identity-engine all` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id reset cloud-identity-engine name` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id reset cluster-state` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id reset com statistics` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id reset conn-mgr statistics` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id reset ip-user-mapping-stats` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id reset relay-statistics` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id reset user-id-manager type` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id save hip-profile-database` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id set agent` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id set all` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id set base` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id set features` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id set hip` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id set ldap` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id set misc` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id set relay` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id set third-party` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id set userid` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id test agentless` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id test cp-login ip-address` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id test cp-logout ip-address` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id test debug-log-category` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id test gp-login ip-address` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id test gp-logout ip-address` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id test hip-profile-database size` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id test hip-report user` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id test hip-update ip` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id test idmgr-change-max type user-group new-max-id` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id test idmgr-restore-default-max type user-group` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id test probing` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id test sso-login ip-address` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id unset agent` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id unset all` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id unset base` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id unset features` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id unset hip` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id unset ldap` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id unset misc` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id unset relay` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id unset third-party` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug user-id unset userid` | device | `panos_debug_user_id` | (live device state — SSH via --remote) |
| `debug vardata-receiver off` | device | `panos_debug_vardata_receiver` | (live device state — SSH via --remote) |
| `debug vardata-receiver on` | device | `panos_debug_vardata_receiver` | (live device state — SSH via --remote) |
| `debug vardata-receiver set all` | device | `panos_debug_vardata_receiver` | (live device state — SSH via --remote) |
| `debug vardata-receiver set third-party` | device | `panos_debug_vardata_receiver` | (live device state — SSH via --remote) |
| `debug vardata-receiver show` | device | `panos_debug_vardata_receiver` | (live device state — SSH via --remote) |
| `debug vardata-receiver statistics` | device | `panos_debug_vardata_receiver` | (live device state — SSH via --remote) |
| `debug vardata-receiver unset all` | device | `panos_debug_vardata_receiver` | (live device state — SSH via --remote) |
| `debug vardata-receiver unset third-party` | device | `panos_debug_vardata_receiver` | (live device state — SSH via --remote) |
| `debug vm-monitor clear source-name` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug vm-monitor reset source-name` | device | `panos_debug_misc` | (live device state — SSH via --remote) |
| `debug wildfire batch-forward set disable` | device | `panos_debug_wildfire` | (live device state — SSH via --remote) |
| `debug wildfire batch-forward set max-count` | device | `panos_debug_wildfire` | (live device state — SSH via --remote) |
| `debug wildfire batch-forward set timeout` | device | `panos_debug_wildfire` | (live device state — SSH via --remote) |
| `debug wildfire cloud-info channel` | device | `panos_debug_wildfire` | (live device state — SSH via --remote) |
| `debug wildfire content-info` | device | `panos_debug_wildfire` | (live device state — SSH via --remote) |
| `debug wildfire dp-status` | device | `panos_debug_wildfire` | (live device state — SSH via --remote) |
| `debug wildfire file-cache` | device | `panos_debug_wildfire` | (live device state — SSH via --remote) |
| `debug wildfire file-digest sha256` | device | `panos_debug_wildfire` | (live device state — SSH via --remote) |
| `debug wildfire monitor-log` | device | `panos_debug_wildfire` | (live device state — SSH via --remote) |
| `debug wildfire monitor-log interval` | device | `panos_debug_wildfire` | (live device state — SSH via --remote) |
| `debug wildfire monitor-log max-size` | device | `panos_debug_wildfire` | (live device state — SSH via --remote) |
| `debug wildfire report-process channel` | device | `panos_debug_wildfire` | (live device state — SSH via --remote) |
| `debug wildfire reset all` | device | `panos_debug_wildfire` | (live device state — SSH via --remote) |
| `debug wildfire reset dp-receiver` | device | `panos_debug_wildfire` | (live device state — SSH via --remote) |
| `debug wildfire reset file-cache` | device | `panos_debug_wildfire` | (live device state — SSH via --remote) |
| `debug wildfire reset forwarding channel` | device | `panos_debug_wildfire` | (live device state — SSH via --remote) |
| `debug wildfire reset log-cache channel` | device | `panos_debug_wildfire` | (live device state — SSH via --remote) |
| `debug wildfire reset report-cache channel` | device | `panos_debug_wildfire` | (live device state — SSH via --remote) |
| `debug wildfire server-selection` | device | `panos_debug_wildfire` | (live device state — SSH via --remote) |
| `debug wildfire transition-file-list` | device | `panos_debug_wildfire` | (live device state — SSH via --remote) |
| `debug wildfire upload-log log disable` | device | `panos_debug_wildfire` | (live device state — SSH via --remote) |
| `debug wildfire upload-log log enable` | device | `panos_debug_wildfire` | (live device state — SSH via --remote) |
| `debug wildfire upload-log log extended-log` | device | `panos_debug_wildfire` | (live device state — SSH via --remote) |
| `debug wildfire upload-log log max-size` | device | `panos_debug_wildfire` | (live device state — SSH via --remote) |
| `debug wildfire upload-log log settings` | device | `panos_debug_wildfire` | (live device state — SSH via --remote) |
| `debug wildfire upload-log show channel` | device | `panos_debug_wildfire` | (live device state — SSH via --remote) |
| `delete admin-sessions username` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete anti-virus update` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete auth` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete authentication system-lock-files` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete authentication user-file ssh-known-hosts self` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete authentication user-file ssh-known-hosts user username` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete config saved` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete config-audit-history` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete content cache curr-content version` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete content cache old-content` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete content update` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete core data-plane file` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete core large-core file` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete core management-plane file` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete data-capture directory` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete debug-filter file` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete debug-log dp-log file` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete debug-log mp-global file` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete debug-log mp-log file` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete device-serialno host all` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete device-serialno host all-from-cloud` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete device-serialno host all-from-ldap` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete device-serialno host serialno` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete dnsproxy file` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete global-protect global-protect-portal portal` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete global-protect-client image` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete global-protect-client version` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete global-protect-clientless-vpn update` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete high-availability-key` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete high-availability-known-hosts` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete hip-mdm-cache mobile-id` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete hip-profile-database all` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete hip-profile-database check-delete-all-status` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete hip-profile-database entry ip` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete hip-report all logout-only` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete hip-report report user` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete iot cache curr-iot version` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete iot cache old-iot` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete license key` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete license token-file` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete logo` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete pcap directory` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete policy-cache` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete pprof management-plane file` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete report custom scope` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete report predefined scope` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete report summary scope` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete runtime-user-db` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete server cert` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete software version` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete ssh-authentication-public-key` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete sslmgr-store certificate-info portal name` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete sslmgr-store satellite-info portal name` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete sslmgr-store satellite-info-revoke-certificate portal` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete unknown-pcap directory` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete url-database all` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete url-database url` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete user-group-cache` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete wf-private update` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete wildfire update` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete wildfire-realtime-cache virus-pattern-type` | device | `panos_delete` | (live device state — SSH via --remote) |
| `delete wildfire-realtime-stats` | device | `panos_delete` | (live device state — SSH via --remote) |
| `diff config num-context-lines` | device | `panos_diff` | (live device state — SSH via --remote) |
| `ftp export log` | device | `panos_ftp` | (live device state — SSH via --remote) |
| `grep invert-match` | device | `panos_grep` | (live device state — SSH via --remote) |
| `less agent-log` | device | `panos_less` | (live device state — SSH via --remote) |
| `less custom-page` | device | `panos_less` | (live device state — SSH via --remote) |
| `less db-log` | device | `panos_less` | (live device state — SSH via --remote) |
| `less dp-backtrace` | device | `panos_less` | (live device state — SSH via --remote) |
| `less dp-log` | device | `panos_less` | (live device state — SSH via --remote) |
| `less largecore-mp-backtrace` | device | `panos_less` | (live device state — SSH via --remote) |
| `less mp-backtrace` | device | `panos_less` | (live device state — SSH via --remote) |
| `less mp-global` | device | `panos_less` | (live device state — SSH via --remote) |
| `less mp-log` | device | `panos_less` | (live device state — SSH via --remote) |
| `less plugins-log` | device | `panos_less` | (live device state — SSH via --remote) |
| `less webserver-log` | device | `panos_less` | (live device state — SSH via --remote) |
| `ping bypass-routing` | device | `panos_ping` | (live device state — SSH via --remote) |
| `request acknowledge logid` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request address-expansion expand object-name` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request anti-virus downgrade install` | device | `panos_request_anti_virus` | (live device state — SSH via --remote) |
| `request anti-virus upgrade check` | device | `panos_request_anti_virus` | (live device state — SSH via --remote) |
| `request anti-virus upgrade download sync-to-peer` | device | `panos_request_anti_virus` | (live device state — SSH via --remote) |
| `request anti-virus upgrade info` | device | `panos_request_anti_virus` | (live device state — SSH via --remote) |
| `request anti-virus upgrade install commit` | device | `panos_request_anti_virus` | (live device state — SSH via --remote) |
| `request api key expiration` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request authentication unlock-admin user` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request authentication unlock-user vsys` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request authkey set` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request certificate fetch otp` | device | `panos_request_certificate` | (live device state — SSH via --remote) |
| `request certificate generate certificate-name` | device | `panos_request_certificate` | (live device state — SSH via --remote) |
| `request certificate generate-scep-client-cert certificate-name` | device | `panos_request_certificate` | (live device state — SSH via --remote) |
| `request certificate import-scep-ca-cert certificate-name` | device | `panos_request_certificate` | (live device state — SSH via --remote) |
| `request certificate is-blocked certificate-name` | device | `panos_request_certificate` | (live device state — SSH via --remote) |
| `request certificate renew certificate-name` | device | `panos_request_certificate` | (live device state — SSH via --remote) |
| `request certificate revoke certificate-name` | device | `panos_request_certificate` | (live device state — SSH via --remote) |
| `request certificate revoke sslmgr-store db-serialno` | device | `panos_request_certificate` | (live device state — SSH via --remote) |
| `request certificate show certificate-name` | device | `panos_request_certificate` | (live device state — SSH via --remote) |
| `request certificate show-blocked` | device | `panos_request_certificate` | (live device state — SSH via --remote) |
| `request certificate show-blocked shared` | device | `panos_request_certificate` | (live device state — SSH via --remote) |
| `request clean-replay entries` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request clear-commit-tasks` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request commit-lock add comment` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request commit-lock remove admin` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request config diff ver1` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request config list commit-versions filter filter-data` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request config list commit-versions filter filter-query` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request config list commit-versions locations version` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request config-lock add comment` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request config-lock remove` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request content downgrade skip-content-validity-check` | device | `panos_request_content` | (live device state — SSH via --remote) |
| `request content upgrade check` | device | `panos_request_content` | (live device state — SSH via --remote) |
| `request content upgrade download sync-to-peer` | device | `panos_request_content` | (live device state — SSH via --remote) |
| `request content upgrade info` | device | `panos_request_content` | (live device state — SSH via --remote) |
| `request content upgrade install commit` | device | `panos_request_content` | (live device state — SSH via --remote) |
| `request content validity-check` | device | `panos_request_content` | (live device state — SSH via --remote) |
| `request cpld-restart` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request data-filtering access-password create password` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request data-filtering access-password delete` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request data-filtering access-password modify old-password` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request determine-new-applications version` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request device-quarantine-list add ip` | device | `panos_request_device_quarantine_list` | (live device state — SSH via --remote) |
| `request device-quarantine-list delete host` | device | `panos_request_device_quarantine_list` | (live device state — SSH via --remote) |
| `request device-quarantine-list show all option` | device | `panos_request_device_quarantine_list` | (live device state — SSH via --remote) |
| `request device-quarantine-list show hostid` | device | `panos_request_device_quarantine_list` | (live device state — SSH via --remote) |
| `request device-quarantine-list show serialno` | device | `panos_request_device_quarantine_list` | (live device state — SSH via --remote) |
| `request device-registration username` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request device-telemetry` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request dhcp client ipv6 release` | device | `panos_request_dhcp` | (live device state — SSH via --remote) |
| `request dhcp client ipv6 renew` | device | `panos_request_dhcp` | (live device state — SSH via --remote) |
| `request dhcp client management-interface` | device | `panos_request_dhcp` | (live device state — SSH via --remote) |
| `request dhcp client release` | device | `panos_request_dhcp` | (live device state — SSH via --remote) |
| `request dhcp client renew` | device | `panos_request_dhcp` | (live device state — SSH via --remote) |
| `request dhcpv6 client management-interface` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request disable-ztp` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request dnsproxy license refresh` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request encryption-level level` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request get-application-status application` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request get-disabled-applications` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request global-protect-client software activate file` | device | `panos_request_global_protect_client` | (live device state — SSH via --remote) |
| `request global-protect-client software activate version` | device | `panos_request_global_protect_client` | (live device state — SSH via --remote) |
| `request global-protect-client software check` | device | `panos_request_global_protect_client` | (live device state — SSH via --remote) |
| `request global-protect-client software download sync-to-peer` | device | `panos_request_global_protect_client` | (live device state — SSH via --remote) |
| `request global-protect-client software info` | device | `panos_request_global_protect_client` | (live device state — SSH via --remote) |
| `request global-protect-clientless-vpn downgrade install` | device | `panos_request_global_protect_clientless_vpn` | (live device state — SSH via --remote) |
| `request global-protect-clientless-vpn upgrade check` | device | `panos_request_global_protect_clientless_vpn` | (live device state — SSH via --remote) |
| `request global-protect-clientless-vpn upgrade download latest sync-to-peer` | device | `panos_request_global_protect_clientless_vpn` | (live device state — SSH via --remote) |
| `request global-protect-clientless-vpn upgrade info` | device | `panos_request_global_protect_clientless_vpn` | (live device state — SSH via --remote) |
| `request global-protect-clientless-vpn upgrade install commit` | device | `panos_request_global_protect_clientless_vpn` | (live device state — SSH via --remote) |
| `request global-protect-gateway check-client-logout-all-status` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request global-protect-gateway client-logout gateway` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request global-protect-gateway client-logout-all gateway` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request global-protect-gateway satellite-logout gateway` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request global-protect-portal client-logout portal` | device | `panos_request_global_protect_portal` | (live device state — SSH via --remote) |
| `request global-protect-portal refresh-csc-cookie-key` | device | `panos_request_global_protect_portal` | (live device state — SSH via --remote) |
| `request global-protect-portal refresh-scep-cookie-key` | device | `panos_request_global_protect_portal` | (live device state — SSH via --remote) |
| `request global-protect-portal restore-satellite-cookie-expiration` | device | `panos_request_global_protect_portal` | (live device state — SSH via --remote) |
| `request global-protect-portal set-satellite-cookie-expiration value` | device | `panos_request_global_protect_portal` | (live device state — SSH via --remote) |
| `request global-protect-portal ticket portal` | device | `panos_request_global_protect_portal` | (live device state — SSH via --remote) |
| `request global-protect-satellite get-gateway-config satellite` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request global-protect-satellite get-portal-config satellite` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request global-protect-satellite refresh-cookie-key` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request high-availability cluster clear-cache` | device | `panos_request_high_availability` | (live device state — SSH via --remote) |
| `request high-availability cluster sync-from` | device | `panos_request_high_availability` | (live device state — SSH via --remote) |
| `request high-availability session-reestablish force` | device | `panos_request_high_availability` | (live device state — SSH via --remote) |
| `request high-availability state functional` | device | `panos_request_high_availability` | (live device state — SSH via --remote) |
| `request high-availability state peer` | device | `panos_request_high_availability` | (live device state — SSH via --remote) |
| `request high-availability state suspend` | device | `panos_request_high_availability` | (live device state — SSH via --remote) |
| `request high-availability sync-to-remote` | device | `panos_request_high_availability` | (live device state — SSH via --remote) |
| `request high-availability sync-to-remote id-manager` | device | `panos_request_high_availability` | (live device state — SSH via --remote) |
| `request hsm` | device | `panos_request_hsm` | (live device state — SSH via --remote) |
| `request hsm authenticate server` | device | `panos_request_hsm` | (live device state — SSH via --remote) |
| `request hsm client-version` | device | `panos_request_hsm` | (live device state — SSH via --remote) |
| `request hsm ha create-ha-group password` | device | `panos_request_hsm` | (live device state — SSH via --remote) |
| `request hsm ha recover` | device | `panos_request_hsm` | (live device state — SSH via --remote) |
| `request hsm ha replace-server password` | device | `panos_request_hsm` | (live device state — SSH via --remote) |
| `request hsm ha synchronize password` | device | `panos_request_hsm` | (live device state — SSH via --remote) |
| `request hsm login password` | device | `panos_request_hsm` | (live device state — SSH via --remote) |
| `request hsm server-enroll` | device | `panos_request_hsm` | (live device state — SSH via --remote) |
| `request iot upgrade` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request iot validity-check` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request last-acknowledge-time` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request license api-key delete` | device | `panos_request_license` | (live device state — SSH via --remote) |
| `request license api-key set key` | device | `panos_request_license` | (live device state — SSH via --remote) |
| `request license api-key show` | device | `panos_request_license` | (live device state — SSH via --remote) |
| `request license deactivate key mode` | device | `panos_request_license` | (live device state — SSH via --remote) |
| `request license deactivate vm-capacity mode` | device | `panos_request_license` | (live device state — SSH via --remote) |
| `request license fetch auth-code` | device | `panos_request_license` | (live device state — SSH via --remote) |
| `request license info` | device | `panos_request_license` | (live device state — SSH via --remote) |
| `request license install` | device | `panos_request_license` | (live device state — SSH via --remote) |
| `request list-content-downloads` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request log-collector-forwarding status` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request logdb migrate-to-panorama start type` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request logdb migrate-to-panorama status type` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request logdb migrate-to-panorama stop type` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request logging-service-forwarding certificate delete` | device | `panos_request_logging_service_forwarding` | (live device state — SSH via --remote) |
| `request logging-service-forwarding certificate fetch` | device | `panos_request_logging_service_forwarding` | (live device state — SSH via --remote) |
| `request logging-service-forwarding certificate fetch-noproxy pre-shared-key` | device | `panos_request_logging_service_forwarding` | (live device state — SSH via --remote) |
| `request logging-service-forwarding certificate info` | device | `panos_request_logging_service_forwarding` | (live device state — SSH via --remote) |
| `request logging-service-forwarding customerinfo` | device | `panos_request_logging_service_forwarding` | (live device state — SSH via --remote) |
| `request logging-service-forwarding status` | device | `panos_request_logging_service_forwarding` | (live device state — SSH via --remote) |
| `request master-key new-master-key` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request mongo set storage-engine instance` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request mongo show storage-engine instance` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request multi-config` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request panorama-connectivity-check` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request password-change-history dump-history` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request password-change-history re-encrypt old-master-key` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request password-hash password` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request pppoe ipv6 dhcpv6 release` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request pppoe ipv6 dhcpv6 renew` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request quota-enforcement` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request resolve vsys` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request restart dataplane` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request restart software` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request restart system with-swap-scrub` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request routing` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request routing show-config virtual-router` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request routing show-error virtual-router` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request saas_agent certificate info` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request session-discard id` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request set-application-status-recursive enable-dependent-apps` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request shutdown system with-swap-scrub` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request stats dump` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request streaming-telemetry reload-config` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request support` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request system bootstrap-usb delete bundle` | device | `panos_request_system` | (live device state — SSH via --remote) |
| `request system bootstrap-usb prepare from` | device | `panos_request_system` | (live device state — SSH via --remote) |
| `request system external-list global-find string` | device | `panos_request_system` | (live device state — SSH via --remote) |
| `request system external-list list-capacities` | device | `panos_request_system` | (live device state — SSH via --remote) |
| `request system external-list refresh type domain name` | device | `panos_request_system` | (live device state — SSH via --remote) |
| `request system external-list refresh type ip name` | device | `panos_request_system` | (live device state — SSH via --remote) |
| `request system external-list refresh type url name` | device | `panos_request_system` | (live device state — SSH via --remote) |
| `request system external-list show type` | device | `panos_request_system` | (live device state — SSH via --remote) |
| `request system external-list stats type` | device | `panos_request_system` | (live device state — SSH via --remote) |
| `request system external-list url-test` | device | `panos_request_system` | (live device state — SSH via --remote) |
| `request system fqdn` | device | `panos_request_system` | (live device state — SSH via --remote) |
| `request system idmap-sync` | device | `panos_request_system` | (live device state — SSH via --remote) |
| `request system patch apply` | device | `panos_request_system` | (live device state — SSH via --remote) |
| `request system patch check` | device | `panos_request_system` | (live device state — SSH via --remote) |
| `request system patch download version` | device | `panos_request_system` | (live device state — SSH via --remote) |
| `request system patch info version` | device | `panos_request_system` | (live device state — SSH via --remote) |
| `request system patch install version` | device | `panos_request_system` | (live device state — SSH via --remote) |
| `request system patch revert` | device | `panos_request_system` | (live device state — SSH via --remote) |
| `request system patch scp-export profile-name` | device | `panos_request_system` | (live device state — SSH via --remote) |
| `request system patch scp-import profile-name` | device | `panos_request_system` | (live device state — SSH via --remote) |
| `request system private-data-reset shutdown` | device | `panos_request_system` | (live device state — SSH via --remote) |
| `request system self-test crypto` | device | `panos_request_system` | (live device state — SSH via --remote) |
| `request system self-test force-crypto-failure dp` | device | `panos_request_system` | (live device state — SSH via --remote) |
| `request system self-test force-crypto-failure mp` | device | `panos_request_system` | (live device state — SSH via --remote) |
| `request system self-test force-software-integrity-failure` | device | `panos_request_system` | (live device state — SSH via --remote) |
| `request system self-test software-integrity` | device | `panos_request_system` | (live device state — SSH via --remote) |
| `request system self-test-job` | device | `panos_request_system` | (live device state — SSH via --remote) |
| `request system software download scp-profile` | device | `panos_request_system` | (live device state — SSH via --remote) |
| `request system software eligible to-version` | device | `panos_request_system` | (live device state — SSH via --remote) |
| `request system software info` | device | `panos_request_system` | (live device state — SSH via --remote) |
| `request system software install load-config` | device | `panos_request_system` | (live device state — SSH via --remote) |
| `request system software scp-export profile-name` | device | `panos_request_system` | (live device state — SSH via --remote) |
| `request system software scp-import profile-name` | device | `panos_request_system` | (live device state — SSH via --remote) |
| `request tech-support copy-to-remote-host remote-hostname` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request tech-support dump` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request telemetry-data dump` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request ui telemetry` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request url-filtering install pandb-database` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request url-filtering save url-database` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request url-filtering update url` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request user-id cloud-identity-engine config-data status` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request wf-private downgrade install` | device | `panos_request_wf_private` | (live device state — SSH via --remote) |
| `request wf-private upgrade check` | device | `panos_request_wf_private` | (live device state — SSH via --remote) |
| `request wf-private upgrade download latest sync-to-peer` | device | `panos_request_wf_private` | (live device state — SSH via --remote) |
| `request wf-private upgrade info` | device | `panos_request_wf_private` | (live device state — SSH via --remote) |
| `request wf-private upgrade install commit` | device | `panos_request_wf_private` | (live device state — SSH via --remote) |
| `request wildfire downgrade install` | device | `panos_request_wildfire` | (live device state — SSH via --remote) |
| `request wildfire registration channel` | device | `panos_request_wildfire` | (live device state — SSH via --remote) |
| `request wildfire upgrade check` | device | `panos_request_wildfire` | (live device state — SSH via --remote) |
| `request wildfire upgrade download latest sync-to-peer` | device | `panos_request_wildfire` | (live device state — SSH via --remote) |
| `request wildfire upgrade info` | device | `panos_request_wildfire` | (live device state — SSH via --remote) |
| `request wildfire upgrade install commit` | device | `panos_request_wildfire` | (live device state — SSH via --remote) |
| `request wildfire-realtime-cache add virus-pattern-type` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `request wildfire-realtime-cache delete virus-pattern-type` | device | `panos_request_misc` | (live device state — SSH via --remote) |
| `schedule botnet-report period` | device | `panos_schedule` | (live device state — SSH via --remote) |
| `schedule saas-applications-usage-report skip-detailed-report` | device | `panos_schedule` | (live device state — SSH via --remote) |
| `schedule uar-report user` | device | `panos_schedule` | (live device state — SSH via --remote) |
| `scp export` | device | `panos_scp` | (live device state — SSH via --remote) |
| `scp export certificate to` | device | `panos_scp` | (live device state — SSH via --remote) |
| `scp export core-file data-plane from` | device | `panos_scp` | (live device state — SSH via --remote) |
| `scp export core-file large-corefile from` | device | `panos_scp` | (live device state — SSH via --remote) |
| `scp export core-file management-plane from` | device | `panos_scp` | (live device state — SSH via --remote) |
| `scp export debug bootmem_file from` | device | `panos_scp` | (live device state — SSH via --remote) |
| `scp export log` | device | `panos_scp` | (live device state — SSH via --remote) |
| `scp export log-file data-plane to` | device | `panos_scp` | (live device state — SSH via --remote) |
| `scp export log-file management-plane to` | device | `panos_scp` | (live device state — SSH via --remote) |
| `scp export pprof-file management-plane from` | device | `panos_scp` | (live device state — SSH via --remote) |
| `scp export stats-dump to` | device | `panos_scp` | (live device state — SSH via --remote) |
| `scp export threat-pcap pcap-id` | device | `panos_scp` | (live device state — SSH via --remote) |
| `scp import` | device | `panos_scp` | (live device state — SSH via --remote) |
| `scp import certificate from` | device | `panos_scp` | (live device state — SSH via --remote) |
| `scp import hsm-ciphertrust-client-cert from` | device | `panos_scp` | (live device state — SSH via --remote) |
| `scp import hsm-ciphertrust-client-key from` | device | `panos_scp` | (live device state — SSH via --remote) |
| `scp import hsm-ciphertrust-server-cert from` | device | `panos_scp` | (live device state — SSH via --remote) |
| `scp import hsm-server-cert from` | device | `panos_scp` | (live device state — SSH via --remote) |
| `scp import idp-metadata profile-name` | device | `panos_scp` | (live device state — SSH via --remote) |
| `scp import keypair from` | device | `panos_scp` | (live device state — SSH via --remote) |
| `scp import private-key from` | device | `panos_scp` | (live device state — SSH via --remote) |
| `set advanced-routing fib check default-interval` | device | `panos_set_advanced_routing` | (live device state — SSH via --remote) |
| `set advanced-routing fib check disable` | device | `panos_set_advanced_routing` | (live device state — SSH via --remote) |
| `set advanced-routing fib check disable-auto-recovery` | device | `panos_set_advanced_routing` | (live device state — SSH via --remote) |
| `set advanced-routing fib check interval` | device | `panos_set_advanced_routing` | (live device state — SSH via --remote) |
| `set advanced-routing fib check recovery-failure-threshold` | device | `panos_set_advanced_routing` | (live device state — SSH via --remote) |
| `set application dump off` | device | `panos_set_application` | (live device state — SSH via --remote) |
| `set application dump on limit` | device | `panos_set_application` | (live device state — SSH via --remote) |
| `set application traceroute enable` | device | `panos_set_application` | (live device state — SSH via --remote) |
| `set application traceroute ttl-threshold` | device | `panos_set_application` | (live device state — SSH via --remote) |
| `set audit-comment xpath` | device | `panos_set_misc` | (live device state — SSH via --remote) |
| `set auth remote-host-check` | device | `panos_set_misc` | (live device state — SSH via --remote) |
| `set auth strict-username-check` | device | `panos_set_misc` | (live device state — SSH via --remote) |
| `set authentication radius-vsa-off` | device | `panos_set_misc` | (live device state — SSH via --remote) |
| `set authentication radius-vsa-on` | device | `panos_set_misc` | (live device state — SSH via --remote) |
| `set authentication saml_signature_digest_algorithm` | device | `panos_set_misc` | (live device state — SSH via --remote) |
| `set cli` | device | `panos_set_cli` | (live device state — SSH via --remote) |
| `set cli config-output-format` | device | `panos_set_cli` | (live device state — SSH via --remote) |
| `set cli hide-ip value` | device | `panos_set_cli` | (live device state — SSH via --remote) |
| `set cli hide-user value` | device | `panos_set_cli` | (live device state — SSH via --remote) |
| `set cli terminal height` | device | `panos_set_cli` | (live device state — SSH via --remote) |
| `set cli terminal type` | device | `panos_set_cli` | (live device state — SSH via --remote) |
| `set cli terminal width` | device | `panos_set_cli` | (live device state — SSH via --remote) |
| `set cli timeout idle` | device | `panos_set_cli` | (live device state — SSH via --remote) |
| `set clock date` | device | `panos_set_misc` | (live device state — SSH via --remote) |
| `set data-access-password` | device | `panos_set_misc` | (live device state — SSH via --remote) |
| `set device-inventory-edit add-device mac` | device | `panos_set_misc` | (live device state — SSH via --remote) |
| `set device-inventory-edit edit-devices hostname` | device | `panos_set_misc` | (live device state — SSH via --remote) |
| `set device-inventory-upload csvfile` | device | `panos_set_misc` | (live device state — SSH via --remote) |
| `set fwd-uni-dhcp-packet-on-dhcp-client-intf` | device | `panos_set_misc` | (live device state — SSH via --remote) |
| `set global-protect arg-maxlen` | device | `panos_set_global_protect` | (live device state — SSH via --remote) |
| `set global-protect global-protect-portal portal` | device | `panos_set_global_protect` | (live device state — SSH via --remote) |
| `set global-protect redirect location` | device | `panos_set_global_protect` | (live device state — SSH via --remote) |
| `set global-protect redirect off` | device | `panos_set_global_protect` | (live device state — SSH via --remote) |
| `set global-protect redirect on` | device | `panos_set_global_protect` | (live device state — SSH via --remote) |
| `set global-protect redirect show` | device | `panos_set_global_protect` | (live device state — SSH via --remote) |
| `set global-protect satellite-serialnumberip-auth` | device | `panos_set_global_protect` | (live device state — SSH via --remote) |
| `set logrcvr offline-logpurger interval` | device | `panos_set_misc` | (live device state — SSH via --remote) |
| `set logrcvr offline-logpurger percentage-threshold` | device | `panos_set_misc` | (live device state — SSH via --remote) |
| `set management-server logging` | device | `panos_set_misc` | (live device state — SSH via --remote) |
| `set max-num-images count` | device | `panos_set_misc` | (live device state — SSH via --remote) |
| `set mgmtbond` | device | `panos_set_misc` | (live device state — SSH via --remote) |
| `set nw-id-api data` | device | `panos_set_misc` | (live device state — SSH via --remote) |
| `set password` | device | `panos_set_misc` | (live device state — SSH via --remote) |
| `set preserve-prenat-feature adjust-mtu` | device | `panos_set_misc` | (live device state — SSH via --remote) |
| `set preserve-prenat-feature verify-checksum` | device | `panos_set_misc` | (live device state — SSH via --remote) |
| `set quarantine data` | device | `panos_set_misc` | (live device state — SSH via --remote) |
| `set session` | device | `panos_set_session` | (live device state — SSH via --remote) |
| `set session accelerated-aging-scaling-factor` | device | `panos_set_session` | (live device state — SSH via --remote) |
| `set session accelerated-aging-threshold` | device | `panos_set_session` | (live device state — SSH via --remote) |
| `set session default` | device | `panos_set_session` | (live device state — SSH via --remote) |
| `set session ingress_backlogs_duration` | device | `panos_set_session` | (live device state — SSH via --remote) |
| `set session ingress_backlogs_threshold` | device | `panos_set_session` | (live device state — SSH via --remote) |
| `set session lag-flow-key-type` | device | `panos_set_session` | (live device state — SSH via --remote) |
| `set session pvst-native-vlan-id` | device | `panos_set_session` | (live device state — SSH via --remote) |
| `set session resource-limit-behavior` | device | `panos_set_session` | (live device state — SSH via --remote) |
| `set session scan-scaling-factor` | device | `panos_set_session` | (live device state — SSH via --remote) |
| `set session scan-threshold` | device | `panos_set_session` | (live device state — SSH via --remote) |
| `set session tcp-cong-ctrl` | device | `panos_set_session` | (live device state — SSH via --remote) |
| `set session tcp-reject-small-initial-window-threshold` | device | `panos_set_session` | (live device state — SSH via --remote) |
| `set session tcp-rsts` | device | `panos_set_session` | (live device state — SSH via --remote) |
| `set session timeout-scan` | device | `panos_set_session` | (live device state — SSH via --remote) |
| `set session timeout-tcp-delayed-ack` | device | `panos_set_session` | (live device state — SSH via --remote) |
| `set session timeout-tcp-half-closed` | device | `panos_set_session` | (live device state — SSH via --remote) |
| `set session timeout-tcp-time-wait` | device | `panos_set_session` | (live device state — SSH via --remote) |
| `set session timeout-tcp-unverified-rst` | device | `panos_set_session` | (live device state — SSH via --remote) |
| `set session timeout-tcphandshake` | device | `panos_set_session` | (live device state — SSH via --remote) |
| `set session timeout-tcpinit` | device | `panos_set_session` | (live device state — SSH via --remote) |
| `set snmpd refresh-timer-period` | device | `panos_set_misc` | (live device state — SSH via --remote) |
| `set ssh service-restart` | device | `panos_set_misc` | (live device state — SSH via --remote) |
| `set ssh-authentication public-key` | device | `panos_set_misc` | (live device state — SSH via --remote) |
| `set ssl add-secure-renegotiation-extension` | device | `panos_set_misc` | (live device state — SSH via --remote) |
| `set ssl-conn-on-cert fail-all-conns` | device | `panos_set_misc` | (live device state — SSH via --remote) |
| `set ssl-conn-on-cert fail-syslog-conns` | device | `panos_set_misc` | (live device state — SSH via --remote) |
| `set sslmgr-check-cert-jobs max-limit` | device | `panos_set_misc` | (live device state — SSH via --remote) |
| `set syslog fqdn-refresh` | device | `panos_set_syslog` | (live device state — SSH via --remote) |
| `set syslog ssl-conn-validation all-conns` | device | `panos_set_syslog` | (live device state — SSH via --remote) |
| `set syslog ssl-conn-validation explicit crl` | device | `panos_set_syslog` | (live device state — SSH via --remote) |
| `set syslog ssl-conn-validation explicit eku` | device | `panos_set_syslog` | (live device state — SSH via --remote) |
| `set syslog ssl-conn-validation explicit ocsp` | device | `panos_set_syslog` | (live device state — SSH via --remote) |
| `set system setting` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting additional-threat-log` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting alg-natref` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting alg-persistent-nat` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting arp-cache-timeout` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting ctd` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting ctd ctd-agent-assigned-cores` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting ctd feature-forward cloud-appid-prefiltering` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting ctd feature-forward mica` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting ctd lscan-mode` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting ctd lscan-mode-default` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting ctd max-sess-hash-limit` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting ctd nonblocking-pattern-match-interval` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting ctd pkt-proc-boundary` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting ctd pkt-proc-loop-high` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting ctd pkt-proc-loop-low` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting ctd regex-stats-on` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting ctd wif-shared-buf-threshold` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting ctd-mode` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting ctd-mode-default` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting delay-interface-process interface` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting dfa-mode` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting dfa-mode-default` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting hardware-acl-blocking-duration` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting hardware-acl-blocking-enable` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting icmp6-error` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting ip6-defrag-timeout` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting jumbo-frame` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting layer4-checksum` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting logging default` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting logging default-policy-logging` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting logging log-compression` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting logging log-suppression` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting logging max-log-rate` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting logging max-packet-rate` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting mp-vr-vif-install-only-host-route` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting multi-vsys` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting packet ip-frag-limit` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting packet-path-test enable` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting packet-path-test show` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting paloalto-networks-service-proxy` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting persistent-dipp-alert` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting pow` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting pppoe-dont-send-eol interface` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting shared-policy` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting software-acl-blocking-duration` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting ssl-decrypt` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting ssl-decrypt answer-timeout` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting ssl-decrypt tunnel-taildrop-threshold` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting target-vsys` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting template` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting util assert-crash-once` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting wildfire disk-quota` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting wildfire disk-quota global` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting wildfire interval report-update-interval` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting wildfire interval server-list-update-interval` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting zip enable` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set system setting zip hw-reset` | device | `panos_set_system` | (live device state — SSH via --remote) |
| `set transceiver-monitor-rate slot` | device | `panos_set_misc` | (live device state — SSH via --remote) |
| `set user-id data` | device | `panos_set_misc` | (live device state — SSH via --remote) |
| `set xmlapi-group add group` | device | `panos_set_misc` | (live device state — SSH via --remote) |
| `set xmlapi-group delete group` | device | `panos_set_misc` | (live device state — SSH via --remote) |
| `set xmlapi-group refresh group` | device | `panos_set_misc` | (live device state — SSH via --remote) |
| `set ztp panorama-timeout` | device | `panos_set_misc` | (live device state — SSH via --remote) |
| `show adem probes` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show adem routeinfo destination` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show admins` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show advanced-routing bfd active-profile name` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing bfd details logical-router` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing bfd drop-counters session-id` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing bfd summary logical-router` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing bgp filters access-list logical-router` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing bgp filters prefix-list logical-router` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing bgp filters route-map logical-router` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing bgp loc-rib-detail peer` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing bgp peer` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing bgp peer detail peer-name` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing bgp peer status peer-name` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing bgp peer-groups logical-router` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing bgp rib-out-detail peer` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing bgp route afi` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing bgp summary logical-router` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing fib afi` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing interface logical-router` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing logical-router lr-name` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing multicast fib group` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing multicast group-permission interface` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing multicast igmp interface logical-router` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing multicast igmp membership interface` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing multicast igmp statistics interface` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing multicast msdp peer detail peer-name` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing multicast msdp peer status peer-name` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing multicast msdp sa logical-router` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing multicast msdp statistics logical-router` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing multicast msdp summary logical-router` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing multicast pim elected-bsr logical-router` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing multicast pim group-mapping group` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing multicast pim interface logical-router` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing multicast pim neighbor logical-router` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing multicast pim rpf static` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing multicast pim state logical-router` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing multicast pim statistics interface` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing multicast route group` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing ospf` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing ospf dumplsdb adv-rtr` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing ospf interface brief` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing ospf lsdb adv-rtr` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing ospf neighbor brief` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing ospf virt-neighbor brief` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing ospfv3` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing ospfv3 dumplsdb scope` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing ospfv3 interface brief` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing ospfv3 lsdb scope` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing ospfv3 neighbor brief` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing ospfv3 virt-neighbor brief` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing resource logical-router` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing rip` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing route destination` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show advanced-routing static-route-path-monitor logical-router` | device | `panos_show_advanced_routing` | (live device state — SSH via --remote) |
| `show api-key-expiration-ts` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show applications vsys` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show auth` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show authentication allowlist` | device | `panos_show_authentication` | (live device state — SSH via --remote) |
| `show authentication groupdb` | device | `panos_show_authentication` | (live device state — SSH via --remote) |
| `show authentication groupnames` | device | `panos_show_authentication` | (live device state — SSH via --remote) |
| `show authentication local-user-db vsys` | device | `panos_show_authentication` | (live device state — SSH via --remote) |
| `show authentication locked-users vsys` | device | `panos_show_authentication` | (live device state — SSH via --remote) |
| `show authentication service-principal vsys` | device | `panos_show_authentication` | (live device state — SSH via --remote) |
| `show authentication service-principals vsys` | device | `panos_show_authentication` | (live device state — SSH via --remote) |
| `show authentication statistics username` | device | `panos_show_authentication` | (live device state — SSH via --remote) |
| `show bad-custom-signature` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show bonjour interface` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show chassis inventory` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show chassis-ready` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show cli` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show clock more` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show cloud-appid` | device | `panos_show_cloud_appid` | (live device state — SSH via --remote) |
| `show cloud-appid app-to-filtergroup-mapping batch-idx` | device | `panos_show_cloud_appid` | (live device state — SSH via --remote) |
| `show cloud-appid application` | device | `panos_show_cloud_appid` | (live device state — SSH via --remote) |
| `show cloud-appid application-filter all` | device | `panos_show_cloud_appid` | (live device state — SSH via --remote) |
| `show cloud-appid application-filter option vsys` | device | `panos_show_cloud_appid` | (live device state — SSH via --remote) |
| `show cloud-appid application-group all` | device | `panos_show_cloud_appid` | (live device state — SSH via --remote) |
| `show cloud-appid application-group option vsys` | device | `panos_show_cloud_appid` | (live device state — SSH via --remote) |
| `show cloud-appid cloud-app-data app-metadata` | device | `panos_show_cloud_appid` | (live device state — SSH via --remote) |
| `show cloud-appid cloud-app-data application all` | device | `panos_show_cloud_appid` | (live device state — SSH via --remote) |
| `show cloud-appid cloud-app-data application app-id` | device | `panos_show_cloud_appid` | (live device state — SSH via --remote) |
| `show cloud-appid cloud-app-data application cloud-app-name` | device | `panos_show_cloud_appid` | (live device state — SSH via --remote) |
| `show cloud-appid cloud-app-data application statistics` | device | `panos_show_cloud_appid` | (live device state — SSH via --remote) |
| `show cloud-appid cloud-app-data container all` | device | `panos_show_cloud_appid` | (live device state — SSH via --remote) |
| `show cloud-appid cloud-app-data container container-id` | device | `panos_show_cloud_appid` | (live device state — SSH via --remote) |
| `show cloud-appid cloud-app-data container container-name` | device | `panos_show_cloud_appid` | (live device state — SSH via --remote) |
| `show cloud-appid cloud-app-data container statistics` | device | `panos_show_cloud_appid` | (live device state — SSH via --remote) |
| `show cloud-appid signature-dp` | device | `panos_show_cloud_appid` | (live device state — SSH via --remote) |
| `show cloud-appid signature-dp app-signature all` | device | `panos_show_cloud_appid` | (live device state — SSH via --remote) |
| `show cloud-appid signature-dp app-signature cloud-app-name` | device | `panos_show_cloud_appid` | (live device state — SSH via --remote) |
| `show cloud-appid signature-dp app-signature signature-id` | device | `panos_show_cloud_appid` | (live device state — SSH via --remote) |
| `show cloud-appid signature-dp app-signature statistics` | device | `panos_show_cloud_appid` | (live device state — SSH via --remote) |
| `show cloud-appid signature-dp appid` | device | `panos_show_cloud_appid` | (live device state — SSH via --remote) |
| `show cloud-appid signature-dp threat-signature all` | device | `panos_show_cloud_appid` | (live device state — SSH via --remote) |
| `show cloud-appid signature-dp threat-signature cloud-app-name` | device | `panos_show_cloud_appid` | (live device state — SSH via --remote) |
| `show cloud-appid signature-dp threat-signature statistics` | device | `panos_show_cloud_appid` | (live device state — SSH via --remote) |
| `show cloud-appid signature-dp threat-signature threat-id` | device | `panos_show_cloud_appid` | (live device state — SSH via --remote) |
| `show cloud-appid task all option` | device | `panos_show_cloud_appid` | (live device state — SSH via --remote) |
| `show cloud-appid task statistics` | device | `panos_show_cloud_appid` | (live device state — SSH via --remote) |
| `show cloud-appid task task-index` | device | `panos_show_cloud_appid` | (live device state — SSH via --remote) |
| `show cloud-appid transaction all option` | device | `panos_show_cloud_appid` | (live device state — SSH via --remote) |
| `show cloud-appid transaction trans-index` | device | `panos_show_cloud_appid` | (live device state — SSH via --remote) |
| `show cloud-auth-service-alerts` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show cloud-auth-service-metadata region_id` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show cloud-auth-service-profiles tenant_id` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show cloud-auth-service-regions force_refresh` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show cloud-auth-service-tenants region_id` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show cloud-management-status` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show cloud-userid` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show cluster` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show cluster-userid statistics` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show commit-locks vsys` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show config` | device | `panos_show_config` | (live device state — SSH via --remote) |
| `show config audit base-version` | device | `panos_show_config` | (live device state — SSH via --remote) |
| `show config audit base-version-no-deletes` | device | `panos_show_config` | (live device state — SSH via --remote) |
| `show config audit info` | device | `panos_show_config` | (live device state — SSH via --remote) |
| `show config audit version` | device | `panos_show_config` | (live device state — SSH via --remote) |
| `show config commit-scope partial shared-object` | device | `panos_show_config` | (live device state — SSH via --remote) |
| `show config effective-running xpath` | device | `panos_show_config` | (live device state — SSH via --remote) |
| `show config list admins partial shared-object` | device | `panos_show_config` | (live device state — SSH via --remote) |
| `show config list audit-comments xpath` | device | `panos_show_config` | (live device state — SSH via --remote) |
| `show config list change-summary partial admin` | device | `panos_show_config` | (live device state — SSH via --remote) |
| `show config list changes partial shared-object` | device | `panos_show_config` | (live device state — SSH via --remote) |
| `show config pushed-shared-policy vsys` | device | `panos_show_config` | (live device state — SSH via --remote) |
| `show config running xpath` | device | `panos_show_config` | (live device state — SSH via --remote) |
| `show config saved` | device | `panos_show_config` | (live device state — SSH via --remote) |
| `show config-locks vsys` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show counter global filter category` | device | `panos_show_counter` | (live device state — SSH via --remote) |
| `show counter global name` | device | `panos_show_counter` | (live device state — SSH via --remote) |
| `show counter interface` | device | `panos_show_counter` | (live device state — SSH via --remote) |
| `show counter management-server` | device | `panos_show_counter` | (live device state — SSH via --remote) |
| `show counter rate` | device | `panos_show_counter` | (live device state — SSH via --remote) |
| `show counter total-throughput` | device | `panos_show_counter` | (live device state — SSH via --remote) |
| `show ctd-agent` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show ctd-agent debug` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show ctd-agent status` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show device-certificate` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show device-telemetry` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show device-telemetry stats` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show deviceconfig high-availability election-option` | device | `panos_show_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig high-availability election-option timers` | device | `panos_show_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig high-availability path-monitoring` | device | `panos_show_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig high-availability path-monitoring path-group` | device | `panos_show_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig high-availability peer` | device | `panos_show_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig high-availability peer encryption` | device | `panos_show_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig setting cloud-host-compliance` | device | `panos_show_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig setting management log-forwarding-from-device` | device | `panos_show_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig setting management secure-conn-server authorization-list` | device | `panos_show_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig setting wildfire private-cloud-secure-conn-client` | device | `panos_show_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig setting wildfire private-cloud-secure-conn-client certificate-type` | device | `panos_show_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system config-bundle-export-schedule` | device | `panos_show_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system deployment-update-schedule` | device | `panos_show_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system dlsrvr` | device | `panos_show_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system hsm-settings provider aws-cloudhsm` | device | `panos_show_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system hsm-settings provider aws-cloudhsm health-check-settings` | device | `panos_show_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system hsm-settings provider aws-cloudhsm hsm-cluster` | device | `panos_show_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system maintenance-user` | device | `panos_show_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system management-tunnel` | device | `panos_show_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system management-tunnel crypto-profiles` | device | `panos_show_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system management-tunnel crypto-profiles ikev2-crypto-profiles` | device | `panos_show_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system management-tunnel crypto-profiles ipsec-crypto-profiles` | device | `panos_show_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system management-tunnel ikev2-gateway` | device | `panos_show_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system management-tunnel tunnel` | device | `panos_show_deviceconfig` | (live device state — SSH via --remote) |
| `show deviceconfig system push-schedule` | device | `panos_show_deviceconfig` | (live device state — SSH via --remote) |
| `show dhcp client ipv6 pool-details` | device | `panos_show_dhcp` | (live device state — SSH via --remote) |
| `show dhcp client ipv6 state interface` | device | `panos_show_dhcp` | (live device state — SSH via --remote) |
| `show dhcp client ipv6-gateway-address` | device | `panos_show_dhcp` | (live device state — SSH via --remote) |
| `show dhcp client mgmt-interface-state` | device | `panos_show_dhcp` | (live device state — SSH via --remote) |
| `show dhcp client mgmt6-interface-state` | device | `panos_show_dhcp` | (live device state — SSH via --remote) |
| `show dhcp client state` | device | `panos_show_dhcp` | (live device state — SSH via --remote) |
| `show dhcp inherited state interface` | device | `panos_show_dhcp` | (live device state — SSH via --remote) |
| `show dhcp server lease interface` | device | `panos_show_dhcp` | (live device state — SSH via --remote) |
| `show dhcp server settings` | device | `panos_show_dhcp` | (live device state — SSH via --remote) |
| `show dns-proxy cache all` | device | `panos_show_dns_proxy` | (live device state — SSH via --remote) |
| `show dns-proxy cache dump file` | device | `panos_show_dns_proxy` | (live device state — SSH via --remote) |
| `show dns-proxy cache filter fqdn` | device | `panos_show_dns_proxy` | (live device state — SSH via --remote) |
| `show dns-proxy cache mgmt-obj` | device | `panos_show_dns_proxy` | (live device state — SSH via --remote) |
| `show dns-proxy cache name` | device | `panos_show_dns_proxy` | (live device state — SSH via --remote) |
| `show dns-proxy ddns interface name` | device | `panos_show_dns_proxy` | (live device state — SSH via --remote) |
| `show dns-proxy dns-signature cache fqdn` | device | `panos_show_dns_proxy` | (live device state — SSH via --remote) |
| `show dns-proxy dns-signature content` | device | `panos_show_dns_proxy` | (live device state — SSH via --remote) |
| `show dns-proxy dns-signature counters` | device | `panos_show_dns_proxy` | (live device state — SSH via --remote) |
| `show dns-proxy dns-signature info` | device | `panos_show_dns_proxy` | (live device state — SSH via --remote) |
| `show dns-proxy encrypted-dns` | device | `panos_show_dns_proxy` | (live device state — SSH via --remote) |
| `show dns-proxy fqdn all` | device | `panos_show_dns_proxy` | (live device state — SSH via --remote) |
| `show dns-proxy fqdn mgmt-obj` | device | `panos_show_dns_proxy` | (live device state — SSH via --remote) |
| `show dns-proxy fqdn name` | device | `panos_show_dns_proxy` | (live device state — SSH via --remote) |
| `show dns-proxy settings all` | device | `panos_show_dns_proxy` | (live device state — SSH via --remote) |
| `show dns-proxy settings mgmt-obj` | device | `panos_show_dns_proxy` | (live device state — SSH via --remote) |
| `show dns-proxy settings name` | device | `panos_show_dns_proxy` | (live device state — SSH via --remote) |
| `show dns-proxy socket-count all` | device | `panos_show_dns_proxy` | (live device state — SSH via --remote) |
| `show dns-proxy static-entries all` | device | `panos_show_dns_proxy` | (live device state — SSH via --remote) |
| `show dns-proxy static-entries dump file` | device | `panos_show_dns_proxy` | (live device state — SSH via --remote) |
| `show dns-proxy static-entries filter fqdn` | device | `panos_show_dns_proxy` | (live device state — SSH via --remote) |
| `show dns-proxy static-entries name` | device | `panos_show_dns_proxy` | (live device state — SSH via --remote) |
| `show dns-proxy statistics all` | device | `panos_show_dns_proxy` | (live device state — SSH via --remote) |
| `show dns-proxy statistics mgmt-obj` | device | `panos_show_dns_proxy` | (live device state — SSH via --remote) |
| `show dns-proxy statistics name` | device | `panos_show_dns_proxy` | (live device state — SSH via --remote) |
| `show dos-block-table all start-at` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show dos-block-table hardware start-at` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show dos-block-table software start-at` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show dos-block-table summary` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show dos-protection rule` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show dos-protection zone` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show global-protect` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show global-protect-firewall summary firewall-client-version-last-activity-time` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show global-protect-gateway current-satellite gateway` | device | `panos_show_global_protect_gateway` | (live device state — SSH via --remote) |
| `show global-protect-gateway current-user gateway` | device | `panos_show_global_protect_gateway` | (live device state — SSH via --remote) |
| `show global-protect-gateway flow name` | device | `panos_show_global_protect_gateway` | (live device state — SSH via --remote) |
| `show global-protect-gateway flow tunnel-id` | device | `panos_show_global_protect_gateway` | (live device state — SSH via --remote) |
| `show global-protect-gateway flow-site-to-site name` | device | `panos_show_global_protect_gateway` | (live device state — SSH via --remote) |
| `show global-protect-gateway flow-site-to-site tunnel-id` | device | `panos_show_global_protect_gateway` | (live device state — SSH via --remote) |
| `show global-protect-gateway gateway name` | device | `panos_show_global_protect_gateway` | (live device state — SSH via --remote) |
| `show global-protect-gateway previous-satellite gateway` | device | `panos_show_global_protect_gateway` | (live device state — SSH via --remote) |
| `show global-protect-gateway previous-user gateway` | device | `panos_show_global_protect_gateway` | (live device state — SSH via --remote) |
| `show global-protect-gateway statistics gateway` | device | `panos_show_global_protect_gateway` | (live device state — SSH via --remote) |
| `show global-protect-gateway summary all` | device | `panos_show_global_protect_gateway` | (live device state — SSH via --remote) |
| `show global-protect-gateway summary detail name` | device | `panos_show_global_protect_gateway` | (live device state — SSH via --remote) |
| `show global-protect-mdm state` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show global-protect-mdm statistics` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show global-protect-portal cookie-cache portal` | device | `panos_show_global_protect_portal` | (live device state — SSH via --remote) |
| `show global-protect-portal current-user portal` | device | `panos_show_global_protect_portal` | (live device state — SSH via --remote) |
| `show global-protect-portal global-protect-portal portal` | device | `panos_show_global_protect_portal` | (live device state — SSH via --remote) |
| `show global-protect-portal satellite-cookie-expiration` | device | `panos_show_global_protect_portal` | (live device state — SSH via --remote) |
| `show global-protect-portal satellite-serialnumberip-auth status` | device | `panos_show_global_protect_portal` | (live device state — SSH via --remote) |
| `show global-protect-portal statistics portal` | device | `panos_show_global_protect_portal` | (live device state — SSH via --remote) |
| `show global-protect-portal summary all` | device | `panos_show_global_protect_portal` | (live device state — SSH via --remote) |
| `show global-protect-portal summary detail name` | device | `panos_show_global_protect_portal` | (live device state — SSH via --remote) |
| `show global-protect-satellite current-gateway satellite` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show global-protect-satellite interface` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show global-protect-satellite satellite name` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show gp-broker gpsvc counter` | device | `panos_show_gp_broker` | (live device state — SSH via --remote) |
| `show gp-broker gpsvc task all option` | device | `panos_show_gp_broker` | (live device state — SSH via --remote) |
| `show gp-broker gpsvc task src-ip` | device | `panos_show_gp_broker` | (live device state — SSH via --remote) |
| `show gp-broker gpsvc task task-index` | device | `panos_show_gp_broker` | (live device state — SSH via --remote) |
| `show gp-broker gpsvc task user` | device | `panos_show_gp_broker` | (live device state — SSH via --remote) |
| `show gp-broker gpsvc version` | device | `panos_show_gp_broker` | (live device state — SSH via --remote) |
| `show gp-broker ipc-stat` | device | `panos_show_gp_broker` | (live device state — SSH via --remote) |
| `show gp-broker panos-config` | device | `panos_show_gp_broker` | (live device state — SSH via --remote) |
| `show high-availability` | device | `panos_show_high_availability` | (live device state — SSH via --remote) |
| `show high-availability cluster` | device | `panos_show_high_availability` | (live device state — SSH via --remote) |
| `show high-availability cluster session-synchronization all` | device | `panos_show_high_availability` | (live device state — SSH via --remote) |
| `show high-availability cluster session-synchronization device device-id` | device | `panos_show_high_availability` | (live device state — SSH via --remote) |
| `show high-availability cluster session-synchronization device device-name` | device | `panos_show_high_availability` | (live device state — SSH via --remote) |
| `show high-availability cluster statistics all` | device | `panos_show_high_availability` | (live device state — SSH via --remote) |
| `show high-availability cluster statistics device device-id` | device | `panos_show_high_availability` | (live device state — SSH via --remote) |
| `show high-availability cluster statistics device device-name` | device | `panos_show_high_availability` | (live device state — SSH via --remote) |
| `show high-availability control-link statistics` | device | `panos_show_high_availability` | (live device state — SSH via --remote) |
| `show high-availability interface` | device | `panos_show_high_availability` | (live device state — SSH via --remote) |
| `show high-availability pre-negotiation summary` | device | `panos_show_high_availability` | (live device state — SSH via --remote) |
| `show hsm` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show iot device-inventory all match` | device | `panos_show_iot` | (live device state — SSH via --remote) |
| `show iot device-inventory all match ip` | device | `panos_show_iot` | (live device state — SSH via --remote) |
| `show iot device-inventory summmary` | device | `panos_show_iot` | (live device state — SSH via --remote) |
| `show iot dhcp-server status all` | device | `panos_show_iot` | (live device state — SSH via --remote) |
| `show iot dhcp-server status server` | device | `panos_show_iot` | (live device state — SSH via --remote) |
| `show iot dp-quarantine-cache all option` | device | `panos_show_iot` | (live device state — SSH via --remote) |
| `show iot dp-quarantine-cache ip` | device | `panos_show_iot` | (live device state — SSH via --remote) |
| `show iot eal` | device | `panos_show_iot` | (live device state — SSH via --remote) |
| `show iot eal dpi-stats all` | device | `panos_show_iot` | (live device state — SSH via --remote) |
| `show iot eal dpi-stats subtype` | device | `panos_show_iot` | (live device state — SSH via --remote) |
| `show iot edit-device-inventory id` | device | `panos_show_iot` | (live device state — SSH via --remote) |
| `show iot edit-device-inventory jobs` | device | `panos_show_iot` | (live device state — SSH via --remote) |
| `show iot export-device-inventory all match` | device | `panos_show_iot` | (live device state — SSH via --remote) |
| `show iot export-device-inventory all match ip` | device | `panos_show_iot` | (live device state — SSH via --remote) |
| `show iot host-cache all option` | device | `panos_show_iot` | (live device state — SSH via --remote) |
| `show iot host-cache hostid` | device | `panos_show_iot` | (live device state — SSH via --remote) |
| `show iot icd statistics` | device | `panos_show_iot` | (live device state — SSH via --remote) |
| `show iot icd version` | device | `panos_show_iot` | (live device state — SSH via --remote) |
| `show iot ip-device-mapping all option` | device | `panos_show_iot` | (live device state — SSH via --remote) |
| `show iot ip-device-mapping ip` | device | `panos_show_iot` | (live device state — SSH via --remote) |
| `show iot ip-device-mapping-mp all option` | device | `panos_show_iot` | (live device state — SSH via --remote) |
| `show iot ip-device-mapping-mp ip` | device | `panos_show_iot` | (live device state — SSH via --remote) |
| `show jobs pending` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show jobs processed` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show lacp aggregate-ethernet` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show ldl` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show license-token-files name` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show lldp` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show location ip` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show log` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log alarm` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log alarm csv-output equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log alarm direction equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log alarm dport equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log alarm opaque contains` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log alarm receive_time in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log alarm sport equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log appstat csv-output equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log appstat direction equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log appstat end-time equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log appstat name equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log appstat name not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log appstat query equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log appstat receive_time in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log appstat risk` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log appstat start-time equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log auth` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log auth clienttype equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log auth csv-output equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log auth direction equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log auth ip in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log auth ip not-in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log auth receive_time in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log config client equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log config client not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log config cmd equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log config cmd not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log config csv-output equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log config direction equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log config end-time equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log config query equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log config receive_time in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log config result equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log config result not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log config start-time equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log corr` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log corr csv-output equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log corr direction equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log corr receive_time in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log corr severity` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log corr src in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log corr src not-in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log corr-categ` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log corr-categ csv-output equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log corr-categ direction equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log corr-categ receive_time in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log corr-categ severity` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log corr-categ src in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log corr-categ src not-in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log corr-detail match-oid equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log corr-detail object-name equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log data` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log data action equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log data action not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log data csv-output equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log data direction equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log data dport equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log data dport not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log data dst in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log data dst not-in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log data receive_time in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log data sport equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log data sport not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log data src in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log data src not-in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log data suppress-threatid-mapping equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log decryption` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log decryption action equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log decryption action not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log decryption csv-output equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log decryption direction equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log decryption dport equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log decryption dport not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log decryption dst in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log decryption dst not-in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log decryption ec_curve equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log decryption proxy_type equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log decryption receive_time in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log decryption show-tracker equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log decryption sport equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log decryption sport not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log decryption src in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log decryption src not-in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log decryption tls_auth equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log decryption tls_enc equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log decryption tls_keyxchg equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log decryption tls_version equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log globalprotect` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log globalprotect csv-output equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log globalprotect direction equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log globalprotect machinename contains` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log globalprotect machinename equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log globalprotect machinename not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log globalprotect private_ip equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log globalprotect private_ip in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log globalprotect private_ip not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log globalprotect public_ip equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log globalprotect public_ip in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log globalprotect public_ip not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log globalprotect receive_time equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log globalprotect receive_time in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log globalprotect receive_time not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log hipmatch` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log hipmatch csv-output equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log hipmatch direction equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log hipmatch machinename equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log hipmatch machinename not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log hipmatch matchname equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log hipmatch matchname not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log hipmatch matchtype equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log hipmatch matchtype not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log hipmatch os equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log hipmatch os not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log hipmatch receive_time in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log hipmatch src in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log hipmatch src not-in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log iptag` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log iptag csv-output equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log iptag datasource_subtype equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log iptag datasource_subtype not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log iptag datasource_type equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log iptag datasource_type not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log iptag datasourcename equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log iptag datasourcename not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log iptag direction equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log iptag event_id equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log iptag event_id not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log iptag ip in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log iptag ip not-in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log iptag ip_subnet_range equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log iptag ip_subnet_range not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log iptag receive_time in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log iptag tag_name equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log iptag tag_name not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log mdm receive_time in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log system csv-output equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log system direction equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log system end-time equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log system opaque contains` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log system query equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log system receive_time in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log system severity` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log system start-time equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log threat` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log threat action equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log threat action not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log threat csv-output equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log threat direction equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log threat dport equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log threat dport not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log threat dst in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log threat dst not-in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log threat pcap-dump equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log threat receive_time in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log threat sport equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log threat sport not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log threat src in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log threat src not-in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log threat suppress-threatid-mapping equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log trace csv-output equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log trace direction equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log trace end-time equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log trace query equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log trace receive_time in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log trace sessionid equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log trace sessionid not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log trace start-time equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log traffic action equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log traffic action not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log traffic csv-output equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log traffic direction equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log traffic dport equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log traffic dport not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log traffic dst in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log traffic dst not-in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log traffic http2_connection equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log traffic http2_connection not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log traffic receive_time in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log traffic session-end-reason equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log traffic session-end-reason not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log traffic show-tracker equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log traffic sport equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log traffic sport not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log traffic src in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log traffic src not-in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log tunnel` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log tunnel action equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log tunnel action not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log tunnel csv-output equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log tunnel direction equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log tunnel dport equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log tunnel dport not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log tunnel dst in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log tunnel dst not-in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log tunnel receive_time in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log tunnel severity` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log tunnel sport equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log tunnel sport not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log tunnel src in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log tunnel src not-in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log url` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log url action equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log url action not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log url csv-output equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log url direction equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log url dport equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log url dport not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log url dst in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log url dst not-in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log url receive_time in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log url sport equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log url sport not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log url src in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log url src not-in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log url suppress-threatid-mapping equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log userid` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log userid beginport equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log userid beginport not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log userid csv-output equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log userid datasource equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log userid datasourcetype equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log userid direction equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log userid endport equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log userid endport not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log userid ip in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log userid ip not-in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log userid receive_time in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log wildfire` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log wildfire category equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log wildfire category not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log wildfire csv-output equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log wildfire direction equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log wildfire dport equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log wildfire dport not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log wildfire dst in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log wildfire dst not-in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log wildfire receive_time in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log wildfire sport equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log wildfire sport not-equal` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log wildfire src in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log wildfire src not-in` | device | `panos_show_log` | (live device state — SSH via --remote) |
| `show log-collector-group` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show logging-status verbose` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show logrcvr ip-cache vsys` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show logrcvr offline-logpurger` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show mac` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show macsec association interface` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show macsec stats interface` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show management-clients` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show management-server candidate config-size` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show management-server last-committed config-size` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show max-num-images` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show mgt-config devices` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show mlav` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show neighbor` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show net-inspection details` | device | `panos_show_net_inspection` | (live device state — SSH via --remote) |
| `show net-inspection evaluator index` | device | `panos_show_net_inspection` | (live device state — SSH via --remote) |
| `show net-inspection evaluator zone` | device | `panos_show_net_inspection` | (live device state — SSH via --remote) |
| `show net-inspection exempt` | device | `panos_show_net_inspection` | (live device state — SSH via --remote) |
| `show net-inspection filter index` | device | `panos_show_net_inspection` | (live device state — SSH via --remote) |
| `show net-inspection filter rule-name` | device | `panos_show_net_inspection` | (live device state — SSH via --remote) |
| `show net-inspection filter zone` | device | `panos_show_net_inspection` | (live device state — SSH via --remote) |
| `show net-inspection status` | device | `panos_show_net_inspection` | (live device state — SSH via --remote) |
| `show netstat route` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show ntp` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show object dynamic-address-group all` | device | `panos_show_object` | (live device state — SSH via --remote) |
| `show object dynamic-address-group name` | device | `panos_show_object` | (live device state — SSH via --remote) |
| `show object registered-ip limit` | device | `panos_show_object` | (live device state — SSH via --remote) |
| `show object registered-user all start-point` | device | `panos_show_object` | (live device state — SSH via --remote) |
| `show object registered-user user` | device | `panos_show_object` | (live device state — SSH via --remote) |
| `show object static ip` | device | `panos_show_object` | (live device state — SSH via --remote) |
| `show obsolete-disabled-ssl-exclusions` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show operational-mode` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show oss-license` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show panorama-certificates` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show panorama-status` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show parent-info all` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show parent-info filter saddr` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show parent-info info` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show pbf return-mac all` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show pbf return-mac name` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show pbf rule all detail` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show pbf rule name` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show policy-recommendation iot max-count` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show policy-recommendation saas max-count` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show pppoe inherited state interface` | device | `panos_show_pppoe` | (live device state — SSH via --remote) |
| `show pppoe interface` | device | `panos_show_pppoe` | (live device state — SSH via --remote) |
| `show pppoe ipv6 interface` | device | `panos_show_pppoe` | (live device state — SSH via --remote) |
| `show pppoe ipv6 pool-details` | device | `panos_show_pppoe` | (live device state — SSH via --remote) |
| `show pppoe ipv6 prefix interface` | device | `panos_show_pppoe` | (live device state — SSH via --remote) |
| `show predefined xpath` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show predefined-iot xpath` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show qos interface` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show query corr-detail id` | device | `panos_show_query` | (live device state — SSH via --remote) |
| `show query effective-queries query` | device | `panos_show_query` | (live device state — SSH via --remote) |
| `show query jobs` | device | `panos_show_query` | (live device state — SSH via --remote) |
| `show query result id` | device | `panos_show_query` | (live device state — SSH via --remote) |
| `show query stats` | device | `panos_show_query` | (live device state — SSH via --remote) |
| `show redistribution agent state` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show redistribution agent statistics` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show redistribution service client` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show redistribution service status` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show report cache cache_id` | device | `panos_show_report` | (live device state — SSH via --remote) |
| `show report cache info` | device | `panos_show_report` | (live device state — SSH via --remote) |
| `show report custom` | device | `panos_show_report` | (live device state — SSH via --remote) |
| `show report custom database equal` | device | `panos_show_report` | (live device state — SSH via --remote) |
| `show report custom receive_time in` | device | `panos_show_report` | (live device state — SSH via --remote) |
| `show report directory-listing` | device | `panos_show_report` | (live device state — SSH via --remote) |
| `show report exec_mgr batch_id` | device | `panos_show_report` | (live device state — SSH via --remote) |
| `show report exec_mgr info` | device | `panos_show_report` | (live device state — SSH via --remote) |
| `show report id` | device | `panos_show_report` | (live device state — SSH via --remote) |
| `show report jobs` | device | `panos_show_report` | (live device state — SSH via --remote) |
| `show report predefined end-time equal` | device | `panos_show_report` | (live device state — SSH via --remote) |
| `show report predefined name equal` | device | `panos_show_report` | (live device state — SSH via --remote) |
| `show report predefined start-time equal` | device | `panos_show_report` | (live device state — SSH via --remote) |
| `show resource limit` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show routing bfd active-profile name` | device | `panos_show_routing` | (live device state — SSH via --remote) |
| `show routing bfd details virtual-router` | device | `panos_show_routing` | (live device state — SSH via --remote) |
| `show routing bfd drop-counters session-id` | device | `panos_show_routing` | (live device state — SSH via --remote) |
| `show routing bfd summary virtual-router` | device | `panos_show_routing` | (live device state — SSH via --remote) |
| `show routing fib virtual-router` | device | `panos_show_routing` | (live device state — SSH via --remote) |
| `show routing interface` | device | `panos_show_routing` | (live device state — SSH via --remote) |
| `show routing multicast fib group` | device | `panos_show_routing` | (live device state — SSH via --remote) |
| `show routing multicast group-permission interface` | device | `panos_show_routing` | (live device state — SSH via --remote) |
| `show routing multicast igmp interface virtual-router` | device | `panos_show_routing` | (live device state — SSH via --remote) |
| `show routing multicast igmp membership interface` | device | `panos_show_routing` | (live device state — SSH via --remote) |
| `show routing multicast igmp statistics interface` | device | `panos_show_routing` | (live device state — SSH via --remote) |
| `show routing multicast pim elected-bsr` | device | `panos_show_routing` | (live device state — SSH via --remote) |
| `show routing multicast pim group-mapping group` | device | `panos_show_routing` | (live device state — SSH via --remote) |
| `show routing multicast pim interface virtual-router` | device | `panos_show_routing` | (live device state — SSH via --remote) |
| `show routing multicast pim neighbor virtual-router` | device | `panos_show_routing` | (live device state — SSH via --remote) |
| `show routing multicast pim state virtual-router` | device | `panos_show_routing` | (live device state — SSH via --remote) |
| `show routing multicast pim statistics interface` | device | `panos_show_routing` | (live device state — SSH via --remote) |
| `show routing multicast route group` | device | `panos_show_routing` | (live device state — SSH via --remote) |
| `show routing path-monitor virtual-router` | device | `panos_show_routing` | (live device state — SSH via --remote) |
| `show routing protocol bgp` | device | `panos_show_routing` | (live device state — SSH via --remote) |
| `show routing protocol bgp peer peer-name` | device | `panos_show_routing` | (live device state — SSH via --remote) |
| `show routing protocol bgp peer-group group-name` | device | `panos_show_routing` | (live device state — SSH via --remote) |
| `show routing protocol bgp policy virtual-router` | device | `panos_show_routing` | (live device state — SSH via --remote) |
| `show routing protocol bgp summary virtual-router` | device | `panos_show_routing` | (live device state — SSH via --remote) |
| `show routing protocol ospf` | device | `panos_show_routing` | (live device state — SSH via --remote) |
| `show routing protocol ospfv3` | device | `panos_show_routing` | (live device state — SSH via --remote) |
| `show routing protocol ospfv3 dumplsdb scope` | device | `panos_show_routing` | (live device state — SSH via --remote) |
| `show routing protocol ospfv3 interface brief` | device | `panos_show_routing` | (live device state — SSH via --remote) |
| `show routing protocol ospfv3 lsdb scope` | device | `panos_show_routing` | (live device state — SSH via --remote) |
| `show routing protocol ospfv3 neighbor brief` | device | `panos_show_routing` | (live device state — SSH via --remote) |
| `show routing protocol ospfv3 virt-neighbor brief` | device | `panos_show_routing` | (live device state — SSH via --remote) |
| `show routing protocol redist` | device | `panos_show_routing` | (live device state — SSH via --remote) |
| `show routing protocol rip` | device | `panos_show_routing` | (live device state — SSH via --remote) |
| `show routing resource` | device | `panos_show_routing` | (live device state — SSH via --remote) |
| `show routing route destination` | device | `panos_show_routing` | (live device state — SSH via --remote) |
| `show routing summary virtual-router` | device | `panos_show_routing` | (live device state — SSH via --remote) |
| `show rule-hit-count vsys` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show rule-hit-count vsys all rule-base` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show rule-hit-count vsys list entry` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show rule-hit-count vsys list rule-base` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show running` | device | `panos_show_running` | (live device state — SSH via --remote) |
| `show running appinfo2ip saddr` | device | `panos_show_running` | (live device state — SSH via --remote) |
| `show running application cache all` | device | `panos_show_running` | (live device state — SSH via --remote) |
| `show running application disabled` | device | `panos_show_running` | (live device state — SSH via --remote) |
| `show running application setting` | device | `panos_show_running` | (live device state — SSH via --remote) |
| `show running application statistics` | device | `panos_show_running` | (live device state — SSH via --remote) |
| `show running application-signature statistics` | device | `panos_show_running` | (live device state — SSH via --remote) |
| `show running dns-cache statistics` | device | `panos_show_running` | (live device state — SSH via --remote) |
| `show running global-ippool summary-only` | device | `panos_show_running` | (live device state — SSH via --remote) |
| `show running ipv6 address` | device | `panos_show_running` | (live device state — SSH via --remote) |
| `show running ml-block-cache top` | device | `panos_show_running` | (live device state — SSH via --remote) |
| `show running ml-block-cache url` | device | `panos_show_running` | (live device state — SSH via --remote) |
| `show running mlav-model status` | device | `panos_show_running` | (live device state — SSH via --remote) |
| `show running nat-policy vsys` | device | `panos_show_running` | (live device state — SSH via --remote) |
| `show running nat-rule-ippool rule` | device | `panos_show_running` | (live device state — SSH via --remote) |
| `show running ndp-proxy interface` | device | `panos_show_running` | (live device state — SSH via --remote) |
| `show running network-packet-broker` | device | `panos_show_running` | (live device state — SSH via --remote) |
| `show running persistent-dipp-client ip-utilization pool` | device | `panos_show_running` | (live device state — SSH via --remote) |
| `show running persistent-dipp-client pool` | device | `panos_show_running` | (live device state — SSH via --remote) |
| `show running persistent-dipp-client-translation ip` | device | `panos_show_running` | (live device state — SSH via --remote) |
| `show running persistent-dipp-pool ip-utilization` | device | `panos_show_running` | (live device state — SSH via --remote) |
| `show running resource-monitor day last` | device | `panos_show_running` | (live device state — SSH via --remote) |
| `show running resource-monitor hour last` | device | `panos_show_running` | (live device state — SSH via --remote) |
| `show running resource-monitor ingress-backlogs` | device | `panos_show_running` | (live device state — SSH via --remote) |
| `show running resource-monitor minute last` | device | `panos_show_running` | (live device state — SSH via --remote) |
| `show running resource-monitor second last` | device | `panos_show_running` | (live device state — SSH via --remote) |
| `show running resource-monitor week last` | device | `panos_show_running` | (live device state — SSH via --remote) |
| `show running rule-use highlight vsys` | device | `panos_show_running` | (live device state — SSH via --remote) |
| `show running rule-use hit-count vsys` | device | `panos_show_running` | (live device state — SSH via --remote) |
| `show running security-policy rule-index` | device | `panos_show_running` | (live device state — SSH via --remote) |
| `show running tcp state` | device | `panos_show_running` | (live device state — SSH via --remote) |
| `show running tunnel flow` | device | `panos_show_running` | (live device state — SSH via --remote) |
| `show running tunnel flow all filter type` | device | `panos_show_running` | (live device state — SSH via --remote) |
| `show running tunnel flow context` | device | `panos_show_running` | (live device state — SSH via --remote) |
| `show running tunnel flow name` | device | `panos_show_running` | (live device state — SSH via --remote) |
| `show running tunnel flow tunnel-id` | device | `panos_show_running` | (live device state — SSH via --remote) |
| `show running url` | device | `panos_show_running` | (live device state — SSH via --remote) |
| `show running url-cache` | device | `panos_show_running` | (live device state — SSH via --remote) |
| `show running url-info` | device | `panos_show_running` | (live device state — SSH via --remote) |
| `show sdwan connection` | device | `panos_show_sdwan` | (live device state — SSH via --remote) |
| `show sdwan details` | device | `panos_show_sdwan` | (live device state — SSH via --remote) |
| `show sdwan details basic` | device | `panos_show_sdwan` | (live device state — SSH via --remote) |
| `show sdwan details rule id` | device | `panos_show_sdwan` | (live device state — SSH via --remote) |
| `show sdwan details rule idx` | device | `panos_show_sdwan` | (live device state — SSH via --remote) |
| `show sdwan details session id` | device | `panos_show_sdwan` | (live device state — SSH via --remote) |
| `show sdwan event` | device | `panos_show_sdwan` | (live device state — SSH via --remote) |
| `show sdwan path-monitor details` | device | `panos_show_sdwan` | (live device state — SSH via --remote) |
| `show sdwan path-monitor dia-anypath packet-buffer` | device | `panos_show_sdwan` | (live device state — SSH via --remote) |
| `show sdwan path-monitor parameter active` | device | `panos_show_sdwan` | (live device state — SSH via --remote) |
| `show sdwan path-monitor parameter adaptive` | device | `panos_show_sdwan` | (live device state — SSH via --remote) |
| `show sdwan path-monitor parameter all-dp` | device | `panos_show_sdwan` | (live device state — SSH via --remote) |
| `show sdwan path-monitor parameter conn-idx` | device | `panos_show_sdwan` | (live device state — SSH via --remote) |
| `show sdwan path-monitor parameter path-name` | device | `panos_show_sdwan` | (live device state — SSH via --remote) |
| `show sdwan path-monitor parameter vif` | device | `panos_show_sdwan` | (live device state — SSH via --remote) |
| `show sdwan path-monitor policy-map` | device | `panos_show_sdwan` | (live device state — SSH via --remote) |
| `show sdwan path-monitor stats active` | device | `panos_show_sdwan` | (live device state — SSH via --remote) |
| `show sdwan path-monitor stats adaptive` | device | `panos_show_sdwan` | (live device state — SSH via --remote) |
| `show sdwan path-monitor stats all-dp` | device | `panos_show_sdwan` | (live device state — SSH via --remote) |
| `show sdwan path-monitor stats conn-idx` | device | `panos_show_sdwan` | (live device state — SSH via --remote) |
| `show sdwan path-monitor stats dia-vif` | device | `panos_show_sdwan` | (live device state — SSH via --remote) |
| `show sdwan path-monitor stats path-name` | device | `panos_show_sdwan` | (live device state — SSH via --remote) |
| `show sdwan path-monitor stats vif` | device | `panos_show_sdwan` | (live device state — SSH via --remote) |
| `show sdwan pool details` | device | `panos_show_sdwan` | (live device state — SSH via --remote) |
| `show sdwan rule vif` | device | `panos_show_sdwan` | (live device state — SSH via --remote) |
| `show sdwan session distribution policy-name` | device | `panos_show_sdwan` | (live device state — SSH via --remote) |
| `show sdwan session log session-id` | device | `panos_show_sdwan` | (live device state — SSH via --remote) |
| `show sdwan session path-select session-id` | device | `panos_show_sdwan` | (live device state — SSH via --remote) |
| `show session` | device | `panos_show_session` | (live device state — SSH via --remote) |
| `show session all start-at` | device | `panos_show_session` | (live device state — SSH via --remote) |
| `show session cache all filter from` | device | `panos_show_session` | (live device state — SSH via --remote) |
| `show session cache external md5` | device | `panos_show_session` | (live device state — SSH via --remote) |
| `show session cache md5` | device | `panos_show_session` | (live device state — SSH via --remote) |
| `show session id` | device | `panos_show_session` | (live device state — SSH via --remote) |
| `show session packet-buffer-protection` | device | `panos_show_session` | (live device state — SSH via --remote) |
| `show shared address-group` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared application` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared application-filter` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared external-list` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared post-rulebase` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared post-rulebase application-override rules` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared post-rulebase authentication rules` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared post-rulebase decryption rules` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared post-rulebase default-security-rules rules` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared post-rulebase dos rules` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared post-rulebase nat rules` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared post-rulebase network-packet-broker rules` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared post-rulebase pbf rules` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared post-rulebase qos rules` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared post-rulebase sdwan rules` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared post-rulebase security rules` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared post-rulebase tunnel-inspect rules` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared pre-rulebase` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared pre-rulebase application-override rules` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared pre-rulebase authentication rules` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared pre-rulebase decryption rules` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared pre-rulebase dos rules` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared pre-rulebase nat rules` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared pre-rulebase network-packet-broker rules` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared pre-rulebase pbf rules` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared pre-rulebase qos rules` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared pre-rulebase sdwan rules` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared pre-rulebase security rules` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared pre-rulebase tunnel-inspect rules` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared profiles` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared profiles ai-security` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared profiles data-filtering` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared profiles data-objects` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared profiles decryption` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared profiles dos-protection` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared profiles file-blocking` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared profiles gtp` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared profiles hip-objects` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared profiles host-compliance-objects` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared profiles sctp` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared profiles sdwan-error-correction` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared profiles sdwan-path-quality` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared profiles sdwan-saas-quality` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared profiles sdwan-traffic-distribution` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared profiles spyware` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared profiles url-filtering` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared profiles virus` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared profiles vulnerability` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared profiles wildfire-analysis` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared region` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared schedule` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared service` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared threats` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared threats spyware` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show shared threats vulnerability` | device | `panos_show_shared` | (live device state — SSH via --remote) |
| `show snmpd refresh-timer-period` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show sp-metadata captive-portal authprofile` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show sp-metadata global-protect authprofile` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show sp-metadata management authprofile` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show ssh-fingerprints hash-type` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show ssl-conn-on-cert` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show sslmgr-max-check-cert-jobs` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show sslmgr-store certificate-info issuer` | device | `panos_show_sslmgr_store` | (live device state — SSH via --remote) |
| `show sslmgr-store certificate-info portal name` | device | `panos_show_sslmgr_store` | (live device state — SSH via --remote) |
| `show sslmgr-store config-ca-certificate subjectname-hash` | device | `panos_show_sslmgr_store` | (live device state — SSH via --remote) |
| `show sslmgr-store config-certificate-info db-serialno` | device | `panos_show_sslmgr_store` | (live device state — SSH via --remote) |
| `show sslmgr-store satellite-info portal name` | device | `panos_show_sslmgr_store` | (live device state — SSH via --remote) |
| `show sslmgr-store serialno-certificate-info db-serialno` | device | `panos_show_sslmgr_store` | (live device state — SSH via --remote) |
| `show statistics` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show streaming-telemetry region-list` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show syslog-ssl-conn-validation` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show system` | device | `panos_show_system` | (live device state — SSH via --remote) |
| `show system crypto entropy-status` | device | `panos_show_system` | (live device state — SSH via --remote) |
| `show system disk-space files` | device | `panos_show_system` | (live device state — SSH via --remote) |
| `show system environmentals fans slot` | device | `panos_show_system` | (live device state — SSH via --remote) |
| `show system environmentals power slot` | device | `panos_show_system` | (live device state — SSH via --remote) |
| `show system environmentals slot` | device | `panos_show_system` | (live device state — SSH via --remote) |
| `show system environmentals thermal slot` | device | `panos_show_system` | (live device state — SSH via --remote) |
| `show system resources follow` | device | `panos_show_system` | (live device state — SSH via --remote) |
| `show system setting` | device | `panos_show_system` | (live device state — SSH via --remote) |
| `show system setting ctd` | device | `panos_show_system` | (live device state — SSH via --remote) |
| `show system setting ctd threat id` | device | `panos_show_system` | (live device state — SSH via --remote) |
| `show system setting logging log-compression` | device | `panos_show_system` | (live device state — SSH via --remote) |
| `show system setting ssl-decrypt` | device | `panos_show_system` | (live device state — SSH via --remote) |
| `show system setting ssl-decrypt exclude-cache xml yes` | device | `panos_show_system` | (live device state — SSH via --remote) |
| `show system setting ssl-decrypt gp-cookie-cache user` | device | `panos_show_system` | (live device state — SSH via --remote) |
| `show system setting ssl-decrypt memory detail` | device | `panos_show_system` | (live device state — SSH via --remote) |
| `show system setting url-cache` | device | `panos_show_system` | (live device state — SSH via --remote) |
| `show system state browser` | device | `panos_show_system` | (live device state — SSH via --remote) |
| `show system state filter` | device | `panos_show_system` | (live device state — SSH via --remote) |
| `show system state filter-pretty` | device | `panos_show_system` | (live device state — SSH via --remote) |
| `show system statistics` | device | `panos_show_system` | (live device state — SSH via --remote) |
| `show threat id` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show transceiver` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show transceiver-detail` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show transceiver-eeprom` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show transceiver-monitor-rate` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show tunnel-acceleration` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show upgrade-history` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show url-cloud status` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show user cloud-identity-engine client statistics` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user cloud-identity-engine statistics all` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user cloud-identity-engine statistics name` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user cloud-identity-engine status all` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user cloud-identity-engine status name` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user cookie-surrogate-cache-dp all` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user cookie-surrogate-cache-dp username` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user credential-filter` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user email-lookup email` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user group name` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user group-mapping naming-context server` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user group-mapping state` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user group-mapping statistics` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user group-mapping-service query` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user group-mapping-service status` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user group-policy-dp` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user group-policy-dp gid` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user group-selection sp_vsys_id` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user hip-report user` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user ip-port-user-mapping all` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user ip-port-user-mapping ip` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user ip-port-user-mapping source-user` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user ip-port-user-mapping-mp all` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user ip-port-user-mapping-mp ip` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user ip-port-user-mapping-mp source-user` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user ip-user-mapping all option` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user ip-user-mapping ip` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user ip-user-mapping-mp limit` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user ldap-device-serialno all` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user ldap-device-serialno serialno` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user local-user-db vsys` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user server-monitor auto-discover domain` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user server-monitor state` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user server-monitor statistics` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user ts-agent state` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user ts-agent statistics` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user uid2primeuid-dp all` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user uid2primeuid-dp uid` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user user-attributes user` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user user-cache-dp all` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user user-cache-dp uid` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user user-id-agent config all` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user user-id-agent config name` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user user-id-agent state` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user user-id-agent statistics` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user user-id-service client` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user user-id-service ipuser-update-list option` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user user-id-service status` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user user-ids all option` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user user-ids match-user` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user user-policy-dp all` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user user-policy-dp uid` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show user xml-api multiusersystem` | device | `panos_show_user` | (live device state — SSH via --remote) |
| `show virtual-wire` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show vlan` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show vm-monitor source all` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show vm-monitor source state` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show vm-monitor source statistics` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show vpn flow name` | device | `panos_show_vpn` | (live device state — SSH via --remote) |
| `show vpn flow tunnel-id` | device | `panos_show_vpn` | (live device state — SSH via --remote) |
| `show vpn gateway match` | device | `panos_show_vpn` | (live device state — SSH via --remote) |
| `show vpn gateway name` | device | `panos_show_vpn` | (live device state — SSH via --remote) |
| `show vpn ike-hashurl` | device | `panos_show_vpn` | (live device state — SSH via --remote) |
| `show vpn ike-sa detail gateway` | device | `panos_show_vpn` | (live device state — SSH via --remote) |
| `show vpn ike-sa gateway` | device | `panos_show_vpn` | (live device state — SSH via --remote) |
| `show vpn ike-sa match` | device | `panos_show_vpn` | (live device state — SSH via --remote) |
| `show vpn ipsec-sa match` | device | `panos_show_vpn` | (live device state — SSH via --remote) |
| `show vpn ipsec-sa summary` | device | `panos_show_vpn` | (live device state — SSH via --remote) |
| `show vpn ipsec-sa tunnel` | device | `panos_show_vpn` | (live device state — SSH via --remote) |
| `show vpn tunnel match` | device | `panos_show_vpn` | (live device state — SSH via --remote) |
| `show vpn tunnel name` | device | `panos_show_vpn` | (live device state — SSH via --remote) |
| `show wildfire` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show wildfire-appliance-cluster` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show wildfire-realtime-cache total` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show wildfire-realtime-cache virus-pattern-type` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show wildfire-realtime-cloud-status` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show wildfire-realtime-stats` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `show zone-protection zone` | device | `panos_show_misc` | (live device state — SSH via --remote) |
| `ssh inet` | device | `panos_ssh` | (live device state — SSH via --remote) |
| `tail follow` | device | `panos_tail` | (live device state — SSH via --remote) |
| `target set` | device | `panos_target` | (live device state — SSH via --remote) |
| `target show` | device | `panos_target` | (live device state — SSH via --remote) |
| `test advanced-routing bgp logical-router` | device | `panos_test` | (live device state — SSH via --remote) |
| `test advanced-routing fib-lookup ip` | device | `panos_test` | (live device state — SSH via --remote) |
| `test advanced-routing mfib-lookup group` | device | `panos_test` | (live device state — SSH via --remote) |
| `test advanced-routing multicast msdp logical-router` | device | `panos_test` | (live device state — SSH via --remote) |
| `test arp gratuitous interface` | device | `panos_test` | (live device state — SSH via --remote) |
| `test authentication authentication-profile` | device | `panos_test` | (live device state — SSH via --remote) |
| `test authentication-policy-match from` | device | `panos_test` | (live device state — SSH via --remote) |
| `test botnet domain` | device | `panos_test` | (live device state — SSH via --remote) |
| `test cookie-surrogate username` | device | `panos_test` | (live device state — SSH via --remote) |
| `test custom-signature-perf pattern` | device | `panos_test` | (live device state — SSH via --remote) |
| `test custom-signature-type pattern` | device | `panos_test` | (live device state — SSH via --remote) |
| `test custom-url url` | device | `panos_test` | (live device state — SSH via --remote) |
| `test data-filtering ccn` | device | `panos_test` | (live device state — SSH via --remote) |
| `test data-filtering pattern` | device | `panos_test` | (live device state — SSH via --remote) |
| `test data-filtering ssn` | device | `panos_test` | (live device state — SSH via --remote) |
| `test decryption-policy-match from` | device | `panos_test` | (live device state — SSH via --remote) |
| `test dns-proxy ddns update interface name` | device | `panos_test` | (live device state — SSH via --remote) |
| `test dns-proxy dns-signature fqdn` | device | `panos_test` | (live device state — SSH via --remote) |
| `test dns-proxy fqdn refresh all` | device | `panos_test` | (live device state — SSH via --remote) |
| `test dns-proxy fqdn refresh entry fqdn` | device | `panos_test` | (live device state — SSH via --remote) |
| `test dns-proxy query name` | device | `panos_test` | (live device state — SSH via --remote) |
| `test dos-policy-match from` | device | `panos_test` | (live device state — SSH via --remote) |
| `test generate-saml-url captive-portal vsys` | device | `panos_test` | (live device state — SSH via --remote) |
| `test generate-saml-url global-protect vsys` | device | `panos_test` | (live device state — SSH via --remote) |
| `test generate-saml-url management interface` | device | `panos_test` | (live device state — SSH via --remote) |
| `test global-protect-mdm hipreport request mobile-id` | device | `panos_test` | (live device state — SSH via --remote) |
| `test global-protect-satellite gateway-connect satellite` | device | `panos_test` | (live device state — SSH via --remote) |
| `test global-protect-satellite gateway-disconnect satellite` | device | `panos_test` | (live device state — SSH via --remote) |
| `test global-protect-satellite gateway-reconnect satellite` | device | `panos_test` | (live device state — SSH via --remote) |
| `test http-profile vsys` | device | `panos_test` | (live device state — SSH via --remote) |
| `test http-profile-server-auth-token vsys` | device | `panos_test` | (live device state — SSH via --remote) |
| `test http-server vsys` | device | `panos_test` | (live device state — SSH via --remote) |
| `test macsec association interface` | device | `panos_test` | (live device state — SSH via --remote) |
| `test mfa-vendors mfa-server-profile` | device | `panos_test` | (live device state — SSH via --remote) |
| `test nat-policy-match from` | device | `panos_test` | (live device state — SSH via --remote) |
| `test nd router-advertisement interface` | device | `panos_test` | (live device state — SSH via --remote) |
| `test nptv6 cks-neutral dest-network` | device | `panos_test` | (live device state — SSH via --remote) |
| `test pbf-policy-match from` | device | `panos_test` | (live device state — SSH via --remote) |
| `test pppoe interface` | device | `panos_test` | (live device state — SSH via --remote) |
| `test pppoe ipv6 interface` | device | `panos_test` | (live device state — SSH via --remote) |
| `test qos-policy-match from` | device | `panos_test` | (live device state — SSH via --remote) |
| `test routing bgp virtual-router` | device | `panos_test` | (live device state — SSH via --remote) |
| `test routing fib-lookup ip` | device | `panos_test` | (live device state — SSH via --remote) |
| `test routing mfib-lookup group` | device | `panos_test` | (live device state — SSH via --remote) |
| `test routing ospf logical-router` | device | `panos_test` | (live device state — SSH via --remote) |
| `test routing ospfv3 logical-router` | device | `panos_test` | (live device state — SSH via --remote) |
| `test scp-server-connection confirm hostname` | device | `panos_test` | (live device state — SSH via --remote) |
| `test scp-server-connection initiate hostname` | device | `panos_test` | (live device state — SSH via --remote) |
| `test security-policy-match from` | device | `panos_test` | (live device state — SSH via --remote) |
| `test smtp-server vsys` | device | `panos_test` | (live device state — SSH via --remote) |
| `test ssl-exclude-list predefined hostname` | device | `panos_test` | (live device state — SSH via --remote) |
| `test ssl-exclude-list shared hostname` | device | `panos_test` | (live device state — SSH via --remote) |
| `test ssl-exclude-list vsys hostname` | device | `panos_test` | (live device state — SSH via --remote) |
| `test stats-service` | device | `panos_test` | (live device state — SSH via --remote) |
| `test tag-filter` | device | `panos_test` | (live device state — SSH via --remote) |
| `test threat-vault connection` | device | `panos_test` | (live device state — SSH via --remote) |
| `test uid` | device | `panos_test` | (live device state — SSH via --remote) |
| `test url-info-cloud` | device | `panos_test` | (live device state — SSH via --remote) |
| `test url-info-host` | device | `panos_test` | (live device state — SSH via --remote) |
| `test url-wpc` | device | `panos_test` | (live device state — SSH via --remote) |
| `test user-id custom-group group-mapping` | device | `panos_test` | (live device state — SSH via --remote) |
| `test user-id user-id-syslog-parse field-identifier event-string` | device | `panos_test` | (live device state — SSH via --remote) |
| `test user-id user-id-syslog-parse regex-identifier event-regex` | device | `panos_test` | (live device state — SSH via --remote) |
| `test uuid enable` | device | `panos_test` | (live device state — SSH via --remote) |
| `test vpn ike-sa gateway` | device | `panos_test` | (live device state — SSH via --remote) |
| `test vpn ipsec-sa tunnel` | device | `panos_test` | (live device state — SSH via --remote) |
| `test wildfire registration channel` | device | `panos_test` | (live device state — SSH via --remote) |
| `test x-authenticated-user ip` | device | `panos_test` | (live device state — SSH via --remote) |
| `tftp export` | device | `panos_tftp` | (live device state — SSH via --remote) |
| `tftp export core-file data-plane from` | device | `panos_tftp` | (live device state — SSH via --remote) |
| `tftp export core-file large-corefile from` | device | `panos_tftp` | (live device state — SSH via --remote) |
| `tftp export core-file management-plane from` | device | `panos_tftp` | (live device state — SSH via --remote) |
| `tftp export debug bootmem_file from` | device | `panos_tftp` | (live device state — SSH via --remote) |
| `tftp export log-file data-plane to` | device | `panos_tftp` | (live device state — SSH via --remote) |
| `tftp export log-file management-plane to` | device | `panos_tftp` | (live device state — SSH via --remote) |
| `tftp export stats-dump to` | device | `panos_tftp` | (live device state — SSH via --remote) |
| `tftp export threat-pcap pcap-id` | device | `panos_tftp` | (live device state — SSH via --remote) |
| `tftp import` | device | `panos_tftp` | (live device state — SSH via --remote) |
| `tftp import certificate from` | device | `panos_tftp` | (live device state — SSH via --remote) |
| `tftp import keypair from` | device | `panos_tftp` | (live device state — SSH via --remote) |
| `tftp import private-key from` | device | `panos_tftp` | (live device state — SSH via --remote) |
| `traceroute ipv4` | device | `panos_traceroute` | (live device state — SSH via --remote) |

## Posture

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `delete posture root` | global | `posture_root_write` | DELETE https://api.strata.paloaltonetworks.com/posture/checks/v1/{id} |
| `set posture batch-delete` | global | `posture_batch_delete_write` | POST https://api.strata.paloaltonetworks.com/posture/checks/v1/batch-delete |
| `set posture batch-upsert` | global | `posture_batch_upsert_write` | POST https://api.strata.paloaltonetworks.com/posture/checks/v1/batch-upsert |
| `set posture clone` | global | `posture_clone_write` | POST https://api.strata.paloaltonetworks.com/posture/checks/v1/{id}:clone |
| `set posture reports config-file-upload` | global | `posture_reports_config_file_upload_write` | POST https://api.strata.paloaltonetworks.com/posture/checks/v1/reports/config-file-upload |
| `set posture root` | global | `posture_root_write` | POST https://api.strata.paloaltonetworks.com/posture/checks/v1 |
| `show posture id` | global | `posture_read` | GET https://api.strata.paloaltonetworks.com/posture/checks/v1/{id} |
| `show posture reports bpa-result id` | global | `posture_reports_bpa_result_read` | GET https://api.strata.paloaltonetworks.com/posture/checks/v1/reports/{id}/bpa-result |
| `show posture root` | global | `posture_root_read` | GET https://api.strata.paloaltonetworks.com/posture/checks/v1 |
| `update posture root` | global | `posture_root_write` | PUT https://api.strata.paloaltonetworks.com/posture/checks/v1/{id} |

## Sase

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `delete sase agent-profiles` | global | `sase_agent_profiles_write` | DELETE https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/agent-profiles |
| `delete sase authentication-settings` | global | `sase_authentication_settings_write` | DELETE https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/authentication-settings |
| `delete sase bandwidth-allocations` | global | `sase_bandwidth_allocations_write` | DELETE https://api.strata.paloaltonetworks.com/config/deployment/v1/bandwidth-allocations |
| `delete sase forwarding-profiles` | global | `sase_forwarding_profiles_write` | DELETE https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profiles/{id} |
| `delete sase fp-custom-proxies` | global | `sase_fp_custom_proxies_write` | DELETE https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profile-regional-and-custom-proxies/{id} |
| `delete sase fp-destinations` | global | `sase_fp_destinations_write` | DELETE https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profile-destinations/{id} |
| `delete sase fp-source-apps` | global | `sase_fp_source_apps_write` | DELETE https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profile-source-applications/{id} |
| `delete sase fp-user-locations` | global | `sase_fp_user_locations_write` | DELETE https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profile-user-locations/{id} |
| `delete sase infrastructure-settings` | global | `sase_infrastructure_settings_write` | DELETE https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/infrastructure-settings |
| `delete sase internal-dns-servers` | global | `sase_internal_dns_servers_write` | DELETE https://api.strata.paloaltonetworks.com/config/deployment/v1/internal-dns-servers/{id} |
| `delete sase remote-networks` | global | `sase_remote_networks_write` | DELETE https://api.strata.paloaltonetworks.com/config/deployment/v1/remote-networks/{id} |
| `delete sase service-connection-groups` | global | `sase_service_connection_groups_write` | DELETE https://api.strata.paloaltonetworks.com/config/deployment/v1/service-connection-groups/{id} |
| `delete sase service-connections` | global | `sase_service_connections_write` | DELETE https://api.strata.paloaltonetworks.com/config/deployment/v1/service-connections/{id} |
| `delete sase sites` | global | `sase_sites_write` | DELETE https://api.strata.paloaltonetworks.com/config/deployment/v1/sites/{id} |
| `delete sase traffic-steering-rules` | global | `sase_traffic_steering_rules_write` | DELETE https://api.strata.paloaltonetworks.com/config/deployment/v1/traffic-steering-rules/{id} |
| `delete sase tunnel-profiles` | global | `sase_tunnel_profiles_write` | DELETE https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/tunnel-profiles |
| `set sase agent-profiles` | global | `sase_agent_profiles_write` | POST https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/agent-profiles |
| `set sase authentication-settings` | global | `sase_authentication_settings_write` | POST https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/authentication-settings |
| `set sase authentication-settings move` | global | `sase_authentication_settings_move_write` | POST https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/authentication-settings/{name}:move |
| `set sase bandwidth-allocations` | global | `sase_bandwidth_allocations_write` | POST https://api.strata.paloaltonetworks.com/config/deployment/v1/bandwidth-allocations |
| `set sase enable` | global | `sase_enable_write` | POST https://api.strata.paloaltonetworks.com/config/deployment/v1/enable |
| `set sase forwarding-profiles` | global | `sase_forwarding_profiles_write` | POST https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profiles |
| `set sase fp-custom-proxies` | global | `sase_fp_custom_proxies_write` | POST https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profile-regional-and-custom-proxies |
| `set sase fp-destinations` | global | `sase_fp_destinations_write` | POST https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profile-destinations |
| `set sase fp-source-apps` | global | `sase_fp_source_apps_write` | POST https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profile-source-applications |
| `set sase fp-user-locations` | global | `sase_fp_user_locations_write` | POST https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profile-user-locations |
| `set sase infrastructure-settings` | global | `sase_infrastructure_settings_write` | POST https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/infrastructure-settings |
| `set sase internal-dns-servers` | global | `sase_internal_dns_servers_write` | POST https://api.strata.paloaltonetworks.com/config/deployment/v1/internal-dns-servers |
| `set sase mobileagent enable` | global | `sase_enable_write` | POST https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/enable |
| `set sase remote-networks` | global | `sase_remote_networks_write` | POST https://api.strata.paloaltonetworks.com/config/deployment/v1/remote-networks |
| `set sase service-connection-groups` | global | `sase_service_connection_groups_write` | POST https://api.strata.paloaltonetworks.com/config/deployment/v1/service-connection-groups |
| `set sase service-connections` | global | `sase_service_connections_write` | POST https://api.strata.paloaltonetworks.com/config/deployment/v1/service-connections |
| `set sase sites` | global | `sase_sites_write` | POST https://api.strata.paloaltonetworks.com/config/deployment/v1/sites |
| `set sase traffic-steering-rules` | global | `sase_traffic_steering_rules_write` | POST https://api.strata.paloaltonetworks.com/config/deployment/v1/traffic-steering-rules |
| `set sase tunnel-profiles` | global | `sase_tunnel_profiles_write` | POST https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/tunnel-profiles |
| `show sase agent-profiles` | global | `sase_agent_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/agent-profiles |
| `show sase agent-versions` | global | `sase_agent_versions_read` | GET https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/agent-versions |
| `show sase authentication-settings` | global | `sase_authentication_settings_read` | GET https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/authentication-settings |
| `show sase bandwidth-allocations` | global | `sase_bandwidth_allocations_read` | GET https://api.strata.paloaltonetworks.com/config/deployment/v1/bandwidth-allocations |
| `show sase bgp-routing` | global | `sase_bgp_routing_read` | GET https://api.strata.paloaltonetworks.com/config/deployment/v1/bgp-routing |
| `show sase enable` | global | `sase_enable_read` | GET https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/enable |
| `show sase forwarding-profiles` | global | `sase_forwarding_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profiles |
| `show sase forwarding-profiles id` | global | `sase_forwarding_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profiles/{id} |
| `show sase fp-custom-proxies` | global | `sase_fp_custom_proxies_read` | GET https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profile-regional-and-custom-proxies |
| `show sase fp-custom-proxies id` | global | `sase_fp_custom_proxies_read` | GET https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profile-regional-and-custom-proxies/{id} |
| `show sase fp-destinations` | global | `sase_fp_destinations_read` | GET https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profile-destinations |
| `show sase fp-destinations id` | global | `sase_fp_destinations_read` | GET https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profile-destinations/{id} |
| `show sase fp-source-apps` | global | `sase_fp_source_apps_read` | GET https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profile-source-applications |
| `show sase fp-source-apps id` | global | `sase_fp_source_apps_read` | GET https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profile-source-applications/{id} |
| `show sase fp-user-locations` | global | `sase_fp_user_locations_read` | GET https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profile-user-locations |
| `show sase fp-user-locations id` | global | `sase_fp_user_locations_read` | GET https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profile-user-locations/{id} |
| `show sase global-settings` | global | `sase_global_settings_read` | GET https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/global-settings |
| `show sase infrastructure-settings` | global | `sase_infrastructure_settings_read` | GET https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/infrastructure-settings |
| `show sase internal-dns-servers` | global | `sase_internal_dns_servers_read` | GET https://api.strata.paloaltonetworks.com/config/deployment/v1/internal-dns-servers |
| `show sase internal-dns-servers id` | global | `sase_internal_dns_servers_read` | GET https://api.strata.paloaltonetworks.com/config/deployment/v1/internal-dns-servers/{id} |
| `show sase locations` | global | `sase_locations_read` | GET https://api.strata.paloaltonetworks.com/config/deployment/v1/locations |
| `show sase mobileagent locations` | global | `sase_locations_read` | GET https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/locations |
| `show sase remote-networks` | global | `sase_remote_networks_read` | GET https://api.strata.paloaltonetworks.com/config/deployment/v1/remote-networks |
| `show sase remote-networks id` | global | `sase_remote_networks_read` | GET https://api.strata.paloaltonetworks.com/config/deployment/v1/remote-networks/{id} |
| `show sase service-connection-groups` | global | `sase_service_connection_groups_read` | GET https://api.strata.paloaltonetworks.com/config/deployment/v1/service-connection-groups |
| `show sase service-connection-groups id` | global | `sase_service_connection_groups_read` | GET https://api.strata.paloaltonetworks.com/config/deployment/v1/service-connection-groups/{id} |
| `show sase service-connections` | global | `sase_service_connections_read` | GET https://api.strata.paloaltonetworks.com/config/deployment/v1/service-connections |
| `show sase service-connections id` | global | `sase_service_connections_read` | GET https://api.strata.paloaltonetworks.com/config/deployment/v1/service-connections/{id} |
| `show sase shared-infrastructure-settings` | global | `sase_shared_infrastructure_settings_read` | GET https://api.strata.paloaltonetworks.com/config/deployment/v1/shared-infrastructure-settings |
| `show sase sites` | global | `sase_sites_read` | GET https://api.strata.paloaltonetworks.com/config/deployment/v1/sites |
| `show sase sites id` | global | `sase_sites_read` | GET https://api.strata.paloaltonetworks.com/config/deployment/v1/sites/{id} |
| `show sase traffic-steering-rules` | global | `sase_traffic_steering_rules_read` | GET https://api.strata.paloaltonetworks.com/config/deployment/v1/traffic-steering-rules |
| `show sase traffic-steering-rules id` | global | `sase_traffic_steering_rules_read` | GET https://api.strata.paloaltonetworks.com/config/deployment/v1/traffic-steering-rules/{id} |
| `show sase tunnel-profiles` | global | `sase_tunnel_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/tunnel-profiles |
| `update sase agent-profiles` | global | `sase_agent_profiles_write` | PUT https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/agent-profiles |
| `update sase authentication-settings` | global | `sase_authentication_settings_write` | PUT https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/authentication-settings |
| `update sase bandwidth-allocations` | global | `sase_bandwidth_allocations_write` | PUT https://api.strata.paloaltonetworks.com/config/deployment/v1/bandwidth-allocations |
| `update sase bgp-routing` | global | `sase_bgp_routing_write` | PUT https://api.strata.paloaltonetworks.com/config/deployment/v1/bgp-routing |
| `update sase forwarding-profiles` | global | `sase_forwarding_profiles_write` | PUT https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profiles/{id} |
| `update sase fp-custom-proxies` | global | `sase_fp_custom_proxies_write` | PUT https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profile-regional-and-custom-proxies/{id} |
| `update sase fp-destinations` | global | `sase_fp_destinations_write` | PUT https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profile-destinations/{id} |
| `update sase fp-source-apps` | global | `sase_fp_source_apps_write` | PUT https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profile-source-applications/{id} |
| `update sase fp-user-locations` | global | `sase_fp_user_locations_write` | PUT https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/forwarding-profile-user-locations/{id} |
| `update sase global-settings` | global | `sase_global_settings_write` | PUT https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/global-settings |
| `update sase infrastructure-settings` | global | `sase_infrastructure_settings_write` | PUT https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/infrastructure-settings |
| `update sase internal-dns-servers` | global | `sase_internal_dns_servers_write` | PUT https://api.strata.paloaltonetworks.com/config/deployment/v1/internal-dns-servers/{id} |
| `update sase locations` | global | `sase_locations_write` | PUT https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/locations |
| `update sase remote-networks` | global | `sase_remote_networks_write` | PUT https://api.strata.paloaltonetworks.com/config/deployment/v1/remote-networks/{id} |
| `update sase service-connection-groups` | global | `sase_service_connection_groups_write` | PUT https://api.strata.paloaltonetworks.com/config/deployment/v1/service-connection-groups/{id} |
| `update sase service-connections` | global | `sase_service_connections_write` | PUT https://api.strata.paloaltonetworks.com/config/deployment/v1/service-connections/{id} |
| `update sase shared-infrastructure-settings` | global | `sase_shared_infrastructure_settings_write` | PUT https://api.strata.paloaltonetworks.com/config/deployment/v1/shared-infrastructure-settings |
| `update sase sites` | global | `sase_sites_write` | PUT https://api.strata.paloaltonetworks.com/config/deployment/v1/sites/{id} |
| `update sase traffic-steering-rules` | global | `sase_traffic_steering_rules_write` | PUT https://api.strata.paloaltonetworks.com/config/deployment/v1/traffic-steering-rules/{id} |
| `update sase tunnel-profiles` | global | `sase_tunnel_profiles_write` | PUT https://api.strata.paloaltonetworks.com/config/mobile-agent/v1/tunnel-profiles |

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
| `set subscription instances` | global | `subscription_instances_write` | POST https://api.sase.paloaltonetworks.com/subscription/v1/instances |
| `show subscription instances` | global | `subscription_instances_read` | GET https://api.sase.paloaltonetworks.com/subscription/v1/instances |
| `show subscription licenses` | global | `subscription_licenses_read` | GET https://api.sase.paloaltonetworks.com/subscription/v1/licenses |

## Tenancy

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `delete tenant-service-groups` | global | `tenant_service_groups_write` | DELETE https://api.sase.paloaltonetworks.com/tenancy/v1/tenant_service_groups/{tsg_id} |
| `set tenant-service-groups` | global | `tenant_service_groups_write` | POST https://api.sase.paloaltonetworks.com/tenancy/v1/tenant_service_groups |
| `set tenant-service-groups list-ancestors` | global | `tenant_service_groups_list_ancestors_write` | POST https://api.sase.paloaltonetworks.com/tenancy/v1/tenant_service_groups/{tsg_id}/operations/list_ancestors |
| `set tenant-service-groups list-children` | global | `tenant_service_groups_list_children_write` | POST https://api.sase.paloaltonetworks.com/tenancy/v1/tenant_service_groups/{tsg_id}/operations/list_children |
| `show tenant-service-groups` | global | `tenant_service_groups_read` | GET https://api.sase.paloaltonetworks.com/tenancy/v1/tenant_service_groups |
| `show tenant-service-groups id` | global | `tenant_service_groups_read` | GET https://api.sase.paloaltonetworks.com/tenancy/v1/tenant_service_groups/{tsg_id} |
| `update tenant-service-groups` | global | `tenant_service_groups_write` | PUT https://api.sase.paloaltonetworks.com/tenancy/v1/tenant_service_groups/{tsg_id} |
