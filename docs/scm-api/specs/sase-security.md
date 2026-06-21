# Security Services

**Version:** 2.0.0  
**Source:** `openapi-specs/scm/config/sase/security/security-services-R2-2026.yaml`  
**Base URL:** `https://api.strata.paloaltonetworks.com/config/security/v1`  
**Endpoints:** 113  
**GitHub:** https://github.com/PaloAltoNetworks/pan.dev/blob/master/openapi-specs/scm/config/sase/security/security-services-R2-2026.yaml

---

## Endpoints

### `GET /anti-spyware-profiles`

**Summary:** List anti-spyware profiles  
**Operation ID:** `ListAntiSpywareProfiles`  
**Tags:** Anti-Spyware Profiles  
**Container scope:** folder | snippet | device  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /anti-spyware-profiles`

**Summary:** Create an anti-spyware profile  
**Operation ID:** `CreateAntiSpywareProfiles`  
**Tags:** Anti-Spyware Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `anti-spyware-profiles`  
**Required fields:** `id`, `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /anti-spyware-profiles/{id}`

**Summary:** Get an anti-spyware profile  
**Operation ID:** `GetAntiSpywareProfilesByID`  
**Tags:** Anti-Spyware Profiles  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /anti-spyware-profiles/{id}`

**Summary:** Update an anti-spyware profile  
**Operation ID:** `UpdateAntiSpywareProfilesByID`  
**Tags:** Anti-Spyware Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `anti-spyware-profiles`  
**Required fields:** `id`, `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /anti-spyware-profiles/{id}`

**Summary:** Delete an anti-spyware profile  
**Operation ID:** `DeleteAntiSpywareProfilesByID`  
**Tags:** Anti-Spyware Profiles  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /anti-spyware-signatures`

**Summary:** List anti-spyware signatures  
**Operation ID:** `ListAntiSpywareSignatures`  
**Tags:** Anti-Spyware Signatures  
**Container scope:** folder | snippet | device  
**Query params:** offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /anti-spyware-signatures`

**Summary:** Create an anti-spyware signature  
**Operation ID:** `CreateAntiSpywareSignatures`  
**Tags:** Anti-Spyware Signatures  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `anti-spyware-signatures`  
**Required fields:** `threat_id`, `threatname`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /anti-spyware-signatures/{id}`

**Summary:** Get an anti-spyware signature  
**Operation ID:** `GetAntiSpywareSignaturesByID`  
**Tags:** Anti-Spyware Signatures  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /anti-spyware-signatures/{id}`

**Summary:** Update an anti-spyware signature  
**Operation ID:** `UpdateAntiSpywareSignaturesByID`  
**Tags:** Anti-Spyware Signatures  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `anti-spyware-signatures`  
**Required fields:** `threat_id`, `threatname`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /anti-spyware-signatures/{id}`

**Summary:** Delete an anti-spyware signature  
**Operation ID:** `DeleteAntiSpywareSignaturesByID`  
**Tags:** Anti-Spyware Signatures  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /app-override-rules`

**Summary:** List application override rules  
**Operation ID:** `ListApplicationOverrideRules`  
**Tags:** Application Override Rules  
**Container scope:** folder | snippet | device  
**Query params:** name, position, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /app-override-rules`

**Summary:** Create an application override rule  
**Operation ID:** `CreateApplicationOverrideRules`  
**Tags:** Application Override Rules  
**Container scope:** folder | snippet | device (in request body)  
**Query params:** position  
**Body schema:** `app-override-rules`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 409, default

### `GET /app-override-rules/{id}`

**Summary:** Get an application override rule  
**Operation ID:** `GetApplicationOverrideRulesByID`  
**Tags:** Application Override Rules  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /app-override-rules/{id}`

**Summary:** Update an application override rule  
**Operation ID:** `UpdateApplicationOverrideRulesByID`  
**Tags:** Application Override Rules  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `app-override-rules`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /app-override-rules/{id}`

**Summary:** Delete an application override rule  
**Operation ID:** `DeleteApplicationOverrideRulesByID`  
**Tags:** Application Override Rules  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `POST /app-override-rules/{id}:move`

**Summary:** Move an application override rule  
**Operation ID:** `MoveApplicationOverrideRulesByID`  
**Tags:** Application Override Rules  
**Body schema:** `rule-based-move`  
**Required fields:** `destination`, `rulebase`  
**Response codes:** 200, 400, 401, 403, 409, default

### `GET /data-filtering-profiles`

**Summary:** List Data Filtering Profiles  
**Operation ID:** `ListDataFilteringProfiles`  
**Tags:** DataFiltering  
**Container scope:** folder | snippet | device  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /data-filtering-profiles`

