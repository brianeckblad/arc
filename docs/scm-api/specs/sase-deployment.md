# Network Deployment

**Version:** 2.0.0  
**Source:** `openapi-specs/scm/config/sase/deployment/deployment-services-march.yaml`  
**Base URL:** `https://api.strata.paloaltonetworks.com/config/deployment/v1`  
**Endpoints:** 40  
**GitHub:** https://github.com/PaloAltoNetworks/pan.dev/blob/master/openapi-specs/scm/config/sase/deployment/deployment-services-march.yaml

---

## Endpoints

### `GET /bandwidth-allocations`

**Summary:** List bandwidth regions  
**Operation ID:** `ListBandwidthAllocations`  
**Tags:** Bandwidth Allocations  
**Query params:** limit, offset  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /bandwidth-allocations`

**Summary:** Create a bandwidth allocation  
**Operation ID:** `CreateBandwidthAllocations`  
**Tags:** Bandwidth Allocations  
**Body schema:** `bandwidth-allocations`  
**Required fields:** `name`, `allocated_bandwidth`  
**Response codes:** 201, 400, 401, 403, 409, default

### `PUT /bandwidth-allocations`

**Summary:** Update a bandwidth allocation  
**Operation ID:** `UpdateBandwidthAllocations`  
**Tags:** Bandwidth Allocations  
**Body schema:** `bandwidth-allocations`  
**Required fields:** `name`, `allocated_bandwidth`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /bandwidth-allocations`

**Summary:** Delete a bandwidth allocation  
**Operation ID:** `DeleteBandwidthAllocations`  
**Tags:** Bandwidth Allocations  
**Query params:** name, spn_name_list  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /bgp-routing`

**Summary:** Get BGP routing settings  
**Operation ID:** `GetBGPRouting`  
**Tags:** BGP Routing  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /bgp-routing`

**Summary:** Update BGP routing settings  
**Operation ID:** `UpdateBGPRouting`  
**Tags:** BGP Routing  
**Body schema:** `bgp-routing`  
**Type variants (oneOf/anyOf):** `routing_preference(default/hot_potato_routing)`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `POST /enable`

**Summary:** Create application defaults  
**Operation ID:** `CreateApplicationDefaults`  
**Tags:** Application Defaults  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /internal-dns-servers`

**Summary:** List internal DNS servers  
**Operation ID:** `ListInternalDNSServers`  
**Tags:** Internal DNS Servers  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /internal-dns-servers`

**Summary:** Create a internal DNS server  
**Operation ID:** `CreateInternalDNSServers`  
**Tags:** Internal DNS Servers  
**Body schema:** `internal-dns-servers`  
**Required fields:** `id`, `name`, `domain_name`, `primary`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /internal-dns-servers/{id}`

**Summary:** Get an internal DNS server  
**Operation ID:** `GetInternalDNSServersByID`  
**Tags:** Internal DNS Servers  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /internal-dns-servers/{id}`

**Summary:** Update an internal DNS server  
**Operation ID:** `UpdateInternalDNSServersByID`  
**Tags:** Internal DNS Servers  
**Body schema:** `internal-dns-servers`  
**Required fields:** `id`, `name`, `domain_name`, `primary`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /internal-dns-servers/{id}`

**Summary:** Delete an internal DNS server  
**Operation ID:** `DeleteInternalDNSServersByID`  
**Tags:** Internal DNS Servers  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /locations`

**Summary:** List locations  
**Operation ID:** `ListLocations`  
**Tags:** Network Locations  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /remote-networks`

**Summary:** List remote networks  
**Operation ID:** `ListRemoteNetworks`  
**Tags:** Remote Networks  
**Container scope:** folder  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /remote-networks`

**Summary:** Create a remote network  
**Operation ID:** `CreateRemoteNetworks`  
**Tags:** Remote Networks  
**Body schema:** `remote-networks`  
**Required fields:** `id`, `name`, `folder`, `license_type`, `region`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /remote-networks/{id}`

**Summary:** Get a remote network  
**Operation ID:** `GetRemoteNetworksByID`  
**Tags:** Remote Networks  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /remote-networks/{id}`

**Summary:** Update a remote network  
**Operation ID:** `UpdateRemoteNetworksByID`  
**Tags:** Remote Networks  
**Body schema:** `remote-networks`  
**Required fields:** `id`, `name`, `folder`, `license_type`, `region`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /remote-networks/{id}`

**Summary:** Delete a remote network  
**Operation ID:** `DeleteRemoteNetworksByID`  
**Tags:** Remote Networks  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /service-connections`

