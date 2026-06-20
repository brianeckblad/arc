# Service Accounts

**Version:** 1.0  
**Source:** `openapi-specs/scm/iam/ServiceAccounts.yaml`  
**Base URL:** `https://api.sase.paloaltonetworks.com`  
**Endpoints:** 6  
**GitHub:** https://github.com/PaloAltoNetworks/pan.dev/blob/master/openapi-specs/scm/iam/ServiceAccounts.yaml

---

## Endpoints

### `GET /iam/v1/service_accounts`

**Summary:** List all service accounts  
**Operation ID:** `get-iam-v1-service_accounts`  
**Tags:** ServiceAccounts  
**Response codes:** 200

### `POST /iam/v1/service_accounts`

**Summary:** Create a service account  
**Operation ID:** `post-iam-v1-service_accounts`  
**Tags:** ServiceAccounts  
**Body schema:** `service_account_create`  
**Response codes:** 201

### `DELETE /iam/v1/service_accounts/{id}`

**Summary:** Delete a service account  
**Operation ID:** `delete-iam-v1-service_accounts-id`  
**Tags:** ServiceAccounts  
**Response codes:** 204

### `GET /iam/v1/service_accounts/{id}`

**Summary:** Get a service account  
**Operation ID:** `get-iam-v1-service_accounts-id`  
**Tags:** ServiceAccounts  
**Response codes:** 200

### `PUT /iam/v1/service_accounts/{id}`

**Summary:** Update a service account  
**Operation ID:** `put-iam-v1-service_accounts-id`  
**Tags:** ServiceAccounts  
**Body schema:** `service_account_update`  
**Response codes:** 202

### `POST /iam/v1/service_accounts/{id}/operations/reset`

**Summary:** Reset a service account  
**Operation ID:** `post-iam-v1-service_accounts-id-operations-reset`  
**Tags:** ServiceAccounts  
**Response codes:** 201