**Summary:** Create Data Filtering Profile  
**Operation ID:** `CreateDataFilteringProfiles`  
**Tags:** DataFiltering  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `data-filtering-profiles`  
**Response codes:** 200, 400, 401, 403, 409, default

### `GET /data-filtering-profiles/{id}`

**Summary:** Get Data Filtering Profile by ID  
**Operation ID:** `GetDataFilteringProfilesByID`  
**Tags:** DataFiltering  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /data-filtering-profiles/{id}`

**Summary:** Update Data Filtering Profile by ID  
**Operation ID:** `UpdateDataFilteringProfilesByID`  
**Tags:** DataFiltering  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `data-filtering-profiles`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /data-filtering-profiles/{id}`

**Summary:** Delete Data Filtering Profile by ID  
**Operation ID:** `DeleteDataFilteringProfilesByID`  
**Tags:** DataFiltering  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /data-objects`

**Summary:** List Data Objects  
**Operation ID:** `ListDataObjects`  
**Tags:** DataObjects  
**Container scope:** folder | snippet | device  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /data-objects`

**Summary:** Create Data Object  
**Operation ID:** `CreateDataObjects`  
**Tags:** DataObjects  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `data-objects`  
**Response codes:** 200, 400, 401, 403, 409, default

### `GET /data-objects/{id}`

**Summary:** Get Data Object by ID  
**Operation ID:** `GetDataObjectsByID`  
**Tags:** DataObjects  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /data-objects/{id}`

**Summary:** Update Data Object by ID  
**Operation ID:** `UpdateDataObjectsByID`  
**Tags:** DataObjects  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `data-objects`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /data-objects/{id}`

**Summary:** Delete Data Object by ID  
**Operation ID:** `DeleteDataObjectsByID`  
**Tags:** DataObjects  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /decryption-exclusions`

**Summary:** List decryption exclusions  
**Operation ID:** `ListDecryptionExclusions`  
**Tags:** Decryption Exclusions  
**Container scope:** folder | snippet | device  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 409, default

### `POST /decryption-exclusions`

**Summary:** Create a decryption exclusion  
**Operation ID:** `CreateDecryptionExclusions`  
**Tags:** Decryption Exclusions  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `decryption-exclusions`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /decryption-exclusions/{id}`

**Summary:** Get a decryption exclusion  
**Operation ID:** `GetDecryptionExclusionsByID`  
**Tags:** Decryption Exclusions  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /decryption-exclusions/{id}`

**Summary:** Update a decryption exclusion  
**Operation ID:** `UpdateDecryptionExclusionsByID`  
**Tags:** Decryption Exclusions  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `decryption-exclusions`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /decryption-exclusions/{id}`

**Summary:** Delete a decryption exclusion  
**Operation ID:** `DeleteDecryptionExclusionsByID`  
**Tags:** Decryption Exclusions  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /decryption-profiles`

**Summary:** List decryption profiles  
**Operation ID:** `ListDecryptionProfiles`  
**Tags:** Decryption Profiles  
**Container scope:** folder | snippet | device  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /decryption-profiles`

**Summary:** Create a decryption profile  
**Operation ID:** `CreateDecryptionProfiles`  
**Tags:** Decryption Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `decryption-profiles`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /decryption-profiles/{id}`

**Summary:** Get a decryption profile  
**Operation ID:** `GetDecryptionProfilesByID`  
**Tags:** Decryption Profiles  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /decryption-profiles/{id}`

**Summary:** Update a decryption profile  
**Operation ID:** `UpdateDecryptionProfilesByID`  
**Tags:** Decryption Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `decryption-profiles`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /decryption-profiles/{id}`

**Summary:** Delete a decryption profile  
**Operation ID:** `DeleteDecryptionProfilesByID`  
**Tags:** Decryption Profiles  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /decryption-rules`

