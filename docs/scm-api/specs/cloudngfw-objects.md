# Objects

**Version:** 2.0.0  
**Source:** `openapi-specs/scm/config/cloudngfw/objects/objects-june.yaml`  
**Base URL:** `https://api.strata.paloaltonetworks.com/config/objects/v1`  
**Endpoints:** 105  
**GitHub:** https://github.com/PaloAltoNetworks/pan.dev/blob/master/openapi-specs/scm/config/cloudngfw/objects/objects-june.yaml

---

## Endpoints

### `GET /addresses`

**Summary:** List addresses  
**Operation ID:** `ListAddresses`  
**Tags:** Addresses  
**Container scope:** folder | snippet | device  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /addresses`

**Summary:** Create an address  
**Operation ID:** `CreateAddresses`  
**Tags:** Addresses  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `addresses`  
**Required fields:** `id`, `name`  
**Type variants (oneOf/anyOf):** `ip_netmask` | `ip_range` | `ip_wildcard` | `fqdn`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /addresses/{id}`

**Summary:** Get an address  
**Operation ID:** `GetAddressesByID`  
**Tags:** Addresses  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /addresses/{id}`

**Summary:** Update an address  
**Operation ID:** `UpdateAddressesByID`  
**Tags:** Addresses  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `addresses`  
**Required fields:** `id`, `name`  
**Type variants (oneOf/anyOf):** `ip_netmask` | `ip_range` | `ip_wildcard` | `fqdn`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /addresses/{id}`

**Summary:** Delete an address  
**Operation ID:** `DeleteAddressesByID`  
**Tags:** Addresses  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /advanced-device-objects`

**Summary:** List advanced device objects  
**Operation ID:** `ListAdvancedDeviceObjects`  
**Tags:** Advanced Device Objects  
**Container scope:** folder | snippet | device  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /advanced-device-objects`

**Summary:** Create an advanced device object  
**Operation ID:** `CreateAdvancedDeviceObjects`  
**Tags:** Advanced Device Objects  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `advanced-device-objects`  
**Required fields:** `id`, `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `PUT /advanced-device-objects`

**Summary:** Update an advanced device object by path  
**Operation ID:** `UpdateAdvancedDeviceObjectsByPath`  
**Tags:** Advanced Device Objects  
**Container scope:** folder | snippet | device  
**Query params:** name  
**Body schema:** `advanced-device-objects`  
**Required fields:** `id`, `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /advanced-device-objects`

**Summary:** Delete advanced device objects by names  
**Operation ID:** `DeleteAdvancedDeviceObjectsByNames`  
**Tags:** Advanced Device Objects  
**Container scope:** folder | snippet | device  
**Query params:** name  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /advanced-device-objects/{id}`

**Summary:** Get an advanced device object  
**Operation ID:** `GetAdvancedDeviceObjectsByID`  
**Tags:** Advanced Device Objects  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /advanced-device-objects/{id}`

**Summary:** Update an advanced device object  
**Operation ID:** `UpdateAdvancedDeviceObjectsByID`  
**Tags:** Advanced Device Objects  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `advanced-device-objects`  
**Required fields:** `id`, `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /advanced-device-objects/{id}`

**Summary:** Delete an advanced device object  
**Operation ID:** `DeleteAdvancedDeviceObjectsByID`  
**Tags:** Advanced Device Objects  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /address-groups`

**Summary:** List address groups  
**Operation ID:** `ListAddressGroups`  
**Tags:** Address Groups  
**Container scope:** folder | snippet | device  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /address-groups`

**Summary:** Create an address group  
**Operation ID:** `CreateAddressGroups`  
**Tags:** Address Groups  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `address-groups`  
**Required fields:** `id`, `name`  
**Type variants (oneOf/anyOf):** `static` | `dynamic`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /address-groups/{id}`

**Summary:** Get an address group  
**Operation ID:** `GetAddressGroupsByID`  
**Tags:** Address Groups  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /address-groups/{id}`

**Summary:** Update an address group  
**Operation ID:** `UpdateAddressGroupsByID`  
**Tags:** Address Groups  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `address-groups`  
**Required fields:** `id`, `name`  
**Type variants (oneOf/anyOf):** `static` | `dynamic`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /address-groups/{id}`

