# Device Settings

**Version:** 2.0.0  
**Source:** `openapi-specs/scm/config/ngfw/device/device-settings_April.yaml`  
**Base URL:** `https://api.strata.paloaltonetworks.com/config/device/v1`  
**Endpoints:** 71  
**GitHub:** https://github.com/PaloAltoNetworks/pan.dev/blob/master/openapi-specs/scm/config/ngfw/device/device-settings_April.yaml

---

## Endpoints

### `GET /authentication-settings`

**Summary:** List authentication settings  
**Operation ID:** `ListAuthenticationSettings`  
**Tags:** Authentication Settings  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /authentication-settings`

**Summary:** Create authentication settings  
**Operation ID:** `CreateAuthenticationSettings`  
**Tags:** Authentication Settings  
**Response codes:** 201, 400, 401, 403, 404, 409, default

### `GET /authentication-settings/{id}`

**Summary:** Get existing authentication settings  
**Operation ID:** `GetAuthenticationSettingsByID`  
**Tags:** Authentication Settings  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /authentication-settings/{id}`

**Summary:** Update authentication settings  
**Operation ID:** `UpdateAuthenticationSettingsByID`  
**Tags:** Authentication Settings  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /authentication-settings/{id}`

**Summary:** Delete authentication settings  
**Operation ID:** `DeleteAuthenticationSettingsByID`  
**Tags:** Authentication Settings  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /content-id-settings`

**Summary:** List Content-ID settings  
**Operation ID:** `ListContentIDSettings`  
**Tags:** Content-ID Settings  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /content-id-settings`

**Summary:** Create Content-ID settings  
**Operation ID:** `CreateContentIDSettings`  
**Tags:** Content-ID Settings  
**Response codes:** 201, 400, 401, 403, 404, 409, default

### `GET /content-id-settings/{id}`

**Summary:** Get existing Content-ID settings  
**Operation ID:** `GetContentIDSettingsByID`  
**Tags:** Content-ID Settings  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /content-id-settings/{id}`

**Summary:** Update Content-ID settings  
**Operation ID:** `UpdateContentIDSettingsByID`  
**Tags:** Content-ID Settings  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /content-id-settings/{id}`

**Summary:** Delete Content-ID settings  
**Operation ID:** `DeleteContentIDSettingsByID`  
**Tags:** Content-ID Settings  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /device-redistribution-collector`

**Summary:** List device redistribution collector settings  
**Operation ID:** `ListDeviceRedistributionCollectorSettings`  
**Tags:** Device Redistribution Collector Settings  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /device-redistribution-collector`

**Summary:** Create device redistribution collector settings  
**Operation ID:** `CreateDeviceRedistributionCollectorSettings`  
**Tags:** Device Redistribution Collector Settings  
**Response codes:** 201, 400, 401, 403, 404, 409, default

### `GET /device-redistribution-collector/{id}`

**Summary:** Get existing device redistribution collector settings  
**Operation ID:** `GetDeviceRedistributionCollectorSettingsByID`  
**Tags:** Device Redistribution Collector Settings  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /device-redistribution-collector/{id}`

**Summary:** Update device redistribution collector settings  
**Operation ID:** `UpdateDeviceRedistributionCollectorSettingsByID`  
**Tags:** Device Redistribution Collector Settings  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /device-redistribution-collector/{id}`

**Summary:** Delete device redistribution collector settings  
**Operation ID:** `DeleteDeviceRedistributionCollectorSettingsByID`  
**Tags:** Device Redistribution Collector Settings  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /general-settings`

**Summary:** List general settings  
**Operation ID:** `ListGeneralSettings`  
**Tags:** General Settings  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /general-settings`

**Summary:** Create general settings  
**Operation ID:** `CreateGeneralSettings`  
**Tags:** General Settings  
**Response codes:** 201, 400, 401, 403, 404, 409, default

### `GET /general-settings/{id}`

**Summary:** Get existing general settings  
**Operation ID:** `GetGeneralSettingsByID`  
**Tags:** General Settings  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /general-settings/{id}`

**Summary:** Update general settings  
**Operation ID:** `UpdateGeneralSettingsByID`  
**Tags:** General Settings  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /general-settings/{id}`

**Summary:** Delete general settings  
**Operation ID:** `DeleteGeneralSettingsByID`  
**Tags:** General Settings  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /ha-configurations`

