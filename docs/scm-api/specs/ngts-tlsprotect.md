# TLS Protect Cloud API for Strata Cloud Manager

**Version:** 1.0.0  
**Source:** `openapi-specs/scm/config/ngts/tlsprotect-cloud.json`  
**Base URL:** `https://api.strata.paloaltonetworks.com/ngts`  
**Endpoints:** 147  
**GitHub:** https://github.com/PaloAltoNetworks/pan.dev/blob/master/openapi-specs/scm/config/ngts/tlsprotect-cloud.json

---

## Endpoints

### `GET /outagedetection/v1/certificates`

**Summary:** Retrieve all certificate data  
**Operation ID:** `certificates_getAll`  
**Tags:** Certificates  
**Query params:** ownershipTree, excludeSupersededInstances, subject, limit  
**Response codes:** 200, 400, 412

### `POST /outagedetection/v1/certificates`

**Summary:** Import a set of raw certificates  
**Operation ID:** `certificateimports_create`  
**Tags:** Certificate Import  
**Body schema:** `CertificateImportRequest1`  
**Required fields:** `certificates`  
**Response codes:** 201, 400, 412

### `GET /outagedetection/v1/certificates/{id}`

**Summary:** Get a certificate details  
**Operation ID:** `certificates_getById`  
**Tags:** Certificates  
**Query params:** ownershipTree, excludeSupersededInstances  
**Response codes:** 200, 400, 404, 412

### `GET /outagedetection/v1/certificates/{id}/contents`

**Summary:** Download a certificate  
**Operation ID:** `certificates_getContentsById`  
**Tags:** Certificates  
**Query params:** format, chainOrder  
**Response codes:** 200, 400, 404, 412

### `POST /outagedetection/v1/certificates/validation`

**Summary:** Request validation for a set of  
**Operation ID:** `certificates_validation`  
**Tags:** Certificates  
**Body schema:** `CertificateValidationRequest`  
**Required fields:** `certificateIds`  
**Response codes:** 202, 400, 412

### `POST /outagedetection/v1/certificates/retirement`

**Summary:** Retire certificates  
**Operation ID:** `certificateretirement_retireCertificates`  
**Tags:** Certificates  
**Body schema:** `CertificateRetirementRequest`  
**Required fields:** `certificateIds`  
**Response codes:** 200, 400, 412

### `POST /outagedetection/v1/certificates/recovery`

**Summary:** Recover a set of certificates  
**Operation ID:** `certificateretirement_recoverCertificates`  
**Tags:** Certificates  
**Body schema:** `CertificateRecoveryRequest`  
**Required fields:** `certificateIds`  
**Response codes:** 200, 400, 412

### `POST /outagedetection/v1/certificates/deletion`

**Summary:** Delete a set of retired certificates  
**Operation ID:** `certificateretirement_deleteCertificates`  
**Tags:** Certificates  
**Body schema:** `CertificateDeletionRequest`  
**Required fields:** `certificateIds`  
**Response codes:** 204, 400, 412

### `POST /outagedetection/v1/certificatesearch`

**Summary:** Retrieve certificate data matching search criteria  
**Operation ID:** `certificates_search_getByExpression`  
**Tags:** Certificates  
**Query params:** ownershipTree, excludeSupersededInstances  
**Body schema:** `Filter`  
**Type variants (oneOf/anyOf):** `expression(operands+operator/operand+operator/field+operator)`  
**Response codes:** 200, 400, 412

### `GET /outagedetection/v1/certificateinstances`

**Summary:** Retrieve Certificate Instances  
**Operation ID:** `certificateinstances_getAll`  
**Tags:** TLS Server Endpoints  
**Query params:** source, ipAddress, hostname, limit  
**Response codes:** 200, 400, 412

### `GET /outagedetection/v1/certificateinstances/{id}`

**Summary:** Get a certificate installation details  
**Operation ID:** `certificateinstances_getById`  
**Tags:** TLS Server Endpoints  
**Response codes:** 200, 400, 404, 412

### `POST /outagedetection/v1/certificateinstances/validation`

**Summary:** Request validation for a set of  
**Operation ID:** `certificateinstances_validation`  
**Tags:** TLS Server Endpoints  
**Body schema:** `CertificateInstanceValidationRequest`  
**Required fields:** `instanceIds`  
**Response codes:** 202, 400, 412

### `POST /outagedetection/v1/certificateinstancesearch`

**Summary:** Retrieve certificate instance data matching search  
**Operation ID:** `certificateinstances_search_getByExpression`  
**Tags:** TLS Server Endpoints  
**Body schema:** `Filter`  
**Type variants (oneOf/anyOf):** `expression(operands+operator/operand+operator/field+operator)`  
**Response codes:** 200, 400, 412

### `GET /v1/integrationservices`

**Summary:** Get a list of services  
**Operation ID:** `integrationsservices_getAll`  
**Tags:** Certificate Discovery  
**Query params:** totalCount, edgeInstanceId  
**Response codes:** 200, 400, 412

### `POST /v1/integrationservices`

**Summary:** Add a service  
**Operation ID:** `integrationsservices_create`  
**Tags:** Certificate Discovery  
**Body schema:** `IntegrationServiceCreationRequest`  
**Required fields:** `environmentId`, `name`, `serviceType`, `workTypes`  
**Response codes:** 201, 400

### `GET /v1/integrationservices/{id}`

