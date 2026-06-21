# Advanced DNS Security Resolver Configuration

**Version:** 1.0.0  
**Source:** `openapi-specs/scm/config/adnsr/adnsr.yaml`  
**Base URL:** `https://api.strata.paloaltonetworks.com`  
**Endpoints:** 44  
**GitHub:** https://github.com/PaloAltoNetworks/pan.dev/blob/master/openapi-specs/scm/config/adnsr/adnsr.yaml

---

## Endpoints

### `GET /adns-resolver/v1/ca-certs`

**Summary:** List EDL CA certificates  
**Operation ID:** `ListCACerts`  
**Tags:** EDL CA Certificates  
**Response codes:** 200, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default

### `DELETE /adns-resolver/v1/ca-certs/{ca-cert-id}`

**Summary:** Delete an EDL CA certificate  
**Operation ID:** `DeleteCACertByID`  
**Tags:** EDL CA Certificates  
**Response codes:** 204, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default

### `GET /adns-resolver/v1/ca-certs/{ca-cert-id}`

**Summary:** Get an EDL CA certificate  
**Operation ID:** `GetCACertByID`  
**Tags:** EDL CA Certificates  
**Response codes:** 200, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default

### `GET /adns-resolver/v1/ca-certs/{ca-cert-id}/download`

**Summary:** Download an EDL CA certificate as PEM file  
**Operation ID:** `DownloadCACertAsFile`  
**Tags:** EDL CA Certificates  
**Response codes:** 200, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default

### `POST /adns-resolver/v1/ca-certs:upload`

**Summary:** Upload an EDL CA certificate from file  
**Operation ID:** `UploadCACertFromFile`  
**Tags:** EDL CA Certificates  
**Required fields:** `name`, `cert`  
**Response codes:** 201, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default

### `GET /adns-resolver/v1/connection-sources`

**Summary:** List Connection Sources  
**Operation ID:** `ListConnectionSources`  
**Tags:** Connection Source  
**Query params:** limit, offset, sort_by, sort_order, search  
**Response codes:** 200, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default

### `POST /adns-resolver/v1/connection-sources`

**Summary:** Create a Connection Source  
**Operation ID:** `CreateConnectionSource`  
**Tags:** Connection Source  
**Body schema:** `connection-source-input`  
**Required fields:** `name`, `profile_id`  
**Response codes:** 201, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default

### `GET /adns-resolver/v1/connection-sources/subnets`

**Summary:** List Subnets  
**Operation ID:** `ListSubnets`  
**Tags:** Connection Source  
**Query params:** limit, offset, sort_by, sort_order, search  
**Response codes:** 200, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default

### `GET /adns-resolver/v1/connection-sources/subnets/{subnet-id}`

**Summary:** Get a Subnet  
**Operation ID:** `GetSubnetByID`  
**Tags:** Connection Source  
**Response codes:** 200, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default

### `DELETE /adns-resolver/v1/connection-sources/{connection-source-id}`

**Summary:** Delete a Connection Source  
**Operation ID:** `DeleteConnectionSourceByID`  
**Tags:** Connection Source  
**Response codes:** 204, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default

### `GET /adns-resolver/v1/connection-sources/{connection-source-id}`

**Summary:** Get a Connection Source  
**Operation ID:** `GetConnectionSourceByID`  
**Tags:** Connection Source  
**Response codes:** 200, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default

### `PUT /adns-resolver/v1/connection-sources/{connection-source-id}`

**Summary:** Update a Connection Source  
**Operation ID:** `UpdateConnectionSourceByID`  
**Tags:** Connection Source  
**Body schema:** `connection-source-input`  
**Required fields:** `name`, `profile_id`  
**Response codes:** 200, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default

### `GET /adns-resolver/v1/connection-sources/{connection-source-id}/subnets`

**Summary:** List Connection Source Subnets  
**Operation ID:** `ListConnectionSourceSubnets`  
**Tags:** Connection Source  
**Query params:** limit, offset, sort_by, sort_order, search  
**Response codes:** 200, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default

### `POST /adns-resolver/v1/connection-sources/{connection-source-id}/subnets`

**Summary:** Create a Connection Source subnet  
**Operation ID:** `CreateConnectionSourceSubnet`  
**Tags:** Connection Source  
**Body schema:** `subnet-input`  
**Required fields:** `cidr`  
**Response codes:** 201, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default

