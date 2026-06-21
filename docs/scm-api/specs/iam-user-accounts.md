# User Accounts

**Version:** 1.0  
**Source:** `openapi-specs/scm/iam/UserAccounts.yaml`  
**Base URL:** `https://api.sase.paloaltonetworks.com`  
**Endpoints:** 2  
**GitHub:** https://github.com/PaloAltoNetworks/pan.dev/blob/master/openapi-specs/scm/iam/UserAccounts.yaml

---

## Endpoints

### `GET /iam/v1/sso_users`

**Summary:** Verify a user account  
**Operation ID:** `get-iam-v1-sso_users`  
**Tags:** UserAccounts  
**Query params:** email  
**Response codes:** 200

### `POST /iam/v1/sso_users`

**Summary:** Create an SSO account  
**Operation ID:** `post-iam-v1-sso_users`  
**Tags:** UserAccounts  
**Body schema:** `user_register`  
**Required fields:** `email`, `firstname`, `lastname`  
**Response codes:** 200
