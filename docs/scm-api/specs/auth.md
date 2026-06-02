# Authentication Service API

**Version:** 1.0  
**Source:** `openapi-specs/scm/auth/AuthService.yaml`  
**Base URL:** `https://auth.apps.paloaltonetworks.com`  
**Endpoints:** 3  
**GitHub:** https://github.com/PaloAltoNetworks/pan.dev/blob/master/openapi-specs/scm/auth/AuthService.yaml

---

## Endpoints

### `POST /auth/v1/oauth2/access_token`

**Summary:** Create an access token  
**Operation ID:** `post-auth-v1-oauth2-access_token`  
**Tags:** AuthService  
**Response codes:** 200, 400, 401

### `POST /auth/v1/oauth2/userinfo`

**Summary:** Retrieve oAuth oAuth 2.0 claims  
**Operation ID:** `post-auth-v1-oauth2-userinfo`  
**Tags:** AuthService  
**Response codes:** 200, 400, 401

### `GET /auth/v1/oauth2/userinfo`

**Summary:** Retrieve oAuth 2.0 claims  
**Operation ID:** `get-auth-v1-oauth2-userinfo`  
**Tags:** AuthService  
**Response codes:** 200, 400, 401