**Summary:** Get service details  
**Operation ID:** `integrationsservices_getById`  
**Tags:** Certificate Discovery  
**Response codes:** 200, 400, 404, 412

### `DELETE /v1/integrationservices/{id}`

**Summary:** Remove a service  
**Operation ID:** `integrationsservices_delete`  
**Tags:** Certificate Discovery  
**Query params:** retireCertificates  
**Response codes:** 204, 400, 404, 412

### `PATCH /v1/integrationservices/{id}`

**Summary:** Update Service properties  
**Operation ID:** `integrationsservices_update`  
**Tags:** Certificate Discovery  
**Body schema:** `IntegrationServiceUpdateRequest`  
**Response codes:** 200, 400, 404, 412

### `POST /v1/certificates/imports`

**Summary:** Import a list of certificates and  
**Operation ID:** `certificates_import`  
**Tags:** Private Key Import  
**Body schema:** `CertificateImportRequest2`  
**Required fields:** `edgeInstanceId`, `encryptionKeyId`, `importInformation`  
**Response codes:** 201, 400, 412

### `GET /v1/certificates/imports/{id}`

**Summary:** Retrieve import details  
**Operation ID:** `certificatesImport_getByImportId`  
**Tags:** Private Key Import  
**Response codes:** 200, 400, 404, 412

### `GET /outagedetection/v1/certificaterequests`

**Summary:** Get the details of all certificate  
**Operation ID:** `certificaterequests_getAll`  
**Tags:** Certificate Request  
**Response codes:** 200, 400, 412

### `POST /outagedetection/v1/certificaterequests`

**Summary:** Create a certificate request  
**Operation ID:** `certificaterequests_create`  
**Tags:** Certificate Request  
**Body schema:** `CertificateRequestRequest`  
**Required fields:** `applicationId`, `certificateIssuingTemplateId`, `isVaaSGenerated`  
**Response codes:** 201, 400, 412

### `GET /outagedetection/v1/certificaterequests/{id}`

**Summary:** Get a certificate request details  
**Operation ID:** `certificaterequests_getById`  
**Tags:** Certificate Request  
**Response codes:** 200, 400, 404, 412

### `POST /outagedetection/v1/certificaterequests/{id}/resubmission`

**Summary:** Resubmit a certificate request  
**Operation ID:** `certificaterequests_resubmitById`  
**Tags:** Certificate Request  
**Body schema:** `CertificateRequestResubmissionRequest`  
**Response codes:** 200, 400, 404, 412

### `POST /outagedetection/v1/certificaterequests/validation`

**Summary:** Validate a certificate request  
**Operation ID:** `certificaterequests_validation`  
**Tags:** Certificate Request  
**Body schema:** `CertificateRequestRequest`  
**Required fields:** `applicationId`, `certificateIssuingTemplateId`, `isVaaSGenerated`  
**Response codes:** 201, 400, 412

### `POST /outagedetection/v1/certificaterequestssearch`

**Summary:** Get the details of certificate requests  
**Operation ID:** `getCertificateRequestsByExpression`  
**Tags:** Certificate Request  
**Body schema:** `Filter`  
**Type variants (oneOf/anyOf):** `expression(operands+operator/operand+operator/field+operator)`  
**Response codes:** 200, 400, 412

### `GET /v1/certificateissuingtemplates`

**Summary:** Get the details of issuing templates  
**Operation ID:** `certificateissuingtemplate_getAll`  
**Tags:** Certificate Policy  
**Query params:** certificateAuthorityAccountId  
**Response codes:** 200, 400, 412

### `POST /v1/certificateissuingtemplates`

**Summary:** Add an issuing template  
**Operation ID:** `certificateissuingtemplate_create`  
**Tags:** Certificate Policy  
**Body schema:** `CertificateIssuingTemplateRequest`  
**Required fields:** `certificateAuthority`, `certificateAuthorityProductOptionId`, `keyReuse`, `keyTypes`, `name`, `product`  
**Response codes:** 201, 400, 404, 409, 412

### `GET /v1/certificateissuingtemplates/{id}`

**Summary:** Get an issuing template details  
**Operation ID:** `certificateissuingtemplate_getById`  
**Tags:** Certificate Policy  
**Response codes:** 200, 400, 404, 412

### `PUT /v1/certificateissuingtemplates/{id}`

**Summary:** Overwrite an issuing template details  
**Operation ID:** `certificateissuingtemplate_update`  
**Tags:** Certificate Policy  
**Body schema:** `CertificateIssuingTemplateRequest`  
**Required fields:** `certificateAuthority`, `certificateAuthorityProductOptionId`, `keyReuse`, `keyTypes`, `name`, `product`  
**Response codes:** 200, 202, 400, 404, 412

### `DELETE /v1/certificateissuingtemplates/{id}`

**Summary:** Remove an issuing template  
**Operation ID:** `certificateissuingtemplate_delete`  
**Tags:** Certificate Policy  
**Response codes:** 204, 400, 404, 412

### `POST /v1/certificateissuingtemplates/domainssynchronization`

**Summary:** Synchronize issuing templates domains with CA  
**Operation ID:** `domainssynchronization`  
**Tags:** Certificate Policy  
**Body schema:** `IssuingTemplatesDomainsSyncRequest`  
**Required fields:** `action`, `certificateAuthorityAccountId`, `issuingTemplatesIds`  
**Response codes:** 200

