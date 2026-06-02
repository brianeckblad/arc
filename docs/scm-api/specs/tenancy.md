# Tenant Service Group

**Version:** 1.0  
**Source:** `openapi-specs/scm/tenancy/TenantServiceGroup.yaml`  
**Base URL:** `https://api.sase.paloaltonetworks.com`  
**Endpoints:** 7  
**GitHub:** https://github.com/PaloAltoNetworks/pan.dev/blob/master/openapi-specs/scm/tenancy/TenantServiceGroup.yaml

---

## Endpoints

### `GET /tenancy/v1/tenant_service_groups`

**Summary:** List all tenant service groups  
**Operation ID:** `get-tenancy-v1-tenant_service_groups`  
**Tags:** TenantServiceGroup  
**Response codes:** 200, 401, 403, 404, 500

### `POST /tenancy/v1/tenant_service_groups`

**Summary:** Create a tenant service group  
**Operation ID:** `post-tenancy-v1-tenant_service_groups`  
**Tags:** TenantServiceGroup  
**Response codes:** 200, 400, 401, 403, 404, 500

### `DELETE /tenancy/v1/tenant_service_groups/{tsg_id}`

**Summary:** Delete a tenant service group  
**Operation ID:** `delete-tenancy-v1-tenant_service_groups-tsg_id`  
**Tags:** TenantServiceGroup  
**Response codes:** 200, 401, 403, 404, 500

### `GET /tenancy/v1/tenant_service_groups/{tsg_id}`

**Summary:** Get a tenant service group  
**Operation ID:** `get-tenancy-v1-tenant_service_groups-tsg_id`  
**Tags:** TenantServiceGroup  
**Response codes:** 200, 401, 403, 404, 500

### `PUT /tenancy/v1/tenant_service_groups/{tsg_id}`

**Summary:** Update a tenant service group  
**Operation ID:** `put-tenancy-v1-tenant_service_groups-tsg_id`  
**Tags:** TenantServiceGroup  
**Response codes:** 200, 401, 403, 404, 500

### `POST /tenancy/v1/tenant_service_groups/{tsg_id}/operations/list_ancestors`

**Summary:** List tenant service group ancestors  
**Operation ID:** `post-tenancy-v1-tenant_service_groups-tsg_id-operations-list_ancestors`  
**Tags:** TenantServiceGroup  
**Response codes:** 200, 401, 403, 404, 500

### `POST /tenancy/v1/tenant_service_groups/{tsg_id}/operations/list_children`

**Summary:** List tenant service group children  
**Operation ID:** `post-tenancy-v1-tenant_service_groups-tsg_id-operations-list_children`  
**Tags:** TenantServiceGroup  
**Response codes:** 200, 401, 403, 404, 500
