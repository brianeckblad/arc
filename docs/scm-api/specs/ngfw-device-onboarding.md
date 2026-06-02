# Device Onboarding

**Version:** 2.0.0  
**Source:** `openapi-specs/scm/config/ngfw/setup/device-onboarding/device-onboarding-updated.yaml`  
**Base URL:** `https://api.strata.paloaltonetworks.com/config/setup/device-onboarding/v1`  
**Endpoints:** 21  
**GitHub:** https://github.com/PaloAltoNetworks/pan.dev/blob/master/openapi-specs/scm/config/ngfw/setup/device-onboarding/device-onboarding-updated.yaml

---

## Endpoints

### `POST /sites`

**Summary:** Create sites  
**Operation ID:** `createSites`  
**Tags:** Sites  
**Response codes:** 201, 400, 409, 500

### `GET /sites`

**Summary:** List sites  
**Operation ID:** `listSites`  
**Tags:** Sites  
**Response codes:** 200, 500

### `GET /sites/{id}`

**Summary:** Get a site  
**Operation ID:** `getSiteByID`  
**Tags:** Sites  
**Response codes:** 200, 404, 500

### `PUT /sites/{id}`

**Summary:** Update a site  
**Operation ID:** `updateSiteByID`  
**Tags:** Sites  
**Response codes:** 200, 404, 409, 500

### `DELETE /sites/{id}`

**Summary:** Delete a site  
**Operation ID:** `deleteSiteByID`  
**Tags:** Sites  
**Response codes:** 200, 404, 409, 500

### `POST /properties`

**Summary:** Create a property  
**Operation ID:** `createProperty`  
**Tags:** Properties  
**Response codes:** 201, 400, 409, 500

### `GET /properties`

**Summary:** List properties  
**Operation ID:** `listProperties`  
**Tags:** Properties  
**Response codes:** 200, 500

### `GET /properties/{id}`

**Summary:** Get a property  
**Operation ID:** `getPropertyByID`  
**Tags:** Properties  
**Response codes:** 200, 404, 500

### `PUT /properties/{id}`

**Summary:** Update a property  
**Operation ID:** `updatePropertyByID`  
**Tags:** Properties  
**Response codes:** 200, 404, 409, 500

### `DELETE /properties/{id}`

**Summary:** Delete a property  
**Operation ID:** `deletePropertyByID`  
**Tags:** Properties  
**Response codes:** 200, 404, 409, 500

### `POST /onboarding-rules`

**Summary:** Create an onboarding rule  
**Operation ID:** `createOnboardingRule`  
**Tags:** Onboarding Rules  
**Response codes:** 201, 400, 409, 500

### `GET /onboarding-rules`

**Summary:** List onboarding rules  
**Operation ID:** `listOnboardingRules`  
**Tags:** Onboarding Rules  
**Response codes:** 200, 500

### `POST /onboarding-rules/{id}:move`

**Summary:** Move an onboarding rule  
**Operation ID:** `moveOnboardingRuleByID`  
**Tags:** Onboarding Rules  
**Response codes:** 200, 400, 404, 500

### `GET /onboarding-rules/{id}`

**Summary:** Get an onboarding rule  
**Operation ID:** `getOnboardingRuleByID`  
**Tags:** Onboarding Rules  
**Response codes:** 200, 404, 500

### `PUT /onboarding-rules/{id}`

**Summary:** Update an onboarding rule  
**Operation ID:** `updateOnboardingRuleByID`  
**Tags:** Onboarding Rules  
**Response codes:** 200, 400, 404, 409, 500

### `DELETE /onboarding-rules/{id}`

**Summary:** Delete an onboarding rule  
**Operation ID:** `deleteOnboardingRuleByID`  
**Tags:** Onboarding Rules  
**Response codes:** 200, 404, 409, 500

### `POST /site-groups`

**Summary:** Create a site group  
**Operation ID:** `createSiteGroup`  
**Tags:** Site Groups  
**Response codes:** 201, 400, 409, 500

### `GET /site-groups`

**Summary:** List site groups  
**Operation ID:** `listSiteGroups`  
**Tags:** Site Groups  
**Response codes:** 200, 500

### `GET /site-groups/{id}`

**Summary:** Get a site group  
**Operation ID:** `getSiteGroupByID`  
**Tags:** Site Groups  
**Response codes:** 200, 404, 500

### `PUT /site-groups/{id}`

**Summary:** Update a site group  
**Operation ID:** `updateSiteGroupByID`  
**Tags:** Site Groups  
**Response codes:** 200, 404, 409, 500

### `DELETE /site-groups/{id}`

**Summary:** Delete a site group  
**Operation ID:** `deleteSiteGroupByID`  
**Tags:** Site Groups  
**Response codes:** 200, 404, 409, 500