**Summary:** List high availability configurations  
**Operation ID:** `ListHAConfigurations`  
**Tags:** High Availability Configurations  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /ha-configurations`

**Summary:** Create high availability configurations  
**Operation ID:** `CreateHAConfigurations`  
**Tags:** High Availability Configurations  
**Response codes:** 201, 400, 401, 403, 404, 409, default

### `GET /ha-configurations/{id}`

**Summary:** Get existing high availability configurations  
**Operation ID:** `GetHAConfigurationsByID`  
**Tags:** High Availability Configurations  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /ha-configurations/{id}`

**Summary:** Update high availability configurations  
**Operation ID:** `UpdateHAConfigurationsByID`  
**Tags:** High Availability Configurations  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /ha-configurations/{id}`

**Summary:** Delete high availability configurations  
**Operation ID:** `DeleteHAConfigurationsByID`  
**Tags:** High Availability Configurations  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /ha-devices`

**Summary:** List high availability devices  
**Operation ID:** `ListHADevices`  
**Tags:** High Availability Devices  
**Response codes:** 200, 400, 401, 403, 404, default

### `GET /management-interface`

**Summary:** List management interface settings  
**Operation ID:** `ListManagementInterfaceSettings`  
**Tags:** Management Interface Settings  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /management-interface`

**Summary:** Create management interface settings  
**Operation ID:** `CreateManagementInterfaceSettings`  
**Tags:** Management Interface Settings  
**Response codes:** 201, 400, 401, 403, 404, 409, default

### `GET /management-interface/{id}`

**Summary:** Get existing management interface settings  
**Operation ID:** `GetManagementInterfaceSettingsByID`  
**Tags:** Management Interface Settings  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /management-interface/{id}`

**Summary:** Update management interface settings  
**Operation ID:** `UpdateManagementInterfaceSettingsByID`  
**Tags:** Management Interface Settings  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /management-interface/{id}`

**Summary:** Delete management interface settings  
**Operation ID:** `DeleteManagementInterfaceSettingsByID`  
**Tags:** Management Interface Settings  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /motd-banner-settings`

**Summary:** List login banner settings  
**Operation ID:** `ListLoginBannerSettings`  
**Tags:** Login Banner Settings  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /motd-banner-settings`

**Summary:** Create login banner settings  
**Operation ID:** `CreateLoginBannerSettings`  
**Tags:** Login Banner Settings  
**Response codes:** 201, 400, 401, 403, 404, 409, default

### `GET /motd-banner-settings/{id}`

**Summary:** Get existing login banner settings  
**Operation ID:** `GetLoginBannerSettingsByID`  
**Tags:** Login Banner Settings  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /motd-banner-settings/{id}`

**Summary:** Update login banner settings  
**Operation ID:** `UpdateLoginBannerSettingsByID`  
**Tags:** Login Banner Settings  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /motd-banner-settings/{id}`

**Summary:** Delete login banner settings  
**Operation ID:** `DeleteLoginBannerSettingsByID`  
**Tags:** Login Banner Settings  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /service-route`

**Summary:** List service route settings  
**Operation ID:** `ListServiceRouteSettings`  
**Tags:** Service Route Settings  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /service-route`

**Summary:** Create service route settings  
**Operation ID:** `CreateServiceRouteSettings`  
**Tags:** Service Route Settings  
**Response codes:** 201, 400, 401, 403, 404, 409, default

### `GET /service-route/{id}`

**Summary:** Get existing service route settings  
**Operation ID:** `GetServiceRouteSettingsByID`  
**Tags:** Service Route Settings  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /service-route/{id}`

**Summary:** Update service route settings  
**Operation ID:** `UpdateServiceRouteSettingsByID`  
**Tags:** Service Route Settings  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /service-route/{id}`

**Summary:** Delete service route settings  
**Operation ID:** `DeleteServiceRouteSettingsByID`  
**Tags:** Service Route Settings  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /service-settings`

**Summary:** List service settings  
**Operation ID:** `ListServiceSettings`  
**Tags:** Service Settings  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /service-settings`

**Summary:** Create service settings  
**Operation ID:** `CreateServiceSettings`  
**Tags:** Service Settings  
**Response codes:** 201, 400, 401, 403, 404, 409, default

### `GET /service-settings/{id}`

**Summary:** Get existing service settings  
**Operation ID:** `GetServiceSettingsByID`  
**Tags:** Service Settings  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /service-settings/{id}`

**Summary:** Update service settings  
**Operation ID:** `UpdateServiceSettingsByID`  
**Tags:** Service Settings  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /service-settings/{id}`

**Summary:** Delete service settings  
**Operation ID:** `DeleteServiceSettingsByID`  
**Tags:** Service Settings  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /session-settings`

