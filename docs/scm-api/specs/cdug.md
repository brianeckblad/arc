# CIE - Cloud Dynamic User Group CRUD Operations APIs Mounted on Strata Cloud Manager

**Version:** 1.0.0  
**Source:** `openapi-specs/scm/config/cdug/cdug.yaml`  
**Base URL:** `n/a`  
**Endpoints:** 6  
**GitHub:** https://github.com/PaloAltoNetworks/pan.dev/blob/master/openapi-specs/scm/config/cdug/cdug.yaml

---

## Endpoints

### `GET /directory-sync/v1/cloud-dug-definition/category`

**Summary:** Retrieve Dynamic Group Categories  
**Operation ID:** `GetDirectory-syncV1Cloud-dug-definitionCategory`  
**Tags:** Cloud Dynamic User Groups  
**Query params:** domain  
**Response codes:** 200, 400, 401, 404, 500

### `GET /directory-sync/v1/user-attr-values`

**Summary:** Retrieve User Attribute Values  
**Operation ID:** `GetDirectory-syncV1User-attr-values`  
**Tags:** Cloud Dynamic User Groups  
**Query params:** domain, attrName, riskSourceId  
**Response codes:** 200, 400, 401, 500

### `POST /directory-sync/v1/cloud-dug-definition`

**Summary:** Create Cloud Dynamic User Groups  
**Operation ID:** `PostDirectory-syncV1Cloud-dug-definition`  
**Tags:** Cloud Dynamic User Groups  
**Body schema:** `GroupCreateRequest`  
**Required fields:** `domain`, `value`, `useNormalizedAttrs`  
**Response codes:** 200, 400, 401, 500

### `GET /directory-sync/v1/cloud-dug-definition/group`

**Summary:** Retrieve Cloud Dynamic User Groups  
**Operation ID:** `GetDirectory-syncV1Cloud-dug-definitionGroup`  
**Tags:** Cloud Dynamic User Groups  
**Query params:** domain, aggregationId, objectGUID, defID, useNormalizedAttrs, pageNum, pageSz  
**Response codes:** 200, 400, 401, 404, 500

### `PUT /directory-sync/v1/cloud-dug-definition/group`

**Summary:** Update Cloud Dynamic User Groups  
**Operation ID:** `PutDirectory-syncV1Cloud-dug-definitionGroup`  
**Tags:** Cloud Dynamic User Groups  
**Body schema:** `GroupUpdateRequest`  
**Required fields:** `domain`, `value`, `useNormalizedAttrs`  
**Response codes:** 200, 400, 401, 500

### `DELETE /directory-sync/v1/cloud-dug-definition/group`

**Summary:** Delete Cloud Dynamic User Groups  
**Operation ID:** `DeleteDirectory-syncV1Cloud-dug-definitionGroup`  
**Tags:** Cloud Dynamic User Groups  
**Query params:** domain, objectGUID, defID  
**Response codes:** 200, 400, 401, 500