### `GET /v1/credentialmanagerconfigurations`

**Summary:** Retrieves a set of Credential Manager  
**Operation ID:** `get-public-cms-conf`  
**Tags:** Credential Management  
**Query params:** cmsTypes  
**Response codes:** 200, 400, 401, 403, 404, 500

### `POST /v1/credentialmanagerconfigurations`

**Summary:** Add a set of Credential Manager  
**Operation ID:** `post-public-cms-conf`  
**Tags:** Credential Management  
**Response codes:** 201, 400, 401, 403, 404, 500

### `PUT /v1/credentialmanagerconfigurations`

**Summary:** Update a Credential Manager Service configuration  
**Operation ID:** `put-public-cms-conf`  
**Tags:** Credential Management  
**Response codes:** 200, 400, 401, 403, 404, 500

### `GET /v1/credentialmanagerconfigurations/{id}`

**Summary:** Retrieves a Credential Manager Service configurati  
**Operation ID:** `get-public-cms-conf-id`  
**Tags:** Credential Management  
**Response codes:** 200, 400, 401, 403, 404, 500

### `DELETE /v1/credentialmanagerconfigurations/{id}`

**Summary:** Delete a Credential Manager Service configuration  
**Operation ID:** `delete-public-cms-conf-id`  
**Tags:** Credential Management  
**Response codes:** 204, 400, 401, 403, 404, 500

### `POST /v1/credentialmanagerconfigurations/test`

**Summary:** Test the connection to a privileged  
**Operation ID:** `post-public-cms-conf-test`  
**Tags:** Credential Management  
**Response codes:** 200, 400, 401, 403, 404, 500

### `POST /v1/credentialmanagerconfigurations/{id}/test`

**Summary:** Test the connection to an external  
**Operation ID:** `post-public-cms-conf-test-id`  
**Tags:** Credential Management  
**Response codes:** 200, 400, 401, 403, 404, 500

### `GET /v1/credentials`

**Summary:** Retrieves credentials for a company  
**Operation ID:** `get-public-cms-credential`  
**Tags:** Credential Management  
**Query params:** details, cmsTypes, ids, teamIds, authTypes  
**Response codes:** 200, 400, 401, 403, 422, 500

### `POST /v1/credentials`

**Summary:** Add a set of new shared  
**Operation ID:** `post-public-cms-credential`  
**Tags:** Credential Management  
**Response codes:** 201, 400, 401, 403, 422, 500

### `PUT /v1/credentials`

**Summary:** Update a shared credential  
**Operation ID:** `put-public-cms-credential`  
**Tags:** Credential Management  
**Response codes:** 200, 400, 401, 403, 422, 500

### `DELETE /v1/credentials`

**Summary:** Delete shared credentials  
**Operation ID:** `delete-public-cms-credential`  
**Tags:** Credential Management  
**Query params:** ids  
**Response codes:** 200, 400, 401, 403, 422, 500

### `GET /v1/credentials/{id}`

**Summary:** Retrieves shared credential by ID  
**Operation ID:** `get-public-cms-credential-id`  
**Tags:** Credential Management  
**Query params:** details  
**Response codes:** 200, 400, 401, 403, 422, 500

### `DELETE /v1/credentials/{id}`

**Summary:** Delete shared credential by ID  
**Operation ID:** `delete-public-cms-credential-id`  
**Tags:** Credential Management  
**Response codes:** 204, 400, 401, 403, 422, 500

### `POST /v1/credentials/test`

**Summary:** Test the access to shared credential  
**Operation ID:** `post-public-cms-credential-test-id`  
**Tags:** Credential Management  
**Response codes:** 200, 400, 401, 403, 404, 500

### `GET /v1/machineidentities`

**Summary:** Get the details of all machine  
**Operation ID:** `machineidentities_getAll`  
**Tags:** Machine Installations  
**Response codes:** 200, 400, 412

### `POST /v1/machineidentities`

**Summary:** Add a machine identity to a  
**Operation ID:** `machineidentities_create`  
**Tags:** Machine Installations  
**Body schema:** `MachineIdentityCreationRequest`  
**Required fields:** `certificateId`, `machineId`  
**Response codes:** 201, 400

### `GET /v1/machineidentities/{id}`

**Summary:** Get a machine identity details  
**Operation ID:** `machineidentities_getById`  
**Tags:** Machine Installations  
**Response codes:** 200, 400, 404, 412

### `DELETE /v1/machineidentities/{id}`

**Summary:** Remove a machine identity  
**Operation ID:** `machineidentities_delete`  
**Tags:** Machine Installations  
**Response codes:** 204, 400, 404, 412

### `PATCH /v1/machineidentities/{id}`

**Summary:** Update a machine identity details  
**Operation ID:** `machineidentities_update`  
**Tags:** Machine Installations  
**Body schema:** `MachineIdentityUpdateRequest`  
**Response codes:** 200, 400, 404, 412

### `POST /v1/machineidentities/{id}/workflows`

**Summary:** Initiate a machine workflow  
**Operation ID:** `machineidentities_initiateWorkflow`  
**Tags:** Machine Installations  
**Body schema:** `MachineIdentityWorkflowRequest`  
**Required fields:** `workflowName`  
**Response codes:** 201, 400, 404, 412

### `POST /v1/machineidentitysearch`

