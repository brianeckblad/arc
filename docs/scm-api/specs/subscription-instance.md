# Instances

**Version:** 1.0  
**Source:** `openapi-specs/scm/subscription/Instance.yaml`  
**Base URL:** `https://api.sase.paloaltonetworks.com`  
**Endpoints:** 2  
**GitHub:** https://github.com/PaloAltoNetworks/pan.dev/blob/master/openapi-specs/scm/subscription/Instance.yaml

---

## Endpoints

### `GET /subscription/v1/instances`

**Summary:** List instances  
**Operation ID:** `get-subscription-v1-instances`  
**Tags:** Instance  
**Query params:** with_children  
**Response codes:** 200

### `POST /subscription/v1/instances`

**Summary:** Create an instance  
**Operation ID:** `post-subscription-v1-instances`  
**Tags:** Instance  
**Type variants (oneOf/anyOf):** `Root Type for create free app instance Payload` | `Root Type for onboard instance Payload`  
**Response codes:** 200, 400
