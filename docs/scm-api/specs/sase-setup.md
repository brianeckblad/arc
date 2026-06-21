# Configuration Setup

**Version:** 2.0.0  
**Source:** `openapi-specs/scm/config/sase/setup/config-setup-feb-v1.yaml`  
**Base URL:** `https://api.strata.paloaltonetworks.com/config/setup/v1`  
**Endpoints:** 47  
**GitHub:** https://github.com/PaloAltoNetworks/pan.dev/blob/master/openapi-specs/scm/config/sase/setup/config-setup-feb-v1.yaml

---

## Endpoints

### `GET /labels`

**Summary:** List labels  
**Operation ID:** `ListLabels`  
**Tags:** Labels  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /labels`

**Summary:** Create a label  
**Operation ID:** `CreateLabel`  
**Tags:** Labels  
**Body schema:** `labels`  
**Required fields:** `name`, `id`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /labels/{id}`

**Summary:** Get a label  
**Operation ID:** `GetLabelByID`  
**Tags:** Labels  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /labels/{id}`

**Summary:** Update a label  
**Operation ID:** `UpdateLabelByID`  
**Tags:** Labels  
**Body schema:** `labels`  
**Required fields:** `name`, `id`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /labels/{id}`

**Summary:** Delete a label  
**Operation ID:** `DeleteLabelByID`  
**Tags:** Labels  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /variables`

**Summary:** List variables  
**Operation ID:** `ListVariables`  
**Tags:** Variables  
**Container scope:** folder | snippet | device  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /variables`

**Summary:** Create a variable  
**Operation ID:** `CreateVariable`  
**Tags:** Variables  
**Container scope:** folder | snippet | device  
**Body schema:** `variables`  
**Required fields:** `name`, `id`, `type`, `value`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /variables/{id}`

**Summary:** Get a variables  
**Operation ID:** `GetVariableByID`  
**Tags:** Variables  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /variables/{id}`

**Summary:** Update a variable  
**Operation ID:** `UpdateVariableByID`  
**Tags:** Variables  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `variables`  
**Required fields:** `name`, `id`, `type`, `value`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /variables/{id}`

**Summary:** Delete a variable  
**Operation ID:** `DeleteVariableByID`  
**Tags:** Variables  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /snippets`

**Summary:** List snippets  
**Operation ID:** `ListSnippets`  
**Tags:** Snippets  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /snippets`

**Summary:** Create a snippet  
**Operation ID:** `CreateSnippet`  
**Tags:** Snippets  
**Body schema:** `snippets`  
**Required fields:** `name`, `id`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /snippets/{id}`

**Summary:** Get a snippet  
**Operation ID:** `GetSnippetByID`  
**Tags:** Snippets  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /snippets/{id}`

**Summary:** Update a snippet  
**Operation ID:** `UpdateSnippetByID`  
**Tags:** Snippets  
**Body schema:** `snippets`  
**Required fields:** `name`, `id`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /snippets/{id}`

**Summary:** Delete a snippet  
**Operation ID:** `DeleteSnippetByID`  
**Tags:** Snippets  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /folders`

**Summary:** List folders  
**Operation ID:** `ListFolders`  
**Tags:** Folders  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /folders`

**Summary:** Create a folder  
**Operation ID:** `CreateFolder`  
**Tags:** Folders  
**Body schema:** `folders`  
**Required fields:** `name`, `id`, `parent`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /folders/{id}`

**Summary:** Get a folder  
**Operation ID:** `GetFolderByID`  
**Tags:** Folders  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /folders/{id}`

**Summary:** Update a folder  
**Operation ID:** `UpdateFolderByID`  
**Tags:** Folders  
**Body schema:** `folders`  
**Required fields:** `name`, `id`, `parent`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /folders/{id}`

**Summary:** Delete a folder  
**Operation ID:** `DeleteFolderByID`  
**Tags:** Folders  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /devices`

**Summary:** List devices  
**Operation ID:** `ListDevices`  
**Tags:** Devices  
**Query params:** pagination, limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `GET /devices/{id}`

**Summary:** Get a device  
**Operation ID:** `GetDeviceByID`  
**Tags:** Devices  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /devices/{id}`

**Summary:** Update a device  
**Operation ID:** `UpdateDeviceByID`  
**Tags:** Devices  
**Body schema:** `devices-put`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /snippet-categories`

**Summary:** List snippets categories  
**Operation ID:** `ListSnippetCategories`  
**Tags:** Snippet Categories  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `GET /snippet-categories/{id}`

**Summary:** Get a snippet category  
**Operation ID:** `GetSnippetCategoryByID`  
**Tags:** Snippet Categories  
**Response codes:** 200, 400, 401, 403, 404, default

### `DELETE /snippet-categories/{id}`

**Summary:** Delete a snippet category  
**Operation ID:** `DeleteSnippetCategoryByID`  
**Tags:** Snippet Categories  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /trusted-tenant-overview`

**Summary:** Trusted Tenants Overview  
**Operation ID:** `GetTrustedTenantsOverview`  
**Tags:** Trusted Tenants Overview  
**Response codes:** 200, 400, 401, 403, 404, default

### `GET /trusted-tenants`

**Summary:** Trusted Tenants With Snippets  
**Operation ID:** `ListTrustedTenantsWithSnippets`  
**Tags:** Trust Information  
**Query params:** type  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /trusts`

**Summary:** Create a trust  
**Operation ID:** `CreateTrust`  
**Tags:** Trusts  
**Body schema:** `trusts`  
**Response codes:** 201, 400, 401, 403, 409, default