**Summary:** List service connections  
**Operation ID:** `ListServiceConnections`  
**Tags:** Service Connections  
**Container scope:** folder  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /service-connections`

**Summary:** Create a service connection  
**Operation ID:** `CreateServiceConnections`  
**Tags:** Service Connections  
**Body schema:** `service-connections`  
**Required fields:** `id`, `name`, `ipsec_tunnel`, `region`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /service-connections/{id}`

**Summary:** Get a service connection  
**Operation ID:** `GetServiceConnectionsByID`  
**Tags:** Service Connections  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /service-connections/{id}`

**Summary:** Update a service connection  
**Operation ID:** `UpdateServiceConnectionsByID`  
**Tags:** Service Connections  
**Body schema:** `service-connections`  
**Required fields:** `id`, `name`, `ipsec_tunnel`, `region`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /service-connections/{id}`

**Summary:** Delete a service connection  
**Operation ID:** `DeleteServiceConnectionsByID`  
**Tags:** Service Connections  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /service-connection-groups`

**Summary:** List service connection groups  
**Operation ID:** `ListServiceConnectionGroups`  
**Tags:** Service Connection Groups  
**Container scope:** folder  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /service-connection-groups`

**Summary:** Create a service connection group  
**Operation ID:** `CreateServiceConnectionGroups`  
**Tags:** Service Connection Groups  
**Body schema:** `service-connection-groups`  
**Required fields:** `id`, `name`, `target`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /service-connection-groups/{id}`

**Summary:** Get a service connection group  
**Operation ID:** `GetServiceConnectionGroupsByID`  
**Tags:** Service Connection Groups  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /service-connection-groups/{id}`

**Summary:** Update a service connection group  
**Operation ID:** `UpdateServiceConnectionGroupsByID`  
**Tags:** Service Connection Groups  
**Body schema:** `service-connection-groups`  
**Required fields:** `id`, `name`, `target`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /service-connection-groups/{id}`

**Summary:** Delete a service connection group  
**Operation ID:** `DeleteServiceConnectionGroupsByID`  
**Tags:** Service Connection Groups  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /shared-infrastructure-settings`

**Summary:** Get shared infrastructure settings  
**Operation ID:** `GetSharedInfrastructureSettings`  
**Tags:** Shared Infrastructure Settings  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /shared-infrastructure-settings`

**Summary:** Update infrastructure settings  
**Operation ID:** `UpdateSharedInfrastructureSettings`  
**Tags:** Shared Infrastructure Settings  
**Body schema:** `edit-shared-infrastructure-settings`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /traffic-steering-rules`

**Summary:** List traffic steering rules  
**Operation ID:** `ListTrafficSteeringRules`  
**Tags:** Traffic Steering Rules  
**Container scope:** folder  
**Query params:** name, limit, offset  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /traffic-steering-rules`

**Summary:** Create a traffic steering rule  
**Operation ID:** `CreateTrafficSteeringRules`  
**Tags:** Traffic Steering Rules  
**Container scope:** folder  
**Body schema:** `traffic-steering-rules`  
**Required fields:** `id`, `name`, `service`, `source`  
**Type variants (oneOf/anyOf):** `action(forward)`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /traffic-steering-rules/{id}`

**Summary:** Get a traffic steering rule  
**Operation ID:** `GetTrafficSteeringRulesByID`  
**Tags:** Traffic Steering Rules  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /traffic-steering-rules/{id}`

**Summary:** Update a traffic steering rule  
**Operation ID:** `UpdateTrafficSteeringRulesByID`  
**Tags:** Traffic Steering Rules  
**Body schema:** `traffic-steering-rules`  
**Required fields:** `id`, `name`, `service`, `source`  
**Type variants (oneOf/anyOf):** `action(forward)`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /traffic-steering-rules/{id}`

**Summary:** Delete a traffic steering rule  
**Operation ID:** `DeleteTrafficSteeringRulesByID`  
**Tags:** Traffic Steering Rules  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /sites`

**Summary:** List sites  
**Operation ID:** `ListSites`  
**Tags:** Sites  
**Container scope:** folder  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /sites`

**Summary:** Create a site  
**Operation ID:** `CreateSites`  
**Tags:** Sites  
**Body schema:** `sites`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /sites/{id}`

**Summary:** Get a site  
**Operation ID:** `GetSitesByID`  
**Tags:** Sites  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /sites/{id}`

**Summary:** Update a site  
**Operation ID:** `UpdateSitesByID`  
**Tags:** Sites  
**Body schema:** `sites`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /sites/{id}`

**Summary:** Delete a site  
**Operation ID:** `DeleteSitesByID`  
**Tags:** Sites  
**Response codes:** 200, 400, 401, 403, 404, 409, default
