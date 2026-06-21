# GlobalProtect

**Version:** 2.0.0  
**Source:** `openapi-specs/scm/config/sase/mobileagent/mobile-agent-feb-v1.yaml`  
**Base URL:** `https://api.strata.paloaltonetworks.com/config/mobile-agent/v1`  
**Endpoints:** 49  
**GitHub:** https://github.com/PaloAltoNetworks/pan.dev/blob/master/openapi-specs/scm/config/sase/mobileagent/mobile-agent-feb-v1.yaml

---

## Endpoints

### `GET /agent-profiles`

**Summary:** List GlobalProtect agent profiles  
**Operation ID:** `ListGlobalProtectAgentProfiles`  
**Tags:** Application Settings  
**Container scope:** folder  
**Query params:** name, limit, offset  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /agent-profiles`

**Summary:** Create a GlobalProtect agent profile  
**Operation ID:** `CreateGlobalProtectAgentProfiles`  
**Tags:** Application Settings  
**Container scope:** folder  
**Body schema:** `agent-profiles`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `PUT /agent-profiles`

**Summary:** Update a GlobalProtect agent profile  
**Operation ID:** `UpdateGlobalProtectAgentProfiles`  
**Tags:** Application Settings  
**Container scope:** folder  
**Body schema:** `agent-profiles`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /agent-profiles`

**Summary:** Delete a GlobalProtect agent profile  
**Operation ID:** `DeleteGlobalProtectAgentProfiles`  
**Tags:** Application Settings  
**Container scope:** folder  
**Query params:** name  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /agent-versions`

**Summary:** List GlobalProtect agent versions  
**Operation ID:** `ListGlobalProtectVersions`  
**Tags:** Agent Versions  
**Response codes:** 200, 400, 401, 403, 404, default

### `GET /authentication-settings`

**Summary:** List GlobalProtect authentication settings  
**Operation ID:** `GetGlobalProtectAuthenticationSettings`  
**Tags:** Agent Authentication Settings  
**Container scope:** folder  
**Query params:** name, limit, offset  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /authentication-settings`

**Summary:** Create a GlobalProtect authentication setting  
**Operation ID:** `CreateGlobalProtectAuthenticationSettings`  
**Tags:** Agent Authentication Settings  
**Container scope:** folder  
**Body schema:** `authentication-settings`  
**Required fields:** `authentication_profile`, `os`, `user_credential_or_client_cert_required`  
**Response codes:** 201, 400, 401, 403, 409, default

### `PUT /authentication-settings`

**Summary:** Update a GlobalProtect authentication setting  
**Operation ID:** `UpdateGlobalProtectAuthenticationSettings`  
**Tags:** Agent Authentication Settings  
**Container scope:** folder  
**Body schema:** `authentication-settings`  
**Required fields:** `authentication_profile`, `os`, `user_credential_or_client_cert_required`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /authentication-settings`

**Summary:** Delete a GlobalProtect authentication setting  
**Operation ID:** `DeleteGlobalProtectAuthenticationSettings`  
**Tags:** Agent Authentication Settings  
**Container scope:** folder  
**Query params:** name  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `POST /authentication-settings/{name}:move`

**Summary:** Move a GlobalProtect authentication setting  
**Operation ID:** `MoveGlobalProtectAuthenticationSettings`  
**Tags:** Agent Authentication Settings  
**Container scope:** folder  
**Body schema:** `move-auth-settings`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /enable`

**Summary:** Get GlobalProtect enablement status  
**Operation ID:** `GetGlobalProtectEnablement`  
**Tags:** GlobalProtect Enablement  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /enable`

**Summary:** Enable GlobalProtect  
**Operation ID:** `CreateGlobalProtectEnablement`  
**Tags:** GlobalProtect Enablement  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /global-settings`

**Summary:** List GlobalProtect global settings  
**Operation ID:** `GetGlobalProtectSettings`  
**Tags:** Global Settings  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /global-settings`

**Summary:** Update GlobalProtect global settings  
**Operation ID:** `UpdateMobileAgentSettings`  
**Tags:** Global Settings  
**Body schema:** `mobile-agent-global-settings`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /infrastructure-settings`