### `DELETE /adns-resolver/v1/connection-sources/{connection-source-id}/subnets/{subnet-id}`

**Summary:** Delete a Connection Source Subnet  
**Operation ID:** `DeleteConnectionSourceSubnetByID`  
**Tags:** Connection Source  
**Response codes:** 204, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default

### `GET /adns-resolver/v1/connection-sources/{connection-source-id}/subnets/{subnet-id}`

**Summary:** Get a Connection Source Subnet  
**Operation ID:** `GetConnectionSourceSubnetByID`  
**Tags:** Connection Source  
**Response codes:** 200, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default

### `POST /adns-resolver/v1/connection-sources/{connection-source-id}/subnets/{subnet-id}:verify-update`

**Summary:** Verify a subnet for a connection source  
**Operation ID:** `VerifyAndUpdateConnectionSourceSubnetByID`  
**Tags:** Connection Source  
**Body schema:** `verify-and-update-subnet-input`  
**Required fields:** `cidr`, `verification_url`, `token`  
**Response codes:** 200, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default

### `GET /adns-resolver/v1/custom-fqdns`

**Summary:** List Custom FQDNs  
**Operation ID:** `ListCustomFqdns`  
**Tags:** Custom FQDN  
**Query params:** limit, offset, sort_by, sort_order, search  
**Response codes:** 200, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default

### `POST /adns-resolver/v1/custom-fqdns`

**Summary:** Create a Custom FQDN  
**Operation ID:** `CreateCustomFqdn`  
**Tags:** Custom FQDN  
**Required fields:** `name`, `fqdns`, `Fqdns`  
**Response codes:** 201, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default

### `DELETE /adns-resolver/v1/custom-fqdns/{custom-fqdn-id}`

**Summary:** Delete a Custom FQDN  
**Operation ID:** `DeleteCustomFqdnByID`  
**Tags:** Custom FQDN  
**Response codes:** 204, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default

### `GET /adns-resolver/v1/custom-fqdns/{custom-fqdn-id}`

**Summary:** Get a custom fqdn  
**Operation ID:** `GetCustomFqdnByID`  
**Tags:** Custom FQDN  
**Query params:** fqdn-limit, fqdn-offset  
**Response codes:** 200, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default

### `PUT /adns-resolver/v1/custom-fqdns/{custom-fqdn-id}`

**Summary:** Update a Custom FQDN  
**Operation ID:** `UpdateCustomFqdnByID`  
**Tags:** Custom FQDN  
**Required fields:** `name`, `fqdns`, `Fqdns`  
**Response codes:** 200, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default

### `GET /adns-resolver/v1/edls`

**Summary:** List EDL definitions  
**Operation ID:** `ListEDLDefinitions`  
**Tags:** EDL Definitions  
**Response codes:** 200, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default

### `POST /adns-resolver/v1/edls`

**Summary:** Create an EDL definition  
**Operation ID:** `CreateEDLDefinition`  
**Tags:** EDL Definitions  
**Body schema:** `edl-definition-input`  
**Response codes:** 201, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default

### `DELETE /adns-resolver/v1/edls/{edl-id}`

**Summary:** Delete an EDL definition  
**Operation ID:** `DeleteEDLDefinitionByID`  
**Tags:** EDL Definitions  
**Response codes:** 204, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default

### `GET /adns-resolver/v1/edls/{edl-id}`

**Summary:** Get an EDL definition  
**Operation ID:** `GetEDLDefinitionByID`  
**Tags:** EDL Definitions  
**Response codes:** 200, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default

### `PUT /adns-resolver/v1/edls/{edl-id}`

**Summary:** Update an EDL definition  
**Operation ID:** `UpdateEDLDefinitionByID`  
**Tags:** EDL Definitions  
**Body schema:** `edl-definition-input`  
**Response codes:** 200, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default

### `GET /adns-resolver/v1/internal-domains`

**Summary:** List internal domains  
**Operation ID:** `ListInternalDomains`  
**Tags:** Internal Domains  
**Query params:** limit, offset, sort_by, sort_order, search, type  
**Response codes:** 200, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default

### `POST /adns-resolver/v1/internal-domains`

