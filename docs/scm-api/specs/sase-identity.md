# Identity Services

**Version:** 2.0.0  
**Source:** `openapi-specs/scm/config/sase/identity/identity-services-march.yaml`  
**Base URL:** `https://api.strata.paloaltonetworks.com/config/identity/v1`  
**Endpoints:** 88  
**GitHub:** https://github.com/PaloAltoNetworks/pan.dev/blob/master/openapi-specs/scm/config/sase/identity/identity-services-march.yaml

---

## Endpoints

### `GET /authentication-rules`

**Summary:** List authentication rules  
**Operation ID:** `ListAuthenticationRules`  
**Tags:** Authentication Rules  
**Container scope:** folder | snippet | device  
**Query params:** name, position, limit, offset  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /authentication-rules`

**Summary:** Create an authentication rule  
**Operation ID:** `CreateAuthenticationRules`  
**Tags:** Authentication Rules  
**Container scope:** folder | snippet | device (in request body)  
**Query params:** position  
**Body schema:** `authentication-rules`  
**Required fields:** `name`, `from`, `to`, `source`, `destination`, `service`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /authentication-rules/{id}`

**Summary:** Get an authentication rule  
**Operation ID:** `GetAuthenticationRulesByID`  
**Tags:** Authentication Rules  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /authentication-rules/{id}`

**Summary:** Update an authentication rule  
**Operation ID:** `UpdateAuthenticationRulesByID`  
**Tags:** Authentication Rules  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `authentication-rules`  
**Required fields:** `name`, `from`, `to`, `source`, `destination`, `service`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /authentication-rules/{id}`

**Summary:** Delete an authentication rule  
**Operation ID:** `DeleteAuthenticationRulesByID`  
**Tags:** Authentication Rules  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `POST /authentication-rules/{id}:move`

**Summary:** Move an authentication rule  
**Operation ID:** `MoveAuthenticationRulesByID`  
**Tags:** Authentication Rules  
**Body schema:** `rule-based-move`  
**Required fields:** `destination`, `rulebase`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /authentication-portals`

**Summary:** List authentication portals  
**Operation ID:** `ListAuthenticationPortals`  
**Tags:** Authentication Portals  
**Container scope:** folder | snippet | device  
**Query params:** name, limit, offset  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /authentication-portals`

**Summary:** Create an authentication portal  
**Operation ID:** `CreateAuthenticationPortals`  
**Tags:** Authentication Portals  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `authentication-portals`  
**Required fields:** `redirect_host`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /authentication-portals/{id}`

**Summary:** Get an authentication portal  
**Operation ID:** `GetAuthenticationPortalsByID`  
**Tags:** Authentication Portals  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /authentication-portals/{id}`

**Summary:** Update an authentication portal  
**Operation ID:** `UpdateAuthenticationPortalsByID`  
**Tags:** Authentication Portals  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `authentication-portals`  
**Required fields:** `redirect_host`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /authentication-portals/{id}`

**Summary:** Delete an authentication portal  
**Operation ID:** `DeleteAuthenticationPortalsByID`  
**Tags:** Authentication Portals  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /authentication-profiles`

**Summary:** List authentication profiles  
**Operation ID:** `ListAuthenticationProfiles`  
**Tags:** Authentication Profiles  
**Container scope:** folder | snippet | device  
**Query params:** name, limit, offset  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /authentication-profiles`

**Summary:** Create an authentication profile  
**Operation ID:** `CreateAuthenticationProfiles`  
**Tags:** Authentication Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `authentication-profiles`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /authentication-profiles/{id}`

**Summary:** Get an authentication profile  
**Operation ID:** `GetAuthenticationProfilesByID`  
**Tags:** Authentication Profiles  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /authentication-profiles/{id}`

**Summary:** Update an authentication profile  
**Operation ID:** `UpdateAuthenticationProfilesByID`  
**Tags:** Authentication Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `authentication-profiles`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /authentication-profiles/{id}`

**Summary:** Delete an authentication profile  
**Operation ID:** `DeleteAuthenticationProfilesByID`  
**Tags:** Authentication Profiles  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /local-users`

**Summary:** List local users  
**Operation ID:** `ListLocalUsers`  
**Tags:** Local Users  
**Container scope:** folder | snippet | device  
**Query params:** name, limit, offset  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /local-users`

