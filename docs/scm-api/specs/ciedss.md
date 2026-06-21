# CIE Directory Sync Service APIs Mounted on Strata Cloud Manger

**Version:** 1.0.1  
**Source:** `openapi-specs/scm/config/ciedss/CIE-DSS-R2.yaml`  
**Base URL:** `https://api.sase.paloaltonetworks.com`  
**Endpoints:** 4  
**GitHub:** https://github.com/PaloAltoNetworks/pan.dev/blob/master/openapi-specs/scm/config/ciedss/CIE-DSS-R2.yaml

---

## Endpoints

### `GET /cie/directory-sync/v1/domains`

**Summary:** Fetch domains from the CIE Directory Sync Service  
**Tags:** Directory Sync Service  
**Response codes:** 200, 500

### `POST /cie/directory-sync/v1/cache-users`

**Summary:** Fetch user information from the CIE Directory Sync Service across multiple scenarios.  
**Tags:** Directory Sync Service  
**Type variants (oneOf/anyOf):** `attrs+useNormalizedAttrs` | `name` | `filter+attrs`  
**Response codes:** 200, 400, 500

### `POST /cie/directory-sync/v1/cache-groups`

**Summary:** Fetch group information from the CIE Directory Sync Service across multiple scenarios.  
**Tags:** Directory Sync Service  
**Type variants (oneOf/anyOf):** `attrs+useNormalizedAttrs` | `attrs` | `filter`  
**Response codes:** 200, 400, 500

### `POST /cie/directory-sync/v1/connection/update-secret`

**Summary:** Update directory connection client secret  
**Tags:** Directory Sync Service  
**Required fields:** `directoryId`, `provider`, `client_secret`  
**Response codes:** 200, 400, 404, 421, 500