**Summary:** Get the details of machine identities  
**Operation ID:** `getMachineIdentitiesByExpression`  
**Tags:** Machine Installations  
**Body schema:** `MachineIdentitySearchRequest`  
**Response codes:** 200, 400, 412

### `GET /v1/machinetypes`

**Summary:** List Machine Types  
**Operation ID:** `machineTypes_getAll`  
**Tags:** Machine Types  
**Response codes:** default

### `GET /v1/machines`

**Summary:** Get the details of all machines  
**Operation ID:** `machines_getAll`  
**Tags:** Machines  
**Response codes:** 200, 400, 412

### `POST /v1/machines`

**Summary:** Add a machine  
**Operation ID:** `machines_create`  
**Tags:** Machines  
**Body schema:** `MachineCreationRequest`  
**Required fields:** `connectionDetails`, `name`, `pluginId`  
**Response codes:** 201, 400

### `GET /v1/machines/{id}`

**Summary:** Get a machine details  
**Operation ID:** `machines_getById`  
**Tags:** Machines  
**Response codes:** 200, 400, 404, 412

### `DELETE /v1/machines/{id}`

**Summary:** Delete a machine  
**Operation ID:** `machines_delete`  
**Tags:** Machines  
**Response codes:** 204, 400, 404, 412

### `PATCH /v1/machines/{id}`

**Summary:** Update a machine details  
**Operation ID:** `machines_update`  
**Tags:** Machines  
**Body schema:** `MachineUpdateRequest`  
**Response codes:** 200, 400, 404, 412

### `POST /v1/machines/{id}/workflows`

**Summary:** Initiate the workflow  
**Operation ID:** `machines_initiateWorkflow`  
**Tags:** Machines  
**Body schema:** `MachineWorkflowRequest`  
**Response codes:** 201, 400

### `POST /v1/machinesearch`

**Summary:** Get the details of machines matching  
**Operation ID:** `getMachinesByExpression`  
**Tags:** Machines  
**Query params:** ownershipTree  
**Body schema:** `MachinesSearchRequest`  
**Response codes:** 200, 400, 412

### `POST /v1/machines/{id}/batchprovisionings/abort`

**Summary:** Abort active batch provisioning for a  
**Operation ID:** `abort-v1-batchprovisionings-forMachineId`  
**Tags:** Machines  
**Response codes:** 202, 403, 404, 405, 500

### `GET /v1/machines/{id}/discovery`

**Summary:** Get the discovery results for a  
**Operation ID:** `machineDiscoveryResults_getByMachineId`  
**Tags:** Machines  
**Response codes:** 200, 400, 404, 412

### `POST /v1/machines/{id}/discovery/abort`

**Summary:** Abort machine discovery  
**Operation ID:** `machineDiscoveryResults_abortdiscovery`  
**Tags:** Machines  
**Response codes:** 202, 403, 404, 405

### `POST /v1/activitylogsearch`

**Summary:** Retrieve count and activity log entries  
**Operation ID:** `activitylogs_getByExpression`  
**Tags:** Event Logs  
**Body schema:** `ActivityLogFilter`  
**Type variants (oneOf/anyOf):** `expression(operands+operator/operand+operator/field+operator)`  
**Response codes:** 200, 400, 412

### `POST /v1/activitylogsearch/export`

**Summary:** Export filtered event log data to  
**Operation ID:** `activitylogs_getAllByExpression`  
**Tags:** Event Logs  
**Body schema:** `ActivityLogFilter`  
**Type variants (oneOf/anyOf):** `expression(operands+operator/operand+operator/field+operator)`  
**Response codes:** 200, 400, 412

### `GET /v1/activitytypes`

**Summary:** Retrieve types of activities used for  
**Operation ID:** `activitylogtypes_get`  
**Tags:** Event Logs  
**Response codes:** 200, 400, 412

### `POST /v1/edgeinstances/{id}/update`

**Summary:** Trigger manual update of Satellite Instance  
**Operation ID:** `create-edgeinstances-update`  
**Tags:** VSatellite  
**Response codes:** 202, 400, 404, 412

### `GET /v1/edgeencryptionkeys`

**Summary:** Retrieve Satellite Encryption Keys  
**Operation ID:** `edgeencryptionkeys_getAll`  
**Tags:** VSatellite  
**Query params:** edgeInstanceId  
**Response codes:** 200

### `GET /v1/edgeencryptionkeys/{id}`

**Summary:** Retrieve SatelliteEncryption Key By Id  
**Operation ID:** `edgeencryptionkeys_getById`  
**Tags:** VSatellite  
**Response codes:** 200, 400, 404, 412

### `GET /v1/edgeinstances`

**Summary:** Retrieve Satellite Instances  
**Operation ID:** `edgeinstances_getAll`  
**Tags:** VSatellite  
**Query params:** environmentId  
**Response codes:** 200

### `GET /v1/edgeinstances/{id}`

**Summary:** Retrieve Satellite Instance By Id  
**Operation ID:** `edgeinstances_getById`  
**Tags:** VSatellite  
**Query params:** statusDetails  
**Response codes:** 200, 400, 404, 412

### `PUT /v1/edgeinstances/{id}`

**Summary:** Update Satellite Instance  
**Operation ID:** `edgeinstances_update`  
**Tags:** VSatellite  
**Body schema:** `EdgeInstanceRequest`  
**Required fields:** `name`  
**Response codes:** 200, 400, 404, 412