**Summary:** Create a local user  
**Operation ID:** `CreateLocalUsers`  
**Tags:** Local Users  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `local-users`  
**Required fields:** `id`, `name`, `password`  
**Response codes:** 200, 400, 401, 403, 409, default

### `GET /local-users/{id}`

**Summary:** Get a local user  
**Operation ID:** `GetLocalUsersByID`  
**Tags:** Local Users  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /local-users/{id}`

**Summary:** Update a local user  
**Operation ID:** `UpdateLocalUsersByID`  
**Tags:** Local Users  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `local-users`  
**Required fields:** `id`, `name`, `password`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /local-users/{id}`

**Summary:** Delete a local user  
**Operation ID:** `DeleteLocalUsersByID`  
**Tags:** Local Users  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /local-user-groups`

**Summary:** List local user groups  
**Operation ID:** `ListLocalUserGroups`  
**Tags:** Local User Groups  
**Container scope:** folder | snippet | device  
**Query params:** name, limit, offset  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /local-user-groups`

**Summary:** Create a local user group  
**Operation ID:** `CreateLocalUserGroups`  
**Tags:** Local User Groups  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `local-user-groups`  
**Required fields:** `id`, `name`  
**Response codes:** 200, 400, 401, 403, 409, default

### `GET /local-user-groups/{id}`

**Summary:** Get a local user group  
**Operation ID:** `GetLocalUserGroupsByID`  
**Tags:** Local User Groups  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /local-user-groups/{id}`

**Summary:** Update a local user group  
**Operation ID:** `UpdateLocalUserGroupsByID`  
**Tags:** Local User Groups  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `local-user-groups`  
**Required fields:** `id`, `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /local-user-groups/{id}`

**Summary:** Delete a local user group  
**Operation ID:** `DeleteLocalUserGroupsByID`  
**Tags:** Local User Groups  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /saml-server-profiles`

**Summary:** List SAML server profiles  
**Operation ID:** `ListSAMLServerProfiles`  
**Tags:** SAML Server Profiles  
**Container scope:** folder | snippet | device  
**Query params:** name, limit, offset  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /saml-server-profiles`

**Summary:** Create a SAML server profile  
**Operation ID:** `CreateSAMLServerProfiles`  
**Tags:** SAML Server Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `saml-server-profiles`  
**Required fields:** `id`, `name`, `entity_id`, `certificate`, `sso_bindings`, `sso_url`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /saml-server-profiles/{id}`

**Summary:** Get a SAML server profile  
**Operation ID:** `GetSAMLServerProfilesByID`  
**Tags:** SAML Server Profiles  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /saml-server-profiles/{id}`

**Summary:** Update a SAML server profile  
**Operation ID:** `UpdateSAMLServerProfilesByID`  
**Tags:** SAML Server Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `saml-server-profiles`  
**Required fields:** `id`, `name`, `entity_id`, `certificate`, `sso_bindings`, `sso_url`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /saml-server-profiles/{id}`

**Summary:** Delete a SAML server profile  
**Operation ID:** `DeleteSAMLServerProfilesByID`  
**Tags:** SAML Server Profiles  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /ldap-server-profiles`

**Summary:** List LDAP server profiles  
**Operation ID:** `ListLDAPServerProfiles`  
**Tags:** LDAP Server Profiles  
**Container scope:** folder | snippet | device  
**Query params:** name, limit, offset  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /ldap-server-profiles`

**Summary:** Create an LDAP server profile  
**Operation ID:** `CreateLDAPServerProfiles`  
**Tags:** LDAP Server Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `ldap-server-profiles`  
**Required fields:** `id`, `name`, `server`  
**Response codes:** 200, 400, 401, 403, 409, default

### `GET /ldap-server-profiles/{id}`

**Summary:** Get an LDAP server profile  
**Operation ID:** `GetLDAPServerProfilesByID`  
**Tags:** LDAP Server Profiles  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /ldap-server-profiles/{id}`

**Summary:** Update an LDAP server profile  
**Operation ID:** `UpdateLDAPServerProfiles`  
**Tags:** LDAP Server Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `ldap-server-profiles`  
**Required fields:** `id`, `name`, `server`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /ldap-server-profiles/{id}`