**Summary:** List GlobalProtect infrastructure settings  
**Operation ID:** `GetGlobalProtectInfrastructureSettings`  
**Tags:** Infrastructure Settings  
**Container scope:** folder  
**Query params:** name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /infrastructure-settings`

**Summary:** Create a GlobalProtect infrastructure setting  
**Operation ID:** `CreateGlobalProtectInfrastructureSettings`  
**Tags:** Infrastructure Settings  
**Container scope:** folder  
**Body schema:** `mobile-agent-infrastructure-settings`  
**Required fields:** `id`, `name`, `dns_servers`, `ip_pools`, `portal_hostname`  
**Response codes:** 201, 400, 401, 403, 409, default

### `PUT /infrastructure-settings`

**Summary:** Update a GlobalProtect infrastructure setting  
**Operation ID:** `UpdateGlobalProtectInfrastructureSettings`  
**Tags:** Infrastructure Settings  
**Container scope:** folder  
**Body schema:** `mobile-agent-infrastructure-settings`  
**Required fields:** `id`, `name`, `dns_servers`, `ip_pools`, `portal_hostname`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /infrastructure-settings`

**Summary:** Delete a GlobalProtect infrastructure setting  
**Operation ID:** `DeleteGlobalProtectInfrastructureSettings`  
**Tags:** Infrastructure Settings  
**Container scope:** folder  
**Query params:** name  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /locations`

**Summary:** List GlobalProtect locations  
**Operation ID:** `ListGlobalProtectLocations`  
**Tags:** Mobile User Locations  
**Container scope:** folder  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /locations`

**Summary:** Select a GlobalProtect location  
**Operation ID:** `UpdateGlobalProtectLocations`  
**Tags:** Mobile User Locations  
**Container scope:** folder  
**Body schema:** `mobile-agent-locations`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /tunnel-profiles`

**Summary:** List GlobalProtect tunnel settings  
**Operation ID:** `ListGlobalProtectTunnelSettings`  
**Tags:** Tunnel Settings  
**Container scope:** folder  
**Query params:** name, limit, offset  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /tunnel-profiles`

**Summary:** Create a GlobalProtect tunnel setting  
**Operation ID:** `CreateGlobalProtectTunnelSettings`  
**Tags:** Tunnel Settings  
**Container scope:** folder  
**Body schema:** `tunnel-profiles`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `PUT /tunnel-profiles`

**Summary:** Update a GlobalProtect tunnel setting  
**Operation ID:** `UpdateGlobalProtectTunnelSettings`  
**Tags:** Tunnel Settings  
**Container scope:** folder  
**Body schema:** `tunnel-profiles`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /tunnel-profiles`

**Summary:** Delete a GlobalProtect tunnel setting  
**Operation ID:** `DeleteGlobalProtectTunnelSettings`  
**Tags:** Tunnel Settings  
**Container scope:** folder  
**Query params:** name  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /forwarding-profiles`

**Summary:** List GlobalProtect forwarding profiles  
**Operation ID:** `ListGlobalProtectForwardingProfiles`  
**Tags:** Forwarding Profiles  
**Container scope:** folder  
**Query params:** name, limit, offset  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /forwarding-profiles`

**Summary:** Create a GlobalProtect forwarding profile  
**Operation ID:** `CreateGlobalProtectForwardingProfile`  
**Tags:** Forwarding Profiles  
**Container scope:** folder  
**Body schema:** `forwarding-profile`  
**Required fields:** `name`  
**Type variants (oneOf/anyOf):** `type(pac_file/global_protect_proxy/ztna_agent)`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /forwarding-profiles/{id}`

**Summary:** Get a GlobalProtect forwarding profile  
**Operation ID:** `GetGlobalProtectForwardingProfileByID`  
**Tags:** Forwarding Profiles  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /forwarding-profiles/{id}`

**Summary:** Update a GlobalProtect forwarding profile  
**Operation ID:** `UpdateGlobalProtectForwardingProfileByID`  
**Tags:** Forwarding Profiles  
**Body schema:** `forwarding-profile`  
**Required fields:** `name`  
**Type variants (oneOf/anyOf):** `type(pac_file/global_protect_proxy/ztna_agent)`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /forwarding-profiles/{id}`

**Summary:** Delete a GlobalProtect forwarding profile  
**Operation ID:** `DeleteGlobalProtectForwardingProfile`  
**Tags:** Forwarding Profiles  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /forwarding-profile-destinations`

**Summary:** List GlobalProtect destinations  
**Operation ID:** `ListGlobalProtectDestinations`  
**Tags:** Destinations  
**Container scope:** folder  
**Query params:** name, limit, offset  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /forwarding-profile-destinations`

**Summary:** Create a GlobalProtect destination  
**Operation ID:** `CreateGlobalProtectDestination`  
**Tags:** Destinations  
**Container scope:** folder  
**Body schema:** `destination`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /forwarding-profile-destinations/{id}`

**Summary:** Get a GlobalProtect destination  
**Operation ID:** `GetGlobalProtectDestinationByID`  
**Tags:** Destinations  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /forwarding-profile-destinations/{id}`