**Summary:** Delete an address group  
**Operation ID:** `DeleteAddressGroupsByID`  
**Tags:** Address Groups  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /applications`

**Summary:** List applications  
**Operation ID:** `ListApplications`  
**Tags:** Applications  
**Container scope:** folder | snippet | device  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /applications`

**Summary:** Create an application  
**Operation ID:** `CreateApplications`  
**Tags:** Applications  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `applications`  
**Required fields:** `name`, `category`, `risk`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /applications/{id}`

**Summary:** Get the application by id  
**Operation ID:** `GetApplicationsByID`  
**Tags:** Applications  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /applications/{id}`

**Summary:** Update an application  
**Operation ID:** `UpdateApplicationsByID`  
**Tags:** Applications  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `applications`  
**Required fields:** `name`, `category`, `risk`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /applications/{id}`

**Summary:** Delete an application  
**Operation ID:** `DeleteApplicationsByID`  
**Tags:** Applications  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /application-filters`

**Summary:** List application filters  
**Operation ID:** `ListApplicationFilters`  
**Tags:** Application Filters  
**Container scope:** folder | snippet | device  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /application-filters`

**Summary:** Create an application filter  
**Operation ID:** `CreateApplicationFilters`  
**Tags:** Application Filters  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `application-filters`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /application-filters/{id}`

**Summary:** Get an application filter  
**Operation ID:** `GetApplicationFiltersByID`  
**Tags:** Application Filters  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /application-filters/{id}`

**Summary:** Update an application filter  
**Operation ID:** `UpdateApplicationFiltersByID`  
**Tags:** Application Filters  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `application-filters`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /application-filters/{id}`

**Summary:** Delete an application filter  
**Operation ID:** `DeleteApplicationFiltersByID`  
**Tags:** Application Filters  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /application-groups`

**Summary:** List application groups  
**Operation ID:** `ListApplicationGroups`  
**Tags:** Application Groups  
**Container scope:** folder | snippet | device  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /application-groups`

**Summary:** Create an application group  
**Operation ID:** `CreateApplicationGroups`  
**Tags:** Application Groups  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `application-groups`  
**Required fields:** `id`, `name`, `members`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /application-groups/{id}`

**Summary:** Get an application group  
**Operation ID:** `GetApplicationGroupsByID`  
**Tags:** Application Groups  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /application-groups/{id}`

**Summary:** Update an application group  
**Operation ID:** `UpdateApplicationGroupsByID`  
**Tags:** Application Groups  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `application-groups`  
**Required fields:** `id`, `name`, `members`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /application-groups/{id}`

**Summary:** Delete an application group  
**Operation ID:** `DeleteApplicationGroupsByID`  
**Tags:** Application Groups  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /auto-tag-actions`

**Summary:** List auto-tag actions  
**Operation ID:** `ListAuto-TagActions`  
**Tags:** Auto-Tag Actions  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /auto-tag-actions`

**Summary:** Create an auto-tag action  
**Operation ID:** `CreateAuto-TagActions`  
**Tags:** Auto-Tag Actions  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `auto-tag-actions`  
**Required fields:** `name`, `log_type`, `filter`  
**Response codes:** 201, 400, 401, 403, 409, default

### `PUT /auto-tag-actions`

**Summary:** Update an auto-tag action  
**Operation ID:** `UpdateAuto-TagActions`  
**Tags:** Auto-Tag Actions  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `auto-tag-actions`  
**Required fields:** `name`, `log_type`, `filter`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /auto-tag-actions`

**Summary:** Delete an Auto-Tag action  
**Operation ID:** `DeleteAuto-TagActions`  
**Tags:** Auto-Tag Actions  
**Query params:** name  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /device-context-segments`

**Summary:** List device context segments  
**Operation ID:** `ListDeviceContextSegments`  
**Tags:** Device Context Segments  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /device-context-segments`

**Summary:** Create a device context segment  
**Operation ID:** `CreateDeviceContextSegment`  
**Tags:** Device Context Segments  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `device-context-segments`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `DELETE /device-context-segments`

**Summary:** Delete device context segments by name  
**Operation ID:** `DeleteDeviceContextSegmentsByName`  
**Tags:** Device Context Segments  
**Query params:** name  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /device-context-segments/{id}`

**Summary:** Get a device context segment  
**Operation ID:** `GetDeviceContextSegmentByID`  
**Tags:** Device Context Segments  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /device-context-segments/{id}`