**Summary:** Delete an LDAP server profile  
**Operation ID:** `DeleteLDAPServerProfilesByID`  
**Tags:** LDAP Server Profiles  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /radius-server-profiles`

**Summary:** List RADIUS server profiles  
**Operation ID:** `ListRADIUSServerProfiles`  
**Tags:** RADIUS Server Profiles  
**Container scope:** folder | snippet | device  
**Query params:** name, limit, offset  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /radius-server-profiles`

**Summary:** Create a RADIUS server profile  
**Operation ID:** `CreateRADIUSServerProfiles`  
**Tags:** RADIUS Server Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `radius-server-profiles`  
**Required fields:** `name`, `server`, `protocol`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /radius-server-profiles/{id}`

**Summary:** Get a RADIUS server profile  
**Operation ID:** `GetRADIUSServerProfilesByID`  
**Tags:** RADIUS Server Profiles  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /radius-server-profiles/{id}`

**Summary:** Update a RADIUS server profile  
**Operation ID:** `UpdateRADIUSServerProfilesByID`  
**Tags:** RADIUS Server Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `radius-server-profiles`  
**Required fields:** `name`, `server`, `protocol`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /radius-server-profiles/{id}`

**Summary:** Delete a RADIUS server profile  
**Operation ID:** `DeleteRADIUSServerProfilesByID`  
**Tags:** RADIUS Server Profiles  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /tacacs-server-profiles`

**Summary:** List TACACS server profiles  
**Operation ID:** `ListTACACSServerProfiles`  
**Tags:** TACACS Server Profiles  
**Container scope:** folder | snippet | device  
**Query params:** name, limit, offset  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /tacacs-server-profiles`

**Summary:** Create a TACACS server profile  
**Operation ID:** `CreateTACACSServerProfiles`  
**Tags:** TACACS Server Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `tacacs-server-profiles`  
**Required fields:** `id`, `name`, `server`, `protocol`  
**Response codes:** 200, 400, 401, 403, 409, default

### `GET /tacacs-server-profiles/{id}`

**Summary:** Get a TACACS server profile  
**Operation ID:** `GetTACACSServerProfilesByID`  
**Tags:** TACACS Server Profiles  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /tacacs-server-profiles/{id}`

**Summary:** Update a TACACS server profile  
**Operation ID:** `UpdateTACACSServerProfilesByID`  
**Tags:** TACACS Server Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `tacacs-server-profiles`  
**Required fields:** `id`, `name`, `server`, `protocol`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /tacacs-server-profiles/{id}`

**Summary:** Delete a TACACS server profile  
**Operation ID:** `DeleteTACACSServerProfilesByID`  
**Tags:** TACACS Server Profiles  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /kerberos-server-profiles`

**Summary:** List Kerberos server profiles  
**Operation ID:** `ListKerberosServerProfiles`  
**Tags:** Kerberos Server Profiles  
**Container scope:** folder | snippet | device  
**Query params:** name, limit, offset  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /kerberos-server-profiles`

**Summary:** Create a Kerberos server profile  
**Operation ID:** `CreateKerberosServerProfiles`  
**Tags:** Kerberos Server Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `kerberos-server-profiles`  
**Required fields:** `id`, `name`, `server`  
**Response codes:** 200, 400, 401, 403, 409, default

### `GET /kerberos-server-profiles/{id}`

**Summary:** Get a Kerberos server profile  
**Operation ID:** `GetKerberosServerProfilesByID`  
**Tags:** Kerberos Server Profiles  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /kerberos-server-profiles/{id}`

**Summary:** Update a Kerberos server profile  
**Operation ID:** `UpdateKerberosServerProfilesByID`  
**Tags:** Kerberos Server Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `kerberos-server-profiles`  
**Required fields:** `id`, `name`, `server`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /kerberos-server-profiles/{id}`

**Summary:** Delete a Kerberos server profile  
**Operation ID:** `DeleteKerberosServerProfilesByID`  
**Tags:** Kerberos Server Profiles  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /authentication-sequences`