### `DELETE /trusts`

**Summary:** Delete a Trust  
**Operation ID:** `DeleteTrust`  
**Tags:** Trusts  
**Query params:** trustids, type  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `POST /trust-validations`

**Summary:** Validates Trust  
**Operation ID:** `ValidateTrust`  
**Tags:** Trust Validations  
**Body schema:** `trusts_validation_payload`  
**Required fields:** `tsg`, `donor_tenant_name`, `recipient_tenant_name`, `trust_id`, `psk`  
**Response codes:** 200, 400, 401, 403, 409, default

### `GET /subscribed-tenants/{id}`

**Summary:** Get Subscribed Tenants  
**Operation ID:** `ListSubscribedTenantsByID`  
**Tags:** Subscribed Tenants  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /subscribed-tenants`

**Summary:** Create Subscribed Tenant  
**Operation ID:** `CreateSubscribedTenant`  
**Tags:** Subscribed Tenants  
**Body schema:** `add_subscriber_request_payload`  
**Response codes:** 200, 400, 401, 403, 409, default

### `PUT /subscribed-tenants`

**Summary:** Update a subscribed tenant  
**Operation ID:** `UpdateSubscribedTenantBySnippetID`  
**Tags:** Subscribed Tenants  
**Body schema:** `subscriber_property_payload`  
**Required fields:** `tsg_id`, `snippet_id`, `snippet_name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /subscribed-tenants`

**Summary:** Delete a subscribed tenant  
**Operation ID:** `DeleteSubscribedTenantBySnippedID`  
**Tags:** Subscribed Tenants  
**Query params:** snippet-id, tsgs  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `POST /snippet-snapshots`

**Summary:** Save Snippet Snapshots  
**Operation ID:** `SaveSnippetSnapshot`  
**Tags:** Snippet Snapshots  
**Body schema:** `save_snippet_snapshot_payload`  
**Required fields:** `id`, `description`  
**Response codes:** 200, 400, 401, 403, 409, default

### `POST /snippet-snapshots:publish`

**Summary:** Publish Snippet Snapshots  
**Operation ID:** `PublishSnippetSnapshot`  
**Tags:** Snippet Snapshots  
**Body schema:** `snippet_snapshot_publish_request`  
**Response codes:** 200, 400, 401, 403, 409, default

### `POST /snippet-snapshots:compare`

**Summary:** Compare Snippet Snapshots  
**Operation ID:** `CompareSnippetSnapshot`  
**Tags:** Snippet Snapshots  
**Body schema:** `compare_snippet_snapshot_config_payload`  
**Required fields:** `id`, `version`, `comparing_version`  
**Response codes:** 200, 400, 401, 403, 409, default

### `POST /snippet-snapshots:diff`

**Summary:** Diff Snippet Snapshots  
**Operation ID:** `DiffSnippetSnapshot`  
**Tags:** Snippet Snapshots  
**Body schema:** `compare_tlo_payload`  
**Required fields:** `snippet_id`, `object_id`, `version`, `comparing_version    -`  
**Response codes:** 200, 400, 401, 403, 409, default

### `POST /snippet-snapshots:load`

**Summary:** Load Snippet Snapshots  
**Operation ID:** `LoadSnippetSnapshot`  
**Tags:** Snippet Snapshots  
**Body schema:** `snippet_snapshot_load_snippet_payload`  
**Required fields:** `id`, `version`  
**Response codes:** 200, 400, 401, 403, 409, default

### `POST /snippet-snapshots:updates`

**Summary:** Update Snippet Snapshots  
**Operation ID:** `UpdateSnippetSnapshot`  
**Tags:** Snippet Snapshots  
**Body schema:** `snippet_snapshot_subscriber_compare_payload`  
**Required fields:** `id`, `tenant_id`  
**Response codes:** 200, 400, 401, 403, 409, default

### `POST /snippet-snapshots:convert`

**Summary:** Convert Snippet Snapshots  
**Operation ID:** `ConvertSnippetSnapshot`  
**Tags:** Snippet Snapshots  
**Body schema:** `common_snippet_snapshot_payload`  
**Response codes:** 200, 400, 401, 403, 409, default

### `GET /shared-snippets`

**Summary:** Get Shared Snippets  
**Operation ID:** `ListSharedSnippets`  
**Tags:** Shared Snippets  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /shared-snippets`

**Summary:** Update Shared Snippets  
**Operation ID:** `ConvertSharedSnippets`  
**Tags:** Shared Snippets  
**Body schema:** `snippet_share_upload_payload`  
**Required fields:** `id`  
**Response codes:** 200, 400, 401, 403, 409, default

### `POST /shared-snippets:load`

**Summary:** Load Shared Snippets  
**Operation ID:** `LoadSharedSnippets`  
**Tags:** Shared Snippets  
**Body schema:** `snippet_share_load_payload`  
**Required fields:** `id`  
**Response codes:** 200, 400, 401, 403, 409, default

### `GET /snippet-audit-logs/{id}`

**Summary:** Get a snippet audit logs  
**Operation ID:** `GetSnippetAuditLogsByID`  
**Tags:** Snippet Audit Logs  
**Query params:** type  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /snippet-audit-logs`

**Summary:** Create snippet audit logs configuration  
**Operation ID:** `CreateSnippetAuditLogs`  
**Tags:** Snippet Audit Logs  
**Body schema:** `snippet_audit_payload`  
**Response codes:** 200, 400, 401, 403, 409, default