**Summary:** List decryption rules  
**Operation ID:** `ListDecryptionRules`  
**Tags:** Decryption Rules  
**Container scope:** folder | snippet | device  
**Query params:** name, position, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /decryption-rules`

**Summary:** Create a decryption rule  
**Operation ID:** `CreateDecryptionRules`  
**Tags:** Decryption Rules  
**Container scope:** folder | snippet | device (in request body)  
**Query params:** position  
**Body schema:** `decryption-rules`  
**Required fields:** `name`, `action`, `category`, `destination`, `service`, `source`, `source_user`, `from`, `to`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /decryption-rules/{id}`

**Summary:** Get a decryption rule  
**Operation ID:** `GetDecryptionRulesByID`  
**Tags:** Decryption Rules  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /decryption-rules/{id}`

**Summary:** Update a decryption rule  
**Operation ID:** `UpdateDecryptionRulesByID`  
**Tags:** Decryption Rules  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `decryption-rules`  
**Required fields:** `name`, `action`, `category`, `destination`, `service`, `source`, `source_user`, `from`, `to`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /decryption-rules/{id}`

**Summary:** Delete a decryption rule  
**Operation ID:** `DeleteDecryptionRulesByID`  
**Tags:** Decryption Rules  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `POST /decryption-rules/{id}:move`

**Summary:** Move a decryption rule  
**Operation ID:** `MoveDecryptionRulesByID`  
**Tags:** Decryption Rules  
**Body schema:** `rule-based-move`  
**Required fields:** `destination`, `rulebase`  
**Response codes:** 200, 400, 401, 403, 409, default

### `GET /ssl-decryption-settings`

**Summary:** GET Ssl Decryption Settings  
**Operation ID:** `getSslDecryptionSettings`  
**Tags:** Ssl Decryption Settings  
**Container scope:** folder | snippet | device  
**Query params:** offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /ssl-decryption-settings`

**Summary:** POST Ssl Decryption Settings  
**Operation ID:** `postSslDecryptionSettings`  
**Tags:** Ssl Decryption Settings  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `ssl-decryption-settings`  
**Response codes:** 200, 400, 401, 403, 409, default

### `PUT /ssl-decryption-settings`

**Summary:** PUT Ssl Decryption Settings  
**Operation ID:** `putSslDecryptionSettings`  
**Tags:** Ssl Decryption Settings  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `ssl-decryption-settings-get-put`  
**Required fields:** `ssl_decrypt`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /ssl-decryption-settings`

**Summary:** DELETE Ssl Decryption Settings  
**Operation ID:** `deleteSslDecryptionSettings`  
**Tags:** Ssl Decryption Settings  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /dns-security-profiles`

**Summary:** List DNS security profiles  
**Operation ID:** `ListDNSSecurityProfiles`  
**Tags:** DNS Security Profiles  
**Container scope:** folder | snippet | device  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /dns-security-profiles`

**Summary:** Create a DNS security profile  
**Operation ID:** `CreateDNSSecurityProfiles`  
**Tags:** DNS Security Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `dns-security-profiles`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /dns-security-profiles/{id}`

**Summary:** Get a DNS security profile  
**Operation ID:** `GetDNSSecurityProfilesByID`  
**Tags:** DNS Security Profiles  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /dns-security-profiles/{id}`

**Summary:** Update a DNS security profile  
**Operation ID:** `UpdateDNSSecurityProfilesByID`  
**Tags:** DNS Security Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `dns-security-profiles`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /dns-security-profiles/{id}`

**Summary:** Delete a DNS security profile  
**Operation ID:** `DeleteDNSSecurityProfilesByID`  
**Tags:** DNS Security Profiles  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /dos-protection-profiles`

**Summary:** List DoS protection profiles  
**Operation ID:** `ListDoSProtectionProfiles`  
**Tags:** DoS Protection Profiles  
**Container scope:** folder | snippet | device  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /dos-protection-profiles`

**Summary:** Create a DoS protection profile  
**Operation ID:** `CreateDoSProtectionProfiles`  
**Tags:** DoS Protection Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `dos-protection-profiles`  
**Required fields:** `name`, `type`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /dos-protection-profiles/{id}`

**Summary:** Get a DoS protection profile  
**Operation ID:** `GetDoSProtectionProfilesByID`  
**Tags:** DoS Protection Profiles  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /dos-protection-profiles/{id}`

**Summary:** Update a DoS protection profile  
**Operation ID:** `UpdateDoSProtectionProfilesByID`  
**Tags:** DoS Protection Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `dos-protection-profiles`  
**Required fields:** `name`, `type`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /dos-protection-profiles/{id}`