**Summary:** List authentication sequences  
**Operation ID:** `ListAuthenticationSequences`  
**Tags:** Authentication Sequences  
**Container scope:** folder | snippet | device  
**Query params:** name, limit, offset  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /authentication-sequences`

**Summary:** Create an authentication sequence  
**Operation ID:** `CreateAuthenticationSequences`  
**Tags:** Authentication Sequences  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `authentication-sequences`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /authentication-sequences/{id}`

**Summary:** Get an authentication sequence  
**Operation ID:** `GetAuthenticationSequencesByID`  
**Tags:** Authentication Sequences  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /authentication-sequences/{id}`

**Summary:** Update an authentication sequence  
**Operation ID:** `UpdateAuthenticationSequencesByID`  
**Tags:** Authentication Sequences  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `authentication-sequences`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /authentication-sequences/{id}`

**Summary:** Delete an authentication sequence  
**Operation ID:** `DeleteAuthenticationSequencesByID`  
**Tags:** Authentication Sequences  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /mfa-servers`

**Summary:** List MFA servers  
**Operation ID:** `ListMFAServers`  
**Tags:** MFA Servers  
**Container scope:** folder | snippet | device  
**Query params:** name, position, limit, offset  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /mfa-servers`

**Summary:** Create an MFA server  
**Operation ID:** `CreateMFAServers`  
**Tags:** MFA Servers  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `mfa-servers`  
**Required fields:** `name`, `mfa_cert_profile`  
**Response codes:** 200, 400, 401, 403, 409, default

### `GET /mfa-servers/{id}`

**Summary:** Get an MFA server  
**Operation ID:** `GetMFAServersByID`  
**Tags:** MFA Servers  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /mfa-servers/{id}`

**Summary:** Update an MFA server  
**Operation ID:** `UpdateMFAServersByID`  
**Tags:** MFA Servers  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `mfa-servers`  
**Required fields:** `name`, `mfa_cert_profile`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /mfa-servers/{id}`

**Summary:** Delete an MFA server  
**Operation ID:** `DeleteMFAServersByID`  
**Tags:** MFA Servers  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /certificates`

**Summary:** List certificates  
**Operation ID:** `ListCertificates`  
**Tags:** Certificates  
**Container scope:** folder | snippet | device  
**Query params:** name, limit, offset  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /certificates`

**Summary:** Generate a certificate  
**Operation ID:** `CreateCertificates`  
**Tags:** Certificates  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `certificates-post`  
**Required fields:** `id`, `name`, `common_name`, `signed_by`, `algorithm`, `certificate_name`, `digest`  
**Response codes:** 201, 400, 401, 403, 409, default

### `POST /certificates:import`

**Summary:** Import a certificate  
**Operation ID:** `ImportCertificates`  
**Tags:** Certificates  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `certificates-import`  
**Required fields:** `name`, `certificate_file`, `format`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /certificates/{id}`

**Summary:** Get a certificate  
**Operation ID:** `GetCertificatesByID`  
**Tags:** Certificates  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /certificates/{id}`

**Summary:** Delete a certificate  
**Operation ID:** `DeleteCertificatesByID`  
**Tags:** Certificates  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `POST /certificates/{id}:export`

**Summary:** Export a certificate  
**Operation ID:** `ExportCertificateByID`  
**Tags:** Certificates  
**Body schema:** `export-certificate-payload`  
**Required fields:** `format`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /certificate-profiles`

**Summary:** List certificate profiles  
**Operation ID:** `ListCertificateProfiles`  
**Tags:** Certificate Profiles  
**Container scope:** folder | snippet | device  
**Query params:** name, limit, offset  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /certificate-profiles`

**Summary:** Create a certificate profile  
**Operation ID:** `CreateCertificateProfiles`  
**Tags:** Certificate Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `certificate-profiles`  
**Required fields:** `name`, `ca_certificates`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /certificate-profiles/{id}`

**Summary:** Get a certificate profile  
**Operation ID:** `GetCertificateProfilesByID`  
**Tags:** Certificate Profiles  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /certificate-profiles/{id}`

