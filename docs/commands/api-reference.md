# ARC Command → SCM API Reference

Generated from each command's doc front-matter (`api:` field) and the live
registry. Regenerate with `python app/scripts/generate_command_docs.py` (runs on `docsupdate`).

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
| `delete ha-configurations` | device | `ha_configurations_write` | DELETE https://api.strata.paloaltonetworks.com/config/device/v1/ha-configurations |
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
| `show ha-configurations` | device | `ha_configurations_read` | GET https://api.strata.paloaltonetworks.com/config/device/v1/ha-configurations |
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
| `delete authentication-profile` | folder | `authentication` | — |
| `delete local-user` | folder | `local_users` | — |
| `set authentication-profile` | folder | `authentication` | — |
| `set local-user` | folder | `local_users` | — |
| `show authentication-profile` | folder | `authentication` | GET /config/identity/v1/authentication-profiles |
| `show authentication-rules` | folder | `authentication` | GET /config/identity/v1/authentication-rules |
| `show certificate-profile` | folder | `certificates` | GET /config/identity/v1/certificate-profiles |
| `show local-user` | folder | `local_users` | GET /config/identity/v1/local-users |
| `show local-user-group` | folder | `local_users` | GET /config/identity/v1/local-user-groups |
| `show mfa-server` | folder | `authentication` | GET /config/identity/v1/mfa-servers |
| `show radius-server` | folder | `authentication` | GET /config/identity/v1/radius-server-profiles |
| `show tls-service-profile` | folder | `certificates` | GET /config/identity/v1/tls-service-profiles |
| `show user ip-user-mapping` | device | `local_users` | (live device state — via the SCM device tunnel; no SSH/2FA) |

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
| `delete nat-rule` | folder | `nat_rules` | — |
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
| `show arp` | device | `show_arp` | (live device state — via the SCM device tunnel; no SSH/2FA) |
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
| `show routing bgp` | device | `bgp_routing` | (live device state — via the SCM device tunnel; no SSH/2FA) |
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
| `show session all` | device | `show_sessions` | (live device state — via the SCM device tunnel; no SSH/2FA) |
| `show system-match-list` | global | `system_match_list_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/system-match-list |
| `show system-match-list id` | global | `system_match_list_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/system-match-list/{id} |
| `show tunnel-interfaces` | global | `tunnel_interfaces_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/tunnel-interfaces |
| `show tunnel-interfaces id` | global | `tunnel_interfaces_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/tunnel-interfaces/{id} |
| `show userid-match-list` | global | `userid_match_list_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/userid-match-list |
| `show userid-match-list id` | global | `userid_match_list_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/userid-match-list/{id} |
| `show vlan-interfaces` | global | `vlan_interfaces_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/vlan-interfaces |
| `show vlan-interfaces id` | global | `vlan_interfaces_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/vlan-interfaces/{id} |
| `show vpn ike-sa` | device | `ipsec_vpn` | (live device state — via the SCM device tunnel; no SSH/2FA) |
| `show vpn tunnel` | device | `ipsec_vpn` | (live device state — via the SCM device tunnel; no SSH/2FA) |
| `show zone` | folder | `show_zone` | GET /config/network/v1/zones |
| `show zone-profiles` | global | `zone_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/zone-protection-profiles |
| `show zone-profiles id` | global | `zone_profiles_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/zone-protection-profiles/{id} |
| `show zones id` | global | `zones_read` | GET https://api.strata.paloaltonetworks.com/config/network/v1/zones/{id} |
| `test nat-policy-match` | device | `test_nat` | (live device state — via the SCM device tunnel; no SSH/2FA) |
| `test url` | device | `test_url` | (live device state — via the SCM device tunnel; no SSH/2FA) |
| `traceroute host` | device | `traceroute` | (live device state — via the SCM device tunnel; no SSH/2FA) |
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
| `update nat-rule` | folder | `nat_rules` | — |
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
| `clone` | folder | `clone_object` | — |
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
| `show address search` | folder | `show_address` | — |
| `show address tag` | folder | `show_address` | — |
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
| `show service search` | folder | `show_service` | — |
| `show service-group` | folder | `service_groups` | GET /config/objects/v1/service-groups |
| `show tag` | folder | `show_tag` | GET /config/objects/v1/tags |
| `update address` | folder | `update_objects` | PUT /config/objects/v1/addresses/{id} |
| `update address bulk` | folder | `update_objects` | — |
| `update address-group` | folder | `update_objects` | PUT /config/objects/v1/address-groups/{id} |
| `update external-dynamic-list` | folder | `update_objects` | PUT /config/objects/v1/external-dynamic-lists/{id} |
| `update service` | folder | `update_objects` | PUT /config/objects/v1/services/{id} |
| `update service-group` | folder | `update_objects` | PUT /config/objects/v1/service-groups/{id} |
| `update tag` | folder | `update_objects` | PUT /config/objects/v1/tags/{id} |

## Operations

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `clear session all` | device | `show_session` | (live device state — via the SCM device tunnel; no SSH/2FA) |
| `clear session id` | device | `show_session` | (live device state — via the SCM device tunnel; no SSH/2FA) |
| `commit` | folder | — | POST /config/setup/v1/config-versions/candidate:push |
| `load config version` | global | `config_rollback` | — |
| `ping host` | device | `ping` | (live device state — via the SCM device tunnel; no SSH/2FA) |
| `request system reboot` | device | `request_system_reboot` | (live device state — via the SCM device tunnel; no SSH/2FA) |
| `request system shutdown` | device | `request_system_reboot` | (live device state — via the SCM device tunnel; no SSH/2FA) |
| `request system software check` | device | `request_system_software` | (live device state — via the SCM device tunnel; no SSH/2FA) |
| `set jobs bgp-policy-export` | global | `jobs_bgp_policy_export_write` | POST https://api.strata.paloaltonetworks.com/operations/v1/jobs/bgp-policy-export |
| `set jobs device-interfaces` | global | `jobs_device_interfaces_write` | POST https://api.strata.paloaltonetworks.com/operations/v1/jobs/device-interfaces |
| `set jobs device-rules` | global | `jobs_device_rules_write` | POST https://api.strata.paloaltonetworks.com/operations/v1/jobs/device-rules |
| `set jobs dns-proxy` | global | `jobs_dns_proxy_write` | POST https://api.strata.paloaltonetworks.com/operations/v1/jobs/dns-proxy |
| `set jobs fib-table` | global | `jobs_fib_table_write` | POST https://api.strata.paloaltonetworks.com/operations/v1/jobs/fib-table |
| `set jobs logging-service-forwarding-status` | global | `jobs_logging_service_forwarding_status_write` | POST https://api.strata.paloaltonetworks.com/operations/v1/jobs/logging-service-forwarding-status |
| `set jobs route-table` | global | `jobs_route_table_write` | POST https://api.strata.paloaltonetworks.com/operations/v1/jobs/route-table |
| `show config format set` | folder | `config_view` | — |
| `show config running` | folder | `config_view` | (live device state — SSH via --remote) |
| `show config versions` | global | `config_view` | — |
| `show device jobs id` | global | `device_jobs_read` | GET https://api.strata.paloaltonetworks.com/operations/v1/device/jobs/{id} |
| `show diff` | global | `config_view` | — |
| `show jobs all` | global | `show_jobs` | GET /config/setup/v1/jobs |
| `show jobs id` | global | `show_jobs` | GET /config/setup/v1/jobs/{id} |
| `show local-config download` | device | `local_config_download_read` | GET https://api.strata.paloaltonetworks.com/operations/v1/local-config/download |
| `show local-config versions` | device | `local_config_versions_read` | GET https://api.strata.paloaltonetworks.com/operations/v1/local-config/versions |
| `show log detail` | global | `sls_logs` | — |
| `show log system` | global | `sls_logs` | (live device state — SSH via --remote) |
| `show log threat` | global | `sls_logs` | (live device state — SSH via --remote) |
| `show log traffic` | global | `sls_logs` | (live device state — SSH via --remote) |
| `show system disk-space` | device | `show_system_disk_space` | (live device state — via the SCM device tunnel; no SSH/2FA) |
| `show system info` | device | `show_system_info` | GET /config/setup/v1/devices/{id} |
| `show system resources` | device | `show_system_resources` | (live device state — via the SCM device tunnel; no SSH/2FA) |

## Panos-Config

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `check data-access-passwd system` | remote | `panos_config_check` | (live device state — SSH via --remote; expect device 2FA) |
| `check full-commit-required` | remote | `panos_config_check` | (live device state — SSH via --remote; expect device 2FA) |
| `check pending-changes` | remote | `panos_config_check` | (live device state — SSH via --remote; expect device 2FA) |
| `commit description` | remote | `panos_config_commit` | (live device state — SSH via --remote; expect device 2FA) |
| `load config key` | remote | `panos_config_load` | (live device state — SSH via --remote; expect device 2FA) |
| `load device-state` | remote | `panos_config_load` | (live device state — SSH via --remote; expect device 2FA) |
| `save config to` | remote | `panos_config_save` | (live device state — SSH via --remote; expect device 2FA) |
| `save device-state` | remote | `panos_config_save` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig high-availability` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig high-availability enabled` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting autofocus` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting autofocus autofocus-url` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting autofocus enabled` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting autofocus query-timeout` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting cloud-userid` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting cloud-userid address` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting cloud-userid disabled` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting cloud-userid segment-assignment` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting cloudapp` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting cloudapp cloudapp-srvr-addr` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting cloudapp cloudapp-srvr-addr address` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting cloudapp disable` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting custom-logo` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting iot` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting iot edge` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting iot edge address` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting management admin-lockout` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting management admin-session` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting management admin-session max-session-count` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting management admin-session max-session-time` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting management api` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting management api key` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting management api key certificate` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting management api key lifetime` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting management appusage-lifetime` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting management audit-tracking` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting management audit-tracking op-commands` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting management audit-tracking send-syslog` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting management audit-tracking ui-actions` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting management browse-activity-report-setting` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting management browse-activity-report-setting average-browse-time` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting management browse-activity-report-setting page-load-threshold` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting management common-criteria self-test-schedule` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting management common-criteria self-test-schedule crypto start-time` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting management common-criteria self-test-schedule software-integrity start-time` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting management disable-predefined-correlation-objs` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting management disable-predefined-reports` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting management hostname-type-in-syslog` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting management idle-timeout` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting management max-audit-versions` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting management max-rows-in-csv-export` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting management max-rows-in-pdf-report` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting management panorama-ssl-send-retries` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting management panorama-tcp-receive-timeout` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting management panorama-tcp-send-timeout` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting management quota-settings` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting management report-expiration-period` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting management report-run-time` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting management rule-audit-comment-regex` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting management secure-conn-client` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting management secure-conn-client certificate-type local certificate` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting management secure-conn-client certificate-type local certificate-profile` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting management secure-conn-client certificate-type scep certificate-profile` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting management secure-conn-client certificate-type scep scep-profile` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting management secure-conn-server` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting management secure-conn-server certificate-profile` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting management secure-conn-server enable-secure-user-id-communication` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting management secure-conn-server ssl-tls-service-profile` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting session offload` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting session packet-buffer-protection-use-buffer` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting session persistent-dipp-alert-enable` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting session-tracking` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting session-tracking disable` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting session-tracking user-re-authentication` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting session-tracking user-re-authentication disable` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig setting ssl-decrypt use-mp-sess-cache` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system auto-renew-mkey-lifetime` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system device-telemetry` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system device-telemetry device-health-performance` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system device-telemetry product-usage` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system device-telemetry region` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system device-telemetry threat-prevention` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system dns-security-server` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system dns-setting servers` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system dns-setting servers primary` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system dns-setting servers secondary` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system geo-location` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system geo-location latitude` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system geo-location longitude` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system hsm-settings` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system hsm-settings provider` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system hsm-settings provider ciphertrust-manager hsm-server` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system hsm-settings provider ncipher-nshield-connect hsm-server` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system hsm-settings provider ncipher-nshield-connect rfs-address` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system hsm-settings provider safenet-network ha` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system hsm-settings provider safenet-network ha auto-recovery-retry` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system hsm-settings provider safenet-network ha ha-group-name` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system hsm-settings provider safenet-network hsm-server` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system inline-cloud-proxy` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system locale` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system log-link` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system motd-and-banner` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system motd-and-banner message` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system motd-and-banner severity` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system mtu` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system ntp-servers` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system ntp-servers primary-ntp-server authentication-type` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system ntp-servers primary-ntp-server authentication-type symmetric-key algorithm` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system ntp-servers primary-ntp-server authentication-type symmetric-key algorithm md5 authentication-key` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system ntp-servers primary-ntp-server authentication-type symmetric-key algorithm sha1 authentication-key` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system ntp-servers primary-ntp-server authentication-type symmetric-key key-id` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system ntp-servers primary-ntp-server ntp-server-address` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system ntp-servers secondary-ntp-server authentication-type` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system ntp-servers secondary-ntp-server authentication-type symmetric-key algorithm` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system ntp-servers secondary-ntp-server authentication-type symmetric-key algorithm md5 authentication-key` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system ntp-servers secondary-ntp-server authentication-type symmetric-key algorithm sha1 authentication-key` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system ntp-servers secondary-ntp-server authentication-type symmetric-key key-id` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system ntp-servers secondary-ntp-server ntp-server-address` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system panorama local-panorama panorama-server` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system permitted-ip` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system secure-proxy-port` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system service` | remote | `panos_config_recovery` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system snmp-setting` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system snmp-setting access-setting version` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system snmp-setting access-setting version v2c snmp-community-string` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system snmp-setting access-setting version v3 users` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system snmp-setting access-setting version v3 views` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system snmp-setting snmp-system contact` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system snmp-setting snmp-system location` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system snmp-setting snmp-system send-event-specific-traps` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system ssh` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system ssh ha ha-profile` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system ssh mgmt server-profile` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system ssh profiles ha-profiles` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system ssh profiles mgmt-profiles` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system ssh profiles mgmt-profiles server-profiles` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system ssh regenerate-hostkeys ha` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system ssh regenerate-hostkeys ha key-type` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system ssh regenerate-hostkeys ha key-type ecdsa key-length` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system ssh regenerate-hostkeys ha key-type rsa key-length` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system ssh regenerate-hostkeys mgmt` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system ssh regenerate-hostkeys mgmt key-type` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system ssh regenerate-hostkeys mgmt key-type ecdsa key-length` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system ssh regenerate-hostkeys mgmt key-type rsa key-length` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system timezone` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system type` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system type dhcp-client` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system type static` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule anti-virus` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule anti-virus recurring` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule anti-virus recurring daily` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule anti-virus recurring daily action` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule anti-virus recurring daily at` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule anti-virus recurring hourly` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule anti-virus recurring hourly action` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule anti-virus recurring hourly at` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule anti-virus recurring none` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule anti-virus recurring sync-to-peer` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule anti-virus recurring threshold` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule anti-virus recurring weekly` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule anti-virus recurring weekly action` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule anti-virus recurring weekly at` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule anti-virus recurring weekly day-of-week` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule threats` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule threats recurring` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule threats recurring daily` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule threats recurring daily action` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule threats recurring daily at` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule threats recurring daily disable-new-content` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule threats recurring every-30-mins` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule threats recurring every-30-mins action` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule threats recurring every-30-mins at` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule threats recurring every-30-mins disable-new-content` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule threats recurring hourly` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule threats recurring hourly action` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule threats recurring hourly at` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule threats recurring hourly disable-new-content` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule threats recurring new-app-threshold` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule threats recurring none` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule threats recurring sync-to-peer` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule threats recurring threshold` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule threats recurring weekly` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule threats recurring weekly action` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule threats recurring weekly at` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule threats recurring weekly day-of-week` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule threats recurring weekly disable-new-content` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule wf-private` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule wf-private recurring` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule wf-private recurring every-15-mins` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule wf-private recurring every-15-mins action` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule wf-private recurring every-15-mins at` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule wf-private recurring every-30-mins` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule wf-private recurring every-30-mins action` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule wf-private recurring every-30-mins at` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule wf-private recurring every-5-mins` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule wf-private recurring every-5-mins action` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule wf-private recurring every-5-mins at` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule wf-private recurring every-hour` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule wf-private recurring every-hour action` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule wf-private recurring every-hour at` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule wf-private recurring none` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule wf-private recurring sync-to-peer` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule wildfire` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule wildfire recurring` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule wildfire recurring every-15-mins action` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule wildfire recurring every-15-mins at` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule wildfire recurring every-15-mins sync-to-peer` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule wildfire recurring every-30-mins action` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule wildfire recurring every-30-mins at` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule wildfire recurring every-30-mins sync-to-peer` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule wildfire recurring every-hour action` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule wildfire recurring every-hour at` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule wildfire recurring every-hour sync-to-peer` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule wildfire recurring every-min action` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set deviceconfig system update-schedule wildfire recurring every-min sync-to-peer` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `set mgt-config` | remote | `panos_config_mgt_config` | (live device state — SSH via --remote; expect device 2FA) |
| `set mgt-config password-complexity` | remote | `panos_config_mgt_config` | (live device state — SSH via --remote; expect device 2FA) |
| `set mgt-config password-complexity block-username-inclusion` | remote | `panos_config_mgt_config` | (live device state — SSH via --remote; expect device 2FA) |
| `set mgt-config password-complexity enabled` | remote | `panos_config_mgt_config` | (live device state — SSH via --remote; expect device 2FA) |
| `set mgt-config password-complexity minimum-length` | remote | `panos_config_mgt_config` | (live device state — SSH via --remote; expect device 2FA) |
| `set mgt-config password-complexity password-change` | remote | `panos_config_mgt_config` | (live device state — SSH via --remote; expect device 2FA) |
| `set mgt-config password-complexity password-change-on-first-login` | remote | `panos_config_mgt_config` | (live device state — SSH via --remote; expect device 2FA) |
| `set mgt-config password-complexity password-change-period-block` | remote | `panos_config_mgt_config` | (live device state — SSH via --remote; expect device 2FA) |
| `set mgt-config password-complexity password-history-count` | remote | `panos_config_mgt_config` | (live device state — SSH via --remote; expect device 2FA) |
| `set mgt-config password-profile` | remote | `panos_config_mgt_config` | (live device state — SSH via --remote; expect device 2FA) |
| `set shared` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `set shared email-scheduler` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `set shared log-settings` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `set shared pdf-summary-report` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `set shared report-group` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `set shared response-page remote-browser-isolation` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `set shared response-page url-reply` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show application` | remote | `panos_config_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show application-tag` | remote | `panos_config_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show authentication-object` | remote | `panos_config_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show captive-portal` | remote | `panos_config_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show captive-portal mode` | remote | `panos_config_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show captive-portal mode redirect session-cookie` | remote | `panos_config_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show cloud-identity-engine` | remote | `panos_config_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show device-object` | remote | `panos_config_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig high-availability` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig high-availability cluster` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig high-availability cluster cluster-members` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig high-availability group` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig high-availability group election-option timers` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig high-availability group mode active-active` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig high-availability group mode active-active network-configuration` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig high-availability group mode active-active network-configuration sync` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig high-availability group mode active-active session-owner-selection` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig high-availability group mode active-active session-owner-selection first-packet session-setup` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig high-availability group mode active-active virtual-address` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig high-availability group mode active-passive` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig high-availability group monitoring link-monitoring` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig high-availability group monitoring link-monitoring link-group` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig high-availability group monitoring path-monitoring` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig high-availability group monitoring path-monitoring path-group` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig high-availability group state-synchronization ha2-keep-alive` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig high-availability interface` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig high-availability interface ha1` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig high-availability interface ha1 encryption` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig setting` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig setting application` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig setting application traceroute` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig setting cloudapp` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig setting cloudapp cloudapp-srvr-addr` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig setting custom-logo` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig setting dhcp-syslog-server` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig setting iot` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig setting iot edge` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig setting logging` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig setting logging enhanced-application-logging disable-application` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig setting logging enhanced-application-logging disable-global` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig setting management` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig setting management api` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig setting management api key` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig setting management common-criteria` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig setting management common-criteria self-test-schedule` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig setting management common-criteria-alarm-generation` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig setting management quota-settings` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig setting management secure-conn-client` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig setting management secure-conn-client certificate-type` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig setting session-tracking` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig setting session-tracking user-re-authentication` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig setting vpn` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig setting vpn ikev2` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig setting wildfire` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig setting wildfire cloud-inline-wf-session-info-select` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig setting wildfire cloud-inline-wildfire` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig setting wildfire cloud-inline-wildfire file-size-limit` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig setting wildfire file-size-limit` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig setting wildfire session-info-select` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system dns-setting` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system dns-setting servers` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system dns-setting servers encrypted-dns` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system dns-setting servers encrypted-dns connection-type` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system hsm-settings` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system hsm-settings provider` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system hsm-settings provider ciphertrust-manager hsm-server` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system hsm-settings provider ncipher-nshield-connect hsm-server` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system hsm-settings provider safenet-network ha` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system hsm-settings provider safenet-network hsm-server` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system ipv6-gw-type` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system ipv6-type` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system log-export-schedule` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system log-link` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system ntp-servers` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system ntp-servers primary-ntp-server authentication-type` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system ntp-servers primary-ntp-server authentication-type symmetric-key algorithm` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system ntp-servers secondary-ntp-server authentication-type` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system ntp-servers secondary-ntp-server authentication-type symmetric-key algorithm` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system panorama` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system permitted-ip` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system route` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system route destination` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system route service` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system snmp-setting` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system snmp-setting access-setting version` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system snmp-setting access-setting version v3 users` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system snmp-setting access-setting version v3 views` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system ssh` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system ssh profiles ha-profiles` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system ssh profiles mgmt-profiles` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system ssh profiles mgmt-profiles server-profiles` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system ssh regenerate-hostkeys ha` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system ssh regenerate-hostkeys ha key-type` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system ssh regenerate-hostkeys mgmt` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system ssh regenerate-hostkeys mgmt key-type` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system type` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system update-schedule` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system update-schedule anti-virus recurring` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system update-schedule app-profile recurring` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system update-schedule global-protect-clientless-vpn recurring` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system update-schedule global-protect-datafile recurring` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system update-schedule threats recurring` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system update-schedule wf-private recurring` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system update-schedule wildfire recurring` | remote | `panos_config_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show disable-inspect` | remote | `panos_config_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show display-name` | remote | `panos_config_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show dynamic-user-group` | remote | `panos_config_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show email-scheduler` | remote | `panos_config_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show external-list` | remote | `panos_config_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show global-protect global-protect-gateway` | remote | `panos_config_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show global-protect global-protect-portal` | remote | `panos_config_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show group-mapping` | remote | `panos_config_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show import` | remote | `panos_config_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show iptag-include-exclude-list` | remote | `panos_config_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show iptag-include-exclude-list include-exclude-network` | remote | `panos_config_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show ipuser-include-exclude-list` | remote | `panos_config_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show ipuser-include-exclude-list include-exclude-network` | remote | `panos_config_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show mgt-config` | remote | `panos_config_mgt_config` | (live device state — SSH via --remote; expect device 2FA) |
| `show mgt-config access-domain` | remote | `panos_config_mgt_config` | (live device state — SSH via --remote; expect device 2FA) |
| `show mgt-config password-complexity` | remote | `panos_config_mgt_config` | (live device state — SSH via --remote; expect device 2FA) |
| `show mgt-config password-complexity password-change` | remote | `panos_config_mgt_config` | (live device state — SSH via --remote; expect device 2FA) |
| `show mgt-config password-profile` | remote | `panos_config_mgt_config` | (live device state — SSH via --remote; expect device 2FA) |
| `show mgt-config users` | remote | `panos_config_mgt_config` | (live device state — SSH via --remote; expect device 2FA) |
| `show network` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network dhcp` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network dhcp interface` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network dns-proxy` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network ike` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network ike crypto-profiles` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network ike crypto-profiles global-protect-app-crypto-profiles` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network ike crypto-profiles ike-crypto-profiles` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network ike crypto-profiles ipsec-crypto-profiles` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network ike gateway` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface aggregate-ethernet` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface ethernet` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface loopback` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface loopback adjust-tcp-mss` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface loopback ip` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface loopback ipv6` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface loopback ipv6 address` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface loopback units` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface sdwan` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface sdwan units` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface tunnel` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface tunnel ip` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface tunnel ipv6` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface tunnel ipv6 address` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface tunnel units` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan adjust-tcp-mss` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan arp` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ddns-config` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ddns-config ddns-vendor-config` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan dhcp-client` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan dhcp-client send-hostname` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ip` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ipv6` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ipv6 address` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ipv6 dhcp-client` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ipv6 dhcp-client neighbor-discovery dns-server` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ipv6 dhcp-client neighbor-discovery dns-server source` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ipv6 dhcp-client neighbor-discovery dns-server source manual server` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ipv6 dhcp-client neighbor-discovery dns-suffix` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ipv6 dhcp-client neighbor-discovery dns-suffix source` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ipv6 dhcp-client neighbor-discovery dns-suffix source manual suffix` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ipv6 dhcp-client neighbor-discovery neighbor` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ipv6 dhcp-client prefix-delegation enable` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ipv6 dhcp-client v6-options enable` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ipv6 inherited` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ipv6 inherited assign-addr` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ipv6 inherited neighbor-discovery` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ipv6 inherited neighbor-discovery dns-server` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ipv6 inherited neighbor-discovery dns-server source` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ipv6 inherited neighbor-discovery dns-server source manual server` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ipv6 inherited neighbor-discovery dns-suffix` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ipv6 inherited neighbor-discovery dns-suffix source` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ipv6 inherited neighbor-discovery dns-suffix source manual suffix` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ipv6 inherited neighbor-discovery neighbor` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ipv6 inherited neighbor-discovery router-advertisement` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ipv6 neighbor-discovery` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ipv6 neighbor-discovery neighbor` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ipv6 neighbor-discovery router-advertisement` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ipv6 neighbor-discovery router-advertisement dns-support` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ipv6 neighbor-discovery router-advertisement dns-support server` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ipv6 neighbor-discovery router-advertisement dns-support suffix` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ipv6 pppoe` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ipv6 pppoe dhcpv6 prefix-delegation` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ipv6 pppoe dhcpv6 prefix-delegation enable` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ipv6 pppoe dhcpv6 v6-options` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ipv6 pppoe dhcpv6 v6-options enable` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ipv6 pppoe neighbor-discovery dns-server` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ipv6 pppoe neighbor-discovery dns-server source` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ipv6 pppoe neighbor-discovery dns-server source manual server` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ipv6 pppoe neighbor-discovery dns-suffix` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ipv6 pppoe neighbor-discovery dns-suffix source` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ipv6 pppoe neighbor-discovery dns-suffix source manual suffix` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ipv6 pppoe neighbor-discovery neighbor` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ndp-proxy` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan ndp-proxy address` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network interface vlan units` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network lldp` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network logical-router` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network macsec` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network macsec crypto-profiles` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network macsec interfaces` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network macsec pre-shared-key-profiles` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network profiles` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network profiles bfd-profile` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network profiles interface-management-profile` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network profiles lldp-profile` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network profiles monitor-profile` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network profiles zone-protection-profile` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network qos` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network qos interface` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network qos profile` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network routing-profile` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network routing-profile bfd` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network routing-profile bgp` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network routing-profile bgp address-family-profile` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network routing-profile bgp auth-profile` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network routing-profile bgp dampening-profile` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network routing-profile bgp filtering-profile` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network routing-profile bgp redistribution-profile` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network routing-profile bgp timer-profile` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network routing-profile filters` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network routing-profile filters access-list` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network routing-profile filters as-path-access-list` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network routing-profile filters community-list` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network routing-profile filters prefix-list` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network routing-profile filters route-maps` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network routing-profile filters route-maps bgp bgp-entry` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network routing-profile filters route-maps redistribution redist-entry` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network routing-profile multicast` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network routing-profile ospf` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network routing-profile ospf auth-profile` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network routing-profile ospf if-timer-profile` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network routing-profile ospf redistribution-profile` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network routing-profile ospf spf-timer-profile` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network routing-profile ospfv3` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network routing-profile ospfv3 auth-profile` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network routing-profile ospfv3 if-timer-profile` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network routing-profile ospfv3 redistribution-profile` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network routing-profile ospfv3 spf-timer-profile` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network routing-profile rip` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network routing-profile rip auth-profile` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network routing-profile rip global-timer-profile` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network routing-profile rip redistribution-profile` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network tunnel` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network tunnel global-protect-gateway` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network tunnel global-protect-site-to-site` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network tunnel gre` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network tunnel ipsec` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network underlay-net` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network underlay-net ip-mapping` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network virtual-router` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network virtual-wire` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show network vlan` | remote | `panos_config_network` | (live device state — SSH via --remote; expect device 2FA) |
| `show pdf-summary-report` | remote | `panos_config_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show profiles` | remote | `panos_config_profiles` | (live device state — SSH via --remote; expect device 2FA) |
| `show profiles data-filtering` | remote | `panos_config_profiles` | (live device state — SSH via --remote; expect device 2FA) |
| `show profiles data-objects` | remote | `panos_config_profiles` | (live device state — SSH via --remote; expect device 2FA) |
| `show profiles decryption` | remote | `panos_config_profiles` | (live device state — SSH via --remote; expect device 2FA) |
| `show profiles dos-protection` | remote | `panos_config_profiles` | (live device state — SSH via --remote; expect device 2FA) |
| `show profiles file-blocking` | remote | `panos_config_profiles` | (live device state — SSH via --remote; expect device 2FA) |
| `show profiles hip-objects` | remote | `panos_config_profiles` | (live device state — SSH via --remote; expect device 2FA) |
| `show profiles packet-broker` | remote | `panos_config_profiles` | (live device state — SSH via --remote; expect device 2FA) |
| `show profiles sdwan-error-correction` | remote | `panos_config_profiles` | (live device state — SSH via --remote; expect device 2FA) |
| `show profiles sdwan-path-quality` | remote | `panos_config_profiles` | (live device state — SSH via --remote; expect device 2FA) |
| `show profiles sdwan-saas-quality` | remote | `panos_config_profiles` | (live device state — SSH via --remote; expect device 2FA) |
| `show profiles sdwan-traffic-distribution` | remote | `panos_config_profiles` | (live device state — SSH via --remote; expect device 2FA) |
| `show profiles spyware` | remote | `panos_config_profiles` | (live device state — SSH via --remote; expect device 2FA) |
| `show profiles url-filtering` | remote | `panos_config_profiles` | (live device state — SSH via --remote; expect device 2FA) |
| `show profiles virus` | remote | `panos_config_profiles` | (live device state — SSH via --remote; expect device 2FA) |
| `show profiles vulnerability` | remote | `panos_config_profiles` | (live device state — SSH via --remote; expect device 2FA) |
| `show profiles wildfire-analysis` | remote | `panos_config_profiles` | (live device state — SSH via --remote; expect device 2FA) |
| `show redistribution-agent` | remote | `panos_config_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show redistribution-collector` | remote | `panos_config_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show redistribution-collector setting` | remote | `panos_config_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show report-group` | remote | `panos_config_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show reports` | remote | `panos_config_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show route` | remote | `panos_config_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show route service` | remote | `panos_config_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show rulebase` | remote | `panos_config_rulebase` | (live device state — SSH via --remote; expect device 2FA) |
| `show rulebase application-override rules` | remote | `panos_config_rulebase` | (live device state — SSH via --remote; expect device 2FA) |
| `show rulebase authentication rules` | remote | `panos_config_rulebase` | (live device state — SSH via --remote; expect device 2FA) |
| `show rulebase decryption rules` | remote | `panos_config_rulebase` | (live device state — SSH via --remote; expect device 2FA) |
| `show rulebase default-security-rules rules` | remote | `panos_config_rulebase` | (live device state — SSH via --remote; expect device 2FA) |
| `show rulebase dos rules` | remote | `panos_config_rulebase` | (live device state — SSH via --remote; expect device 2FA) |
| `show rulebase nat rules` | remote | `panos_config_rulebase` | (live device state — SSH via --remote; expect device 2FA) |
| `show rulebase network-packet-broker rules` | remote | `panos_config_rulebase` | (live device state — SSH via --remote; expect device 2FA) |
| `show rulebase pbf rules` | remote | `panos_config_rulebase` | (live device state — SSH via --remote; expect device 2FA) |
| `show rulebase qos rules` | remote | `panos_config_rulebase` | (live device state — SSH via --remote; expect device 2FA) |
| `show rulebase sdwan rules` | remote | `panos_config_rulebase` | (live device state — SSH via --remote; expect device 2FA) |
| `show rulebase security rules` | remote | `panos_config_rulebase` | (live device state — SSH via --remote; expect device 2FA) |
| `show rulebase tunnel-inspect rules` | remote | `panos_config_rulebase` | (live device state — SSH via --remote; expect device 2FA) |
| `show sdwan-interface-profile` | remote | `panos_config_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show setting` | remote | `panos_config_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared admin-role` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared alg-override` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared alg-override application` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared authentication-profile` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared botnet` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared botnet configuration http` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared botnet configuration other-applications` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared botnet configuration unknown-applications` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared botnet configuration unknown-applications unknown-tcp session-length` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared botnet configuration unknown-applications unknown-udp session-length` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared certificate-profile` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared email-scheduler` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared local-user-database` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared local-user-database user` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared local-user-database user-group` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared log-settings` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared log-settings config` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared log-settings config match-list` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared log-settings email` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared log-settings http` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared log-settings profiles` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared log-settings snmptrap` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared log-settings syslog` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared log-settings system` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared log-settings system match-list` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared override` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared override application` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared pdf-summary-report` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared report-group` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared reports` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared response-page` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared scep` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared server-profile` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared server-profile kerberos` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared server-profile ldap` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared server-profile mfa-server-profile` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared server-profile netflow` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared server-profile radius` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared server-profile saml-idp` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared server-profile scp` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared server-profile tacplus` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared ssl-decrypt` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared ssl-decrypt forward-trust-certificate` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared ssl-decrypt forward-untrust-certificate` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared ssl-decrypt ssl-exclude-cert` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared ssl-tls-service-profile` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared user-id-hub` | remote | `panos_config_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show threats` | remote | `panos_config_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show threats spyware` | remote | `panos_config_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show threats vulnerability` | remote | `panos_config_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show ts-agent` | remote | `panos_config_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show url-admin-override` | remote | `panos_config_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show url-admin-override mode` | remote | `panos_config_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show user-context-segment` | remote | `panos_config_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show user-context-segment assignments` | remote | `panos_config_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show user-id-collector` | remote | `panos_config_user_id_collector` | (live device state — SSH via --remote; expect device 2FA) |
| `show user-id-collector include-exclude-network` | remote | `panos_config_user_id_collector` | (live device state — SSH via --remote; expect device 2FA) |
| `show user-id-collector include-exclude-network-sequence` | remote | `panos_config_user_id_collector` | (live device state — SSH via --remote; expect device 2FA) |
| `show user-id-collector server-monitor` | remote | `panos_config_user_id_collector` | (live device state — SSH via --remote; expect device 2FA) |
| `show user-id-collector setting` | remote | `panos_config_user_id_collector` | (live device state — SSH via --remote; expect device 2FA) |
| `show user-id-collector syslog-parse-profile` | remote | `panos_config_user_id_collector` | (live device state — SSH via --remote; expect device 2FA) |
| `show user-id-ssl-auth` | remote | `panos_config_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show vm-info-source` | remote | `panos_config_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show x-authenticated-user` | remote | `panos_config_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `validate full` | remote | `panos_config_validate` | (live device state — SSH via --remote; expect device 2FA) |
| `validate partial device-and-network` | remote | `panos_config_validate` | (live device state — SSH via --remote; expect device 2FA) |