### `POST /v1/pairingcodes/satellite`

**Summary:** Create Pairing Code for Satellite Instance  
**Operation ID:** `pairingcodes_create`  
**Tags:** VSatellite  
**Body schema:** `PairingCodeRequest`  
**Response codes:** 201, 400

### `POST /v1/recoverycodes/satellite`

**Summary:** Create Recovery Code for Satellite Instance  
**Operation ID:** `recoverycodes_create`  
**Tags:** VSatellite  
**Body schema:** `RecoveryCodeRequest`  
**Required fields:** `edgeInstanceId`  
**Response codes:** 201, 400

### `GET /v1/edgeworkers`

**Summary:** Retrieve Satellite Workers  
**Operation ID:** `edgeworkers_getAll`  
**Tags:** VSatellite  
**Query params:** edgeInstanceId  
**Response codes:** 200

### `POST /v1/edgeworkers`

**Summary:** Create Satellite Worker  
**Operation ID:** `edgeworkers_create`  
**Tags:** VSatellite  
**Body schema:** `EdgeWorkerRequest`  
**Response codes:** 201, 400, 412

### `POST /v1/edgeworkers/{id}/pair`

**Summary:** Pair Satellite Worker with Satellite Instance  
**Operation ID:** `edgeworkers_pair`  
**Tags:** VSatellite  
**Body schema:** `EdgeWorkerRequest`  
**Response codes:** 200, 400, 412

### `DELETE /v1/edgeworkers/{id}`

**Summary:** Delete Satellite Worker  
**Operation ID:** `edgeworker_delete`  
**Tags:** VSatellite  
**Response codes:** 204, 400, 404, 412

### `GET /v1/updatesconfig`

**Summary:** Retrieve Updates configuration  
**Operation ID:** `updatesconfig_get`  
**Tags:** VSatellite  
**Response codes:** 200

### `PATCH /v1/updatesconfig`

**Summary:** Create or Update Configuration  
**Operation ID:** `updatesconfig_patch`  
**Tags:** VSatellite  
**Body schema:** `UpdatesConfigRequest`  
**Required fields:** `updateConfigSchedulerPattern`  
**Type variants (oneOf/anyOf):** `updateConfigSchedulerPattern(duration+startTime/daysOfWeek+duration)`  
**Response codes:** 200

### `GET /outagedetection/v1/inventorymonitoringconfig/{type}`

**Summary:** Get the details of the current  
**Operation ID:** `inventorymonitoringconfiguration_getByType`  
**Tags:** Certificate Inventory Monitoring  
**Response codes:** 200, 400, 404, 412

### `PUT /outagedetection/v1/inventorymonitoringconfig/{type}`

**Summary:** Updates existing inventory monitoring configuratio  
**Operation ID:** `inventorymonitoringconfiguration_update`  
**Tags:** Certificate Inventory Monitoring  
**Body schema:** `InventoryMonitoringConfigRequest`  
**Response codes:** 200, 400, 412

### `PUT /outagedetection/v1/inventorymonitoringconfig/{type}/scheduler`

**Summary:** Update inventory monitoring scheduler by type  
**Operation ID:** `inventorymonitoringconfigurationscheduler_update`  
**Tags:** Certificate Inventory Monitoring  
**Query params:** runNow  
**Response codes:** 200, 400, 412

### `GET /v1/expirationnotifications/tenantconfiguration`

**Summary:** Retrieve the certificate expiration notification c  
**Operation ID:** `get-v1-tenant-expiration-notification-configuration`  
**Tags:** Certificate Inventory Monitoring  
**Response codes:** 200, 400, 401, 500

### `PUT /v1/expirationnotifications/tenantconfiguration`

**Summary:** Update the certificate expiration notification con  
**Operation ID:** `put-v1-tenant-expiration-notification-configuration`  
**Tags:** Certificate Inventory Monitoring  
**Body schema:** `TenantExpirationNotificationConfiguration`  
**Response codes:** 200, 400, 401, 500

### `GET /v1/autorenewal/tenantconfiguration`

**Summary:** Retrieve the monitoring configuration  
**Operation ID:** `get-v1-tenant-renewal-configuration`  
**Tags:** Certificate Auto-renewal Monitoring  
**Response codes:** 200, 400, 401, 500

### `PUT /v1/autorenewal/tenantconfiguration`

**Summary:** Update the monitoring configuration  
**Operation ID:** `put-v1-tenant-renewal-configuration`  
**Tags:** Certificate Auto-renewal Monitoring  
**Body schema:** `TenantRenewalConfiguration`  
**Required fields:** `id`, `renewalWindow`  
**Response codes:** 200, 400, 401, 500

### `POST /v1/autorenewal/trigger`

**Summary:** Attempt to initiate the certificate renewal  
**Operation ID:** `post-v1-run-autorenewal`  
**Tags:** Certificate Auto-renewal Monitoring  
**Response codes:** 200

### `GET /v1/autorenewal/status`

**Summary:** Get the current certificate auto-renewal monitorin  
**Operation ID:** `get-v1-status`  
**Tags:** Certificate Auto-renewal Monitoring  
**Response codes:** 200, 401, 500

### `GET /v1/tags`

**Summary:** Retrieve all tags  
**Operation ID:** `tags_getAll`  
**Tags:** Certificate Tags  
**Response codes:** 200, 400, 412

### `POST /v1/tags`