**Summary:** Update a certificate profile  
**Operation ID:** `UpdateCertificateProfilesByID`  
**Tags:** Certificate Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `certificate-profiles`  
**Required fields:** `name`, `ca_certificates`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /certificate-profiles/{id}`

**Summary:** Delete a certificate profile  
**Operation ID:** `DeleteCertificateProfilesByID`  
**Tags:** Certificate Profiles  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /scep-profiles`

**Summary:** List SCEP profiles  
**Operation ID:** `ListSCEPProfiles`  
**Tags:** SCEP Profiles  
**Container scope:** folder | snippet | device  
**Query params:** name, limit, offset  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /scep-profiles`

**Summary:** Create a SCEP profile  
**Operation ID:** `CreateSCEPProfiles`  
**Tags:** SCEP Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `scep-profiles`  
**Required fields:** `id`, `name`, `scep_challenge`, `scep_url`, `ca_identity_name`, `subject`, `algorithm`, `digest`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /scep-profiles/{id}`

**Summary:** Get a SCEP profile  
**Operation ID:** `GetSCEPProfilesByID`  
**Tags:** SCEP Profiles  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /scep-profiles/{id}`

**Summary:** Update a SCEP profile  
**Operation ID:** `UpdateSCEPProfilesByID`  
**Tags:** SCEP Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `scep-profiles`  
**Required fields:** `id`, `name`, `scep_challenge`, `scep_url`, `ca_identity_name`, `subject`, `algorithm`, `digest`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /scep-profiles/{id}`

**Summary:** Delete a SCEP profile  
**Operation ID:** `DeleteSCEPProfilesByID`  
**Tags:** SCEP Profiles  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /trusted-certificate-authorities`

**Summary:** List trusted certificate authorities  
**Operation ID:** `ListTrustedCertificateAuthorities`  
**Tags:** Trusted Certificate Authorities  
**Container scope:** folder | snippet | device  
**Query params:** name, limit, offset  
**Response codes:** 200, 400, 401, 403, 404, default

### `GET /tls-service-profiles`

**Summary:** List TLS service profiles  
**Operation ID:** `ListTLSServiceProfiles`  
**Tags:** TLS Service Profiles  
**Container scope:** folder | snippet | device  
**Query params:** name, limit, offset  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /tls-service-profiles`

**Summary:** Create a TLS service profile  
**Operation ID:** `CreateTLSServiceProfiles`  
**Tags:** TLS Service Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `tls-service-profiles`  
**Required fields:** `id`, `name`, `certificate`, `protocol_settings`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /tls-service-profiles/{id}`

**Summary:** Get a TLS service profile  
**Operation ID:** `GetTLSServiceProfilesByID`  
**Tags:** TLS Service Profiles  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /tls-service-profiles/{id}`

**Summary:** Update a TLS service profile  
**Operation ID:** `UpdateTLSServiceProfilesByID`  
**Tags:** TLS Service Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `tls-service-profiles`  
**Required fields:** `id`, `name`, `certificate`, `protocol_settings`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /tls-service-profiles/{id}`

**Summary:** Delete a TLS service profile  
**Operation ID:** `DeleteTLSServiceProfilesByID`  
**Tags:** TLS Service Profiles  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /ocsp-responders`

**Summary:** List OCSP responders  
**Operation ID:** `ListOCSPResponders`  
**Tags:** OCSP Responders  
**Container scope:** folder | snippet | device  
**Query params:** name, limit, offset  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /ocsp-responders`

**Summary:** Create an OCSP responder  
**Operation ID:** `CreateOCSPResponders`  
**Tags:** OCSP Responders  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `ocsp-responders`  
**Required fields:** `id`, `name`, `host_name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /ocsp-responders/{id}`

**Summary:** Get an OCSP responder  
**Operation ID:** `GetOCSPRespondersByID`  
**Tags:** OCSP Responders  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /ocsp-responders/{id}`

**Summary:** Update an OCSP responder  
**Operation ID:** `UpdateOCSPRespondersByID`  
**Tags:** OCSP Responders  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `ocsp-responders`  
**Required fields:** `id`, `name`, `host_name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /ocsp-responders/{id}`

**Summary:** Delete an OCSP responder  
**Operation ID:** `DeleteOCSPRespondersByID`  
**Tags:** OCSP Responders  
**Response codes:** 200, 400, 401, 403, 404, 409, default
