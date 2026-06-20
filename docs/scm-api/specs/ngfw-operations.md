# Operations and Troubleshooting

**Version:** 2.0.0  
**Source:** `openapi-specs/scm/config/ngfw-operations/operations-R2-2026.yaml`  
**Base URL:** `https://api.strata.paloaltonetworks.com/operations/v1`  
**Endpoints:** 10  
**GitHub:** https://github.com/PaloAltoNetworks/pan.dev/blob/master/openapi-specs/scm/config/ngfw-operations/operations-R2-2026.yaml

---

## Endpoints

### `GET /local-config/versions`

**Summary:** List local configuration versions for a device  
**Operation ID:** `getLocalConfigVersions`  
**Tags:** Device Operations  
**Container scope:** device  
**Response codes:** 200, 400, 401, 403, 404, default

### `GET /local-config/download`

**Summary:** Download local configuration file  
**Operation ID:** `downloadLocalConfig`  
**Tags:** Device Operations  
**Container scope:** device  
**Query params:** version  
**Response codes:** 200, 400, 404, 500, default

### `POST /jobs/route-table`

**Summary:** Initiate a job to retrieve route table from device(s)  
**Operation ID:** `requestRouteTable`  
**Tags:** Device Operations  
**Required fields:** `devices`  
**Response codes:** 201, 400, 401, 403, 404, default

### `POST /jobs/dns-proxy`

**Summary:** Initiate a job to retrieve the dns proxy table from device(s)  
**Operation ID:** `requestDnsProxy`  
**Tags:** Device Operations  
**Required fields:** `devices`  
**Response codes:** 201, 400, 401, 403, 404, default

### `POST /jobs/fib-table`

**Summary:** Initiate a job to retrieve FIB table from device(s)  
**Operation ID:** `requestFIBTable`  
**Tags:** Device Operations  
**Required fields:** `devices`  
**Response codes:** 201, 400, 401, 403, 404, default

### `POST /jobs/logging-service-forwarding-status`

**Summary:** Initiate a job to request logging service forwarding status for device(s)  
**Operation ID:** `requestLoggingServiceForwardingStatus`  
**Tags:** Device Operations  
**Required fields:** `devices`  
**Response codes:** 201, 400, 401, 403, 404, default

### `POST /jobs/device-interfaces`

**Summary:** Initiate a job to retrieve network interfaces from device(s)  
**Operation ID:** `requestDeviceInterfaces`  
**Tags:** Device Operations  
**Required fields:** `devices`  
**Response codes:** 201, 400, 401, 403, 404, default

### `POST /jobs/device-rules`

**Summary:** Initiate a job to retrieve rules on one or more device(s)  
**Operation ID:** `requestDeviceRules`  
**Tags:** Device Operations  
**Required fields:** `devices`  
**Response codes:** 201, 400, 401, 403, 404, default

### `POST /jobs/bgp-policy-export`

**Summary:** Initiate a job for BGP Policy Export from device(s)  
**Operation ID:** `bgpPolicyExport`  
**Tags:** Device Operations  
**Required fields:** `devices`  
**Response codes:** 201, 400, 401, 403, 404, default

### `GET /device/jobs/{id}`

**Summary:** Retrieve job status and results, running on a device  
**Operation ID:** `getJobStatus`  
**Tags:** Jobs  
**Response codes:** 200, 401, 403, 404, default