## Panos-Ops

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `clear advanced-routing bfd counters session-id` | remote | `panos_clear_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `clear advanced-routing bfd session-state session-id` | remote | `panos_clear_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `clear advanced-routing bgp logical-router` | remote | `panos_clear_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `clear advanced-routing multicast igmp membership logical-router` | remote | `panos_clear_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `clear advanced-routing multicast igmp statistics logical-router` | remote | `panos_clear_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `clear advanced-routing multicast mroute logical-router` | remote | `panos_clear_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `clear advanced-routing multicast msdp sa logical-router` | remote | `panos_clear_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `clear advanced-routing multicast msdp statistics logical-router` | remote | `panos_clear_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `clear advanced-routing multicast pim statistics logical-router` | remote | `panos_clear_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `clear application-signature statistics` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear arp interface` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear audit-comment xpath` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear auto-tag vsys` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear bonjour interface` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear cluster-flow all` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear cluster-flow id` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear cookie-surrogate-cache all` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear cookie-surrogate-cache username` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear counter all` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear counter global filter category` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear counter global name` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear counter interface` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear device-cache-mp all` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear device-cache-mp ip` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear dhcp lease all expired-only` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear dhcp lease interface` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear dns-proxy cache all domain-name` | remote | `panos_clear_dns_proxy` | (live device state — SSH via --remote; expect device 2FA) |
| `clear dns-proxy cache name` | remote | `panos_clear_dns_proxy` | (live device state — SSH via --remote; expect device 2FA) |
| `clear dns-proxy dns-signature cache fqdn` | remote | `panos_clear_dns_proxy` | (live device state — SSH via --remote; expect device 2FA) |
| `clear dns-proxy dns-signature counters` | remote | `panos_clear_dns_proxy` | (live device state — SSH via --remote; expect device 2FA) |
| `clear dns-proxy encrypted-dns` | remote | `panos_clear_dns_proxy` | (live device state — SSH via --remote; expect device 2FA) |
| `clear dns-proxy statistics all` | remote | `panos_clear_dns_proxy` | (live device state — SSH via --remote; expect device 2FA) |
| `clear dns-proxy statistics name` | remote | `panos_clear_dns_proxy` | (live device state — SSH via --remote; expect device 2FA) |
| `clear dos-block-table all filter source-ip` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear dos-block-table drop-counter` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear dos-protection rule` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear dos-protection zone` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear global-protect redirect location` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear global-protect-portal statistics portal` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear high-availability cluster statistics` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear high-availability control-link statistics` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear high-availability transitions` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear job id` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear lacp counters aggregate-ethernet` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear lldp counters all` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear lldp counters interface` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear log` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear logrcvr offline-logpurger` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear mac` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear nat-rule-cache rule` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear neighbor interface` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear neighbor ndp-monitor` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear net-inspection filter` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear pbf return-mac all` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear pbf return-mac name` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear pbf rule all` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear pbf rule name` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear policy-app-usage-data ruleuuid` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear pppoe interface` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear pppoe ipv6 interface` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear query all-by-session` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear query id` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear report all-by-session` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear report cache` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear report id` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear resiliency statistics` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear routing bfd counters session-id` | remote | `panos_clear_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `clear routing bfd session-state session-id` | remote | `panos_clear_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `clear routing bgp virtual-router` | remote | `panos_clear_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `clear routing multicast igmp statistics virtual-router` | remote | `panos_clear_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `clear routing multicast pim statistics virtual-router` | remote | `panos_clear_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `clear rule-hit-count vsys` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear sdwan event` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear sdwan pool unsuccess` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear session all filter nat` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear snmpd refresh-timer-period` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear ssl-cert-cn` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear ssl-decrypt exclude-cache server` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear statistics` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear uappid-filtergroup-mapping all` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear uappid-filtergroup-mapping id` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear uappid-policy-cache all` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear uappid-policy-cache id` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear ueip address` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear ueip all` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear uid-cache all` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear uid-cache uid` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear uid-map-cache all` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear uid-map-cache uid` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear url-cache all` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear url-cache url` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear user-cache all type` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear user-cache ip` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear user-cache-mp all type` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear user-cache-mp ip` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear user-policy-cache all` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear user-policy-cache uid` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear vpn flow tunnel-id` | remote | `panos_clear_vpn` | (live device state — SSH via --remote; expect device 2FA) |
| `clear vpn ike-hashurl` | remote | `panos_clear_vpn` | (live device state — SSH via --remote; expect device 2FA) |
| `clear vpn ike-preferred-version gateway` | remote | `panos_clear_vpn` | (live device state — SSH via --remote; expect device 2FA) |
| `clear vpn ike-sa gateway` | remote | `panos_clear_vpn` | (live device state — SSH via --remote; expect device 2FA) |
| `clear vpn ipsec-sa tunnel` | remote | `panos_clear_vpn` | (live device state — SSH via --remote; expect device 2FA) |
| `clear wildfire counters` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear xml-api multiusersystem cloud` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `clear zone-protection zone` | remote | `panos_clear_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug advanced-routing` | remote | `panos_debug_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug advanced-routing bgp` | remote | `panos_debug_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug advanced-routing bgp updates in peer-name` | remote | `panos_debug_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug advanced-routing bgp updates out peer-name` | remote | `panos_debug_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug advanced-routing daemon-status logical-router` | remote | `panos_debug_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug advanced-routing fib check` | remote | `panos_debug_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug advanced-routing fib clear logical-router` | remote | `panos_debug_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug advanced-routing fib flush` | remote | `panos_debug_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug advanced-routing fib stats` | remote | `panos_debug_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug advanced-routing fqdn display logical-router` | remote | `panos_debug_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug advanced-routing global off` | remote | `panos_debug_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug advanced-routing global on` | remote | `panos_debug_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug advanced-routing global show` | remote | `panos_debug_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug advanced-routing mpf offload` | remote | `panos_debug_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug advanced-routing mpf stats` | remote | `panos_debug_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug advanced-routing ospfv3 logical-router` | remote | `panos_debug_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug advanced-routing path-monitor id` | remote | `panos_debug_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug advanced-routing pcap` | remote | `panos_debug_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug advanced-routing pcap show` | remote | `panos_debug_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug advanced-routing qtrace disable afi` | remote | `panos_debug_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug advanced-routing qtrace enable afi` | remote | `panos_debug_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug advanced-routing qtrace flush-log` | remote | `panos_debug_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug advanced-routing qtrace show afi` | remote | `panos_debug_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug advanced-routing restart` | remote | `panos_debug_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug advanced-routing zebra events enable` | remote | `panos_debug_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug advanced-routing zebra fpm enable` | remote | `panos_debug_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug advanced-routing zebra kernel msgdump logical-router` | remote | `panos_debug_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug advanced-routing zebra nht detailed` | remote | `panos_debug_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug advanced-routing zebra packet logical-router` | remote | `panos_debug_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug advanced-routing zebra rib detailed` | remote | `panos_debug_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug authentication` | remote | `panos_debug_authentication` | (live device state — SSH via --remote; expect device 2FA) |
| `debug authentication api-key-show key` | remote | `panos_debug_authentication` | (live device state — SSH via --remote; expect device 2FA) |
| `debug authentication connection-debug-off protocol-type` | remote | `panos_debug_authentication` | (live device state — SSH via --remote; expect device 2FA) |
| `debug authentication connection-debug-on protocol-type` | remote | `panos_debug_authentication` | (live device state — SSH via --remote; expect device 2FA) |
| `debug authentication connection-show protocol-type` | remote | `panos_debug_authentication` | (live device state — SSH via --remote; expect device 2FA) |
| `debug authentication on` | remote | `panos_debug_authentication` | (live device state — SSH via --remote; expect device 2FA) |
| `debug authentication set-tacacs-acct-task-q-size qsize` | remote | `panos_debug_authentication` | (live device state — SSH via --remote; expect device 2FA) |
| `debug authentication test-tacacs-acct-server-connection address` | remote | `panos_debug_authentication` | (live device state — SSH via --remote; expect device 2FA) |
| `debug bfd global off` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug bfd global on` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug bfd global show` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cli` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cloud-appid ace-server` | remote | `panos_debug_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cloud-appid cloud-manual-pull` | remote | `panos_debug_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cloud-appid delete-signature-data app-name` | remote | `panos_debug_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cloud-appid delete-signature-data appid` | remote | `panos_debug_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cloud-appid delete-signature-data filter-signature-id` | remote | `panos_debug_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cloud-appid dump config` | remote | `panos_debug_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cloud-appid keep-task-file` | remote | `panos_debug_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cloud-appid reset` | remote | `panos_debug_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cloud-appid reset signature-dp option` | remote | `panos_debug_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cloud-appid set config` | remote | `panos_debug_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cloud-appid unknown-signature-query app-name` | remote | `panos_debug_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cloud-appid unknown-signature-query appid` | remote | `panos_debug_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cloud-appid unknown-signature-query filter-sig-id` | remote | `panos_debug_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cloud-userid clear-cookie type` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cloud-userid reset-connection` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cloud-userid reset-counters` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug contentd status` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cord corr-mgr off` | remote | `panos_debug_cord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cord corr-mgr on` | remote | `panos_debug_cord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cord corr-mgr show back-query status` | remote | `panos_debug_cord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cord corr-mgr show brief` | remote | `panos_debug_cord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cord corr-mgr show failed` | remote | `panos_debug_cord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cord corr-mgr show filter search object` | remote | `panos_debug_cord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cord corr-mgr show instance search category` | remote | `panos_debug_cord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cord corr-mgr show instance summary` | remote | `panos_debug_cord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cord corr-mgr show object id` | remote | `panos_debug_cord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cord corr-mgr show object list` | remote | `panos_debug_cord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cord corr-mgr stats clear object` | remote | `panos_debug_cord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cord corr-mgr stats show object` | remote | `panos_debug_cord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cord delete db` | remote | `panos_debug_cord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cord delete events objectname` | remote | `panos_debug_cord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cord delete instances match` | remote | `panos_debug_cord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cord object-stats clear` | remote | `panos_debug_cord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cord object-stats set` | remote | `panos_debug_cord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cord object-stats show` | remote | `panos_debug_cord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cord object-stats show-setting` | remote | `panos_debug_cord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cord off` | remote | `panos_debug_cord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cord on` | remote | `panos_debug_cord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cord show` | remote | `panos_debug_cord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cord stats` | remote | `panos_debug_cord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cryptod clear hsm-key-cache` | remote | `panos_debug_cryptod` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cryptod global off` | remote | `panos_debug_cryptod` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cryptod global on` | remote | `panos_debug_cryptod` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cryptod global show` | remote | `panos_debug_cryptod` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cryptod show counters` | remote | `panos_debug_cryptod` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cryptod show hsm-thread all` | remote | `panos_debug_cryptod` | (live device state — SSH via --remote; expect device 2FA) |
| `debug cryptod show hsm-thread index` | remote | `panos_debug_cryptod` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane appinfo clear` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane cloud-appid lookup filter-sig-id` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane cloud-appid lookup global-id` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane cloud-appid lookup local-id` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane cloud-appid lookup name` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane cloud-appid reset cache all` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane cloud-appid reset cache appid` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane cloud-appid reset cache hash-slot` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane cloud-appid set report-overlap` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane cloud-appid show` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane cloud-appid show app-sig type` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane cloud-appid show cache` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane cloud-appid show database details` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane cloud-appid show detection` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane ctd-agent adns-telemetry debug` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane ctd-agent adns-telemetry debug-log` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane ctd-agent adns-telemetry freeze` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane ctd-agent adns-telemetry set interval-ms` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane ctd-agent adns-telemetry set max-cache-entry` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane ctd-agent adns-telemetry show` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane ctd-agent adns-telemetry stop` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane ctd-agent clear all` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane ctd-agent config` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane ctd-agent device-cert` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane ctd-agent global off` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane ctd-agent global on` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane ctd-agent global show` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane ctd-agent license` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane ctd-agent reset security-client` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane ctd-agent session id` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane ctd-agent set ace-debug` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane ctd-agent set cloud-trace` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane ctd-agent set host` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane ctd-agent set port` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane ctd-agent set source` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane flow-control disable slot` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane flow-control enable slot` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane flush-log` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane fpga hw_aho offload-bytes-threshold` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane fpga hw_aho offload-request-threshold` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane fpga hw_dfa offload-bytes-threshold` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane fpga hw_dfa offload-request-threshold` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane fpga set sw_aho` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane fpga set sw_dfa` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane fpga state` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt abort` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt bcm counters` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt bcm lport shaper get lport` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt bcm show congestion` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt bcm show flow flow_id` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt bcm show port` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt bcm show queue` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt ce10 cip` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt ce10 dfa` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt ce10 dxaui info instance` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt ce10 dxge info instance` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt ce10 dxge stats instance` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt ce10 pbm status instance` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt ce10 rd instance` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt ce10 show` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt ce10 show-all` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 acl dump count` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 csr` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 csr rd addr` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 csr scan regex` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 csr wr_sem_ctrl_ctr_scan_dis value` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 csr wr_sem_fcr_max_upd_thresh_cfg_pkt_ctr value` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 ddr eye intf` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 debug check` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 dphy_reg rd dcfg` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 event dump count` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 event fetch offset` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 flow ctrs` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 flow dump offset` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 flow histo` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 flow lookup saddr` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 flow tbl_size` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 lag dump count` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 lef dump count` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 lif access table` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 lif dump count` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 lif lookup table` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 lif stats clear` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 lif tbl_size` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 mac dump offset` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 mem rd target_mem` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 nexthop dump type` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 nif check_port` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 nif pkt_cap disable intf` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 nif pkt_cap display intf` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 nif pkt_cap enable intf` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 nif pkt_cap help` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 predict dump count` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 qmap dump pt` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 rd offset` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 route dump pt` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 show config` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 show fc clear` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 show intr` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 show latency` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 show stats` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 show stats port port` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 show status` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 tmi check_port` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 tmi pkt_cap disable intf` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 tmi pkt_cap display intf` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 tmi pkt_cap enable intf` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 tmi pkt_cap help` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 traffic info` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 umctl2_reg rd dcfg` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt fe100 vsys dump count` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt nac aho dump instance` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt nac dfa dump instance` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt nac info instance` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt nac show-all` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt nac stats instance` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt oct bgx config bgx` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt oct bgx status bgx` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt oct bootmem` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt oct csr rd reg` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt oct fpa show` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt oct gmx stats port` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt oct ilk` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt oct pip stats port` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt oct pki dump` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt oct pki port_config port` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt oct pki stats` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt oct pko debug port` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt oct pko stats all` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt oct pko stats port` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt oct pko3` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt oct portmap show` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt oct pow debug all` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal pdt pci list` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal vif` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane internal vif route` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane memory dump bootmem delete file` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane memory dump bootmem disable` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane memory dump bootmem enable log_disk_percent` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane memory dump bootmem show` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane memory status` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane mica reset cache` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane mica reset request-meta-cache adns` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane mica reset rtt` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane mica set cache adns` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane mica set cache default` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane mica set cache disable` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane mica set cache enable` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane mica set cache tp` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane mica set cache url` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane mica set inwf-mlav-prefilter` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane mica set mlc2-http-ldl-prefilter` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane mica set mlc2-micaflag-prefilter` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane mica set request-meta-cache adns` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane mica set telemetry adns-interval` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane mica show cache adns` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane mica show cache tp` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane mica show cache url` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane mica show config` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane mica show request-meta-cache adns entries` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane mica show rtt service` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane mmdbg leakiller memory-pool enable` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane mmdbg leakiller memory-pool show` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane mmdbg leakiller swbuf-pool enable` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane mmdbg leakiller swbuf-pool show` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane mmdbg obj-trace ev_num_per_q set` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane mmdbg obj-trace session level` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane mmdbg obj-trace shared-pool-192 level` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane mmdbg obj-trace shared-pool-24 level` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane mmdbg obj-trace stop` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane mmdbg obj-trace symbol lvl` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane mmdbg obj-trace wqe delay-free` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane mmdbg obj-trace wqe extra-trace` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane mmdbg obj-trace wqe leak-dump num` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane mmdbg obj-trace wqe level` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane mmdbg obj-trace wqe trace-type` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane mmdbg pool-debug overflow-check` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane mmdbg pool-debug reuse-check` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane mmdbg status` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane mmdbg watchpoint address s1dp0` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane monitor detail` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane nat static-mapping add from-ip` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane nat static-mapping del from-ip` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane nat static-mapping show` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane nat sync-ippool rule` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane netflow` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane oprofile opcontrol` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane oprofile opreport` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag aggregate-logs log_name` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag clear all` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag clear capture all` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag clear capture snaplen` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag clear capture stage` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag clear capture trigger` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag clear capture username` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag clear filter index` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag clear filter-marked-session all` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag clear filter-marked-session id` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag clear log counter` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag clear log feature` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag clear log feature all` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag clear log feature appid` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag clear log feature base` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag clear log feature cfg` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag clear log feature ctd` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag clear log feature flow` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag clear log feature misc` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag clear log feature module` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag clear log feature ssl` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag clear log feature tcp` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag clear log feature tdb` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag clear log feature tunnel` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag clear log feature url_trie` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag clear log log` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag set capture off` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag set capture on` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag set capture snaplen` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag set capture stage` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag set capture stage clientless-vpn-client file` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag set capture stage clientless-vpn-server file` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag set capture trigger application from` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag set capture username` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag set filter index` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag set filter match ingress-interface` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag set filter off` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag set filter offload` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag set filter on` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag set filter pre-parse-match` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag set filter-marked-session id` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag set log buffer-threshold` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag set log counter` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag set log cpu-threshold` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag set log feature` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag set log feature all` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag set log feature appid` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag set log feature base` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag set log feature cfg` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag set log feature ctd` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag set log feature flow` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag set log feature misc` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag set log feature module` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag set log feature ssl` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag set log feature tcp` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag set log feature tdb` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag set log feature tunnel` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag set log feature url_trie` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag set log log-option throttle` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag set log off` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag set log on` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag set log timeout` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag set tag` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-diag show` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-path-test counter` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane packet-path-test test proc` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane policy cache-usage-threshold` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane policy switch-cache` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane pool check hardware` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane pool check software` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane pool elastic delete profile name` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane pool elastic reset-defaults` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane pool elastic select-profile name` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane pool elastic set mode` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane pool elastic set profile name` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane pool elastic show config` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane pool elastic show profile active` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane pool elastic show profile all` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane pool elastic show profile capacity` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane pool elastic show profile name` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane pool mem file` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane pool memseg name common sz-pct` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane pool reset-max-usage` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane pool set` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane pool set off` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane pool set on name dthreat` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane pool set on name fptcp sessid-cid` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane pool set on name vcheck` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane pool show all top` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane pool show history top` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane pool show in-use top` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane pool statistics` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane pow performance all core` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane pow performance core` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane pow performance filter` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane pow performance rx_tx_ltncy` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane pow status filter worker` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane pow status global-counters pretty` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane pow status high-watermark reset` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane pow status inflightonly reset` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane pow status niconly brief` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane pow status niconly filter worker` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane pow status nonic reset` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane pow status nosleep filter worker` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane process` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane process cmd off` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane process cmd on` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane process cmd show` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane process comm off` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane process comm on` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane process comm profile-cache` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane process comm show` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane process mprelay off` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane process mprelay on` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane process mprelay show` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane process task dynamic-filter` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane process task off` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane process task on` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane process task show` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane pvst sys-id-ext-rewrite` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane reset` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane reset appid cache` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane reset appid statistics` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane reset appid unknown-cache destination` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane reset ctd` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane reset ctd dns-cache host` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane reset ctd feature-forward stats` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane reset ctd url-block-cache lockout` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane reset ctd wf-cache virus-pattern-type` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane reset dns-cache all` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane reset dns-cache fqdn` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane reset dos block-table` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane reset dos classification-table` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane reset dos rule` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane reset dos zone` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane reset ml-block-cache all` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane reset ml-block-cache url` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane reset ssl-decrypt` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane reset ssl-decrypt notify-cache source` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane set` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane set blocked-forward upload` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane set ctd autogen` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane set ctd ldl-model-enable` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane set ctd wildfire max` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane set ip6-mcast-fwd-check` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane set pbf-no-return-mac-learning` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane set pow no-desched` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane set qos-setting qos-param qlimit` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane set ssl-decrypt blk-send-reset` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane set ssl-decrypt ecdhe-aggressive-keying` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show app-filter-policy vsys` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show app-group-policy vsys` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show ctd` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show ctd credential-enforcement domain-credential` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show ctd credential-enforcement group-mapping vsys` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show ctd dns-cache entries host` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show ctd dns-cache stats` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show ctd feature-forward` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show ctd feature-forward forward-info session-id` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show ctd ldl status` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show ctd lscan app-sig type` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show ctd lscan database context prefix` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show ctd lscan database context-list` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show ctd lscan database details` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show ctd lscan sml-scope appid` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show ctd lscan sml-token appid` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show ctd regex-group dump` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show ctd regex-stats dump` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show ctd session` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show ctd threat id` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show ctd wf-cache virus-pattern-type` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show ctd wif service-mapping` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show ctd wildfire max` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show dns-cache print` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show dns-cache query fqdn` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show dns-cache statistics` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show dos block-table` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show dos classification-table` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show dos free-list` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show dos rule` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show dos zone` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show gtp session-qinfo` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show http2` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show http2 session` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show pow no-desched` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show qos-param qos-qlimit-sw` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show ssl-decrypt bitmask-cipher` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show ssl-decrypt bitmask-version` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show ssl-decrypt dns-cache` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show ssl-decrypt session` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show ssl-decrypt ssl-stats` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show uappid-filtergroup-mapping id` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show uappid-in-policy id` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show uappid-policy-cache uappid` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane show unknown-uappid-cache id` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane task-heartbeat` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane tcp state` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane test dump-nw-id-ebl-tble` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane test dump-nw-id-vsys-tble vsysid` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane test nat-policy-add from` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane test nat-policy-del from` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane test nw-id-lookup vsysid` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane test tunnel-tables` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane test uappid-filtergroup-mapping uappid` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane test uappid-policy-cache uappid` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane test url` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane test url-bloom` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dataplane test url-from-file max-per-sec` | remote | `panos_debug_dataplane` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server clear` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump app-containers name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump app-filters vsys` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump app-groups vsys` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump apps vsys` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump com` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump dynamic-address-group vsys` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump fqdn type dnat vsys` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump fqdn type pbf vsys` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump fqdn type policy vsys` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr global` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr high-availability state` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type dns-proxy all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type dns-proxy id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type dns-proxy name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type edl-domain all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type edl-domain id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type edl-domain name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type edl-ip all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type edl-ip id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type edl-ip name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type hip-profile all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type hip-profile id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type hip-profile name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type http-header-insert-header-value-l all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type http-header-insert-header-value-l id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type http-header-insert-header-value-l name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type http-header-insert-header-value-s all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type http-header-insert-header-value-s id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type http-header-insert-header-value-s name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type interface-group all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type interface-group id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type interface-group name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type macl-rule all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type macl-rule id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type macl-rule name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type monitor-tag all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type monitor-tag id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type monitor-tag name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type ospfv3-virtual-link all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type ospfv3-virtual-link id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type ospfv3-virtual-link name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type sdwan-link-tag all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type sdwan-link-tag id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type sdwan-link-tag name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type shared-app-signature all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type shared-app-signature id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type shared-app-signature name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type shared-application-filter all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type shared-application-filter id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type shared-application-filter name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type shared-application-group all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type shared-application-group id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type shared-application-group name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type shared-bgp-aggr-address all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type shared-bgp-aggr-address id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type shared-bgp-aggr-address name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type shared-bgp-peer all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type shared-bgp-peer id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type shared-bgp-peer name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type shared-bgp-peergrp all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type shared-bgp-peergrp id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type shared-bgp-peergrp name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type shared-qos-group all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type shared-qos-group id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type shared-qos-group name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type shared-region all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type shared-region id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type shared-region name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type shared-spyware all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type shared-spyware id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type shared-spyware name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type shared-url-filtering all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type shared-url-filtering id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type shared-url-filtering name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type tci-rule all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type tci-rule id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type tci-rule name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type vsys-app-signature all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type vsys-app-signature id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type vsys-app-signature name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type vsys-application-filter all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type vsys-application-filter id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type vsys-application-filter name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type vsys-application-group all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type vsys-application-group id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type vsys-application-group name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type vsys-region all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type vsys-region id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type vsys-region name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type vsys-spyware all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type vsys-spyware id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type vsys-spyware name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type vsys-url-filtering all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type vsys-url-filtering id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr redis type vsys-url-filtering name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type dns-proxy all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type dns-proxy id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type dns-proxy name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type edl-domain all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type edl-domain id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type edl-domain name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type edl-ip all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type edl-ip id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type edl-ip name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type hip-profile all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type hip-profile id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type hip-profile name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type http-header-insert-header-value-l all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type http-header-insert-header-value-l id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type http-header-insert-header-value-l name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type http-header-insert-header-value-s all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type http-header-insert-header-value-s id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type http-header-insert-header-value-s name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type interface-group all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type interface-group id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type interface-group name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type macl-rule all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type macl-rule id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type macl-rule name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type monitor-tag all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type monitor-tag id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type monitor-tag name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type ospfv3-virtual-link all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type ospfv3-virtual-link id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type ospfv3-virtual-link name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type sdwan-link-tag all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type sdwan-link-tag id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type sdwan-link-tag name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type shared-app-signature all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type shared-app-signature id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type shared-app-signature name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type shared-application-filter all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type shared-application-filter id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type shared-application-filter name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type shared-application-group all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type shared-application-group id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type shared-application-group name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type shared-bgp-aggr-address all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type shared-bgp-aggr-address id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type shared-bgp-aggr-address name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type shared-bgp-peer all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type shared-bgp-peer id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type shared-bgp-peer name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type shared-bgp-peergrp all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type shared-bgp-peergrp id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type shared-bgp-peergrp name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type shared-qos-group all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type shared-qos-group id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type shared-qos-group name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type shared-region all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type shared-region id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type shared-region name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type shared-spyware all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type shared-spyware id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type shared-spyware name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type shared-url-filtering all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type shared-url-filtering id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type shared-url-filtering name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type tci-rule all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type tci-rule id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type tci-rule name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type vsys-app-signature all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type vsys-app-signature id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type vsys-app-signature name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type vsys-application-filter all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type vsys-application-filter id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type vsys-application-filter name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type vsys-application-group all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type vsys-application-group id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type vsys-application-group name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type vsys-region all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type vsys-region id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type vsys-region name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type vsys-spyware all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type vsys-spyware id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type vsys-spyware name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type vsys-url-filtering all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type vsys-url-filtering id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump idmgr type vsys-url-filtering name` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump logging statistics` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump memory` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump ml7-idblob-flatbuf statistics` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump pan-url-db statistics` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump regips ip` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump regips iprange` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump regips summary` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump regips tag` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server dump tag-table tag` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server ldl show status` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server mlav clear-cache` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server mlav revert-model filetype-id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server mlav set-cloud-url default` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server mlav set-cloud-url url` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server off` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server on` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server pan-url-db` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server pan-url-db db-backup back-duration` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server pcap` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server pcap logical-router on logicalrouter` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server pcap virtual-router on virtualrouter` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server reset com statistics` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server reset config` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server reset id-manager type` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server reset logging statistics` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server set all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server set base` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server set config` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server set misc` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server set mlav` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server set tdb` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server set third-party` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server set url` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server set url_trie` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server set wfrt` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server show` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server test admin-override-password` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server test botnet-domain` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server test dynamic-url cloud` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server test idmgr-change-max type` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server test idmgr-change-max type global-router new-max-id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server test idmgr-change-max type shared-custom-url-category new-max-id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server test idmgr-change-max type ssl-rule new-max-id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server test idmgr-change-max type vsys-application new-max-id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server test idmgr-change-max type vsys-custom-url-category new-max-id` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server test idmgr-restore-default-max type` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server test ldl-model path` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server test ml7-blob path` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server test nw_id options` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server test url-category` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server trigger addrobjrefresh` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server unset all` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server unset base` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server unset config` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server unset misc` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server unset mlav` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server unset tdb` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server unset third-party` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server unset url` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server unset url_trie` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-server unset wfrt` | remote | `panos_debug_device_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug device-telemetry` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dhcpd cluster` | remote | `panos_debug_dhcpd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dhcpd downgrade convert-db` | remote | `panos_debug_dhcpd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dhcpd global off` | remote | `panos_debug_dhcpd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dhcpd global on` | remote | `panos_debug_dhcpd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dhcpd global show` | remote | `panos_debug_dhcpd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dhcpd high-availability ignore-config-sync` | remote | `panos_debug_dhcpd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dhcpd pcap` | remote | `panos_debug_dhcpd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dhcpd pcap logical-router on logicalrouter` | remote | `panos_debug_dhcpd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dhcpd pcap virtual-router on virtualrouter` | remote | `panos_debug_dhcpd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dhcpd show objects` | remote | `panos_debug_dhcpd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug distributord dump relay` | remote | `panos_debug_distributord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug distributord dump relay-ipc-iotd state` | remote | `panos_debug_distributord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug distributord dump relay-ipc-useridd` | remote | `panos_debug_distributord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug distributord hip-relay hip-report-dedup-cache-size set` | remote | `panos_debug_distributord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug distributord hip-relay hip-report-dedup-cache-size show` | remote | `panos_debug_distributord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug distributord hip-relay hip-report-in-cache-aging-interval set` | remote | `panos_debug_distributord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug distributord hip-relay hip-report-in-cache-aging-interval show` | remote | `panos_debug_distributord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug distributord hip-relay reset-hip-report-dedup-cache` | remote | `panos_debug_distributord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug distributord max-handle-concurrent-clients set` | remote | `panos_debug_distributord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug distributord max-handle-concurrent-clients show` | remote | `panos_debug_distributord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug distributord off` | remote | `panos_debug_distributord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug distributord on` | remote | `panos_debug_distributord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug distributord redis-connection-pool ip-user set` | remote | `panos_debug_distributord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug distributord redis-connection-pool ip-user show` | remote | `panos_debug_distributord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug distributord redis-connection-pool other-data-types enable` | remote | `panos_debug_distributord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug distributord redis-connection-pool other-data-types set` | remote | `panos_debug_distributord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug distributord redis-connection-pool other-data-types show` | remote | `panos_debug_distributord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug distributord relay relay-ipc-iotd set qsize` | remote | `panos_debug_distributord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug distributord relay relay-ipc-iotd set relay-iotd-recv-cache-qsize` | remote | `panos_debug_distributord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug distributord relay relay-ipc-iotd set relay-iotd-recv-read-batch-size` | remote | `panos_debug_distributord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug distributord relay relay-ipc-iotd show` | remote | `panos_debug_distributord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug distributord relay relay-ipc-useridd set qsize` | remote | `panos_debug_distributord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug distributord relay relay-ipc-useridd set relay-useridd-recv-cache-qsize` | remote | `panos_debug_distributord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug distributord relay relay-ipc-useridd set relay-useridd-recv-read-batch-size` | remote | `panos_debug_distributord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug distributord relay relay-ipc-useridd show` | remote | `panos_debug_distributord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug distributord relay relay-mode set-dcom-relay-mode-only` | remote | `panos_debug_distributord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug distributord relay relay-mode show-dcom-relay-mode` | remote | `panos_debug_distributord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug distributord reset redistribution-agent` | remote | `panos_debug_distributord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug distributord reset relay-statistics` | remote | `panos_debug_distributord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug distributord set agent` | remote | `panos_debug_distributord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug distributord set client` | remote | `panos_debug_distributord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug distributord set distribute` | remote | `panos_debug_distributord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug distributord set relay` | remote | `panos_debug_distributord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug distributord show` | remote | `panos_debug_distributord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug distributord test debug-log-category` | remote | `panos_debug_distributord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug distributord unset agent` | remote | `panos_debug_distributord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug distributord unset client` | remote | `panos_debug_distributord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug distributord unset distribute` | remote | `panos_debug_distributord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug distributord unset relay` | remote | `panos_debug_distributord` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dnsproxyd` | remote | `panos_debug_dnsproxyd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dnsproxyd clear cache-statistics` | remote | `panos_debug_dnsproxyd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dnsproxyd clear fqdn counters` | remote | `panos_debug_dnsproxyd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dnsproxyd clear sys-stats` | remote | `panos_debug_dnsproxyd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dnsproxyd dns-signature allow-list download` | remote | `panos_debug_dnsproxyd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dnsproxyd dns-signature cache fqdn` | remote | `panos_debug_dnsproxyd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dnsproxyd dns-signature counters` | remote | `panos_debug_dnsproxyd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dnsproxyd dns-signature info` | remote | `panos_debug_dnsproxyd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dnsproxyd dns-signature query bypass-cache` | remote | `panos_debug_dnsproxyd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dnsproxyd dns-signature query_n bypass-cache` | remote | `panos_debug_dnsproxyd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dnsproxyd dns-signature response fqdn` | remote | `panos_debug_dnsproxyd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dnsproxyd dns-signature response_n` | remote | `panos_debug_dnsproxyd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dnsproxyd dns-signature response_n fqdns` | remote | `panos_debug_dnsproxyd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dnsproxyd dns-signature response_n match-subdomains` | remote | `panos_debug_dnsproxyd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dnsproxyd dns-signature threat-info fqdn` | remote | `panos_debug_dnsproxyd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dnsproxyd dns-signature ut threat-info-api api-query-domain fqdn` | remote | `panos_debug_dnsproxyd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dnsproxyd fqdn counters delta` | remote | `panos_debug_dnsproxyd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dnsproxyd fqdn dump brief` | remote | `panos_debug_dnsproxyd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dnsproxyd global off` | remote | `panos_debug_dnsproxyd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dnsproxyd global on` | remote | `panos_debug_dnsproxyd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dnsproxyd global show` | remote | `panos_debug_dnsproxyd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug dnsproxyd show` | remote | `panos_debug_dnsproxyd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug evtmgr` | remote | `panos_debug_evtmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug evtmgr ms` | remote | `panos_debug_evtmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug evtmgr ms debug-log clfy` | remote | `panos_debug_evtmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug evtmgr ms debug-log client` | remote | `panos_debug_evtmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug evtmgr ms debug-log msg` | remote | `panos_debug_evtmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug evtmgr ms debug-log multicast` | remote | `panos_debug_evtmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug evtmgr ms msg-filter msg-class` | remote | `panos_debug_evtmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug evtmgr ms show basic` | remote | `panos_debug_evtmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug evtmgr ms show client-id` | remote | `panos_debug_evtmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug evtmgr ms show detail` | remote | `panos_debug_evtmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug evtmgr ms syslog-enabled` | remote | `panos_debug_evtmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug external-list delete-file all` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug external-list delete-file type domain name` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug external-list delete-file type ip name` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug external-list delete-file type url name` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug global-protect hip set-dp-query-interval` | remote | `panos_debug_global_protect` | (live device state — SSH via --remote; expect device 2FA) |
| `debug global-protect hip show-dp-query-interval` | remote | `panos_debug_global_protect` | (live device state — SSH via --remote; expect device 2FA) |
| `debug global-protect portal clientlessvpn gzip-encoding` | remote | `panos_debug_global_protect` | (live device state — SSH via --remote; expect device 2FA) |
| `debug global-protect portal clientlessvpn host-match-referer` | remote | `panos_debug_global_protect` | (live device state — SSH via --remote; expect device 2FA) |
| `debug global-protect portal interval` | remote | `panos_debug_global_protect` | (live device state — SSH via --remote; expect device 2FA) |
| `debug global-protect portal off` | remote | `panos_debug_global_protect` | (live device state — SSH via --remote; expect device 2FA) |
| `debug global-protect portal on` | remote | `panos_debug_global_protect` | (live device state — SSH via --remote; expect device 2FA) |
| `debug global-protect portal show` | remote | `panos_debug_global_protect` | (live device state — SSH via --remote; expect device 2FA) |
| `debug gp-broker gpsvc key-value` | remote | `panos_debug_gp_broker` | (live device state — SSH via --remote; expect device 2FA) |
| `debug gp-broker gpsvc reload-template` | remote | `panos_debug_gp_broker` | (live device state — SSH via --remote; expect device 2FA) |
| `debug gp-broker gpsvc reset counter` | remote | `panos_debug_gp_broker` | (live device state — SSH via --remote; expect device 2FA) |
| `debug gp-broker gpsvc reset key-value` | remote | `panos_debug_gp_broker` | (live device state — SSH via --remote; expect device 2FA) |
| `debug gp-broker gpsvc task` | remote | `panos_debug_gp_broker` | (live device state — SSH via --remote; expect device 2FA) |
| `debug gp-broker gpsvc test rpc api-name` | remote | `panos_debug_gp_broker` | (live device state — SSH via --remote; expect device 2FA) |
| `debug gp-broker gpsvc trace add user` | remote | `panos_debug_gp_broker` | (live device state — SSH via --remote; expect device 2FA) |
| `debug gp-broker gpsvc trace clear` | remote | `panos_debug_gp_broker` | (live device state — SSH via --remote; expect device 2FA) |
| `debug gp-broker gpsvc trace delete user` | remote | `panos_debug_gp_broker` | (live device state — SSH via --remote; expect device 2FA) |
| `debug gp-broker gpsvc trace global-log` | remote | `panos_debug_gp_broker` | (live device state — SSH via --remote; expect device 2FA) |
| `debug gp-broker gpsvc trace show` | remote | `panos_debug_gp_broker` | (live device state — SSH via --remote; expect device 2FA) |
| `debug gp-broker off` | remote | `panos_debug_gp_broker` | (live device state — SSH via --remote; expect device 2FA) |
| `debug gp-broker on` | remote | `panos_debug_gp_broker` | (live device state — SSH via --remote; expect device 2FA) |
| `debug gp-broker show` | remote | `panos_debug_gp_broker` | (live device state — SSH via --remote; expect device 2FA) |
| `debug high-availability` | remote | `panos_debug_high_availability` | (live device state — SSH via --remote; expect device 2FA) |
| `debug high-availability flap-interface interface` | remote | `panos_debug_high_availability` | (live device state — SSH via --remote; expect device 2FA) |
| `debug high-availability knob set encrypt-init-hold-time` | remote | `panos_debug_high_availability` | (live device state — SSH via --remote; expect device 2FA) |
| `debug high-availability knob set init-hold-time` | remote | `panos_debug_high_availability` | (live device state — SSH via --remote; expect device 2FA) |
| `debug high-availability knob show` | remote | `panos_debug_high_availability` | (live device state — SSH via --remote; expect device 2FA) |
| `debug high-availability on` | remote | `panos_debug_high_availability` | (live device state — SSH via --remote; expect device 2FA) |
| `debug ifmgr dump-detail-history port` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug ifmgr dump-history port` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug ifmgr dump-portdb` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug ifmgr pstate port` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug ike gateway` | remote | `panos_debug_ike` | (live device state — SSH via --remote; expect device 2FA) |
| `debug ike global off` | remote | `panos_debug_ike` | (live device state — SSH via --remote; expect device 2FA) |
| `debug ike global on` | remote | `panos_debug_ike` | (live device state — SSH via --remote; expect device 2FA) |
| `debug ike global show` | remote | `panos_debug_ike` | (live device state — SSH via --remote; expect device 2FA) |
| `debug ike pcap` | remote | `panos_debug_ike` | (live device state — SSH via --remote; expect device 2FA) |
| `debug ike socket` | remote | `panos_debug_ike` | (live device state — SSH via --remote; expect device 2FA) |
| `debug ike stat` | remote | `panos_debug_ike` | (live device state — SSH via --remote; expect device 2FA) |
| `debug ike stat fqdn name` | remote | `panos_debug_ike` | (live device state — SSH via --remote; expect device 2FA) |
| `debug ike stat ipsec counter` | remote | `panos_debug_ike` | (live device state — SSH via --remote; expect device 2FA) |
| `debug ike stat isakmp counter` | remote | `panos_debug_ike` | (live device state — SSH via --remote; expect device 2FA) |
| `debug ike stat sched filter gwid` | remote | `panos_debug_ike` | (live device state — SSH via --remote; expect device 2FA) |
| `debug ike tunnel` | remote | `panos_debug_ike` | (live device state — SSH via --remote; expect device 2FA) |
| `debug iot clear-all type` | remote | `panos_debug_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `debug iot disable-device-id` | remote | `panos_debug_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `debug iot dump relay` | remote | `panos_debug_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `debug iot dump relay-ipc-distributord state` | remote | `panos_debug_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `debug iot eal cortex-server` | remote | `panos_debug_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `debug iot eal key-value` | remote | `panos_debug_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `debug iot eal on` | remote | `panos_debug_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `debug iot eal reset aggregation-non-ack` | remote | `panos_debug_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `debug iot eal reset aggregation-num` | remote | `panos_debug_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `debug iot eal reset connection` | remote | `panos_debug_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `debug iot eal reset counter` | remote | `panos_debug_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `debug iot eal reset key-value` | remote | `panos_debug_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `debug iot eal sending-format` | remote | `panos_debug_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `debug iot eal test load-dpi` | remote | `panos_debug_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `debug iot eal track` | remote | `panos_debug_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `debug iot eal track filter add subtype` | remote | `panos_debug_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `debug iot eal track filter clear` | remote | `panos_debug_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `debug iot eal track filter show` | remote | `panos_debug_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `debug iot eal validate-dpi` | remote | `panos_debug_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `debug iot global counter` | remote | `panos_debug_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `debug iot global off` | remote | `panos_debug_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `debug iot global on` | remote | `panos_debug_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `debug iot global show` | remote | `panos_debug_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `debug iot icd key-value` | remote | `panos_debug_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `debug iot icd on` | remote | `panos_debug_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `debug iot icd reset connection` | remote | `panos_debug_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `debug iot icd reset cookie` | remote | `panos_debug_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `debug iot icd reset key-value` | remote | `panos_debug_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `debug iot icd set-app-match-workers` | remote | `panos_debug_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `debug iot icd trigger-app-match` | remote | `panos_debug_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `debug iot icd verdict-server` | remote | `panos_debug_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `debug iot memory` | remote | `panos_debug_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `debug iot relay-ipc-distributord set qsize` | remote | `panos_debug_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `debug iot relay-ipc-distributord set relay-distd-recv-cache-qsize` | remote | `panos_debug_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `debug iot relay-ipc-distributord set relay-distd-recv-read-batch-size` | remote | `panos_debug_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `debug iot relay-ipc-distributord show` | remote | `panos_debug_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `debug keymgr gateway id` | remote | `panos_debug_keymgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug keymgr global off` | remote | `panos_debug_keymgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug keymgr global on` | remote | `panos_debug_keymgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug keymgr global show` | remote | `panos_debug_keymgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug keymgr list-sa` | remote | `panos_debug_keymgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug keymgr queue` | remote | `panos_debug_keymgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug keymgr socket` | remote | `panos_debug_keymgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug keymgr tunnel id` | remote | `panos_debug_keymgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug l2ctrld global off` | remote | `panos_debug_l2ctrld` | (live device state — SSH via --remote; expect device 2FA) |
| `debug l2ctrld global on` | remote | `panos_debug_l2ctrld` | (live device state — SSH via --remote; expect device 2FA) |
| `debug l2ctrld global show` | remote | `panos_debug_l2ctrld` | (live device state — SSH via --remote; expect device 2FA) |
| `debug l2ctrld lacp off` | remote | `panos_debug_l2ctrld` | (live device state — SSH via --remote; expect device 2FA) |
| `debug l2ctrld lacp on` | remote | `panos_debug_l2ctrld` | (live device state — SSH via --remote; expect device 2FA) |
| `debug l2ctrld lacp set hold-time aggregate-ethernet` | remote | `panos_debug_l2ctrld` | (live device state — SSH via --remote; expect device 2FA) |
| `debug l2ctrld lacp show` | remote | `panos_debug_l2ctrld` | (live device state — SSH via --remote; expect device 2FA) |
| `debug l2ctrld lldp delete neighbor` | remote | `panos_debug_l2ctrld` | (live device state — SSH via --remote; expect device 2FA) |
| `debug l2ctrld lldp off` | remote | `panos_debug_l2ctrld` | (live device state — SSH via --remote; expect device 2FA) |
| `debug l2ctrld lldp on` | remote | `panos_debug_l2ctrld` | (live device state — SSH via --remote; expect device 2FA) |
| `debug l2ctrld lldp pcap` | remote | `panos_debug_l2ctrld` | (live device state — SSH via --remote; expect device 2FA) |
| `debug l2ctrld lldp pcap logical-router on logicalrouter` | remote | `panos_debug_l2ctrld` | (live device state — SSH via --remote; expect device 2FA) |
| `debug l2ctrld lldp pcap virtual-router on virtualrouter` | remote | `panos_debug_l2ctrld` | (live device state — SSH via --remote; expect device 2FA) |
| `debug l2ctrld lldp set stagger-limit` | remote | `panos_debug_l2ctrld` | (live device state — SSH via --remote; expect device 2FA) |
| `debug l2ctrld lldp show` | remote | `panos_debug_l2ctrld` | (live device state — SSH via --remote; expect device 2FA) |
| `debug l3svc captive-portal kerberos-timeout interval` | remote | `panos_debug_l3svc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug l3svc captive-portal kerberos-timeout off` | remote | `panos_debug_l3svc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug l3svc captive-portal kerberos-timeout on` | remote | `panos_debug_l3svc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug l3svc captive-portal kerberos-timeout show` | remote | `panos_debug_l3svc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug l3svc clear` | remote | `panos_debug_l3svc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug l3svc off` | remote | `panos_debug_l3svc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug l3svc on` | remote | `panos_debug_l3svc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug l3svc pcap` | remote | `panos_debug_l3svc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug l3svc pcap logical-router on logicalrouter` | remote | `panos_debug_l3svc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug l3svc pcap virtual-router on virtualrouter` | remote | `panos_debug_l3svc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug l3svc reset user-cache` | remote | `panos_debug_l3svc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug l3svc show user-cache` | remote | `panos_debug_l3svc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug list-admin-history` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug list-blocked-partial-xpaths` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-output-need-utf8` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver container-page entries` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver container-page off` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver container-page on` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver container-page timeout` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver contmgr status` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver corr-mgr off` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver corr-mgr on` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver corr-mgr show back-query status` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver corr-mgr show brief` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver corr-mgr show failed` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver corr-mgr show filter search object` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver corr-mgr show instance search category` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver corr-mgr show instance summary` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver corr-mgr show object id` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver corr-mgr show object list` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver corr-mgr stats clear object` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver corr-mgr stats show object` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver correlation filters show` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver correlation stats show` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver counters filter delta` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver dag always-include-dag` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver dag disable-dag-logging` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver dag dump dag-id vsysid` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver dag dump id-dag dag-idx` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver dag dump ip-dag ip` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver dag dump rule-dag rule_uuid` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver dag off` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver dag on` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver dag show` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver dpi dump clear` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver dpi dump format` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver dpi dump off` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver dpi dump on` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver dump users all` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver dump users id` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver dumplog off` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver dumplog on count` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver edl disable-edl-logging` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver edl dump edl-id vsysid` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver edl dump id-edl edl-idx` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver edl dump ip-edl ip` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver edl dump rule-edl rule_uuid` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver edl off` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver edl on` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver edl show` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver fwd` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver ip-cache clear node-data vsysid` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver ip-cache clear vsys-data vsysid` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver log-flow counters` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver log-flow trace show` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver log-forwarding per-second-stats` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver log-forwarding status` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver log-forwarding-connections per-second-stats` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver log-forwarding-connections status` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver log-purger debug` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver logdb-writer-stats latest` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver memory info verbose` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver memory per-second-stats` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver memory trim` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver netflow` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver on` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver param-tuning rollup` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver param-tuning syslog-threads show` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver param-tuning syslog-threads size` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver param-tuning task-queue show` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver param-tuning task-queue size` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver per-second-stats off` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver per-second-stats on` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver rawlog_fwd clear hints-all` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver rawlog_fwd off` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver rawlog_fwd on` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver rawlog_fwd set hints-expiration-duration` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver rawlog_fwd set hints-max` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver rawlog_fwd show` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver rawlog_fwd show connmgr verbose` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver rawlog_fwd stats global clear` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver rawlog_fwd stats global show verbose` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver rawlog_fwd stats per-lc` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver rawlog_fwd_trial connmgr` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver rawlog_fwd_trial evtmgr` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver rawlog_fwd_trial stats global show verbose` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug log-receiver telemetry-triggers` | remote | `panos_debug_log_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug logdb-usage` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug logview role` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type edl-domain all` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type edl-domain id` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type edl-domain name` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type edl-ip all` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type edl-ip id` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type edl-ip name` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type hip-profile all` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type hip-profile id` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type hip-profile name` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type interface-group all` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type interface-group id` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type interface-group name` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type macl-rule all` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type macl-rule id` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type macl-rule name` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type ospfv3-virtual-link all` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type ospfv3-virtual-link id` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type ospfv3-virtual-link name` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type sdwan-link-tag all` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type sdwan-link-tag id` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type sdwan-link-tag name` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type shared-app-signature all` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type shared-app-signature id` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type shared-app-signature name` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type shared-bgp-aggr-address all` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type shared-bgp-aggr-address id` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type shared-bgp-aggr-address name` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type shared-bgp-peer all` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type shared-bgp-peer id` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type shared-bgp-peer name` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type shared-bgp-peergrp all` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type shared-bgp-peergrp id` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type shared-bgp-peergrp name` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type shared-qos-group all` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type shared-qos-group id` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type shared-qos-group name` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type shared-region all` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type shared-region id` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type shared-region name` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type shared-spyware all` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type shared-spyware id` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type shared-spyware name` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type shared-url-filtering all` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type shared-url-filtering id` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type shared-url-filtering name` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type tci-rule all` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type tci-rule id` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type tci-rule name` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type vsys-app-signature all` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type vsys-app-signature id` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type vsys-app-signature name` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type vsys-region all` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type vsys-region id` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type vsys-region name` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type vsys-spyware all` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type vsys-spyware id` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type vsys-spyware name` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type vsys-url-filtering all` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type vsys-url-filtering id` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd dump idmgr type vsys-url-filtering name` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug lpmgrd status` | remote | `panos_debug_lpmgrd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug macsec global off` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug macsec global on` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug macsec global show` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug macsec pcap` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-interface dhcp client debug` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-interface dhcp client log` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server app-config-trigger` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server autofocus` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server client disable` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server client enable` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server configd-mem` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server contmgr status` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server corr-mgr off` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server corr-mgr on` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server corr-mgr show back-query status` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server corr-mgr show brief` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server corr-mgr show failed` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server corr-mgr show filter search object` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server corr-mgr show instance search category` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server corr-mgr show instance summary` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server corr-mgr show object id` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server corr-mgr show object list` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server corr-mgr stats clear object` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server corr-mgr stats show object` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server db-intervals start-time` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server db-rollup` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server device-monitoring enable` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server dg-ctxt vsys` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server disable-cms-conn-check` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server last-candidatecfg-audit diff base-version` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server last-candidatecfg-audit info` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server last-candidatecfg-audit show version` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server log-forwarding-congestion-ctrl set` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server log-forwarding-congestion-ctrl show` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server max-config-size set size` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server max-config-size show` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server memory` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server ml7 anti-virus install` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server ml7 content install` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server ml7 iot install` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server on` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server req-stats` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server rolledup-intervals start-time` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server rule-hit` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server secure-conn set scep-cert-renewal-time` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server secure-conn set scep-cert-retry-on-failure-interval` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server secure-conn show ha config file` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server secure-conn show mgmt config file` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server secure-conn show mgmt detail` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server secure-conn show scep-cert-renewal-time` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server secure-conn show scep-cert-retry-on-failure-interval` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server set` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server set all` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server snmp-memory-map` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server telemetry-triggers correlated-threat-log-limit` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server telemetry-triggers counters` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server telemetry-triggers per-signature-limit` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server telemetry-triggers raw-threat-log-limit` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server telemetry-triggers related-threat-log-limit` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server template dump-config from` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server toggle-ui-notification` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server unified-log` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server unset` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server unset all` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server user bitmap` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server user info name` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-server vld stats cc` | remote | `panos_debug_management_server` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-websrvr backend off` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-websrvr backend on` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug management-websrvr backend show` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug md-service internal-dump` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug md-service off` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug md-service on` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug md-service show` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug mprelay off` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug mprelay on` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug mprelay show` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug net-inspection packet-limit` | remote | `panos_debug_net_inspection` | (live device state — SSH via --remote; expect device 2FA) |
| `debug net-inspection reset` | remote | `panos_debug_net_inspection` | (live device state — SSH via --remote; expect device 2FA) |
| `debug net-inspection show` | remote | `panos_debug_net_inspection` | (live device state — SSH via --remote; expect device 2FA) |
| `debug net-inspection trace` | remote | `panos_debug_net_inspection` | (live device state — SSH via --remote; expect device 2FA) |
| `debug net-inspection trace-limit` | remote | `panos_debug_net_inspection` | (live device state — SSH via --remote; expect device 2FA) |
| `debug netconfig-agent off` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug netconfig-agent on` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug netconfig-agent show` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug object registered-ip` | remote | `panos_debug_object` | (live device state — SSH via --remote; expect device 2FA) |
| `debug object registered-ip clear all source-name` | remote | `panos_debug_object` | (live device state — SSH via --remote; expect device 2FA) |
| `debug object registered-ip redis-entry ip` | remote | `panos_debug_object` | (live device state — SSH via --remote; expect device 2FA) |
| `debug object registered-ip redis-entry iprange` | remote | `panos_debug_object` | (live device state — SSH via --remote; expect device 2FA) |
| `debug object registered-ip show tag-source tag` | remote | `panos_debug_object` | (live device state — SSH via --remote; expect device 2FA) |
| `debug object registered-ip test cuid-upload` | remote | `panos_debug_object` | (live device state — SSH via --remote; expect device 2FA) |
| `debug object registered-ip test download` | remote | `panos_debug_object` | (live device state — SSH via --remote; expect device 2FA) |
| `debug object registered-ip test download-mode` | remote | `panos_debug_object` | (live device state — SSH via --remote; expect device 2FA) |
| `debug object registered-ip test register tag` | remote | `panos_debug_object` | (live device state — SSH via --remote; expect device 2FA) |
| `debug object registered-ip test unregister tag` | remote | `panos_debug_object` | (live device state — SSH via --remote; expect device 2FA) |
| `debug object registered-user clear all tag-source` | remote | `panos_debug_object` | (live device state — SSH via --remote; expect device 2FA) |
| `debug object registered-user show tag-source user` | remote | `panos_debug_object` | (live device state — SSH via --remote; expect device 2FA) |
| `debug object registered-user test cuid-upload` | remote | `panos_debug_object` | (live device state — SSH via --remote; expect device 2FA) |
| `debug object registered-user test register user` | remote | `panos_debug_object` | (live device state — SSH via --remote; expect device 2FA) |
| `debug object registered-user test unregister user` | remote | `panos_debug_object` | (live device state — SSH via --remote; expect device 2FA) |
| `debug online diagnostics get execution-time` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug online diagnostics run` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug pancfg-directory-usage clean config saved` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug pancfg-directory-usage clean dynamic-updates anti-virus update` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug pancfg-directory-usage clean dynamic-updates content update` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug pancfg-directory-usage clean software-images version` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug pppoed global off` | remote | `panos_debug_pppoed` | (live device state — SSH via --remote; expect device 2FA) |
| `debug pppoed global on` | remote | `panos_debug_pppoed` | (live device state — SSH via --remote; expect device 2FA) |
| `debug pppoed global show` | remote | `panos_debug_pppoed` | (live device state — SSH via --remote; expect device 2FA) |
| `debug pppoed pcap` | remote | `panos_debug_pppoed` | (live device state — SSH via --remote; expect device 2FA) |
| `debug pppoed pcap on file_size` | remote | `panos_debug_pppoed` | (live device state — SSH via --remote; expect device 2FA) |
| `debug pppoed show config` | remote | `panos_debug_pppoed` | (live device state — SSH via --remote; expect device 2FA) |
| `debug pppoed show interface` | remote | `panos_debug_pppoed` | (live device state — SSH via --remote; expect device 2FA) |
| `debug predefined-report-default` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug preserve-prenat feature show` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug proxy discard-partial-client-hello enable` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug proxy discard-partial-client-hello show` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug proxy fast-session-delete enable` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug proxy-protocol debug-level` | remote | `panos_debug_proxy_protocol` | (live device state — SSH via --remote; expect device 2FA) |
| `debug proxy-protocol debug-mode normal` | remote | `panos_debug_proxy_protocol` | (live device state — SSH via --remote; expect device 2FA) |
| `debug proxy-protocol debug-mode session-limit` | remote | `panos_debug_proxy_protocol` | (live device state — SSH via --remote; expect device 2FA) |
| `debug proxy-protocol debug-mode trace-limit` | remote | `panos_debug_proxy_protocol` | (live device state — SSH via --remote; expect device 2FA) |
| `debug proxy-protocol feature enabled` | remote | `panos_debug_proxy_protocol` | (live device state — SSH via --remote; expect device 2FA) |
| `debug proxy-protocol feature hostid-subtlv-type` | remote | `panos_debug_proxy_protocol` | (live device state — SSH via --remote; expect device 2FA) |
| `debug proxy-protocol feature show` | remote | `panos_debug_proxy_protocol` | (live device state — SSH via --remote; expect device 2FA) |
| `debug proxy-protocol feature userid-subtlv-type` | remote | `panos_debug_proxy_protocol` | (live device state — SSH via --remote; expect device 2FA) |
| `debug proxy-protocol packet-dump-max-bytes` | remote | `panos_debug_proxy_protocol` | (live device state — SSH via --remote; expect device 2FA) |
| `debug rasmgr delay-nh-update` | remote | `panos_debug_rasmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug rasmgr delay-nh-update reset` | remote | `panos_debug_rasmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug rasmgr gateway` | remote | `panos_debug_rasmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug rasmgr ippool reset-all` | remote | `panos_debug_rasmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug rasmgr off` | remote | `panos_debug_rasmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug rasmgr on` | remote | `panos_debug_rasmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug rasmgr satellite` | remote | `panos_debug_rasmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug rasmgr show` | remote | `panos_debug_rasmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug rasmgr src-ip-trie gateway-name` | remote | `panos_debug_rasmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug rasmgr statistics` | remote | `panos_debug_rasmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug rasmgr user` | remote | `panos_debug_rasmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug rawlog_fwd enable` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug reportd contmgr status` | remote | `panos_debug_reportd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug reportd corr-mgr off` | remote | `panos_debug_reportd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug reportd corr-mgr on` | remote | `panos_debug_reportd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug reportd corr-mgr show back-query status` | remote | `panos_debug_reportd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug reportd corr-mgr show brief` | remote | `panos_debug_reportd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug reportd corr-mgr show failed` | remote | `panos_debug_reportd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug reportd corr-mgr show filter search object` | remote | `panos_debug_reportd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug reportd corr-mgr show instance search category` | remote | `panos_debug_reportd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug reportd corr-mgr show instance summary` | remote | `panos_debug_reportd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug reportd corr-mgr show object id` | remote | `panos_debug_reportd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug reportd corr-mgr show object list` | remote | `panos_debug_reportd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug reportd corr-mgr stats clear object` | remote | `panos_debug_reportd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug reportd corr-mgr stats show object` | remote | `panos_debug_reportd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug reportd off` | remote | `panos_debug_reportd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug reportd on` | remote | `panos_debug_reportd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug reportd schedule-reports` | remote | `panos_debug_reportd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug reportd send-request-to-7k` | remote | `panos_debug_reportd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug reportd set-timeout` | remote | `panos_debug_reportd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug reportd show` | remote | `panos_debug_reportd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug routing` | remote | `panos_debug_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug routing dctrace both enable` | remote | `panos_debug_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug routing dctrace ips enable` | remote | `panos_debug_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug routing dctrace pd enable` | remote | `panos_debug_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug routing dctrace show` | remote | `panos_debug_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug routing fib clear virtual-router` | remote | `panos_debug_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug routing fib flush` | remote | `panos_debug_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug routing fib stats` | remote | `panos_debug_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug routing fqdn display virtual-router` | remote | `panos_debug_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug routing global off` | remote | `panos_debug_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug routing global on` | remote | `panos_debug_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug routing global show` | remote | `panos_debug_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug routing mib` | remote | `panos_debug_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug routing mpf offload` | remote | `panos_debug_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug routing mpf stats` | remote | `panos_debug_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug routing path-monitor id` | remote | `panos_debug_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug routing pcap` | remote | `panos_debug_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug routing pcap show` | remote | `panos_debug_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug routing qtrace disable afi` | remote | `panos_debug_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug routing qtrace enable afi` | remote | `panos_debug_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug routing qtrace flush-log` | remote | `panos_debug_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug routing qtrace show afi` | remote | `panos_debug_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `debug run-panorama-predefined-report` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug satd dump certificate-pool global` | remote | `panos_debug_satd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug satd dump certificate-pool satellite` | remote | `panos_debug_satd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug satd failed-refresh-timeout satellite name` | remote | `panos_debug_satd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug satd off` | remote | `panos_debug_satd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug satd on` | remote | `panos_debug_satd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug satd show` | remote | `panos_debug_satd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug satd statistics` | remote | `panos_debug_satd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sdwand clear all` | remote | `panos_debug_sdwand` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sdwand event-log filter delete all` | remote | `panos_debug_sdwand` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sdwand event-log filter delete idx` | remote | `panos_debug_sdwand` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sdwand event-log filter off` | remote | `panos_debug_sdwand` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sdwand event-log filter on` | remote | `panos_debug_sdwand` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sdwand event-log filter set index` | remote | `panos_debug_sdwand` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sdwand event-log filter set match ingress-interface` | remote | `panos_debug_sdwand` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sdwand event-log filter show` | remote | `panos_debug_sdwand` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sdwand feature show` | remote | `panos_debug_sdwand` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sdwand global off` | remote | `panos_debug_sdwand` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sdwand global on` | remote | `panos_debug_sdwand` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sdwand global show` | remote | `panos_debug_sdwand` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sdwand path-monitor disable all` | remote | `panos_debug_sdwand` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sdwand path-monitor disable tunnel-id` | remote | `panos_debug_sdwand` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sdwand path-monitor enable all` | remote | `panos_debug_sdwand` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sdwand path-monitor enable tunnel-id` | remote | `panos_debug_sdwand` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sdwand saas branch interval` | remote | `panos_debug_sdwand` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sdwand saas hub interval` | remote | `panos_debug_sdwand` | (live device state — SSH via --remote; expect device 2FA) |
| `debug set-content-download-retry attempts` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug snmpd async` | remote | `panos_debug_snmpd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug snmpd clear_persistence` | remote | `panos_debug_snmpd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug snmpd off` | remote | `panos_debug_snmpd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug snmpd on debug` | remote | `panos_debug_snmpd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug snmpd sysd-disable-retry` | remote | `panos_debug_snmpd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug snmpd sysd-timeout` | remote | `panos_debug_snmpd` | (live device state — SSH via --remote; expect device 2FA) |
| `debug software` | remote | `panos_debug_software` | (live device state — SSH via --remote; expect device 2FA) |
| `debug software core` | remote | `panos_debug_software` | (live device state — SSH via --remote; expect device 2FA) |
| `debug software disk-usage aggressive-cleaning` | remote | `panos_debug_software` | (live device state — SSH via --remote; expect device 2FA) |
| `debug software disk-usage cleanup threshold` | remote | `panos_debug_software` | (live device state — SSH via --remote; expect device 2FA) |
| `debug software disk-usage dagger-fds-cleaning` | remote | `panos_debug_software` | (live device state — SSH via --remote; expect device 2FA) |
| `debug software disk-usage dangling-fds target-name` | remote | `panos_debug_software` | (live device state — SSH via --remote; expect device 2FA) |
| `debug software fd-limit service` | remote | `panos_debug_software` | (live device state — SSH via --remote; expect device 2FA) |
| `debug software generate-sar-report current-date` | remote | `panos_debug_software` | (live device state — SSH via --remote; expect device 2FA) |
| `debug software kernelcfg thp` | remote | `panos_debug_software` | (live device state — SSH via --remote; expect device 2FA) |
| `debug software kernelcfg zram-swap disable` | remote | `panos_debug_software` | (live device state — SSH via --remote; expect device 2FA) |
| `debug software kernelcfg zram-swap enable` | remote | `panos_debug_software` | (live device state — SSH via --remote; expect device 2FA) |
| `debug software kernelcfg zram-swap modify num-dev` | remote | `panos_debug_software` | (live device state — SSH via --remote; expect device 2FA) |
| `debug software kernelcfg zram-swap show` | remote | `panos_debug_software` | (live device state — SSH via --remote; expect device 2FA) |
| `debug software large-core show-reserved-space` | remote | `panos_debug_software` | (live device state — SSH via --remote; expect device 2FA) |
| `debug software logging-level set feature service` | remote | `panos_debug_software` | (live device state — SSH via --remote; expect device 2FA) |
| `debug software logging-level set level` | remote | `panos_debug_software` | (live device state — SSH via --remote; expect device 2FA) |
| `debug software logging-level show feature service` | remote | `panos_debug_software` | (live device state — SSH via --remote; expect device 2FA) |
| `debug software logging-level show feature-defs service` | remote | `panos_debug_software` | (live device state — SSH via --remote; expect device 2FA) |
| `debug software logging-level show level service` | remote | `panos_debug_software` | (live device state — SSH via --remote; expect device 2FA) |
| `debug software logging-size set ratio` | remote | `panos_debug_software` | (live device state — SSH via --remote; expect device 2FA) |
| `debug software logging-size show ratio service` | remote | `panos_debug_software` | (live device state — SSH via --remote; expect device 2FA) |
| `debug software memsize_tracked` | remote | `panos_debug_software` | (live device state — SSH via --remote; expect device 2FA) |
| `debug software monitor_smaps_threshold percentage` | remote | `panos_debug_software` | (live device state — SSH via --remote; expect device 2FA) |
| `debug software phy-limit service` | remote | `panos_debug_software` | (live device state — SSH via --remote; expect device 2FA) |
| `debug software resource subsystem` | remote | `panos_debug_software` | (live device state — SSH via --remote; expect device 2FA) |
| `debug software restart process` | remote | `panos_debug_software` | (live device state — SSH via --remote; expect device 2FA) |
| `debug software trace` | remote | `panos_debug_software` | (live device state — SSH via --remote; expect device 2FA) |
| `debug software virt-limit service` | remote | `panos_debug_software` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sslmgr clear log` | remote | `panos_debug_sslmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sslmgr delete crl` | remote | `panos_debug_sslmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sslmgr delete ocsp` | remote | `panos_debug_sslmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sslmgr delete ocsp-host` | remote | `panos_debug_sslmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sslmgr off` | remote | `panos_debug_sslmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sslmgr on` | remote | `panos_debug_sslmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sslmgr reset` | remote | `panos_debug_sslmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sslmgr save ocsp` | remote | `panos_debug_sslmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sslmgr set` | remote | `panos_debug_sslmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sslmgr set crl-background-download` | remote | `panos_debug_sslmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sslmgr set crl-recv-speed-limit` | remote | `panos_debug_sslmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sslmgr set disable-scep-auth-cookie` | remote | `panos_debug_sslmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sslmgr set max-crl-file-size` | remote | `panos_debug_sslmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sslmgr set max-inflated-crl-file-size` | remote | `panos_debug_sslmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sslmgr set ocsp-host-failure-threshold` | remote | `panos_debug_sslmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sslmgr set ocsp-next-update-time` | remote | `panos_debug_sslmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sslmgr set parallel-processing` | remote | `panos_debug_sslmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sslmgr show` | remote | `panos_debug_sslmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sslmgr show memory` | remote | `panos_debug_sslmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sslmgr statistics` | remote | `panos_debug_sslmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sslmgr tar-all-crl` | remote | `panos_debug_sslmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sslmgr test gp-client-cert-check cert-file` | remote | `panos_debug_sslmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sslmgr test show-cert-check-jobs` | remote | `panos_debug_sslmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sslmgr view crl` | remote | `panos_debug_sslmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sslmgr view ocsp` | remote | `panos_debug_sslmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sslmgr view ocsp-host` | remote | `panos_debug_sslmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sslmgr view pending-crl-downloads` | remote | `panos_debug_sslmgr` | (live device state — SSH via --remote; expect device 2FA) |
| `debug streaming dump` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug streaming tdb` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug streaming-telemetry set-logging-reporting-timeout` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug streaming-telemetry show-region-list` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug streaming-telemetry show-schedule` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug streaming-telemetry show-schedule-path-list` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug swm` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug swm install image` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug swm refresh content` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug swm show revert-status` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sysd prefix-query command` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sysd process-query command` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sysd summary` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug sysd top` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug syslog-params reset-to-default-settings` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug syslog-params settings time-reopen` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug syslog-params show` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug system` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug system disk-life disk-1` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug system disk-smart-info disk-1` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug system ssh-key-reset` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug tac-login` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug techsupport duts` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug techsupport duts add-search-dir` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug techsupport duts set-byte-threshold` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug tund clear all` | remote | `panos_debug_tund` | (live device state — SSH via --remote; expect device 2FA) |
| `debug tund global off` | remote | `panos_debug_tund` | (live device state — SSH via --remote; expect device 2FA) |
| `debug tund global on` | remote | `panos_debug_tund` | (live device state — SSH via --remote; expect device 2FA) |
| `debug tund global show` | remote | `panos_debug_tund` | (live device state — SSH via --remote; expect device 2FA) |
| `debug tund tunnel id` | remote | `panos_debug_tund` | (live device state — SSH via --remote; expect device 2FA) |
| `debug ui telemetry` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug use-proxy-for-email-server` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id agent` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id agent-getall-rate rate` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id agent-getall-rate show` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id clear cloud-identity-engine type` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id clear domain-map from-disk` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id clear email-cache` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id clear gm-srvc-query` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id clear group` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id clear ip-port-user-dp ip` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id clear log` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id cluster-get-all` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id cluster-peer-ip` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id cluster-state` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id cp-redirect-host-v6 clear` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id cp-redirect-host-v6 show` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id cp-redirect-host-v6 value` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dscd off` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dscd on` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dscd subdomains` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump cloud-identity-engine type` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump com statistics` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump conn-mgr statistics` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump domain-id-table domain all` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump domain-id-table domain name` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump edir-user all` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump edir-user user` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump email-cache all` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump email-cache email` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump hip-mdm-cache start-from` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump hip-profile-database entry start-from` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump hip-profile-database ipmapping` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump hip-profile-database statistics` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump hip-report user` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump idmgr high-availability state` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump idmgr redis type computer all` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump idmgr redis type computer id` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump idmgr redis type computer name` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump idmgr redis type user all` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump idmgr redis type user id` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump idmgr redis type user name` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump idmgr redis type user-group all` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump idmgr redis type user-group id` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump idmgr redis type user-group name` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump idmgr type computer all` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump idmgr type computer id` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump idmgr type computer name` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump idmgr type user all` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump idmgr type user id` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump idmgr type user name` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump idmgr type user-group all` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump idmgr type user-group id` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump idmgr type user-group name` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump memory` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump relay-ipc-distributord` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump ts-agent` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump uid-2-metadata user all` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump uid-2-metadata user id` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump uid-2-primeuid user all` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump uid-2-primeuid user id` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump userprefix-2-uid user all` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump userprefix-2-uid user name` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump vm-monitored-objects all` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump vm-monitored-objects ref-id` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump vm-monitored-objects source-name` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id dump vm-monitored-objects type` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id get` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id kerberos list server-monitor` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id kerberos purge server-monitor` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id kerberos test default` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id kerberos test server-name` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id l3svc-max-retry rate` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id l3svc-max-retry show` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id l3svc-max-write-retry rate` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id l3svc-max-write-retry show` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id measure-handle-messages-duration` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id off` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id on` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id refresh cloud-identity-engine all` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id refresh cloud-identity-engine config-data` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id refresh cloud-identity-engine name` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id refresh dp-uid-gid` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id refresh group-mapping all` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id refresh group-mapping group-mapping-name` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id refresh group-mapping xmlapi-groups` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id refresh user-id agent` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id relay-ipc-distributord set qsize` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id relay-ipc-distributord set relay-distd-recv-cache-qsize` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id relay-ipc-distributord set relay-distd-recv-read-batch-size` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id relay-ipc-distributord show` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id reset` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id reset captive-portal ip-address` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id reset cloud-identity-engine all` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id reset cloud-identity-engine name` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id reset cluster-state` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id reset com statistics` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id reset conn-mgr statistics` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id reset ip-user-mapping-stats` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id reset relay-statistics` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id reset user-id-manager type` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id save hip-profile-database` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id set agent` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id set all` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id set base` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id set features` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id set hip` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id set ldap` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id set misc` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id set relay` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id set third-party` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id set userid` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id test agentless` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id test cp-login ip-address` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id test cp-logout ip-address` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id test debug-log-category` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id test gp-login ip-address` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id test gp-logout ip-address` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id test hip-profile-database size` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id test hip-report user` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id test hip-update ip` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id test idmgr-change-max type user-group new-max-id` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id test idmgr-restore-default-max type user-group` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id test probing` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id test sso-login ip-address` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id unset agent` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id unset all` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id unset base` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id unset features` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id unset hip` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id unset ldap` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id unset misc` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id unset relay` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id unset third-party` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug user-id unset userid` | remote | `panos_debug_user_id` | (live device state — SSH via --remote; expect device 2FA) |
| `debug vardata-receiver off` | remote | `panos_debug_vardata_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug vardata-receiver on` | remote | `panos_debug_vardata_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug vardata-receiver set all` | remote | `panos_debug_vardata_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug vardata-receiver set third-party` | remote | `panos_debug_vardata_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug vardata-receiver show` | remote | `panos_debug_vardata_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug vardata-receiver statistics` | remote | `panos_debug_vardata_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug vardata-receiver unset all` | remote | `panos_debug_vardata_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug vardata-receiver unset third-party` | remote | `panos_debug_vardata_receiver` | (live device state — SSH via --remote; expect device 2FA) |
| `debug vm-monitor clear source-name` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug vm-monitor reset source-name` | remote | `panos_debug_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `debug wildfire batch-forward set disable` | remote | `panos_debug_wildfire` | (live device state — SSH via --remote; expect device 2FA) |
| `debug wildfire batch-forward set max-count` | remote | `panos_debug_wildfire` | (live device state — SSH via --remote; expect device 2FA) |
| `debug wildfire batch-forward set timeout` | remote | `panos_debug_wildfire` | (live device state — SSH via --remote; expect device 2FA) |
| `debug wildfire cloud-info channel` | remote | `panos_debug_wildfire` | (live device state — SSH via --remote; expect device 2FA) |
| `debug wildfire content-info` | remote | `panos_debug_wildfire` | (live device state — SSH via --remote; expect device 2FA) |
| `debug wildfire dp-status` | remote | `panos_debug_wildfire` | (live device state — SSH via --remote; expect device 2FA) |
| `debug wildfire file-cache` | remote | `panos_debug_wildfire` | (live device state — SSH via --remote; expect device 2FA) |
| `debug wildfire file-digest sha256` | remote | `panos_debug_wildfire` | (live device state — SSH via --remote; expect device 2FA) |
| `debug wildfire monitor-log` | remote | `panos_debug_wildfire` | (live device state — SSH via --remote; expect device 2FA) |
| `debug wildfire monitor-log interval` | remote | `panos_debug_wildfire` | (live device state — SSH via --remote; expect device 2FA) |
| `debug wildfire monitor-log max-size` | remote | `panos_debug_wildfire` | (live device state — SSH via --remote; expect device 2FA) |
| `debug wildfire report-process channel` | remote | `panos_debug_wildfire` | (live device state — SSH via --remote; expect device 2FA) |
| `debug wildfire reset all` | remote | `panos_debug_wildfire` | (live device state — SSH via --remote; expect device 2FA) |
| `debug wildfire reset dp-receiver` | remote | `panos_debug_wildfire` | (live device state — SSH via --remote; expect device 2FA) |
| `debug wildfire reset file-cache` | remote | `panos_debug_wildfire` | (live device state — SSH via --remote; expect device 2FA) |
| `debug wildfire reset forwarding channel` | remote | `panos_debug_wildfire` | (live device state — SSH via --remote; expect device 2FA) |
| `debug wildfire reset log-cache channel` | remote | `panos_debug_wildfire` | (live device state — SSH via --remote; expect device 2FA) |
| `debug wildfire reset report-cache channel` | remote | `panos_debug_wildfire` | (live device state — SSH via --remote; expect device 2FA) |
| `debug wildfire server-selection` | remote | `panos_debug_wildfire` | (live device state — SSH via --remote; expect device 2FA) |
| `debug wildfire transition-file-list` | remote | `panos_debug_wildfire` | (live device state — SSH via --remote; expect device 2FA) |
| `debug wildfire upload-log log disable` | remote | `panos_debug_wildfire` | (live device state — SSH via --remote; expect device 2FA) |
| `debug wildfire upload-log log enable` | remote | `panos_debug_wildfire` | (live device state — SSH via --remote; expect device 2FA) |
| `debug wildfire upload-log log extended-log` | remote | `panos_debug_wildfire` | (live device state — SSH via --remote; expect device 2FA) |
| `debug wildfire upload-log log max-size` | remote | `panos_debug_wildfire` | (live device state — SSH via --remote; expect device 2FA) |
| `debug wildfire upload-log log settings` | remote | `panos_debug_wildfire` | (live device state — SSH via --remote; expect device 2FA) |
| `debug wildfire upload-log show channel` | remote | `panos_debug_wildfire` | (live device state — SSH via --remote; expect device 2FA) |
| `delete admin-sessions username` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete anti-virus update` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete auth` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete authentication system-lock-files` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete authentication user-file ssh-known-hosts self` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete authentication user-file ssh-known-hosts user username` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete config saved` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete config-audit-history` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete content cache curr-content version` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete content cache old-content` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete content update` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete core data-plane file` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete core large-core file` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete core management-plane file` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete data-capture directory` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete debug-filter file` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete debug-log dp-log file` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete debug-log mp-global file` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete debug-log mp-log file` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete device-serialno host all` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete device-serialno host all-from-cloud` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete device-serialno host all-from-ldap` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete device-serialno host serialno` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete dnsproxy file` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete global-protect global-protect-portal portal` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete global-protect-client image` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete global-protect-client version` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete global-protect-clientless-vpn update` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete high-availability-key` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete high-availability-known-hosts` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete hip-mdm-cache mobile-id` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete hip-profile-database all` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete hip-profile-database check-delete-all-status` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete hip-profile-database entry ip` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete hip-report all logout-only` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete hip-report report user` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete iot cache curr-iot version` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete iot cache old-iot` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete license key` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete license token-file` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete logo` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete pcap directory` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete policy-cache` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete pprof management-plane file` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete report custom scope` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete report predefined scope` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete report summary scope` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete runtime-user-db` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete server cert` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete software version` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete ssh-authentication-public-key` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete sslmgr-store certificate-info portal name` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete sslmgr-store satellite-info portal name` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete sslmgr-store satellite-info-revoke-certificate portal` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete unknown-pcap directory` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete url-database all` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete url-database url` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete user-group-cache` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete wf-private update` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete wildfire update` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete wildfire-realtime-cache virus-pattern-type` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `delete wildfire-realtime-stats` | remote | `panos_delete` | (live device state — SSH via --remote; expect device 2FA) |
| `diff config num-context-lines` | remote | `panos_diff` | (live device state — SSH via --remote; expect device 2FA) |
| `ftp export log` | remote | `panos_ftp` | (live device state — SSH via --remote; expect device 2FA) |
| `grep invert-match` | remote | `panos_grep` | (live device state — SSH via --remote; expect device 2FA) |
| `less agent-log` | remote | `panos_less` | (live device state — SSH via --remote; expect device 2FA) |
| `less custom-page` | remote | `panos_less` | (live device state — SSH via --remote; expect device 2FA) |
| `less db-log` | remote | `panos_less` | (live device state — SSH via --remote; expect device 2FA) |
| `less dp-backtrace` | remote | `panos_less` | (live device state — SSH via --remote; expect device 2FA) |
| `less dp-log` | remote | `panos_less` | (live device state — SSH via --remote; expect device 2FA) |
| `less largecore-mp-backtrace` | remote | `panos_less` | (live device state — SSH via --remote; expect device 2FA) |
| `less mp-backtrace` | remote | `panos_less` | (live device state — SSH via --remote; expect device 2FA) |
| `less mp-global` | remote | `panos_less` | (live device state — SSH via --remote; expect device 2FA) |
| `less mp-log` | remote | `panos_less` | (live device state — SSH via --remote; expect device 2FA) |
| `less plugins-log` | remote | `panos_less` | (live device state — SSH via --remote; expect device 2FA) |
| `less webserver-log` | remote | `panos_less` | (live device state — SSH via --remote; expect device 2FA) |
| `ping bypass-routing` | remote | `panos_ping` | (live device state — SSH via --remote; expect device 2FA) |
| `request acknowledge logid` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request address-expansion expand object-name` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request anti-virus downgrade install` | remote | `panos_request_anti_virus` | (live device state — SSH via --remote; expect device 2FA) |
| `request anti-virus upgrade check` | remote | `panos_request_anti_virus` | (live device state — SSH via --remote; expect device 2FA) |
| `request anti-virus upgrade download sync-to-peer` | remote | `panos_request_anti_virus` | (live device state — SSH via --remote; expect device 2FA) |
| `request anti-virus upgrade info` | remote | `panos_request_anti_virus` | (live device state — SSH via --remote; expect device 2FA) |
| `request anti-virus upgrade install commit` | remote | `panos_request_anti_virus` | (live device state — SSH via --remote; expect device 2FA) |
| `request api key expiration` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request authentication unlock-admin user` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request authentication unlock-user vsys` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request authkey set` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request certificate fetch otp` | remote | `panos_request_certificate` | (live device state — SSH via --remote; expect device 2FA) |
| `request certificate generate certificate-name` | remote | `panos_request_certificate` | (live device state — SSH via --remote; expect device 2FA) |
| `request certificate generate-scep-client-cert certificate-name` | remote | `panos_request_certificate` | (live device state — SSH via --remote; expect device 2FA) |
| `request certificate import-scep-ca-cert certificate-name` | remote | `panos_request_certificate` | (live device state — SSH via --remote; expect device 2FA) |
| `request certificate is-blocked certificate-name` | remote | `panos_request_certificate` | (live device state — SSH via --remote; expect device 2FA) |
| `request certificate renew certificate-name` | remote | `panos_request_certificate` | (live device state — SSH via --remote; expect device 2FA) |
| `request certificate revoke certificate-name` | remote | `panos_request_certificate` | (live device state — SSH via --remote; expect device 2FA) |
| `request certificate revoke sslmgr-store db-serialno` | remote | `panos_request_certificate` | (live device state — SSH via --remote; expect device 2FA) |
| `request certificate show certificate-name` | remote | `panos_request_certificate` | (live device state — SSH via --remote; expect device 2FA) |
| `request certificate show-blocked` | remote | `panos_request_certificate` | (live device state — SSH via --remote; expect device 2FA) |
| `request certificate show-blocked shared` | remote | `panos_request_certificate` | (live device state — SSH via --remote; expect device 2FA) |
| `request clean-replay entries` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request clear-commit-tasks` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request commit-lock add comment` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request commit-lock remove admin` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request config diff ver1` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request config list commit-versions filter filter-data` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request config list commit-versions filter filter-query` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request config list commit-versions locations version` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request config-lock add comment` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request config-lock remove` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request content downgrade skip-content-validity-check` | remote | `panos_request_content` | (live device state — SSH via --remote; expect device 2FA) |
| `request content upgrade check` | remote | `panos_request_content` | (live device state — SSH via --remote; expect device 2FA) |
| `request content upgrade download sync-to-peer` | remote | `panos_request_content` | (live device state — SSH via --remote; expect device 2FA) |
| `request content upgrade info` | remote | `panos_request_content` | (live device state — SSH via --remote; expect device 2FA) |
| `request content upgrade install commit` | remote | `panos_request_content` | (live device state — SSH via --remote; expect device 2FA) |
| `request content validity-check` | remote | `panos_request_content` | (live device state — SSH via --remote; expect device 2FA) |
| `request cpld-restart` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request data-filtering access-password create password` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request data-filtering access-password delete` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request data-filtering access-password modify old-password` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request determine-new-applications version` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request device-quarantine-list add ip` | remote | `panos_request_device_quarantine_list` | (live device state — SSH via --remote; expect device 2FA) |
| `request device-quarantine-list delete host` | remote | `panos_request_device_quarantine_list` | (live device state — SSH via --remote; expect device 2FA) |
| `request device-quarantine-list show all option` | remote | `panos_request_device_quarantine_list` | (live device state — SSH via --remote; expect device 2FA) |
| `request device-quarantine-list show hostid` | remote | `panos_request_device_quarantine_list` | (live device state — SSH via --remote; expect device 2FA) |
| `request device-quarantine-list show serialno` | remote | `panos_request_device_quarantine_list` | (live device state — SSH via --remote; expect device 2FA) |
| `request device-registration username` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request device-telemetry` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request dhcp client ipv6 release` | remote | `panos_request_dhcp` | (live device state — SSH via --remote; expect device 2FA) |
| `request dhcp client ipv6 renew` | remote | `panos_request_dhcp` | (live device state — SSH via --remote; expect device 2FA) |
| `request dhcp client management-interface` | remote | `panos_request_dhcp` | (live device state — SSH via --remote; expect device 2FA) |
| `request dhcp client release` | remote | `panos_request_dhcp` | (live device state — SSH via --remote; expect device 2FA) |
| `request dhcp client renew` | remote | `panos_request_dhcp` | (live device state — SSH via --remote; expect device 2FA) |
| `request dhcpv6 client management-interface` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request disable-ztp` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request dnsproxy license refresh` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request encryption-level level` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request get-application-status application` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request get-disabled-applications` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request global-protect-client software activate file` | remote | `panos_request_global_protect_client` | (live device state — SSH via --remote; expect device 2FA) |
| `request global-protect-client software activate version` | remote | `panos_request_global_protect_client` | (live device state — SSH via --remote; expect device 2FA) |
| `request global-protect-client software check` | remote | `panos_request_global_protect_client` | (live device state — SSH via --remote; expect device 2FA) |
| `request global-protect-client software download sync-to-peer` | remote | `panos_request_global_protect_client` | (live device state — SSH via --remote; expect device 2FA) |
| `request global-protect-client software info` | remote | `panos_request_global_protect_client` | (live device state — SSH via --remote; expect device 2FA) |
| `request global-protect-clientless-vpn downgrade install` | remote | `panos_request_global_protect_clientless_vpn` | (live device state — SSH via --remote; expect device 2FA) |
| `request global-protect-clientless-vpn upgrade check` | remote | `panos_request_global_protect_clientless_vpn` | (live device state — SSH via --remote; expect device 2FA) |
| `request global-protect-clientless-vpn upgrade download latest sync-to-peer` | remote | `panos_request_global_protect_clientless_vpn` | (live device state — SSH via --remote; expect device 2FA) |
| `request global-protect-clientless-vpn upgrade info` | remote | `panos_request_global_protect_clientless_vpn` | (live device state — SSH via --remote; expect device 2FA) |
| `request global-protect-clientless-vpn upgrade install commit` | remote | `panos_request_global_protect_clientless_vpn` | (live device state — SSH via --remote; expect device 2FA) |
| `request global-protect-gateway check-client-logout-all-status` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request global-protect-gateway client-logout gateway` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request global-protect-gateway client-logout-all gateway` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request global-protect-gateway satellite-logout gateway` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request global-protect-portal client-logout portal` | remote | `panos_request_global_protect_portal` | (live device state — SSH via --remote; expect device 2FA) |
| `request global-protect-portal refresh-csc-cookie-key` | remote | `panos_request_global_protect_portal` | (live device state — SSH via --remote; expect device 2FA) |
| `request global-protect-portal refresh-scep-cookie-key` | remote | `panos_request_global_protect_portal` | (live device state — SSH via --remote; expect device 2FA) |
| `request global-protect-portal restore-satellite-cookie-expiration` | remote | `panos_request_global_protect_portal` | (live device state — SSH via --remote; expect device 2FA) |
| `request global-protect-portal set-satellite-cookie-expiration value` | remote | `panos_request_global_protect_portal` | (live device state — SSH via --remote; expect device 2FA) |
| `request global-protect-portal ticket portal` | remote | `panos_request_global_protect_portal` | (live device state — SSH via --remote; expect device 2FA) |
| `request global-protect-satellite get-gateway-config satellite` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request global-protect-satellite get-portal-config satellite` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request global-protect-satellite refresh-cookie-key` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request high-availability cluster clear-cache` | remote | `panos_request_high_availability` | (live device state — SSH via --remote; expect device 2FA) |
| `request high-availability cluster sync-from` | remote | `panos_request_high_availability` | (live device state — SSH via --remote; expect device 2FA) |
| `request high-availability session-reestablish force` | remote | `panos_request_high_availability` | (live device state — SSH via --remote; expect device 2FA) |
| `request high-availability state functional` | remote | `panos_request_high_availability` | (live device state — SSH via --remote; expect device 2FA) |
| `request high-availability state peer` | remote | `panos_request_high_availability` | (live device state — SSH via --remote; expect device 2FA) |
| `request high-availability state suspend` | remote | `panos_request_high_availability` | (live device state — SSH via --remote; expect device 2FA) |
| `request high-availability sync-to-remote` | remote | `panos_request_high_availability` | (live device state — SSH via --remote; expect device 2FA) |
| `request high-availability sync-to-remote id-manager` | remote | `panos_request_high_availability` | (live device state — SSH via --remote; expect device 2FA) |
| `request hsm` | remote | `panos_request_hsm` | (live device state — SSH via --remote; expect device 2FA) |
| `request hsm authenticate server` | remote | `panos_request_hsm` | (live device state — SSH via --remote; expect device 2FA) |
| `request hsm client-version` | remote | `panos_request_hsm` | (live device state — SSH via --remote; expect device 2FA) |
| `request hsm ha create-ha-group password` | remote | `panos_request_hsm` | (live device state — SSH via --remote; expect device 2FA) |
| `request hsm ha recover` | remote | `panos_request_hsm` | (live device state — SSH via --remote; expect device 2FA) |
| `request hsm ha replace-server password` | remote | `panos_request_hsm` | (live device state — SSH via --remote; expect device 2FA) |
| `request hsm ha synchronize password` | remote | `panos_request_hsm` | (live device state — SSH via --remote; expect device 2FA) |
| `request hsm login password` | remote | `panos_request_hsm` | (live device state — SSH via --remote; expect device 2FA) |
| `request hsm server-enroll` | remote | `panos_request_hsm` | (live device state — SSH via --remote; expect device 2FA) |
| `request iot upgrade` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request iot validity-check` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request last-acknowledge-time` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request license api-key delete` | remote | `panos_request_license` | (live device state — SSH via --remote; expect device 2FA) |
| `request license api-key set key` | remote | `panos_request_license` | (live device state — SSH via --remote; expect device 2FA) |
| `request license api-key show` | remote | `panos_request_license` | (live device state — SSH via --remote; expect device 2FA) |
| `request license deactivate key mode` | remote | `panos_request_license` | (live device state — SSH via --remote; expect device 2FA) |
| `request license deactivate vm-capacity mode` | remote | `panos_request_license` | (live device state — SSH via --remote; expect device 2FA) |
| `request license fetch auth-code` | remote | `panos_request_license` | (live device state — SSH via --remote; expect device 2FA) |
| `request license info` | remote | `panos_request_license` | (live device state — SSH via --remote; expect device 2FA) |
| `request license install` | remote | `panos_request_license` | (live device state — SSH via --remote; expect device 2FA) |
| `request list-content-downloads` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request log-collector-forwarding status` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request logdb migrate-to-panorama start type` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request logdb migrate-to-panorama status type` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request logdb migrate-to-panorama stop type` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request logging-service-forwarding certificate delete` | remote | `panos_request_logging_service_forwarding` | (live device state — SSH via --remote; expect device 2FA) |
| `request logging-service-forwarding certificate fetch` | remote | `panos_request_logging_service_forwarding` | (live device state — SSH via --remote; expect device 2FA) |
| `request logging-service-forwarding certificate fetch-noproxy pre-shared-key` | remote | `panos_request_logging_service_forwarding` | (live device state — SSH via --remote; expect device 2FA) |
| `request logging-service-forwarding certificate info` | remote | `panos_request_logging_service_forwarding` | (live device state — SSH via --remote; expect device 2FA) |
| `request logging-service-forwarding customerinfo` | remote | `panos_request_logging_service_forwarding` | (live device state — SSH via --remote; expect device 2FA) |
| `request logging-service-forwarding status` | remote | `panos_request_logging_service_forwarding` | (live device state — SSH via --remote; expect device 2FA) |
| `request master-key new-master-key` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request mongo set storage-engine instance` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request mongo show storage-engine instance` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request multi-config` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request panorama-connectivity-check` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request password-change-history dump-history` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request password-change-history re-encrypt old-master-key` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request password-hash password` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request pppoe ipv6 dhcpv6 release` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request pppoe ipv6 dhcpv6 renew` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request quota-enforcement` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request resolve vsys` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request restart dataplane` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request restart software` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request restart system with-swap-scrub` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request routing` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request routing show-config virtual-router` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request routing show-error virtual-router` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request saas_agent certificate info` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request session-discard id` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request set-application-status-recursive enable-dependent-apps` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request shutdown system with-swap-scrub` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request stats dump` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request streaming-telemetry reload-config` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request support` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request system bootstrap-usb delete bundle` | remote | `panos_request_system` | (live device state — SSH via --remote; expect device 2FA) |
| `request system bootstrap-usb prepare from` | remote | `panos_request_system` | (live device state — SSH via --remote; expect device 2FA) |
| `request system external-list global-find string` | remote | `panos_request_system` | (live device state — SSH via --remote; expect device 2FA) |
| `request system external-list list-capacities` | remote | `panos_request_system` | (live device state — SSH via --remote; expect device 2FA) |
| `request system external-list refresh type domain name` | remote | `panos_request_system` | (live device state — SSH via --remote; expect device 2FA) |
| `request system external-list refresh type ip name` | remote | `panos_request_system` | (live device state — SSH via --remote; expect device 2FA) |
| `request system external-list refresh type url name` | remote | `panos_request_system` | (live device state — SSH via --remote; expect device 2FA) |
| `request system external-list show type` | remote | `panos_request_system` | (live device state — SSH via --remote; expect device 2FA) |
| `request system external-list stats type` | remote | `panos_request_system` | (live device state — SSH via --remote; expect device 2FA) |
| `request system external-list url-test` | remote | `panos_request_system` | (live device state — SSH via --remote; expect device 2FA) |
| `request system fqdn` | remote | `panos_request_system` | (live device state — SSH via --remote; expect device 2FA) |
| `request system idmap-sync` | remote | `panos_request_system` | (live device state — SSH via --remote; expect device 2FA) |
| `request system patch apply` | remote | `panos_request_system` | (live device state — SSH via --remote; expect device 2FA) |
| `request system patch check` | remote | `panos_request_system` | (live device state — SSH via --remote; expect device 2FA) |
| `request system patch download version` | remote | `panos_request_system` | (live device state — SSH via --remote; expect device 2FA) |
| `request system patch info version` | remote | `panos_request_system` | (live device state — SSH via --remote; expect device 2FA) |
| `request system patch install version` | remote | `panos_request_system` | (live device state — SSH via --remote; expect device 2FA) |
| `request system patch revert` | remote | `panos_request_system` | (live device state — SSH via --remote; expect device 2FA) |
| `request system patch scp-export profile-name` | remote | `panos_request_system` | (live device state — SSH via --remote; expect device 2FA) |
| `request system patch scp-import profile-name` | remote | `panos_request_system` | (live device state — SSH via --remote; expect device 2FA) |
| `request system private-data-reset shutdown` | remote | `panos_request_system` | (live device state — SSH via --remote; expect device 2FA) |
| `request system self-test crypto` | remote | `panos_request_system` | (live device state — SSH via --remote; expect device 2FA) |
| `request system self-test force-crypto-failure dp` | remote | `panos_request_system` | (live device state — SSH via --remote; expect device 2FA) |
| `request system self-test force-crypto-failure mp` | remote | `panos_request_system` | (live device state — SSH via --remote; expect device 2FA) |
| `request system self-test force-software-integrity-failure` | remote | `panos_request_system` | (live device state — SSH via --remote; expect device 2FA) |
| `request system self-test software-integrity` | remote | `panos_request_system` | (live device state — SSH via --remote; expect device 2FA) |
| `request system self-test-job` | remote | `panos_request_system` | (live device state — SSH via --remote; expect device 2FA) |
| `request system software download scp-profile` | remote | `panos_request_system` | (live device state — SSH via --remote; expect device 2FA) |
| `request system software eligible to-version` | remote | `panos_request_system` | (live device state — SSH via --remote; expect device 2FA) |
| `request system software info` | remote | `panos_request_system` | (live device state — SSH via --remote; expect device 2FA) |
| `request system software install load-config` | remote | `panos_request_system` | (live device state — SSH via --remote; expect device 2FA) |
| `request system software scp-export profile-name` | remote | `panos_request_system` | (live device state — SSH via --remote; expect device 2FA) |
| `request system software scp-import profile-name` | remote | `panos_request_system` | (live device state — SSH via --remote; expect device 2FA) |
| `request tech-support copy-to-remote-host remote-hostname` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request tech-support dump` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request telemetry-data dump` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request ui telemetry` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request url-filtering install pandb-database` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request url-filtering save url-database` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request url-filtering update url` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request user-id cloud-identity-engine config-data status` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request wf-private downgrade install` | remote | `panos_request_wf_private` | (live device state — SSH via --remote; expect device 2FA) |
| `request wf-private upgrade check` | remote | `panos_request_wf_private` | (live device state — SSH via --remote; expect device 2FA) |
| `request wf-private upgrade download latest sync-to-peer` | remote | `panos_request_wf_private` | (live device state — SSH via --remote; expect device 2FA) |
| `request wf-private upgrade info` | remote | `panos_request_wf_private` | (live device state — SSH via --remote; expect device 2FA) |
| `request wf-private upgrade install commit` | remote | `panos_request_wf_private` | (live device state — SSH via --remote; expect device 2FA) |
| `request wildfire downgrade install` | remote | `panos_request_wildfire` | (live device state — SSH via --remote; expect device 2FA) |
| `request wildfire registration channel` | remote | `panos_request_wildfire` | (live device state — SSH via --remote; expect device 2FA) |
| `request wildfire upgrade check` | remote | `panos_request_wildfire` | (live device state — SSH via --remote; expect device 2FA) |
| `request wildfire upgrade download latest sync-to-peer` | remote | `panos_request_wildfire` | (live device state — SSH via --remote; expect device 2FA) |
| `request wildfire upgrade info` | remote | `panos_request_wildfire` | (live device state — SSH via --remote; expect device 2FA) |
| `request wildfire upgrade install commit` | remote | `panos_request_wildfire` | (live device state — SSH via --remote; expect device 2FA) |
| `request wildfire-realtime-cache add virus-pattern-type` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `request wildfire-realtime-cache delete virus-pattern-type` | remote | `panos_request_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `schedule botnet-report period` | remote | `panos_schedule` | (live device state — SSH via --remote; expect device 2FA) |
| `schedule saas-applications-usage-report skip-detailed-report` | remote | `panos_schedule` | (live device state — SSH via --remote; expect device 2FA) |
| `schedule uar-report user` | remote | `panos_schedule` | (live device state — SSH via --remote; expect device 2FA) |
| `scp export` | remote | `panos_scp` | (live device state — SSH via --remote; expect device 2FA) |
| `scp export certificate to` | remote | `panos_scp` | (live device state — SSH via --remote; expect device 2FA) |
| `scp export core-file data-plane from` | remote | `panos_scp` | (live device state — SSH via --remote; expect device 2FA) |
| `scp export core-file large-corefile from` | remote | `panos_scp` | (live device state — SSH via --remote; expect device 2FA) |
| `scp export core-file management-plane from` | remote | `panos_scp` | (live device state — SSH via --remote; expect device 2FA) |
| `scp export debug bootmem_file from` | remote | `panos_scp` | (live device state — SSH via --remote; expect device 2FA) |
| `scp export log` | remote | `panos_scp` | (live device state — SSH via --remote; expect device 2FA) |
| `scp export log-file data-plane to` | remote | `panos_scp` | (live device state — SSH via --remote; expect device 2FA) |
| `scp export log-file management-plane to` | remote | `panos_scp` | (live device state — SSH via --remote; expect device 2FA) |
| `scp export pprof-file management-plane from` | remote | `panos_scp` | (live device state — SSH via --remote; expect device 2FA) |
| `scp export stats-dump to` | remote | `panos_scp` | (live device state — SSH via --remote; expect device 2FA) |
| `scp export threat-pcap pcap-id` | remote | `panos_scp` | (live device state — SSH via --remote; expect device 2FA) |
| `scp import` | remote | `panos_scp` | (live device state — SSH via --remote; expect device 2FA) |
| `scp import certificate from` | remote | `panos_scp` | (live device state — SSH via --remote; expect device 2FA) |
| `scp import hsm-ciphertrust-client-cert from` | remote | `panos_scp` | (live device state — SSH via --remote; expect device 2FA) |
| `scp import hsm-ciphertrust-client-key from` | remote | `panos_scp` | (live device state — SSH via --remote; expect device 2FA) |
| `scp import hsm-ciphertrust-server-cert from` | remote | `panos_scp` | (live device state — SSH via --remote; expect device 2FA) |
| `scp import hsm-server-cert from` | remote | `panos_scp` | (live device state — SSH via --remote; expect device 2FA) |
| `scp import idp-metadata profile-name` | remote | `panos_scp` | (live device state — SSH via --remote; expect device 2FA) |
| `scp import keypair from` | remote | `panos_scp` | (live device state — SSH via --remote; expect device 2FA) |
| `scp import private-key from` | remote | `panos_scp` | (live device state — SSH via --remote; expect device 2FA) |
| `set advanced-routing fib check default-interval` | remote | `panos_set_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `set advanced-routing fib check disable` | remote | `panos_set_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `set advanced-routing fib check disable-auto-recovery` | remote | `panos_set_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `set advanced-routing fib check interval` | remote | `panos_set_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `set advanced-routing fib check recovery-failure-threshold` | remote | `panos_set_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `set application dump off` | remote | `panos_set_application` | (live device state — SSH via --remote; expect device 2FA) |
| `set application dump on limit` | remote | `panos_set_application` | (live device state — SSH via --remote; expect device 2FA) |
| `set application traceroute enable` | remote | `panos_set_application` | (live device state — SSH via --remote; expect device 2FA) |
| `set application traceroute ttl-threshold` | remote | `panos_set_application` | (live device state — SSH via --remote; expect device 2FA) |
| `set audit-comment xpath` | remote | `panos_set_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `set auth remote-host-check` | remote | `panos_set_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `set auth strict-username-check` | remote | `panos_set_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `set authentication radius-vsa-off` | remote | `panos_set_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `set authentication radius-vsa-on` | remote | `panos_set_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `set authentication saml_signature_digest_algorithm` | remote | `panos_set_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `set cli` | remote | `panos_set_cli` | (live device state — SSH via --remote; expect device 2FA) |
| `set cli config-output-format` | remote | `panos_set_cli` | (live device state — SSH via --remote; expect device 2FA) |
| `set cli hide-ip value` | remote | `panos_set_cli` | (live device state — SSH via --remote; expect device 2FA) |
| `set cli hide-user value` | remote | `panos_set_cli` | (live device state — SSH via --remote; expect device 2FA) |
| `set cli terminal height` | remote | `panos_set_cli` | (live device state — SSH via --remote; expect device 2FA) |
| `set cli terminal type` | remote | `panos_set_cli` | (live device state — SSH via --remote; expect device 2FA) |
| `set cli terminal width` | remote | `panos_set_cli` | (live device state — SSH via --remote; expect device 2FA) |
| `set cli timeout idle` | remote | `panos_set_cli` | (live device state — SSH via --remote; expect device 2FA) |
| `set clock date` | remote | `panos_set_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `set data-access-password` | remote | `panos_set_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `set device-inventory-edit add-device mac` | remote | `panos_set_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `set device-inventory-edit edit-devices hostname` | remote | `panos_set_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `set device-inventory-upload csvfile` | remote | `panos_set_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `set fwd-uni-dhcp-packet-on-dhcp-client-intf` | remote | `panos_set_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `set global-protect arg-maxlen` | remote | `panos_set_global_protect` | (live device state — SSH via --remote; expect device 2FA) |
| `set global-protect global-protect-portal portal` | remote | `panos_set_global_protect` | (live device state — SSH via --remote; expect device 2FA) |
| `set global-protect redirect location` | remote | `panos_set_global_protect` | (live device state — SSH via --remote; expect device 2FA) |
| `set global-protect redirect off` | remote | `panos_set_global_protect` | (live device state — SSH via --remote; expect device 2FA) |
| `set global-protect redirect on` | remote | `panos_set_global_protect` | (live device state — SSH via --remote; expect device 2FA) |
| `set global-protect redirect show` | remote | `panos_set_global_protect` | (live device state — SSH via --remote; expect device 2FA) |
| `set global-protect satellite-serialnumberip-auth` | remote | `panos_set_global_protect` | (live device state — SSH via --remote; expect device 2FA) |
| `set logrcvr offline-logpurger interval` | remote | `panos_set_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `set logrcvr offline-logpurger percentage-threshold` | remote | `panos_set_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `set management-server logging` | remote | `panos_set_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `set max-num-images count` | remote | `panos_set_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `set mgmtbond` | remote | `panos_set_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `set nw-id-api data` | remote | `panos_set_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `set password` | remote | `panos_set_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `set preserve-prenat-feature adjust-mtu` | remote | `panos_set_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `set preserve-prenat-feature verify-checksum` | remote | `panos_set_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `set quarantine data` | remote | `panos_set_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `set session` | remote | `panos_set_session` | (live device state — SSH via --remote; expect device 2FA) |
| `set session accelerated-aging-scaling-factor` | remote | `panos_set_session` | (live device state — SSH via --remote; expect device 2FA) |
| `set session accelerated-aging-threshold` | remote | `panos_set_session` | (live device state — SSH via --remote; expect device 2FA) |
| `set session default` | remote | `panos_set_session` | (live device state — SSH via --remote; expect device 2FA) |
| `set session ingress_backlogs_duration` | remote | `panos_set_session` | (live device state — SSH via --remote; expect device 2FA) |
| `set session ingress_backlogs_threshold` | remote | `panos_set_session` | (live device state — SSH via --remote; expect device 2FA) |
| `set session lag-flow-key-type` | remote | `panos_set_session` | (live device state — SSH via --remote; expect device 2FA) |
| `set session pvst-native-vlan-id` | remote | `panos_set_session` | (live device state — SSH via --remote; expect device 2FA) |
| `set session resource-limit-behavior` | remote | `panos_set_session` | (live device state — SSH via --remote; expect device 2FA) |
| `set session scan-scaling-factor` | remote | `panos_set_session` | (live device state — SSH via --remote; expect device 2FA) |
| `set session scan-threshold` | remote | `panos_set_session` | (live device state — SSH via --remote; expect device 2FA) |
| `set session tcp-cong-ctrl` | remote | `panos_set_session` | (live device state — SSH via --remote; expect device 2FA) |
| `set session tcp-reject-small-initial-window-threshold` | remote | `panos_set_session` | (live device state — SSH via --remote; expect device 2FA) |
| `set session tcp-rsts` | remote | `panos_set_session` | (live device state — SSH via --remote; expect device 2FA) |
| `set session timeout-scan` | remote | `panos_set_session` | (live device state — SSH via --remote; expect device 2FA) |
| `set session timeout-tcp-delayed-ack` | remote | `panos_set_session` | (live device state — SSH via --remote; expect device 2FA) |
| `set session timeout-tcp-half-closed` | remote | `panos_set_session` | (live device state — SSH via --remote; expect device 2FA) |
| `set session timeout-tcp-time-wait` | remote | `panos_set_session` | (live device state — SSH via --remote; expect device 2FA) |
| `set session timeout-tcp-unverified-rst` | remote | `panos_set_session` | (live device state — SSH via --remote; expect device 2FA) |
| `set session timeout-tcphandshake` | remote | `panos_set_session` | (live device state — SSH via --remote; expect device 2FA) |
| `set session timeout-tcpinit` | remote | `panos_set_session` | (live device state — SSH via --remote; expect device 2FA) |
| `set snmpd refresh-timer-period` | remote | `panos_set_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `set ssh service-restart` | remote | `panos_set_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `set ssh-authentication public-key` | remote | `panos_set_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `set ssl add-secure-renegotiation-extension` | remote | `panos_set_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `set ssl-conn-on-cert fail-all-conns` | remote | `panos_set_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `set ssl-conn-on-cert fail-syslog-conns` | remote | `panos_set_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `set sslmgr-check-cert-jobs max-limit` | remote | `panos_set_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `set syslog fqdn-refresh` | remote | `panos_set_syslog` | (live device state — SSH via --remote; expect device 2FA) |
| `set syslog ssl-conn-validation all-conns` | remote | `panos_set_syslog` | (live device state — SSH via --remote; expect device 2FA) |
| `set syslog ssl-conn-validation explicit crl` | remote | `panos_set_syslog` | (live device state — SSH via --remote; expect device 2FA) |
| `set syslog ssl-conn-validation explicit eku` | remote | `panos_set_syslog` | (live device state — SSH via --remote; expect device 2FA) |
| `set syslog ssl-conn-validation explicit ocsp` | remote | `panos_set_syslog` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting additional-threat-log` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting alg-natref` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting alg-persistent-nat` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting arp-cache-timeout` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting ctd` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting ctd ctd-agent-assigned-cores` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting ctd feature-forward cloud-appid-prefiltering` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting ctd feature-forward mica` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting ctd lscan-mode` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting ctd lscan-mode-default` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting ctd max-sess-hash-limit` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting ctd nonblocking-pattern-match-interval` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting ctd pkt-proc-boundary` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting ctd pkt-proc-loop-high` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting ctd pkt-proc-loop-low` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting ctd regex-stats-on` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting ctd wif-shared-buf-threshold` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting ctd-mode` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting ctd-mode-default` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting delay-interface-process interface` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting dfa-mode` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting dfa-mode-default` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting hardware-acl-blocking-duration` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting hardware-acl-blocking-enable` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting icmp6-error` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting ip6-defrag-timeout` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting jumbo-frame` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting layer4-checksum` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting logging default` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting logging default-policy-logging` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting logging log-compression` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting logging log-suppression` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting logging max-log-rate` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting logging max-packet-rate` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting mp-vr-vif-install-only-host-route` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting multi-vsys` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting packet ip-frag-limit` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting packet-path-test enable` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting packet-path-test show` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting paloalto-networks-service-proxy` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting persistent-dipp-alert` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting pow` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting pppoe-dont-send-eol interface` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting shared-policy` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting software-acl-blocking-duration` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting ssl-decrypt` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting ssl-decrypt answer-timeout` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting ssl-decrypt tunnel-taildrop-threshold` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting target-vsys` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting template` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting util assert-crash-once` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting wildfire disk-quota` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting wildfire disk-quota global` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting wildfire interval report-update-interval` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting wildfire interval server-list-update-interval` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting zip enable` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set system setting zip hw-reset` | remote | `panos_set_system` | (live device state — SSH via --remote; expect device 2FA) |
| `set transceiver-monitor-rate slot` | remote | `panos_set_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `set user-id data` | remote | `panos_set_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `set xmlapi-group add group` | remote | `panos_set_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `set xmlapi-group delete group` | remote | `panos_set_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `set xmlapi-group refresh group` | remote | `panos_set_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `set ztp panorama-timeout` | remote | `panos_set_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show adem probes` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show adem routeinfo destination` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show admins` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing bfd active-profile name` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing bfd details logical-router` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing bfd drop-counters session-id` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing bfd summary logical-router` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing bgp filters access-list logical-router` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing bgp filters prefix-list logical-router` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing bgp filters route-map logical-router` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing bgp loc-rib-detail peer` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing bgp peer` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing bgp peer detail peer-name` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing bgp peer status peer-name` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing bgp peer-groups logical-router` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing bgp rib-out-detail peer` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing bgp route afi` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing bgp summary logical-router` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing fib afi` | device | `panos_show_advanced_routing` | (live device state — via the SCM device tunnel; no SSH/2FA) |
| `show advanced-routing interface logical-router` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing logical-router lr-name` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing multicast fib group` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing multicast group-permission interface` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing multicast igmp interface logical-router` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing multicast igmp membership interface` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing multicast igmp statistics interface` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing multicast msdp peer detail peer-name` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing multicast msdp peer status peer-name` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing multicast msdp sa logical-router` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing multicast msdp statistics logical-router` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing multicast msdp summary logical-router` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing multicast pim elected-bsr logical-router` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing multicast pim group-mapping group` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing multicast pim interface logical-router` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing multicast pim neighbor logical-router` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing multicast pim rpf static` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing multicast pim state logical-router` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing multicast pim statistics interface` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing multicast route group` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing ospf` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing ospf dumplsdb adv-rtr` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing ospf interface brief` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing ospf lsdb adv-rtr` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing ospf neighbor brief` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing ospf virt-neighbor brief` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing ospfv3` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing ospfv3 dumplsdb scope` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing ospfv3 interface brief` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing ospfv3 lsdb scope` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing ospfv3 neighbor brief` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing ospfv3 virt-neighbor brief` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing resource logical-router` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing rip` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show advanced-routing route destination` | device | `panos_show_advanced_routing` | (live device state — via the SCM device tunnel; no SSH/2FA) |
| `show advanced-routing static-route-path-monitor logical-router` | remote | `panos_show_advanced_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show api-key-expiration-ts` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show applications vsys` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show auth` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show authentication allowlist` | remote | `panos_show_authentication` | (live device state — SSH via --remote; expect device 2FA) |
| `show authentication groupdb` | remote | `panos_show_authentication` | (live device state — SSH via --remote; expect device 2FA) |
| `show authentication groupnames` | remote | `panos_show_authentication` | (live device state — SSH via --remote; expect device 2FA) |
| `show authentication local-user-db vsys` | remote | `panos_show_authentication` | (live device state — SSH via --remote; expect device 2FA) |
| `show authentication locked-users vsys` | remote | `panos_show_authentication` | (live device state — SSH via --remote; expect device 2FA) |
| `show authentication service-principal vsys` | remote | `panos_show_authentication` | (live device state — SSH via --remote; expect device 2FA) |
| `show authentication service-principals vsys` | remote | `panos_show_authentication` | (live device state — SSH via --remote; expect device 2FA) |
| `show authentication statistics username` | remote | `panos_show_authentication` | (live device state — SSH via --remote; expect device 2FA) |
| `show bad-custom-signature` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show bonjour interface` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show chassis inventory` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show chassis-ready` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show cli` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show clock more` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show cloud-appid` | remote | `panos_show_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `show cloud-appid app-to-filtergroup-mapping batch-idx` | remote | `panos_show_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `show cloud-appid application` | remote | `panos_show_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `show cloud-appid application-filter all` | remote | `panos_show_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `show cloud-appid application-filter option vsys` | remote | `panos_show_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `show cloud-appid application-group all` | remote | `panos_show_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `show cloud-appid application-group option vsys` | remote | `panos_show_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `show cloud-appid cloud-app-data app-metadata` | remote | `panos_show_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `show cloud-appid cloud-app-data application all` | remote | `panos_show_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `show cloud-appid cloud-app-data application app-id` | remote | `panos_show_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `show cloud-appid cloud-app-data application cloud-app-name` | remote | `panos_show_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `show cloud-appid cloud-app-data application statistics` | remote | `panos_show_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `show cloud-appid cloud-app-data container all` | remote | `panos_show_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `show cloud-appid cloud-app-data container container-id` | remote | `panos_show_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `show cloud-appid cloud-app-data container container-name` | remote | `panos_show_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `show cloud-appid cloud-app-data container statistics` | remote | `panos_show_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `show cloud-appid signature-dp` | remote | `panos_show_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `show cloud-appid signature-dp app-signature all` | remote | `panos_show_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `show cloud-appid signature-dp app-signature cloud-app-name` | remote | `panos_show_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `show cloud-appid signature-dp app-signature signature-id` | remote | `panos_show_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `show cloud-appid signature-dp app-signature statistics` | remote | `panos_show_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `show cloud-appid signature-dp appid` | remote | `panos_show_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `show cloud-appid signature-dp threat-signature all` | remote | `panos_show_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `show cloud-appid signature-dp threat-signature cloud-app-name` | remote | `panos_show_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `show cloud-appid signature-dp threat-signature statistics` | remote | `panos_show_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `show cloud-appid signature-dp threat-signature threat-id` | remote | `panos_show_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `show cloud-appid task all option` | remote | `panos_show_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `show cloud-appid task statistics` | remote | `panos_show_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `show cloud-appid task task-index` | remote | `panos_show_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `show cloud-appid transaction all option` | remote | `panos_show_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `show cloud-appid transaction trans-index` | remote | `panos_show_cloud_appid` | (live device state — SSH via --remote; expect device 2FA) |
| `show cloud-auth-service-alerts` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show cloud-auth-service-metadata region_id` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show cloud-auth-service-profiles tenant_id` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show cloud-auth-service-regions force_refresh` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show cloud-auth-service-tenants region_id` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show cloud-management-status` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show cloud-userid` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show cluster` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show cluster-userid statistics` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show commit-locks vsys` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show config` | remote | `panos_show_config` | (live device state — SSH via --remote; expect device 2FA) |
| `show config audit base-version` | remote | `panos_show_config` | (live device state — SSH via --remote; expect device 2FA) |
| `show config audit base-version-no-deletes` | remote | `panos_show_config` | (live device state — SSH via --remote; expect device 2FA) |
| `show config audit info` | remote | `panos_show_config` | (live device state — SSH via --remote; expect device 2FA) |
| `show config audit version` | remote | `panos_show_config` | (live device state — SSH via --remote; expect device 2FA) |
| `show config commit-scope partial shared-object` | remote | `panos_show_config` | (live device state — SSH via --remote; expect device 2FA) |
| `show config effective-running xpath` | remote | `panos_show_config` | (live device state — SSH via --remote; expect device 2FA) |
| `show config list admins partial shared-object` | remote | `panos_show_config` | (live device state — SSH via --remote; expect device 2FA) |
| `show config list audit-comments xpath` | remote | `panos_show_config` | (live device state — SSH via --remote; expect device 2FA) |
| `show config list change-summary partial admin` | remote | `panos_show_config` | (live device state — SSH via --remote; expect device 2FA) |
| `show config list changes partial shared-object` | remote | `panos_show_config` | (live device state — SSH via --remote; expect device 2FA) |
| `show config pushed-shared-policy vsys` | remote | `panos_show_config` | (live device state — SSH via --remote; expect device 2FA) |
| `show config running xpath` | remote | `panos_show_config` | (live device state — SSH via --remote; expect device 2FA) |
| `show config saved` | remote | `panos_show_config` | (live device state — SSH via --remote; expect device 2FA) |
| `show config-locks vsys` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show counter global filter category` | remote | `panos_show_counter` | (live device state — SSH via --remote; expect device 2FA) |
| `show counter global name` | remote | `panos_show_counter` | (live device state — SSH via --remote; expect device 2FA) |
| `show counter interface` | remote | `panos_show_counter` | (live device state — SSH via --remote; expect device 2FA) |
| `show counter management-server` | remote | `panos_show_counter` | (live device state — SSH via --remote; expect device 2FA) |
| `show counter rate` | remote | `panos_show_counter` | (live device state — SSH via --remote; expect device 2FA) |
| `show counter total-throughput` | remote | `panos_show_counter` | (live device state — SSH via --remote; expect device 2FA) |
| `show ctd-agent` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show ctd-agent debug` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show ctd-agent status` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show device-certificate` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show device-telemetry` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show device-telemetry stats` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig high-availability election-option` | remote | `panos_show_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig high-availability election-option timers` | remote | `panos_show_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig high-availability path-monitoring` | remote | `panos_show_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig high-availability path-monitoring path-group` | remote | `panos_show_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig high-availability peer` | remote | `panos_show_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig high-availability peer encryption` | remote | `panos_show_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig setting cloud-host-compliance` | remote | `panos_show_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig setting management log-forwarding-from-device` | remote | `panos_show_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig setting management secure-conn-server authorization-list` | remote | `panos_show_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig setting wildfire private-cloud-secure-conn-client` | remote | `panos_show_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig setting wildfire private-cloud-secure-conn-client certificate-type` | remote | `panos_show_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system config-bundle-export-schedule` | remote | `panos_show_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system deployment-update-schedule` | remote | `panos_show_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system dlsrvr` | remote | `panos_show_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system hsm-settings provider aws-cloudhsm` | remote | `panos_show_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system hsm-settings provider aws-cloudhsm health-check-settings` | remote | `panos_show_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system hsm-settings provider aws-cloudhsm hsm-cluster` | remote | `panos_show_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system maintenance-user` | remote | `panos_show_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system management-tunnel` | remote | `panos_show_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system management-tunnel crypto-profiles` | remote | `panos_show_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system management-tunnel crypto-profiles ikev2-crypto-profiles` | remote | `panos_show_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system management-tunnel crypto-profiles ipsec-crypto-profiles` | remote | `panos_show_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system management-tunnel ikev2-gateway` | remote | `panos_show_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system management-tunnel tunnel` | remote | `panos_show_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show deviceconfig system push-schedule` | remote | `panos_show_deviceconfig` | (live device state — SSH via --remote; expect device 2FA) |
| `show dhcp client ipv6 pool-details` | remote | `panos_show_dhcp` | (live device state — SSH via --remote; expect device 2FA) |
| `show dhcp client ipv6 state interface` | remote | `panos_show_dhcp` | (live device state — SSH via --remote; expect device 2FA) |
| `show dhcp client ipv6-gateway-address` | remote | `panos_show_dhcp` | (live device state — SSH via --remote; expect device 2FA) |
| `show dhcp client mgmt-interface-state` | remote | `panos_show_dhcp` | (live device state — SSH via --remote; expect device 2FA) |
| `show dhcp client mgmt6-interface-state` | remote | `panos_show_dhcp` | (live device state — SSH via --remote; expect device 2FA) |
| `show dhcp client state` | remote | `panos_show_dhcp` | (live device state — SSH via --remote; expect device 2FA) |
| `show dhcp inherited state interface` | remote | `panos_show_dhcp` | (live device state — SSH via --remote; expect device 2FA) |
| `show dhcp server lease interface` | remote | `panos_show_dhcp` | (live device state — SSH via --remote; expect device 2FA) |
| `show dhcp server settings` | remote | `panos_show_dhcp` | (live device state — SSH via --remote; expect device 2FA) |
| `show dns-proxy cache all` | remote | `panos_show_dns_proxy` | (live device state — SSH via --remote; expect device 2FA) |
| `show dns-proxy cache dump file` | remote | `panos_show_dns_proxy` | (live device state — SSH via --remote; expect device 2FA) |
| `show dns-proxy cache filter fqdn` | remote | `panos_show_dns_proxy` | (live device state — SSH via --remote; expect device 2FA) |
| `show dns-proxy cache mgmt-obj` | remote | `panos_show_dns_proxy` | (live device state — SSH via --remote; expect device 2FA) |
| `show dns-proxy cache name` | remote | `panos_show_dns_proxy` | (live device state — SSH via --remote; expect device 2FA) |
| `show dns-proxy ddns interface name` | remote | `panos_show_dns_proxy` | (live device state — SSH via --remote; expect device 2FA) |
| `show dns-proxy dns-signature cache fqdn` | remote | `panos_show_dns_proxy` | (live device state — SSH via --remote; expect device 2FA) |
| `show dns-proxy dns-signature content` | remote | `panos_show_dns_proxy` | (live device state — SSH via --remote; expect device 2FA) |
| `show dns-proxy dns-signature counters` | remote | `panos_show_dns_proxy` | (live device state — SSH via --remote; expect device 2FA) |
| `show dns-proxy dns-signature info` | remote | `panos_show_dns_proxy` | (live device state — SSH via --remote; expect device 2FA) |
| `show dns-proxy encrypted-dns` | remote | `panos_show_dns_proxy` | (live device state — SSH via --remote; expect device 2FA) |
| `show dns-proxy fqdn all` | remote | `panos_show_dns_proxy` | (live device state — SSH via --remote; expect device 2FA) |
| `show dns-proxy fqdn mgmt-obj` | remote | `panos_show_dns_proxy` | (live device state — SSH via --remote; expect device 2FA) |
| `show dns-proxy fqdn name` | remote | `panos_show_dns_proxy` | (live device state — SSH via --remote; expect device 2FA) |
| `show dns-proxy settings all` | remote | `panos_show_dns_proxy` | (live device state — SSH via --remote; expect device 2FA) |
| `show dns-proxy settings mgmt-obj` | remote | `panos_show_dns_proxy` | (live device state — SSH via --remote; expect device 2FA) |
| `show dns-proxy settings name` | remote | `panos_show_dns_proxy` | (live device state — SSH via --remote; expect device 2FA) |
| `show dns-proxy socket-count all` | remote | `panos_show_dns_proxy` | (live device state — SSH via --remote; expect device 2FA) |
| `show dns-proxy static-entries all` | remote | `panos_show_dns_proxy` | (live device state — SSH via --remote; expect device 2FA) |
| `show dns-proxy static-entries dump file` | remote | `panos_show_dns_proxy` | (live device state — SSH via --remote; expect device 2FA) |
| `show dns-proxy static-entries filter fqdn` | remote | `panos_show_dns_proxy` | (live device state — SSH via --remote; expect device 2FA) |
| `show dns-proxy static-entries name` | remote | `panos_show_dns_proxy` | (live device state — SSH via --remote; expect device 2FA) |
| `show dns-proxy statistics all` | device | `panos_show_dns_proxy` | (live device state — via the SCM device tunnel; no SSH/2FA) |
| `show dns-proxy statistics mgmt-obj` | device | `panos_show_dns_proxy` | (live device state — via the SCM device tunnel; no SSH/2FA) |
| `show dns-proxy statistics name` | device | `panos_show_dns_proxy` | (live device state — via the SCM device tunnel; no SSH/2FA) |
| `show dos-block-table all start-at` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show dos-block-table hardware start-at` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show dos-block-table software start-at` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show dos-block-table summary` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show dos-protection rule` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show dos-protection zone` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show global-protect` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show global-protect-firewall summary firewall-client-version-last-activity-time` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show global-protect-gateway current-satellite gateway` | remote | `panos_show_global_protect_gateway` | (live device state — SSH via --remote; expect device 2FA) |
| `show global-protect-gateway current-user gateway` | remote | `panos_show_global_protect_gateway` | (live device state — SSH via --remote; expect device 2FA) |
| `show global-protect-gateway flow name` | remote | `panos_show_global_protect_gateway` | (live device state — SSH via --remote; expect device 2FA) |
| `show global-protect-gateway flow tunnel-id` | remote | `panos_show_global_protect_gateway` | (live device state — SSH via --remote; expect device 2FA) |
| `show global-protect-gateway flow-site-to-site name` | remote | `panos_show_global_protect_gateway` | (live device state — SSH via --remote; expect device 2FA) |
| `show global-protect-gateway flow-site-to-site tunnel-id` | remote | `panos_show_global_protect_gateway` | (live device state — SSH via --remote; expect device 2FA) |
| `show global-protect-gateway gateway name` | remote | `panos_show_global_protect_gateway` | (live device state — SSH via --remote; expect device 2FA) |
| `show global-protect-gateway previous-satellite gateway` | remote | `panos_show_global_protect_gateway` | (live device state — SSH via --remote; expect device 2FA) |
| `show global-protect-gateway previous-user gateway` | remote | `panos_show_global_protect_gateway` | (live device state — SSH via --remote; expect device 2FA) |
| `show global-protect-gateway statistics gateway` | remote | `panos_show_global_protect_gateway` | (live device state — SSH via --remote; expect device 2FA) |
| `show global-protect-gateway summary all` | remote | `panos_show_global_protect_gateway` | (live device state — SSH via --remote; expect device 2FA) |
| `show global-protect-gateway summary detail name` | remote | `panos_show_global_protect_gateway` | (live device state — SSH via --remote; expect device 2FA) |
| `show global-protect-mdm state` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show global-protect-mdm statistics` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show global-protect-portal cookie-cache portal` | remote | `panos_show_global_protect_portal` | (live device state — SSH via --remote; expect device 2FA) |
| `show global-protect-portal current-user portal` | remote | `panos_show_global_protect_portal` | (live device state — SSH via --remote; expect device 2FA) |
| `show global-protect-portal global-protect-portal portal` | remote | `panos_show_global_protect_portal` | (live device state — SSH via --remote; expect device 2FA) |
| `show global-protect-portal satellite-cookie-expiration` | remote | `panos_show_global_protect_portal` | (live device state — SSH via --remote; expect device 2FA) |
| `show global-protect-portal satellite-serialnumberip-auth status` | remote | `panos_show_global_protect_portal` | (live device state — SSH via --remote; expect device 2FA) |
| `show global-protect-portal statistics portal` | remote | `panos_show_global_protect_portal` | (live device state — SSH via --remote; expect device 2FA) |
| `show global-protect-portal summary all` | remote | `panos_show_global_protect_portal` | (live device state — SSH via --remote; expect device 2FA) |
| `show global-protect-portal summary detail name` | remote | `panos_show_global_protect_portal` | (live device state — SSH via --remote; expect device 2FA) |
| `show global-protect-satellite current-gateway satellite` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show global-protect-satellite interface` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show global-protect-satellite satellite name` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show gp-broker gpsvc counter` | remote | `panos_show_gp_broker` | (live device state — SSH via --remote; expect device 2FA) |
| `show gp-broker gpsvc task all option` | remote | `panos_show_gp_broker` | (live device state — SSH via --remote; expect device 2FA) |
| `show gp-broker gpsvc task src-ip` | remote | `panos_show_gp_broker` | (live device state — SSH via --remote; expect device 2FA) |
| `show gp-broker gpsvc task task-index` | remote | `panos_show_gp_broker` | (live device state — SSH via --remote; expect device 2FA) |
| `show gp-broker gpsvc task user` | remote | `panos_show_gp_broker` | (live device state — SSH via --remote; expect device 2FA) |
| `show gp-broker gpsvc version` | remote | `panos_show_gp_broker` | (live device state — SSH via --remote; expect device 2FA) |
| `show gp-broker ipc-stat` | remote | `panos_show_gp_broker` | (live device state — SSH via --remote; expect device 2FA) |
| `show gp-broker panos-config` | remote | `panos_show_gp_broker` | (live device state — SSH via --remote; expect device 2FA) |
| `show high-availability` | remote | `panos_show_high_availability` | (live device state — SSH via --remote; expect device 2FA) |
| `show high-availability cluster` | remote | `panos_show_high_availability` | (live device state — SSH via --remote; expect device 2FA) |
| `show high-availability cluster session-synchronization all` | remote | `panos_show_high_availability` | (live device state — SSH via --remote; expect device 2FA) |
| `show high-availability cluster session-synchronization device device-id` | remote | `panos_show_high_availability` | (live device state — SSH via --remote; expect device 2FA) |
| `show high-availability cluster session-synchronization device device-name` | remote | `panos_show_high_availability` | (live device state — SSH via --remote; expect device 2FA) |
| `show high-availability cluster statistics all` | remote | `panos_show_high_availability` | (live device state — SSH via --remote; expect device 2FA) |
| `show high-availability cluster statistics device device-id` | remote | `panos_show_high_availability` | (live device state — SSH via --remote; expect device 2FA) |
| `show high-availability cluster statistics device device-name` | remote | `panos_show_high_availability` | (live device state — SSH via --remote; expect device 2FA) |
| `show high-availability control-link statistics` | remote | `panos_show_high_availability` | (live device state — SSH via --remote; expect device 2FA) |
| `show high-availability interface` | remote | `panos_show_high_availability` | (live device state — SSH via --remote; expect device 2FA) |
| `show high-availability pre-negotiation summary` | remote | `panos_show_high_availability` | (live device state — SSH via --remote; expect device 2FA) |
| `show hsm` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show iot device-inventory all match` | remote | `panos_show_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `show iot device-inventory all match ip` | remote | `panos_show_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `show iot device-inventory summmary` | remote | `panos_show_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `show iot dhcp-server status all` | remote | `panos_show_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `show iot dhcp-server status server` | remote | `panos_show_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `show iot dp-quarantine-cache all option` | remote | `panos_show_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `show iot dp-quarantine-cache ip` | remote | `panos_show_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `show iot eal` | remote | `panos_show_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `show iot eal dpi-stats all` | remote | `panos_show_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `show iot eal dpi-stats subtype` | remote | `panos_show_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `show iot edit-device-inventory id` | remote | `panos_show_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `show iot edit-device-inventory jobs` | remote | `panos_show_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `show iot export-device-inventory all match` | remote | `panos_show_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `show iot export-device-inventory all match ip` | remote | `panos_show_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `show iot host-cache all option` | remote | `panos_show_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `show iot host-cache hostid` | remote | `panos_show_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `show iot icd statistics` | remote | `panos_show_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `show iot icd version` | remote | `panos_show_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `show iot ip-device-mapping all option` | remote | `panos_show_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `show iot ip-device-mapping ip` | remote | `panos_show_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `show iot ip-device-mapping-mp all option` | remote | `panos_show_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `show iot ip-device-mapping-mp ip` | remote | `panos_show_iot` | (live device state — SSH via --remote; expect device 2FA) |
| `show jobs pending` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show jobs processed` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show lacp aggregate-ethernet` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show ldl` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show license-token-files name` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show lldp` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show location ip` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show log` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log alarm` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log alarm csv-output equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log alarm direction equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log alarm dport equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log alarm opaque contains` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log alarm receive_time in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log alarm sport equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log appstat csv-output equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log appstat direction equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log appstat end-time equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log appstat name equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log appstat name not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log appstat query equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log appstat receive_time in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log appstat risk` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log appstat start-time equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log auth` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log auth clienttype equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log auth csv-output equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log auth direction equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log auth ip in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log auth ip not-in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log auth receive_time in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log config client equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log config client not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log config cmd equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log config cmd not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log config csv-output equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log config direction equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log config end-time equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log config query equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log config receive_time in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log config result equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log config result not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log config start-time equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log corr` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log corr csv-output equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log corr direction equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log corr receive_time in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log corr severity` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log corr src in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log corr src not-in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log corr-categ` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log corr-categ csv-output equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log corr-categ direction equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log corr-categ receive_time in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log corr-categ severity` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log corr-categ src in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log corr-categ src not-in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log corr-detail match-oid equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log corr-detail object-name equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log data` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log data action equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log data action not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log data csv-output equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log data direction equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log data dport equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log data dport not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log data dst in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log data dst not-in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log data receive_time in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log data sport equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log data sport not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log data src in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log data src not-in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log data suppress-threatid-mapping equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log decryption` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log decryption action equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log decryption action not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log decryption csv-output equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log decryption direction equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log decryption dport equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log decryption dport not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log decryption dst in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log decryption dst not-in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log decryption ec_curve equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log decryption proxy_type equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log decryption receive_time in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log decryption show-tracker equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log decryption sport equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log decryption sport not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log decryption src in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log decryption src not-in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log decryption tls_auth equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log decryption tls_enc equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log decryption tls_keyxchg equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log decryption tls_version equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log globalprotect` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log globalprotect csv-output equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log globalprotect direction equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log globalprotect machinename contains` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log globalprotect machinename equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log globalprotect machinename not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log globalprotect private_ip equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log globalprotect private_ip in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log globalprotect private_ip not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log globalprotect public_ip equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log globalprotect public_ip in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log globalprotect public_ip not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log globalprotect receive_time equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log globalprotect receive_time in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log globalprotect receive_time not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log hipmatch` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log hipmatch csv-output equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log hipmatch direction equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log hipmatch machinename equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log hipmatch machinename not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log hipmatch matchname equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log hipmatch matchname not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log hipmatch matchtype equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log hipmatch matchtype not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log hipmatch os equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log hipmatch os not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log hipmatch receive_time in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log hipmatch src in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log hipmatch src not-in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log iptag` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log iptag csv-output equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log iptag datasource_subtype equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log iptag datasource_subtype not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log iptag datasource_type equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log iptag datasource_type not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log iptag datasourcename equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log iptag datasourcename not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log iptag direction equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log iptag event_id equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log iptag event_id not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log iptag ip in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log iptag ip not-in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log iptag ip_subnet_range equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log iptag ip_subnet_range not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log iptag receive_time in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log iptag tag_name equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log iptag tag_name not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log mdm receive_time in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log system csv-output equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log system direction equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log system end-time equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log system opaque contains` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log system query equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log system receive_time in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log system severity` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log system start-time equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log threat action equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log threat action not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log threat csv-output equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log threat direction equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log threat dport equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log threat dport not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log threat dst in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log threat dst not-in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log threat pcap-dump equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log threat receive_time in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log threat sport equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log threat sport not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log threat src in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log threat src not-in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log threat suppress-threatid-mapping equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log trace csv-output equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log trace direction equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log trace end-time equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log trace query equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log trace receive_time in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log trace sessionid equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log trace sessionid not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log trace start-time equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log traffic action equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log traffic action not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log traffic csv-output equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log traffic direction equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log traffic dport equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log traffic dport not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log traffic dst in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log traffic dst not-in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log traffic http2_connection equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log traffic http2_connection not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log traffic receive_time in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log traffic session-end-reason equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log traffic session-end-reason not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log traffic show-tracker equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log traffic sport equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log traffic sport not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log traffic src in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log traffic src not-in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log tunnel` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log tunnel action equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log tunnel action not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log tunnel csv-output equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log tunnel direction equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log tunnel dport equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log tunnel dport not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log tunnel dst in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log tunnel dst not-in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log tunnel receive_time in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log tunnel severity` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log tunnel sport equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log tunnel sport not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log tunnel src in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log tunnel src not-in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log url` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log url action equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log url action not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log url csv-output equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log url direction equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log url dport equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log url dport not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log url dst in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log url dst not-in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log url receive_time in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log url sport equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log url sport not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log url src in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log url src not-in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log url suppress-threatid-mapping equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log userid` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log userid beginport equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log userid beginport not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log userid csv-output equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log userid datasource equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log userid datasourcetype equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log userid direction equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log userid endport equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log userid endport not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log userid ip in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log userid ip not-in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log userid receive_time in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log wildfire` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log wildfire category equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log wildfire category not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log wildfire csv-output equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log wildfire direction equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log wildfire dport equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log wildfire dport not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log wildfire dst in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log wildfire dst not-in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log wildfire receive_time in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log wildfire sport equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log wildfire sport not-equal` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log wildfire src in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log wildfire src not-in` | remote | `panos_show_log` | (live device state — SSH via --remote; expect device 2FA) |
| `show log-collector-group` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show logging-status verbose` | device | `panos_show_misc` | (live device state — via the SCM device tunnel; no SSH/2FA) |
| `show logrcvr ip-cache vsys` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show logrcvr offline-logpurger` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show mac` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show macsec association interface` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show macsec stats interface` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show management-clients` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show management-server candidate config-size` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show management-server last-committed config-size` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show max-num-images` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show mgt-config devices` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show mlav` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show neighbor` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show net-inspection details` | remote | `panos_show_net_inspection` | (live device state — SSH via --remote; expect device 2FA) |
| `show net-inspection evaluator index` | remote | `panos_show_net_inspection` | (live device state — SSH via --remote; expect device 2FA) |
| `show net-inspection evaluator zone` | remote | `panos_show_net_inspection` | (live device state — SSH via --remote; expect device 2FA) |
| `show net-inspection exempt` | remote | `panos_show_net_inspection` | (live device state — SSH via --remote; expect device 2FA) |
| `show net-inspection filter index` | remote | `panos_show_net_inspection` | (live device state — SSH via --remote; expect device 2FA) |
| `show net-inspection filter rule-name` | remote | `panos_show_net_inspection` | (live device state — SSH via --remote; expect device 2FA) |
| `show net-inspection filter zone` | remote | `panos_show_net_inspection` | (live device state — SSH via --remote; expect device 2FA) |
| `show net-inspection status` | remote | `panos_show_net_inspection` | (live device state — SSH via --remote; expect device 2FA) |
| `show netstat route` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show ntp` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show object dynamic-address-group all` | remote | `panos_show_object` | (live device state — SSH via --remote; expect device 2FA) |
| `show object dynamic-address-group name` | remote | `panos_show_object` | (live device state — SSH via --remote; expect device 2FA) |
| `show object registered-ip limit` | remote | `panos_show_object` | (live device state — SSH via --remote; expect device 2FA) |
| `show object registered-user all start-point` | remote | `panos_show_object` | (live device state — SSH via --remote; expect device 2FA) |
| `show object registered-user user` | remote | `panos_show_object` | (live device state — SSH via --remote; expect device 2FA) |
| `show object static ip` | remote | `panos_show_object` | (live device state — SSH via --remote; expect device 2FA) |
| `show obsolete-disabled-ssl-exclusions` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show operational-mode` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show oss-license` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show panorama-certificates` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show panorama-status` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show parent-info all` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show parent-info filter saddr` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show parent-info info` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show pbf return-mac all` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show pbf return-mac name` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show pbf rule all detail` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show pbf rule name` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show policy-recommendation iot max-count` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show policy-recommendation saas max-count` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show pppoe inherited state interface` | remote | `panos_show_pppoe` | (live device state — SSH via --remote; expect device 2FA) |
| `show pppoe interface` | remote | `panos_show_pppoe` | (live device state — SSH via --remote; expect device 2FA) |
| `show pppoe ipv6 interface` | remote | `panos_show_pppoe` | (live device state — SSH via --remote; expect device 2FA) |
| `show pppoe ipv6 pool-details` | remote | `panos_show_pppoe` | (live device state — SSH via --remote; expect device 2FA) |
| `show pppoe ipv6 prefix interface` | remote | `panos_show_pppoe` | (live device state — SSH via --remote; expect device 2FA) |
| `show predefined xpath` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show predefined-iot xpath` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show qos interface` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show query corr-detail id` | remote | `panos_show_query` | (live device state — SSH via --remote; expect device 2FA) |
| `show query effective-queries query` | remote | `panos_show_query` | (live device state — SSH via --remote; expect device 2FA) |
| `show query jobs` | remote | `panos_show_query` | (live device state — SSH via --remote; expect device 2FA) |
| `show query result id` | remote | `panos_show_query` | (live device state — SSH via --remote; expect device 2FA) |
| `show query stats` | remote | `panos_show_query` | (live device state — SSH via --remote; expect device 2FA) |
| `show redistribution agent state` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show redistribution agent statistics` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show redistribution service client` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show redistribution service status` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show report cache cache_id` | remote | `panos_show_report` | (live device state — SSH via --remote; expect device 2FA) |
| `show report cache info` | remote | `panos_show_report` | (live device state — SSH via --remote; expect device 2FA) |
| `show report custom` | remote | `panos_show_report` | (live device state — SSH via --remote; expect device 2FA) |
| `show report custom database equal` | remote | `panos_show_report` | (live device state — SSH via --remote; expect device 2FA) |
| `show report custom receive_time in` | remote | `panos_show_report` | (live device state — SSH via --remote; expect device 2FA) |
| `show report directory-listing` | remote | `panos_show_report` | (live device state — SSH via --remote; expect device 2FA) |
| `show report exec_mgr batch_id` | remote | `panos_show_report` | (live device state — SSH via --remote; expect device 2FA) |
| `show report exec_mgr info` | remote | `panos_show_report` | (live device state — SSH via --remote; expect device 2FA) |
| `show report id` | remote | `panos_show_report` | (live device state — SSH via --remote; expect device 2FA) |
| `show report jobs` | remote | `panos_show_report` | (live device state — SSH via --remote; expect device 2FA) |
| `show report predefined end-time equal` | remote | `panos_show_report` | (live device state — SSH via --remote; expect device 2FA) |
| `show report predefined name equal` | remote | `panos_show_report` | (live device state — SSH via --remote; expect device 2FA) |
| `show report predefined start-time equal` | remote | `panos_show_report` | (live device state — SSH via --remote; expect device 2FA) |
| `show resource limit` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show routing bfd active-profile name` | remote | `panos_show_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show routing bfd details virtual-router` | remote | `panos_show_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show routing bfd drop-counters session-id` | remote | `panos_show_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show routing bfd summary virtual-router` | remote | `panos_show_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show routing fib virtual-router` | device | `panos_show_routing` | (live device state — via the SCM device tunnel; no SSH/2FA) |
| `show routing interface` | remote | `panos_show_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show routing multicast fib group` | remote | `panos_show_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show routing multicast group-permission interface` | remote | `panos_show_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show routing multicast igmp interface virtual-router` | remote | `panos_show_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show routing multicast igmp membership interface` | remote | `panos_show_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show routing multicast igmp statistics interface` | remote | `panos_show_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show routing multicast pim elected-bsr` | remote | `panos_show_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show routing multicast pim group-mapping group` | remote | `panos_show_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show routing multicast pim interface virtual-router` | remote | `panos_show_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show routing multicast pim neighbor virtual-router` | remote | `panos_show_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show routing multicast pim state virtual-router` | remote | `panos_show_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show routing multicast pim statistics interface` | remote | `panos_show_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show routing multicast route group` | remote | `panos_show_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show routing path-monitor virtual-router` | remote | `panos_show_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show routing protocol bgp` | remote | `panos_show_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show routing protocol bgp peer peer-name` | remote | `panos_show_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show routing protocol bgp peer-group group-name` | remote | `panos_show_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show routing protocol bgp policy virtual-router` | remote | `panos_show_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show routing protocol bgp summary virtual-router` | remote | `panos_show_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show routing protocol ospf` | remote | `panos_show_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show routing protocol ospfv3` | remote | `panos_show_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show routing protocol ospfv3 dumplsdb scope` | remote | `panos_show_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show routing protocol ospfv3 interface brief` | remote | `panos_show_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show routing protocol ospfv3 lsdb scope` | remote | `panos_show_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show routing protocol ospfv3 neighbor brief` | remote | `panos_show_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show routing protocol ospfv3 virt-neighbor brief` | remote | `panos_show_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show routing protocol redist` | remote | `panos_show_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show routing protocol rip` | remote | `panos_show_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show routing resource` | remote | `panos_show_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show routing route destination` | device | `panos_show_routing` | (live device state — via the SCM device tunnel; no SSH/2FA) |
| `show routing summary virtual-router` | remote | `panos_show_routing` | (live device state — SSH via --remote; expect device 2FA) |
| `show rule-hit-count vsys` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show rule-hit-count vsys all rule-base` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show rule-hit-count vsys list entry` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show rule-hit-count vsys list rule-base` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show running` | remote | `panos_show_running` | (live device state — SSH via --remote; expect device 2FA) |
| `show running appinfo2ip saddr` | remote | `panos_show_running` | (live device state — SSH via --remote; expect device 2FA) |
| `show running application cache all` | remote | `panos_show_running` | (live device state — SSH via --remote; expect device 2FA) |
| `show running application disabled` | remote | `panos_show_running` | (live device state — SSH via --remote; expect device 2FA) |
| `show running application setting` | remote | `panos_show_running` | (live device state — SSH via --remote; expect device 2FA) |
| `show running application statistics` | remote | `panos_show_running` | (live device state — SSH via --remote; expect device 2FA) |
| `show running application-signature statistics` | remote | `panos_show_running` | (live device state — SSH via --remote; expect device 2FA) |
| `show running dns-cache statistics` | remote | `panos_show_running` | (live device state — SSH via --remote; expect device 2FA) |
| `show running global-ippool summary-only` | remote | `panos_show_running` | (live device state — SSH via --remote; expect device 2FA) |
| `show running ipv6 address` | remote | `panos_show_running` | (live device state — SSH via --remote; expect device 2FA) |
| `show running ml-block-cache top` | remote | `panos_show_running` | (live device state — SSH via --remote; expect device 2FA) |
| `show running ml-block-cache url` | remote | `panos_show_running` | (live device state — SSH via --remote; expect device 2FA) |
| `show running mlav-model status` | remote | `panos_show_running` | (live device state — SSH via --remote; expect device 2FA) |
| `show running nat-policy vsys` | remote | `panos_show_running` | (live device state — SSH via --remote; expect device 2FA) |
| `show running nat-rule-ippool rule` | remote | `panos_show_running` | (live device state — SSH via --remote; expect device 2FA) |
| `show running ndp-proxy interface` | remote | `panos_show_running` | (live device state — SSH via --remote; expect device 2FA) |
| `show running network-packet-broker` | remote | `panos_show_running` | (live device state — SSH via --remote; expect device 2FA) |
| `show running persistent-dipp-client ip-utilization pool` | remote | `panos_show_running` | (live device state — SSH via --remote; expect device 2FA) |
| `show running persistent-dipp-client pool` | remote | `panos_show_running` | (live device state — SSH via --remote; expect device 2FA) |
| `show running persistent-dipp-client-translation ip` | remote | `panos_show_running` | (live device state — SSH via --remote; expect device 2FA) |
| `show running persistent-dipp-pool ip-utilization` | remote | `panos_show_running` | (live device state — SSH via --remote; expect device 2FA) |
| `show running resource-monitor day last` | remote | `panos_show_running` | (live device state — SSH via --remote; expect device 2FA) |
| `show running resource-monitor hour last` | remote | `panos_show_running` | (live device state — SSH via --remote; expect device 2FA) |
| `show running resource-monitor ingress-backlogs` | remote | `panos_show_running` | (live device state — SSH via --remote; expect device 2FA) |
| `show running resource-monitor minute last` | remote | `panos_show_running` | (live device state — SSH via --remote; expect device 2FA) |
| `show running resource-monitor second last` | remote | `panos_show_running` | (live device state — SSH via --remote; expect device 2FA) |
| `show running resource-monitor week last` | remote | `panos_show_running` | (live device state — SSH via --remote; expect device 2FA) |
| `show running rule-use highlight vsys` | remote | `panos_show_running` | (live device state — SSH via --remote; expect device 2FA) |
| `show running rule-use hit-count vsys` | remote | `panos_show_running` | (live device state — SSH via --remote; expect device 2FA) |
| `show running security-policy rule-index` | device | `panos_show_running` | (live device state — via the SCM device tunnel; no SSH/2FA) |
| `show running tcp state` | remote | `panos_show_running` | (live device state — SSH via --remote; expect device 2FA) |
| `show running tunnel flow` | remote | `panos_show_running` | (live device state — SSH via --remote; expect device 2FA) |
| `show running tunnel flow all filter type` | remote | `panos_show_running` | (live device state — SSH via --remote; expect device 2FA) |
| `show running tunnel flow context` | remote | `panos_show_running` | (live device state — SSH via --remote; expect device 2FA) |
| `show running tunnel flow name` | remote | `panos_show_running` | (live device state — SSH via --remote; expect device 2FA) |
| `show running tunnel flow tunnel-id` | remote | `panos_show_running` | (live device state — SSH via --remote; expect device 2FA) |
| `show running url` | remote | `panos_show_running` | (live device state — SSH via --remote; expect device 2FA) |
| `show running url-cache` | remote | `panos_show_running` | (live device state — SSH via --remote; expect device 2FA) |
| `show running url-info` | remote | `panos_show_running` | (live device state — SSH via --remote; expect device 2FA) |
| `show sdwan connection` | remote | `panos_show_sdwan` | (live device state — SSH via --remote; expect device 2FA) |
| `show sdwan details` | remote | `panos_show_sdwan` | (live device state — SSH via --remote; expect device 2FA) |
| `show sdwan details basic` | remote | `panos_show_sdwan` | (live device state — SSH via --remote; expect device 2FA) |
| `show sdwan details rule id` | remote | `panos_show_sdwan` | (live device state — SSH via --remote; expect device 2FA) |
| `show sdwan details rule idx` | remote | `panos_show_sdwan` | (live device state — SSH via --remote; expect device 2FA) |
| `show sdwan details session id` | remote | `panos_show_sdwan` | (live device state — SSH via --remote; expect device 2FA) |
| `show sdwan event` | remote | `panos_show_sdwan` | (live device state — SSH via --remote; expect device 2FA) |
| `show sdwan path-monitor details` | remote | `panos_show_sdwan` | (live device state — SSH via --remote; expect device 2FA) |
| `show sdwan path-monitor dia-anypath packet-buffer` | remote | `panos_show_sdwan` | (live device state — SSH via --remote; expect device 2FA) |
| `show sdwan path-monitor parameter active` | remote | `panos_show_sdwan` | (live device state — SSH via --remote; expect device 2FA) |
| `show sdwan path-monitor parameter adaptive` | remote | `panos_show_sdwan` | (live device state — SSH via --remote; expect device 2FA) |
| `show sdwan path-monitor parameter all-dp` | remote | `panos_show_sdwan` | (live device state — SSH via --remote; expect device 2FA) |
| `show sdwan path-monitor parameter conn-idx` | remote | `panos_show_sdwan` | (live device state — SSH via --remote; expect device 2FA) |
| `show sdwan path-monitor parameter path-name` | remote | `panos_show_sdwan` | (live device state — SSH via --remote; expect device 2FA) |
| `show sdwan path-monitor parameter vif` | remote | `panos_show_sdwan` | (live device state — SSH via --remote; expect device 2FA) |
| `show sdwan path-monitor policy-map` | remote | `panos_show_sdwan` | (live device state — SSH via --remote; expect device 2FA) |
| `show sdwan path-monitor stats active` | remote | `panos_show_sdwan` | (live device state — SSH via --remote; expect device 2FA) |
| `show sdwan path-monitor stats adaptive` | remote | `panos_show_sdwan` | (live device state — SSH via --remote; expect device 2FA) |
| `show sdwan path-monitor stats all-dp` | remote | `panos_show_sdwan` | (live device state — SSH via --remote; expect device 2FA) |
| `show sdwan path-monitor stats conn-idx` | remote | `panos_show_sdwan` | (live device state — SSH via --remote; expect device 2FA) |
| `show sdwan path-monitor stats dia-vif` | remote | `panos_show_sdwan` | (live device state — SSH via --remote; expect device 2FA) |
| `show sdwan path-monitor stats path-name` | remote | `panos_show_sdwan` | (live device state — SSH via --remote; expect device 2FA) |
| `show sdwan path-monitor stats vif` | remote | `panos_show_sdwan` | (live device state — SSH via --remote; expect device 2FA) |
| `show sdwan pool details` | remote | `panos_show_sdwan` | (live device state — SSH via --remote; expect device 2FA) |
| `show sdwan rule vif` | remote | `panos_show_sdwan` | (live device state — SSH via --remote; expect device 2FA) |
| `show sdwan session distribution policy-name` | remote | `panos_show_sdwan` | (live device state — SSH via --remote; expect device 2FA) |
| `show sdwan session log session-id` | remote | `panos_show_sdwan` | (live device state — SSH via --remote; expect device 2FA) |
| `show sdwan session path-select session-id` | remote | `panos_show_sdwan` | (live device state — SSH via --remote; expect device 2FA) |
| `show session` | remote | `panos_show_session` | (live device state — SSH via --remote; expect device 2FA) |
| `show session all start-at` | remote | `panos_show_session` | (live device state — SSH via --remote; expect device 2FA) |
| `show session cache all filter from` | remote | `panos_show_session` | (live device state — SSH via --remote; expect device 2FA) |
| `show session cache external md5` | remote | `panos_show_session` | (live device state — SSH via --remote; expect device 2FA) |
| `show session cache md5` | remote | `panos_show_session` | (live device state — SSH via --remote; expect device 2FA) |
| `show session id` | remote | `panos_show_session` | (live device state — SSH via --remote; expect device 2FA) |
| `show session packet-buffer-protection` | remote | `panos_show_session` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared address-group` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared application` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared application-filter` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared external-list` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared post-rulebase` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared post-rulebase application-override rules` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared post-rulebase authentication rules` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared post-rulebase decryption rules` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared post-rulebase default-security-rules rules` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared post-rulebase dos rules` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared post-rulebase nat rules` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared post-rulebase network-packet-broker rules` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared post-rulebase pbf rules` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared post-rulebase qos rules` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared post-rulebase sdwan rules` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared post-rulebase security rules` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared post-rulebase tunnel-inspect rules` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared pre-rulebase` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared pre-rulebase application-override rules` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared pre-rulebase authentication rules` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared pre-rulebase decryption rules` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared pre-rulebase dos rules` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared pre-rulebase nat rules` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared pre-rulebase network-packet-broker rules` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared pre-rulebase pbf rules` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared pre-rulebase qos rules` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared pre-rulebase sdwan rules` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared pre-rulebase security rules` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared pre-rulebase tunnel-inspect rules` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared profiles` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared profiles ai-security` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared profiles data-filtering` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared profiles data-objects` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared profiles decryption` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared profiles dos-protection` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared profiles file-blocking` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared profiles gtp` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared profiles hip-objects` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared profiles host-compliance-objects` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared profiles sctp` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared profiles sdwan-error-correction` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared profiles sdwan-path-quality` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared profiles sdwan-saas-quality` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared profiles sdwan-traffic-distribution` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared profiles spyware` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared profiles url-filtering` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared profiles virus` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared profiles vulnerability` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared profiles wildfire-analysis` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared region` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared schedule` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared service` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared threats` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared threats spyware` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show shared threats vulnerability` | remote | `panos_show_shared` | (live device state — SSH via --remote; expect device 2FA) |
| `show snmpd refresh-timer-period` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show sp-metadata captive-portal authprofile` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show sp-metadata global-protect authprofile` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show sp-metadata management authprofile` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show ssh-fingerprints hash-type` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show ssl-conn-on-cert` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show sslmgr-max-check-cert-jobs` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show sslmgr-store certificate-info issuer` | remote | `panos_show_sslmgr_store` | (live device state — SSH via --remote; expect device 2FA) |
| `show sslmgr-store certificate-info portal name` | remote | `panos_show_sslmgr_store` | (live device state — SSH via --remote; expect device 2FA) |
| `show sslmgr-store config-ca-certificate subjectname-hash` | remote | `panos_show_sslmgr_store` | (live device state — SSH via --remote; expect device 2FA) |
| `show sslmgr-store config-certificate-info db-serialno` | remote | `panos_show_sslmgr_store` | (live device state — SSH via --remote; expect device 2FA) |
| `show sslmgr-store satellite-info portal name` | remote | `panos_show_sslmgr_store` | (live device state — SSH via --remote; expect device 2FA) |
| `show sslmgr-store serialno-certificate-info db-serialno` | remote | `panos_show_sslmgr_store` | (live device state — SSH via --remote; expect device 2FA) |
| `show statistics` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show streaming-telemetry region-list` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show syslog-ssl-conn-validation` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show system` | remote | `panos_show_system` | (live device state — SSH via --remote; expect device 2FA) |
| `show system crypto entropy-status` | remote | `panos_show_system` | (live device state — SSH via --remote; expect device 2FA) |
| `show system disk-space files` | remote | `panos_show_system` | (live device state — SSH via --remote; expect device 2FA) |
| `show system environmentals fans slot` | remote | `panos_show_system` | (live device state — SSH via --remote; expect device 2FA) |
| `show system environmentals power slot` | remote | `panos_show_system` | (live device state — SSH via --remote; expect device 2FA) |
| `show system environmentals slot` | remote | `panos_show_system` | (live device state — SSH via --remote; expect device 2FA) |
| `show system environmentals thermal slot` | remote | `panos_show_system` | (live device state — SSH via --remote; expect device 2FA) |
| `show system resources follow` | remote | `panos_show_system` | (live device state — SSH via --remote; expect device 2FA) |
| `show system setting` | remote | `panos_show_system` | (live device state — SSH via --remote; expect device 2FA) |
| `show system setting ctd` | remote | `panos_show_system` | (live device state — SSH via --remote; expect device 2FA) |
| `show system setting ctd threat id` | remote | `panos_show_system` | (live device state — SSH via --remote; expect device 2FA) |
| `show system setting logging log-compression` | remote | `panos_show_system` | (live device state — SSH via --remote; expect device 2FA) |
| `show system setting ssl-decrypt` | remote | `panos_show_system` | (live device state — SSH via --remote; expect device 2FA) |
| `show system setting ssl-decrypt exclude-cache xml yes` | remote | `panos_show_system` | (live device state — SSH via --remote; expect device 2FA) |
| `show system setting ssl-decrypt gp-cookie-cache user` | remote | `panos_show_system` | (live device state — SSH via --remote; expect device 2FA) |
| `show system setting ssl-decrypt memory detail` | remote | `panos_show_system` | (live device state — SSH via --remote; expect device 2FA) |
| `show system setting url-cache` | remote | `panos_show_system` | (live device state — SSH via --remote; expect device 2FA) |
| `show system state browser` | remote | `panos_show_system` | (live device state — SSH via --remote; expect device 2FA) |
| `show system state filter` | remote | `panos_show_system` | (live device state — SSH via --remote; expect device 2FA) |
| `show system state filter-pretty` | remote | `panos_show_system` | (live device state — SSH via --remote; expect device 2FA) |
| `show system statistics` | remote | `panos_show_system` | (live device state — SSH via --remote; expect device 2FA) |
| `show threat id` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show transceiver` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show transceiver-detail` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show transceiver-eeprom` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show transceiver-monitor-rate` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show tunnel-acceleration` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show upgrade-history` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show url-cloud status` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show user cloud-identity-engine client statistics` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user cloud-identity-engine statistics all` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user cloud-identity-engine statistics name` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user cloud-identity-engine status all` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user cloud-identity-engine status name` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user cookie-surrogate-cache-dp all` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user cookie-surrogate-cache-dp username` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user credential-filter` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user email-lookup email` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user group name` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user group-mapping naming-context server` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user group-mapping state` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user group-mapping statistics` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user group-mapping-service query` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user group-mapping-service status` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user group-policy-dp` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user group-policy-dp gid` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user group-selection sp_vsys_id` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user hip-report user` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user ip-port-user-mapping all` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user ip-port-user-mapping ip` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user ip-port-user-mapping source-user` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user ip-port-user-mapping-mp all` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user ip-port-user-mapping-mp ip` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user ip-port-user-mapping-mp source-user` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user ip-user-mapping all option` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user ip-user-mapping ip` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user ip-user-mapping-mp limit` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user ldap-device-serialno all` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user ldap-device-serialno serialno` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user local-user-db vsys` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user server-monitor auto-discover domain` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user server-monitor state` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user server-monitor statistics` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user ts-agent state` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user ts-agent statistics` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user uid2primeuid-dp all` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user uid2primeuid-dp uid` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user user-attributes user` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user user-cache-dp all` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user user-cache-dp uid` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user user-id-agent config all` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user user-id-agent config name` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user user-id-agent state` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user user-id-agent statistics` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user user-id-service client` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user user-id-service ipuser-update-list option` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user user-id-service status` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user user-ids all option` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user user-ids match-user` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user user-policy-dp all` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user user-policy-dp uid` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show user xml-api multiusersystem` | remote | `panos_show_user` | (live device state — SSH via --remote; expect device 2FA) |
| `show virtual-wire` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show vlan` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show vm-monitor source all` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show vm-monitor source state` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show vm-monitor source statistics` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show vpn flow name` | remote | `panos_show_vpn` | (live device state — SSH via --remote; expect device 2FA) |
| `show vpn flow tunnel-id` | remote | `panos_show_vpn` | (live device state — SSH via --remote; expect device 2FA) |
| `show vpn gateway match` | remote | `panos_show_vpn` | (live device state — SSH via --remote; expect device 2FA) |
| `show vpn gateway name` | remote | `panos_show_vpn` | (live device state — SSH via --remote; expect device 2FA) |
| `show vpn ike-hashurl` | remote | `panos_show_vpn` | (live device state — SSH via --remote; expect device 2FA) |
| `show vpn ike-sa detail gateway` | remote | `panos_show_vpn` | (live device state — SSH via --remote; expect device 2FA) |
| `show vpn ike-sa gateway` | remote | `panos_show_vpn` | (live device state — SSH via --remote; expect device 2FA) |
| `show vpn ike-sa match` | remote | `panos_show_vpn` | (live device state — SSH via --remote; expect device 2FA) |
| `show vpn ipsec-sa match` | remote | `panos_show_vpn` | (live device state — SSH via --remote; expect device 2FA) |
| `show vpn ipsec-sa summary` | remote | `panos_show_vpn` | (live device state — SSH via --remote; expect device 2FA) |
| `show vpn ipsec-sa tunnel` | remote | `panos_show_vpn` | (live device state — SSH via --remote; expect device 2FA) |
| `show vpn tunnel match` | remote | `panos_show_vpn` | (live device state — SSH via --remote; expect device 2FA) |
| `show vpn tunnel name` | remote | `panos_show_vpn` | (live device state — SSH via --remote; expect device 2FA) |
| `show wildfire` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show wildfire-appliance-cluster` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show wildfire-realtime-cache total` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show wildfire-realtime-cache virus-pattern-type` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show wildfire-realtime-cloud-status` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show wildfire-realtime-stats` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `show zone-protection zone` | remote | `panos_show_misc` | (live device state — SSH via --remote; expect device 2FA) |
| `ssh inet` | remote | `panos_ssh` | (live device state — SSH via --remote; expect device 2FA) |
| `tail follow` | remote | `panos_tail` | (live device state — SSH via --remote; expect device 2FA) |
| `target set` | remote | `panos_target` | (live device state — SSH via --remote; expect device 2FA) |
| `target show` | remote | `panos_target` | (live device state — SSH via --remote; expect device 2FA) |
| `test advanced-routing bgp logical-router` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test advanced-routing fib-lookup ip` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test advanced-routing mfib-lookup group` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test advanced-routing multicast msdp logical-router` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test arp gratuitous interface` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test authentication authentication-profile` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test authentication-policy-match from` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test botnet domain` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test cookie-surrogate username` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test custom-signature-perf pattern` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test custom-signature-type pattern` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test custom-url url` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test data-filtering ccn` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test data-filtering pattern` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test data-filtering ssn` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test decryption-policy-match from` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test dns-proxy ddns update interface name` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test dns-proxy dns-signature fqdn` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test dns-proxy fqdn refresh all` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test dns-proxy fqdn refresh entry fqdn` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test dns-proxy query name` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test dos-policy-match from` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test generate-saml-url captive-portal vsys` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test generate-saml-url global-protect vsys` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test generate-saml-url management interface` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test global-protect-mdm hipreport request mobile-id` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test global-protect-satellite gateway-connect satellite` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test global-protect-satellite gateway-disconnect satellite` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test global-protect-satellite gateway-reconnect satellite` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test http-profile vsys` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test http-profile-server-auth-token vsys` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test http-server vsys` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test macsec association interface` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test mfa-vendors mfa-server-profile` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test nat-policy-match from` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test nd router-advertisement interface` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test nptv6 cks-neutral dest-network` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test pbf-policy-match from` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test pppoe interface` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test pppoe ipv6 interface` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test qos-policy-match from` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test routing bgp virtual-router` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test routing fib-lookup ip` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test routing mfib-lookup group` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test routing ospf logical-router` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test routing ospfv3 logical-router` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test scp-server-connection confirm hostname` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test scp-server-connection initiate hostname` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test security-policy-match from` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test smtp-server vsys` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test ssl-exclude-list predefined hostname` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test ssl-exclude-list shared hostname` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test ssl-exclude-list vsys hostname` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test stats-service` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test tag-filter` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test threat-vault connection` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test uid` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test url-info-cloud` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test url-info-host` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test url-wpc` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test user-id custom-group group-mapping` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test user-id user-id-syslog-parse field-identifier event-string` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test user-id user-id-syslog-parse regex-identifier event-regex` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test uuid enable` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test vpn ike-sa gateway` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test vpn ipsec-sa tunnel` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test wildfire registration channel` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `test x-authenticated-user ip` | remote | `panos_test` | (live device state — SSH via --remote; expect device 2FA) |
| `tftp export` | remote | `panos_tftp` | (live device state — SSH via --remote; expect device 2FA) |
| `tftp export core-file data-plane from` | remote | `panos_tftp` | (live device state — SSH via --remote; expect device 2FA) |
| `tftp export core-file large-corefile from` | remote | `panos_tftp` | (live device state — SSH via --remote; expect device 2FA) |
| `tftp export core-file management-plane from` | remote | `panos_tftp` | (live device state — SSH via --remote; expect device 2FA) |
| `tftp export debug bootmem_file from` | remote | `panos_tftp` | (live device state — SSH via --remote; expect device 2FA) |
| `tftp export log-file data-plane to` | remote | `panos_tftp` | (live device state — SSH via --remote; expect device 2FA) |
| `tftp export log-file management-plane to` | remote | `panos_tftp` | (live device state — SSH via --remote; expect device 2FA) |
| `tftp export stats-dump to` | remote | `panos_tftp` | (live device state — SSH via --remote; expect device 2FA) |
| `tftp export threat-pcap pcap-id` | remote | `panos_tftp` | (live device state — SSH via --remote; expect device 2FA) |
| `tftp import` | remote | `panos_tftp` | (live device state — SSH via --remote; expect device 2FA) |
| `tftp import certificate from` | remote | `panos_tftp` | (live device state — SSH via --remote; expect device 2FA) |
| `tftp import keypair from` | remote | `panos_tftp` | (live device state — SSH via --remote; expect device 2FA) |
| `tftp import private-key from` | remote | `panos_tftp` | (live device state — SSH via --remote; expect device 2FA) |
| `traceroute ipv4` | remote | `panos_traceroute` | (live device state — SSH via --remote; expect device 2FA) |