**Summary:** Create a tag  
**Operation ID:** `tags_create`  
**Tags:** Certificate Tags  
**Body schema:** `TagRequest`  
**Required fields:** `name`  
**Response codes:** 201, 400, 412

### `GET /v1/tags/{name}`

**Summary:** Retrieve tag by name  
**Operation ID:** `tags_getByName`  
**Tags:** Certificate Tags  
**Response codes:** 200, 400, 404, 412

### `DELETE /v1/tags/{name}`

**Summary:** Delete tag by name  
**Operation ID:** `tags_deleteByName`  
**Tags:** Certificate Tags  
**Response codes:** 202, 404, 412

### `GET /v1/tags/{name}/values`

**Summary:** Retrieve values for a tag  
**Operation ID:** `tags_get_values`  
**Tags:** Certificate Tags  
**Response codes:** 200, 400, 404, 412

### `POST /v1/tags/{name}/values`

**Summary:** Create tag values  
**Operation ID:** `tag_values_create`  
**Tags:** Certificate Tags  
**Body schema:** `TagValuesRequest`  
**Required fields:** `values`  
**Response codes:** 201, 400, 412

### `DELETE /v1/tags/{name}/values/{value}`

**Summary:** Delete a tag value  
**Operation ID:** `tags_deleteValueByName`  
**Tags:** Certificate Tags  
**Response codes:** 202, 404, 412

### `GET /v1/tags/values`

**Summary:** Retrieve values for all tags  
**Operation ID:** `tags_getAllValues`  
**Tags:** Certificate Tags  
**Response codes:** 200, 400, 412

### `POST /v1/tags/creation`

**Summary:** Create tags in bulk  
**Operation ID:** `tags_bulk_create`  
**Tags:** Certificate Tags  
**Body schema:** `TagsBulkRequest`  
**Response codes:** 201, 400, 412

### `POST /v1/tags/deletion`

**Summary:** Delete tags in bulk  
**Operation ID:** `tags_bulk_delete`  
**Tags:** Certificate Tags  
**Body schema:** `TagsBulkRequest`  
**Response codes:** 202, 404, 412

### `PATCH /v1/tagsassignment`

**Summary:** Replace Add Or Delete Tags  
**Operation ID:** `tags_assignToEntities`  
**Tags:** Certificate Tags  
**Body schema:** `TagsAssignRequest`  
**Required fields:** `entityIds`  
**Response codes:** 200, 400, 412

### `POST /v1/tagsassignment/aggregates`

**Summary:** Bulk operation to retrieve number of  
**Operation ID:** `tags_assignmentAggregates`  
**Tags:** Certificate Tags  
**Body schema:** `TagsAssignmentAggregatesRequest`  
**Required fields:** `tags`  
**Response codes:** 200, 400, 412

### `POST /v1/distributedissuers/configurations`

**Summary:** Create a new Issuer configuration  
**Operation ID:** `configurations_create`  
**Tags:** Issuer Configurations  
**Body schema:** `ConfigurationCreateRequest`  
**Required fields:** `name`, `policyIds`, `subCaProviderId`  
**Type variants (oneOf/anyOf):** `clientAuthentication(audience+clients/urls/audience+baseUrl)`  
**Response codes:** 201, 400, 412

### `GET /v1/distributedissuers/configurations`

**Summary:** Get the details of all Issuer  
**Operation ID:** `configurations_getAll`  
**Tags:** Issuer Configurations  
**Response codes:** 200, 400, 412

### `GET /v1/distributedissuers/configurations/{id}`

**Summary:** Get configurations details for a specific  
**Operation ID:** `configurations_getById`  
**Tags:** Issuer Configurations  
**Response codes:** 200, 400, 404, 412

### `PATCH /v1/distributedissuers/configurations/{id}`

**Summary:** Update an Issuer configuration details  
**Operation ID:** `configurations_update`  
**Tags:** Issuer Configurations  
**Body schema:** `ConfigurationUpdateRequest`  
**Response codes:** 200, 400, 404, 412

### `DELETE /v1/distributedissuers/configurations/{id}`

**Summary:** Remove an Issuer configuration  
**Operation ID:** `configurations_delete`  
**Tags:** Issuer Configurations  
**Response codes:** 200, 400, 404, 412

### `POST /v1/distributedissuers/subcaproviders`

**Summary:** Create a new Sub CA provider  
**Operation ID:** `subcaproviders_create`  
**Tags:** Issuer Sub CA Providers  
**Body schema:** `SubCaProviderCreateRequest`  
**Required fields:** `caAccountId`, `caProductOptionId`, `caType`, `commonName`, `keyAlgorithm`, `name`, `validityPeriod`  
**Response codes:** 201, 400, 412

### `GET /v1/distributedissuers/subcaproviders`

**Summary:** Get the details of all Sub  
**Operation ID:** `subcaprovider_getAll`  
**Tags:** Issuer Sub CA Providers  
**Response codes:** 200, 400, 412

### `GET /v1/distributedissuers/subcaproviders/{id}`

**Summary:** Get a Sub CA provider details  
**Operation ID:** `subcaproviders_getById`  
**Tags:** Issuer Sub CA Providers  
**Response codes:** 200, 400, 404, 412

### `PATCH /v1/distributedissuers/subcaproviders/{id}`

