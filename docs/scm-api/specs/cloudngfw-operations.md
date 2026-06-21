# Config Operations

**Version:** 2.0.0  
**Source:** `openapi-specs/scm/config/cloudngfw/operations/config-operations-march.yaml`  
**Base URL:** `https://api.strata.paloaltonetworks.com/config/operations/v1`  
**Endpoints:** 8  
**GitHub:** https://github.com/PaloAltoNetworks/pan.dev/blob/master/openapi-specs/scm/config/cloudngfw/operations/config-operations-march.yaml

---

## Endpoints

### `GET /jobs`

**Summary:** List jobs  
**Operation ID:** `ListJobs`  
**Tags:** Jobs  
**Response codes:** 200, 400, 401, 403, 404, default

### `GET /jobs/{id}`

**Summary:** Get a job  
**Operation ID:** `GetJobsByID`  
**Tags:** Jobs  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /config-versions:load`

**Summary:** Load config version  
**Operation ID:** `LoadConfigVersions`  
**Tags:** Config Versions  
**Body schema:** `load-config`  
**Response codes:** 201, 400, 401, 403, 409, default

### `POST /config-versions/candidate:push`

**Summary:** Push the candidate configuration  
**Operation ID:** `PushCandidateConfigVersions`  
**Tags:** Config Versions  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /config-versions`

**Summary:** List configuration versions  
**Operation ID:** `ListConfigVersions`  
**Tags:** Config Versions  
**Query params:** limit, offset  
**Response codes:** 200, 400, 401, 403, 404, default

### `DELETE /config-versions/candidate`

**Summary:** Delete a candidate configuration  
**Operation ID:** `DeleteCandidateConfigVersions`  
**Tags:** Config Versions  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /config-versions/{version}`

**Summary:** Get config by version  
**Operation ID:** `GetConfigVersionsByID`  
**Tags:** Config Versions  
**Response codes:** 200, 400, 401, 403, 404, default

### `GET /config-versions/running`

**Summary:** Get running configuration versions  
**Operation ID:** `GetRunningConfigVersions`  
**Tags:** Config Versions  
**Response codes:** 200, 400, 401, 403, 404, default