## Posture

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `delete posture definitions` | global | `posture_definitions_write` | DELETE https://api.strata.paloaltonetworks.com/posture/compliance-frameworks/v1/definitions/{id} |
| `delete posture root` | global | `posture_root_write` | DELETE https://api.strata.paloaltonetworks.com/posture/checks/v1/{id} |
| `set posture batch-delete` | global | `posture_batch_delete_write` | POST https://api.strata.paloaltonetworks.com/posture/checks/v1/batch-delete |
| `set posture batch-upsert` | global | `posture_batch_upsert_write` | POST https://api.strata.paloaltonetworks.com/posture/checks/v1/batch-upsert |
| `set posture benchmark-monitoring` | global | `posture_benchmark_monitoring_write` | POST https://api.strata.paloaltonetworks.com/posture/compliance-frameworks/v1/benchmark-monitoring |
| `set posture benchmark-monitoring download` | global | `posture_benchmark_monitoring_download_write` | POST https://api.strata.paloaltonetworks.com/posture/compliance-frameworks/v1/benchmark-monitoring/download |
| `set posture clone` | global | `posture_clone_write` | POST https://api.strata.paloaltonetworks.com/posture/checks/v1/{id}:clone |
| `set posture definitions` | global | `posture_definitions_write` | POST https://api.strata.paloaltonetworks.com/posture/compliance-frameworks/v1/definitions |
| `set posture definitions benchmark` | global | `posture_definitions_benchmark_write` | POST https://api.strata.paloaltonetworks.com/posture/compliance-frameworks/v1/definitions/{id}:benchmark |
| `set posture definitions clone` | global | `posture_definitions_clone_write` | POST https://api.strata.paloaltonetworks.com/posture/compliance-frameworks/v1/definitions/{id}:clone |
| `set posture definitions un-benchmark` | global | `posture_definitions_un_benchmark_write` | POST https://api.strata.paloaltonetworks.com/posture/compliance-frameworks/v1/definitions/{id}:un-benchmark |
| `set posture reports config-file-upload` | global | `posture_reports_config_file_upload_write` | POST https://api.strata.paloaltonetworks.com/posture/checks/v1/reports/config-file-upload |
| `set posture root` | global | `posture_root_write` | POST https://api.strata.paloaltonetworks.com/posture/checks/v1 |
| `show posture compliance-controls id` | global | `posture_compliance_controls_read` | GET https://api.strata.paloaltonetworks.com/posture/compliance-frameworks/v1/compliance-controls/{id} |
| `show posture configurations-assessed id` | global | `posture_configurations_assessed_read` | GET https://api.strata.paloaltonetworks.com/posture/compliance-frameworks/v1/configurations-assessed/{id} |
| `show posture definitions` | global | `posture_definitions_read` | GET https://api.strata.paloaltonetworks.com/posture/compliance-frameworks/v1/definitions |
| `show posture definitions id` | global | `posture_definitions_read` | GET https://api.strata.paloaltonetworks.com/posture/compliance-frameworks/v1/definitions/{id} |
| `show posture id` | global | `posture_read` | GET https://api.strata.paloaltonetworks.com/posture/checks/v1/{id} |
| `show posture overall-compliance id` | global | `posture_overall_compliance_read` | GET https://api.strata.paloaltonetworks.com/posture/compliance-frameworks/v1/overall-compliance/{id} |
| `show posture overall-compliance-timeline id` | global | `posture_overall_compliance_timeline_read` | GET https://api.strata.paloaltonetworks.com/posture/compliance-frameworks/v1/overall-compliance-timeline/{id} |
| `show posture reports bpa-result id` | global | `posture_reports_bpa_result_read` | GET https://api.strata.paloaltonetworks.com/posture/checks/v1/reports/{id}/bpa-result |
| `show posture root` | global | `posture_root_read` | GET https://api.strata.paloaltonetworks.com/posture/checks/v1 |
| `show posture summaries` | global | `posture_summaries_read` | GET https://api.strata.paloaltonetworks.com/posture/compliance-frameworks/v1/summaries |
| `update posture definitions` | global | `posture_definitions_write` | PUT https://api.strata.paloaltonetworks.com/posture/compliance-frameworks/v1/definitions/{id} |
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
| `update security-rule` | folder | `update_security` | — |

## Setup

| Command | Scope | Feature flag | SCM API |
|---|---|---|---|
| `delete snippet` | global | `show_snippets` | — |
| `set snippet` | global | `show_snippets` | — |
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