**Summary:** Update a Sub CA provider details  
**Operation ID:** `subcaproviders_update`  
**Tags:** Issuer Sub CA Providers  
**Body schema:** `SubCaProviderUpdateRequest`  
**Response codes:** 200, 400, 404, 412

### `DELETE /v1/distributedissuers/subcaproviders/{id}`

**Summary:** Remove a Sub CA provider  
**Operation ID:** `subcaproviders_delete`  
**Tags:** Issuer Sub CA Providers  
**Response codes:** 200, 400, 404, 412

### `POST /v1/distributedissuers/policies`

**Summary:** Create a new Workload Issuance policy  
**Operation ID:** `policies_create`  
**Tags:** Workload Issuance Policies  
**Body schema:** `PolicyCreateRequest`  
**Required fields:** `extendedKeyUsages`, `keyAlgorithm`, `keyUsages`, `name`, `sans`, `subject`, `validityPeriod`  
**Response codes:** 201, 400, 412

### `GET /v1/distributedissuers/policies`

**Summary:** Get the details of all Workload  
**Operation ID:** `policies_getAll`  
**Tags:** Workload Issuance Policies  
**Response codes:** 200, 400, 412

### `GET /v1/distributedissuers/policies/{id}`

**Summary:** Get a Workload Issuance policy details  
**Operation ID:** `policies_getById`  
**Tags:** Workload Issuance Policies  
**Response codes:** 200, 400, 404, 412

### `PATCH /v1/distributedissuers/policies/{id}`

**Summary:** Update a Workload Issuance policy details  
**Operation ID:** `policies_update`  
**Tags:** Workload Issuance Policies  
**Body schema:** `PolicyUpdateRequest`  
**Response codes:** 200, 400, 404, 412

### `DELETE /v1/distributedissuers/policies/{id}`

**Summary:** Remove a Workload Issuance policy  
**Operation ID:** `policies_delete`  
**Tags:** Workload Issuance Policies  
**Response codes:** 200, 400, 404, 412

### `GET /v1/distributedissuers/intermediatecertificates`

**Summary:** Get the details of all Issuer  
**Operation ID:** `intermediatecertificates_getAll`  
**Tags:** Issuer Certificates  
**Response codes:** 200, 400, 412

### `POST /v1/certificaterequests/{id}/approval/{decision}`

**Summary:** Approve or reject pending certificate request  
**Operation ID:** `certificaterequests_approve`  
**Tags:** Certificate Approvals  
**Body schema:** `ApprovalDecisionRequest`  
**Response codes:** 200, 400, 404, 412

### `POST /v1/certificaterequests/approval/bulk/{decision}`

**Summary:** Approve or reject multiple pending approval  
**Operation ID:** `certificaterequests_bulk_approve`  
**Tags:** Certificate Approvals  
**Body schema:** `BulkApprovalRequest`  
**Required fields:** `ids`  
**Response codes:** 201, 400, 412

### `POST /v1/certificaterequests/approvalrules`

**Summary:** Create an approval rule for certificate  
**Operation ID:** `certificaterequests_approval_rule_create`  
**Tags:** Certificate Approvals  
**Body schema:** `CertificateRequestApprovalRulesRequest`  
**Required fields:** `approvers`, `conditions`, `name`, `type`  
**Response codes:** 201, 400, 412

### `GET /v1/certificaterequests/approvalrules`

**Summary:** Get all approval rules  
**Operation ID:** `certificaterequests_approval_rules_getAll`  
**Tags:** Certificate Approvals  
**Response codes:** 200, 400, 412

### `GET /v1/certificaterequests/approvalrules/{id}`

**Summary:** Retrieve approval rule by id  
**Operation ID:** `certificaterequests_approval_rule_getById`  
**Tags:** Certificate Approvals  
**Response codes:** 200, 400, 404, 412

### `PUT /v1/certificaterequests/approvalrules/{id}`

**Summary:** Update certificate request workflow approval rule  
**Operation ID:** `certificaterequests_approval_rule_update`  
**Tags:** Certificate Approvals  
**Body schema:** `CertificateRequestApprovalRulesUpdateRequest`  
**Required fields:** `approvers`, `conditions`, `name`, `type`  
**Response codes:** 200, 400, 404, 412

### `DELETE /v1/certificaterequests/approvalrules/{id}`

**Summary:** Delete certificate request workflow approval rule  
**Operation ID:** `certificaterequests_approval_rule_delete`  
**Tags:** Certificate Approvals  
**Response codes:** 200, 400, 404, 412

### `GET /v1/certificaterequests/approvalrequests/{entityId}`

**Summary:** Retrieve approval request for specific certificate  
**Operation ID:** `certificaterequests_approvalrequest`  
**Tags:** Certificate Approvals  
**Response codes:** 200, 400, 404, 412

### `POST /v1/certificates/revocations/approvalrules`

**Summary:** Create an approval rule for certificate  
**Operation ID:** `certificaterevocations_approval_rule_create`  
**Tags:** Certificate Revocation Approvals  
**Body schema:** `CertificateRevocationApprovalRulesRequest`  
**Required fields:** `approvers`, `conditions`, `name`, `type`  
**Response codes:** 201, 400, 412

### `GET /v1/certificates/revocations/approvalrules`

**Summary:** Get all certificate revocation approval rules  
**Operation ID:** `certificaterevocations_approval_rules_getAll`  
**Tags:** Certificate Revocation Approvals  
**Response codes:** 200, 400, 412