**Summary:** Create a custom internal domain  
**Operation ID:** `CreateInternalDomain`  
**Tags:** Internal Domains  
**Body schema:** `internal-domain-input`  
**Required fields:** `domain`  
**Response codes:** 201, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default

### `DELETE /adns-resolver/v1/internal-domains/{internal-domain-id}`

**Summary:** Delete a custom internal domain  
**Operation ID:** `DeleteInternalDomainByID`  
**Tags:** Internal Domains  
**Response codes:** 204, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default

### `GET /adns-resolver/v1/internal-domains/{internal-domain-id}`

**Summary:** Get an internal domain  
**Operation ID:** `GetInternalDomainByID`  
**Tags:** Internal Domains  
**Response codes:** 200, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default

### `PUT /adns-resolver/v1/internal-domains/{internal-domain-id}`

**Summary:** Update a custom internal domain  
**Operation ID:** `UpdateInternalDomainByID`  
**Tags:** Internal Domains  
**Body schema:** `internal-domain-input`  
**Required fields:** `domain`  
**Response codes:** 200, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default

### `GET /adns-resolver/v1/misconfigured-domains`

**Summary:** List misconfigured domains  
**Operation ID:** `ListMisconfiguredDomains`  
**Tags:** Misconfigured Domains  
**Query params:** limit, offset, sort_by, sort_order, search  
**Response codes:** 200, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default

### `POST /adns-resolver/v1/misconfigured-domains`

**Summary:** Create a misconfigured domain  
**Operation ID:** `CreateMisconfiguredDomain`  
**Tags:** Misconfigured Domains  
**Body schema:** `misconfigured-domain-input`  
**Required fields:** `domain`  
**Response codes:** 201, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default

### `DELETE /adns-resolver/v1/misconfigured-domains/{misconfigured-domain-id}`

**Summary:** Delete a misconfigured domain  
**Operation ID:** `DeleteMisconfiguredDomainByID`  
**Tags:** Misconfigured Domains  
**Response codes:** 204, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default

### `GET /adns-resolver/v1/misconfigured-domains/{misconfigured-domain-id}`

**Summary:** Get a misconfigured domain  
**Operation ID:** `GetMisconfiguredDomainByID`  
**Tags:** Misconfigured Domains  
**Response codes:** 200, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default

### `PUT /adns-resolver/v1/misconfigured-domains/{misconfigured-domain-id}`

**Summary:** Update a misconfigured domain  
**Operation ID:** `UpdateMisconfiguredDomainByID`  
**Tags:** Misconfigured Domains  
**Body schema:** `misconfigured-domain-input`  
**Required fields:** `domain`  
**Response codes:** 200, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default

### `GET /adns-resolver/v1/profiles`

**Summary:** List profiles  
**Operation ID:** `ListProfiles`  
**Tags:** Profiles  
**Query params:** limit, offset, sort_by, sort_order, search  
**Response codes:** 200, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default

### `POST /adns-resolver/v1/profiles`

**Summary:** Create a profile  
**Operation ID:** `CreateProfile`  
**Tags:** Profiles  
**Body schema:** `profile-input`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default

### `GET /adns-resolver/v1/profiles/categories`

**Summary:** Get profile categories  
**Operation ID:** `ListCategories`  
**Tags:** Profiles  
**Response codes:** 200, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default

### `DELETE /adns-resolver/v1/profiles/{profile-id}`

**Summary:** Delete a profile  
**Operation ID:** `DeleteProfileByID`  
**Tags:** Profiles  
**Response codes:** 204, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default

### `GET /adns-resolver/v1/profiles/{profile-id}`

**Summary:** Get a profile  
**Operation ID:** `GetProfileByID`  
**Tags:** Profiles  
**Response codes:** 200, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default

### `PUT /adns-resolver/v1/profiles/{profile-id}`

**Summary:** Update a profile  
**Operation ID:** `UpdateProfileByID`  
**Tags:** Profiles  
**Body schema:** `profile-input`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default

### `GET /adns-resolver/v1/resolver-info`

**Summary:** Get resolver information  
**Operation ID:** `GetResolverInfo`  
**Tags:** Resolver Info  
**Response codes:** 200, 400, 401, 403, 404, 405, 409, 412, 422, 500, 503, default