**Summary:** List session settings  
**Operation ID:** `ListSessionSettings`  
**Tags:** Session Settings  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /session-settings`

**Summary:** Create session settings  
**Operation ID:** `CreateSessionSettings`  
**Tags:** Session Settings  
**Response codes:** 201, 400, 401, 403, 404, 409, default

### `GET /session-settings/{id}`

**Summary:** Get existing session settings  
**Operation ID:** `GetSessionSettingsByID`  
**Tags:** Session Settings  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /session-settings/{id}`

**Summary:** Update session settings  
**Operation ID:** `UpdateSessionSettingsByID`  
**Tags:** Session Settings  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /session-settings/{id}`

**Summary:** Delete session settings  
**Operation ID:** `DeleteSessionSettingsByID`  
**Tags:** Session Settings  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /session-timeouts`

**Summary:** List session timeouts settings  
**Operation ID:** `ListSessionTimeoutsSettings`  
**Tags:** Session Timeouts Settings  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /session-timeouts`

**Summary:** Create session timeouts settings  
**Operation ID:** `CreateSessionTimeoutsSettings`  
**Tags:** Session Timeouts Settings  
**Response codes:** 201, 400, 401, 403, 404, 409, default

### `GET /session-timeouts/{id}`

**Summary:** Get existing session settings  
**Operation ID:** `GetSessionTimeoutsSettingsByID`  
**Tags:** Session Timeouts Settings  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /session-timeouts/{id}`

**Summary:** Update session settings  
**Operation ID:** `UpdateSessionTimeoutsSettingsByID`  
**Tags:** Session Timeouts Settings  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /session-timeouts/{id}`

**Summary:** Delete session settings  
**Operation ID:** `DeleteSessionTimeoutsSettingsByID`  
**Tags:** Session Timeouts Settings  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /tcp-settings`

**Summary:** List TCP settings  
**Operation ID:** `ListTCPSettings`  
**Tags:** TCP Settings  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /tcp-settings`

**Summary:** Create TCP settings  
**Operation ID:** `CreateTCPSettings`  
**Tags:** TCP Settings  
**Response codes:** 201, 400, 401, 403, 404, 409, default

### `GET /tcp-settings/{id}`

**Summary:** Get existing TCP settings  
**Operation ID:** `GetTCPSettingsByID`  
**Tags:** TCP Settings  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /tcp-settings/{id}`

**Summary:** Update TCP settings  
**Operation ID:** `UpdateTCPSettingsByID`  
**Tags:** TCP Settings  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /tcp-settings/{id}`

**Summary:** Delete TCP settings  
**Operation ID:** `DeleteTCPSettingsByID`  
**Tags:** TCP Settings  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /update-schedule`

**Summary:** List update schedule settings  
**Operation ID:** `ListUpdateScheduleSettings`  
**Tags:** Update Schedule Settings  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /update-schedule`

**Summary:** Create update schedule settings  
**Operation ID:** `CreateUpdateScheduleSettings`  
**Tags:** Update Schedule Settings  
**Response codes:** 201, 400, 401, 403, 404, 409, default

### `GET /update-schedule/{id}`

**Summary:** Get existing update schedule settings  
**Operation ID:** `GetUpdateScheduleSettingsByID`  
**Tags:** Update Schedule Settings  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /update-schedule/{id}`

**Summary:** Update update schedule settings  
**Operation ID:** `UpdateUpdateScheduleSettingsByID`  
**Tags:** Update Schedule Settings  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /update-schedule/{id}`

**Summary:** Delete update schedule settings  
**Operation ID:** `DeleteUpdateScheduleSettingsByID`  
**Tags:** Update Schedule Settings  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /vpn-settings`

**Summary:** List VPN settings  
**Operation ID:** `ListVPNSettings`  
**Tags:** VPN Settings  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /vpn-settings`

**Summary:** Create VPN settings  
**Operation ID:** `CreateVPNSettings`  
**Tags:** VPN Settings  
**Response codes:** 201, 400, 401, 403, 404, 409, default

### `GET /vpn-settings/{id}`

**Summary:** Get existing VPN settings  
**Operation ID:** `GetVPNSettingsByID`  
**Tags:** VPN Settings  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /vpn-settings/{id}`

**Summary:** Update VPN settings  
**Operation ID:** `UpdateVPNSettingsByID`  
**Tags:** VPN Settings  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /vpn-settings/{id}`

**Summary:** Delete VPN settings  
**Operation ID:** `DeleteVPNSettingsByID`  
**Tags:** VPN Settings  
**Response codes:** 200, 400, 401, 403, 404, 409, default