### `GET /v1/certificates/revocations/approvalrules/{id}`

**Summary:** Retrieve certificate revocation approval rule by  
**Operation ID:** `certificaterevocations_approval_rule_getById`  
**Tags:** Certificate Revocation Approvals  
**Response codes:** 200, 400, 404, 412

### `PUT /v1/certificates/revocations/approvalrules/{id}`

**Summary:** Update certificate revocation workflow approval ru  
**Operation ID:** `certificaterevocations_approval_rule_update`  
**Tags:** Certificate Revocation Approvals  
**Body schema:** `CertificateRevocationApprovalRulesUpdateRequest`  
**Required fields:** `approvers`, `conditions`, `name`, `type`  
**Response codes:** 200, 400, 404, 412

### `DELETE /v1/certificates/revocations/approvalrules/{id}`

**Summary:** Delete certificate revocation workflow approval ru  
**Operation ID:** `certificaterevocations_approval_rule_delete`  
**Tags:** Certificate Revocation Approvals  
**Response codes:** 200, 400, 404, 412

### `GET /v1/plugins`

**Summary:** Retrieve all plugins  
**Operation ID:** `get-v1-plugins`  
**Tags:** Plugins (Connectors)  
**Query params:** pluginTypes, includeDisabled  
**Response codes:** 200

### `POST /v1/plugins`

**Summary:** Create a local plugin  
**Operation ID:** `post-v1-plugins`  
**Tags:** Plugins (Connectors)  
**Body schema:** `PublicPluginCreationRequest`  
**Required fields:** `manifest`, `pluginType`  
**Response codes:** 201

### `GET /v1/plugins/{id}`

**Summary:** Retrieve plugin by ID  
**Operation ID:** `get-v1-plugins-id`  
**Tags:** Plugins (Connectors)  
**Response codes:** 200

### `PATCH /v1/plugins/{id}`

**Summary:** Update a local plugin  
**Operation ID:** `patch-v1-plugins-id`  
**Tags:** Plugins (Connectors)  
**Body schema:** `PublicPluginUpdateRequest`  
**Response codes:** 200, 401, 403

### `DELETE /v1/plugins/{id}`

**Summary:** Delete a local plugin  
**Operation ID:** `delete-v1-plugins-id`  
**Tags:** Plugins (Connectors)  
**Response codes:** 204

### `POST /v1/plugins/{id}/disablements`

**Summary:** Disable a plugin  
**Operation ID:** `post-v1-plugins-id-exclusions`  
**Tags:** Plugins (Connectors)  
**Response codes:** 201

### `DELETE /v1/plugins/{id}/disablements`

**Summary:** Remove plugin disablement  
**Operation ID:** `delete-v1-plugins-id-exclusions`  
**Tags:** Plugins (Connectors)  
**Response codes:** 204

### `GET /v1/plugins/disablements`

**Summary:** Retrieve all disabled plugins  
**Operation ID:** `get-v1-plugins-exclusions`  
**Tags:** Plugins (Connectors)  
**Response codes:** 200

### `GET /v1/serviceaccounts`

**Summary:** Retrieves all the Service Accounts the  
**Operation ID:** `get-v1-serviceaccounts`  
**Tags:** Built-In Accounts  
**Response codes:** 200, 400, 401, 500

### `POST /v1/serviceaccounts`

**Summary:** Creates a Service Account  
**Operation ID:** `create-v1-serviceaccounts`  
**Tags:** Built-In Accounts  
**Body schema:** `CreateServiceAccountRequestBody`  
**Response codes:** 200, 400, 401, 500

### `GET /v1/serviceaccounts/{id}`

**Summary:** Gets a Service Account  
**Operation ID:** `get-v1-serviceaccounts-byId`  
**Tags:** Built-In Accounts  
**Response codes:** 200, 400, 401, 500

### `PATCH /v1/serviceaccounts/{id}`

**Summary:** Updates a Service Account  
**Operation ID:** `patch-v1-serviceaccounts-byId`  
**Tags:** Built-In Accounts  
**Body schema:** `PatchServiceAccountByClientIDRequestBody`  
**Response codes:** 204, 400, 401, 500

### `DELETE /v1/serviceaccounts/{id}`

**Summary:** Deletes a Service Account  
**Operation ID:** `delete-v1-serviceaccounts-byId`  
**Tags:** Built-In Accounts  
**Response codes:** 204, 400, 401, 500

### `GET /v1/serviceaccounts/scopes`

**Summary:** Retrieves all the Service Accounts Scopes  
**Operation ID:** `get-v1-serviceaccountscopes`  
**Tags:** Built-In Accounts  
**Response codes:** 200, 400, 401, 500

### `PUT /v1/serviceaccounts/{id}/ocitoken`

**Summary:** Regenerate the OCI registry token for  
**Operation ID:** `put-v1-serviceaccounts-byId-ocitoken`  
**Tags:** Built-In Accounts  
**Response codes:** 200, 400, 401, 500

### `PUT /v1/serviceaccounts/{id}/credentials`

**Summary:** Updates a Service Account credentials  
**Operation ID:** `put-v1-serviceaccounts-byId-credentials`  
**Tags:** Built-In Accounts  
**Body schema:** `PutServiceAccountByClientIDCredentialsRequestBody`  
**Required fields:** `extendCredentialLifetime`  
**Response codes:** 200, 400, 401, 500