**Summary:** Update a GlobalProtect destination  
**Operation ID:** `UpdateGlobalProtectDestinationByID`  
**Tags:** Destinations  
**Body schema:** `destination`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /forwarding-profile-destinations/{id}`

**Summary:** Delete a GlobalProtect destination  
**Operation ID:** `DeleteGlobalProtectDestination`  
**Tags:** Destinations  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /forwarding-profile-source-applications`

**Summary:** List GlobalProtect source applications  
**Operation ID:** `ListGlobalProtectSourceApplications`  
**Tags:** Source Applications  
**Container scope:** folder  
**Query params:** name, limit, offset  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /forwarding-profile-source-applications`

**Summary:** Create a GlobalProtect source application  
**Operation ID:** `CreateGlobalProtectSourceApplication`  
**Tags:** Source Applications  
**Container scope:** folder  
**Body schema:** `source-application`  
**Required fields:** `name`, `applications`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /forwarding-profile-source-applications/{id}`

**Summary:** Get a GlobalProtect source application  
**Operation ID:** `GetGlobalProtectSourceApplicationByID`  
**Tags:** Source Applications  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /forwarding-profile-source-applications/{id}`

**Summary:** Update a GlobalProtect source application  
**Operation ID:** `UpdateGlobalProtectSourceApplicationByID`  
**Tags:** Source Applications  
**Body schema:** `source-application`  
**Required fields:** `name`, `applications`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /forwarding-profile-source-applications/{id}`

**Summary:** Delete a GlobalProtect source application  
**Operation ID:** `DeleteGlobalProtectSourceApplication`  
**Tags:** Source Applications  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /forwarding-profile-user-locations`

**Summary:** List GlobalProtect user locations  
**Operation ID:** `ListGlobalProtectUserLocations`  
**Tags:** User Locations  
**Container scope:** folder  
**Query params:** name, limit, offset  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /forwarding-profile-user-locations`

**Summary:** Create a GlobalProtect user location  
**Operation ID:** `CreateGlobalProtectUserLocation`  
**Tags:** User Locations  
**Container scope:** folder  
**Body schema:** `user-location`  
**Required fields:** `name`, `choice`  
**Type variants (oneOf/anyOf):** `choice(internal-host-detection/ip-addresses)`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /forwarding-profile-user-locations/{id}`

**Summary:** Get a GlobalProtect user location  
**Operation ID:** `GetGlobalProtectUserLocationByID`  
**Tags:** User Locations  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /forwarding-profile-user-locations/{id}`

**Summary:** Update a GlobalProtect user location  
**Operation ID:** `UpdateGlobalProtectUserLocationByID`  
**Tags:** User Locations  
**Body schema:** `user-location`  
**Required fields:** `name`, `choice`  
**Type variants (oneOf/anyOf):** `choice(internal-host-detection/ip-addresses)`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /forwarding-profile-user-locations/{id}`

**Summary:** Delete a GlobalProtect user location  
**Operation ID:** `DeleteGlobalProtectUserLocation`  
**Tags:** User Locations  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /forwarding-profile-regional-and-custom-proxies`

**Summary:** List GlobalProtect regional and custom proxies  
**Operation ID:** `ListGlobalProtectRegionalAndCustomProxies`  
**Tags:** Regional and Custom Proxies  
**Container scope:** folder  
**Query params:** name, limit, offset  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /forwarding-profile-regional-and-custom-proxies`

**Summary:** Create a GlobalProtect regional and custom proxy  
**Operation ID:** `CreateGlobalProtectRegionalAndCustomProxies`  
**Tags:** Regional and Custom Proxies  
**Container scope:** folder  
**Body schema:** `regional-and-custom-proxy`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /forwarding-profile-regional-and-custom-proxies/{id}`

**Summary:** Get a GlobalProtect regional and custom proxy  
**Operation ID:** `GetGlobalProtectRegionalAndCustomProxyByID`  
**Tags:** Regional and Custom Proxies  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /forwarding-profile-regional-and-custom-proxies/{id}`

**Summary:** Update a GlobalProtect regional and custom proxy  
**Operation ID:** `UpdateGlobalProtectRegionalAndCustomProxyByID`  
**Tags:** Regional and Custom Proxies  
**Body schema:** `regional-and-custom-proxy`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /forwarding-profile-regional-and-custom-proxies/{id}`

**Summary:** Delete a GlobalProtect regional and custom proxy  
**Operation ID:** `DeleteGlobalProtectRegionalAndCustomProxies`  
**Tags:** Regional and Custom Proxies  
**Response codes:** 200, 400, 401, 403, 404, 409, default
