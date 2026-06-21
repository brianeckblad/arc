# Custom Roles

**Version:** 1.0  
**Source:** `openapi-specs/scm/iam/CustomRoles.yaml`  
**Base URL:** `https://api.sase.paloaltonetworks.com`  
**Endpoints:** 5  
**GitHub:** https://github.com/PaloAltoNetworks/pan.dev/blob/master/openapi-specs/scm/iam/CustomRoles.yaml

---

## Endpoints

### `GET /iam/v1/custom_roles`

**Summary:** List custom roles  
**Operation ID:** `get-iam-v1-custom_roles`  
**Tags:** CustomRoles  
**Response codes:** 200

### `POST /iam/v1/custom_roles`

**Summary:** Create a custom role  
**Operation ID:** `post-iam-v1-custom_roles`  
**Tags:** CustomRoles  
**Body schema:** `custom_role_create`  
**Required fields:** `name`, `description`  
**Response codes:** 201

### `DELETE /iam/v1/custom_roles/{name}`

**Summary:** Delete a custom role  
**Operation ID:** `delete-iam-v1-custom_roles-name`  
**Tags:** CustomRoles  
**Response codes:** 204

### `GET /iam/v1/custom_roles/{name}`

**Summary:** Get a Custom Role  
**Operation ID:** `get-iam-v1-custom_roles-name`  
**Tags:** CustomRoles  
**Response codes:** 200

### `PUT /iam/v1/custom_roles/{name}`

**Summary:** Update a Custom Role  
**Operation ID:** `put-iam-v1-custom_roles-name`  
**Tags:** CustomRoles  
**Body schema:** `custom_role_update`  
**Required fields:** `description`  
**Response codes:** 202