**Summary:** Delete a DoS protection profile  
**Operation ID:** `DeleteDoSProtectionProfilesByID`  
**Tags:** DoS Protection Profiles  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /dos-protection-rules`

**Summary:** List DoS protection rules  
**Operation ID:** `ListDoSProtectionRules`  
**Tags:** DoS Protection Rules  
**Container scope:** folder | snippet | device  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /dos-protection-rules`

**Summary:** Create a DoS protection rule  
**Operation ID:** `CreateDoSProtectionRules`  
**Tags:** DoS Protection Rules  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `dos-protection-rules`  
**Required fields:** `name`, `type`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /dos-protection-rules/{id}`

**Summary:** Get a DoS protection rule  
**Operation ID:** `GetDoSProtectionRulesByID`  
**Tags:** DoS Protection Rules  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /dos-protection-rules/{id}`

**Summary:** Update a DoS protection rule  
**Operation ID:** `UpdateDoSProtectionRulesByID`  
**Tags:** DoS Protection Rules  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `dos-protection-rules`  
**Required fields:** `name`, `type`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /dos-protection-rules/{id}`

**Summary:** Delete a DoS protection rule  
**Operation ID:** `DeleteDoSProtectionRulesByID`  
**Tags:** DoS Protection Rules  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /file-blocking-profiles`

**Summary:** List file blocking profiles  
**Operation ID:** `ListFileBlockingProfiles`  
**Tags:** File Blocking Profiles  
**Container scope:** folder | snippet | device  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /file-blocking-profiles`

**Summary:** Create a file blocking profiles  
**Operation ID:** `CreateFileBlockingProfiles`  
**Tags:** File Blocking Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `file-blocking-profiles`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /file-blocking-profiles/{id}`

**Summary:** Get a file blocking profile  
**Operation ID:** `GetFileBlockingProfilesByID`  
**Tags:** File Blocking Profiles  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /file-blocking-profiles/{id}`

**Summary:** Update a file blocking profile  
**Operation ID:** `UpdateFileBlockingProfilesByID`  
**Tags:** File Blocking Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `file-blocking-profiles`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /file-blocking-profiles/{id}`

**Summary:** Delete a file blocking profile  
**Operation ID:** `DeleteFileBlockingProfilesByID`  
**Tags:** File Blocking Profiles  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /http-header-profiles`

**Summary:** List HTTP header profiles  
**Operation ID:** `ListHTTPHeaderProfiles`  
**Tags:** HTTP Header Profiles  
**Container scope:** folder | snippet | device  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /http-header-profiles`

**Summary:** Create an HTTP header profile  
**Operation ID:** `CreateHTTPHeaderProfiles`  
**Tags:** HTTP Header Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `http-header-profiles`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /http-header-profiles/{id}`

**Summary:** Get an HTTP header profile  
**Operation ID:** `GetHTTPHeaderProfilesByID`  
**Tags:** HTTP Header Profiles  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /http-header-profiles/{id}`

**Summary:** Update an HTTP header profile  
**Operation ID:** `UpdateHTTPHeaderProfilesByID`  
**Tags:** HTTP Header Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `http-header-profiles`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /http-header-profiles/{id}`

**Summary:** Delete an HTTP header profile  
**Operation ID:** `DeleteHTTPHeaderProfilesByID`  
**Tags:** HTTP Header Profiles  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /profile-groups`

**Summary:** List profile groups  
**Operation ID:** `ListProfileGroups`  
**Tags:** Profile Groups  
**Container scope:** folder | snippet | device  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /profile-groups`

**Summary:** Create a profile group  
**Operation ID:** `CreateProfileGroups`  
**Tags:** Profile Groups  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `profile-groups`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 409, default

### `GET /profile-groups/{id}`

**Summary:** Get a profile group  
**Operation ID:** `GetProfileGroupsByID`  
**Tags:** Profile Groups  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /profile-groups/{id}`

**Summary:** Update a profile group  
**Operation ID:** `UpdateProfileGroupsByID`  
**Tags:** Profile Groups  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `profile-groups`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /profile-groups/{id}`

**Summary:** Delete a profile group  
**Operation ID:** `DeleteProfileGroupsByID`  
**Tags:** Profile Groups  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /security-rules`