**Summary:** Update a device context segment  
**Operation ID:** `UpdateDeviceContextSegmentByID`  
**Tags:** Device Context Segments  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `device-context-segments`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /device-context-segments/{id}`

**Summary:** Delete a device context segment  
**Operation ID:** `DeleteDeviceContextSegmentByID`  
**Tags:** Device Context Segments  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /dynamic-user-groups`

**Summary:** List Dynamic User Groups  
**Operation ID:** `ListDynamicUserGroups`  
**Tags:** Dynamic User Groups  
**Container scope:** folder | snippet | device  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /dynamic-user-groups`

**Summary:** Create a Dynamic User Group  
**Operation ID:** `CreateDynamicUserGroups`  
**Tags:** Dynamic User Groups  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `dynamic-user-groups`  
**Required fields:** `id`, `name`, `filter`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /dynamic-user-groups/{id}`

**Summary:** Get a Dynamic User Group  
**Operation ID:** `GetDynamicUserGroupsByID`  
**Tags:** Dynamic User Groups  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /dynamic-user-groups/{id}`

**Summary:** Update a Dynamic User Group  
**Operation ID:** `UpdateDynamicUserGroupsByID`  
**Tags:** Dynamic User Groups  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `dynamic-user-groups`  
**Required fields:** `id`, `name`, `filter`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /dynamic-user-groups/{id}`

**Summary:** Delete a Dynamic User Group  
**Operation ID:** `DeleteDynamicUserGroupsByID`  
**Tags:** Dynamic User Groups  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /external-dynamic-lists`

**Summary:** List External Dynamic Lists  
**Operation ID:** `ListExternalDynamicLists`  
**Tags:** External Dynamic Lists  
**Container scope:** folder | snippet | device  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /external-dynamic-lists`

**Summary:** Create an External Dynamic List  
**Operation ID:** `CreateExternalDynamicLists`  
**Tags:** External Dynamic Lists  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `external-dynamic-lists`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /external-dynamic-lists/{id}`

**Summary:** Get an External Dynamic List  
**Operation ID:** `GetExternalDynamicListsByID`  
**Tags:** External Dynamic Lists  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /external-dynamic-lists/{id}`

**Summary:** Update an External Dynamic List  
**Operation ID:** `UpdateExternalDynamicListsByID`  
**Tags:** External Dynamic Lists  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `external-dynamic-lists`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /external-dynamic-lists/{id}`

**Summary:** Delete an External Dynamic List  
**Operation ID:** `DeleteExternalDynamicListsByID`  
**Tags:** External Dynamic Lists  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /hip-objects`

**Summary:** List HIP objects  
**Operation ID:** `ListHIPObjects`  
**Tags:** HIP Objects  
**Container scope:** folder | snippet | device  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /hip-objects`

**Summary:** Create a HIP object  
**Operation ID:** `CreateHIPObjects`  
**Tags:** HIP Objects  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `hip-objects`  
**Required fields:** `id`, `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /hip-objects/{id}`

**Summary:** Get a HIP object  
**Operation ID:** `GetHIPObjectsByID`  
**Tags:** HIP Objects  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /hip-objects/{id}`

**Summary:** Update a HIP object  
**Operation ID:** `UpdateHIPObjectsByID`  
**Tags:** HIP Objects  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `hip-objects`  
**Required fields:** `id`, `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /hip-objects/{id}`

**Summary:** Delete a HIP object  
**Operation ID:** `DeleteHIPObjectsByID`  
**Tags:** HIP Objects  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /hip-profiles`

**Summary:** List HIP profiles  
**Operation ID:** `ListHIPProfiles`  
**Tags:** HIP Profiles  
**Container scope:** folder | snippet | device  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /hip-profiles`

**Summary:** Create a HIP profile  
**Operation ID:** `CreateHIPProfiles`  
**Tags:** HIP Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `hip-profiles`  
**Required fields:** `id`, `name`, `match`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /hip-profiles/{id}`

**Summary:** Get a HIP profile  
**Operation ID:** `GetHIPProfilesByID`  
**Tags:** HIP Profiles  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /hip-profiles/{id}`

