# Compliance Center API

**Version:** 1.0.0  
**Source:** `openapi-specs/scm/config/posture-management/compliance-framework/compliance-center-recent-v1.yaml`  
**Base URL:** `https://api.strata.paloaltonetworks.com/posture/compliance-frameworks/v1`  
**Endpoints:** 15  
**GitHub:** https://github.com/PaloAltoNetworks/pan.dev/blob/master/openapi-specs/scm/config/posture-management/compliance-framework/compliance-center-recent-v1.yaml

---

## Endpoints

### `GET /definitions`

**Summary:** List Compliance Frameworks  
**Operation ID:** `getAllFrameworks`  
**Tags:** Compliance Frameworks  
**Query params:** category, status  
**Response codes:** 200, 400, 403, 500

### `POST /definitions`

**Summary:** Create Compliance Framework  
**Operation ID:** `createFramework`  
**Tags:** Compliance Frameworks  
**Body schema:** `ComplianceFrameworkRequest`  
**Response codes:** 201, 400, 403, 500

### `GET /definitions/{id}`

**Summary:** Get Framework Revision  
**Operation ID:** `getLatestRevision`  
**Tags:** Compliance Frameworks  
**Query params:** op  
**Response codes:** 200, 400, 403, 404, 500

### `PUT /definitions/{id}`

**Summary:** Update Compliance Framework  
**Operation ID:** `updateFramework`  
**Tags:** Compliance Frameworks  
**Query params:** release  
**Body schema:** `ComplianceFrameworkRequest`  
**Response codes:** 200, 400, 403, 404, 500

### `DELETE /definitions/{id}`

**Summary:** Delete Compliance Framework  
**Operation ID:** `deleteFramework`  
**Tags:** Compliance Frameworks  
**Response codes:** 204, 400, 403, 404, 500

### `POST /definitions/{id}:clone`

**Summary:** Clone Compliance Framework  
**Operation ID:** `cloneFramework`  
**Tags:** Compliance Frameworks  
**Response codes:** 201, 400, 403, 404, 500

### `POST /definitions/{id}:benchmark`

**Summary:** Benchmark Compliance Framework  
**Operation ID:** `benchmarkFramework`  
**Tags:** Compliance Frameworks  
**Response codes:** 200, 400, 403, 404, 500

### `POST /definitions/{id}:un-benchmark`

**Summary:** Remove Framework Benchmark  
**Operation ID:** `unBenchmarkFramework`  
**Tags:** Compliance Frameworks  
**Response codes:** 200, 400, 403, 404, 500

### `GET /summaries`

**Summary:** List Framework Summaries  
**Operation ID:** `getCFSummary`  
**Tags:** Compliance Analytics  
**Query params:** product  
**Response codes:** 200, 400, 403, 404, 500

### `GET /overall-compliance/{id}`

**Summary:** Get Framework Compliance Scores  
**Operation ID:** `getOverallCompliance`  
**Tags:** Compliance Analytics  
**Response codes:** 200, 400, 403, 404, 500

### `GET /overall-compliance-timeline/{id}`

**Summary:** Get Compliance Timeline  
**Operation ID:** `getConfigurationsAssessedTimeline`  
**Tags:** Compliance Analytics  
**Query params:** product  
**Response codes:** 200, 400, 403, 404, 500

### `GET /configurations-assessed/{id}`

**Summary:** Get Assessed Configurations  
**Operation ID:** `getConfigurationsAssessed`  
**Tags:** Compliance Analytics  
**Query params:** product  
**Response codes:** 200, 400, 403, 404, 500

### `GET /compliance-controls/{id}`

**Summary:** Get Compliance Controls  
**Operation ID:** `getComplianceControls`  
**Tags:** Compliance Analytics  
**Query params:** product  
**Response codes:** 200, 400, 403, 404, 500

### `POST /benchmark-monitoring`

**Summary:** Get Benchmark Monitoring Data  
**Operation ID:** `getBenchmarkMonitoring`  
**Tags:** Benchmark Monitoring  
**Response codes:** 200, 400, 403, 404, 500

### `POST /benchmark-monitoring/download`

**Summary:** Download Benchmark Data  
**Operation ID:** `getBenchmarkMonitoringDownload`  
**Tags:** Benchmark Monitoring  
**Query params:** offset, limit, format, compression  
**Response codes:** 200, 400, 403, 404, 500
