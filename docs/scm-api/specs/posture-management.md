# Posture Management and Assessment API: BPA, Custom Checks, and Compliance

**Version:** 1.0  
**Source:** `openapi-specs/scm/config/posture-management/Posture APIs-updated.yaml`  
**Base URL:** `https://api.strata.paloaltonetworks.com`  
**Endpoints:** 10  
**GitHub:** https://github.com/PaloAltoNetworks/pan.dev/blob/master/openapi-specs/scm/config/posture-management/Posture APIs-updated.yaml

---

## Endpoints

### `POST /posture/checks/v1/reports/config-file-upload`

**Summary:** Initiate a Configuration Upload  
**Operation ID:** `InitiateConfigUpload`  
**Tags:** Config File Upload  
**Required fields:** `delete_after_processing`  
**Response codes:** 201, 400, 429, 500

### `GET /posture/checks/v1/reports/{id}/bpa-result`

**Summary:** Get BPA Processing Status  
**Operation ID:** `GetBpaResultByID`  
**Tags:** Config File Upload  
**Response codes:** 200, 404

### `GET /posture/checks/v1`

**Summary:** List Posture Checks  
**Operation ID:** `ListPostureChecks`  
**Tags:** Custom Posture Checks  
**Query params:** type, object_type, severity, management_type, limit, offset  
**Response codes:** 200, 400, 500

### `POST /posture/checks/v1`

**Summary:** Create Posture Check  
**Operation ID:** `CreatePostureChecks`  
**Tags:** Custom Posture Checks  
**Body schema:** `PostureCheckCreateRequest`  
**Required fields:** `name`, `object_type`, `data`, `severity`  
**Response codes:** 201, 400, 403, 500

### `GET /posture/checks/v1/{id}`

**Summary:** Get Posture Check  
**Operation ID:** `GetPostureChecksByID`  
**Tags:** Custom Posture Checks  
**Response codes:** 200, 404, 500

### `PUT /posture/checks/v1/{id}`

**Summary:** Update Posture Check  
**Operation ID:** `UpdatePostureChecksByID`  
**Tags:** Custom Posture Checks  
**Body schema:** `PostureCheckUpdateRequest`  
**Required fields:** `name`, `object_type`, `data`, `severity`  
**Response codes:** 200, 400, 403, 404, 500

### `DELETE /posture/checks/v1/{id}`

**Summary:** Delete Posture Check  
**Operation ID:** `DeletePostureChecksByID`  
**Tags:** Custom Posture Checks  
**Response codes:** 204, 403, 404, 500

### `POST /posture/checks/v1/{id}:clone`

**Summary:** Clone Posture Check  
**Operation ID:** `ClonePostureChecksByID`  
**Tags:** Custom Posture Checks  
**Body schema:** `PostureCheckCloneRequest`  
**Response codes:** 201, 400, 403, 404, 500

### `POST /posture/checks/v1/batch-upsert`

**Summary:** Batch Upsert Posture Checks  
**Operation ID:** `BatchUpsertPostureChecks`  
**Tags:** Custom Posture Checks  
**Body schema:** `PostureCheckBatchUpsertRequest`  
**Required fields:** `checks`  
**Response codes:** 200, 400, 403, 500

### `POST /posture/checks/v1/batch-delete`

**Summary:** Batch Delete Posture Checks  
**Operation ID:** `BatchDeletePostureChecks`  
**Tags:** Custom Posture Checks  
**Body schema:** `PostureCheckBatchDeleteRequest`  
**Required fields:** `ids`  
**Response codes:** 200, 400, 403, 500