**Summary:** Update a HIP profile  
**Operation ID:** `UpdateHIPProfilesByID`  
**Tags:** HIP Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `hip-profiles`  
**Required fields:** `id`, `name`, `match`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /hip-profiles/{id}`

**Summary:** Delete a HIP profile  
**Operation ID:** `DeleteHIPProfilesByID`  
**Tags:** HIP Profiles  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /http-server-profiles`

**Summary:** List HTTP server profiles  
**Operation ID:** `ListHTTPServerProfiles`  
**Tags:** HTTP Server Profiles  
**Container scope:** folder | snippet | device  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /http-server-profiles`

**Summary:** Create a HTTP server profile  
**Operation ID:** `CreateHTTPServerProfiles`  
**Tags:** HTTP Server Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `http-server-profiles`  
**Required fields:** `id`, `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /http-server-profiles/{id}`

**Summary:** Get a HTTP server profile  
**Operation ID:** `GetHTTPServerProfilesByID`  
**Tags:** HTTP Server Profiles  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /http-server-profiles/{id}`

**Summary:** Update a HTTP server profile  
**Operation ID:** `UpdateHTTPServerProfilesByID`  
**Tags:** HTTP Server Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `http-server-profiles`  
**Required fields:** `id`, `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /http-server-profiles/{id}`

**Summary:** Delete a HTTP server profile  
**Operation ID:** `DeleteHTTPServerProfilesByID`  
**Tags:** HTTP Server Profiles  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /log-forwarding-profiles`

**Summary:** List log forwarding profiles  
**Operation ID:** `ListLogForwardingProfiles`  
**Tags:** Log Forwarding Profiles  
**Container scope:** folder | snippet | device  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /log-forwarding-profiles`

**Summary:** Create a log forwarding profile  
**Operation ID:** `CreateLogForwardingProfiles`  
**Tags:** Log Forwarding Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `log-forwarding-profiles`  
**Required fields:** `name`, `match_list`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /log-forwarding-profiles/{id}`

**Summary:** Get a log forwarding profile  
**Operation ID:** `GetLogForwardingProfilesByID`  
**Tags:** Log Forwarding Profiles  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /log-forwarding-profiles/{id}`

**Summary:** Update a log forwarding profile  
**Operation ID:** `UpdateLogForwardingProfilesByID`  
**Tags:** Log Forwarding Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `log-forwarding-profiles`  
**Required fields:** `name`, `match_list`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /log-forwarding-profiles/{id}`

**Summary:** Delete a log forwarding profile  
**Operation ID:** `DeleteLogForwardingProfilesByID`  
**Tags:** Log Forwarding Profiles  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /quarantined-devices`

**Summary:** List quarantined devices  
**Operation ID:** `ListQuarantinedDevices`  
**Tags:** Quarantined Devices  
**Query params:** host_id, serial_number  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /quarantined-devices`

**Summary:** Create a quarantined device  
**Operation ID:** `CreateQuarantinedDevices`  
**Tags:** Quarantined Devices  
**Body schema:** `quarantined-devices`  
**Required fields:** `host_id`  
**Response codes:** 201, 400, 401, 403, 409, default

### `DELETE /quarantined-devices`

**Summary:** Delete a quarantined device  
**Operation ID:** `DeleteQuarantinedDevices`  
**Tags:** Quarantined Devices  
**Query params:** host_id  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /regions`

**Summary:** List regions  
**Operation ID:** `ListRegions`  
**Tags:** Regions  
**Container scope:** folder | snippet | device  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /regions`

**Summary:** Create a region  
**Operation ID:** `CreateRegions`  
**Tags:** Regions  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `regions`  
**Required fields:** `id`, `name`  
**Response codes:** 201, 400, 401, 403, 404, 409, default

### `GET /regions/{id}`

**Summary:** Get a region  
**Operation ID:** `GetRegionsByID`  
**Tags:** Regions  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /regions/{id}`

**Summary:** Update a region  
**Operation ID:** `UpdateRegionsByID`  
**Tags:** Regions  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `regions`  
**Required fields:** `id`, `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /regions/{id}`

**Summary:** Delete a region  
**Operation ID:** `DeleteRegionsByID`  
**Tags:** Regions  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /schedules`

**Summary:** List schedules  
**Operation ID:** `ListSchedules`  
**Tags:** Schedules  
**Container scope:** folder | snippet | device  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /schedules`