**Summary:** List security rules  
**Operation ID:** `ListRules`  
**Tags:** Security Rules  
**Container scope:** folder | snippet | device  
**Query params:** name, position, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /security-rules`

**Summary:** Create a security rule  
**Operation ID:** `CreateSecurityRules`  
**Tags:** Security Rules  
**Query params:** position  
**Body schema:** `security-rules`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /security-rules/{id}`

**Summary:** Get a security rule  
**Operation ID:** `GetSecurityRulesByID`  
**Tags:** Security Rules  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /security-rules/{id}`

**Summary:** Update a security rule  
**Operation ID:** `UpdateSecurityRulesByID`  
**Tags:** Security Rules  
**Body schema:** `security-rules`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /security-rules/{id}`

**Summary:** Delete a security rule  
**Operation ID:** `DeleteSecurityRulesByID`  
**Tags:** Security Rules  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `POST /security-rules/{id}:move`

**Summary:** Move a security rule  
**Operation ID:** `MoveSecurityRulesByID`  
**Tags:** Security Rules  
**Body schema:** `rule-based-move`  
**Required fields:** `destination`, `rulebase`  
**Response codes:** 200, 400, 401, 403, 409, default

### `GET /url-access-profiles`

**Summary:** List URL access profiles  
**Operation ID:** `ListURLAccessProfiles`  
**Tags:** URL Access Profiles  
**Container scope:** folder | snippet | device  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /url-access-profiles`

**Summary:** Create a URL access profile  
**Operation ID:** `CreateURLAccessProfiles`  
**Tags:** URL Access Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `url-access-profiles`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /url-access-profiles/{id}`

**Summary:** Get a URL access profile  
**Operation ID:** `GetURLAccessProfilesByID`  
**Tags:** URL Access Profiles  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /url-access-profiles/{id}`

**Summary:** Update a URL access Profile  
**Operation ID:** `UpdateURLAccessProfilesByID`  
**Tags:** URL Access Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `url-access-profiles`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /url-access-profiles/{id}`

**Summary:** Delete a URL access profile  
**Operation ID:** `DeleteURLAccessProfilesByID`  
**Tags:** URL Access Profiles  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /url-categories`

**Summary:** List custom URL categories  
**Operation ID:** `ListURLCategories`  
**Tags:** URL Categories  
**Container scope:** folder | snippet | device  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /url-categories`

**Summary:** Create a custom URL category  
**Operation ID:** `CreateURLCategories`  
**Tags:** URL Categories  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `url-categories`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /url-categories/{id}`

**Summary:** Get a custom URL category  
**Operation ID:** `GetURLCategoriesByID`  
**Tags:** URL Categories  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /url-categories/{id}`

**Summary:** Update a custom URL category  
**Operation ID:** `UpdateURLCategoriesByID`  
**Tags:** URL Categories  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `url-categories`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /url-categories/{id}`

**Summary:** Delete a custom URL Category  
**Operation ID:** `DeleteURLCategoriesByID`  
**Tags:** URL Categories  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /url-filtering-categories`

**Summary:** List custom URL categories  
**Operation ID:** `ListURLFilteringCategories`  
**Tags:** URL Filtering Categories  
**Container scope:** folder | snippet | device  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `GET /url-admin-override`

**Summary:** URL Admin Override  
**Operation ID:** `URLAdminOverride`  
**Tags:** URL Admin Override  
**Container scope:** folder | snippet | device  
**Query params:** name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /url-admin-override`

**Summary:** Add URL Admin Override  
**Operation ID:** `AddURLAdminOverride`  
**Tags:** URL Admin Override  
**Container scope:** folder | snippet | device  
**Body schema:** `url-admin-override-post`  
**Type variants (oneOf/anyOf):** `mode(transparent/redirect)`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /url-admin-override/{id}`

**Summary:** Delete a url admin override  
**Operation ID:** `DeleteURLAdminOverrideByUUID`  
**Tags:** URL Admin Override  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /vulnerability-protection-profiles`

**Summary:** List vulnerability protection profiles  
**Operation ID:** `ListVulnerabilityProtectionProfiles`  
**Tags:** Vulnerability Protection Profiles  
**Container scope:** folder | snippet | device  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /vulnerability-protection-profiles`

