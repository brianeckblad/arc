# Access Policies

**Version:** 1.0  
**Source:** `openapi-specs/scm/iam/AccessPolicies.yaml`  
**Base URL:** `https://api.sase.paloaltonetworks.com`  
**Endpoints:** 4  
**GitHub:** https://github.com/PaloAltoNetworks/pan.dev/blob/master/openapi-specs/scm/iam/AccessPolicies.yaml

---

## Endpoints

### `GET /iam/v1/access_policies`

**Summary:** List all access policies  
**Operation ID:** `get-iam-v1-access_policies`  
**Tags:** AccessPolicies  
**Query params:** role, principal  
**Response codes:** 200

### `POST /iam/v1/access_policies`

**Summary:** Assign an access policy  
**Operation ID:** `post-iam-v1-access_policies`  
**Tags:** AccessPolicies  
**Body schema:** `access_policy_create_required`  
**Required fields:** `role`, `principal`, `resource`  
**Response codes:** 201

### `DELETE /iam/v1/access_policies/{id}`

**Summary:** Delete an access policy  
**Operation ID:** `delete-iam-v1-access_policies-id`  
**Tags:** AccessPolicies  
**Response codes:** 200

### `GET /iam/v1/access_policies/{id}`

**Summary:** Get an access policy  
**Operation ID:** `get-iam-v1-access_policies-id`  
**Tags:** AccessPolicies  
**Response codes:** 200