**Summary:** Create a schedule  
**Operation ID:** `CreateSchedules`  
**Tags:** Schedules  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `schedules`  
**Required fields:** `id`, `name`, `schedule_type`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /schedules/{id}`

**Summary:** Get a schedule  
**Operation ID:** `GetSchedulesByID`  
**Tags:** Schedules  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /schedules/{id}`

**Summary:** Update a schedule  
**Operation ID:** `UpdateSchedulesByID`  
**Tags:** Schedules  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `schedules`  
**Required fields:** `id`, `name`, `schedule_type`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /schedules/{id}`

**Summary:** Delete a schedule  
**Operation ID:** `DeleteSchedulesByID`  
**Tags:** Schedules  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /services`

**Summary:** List services  
**Operation ID:** `ListServices`  
**Tags:** Services  
**Container scope:** folder | snippet | device  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /services`

**Summary:** Create a service  
**Operation ID:** `CreateServices`  
**Tags:** Services  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `services`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /services/{id}`

**Summary:** Get a service  
**Operation ID:** `GetServicesByID`  
**Tags:** Services  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /services/{id}`

**Summary:** Update a service  
**Operation ID:** `UpdateServicesByID`  
**Tags:** Services  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `services`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /services/{id}`

**Summary:** Delete a service  
**Operation ID:** `DeleteServicesByID`  
**Tags:** Services  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /service-groups`

**Summary:** List service groups  
**Operation ID:** `ListServiceGroups`  
**Tags:** Service Groups  
**Container scope:** folder | snippet | device  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /service-groups`

**Summary:** Create a service group  
**Operation ID:** `CreateServiceGroups`  
**Tags:** Service Groups  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `service-groups`  
**Required fields:** `id`, `name`, `members`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /service-groups/{id}`

**Summary:** Get the service group by id  
**Operation ID:** `GetServiceGroupsByID`  
**Tags:** Service Groups  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /service-groups/{id}`

**Summary:** Update a service group  
**Operation ID:** `UpdateServiceGroupsByID`  
**Tags:** Service Groups  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `service-groups`  
**Required fields:** `id`, `name`, `members`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /service-groups/{id}`

**Summary:** Delete a service group  
**Operation ID:** `DeleteServiceGroupsByID`  
**Tags:** Service Groups  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /syslog-server-profiles`

**Summary:** List syslog server profiles  
**Operation ID:** `ListSyslogServerProfiles`  
**Tags:** Syslog Server Profiles  
**Container scope:** folder | snippet | device  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /syslog-server-profiles`

**Summary:** Create a syslog server profile  
**Operation ID:** `CreateSyslogServerProfiles`  
**Tags:** Syslog Server Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `syslog-server-profiles`  
**Required fields:** `id`, `name`, `server`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /syslog-server-profiles/{id}`

**Summary:** Get a syslog server profile  
**Operation ID:** `GetSyslogServerProfilesByID`  
**Tags:** Syslog Server Profiles  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /syslog-server-profiles/{id}`

**Summary:** Update a syslog server profile  
**Operation ID:** `UpdateSyslogServerProfilesByID`  
**Tags:** Syslog Server Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `syslog-server-profiles`  
**Required fields:** `id`, `name`, `server`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /syslog-server-profiles/{id}`

**Summary:** Delete a syslog server profile  
**Operation ID:** `DeleteSyslogServerProfilesByID`  
**Tags:** Syslog Server Profiles  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /tags`

**Summary:** List tags  
**Operation ID:** `ListTags`  
**Tags:** Tags  
**Container scope:** folder | snippet | device  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /tags`

**Summary:** Create a tag  
**Operation ID:** `CreateTags`  
**Tags:** Tags  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `tags`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /tags/{id}`

**Summary:** Get a tag  
**Operation ID:** `GetTagsByID`  
**Tags:** Tags  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /tags/{id}`

**Summary:** Update a tag  
**Operation ID:** `UpdateTagsByID`  
**Tags:** Tags  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `tags`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /tags/{id}`

**Summary:** Delete a tag  
**Operation ID:** `DeleteTagsByID`  
**Tags:** Tags  
**Response codes:** 200, 400, 401, 403, 404, 409, default