**Summary:** Create a vulnerability protection profile  
**Operation ID:** `CreateVulnerabilityProtectionProfiles`  
**Tags:** Vulnerability Protection Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `vulnerability-protection-profiles`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /vulnerability-protection-profiles/{id}`

**Summary:** Get a vulnerability protection profile  
**Operation ID:** `GetVulnerabilityProtectionProfilesByID`  
**Tags:** Vulnerability Protection Profiles  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /vulnerability-protection-profiles/{id}`

**Summary:** Update an vulnerability protection profile  
**Operation ID:** `UpdateVulnerabilityProtectionProfilesByID`  
**Tags:** Vulnerability Protection Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `vulnerability-protection-profiles`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /vulnerability-protection-profiles/{id}`

**Summary:** Delete a vulnerability protection profile  
**Operation ID:** `DeleteVulnerabilityProtectionProfilesByID`  
**Tags:** Vulnerability Protection Profiles  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /vulnerability-protection-signatures`

**Summary:** List vulnerability protection signatures  
**Operation ID:** `ListVulnerabilityProtectionSignatures`  
**Tags:** Vulnerability Protection Signatures  
**Container scope:** folder | snippet | device  
**Query params:** offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /vulnerability-protection-signatures`

**Summary:** Create a vulnerability protection signature  
**Operation ID:** `CreateVulnerabilityProtectionSignatures`  
**Tags:** Vulnerability Protection Signatures  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `vulnerability-protection-signatures`  
**Required fields:** `threat_id`, `threatname`, `affected_host`, `severity`, `direction`, `signature`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /vulnerability-protection-signatures/{id}`

**Summary:** Get a vulnerability protection signature  
**Operation ID:** `GetVulnerabilityProtectionSignaturesByID`  
**Tags:** Vulnerability Protection Signatures  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /vulnerability-protection-signatures/{id}`

**Summary:** Update a vulnerability protection signature  
**Operation ID:** `UpdateVulnerabilityProtectionSignaturesByID`  
**Tags:** Vulnerability Protection Signatures  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `vulnerability-protection-signatures`  
**Required fields:** `threat_id`, `threatname`, `affected_host`, `severity`, `direction`, `signature`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /vulnerability-protection-signatures/{id}`

**Summary:** Delete a vulnerability protection signature  
**Operation ID:** `DeleteVulnerabilityProtectionSignaturesByID`  
**Tags:** Vulnerability Protection Signatures  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /wildfire-anti-virus-profiles`

**Summary:** List Wildfire and anti-virus profiles  
**Operation ID:** `ListWildFireAntiVirusProfiles`  
**Tags:** WildFire Anti-Virus Profiles  
**Container scope:** folder | snippet | device  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /wildfire-anti-virus-profiles`

**Summary:** Create a WildFire and anti-virus profile  
**Operation ID:** `CreateWildFireAntiVirusProfiles`  
**Tags:** WildFire Anti-Virus Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `wildfire-anti-virus-profiles`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /wildfire-anti-virus-profiles/{id}`

**Summary:** Get a WildFire and anti-virus profile  
**Operation ID:** `GetWildFireAntiVirusProfilesByID`  
**Tags:** WildFire Anti-Virus Profiles  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /wildfire-anti-virus-profiles/{id}`

**Summary:** Update a wildfire and antivirus profile  
**Operation ID:** `UpdateWildFireAntiVirusProfilesByID`  
**Tags:** WildFire Anti-Virus Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `wildfire-anti-virus-profiles`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /wildfire-anti-virus-profiles/{id}`

**Summary:** Delete a WildFire and anti-virus profile  
**Operation ID:** `DeleteWildFireAntiVirusProfilesByID`  
**Tags:** WildFire Anti-Virus Profiles  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /saas-tenant-restrictions`

**Summary:** Get Saas Tenant Restrictions  
**Operation ID:** `GetSaasTenantRestrictions`  
**Tags:** Saas Tenant Restrictions  
**Container scope:** folder | snippet | device  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `PUT /saas-tenant-restrictions`

**Summary:** Update Saas Tenant Restrictions  
**Operation ID:** `UpdateSaasTenantRestrictions`  
**Tags:** Saas Tenant Restrictions  
**Container scope:** snippet  
**Body schema:** `saas-tenant-restrictions`  
**Response codes:** 200, 400, 401, 403, 404, 409, default
