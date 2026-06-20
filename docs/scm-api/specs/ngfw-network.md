# Network Services

**Version:** 2.0.0  
**Source:** `openapi-specs/scm/config/ngfw/network/network-services-R2-2026.yaml`  
**Base URL:** `https://api.strata.paloaltonetworks.com/config/network/v1`  
**Endpoints:** 246  
**GitHub:** https://github.com/PaloAltoNetworks/pan.dev/blob/master/openapi-specs/scm/config/ngfw/network/network-services-R2-2026.yaml

---

## Endpoints

### `GET /config-match-list`

**Summary:** List config match list entries  
**Operation ID:** `ListConfigMatchList`  
**Tags:** Config Match List  
**Container scope:** folder | snippet | device  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /config-match-list`

**Summary:** Create a config match list entry  
**Operation ID:** `CreateConfigMatchList`  
**Tags:** Config Match List  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `config-match-list`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /config-match-list/{id}`

**Summary:** Get a config match list entry  
**Operation ID:** `GetConfigMatchListByID`  
**Tags:** Config Match List  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /config-match-list/{id}`

**Summary:** Update a config match list entry  
**Operation ID:** `UpdateConfigMatchListByID`  
**Tags:** Config Match List  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `config-match-list`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /config-match-list/{id}`

**Summary:** Delete a config match list entry  
**Operation ID:** `DeleteConfigMatchListByID`  
**Tags:** Config Match List  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /globalprotect-match-list`

**Summary:** List globalprotect match list entries  
**Operation ID:** `ListGlobalprotectMatchList`  
**Tags:** Globalprotect Match List  
**Container scope:** folder | snippet | device  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /globalprotect-match-list`

**Summary:** Create a globalprotect match list entry  
**Operation ID:** `CreateGlobalprotectMatchList`  
**Tags:** Globalprotect Match List  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `globalprotect-match-list`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /globalprotect-match-list/{id}`

**Summary:** Get a globalprotect match list entry  
**Operation ID:** `GetGlobalprotectMatchListByID`  
**Tags:** Globalprotect Match List  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /globalprotect-match-list/{id}`

**Summary:** Update a globalprotect match list entry  
**Operation ID:** `UpdateGlobalprotectMatchListByID`  
**Tags:** Globalprotect Match List  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `globalprotect-match-list`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /globalprotect-match-list/{id}`

**Summary:** Delete a globalprotect match list entry  
**Operation ID:** `DeleteGlobalprotectMatchListByID`  
**Tags:** Globalprotect Match List  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /hipmatch-match-list`

**Summary:** List hipmatch match list entries  
**Operation ID:** `ListHipmatchMatchList`  
**Tags:** Hipmatch Match List  
**Container scope:** folder | snippet | device  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /hipmatch-match-list`

**Summary:** Create a hipmatch match list entry  
**Operation ID:** `CreateHipmatchMatchList`  
**Tags:** Hipmatch Match List  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `hipmatch-match-list`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /hipmatch-match-list/{id}`

**Summary:** Get a hipmatch match list entry  
**Operation ID:** `GetHipmatchMatchListByID`  
**Tags:** Hipmatch Match List  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /hipmatch-match-list/{id}`

**Summary:** Update a hipmatch match list entry  
**Operation ID:** `UpdateHipmatchMatchListByID`  
**Tags:** Hipmatch Match List  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `hipmatch-match-list`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /hipmatch-match-list/{id}`

**Summary:** Delete a hipmatch match list entry  
**Operation ID:** `DeleteHipmatchMatchListByID`  
**Tags:** Hipmatch Match List  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /iptag-match-list`

**Summary:** List iptag match list entries  
**Operation ID:** `ListIptagMatchList`  
**Tags:** Iptag Match List  
**Container scope:** folder | snippet | device  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /iptag-match-list`

**Summary:** Create an iptag match list entry  
**Operation ID:** `CreateIptagMatchList`  
**Tags:** Iptag Match List  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `iptag-match-list`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /iptag-match-list/{id}`

**Summary:** Get an iptag match list entry  
**Operation ID:** `GetIptagMatchListByID`  
**Tags:** Iptag Match List  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /iptag-match-list/{id}`

**Summary:** Update an iptag match list entry  
**Operation ID:** `UpdateIptagMatchListByID`  
**Tags:** Iptag Match List  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `iptag-match-list`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /iptag-match-list/{id}`

**Summary:** Delete an iptag match list entry  
**Operation ID:** `DeleteIptagMatchListByID`  
**Tags:** Iptag Match List  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /system-match-list`

**Summary:** List system match list entries  
**Operation ID:** `ListSystemMatchList`  
**Tags:** System Match List  
**Container scope:** folder | snippet | device  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /system-match-list`

**Summary:** Create a system match list entry  
**Operation ID:** `CreateSystemMatchList`  
**Tags:** System Match List  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `system-match-list`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /system-match-list/{id}`

**Summary:** Get a system match list entry  
**Operation ID:** `GetSystemMatchListByID`  
**Tags:** System Match List  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /system-match-list/{id}`

**Summary:** Update a system match list entry  
**Operation ID:** `UpdateSystemMatchListByID`  
**Tags:** System Match List  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `system-match-list`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /system-match-list/{id}`

**Summary:** Delete a system match list entry  
**Operation ID:** `DeleteSystemMatchListByID`  
**Tags:** System Match List  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /userid-match-list`

**Summary:** List userid match list entries  
**Operation ID:** `ListUseridMatchList`  
**Tags:** Userid Match List  
**Container scope:** folder | snippet | device  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /userid-match-list`

**Summary:** Create a userid match list entry  
**Operation ID:** `CreateUseridMatchList`  
**Tags:** Userid Match List  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `userid-match-list`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /userid-match-list/{id}`

**Summary:** Get a userid match list entry  
**Operation ID:** `GetUseridMatchListByID`  
**Tags:** Userid Match List  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /userid-match-list/{id}`

**Summary:** Update a userid match list entry  
**Operation ID:** `UpdateUseridMatchListByID`  
**Tags:** Userid Match List  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `userid-match-list`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /userid-match-list/{id}`

**Summary:** Delete a userid match list entry  
**Operation ID:** `DeleteUseridMatchListByID`  
**Tags:** Userid Match List  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /ike-crypto-profiles`

**Summary:** List IKE crypto profiles  
**Operation ID:** `ListIKECryptoProfiles`  
**Tags:** IKE Crypto Profiles  
**Container scope:** folder | snippet | device  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /ike-crypto-profiles`

**Summary:** Create an IKE crypto profile  
**Operation ID:** `CreateIKECryptoProfiles`  
**Tags:** IKE Crypto Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `ike-crypto-profiles`  
**Required fields:** `name`, `hash`, `encryption`, `dh_group`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /ike-crypto-profiles/{id}`

**Summary:** Get an IKE crypto profile  
**Operation ID:** `GetIKECryptoProfilesByID`  
**Tags:** IKE Crypto Profiles  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /ike-crypto-profiles/{id}`

**Summary:** Update an IKE crypto profile  
**Operation ID:** `UpdateIKECryptoProfilesByID`  
**Tags:** IKE Crypto Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `ike-crypto-profiles`  
**Required fields:** `name`, `hash`, `encryption`, `dh_group`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /ike-crypto-profiles/{id}`

**Summary:** Delete an IKE crypto profile  
**Operation ID:** `DeleteIKECryptoProfilesByID`  
**Tags:** IKE Crypto Profiles  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /ike-gateways`

**Summary:** List IKE gateways  
**Operation ID:** `ListIKEGateways`  
**Tags:** IKE Gateways  
**Container scope:** folder | snippet | device  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /ike-gateways`

**Summary:** Create an IKE gateway  
**Operation ID:** `CreateIKEGateways`  
**Tags:** IKE Gateways  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `ike-gateways`  
**Required fields:** `name`, `authentication`, `protocol`, `peer_address`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /ike-gateways/{id}`

**Summary:** Get an IKE gateway  
**Operation ID:** `GetIKEGatewaysByID`  
**Tags:** IKE Gateways  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /ike-gateways/{id}`

**Summary:** Update an IKE gateway  
**Operation ID:** `UpdateIKEGatewaysByID`  
**Tags:** IKE Gateways  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `ike-gateways`  
**Required fields:** `name`, `authentication`, `protocol`, `peer_address`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /ike-gateways/{id}`

**Summary:** Delete an IKE gateway  
**Operation ID:** `DeleteIKEGatewaysByID`  
**Tags:** IKE Gateways  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /ipsec-crypto-profiles`

**Summary:** List IPsec crypto profiles  
**Operation ID:** `ListIPsecCryptoProfiles`  
**Tags:** IPsec Crypto Profiles  
**Container scope:** folder | snippet | device  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /ipsec-crypto-profiles`

**Summary:** Create an IPsec crypto profile  
**Operation ID:** `CreateIPsecCryptoProfiles`  
**Tags:** IPsec Crypto Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `ipsec-crypto-profiles`  
**Required fields:** `name`, `lifetime`  
**Type variants (oneOf/anyOf):** `esp` | `ah`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /ipsec-crypto-profiles/{id}`

**Summary:** Get an IPsec crypto profile  
**Operation ID:** `GetIPsecCryptoProfilesByID`  
**Tags:** IPsec Crypto Profiles  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /ipsec-crypto-profiles/{id}`

**Summary:** Update an IPsec crypto profile  
**Operation ID:** `UpdateIPsecCryptoProfilesByID`  
**Tags:** IPsec Crypto Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `ipsec-crypto-profiles`  
**Required fields:** `name`, `lifetime`  
**Type variants (oneOf/anyOf):** `esp` | `ah`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /ipsec-crypto-profiles/{id}`

**Summary:** Delete an IPsec crypto profile  
**Operation ID:** `DeleteIPsecCryptoProfilesByID`  
**Tags:** IPsec Crypto Profiles  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /ipsec-tunnels`

**Summary:** List IPsec tunnels  
**Operation ID:** `ListIPsecTunnels`  
**Tags:** IPsec Tunnels  
**Container scope:** folder | snippet | device  
**Query params:** name, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /ipsec-tunnels`

**Summary:** Create an IPsec tunnel  
**Operation ID:** `CreateIPsecTunnels`  
**Tags:** IPsec Tunnels  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `ipsec-tunnels`  
**Required fields:** `name`, `auto_key`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /ipsec-tunnels/{id}`

**Summary:** Get an IPsec tunnel  
**Operation ID:** `GetIPsecTunnelsByID`  
**Tags:** IPsec Tunnels  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /ipsec-tunnels/{id}`

**Summary:** Update an IPsec tunnel  
**Operation ID:** `UpdateIPsecTunnelsByID`  
**Tags:** IPsec Tunnels  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `ipsec-tunnels`  
**Required fields:** `name`, `auto_key`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /ipsec-tunnels/{id}`

**Summary:** Delete an IPsec tunnel  
**Operation ID:** `DeleteIPsecTunnelsByID`  
**Tags:** IPsec Tunnels  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /qos-policy-rules`

**Summary:** List QoS policy rules  
**Operation ID:** `ListQoSPolicyRules`  
**Tags:** QoS Rules  
**Container scope:** folder | snippet | device  
**Query params:** name, position, offset, limit  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /qos-policy-rules`

**Summary:** Create a QoS policy rule  
**Operation ID:** `CreateQoSPolicyRules`  
**Tags:** QoS Rules  
**Container scope:** folder | snippet | device (in request body)  
**Query params:** position  
**Body schema:** `qos-policy-rules`  
**Required fields:** `name`, `action`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /qos-policy-rules/{id}`

**Summary:** Get a QoS policy rule  
**Operation ID:** `GetQoSPolicyRulesByID`  
**Tags:** QoS Rules  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /qos-policy-rules/{id}`

**Summary:** Update a QoS policy rule  
**Operation ID:** `UpdateQoSPolicyRulesByID`  
**Tags:** QoS Rules  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `qos-policy-rules`  
**Required fields:** `name`, `action`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /qos-policy-rules/{id}`

**Summary:** Delete a QoS policy rule  
**Operation ID:** `DeleteQoSPolicyRulesByID`  
**Tags:** QoS Rules  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `POST /qos-policy-rules/{id}:move`

**Summary:** Move a QoS policy rule  
**Operation ID:** `MoveQoSPolicyRulesByID`  
**Tags:** QoS Rules  
**Body schema:** `rule-based-move`  
**Required fields:** `destination`, `rulebase`  
**Response codes:** 200, 400, 401, 403, 409, default

### `GET /qos-profiles`

**Summary:** List QoS profiles  
**Operation ID:** `ListQoSProfiles`  
**Tags:** QoS Profiles  
**Container scope:** folder | snippet | device  
**Query params:** name, limit, offset  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /qos-profiles`

**Summary:** Create a QoS profile  
**Operation ID:** `CreateQoSProfiles`  
**Tags:** QoS Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `qos-profiles`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /qos-profiles/{id}`

**Summary:** Get a QoS profile  
**Operation ID:** `GetQoSProfilesByID`  
**Tags:** QoS Profiles  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /qos-profiles/{id}`

**Summary:** Update a QoS profile  
**Operation ID:** `UpdateQoSProfilesByID`  
**Tags:** QoS Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `qos-profiles`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /qos-profiles/{id}`

**Summary:** Delete a QoS profile  
**Operation ID:** `DeleteQoSProfilesByID`  
**Tags:** QoS Profiles  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /zones`

**Summary:** List security zones  
**Operation ID:** `ListZones`  
**Tags:** Security Zones  
**Container scope:** folder | snippet | device  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /zones`

**Summary:** Create a security zone  
**Operation ID:** `CreateZones`  
**Tags:** Security Zones  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `zones`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /zones/{id}`

**Summary:** Get a security zone  
**Operation ID:** `GetZonesByID`  
**Tags:** Security Zones  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /zones/{id}`

**Summary:** Update a security zone  
**Operation ID:** `UpdateZonesByID`  
**Tags:** Security Zones  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `zones`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /zones/{id}`

**Summary:** Delete a security zone  
**Operation ID:** `DeleteZonesByID`  
**Tags:** Security Zones  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /zone-protection-profiles`

**Summary:** List zone protection profiles  
**Operation ID:** `ListZoneProtectionProfiles`  
**Tags:** Zone Protection Profiles  
**Container scope:** folder | snippet | device  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /zone-protection-profiles`

**Summary:** Create a zone protection profile  
**Operation ID:** `CreateZoneProtectionProfiles`  
**Tags:** Zone Protection Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `zone-protection-profiles`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /zone-protection-profiles/{id}`

**Summary:** Get a zone protection profile  
**Operation ID:** `GetZoneProtectionProfilesByID`  
**Tags:** Zone Protection Profiles  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /zone-protection-profiles/{id}`

**Summary:** Update a zone protection profile  
**Operation ID:** `UpdateZoneProtectionProfilesByID`  
**Tags:** Zone Protection Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `zone-protection-profiles`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /zone-protection-profiles/{id}`

**Summary:** Delete a zone protection profile  
**Operation ID:** `DeleteZoneProtectionProfilesByID`  
**Tags:** Zone Protection Profiles  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /nat-rules`

**Summary:** List NAT rules  
**Operation ID:** `ListNatRules`  
**Tags:** NAT Rules  
**Container scope:** folder | snippet | device  
**Query params:** limit, offset, name, position  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /nat-rules`

**Summary:** Create a NAT rule  
**Operation ID:** `CreateNatRules`  
**Tags:** NAT Rules  
**Container scope:** folder | snippet | device (in request body)  
**Query params:** position  
**Body schema:** `nat-rules`  
**Required fields:** `id`, `name`, `from`, `to`, `source`, `destination`, `service`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /nat-rules/{id}`

**Summary:** Get a NAT rule  
**Operation ID:** `GetNatRulesByID`  
**Tags:** NAT Rules  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /nat-rules/{id}`

**Summary:** Update a NAT rule  
**Operation ID:** `UpdateNatRulesByID`  
**Tags:** NAT Rules  
**Container scope:** folder | snippet | device (in request body)  
**Query params:** position  
**Body schema:** `nat-rules`  
**Required fields:** `id`, `name`, `from`, `to`, `source`, `destination`, `service`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /nat-rules/{id}`

**Summary:** Delete a NAT rule  
**Operation ID:** `DeleteNatRulesByID`  
**Tags:** NAT Rules  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /aggregate-interfaces`

**Summary:** List Aggregate Interfaces  
**Operation ID:** `ListAggregateInterfaces`  
**Tags:** Aggregate Interfaces  
**Container scope:** folder | snippet | device  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /aggregate-interfaces`

**Summary:** Create an Aggregate Interface  
**Operation ID:** `CreateAggregateInterfaces`  
**Tags:** Aggregate Interfaces  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `aggregate-interfaces`  
**Required fields:** `name`  
**Type variants (oneOf/anyOf):** `layer2` | `layer3`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /aggregate-interfaces/{id}`

**Summary:** Get an Aggregate Interface  
**Operation ID:** `GetAggregateInterfacesByID`  
**Tags:** Aggregate Interfaces  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /aggregate-interfaces/{id}`

**Summary:** Update an Aggregate Interface  
**Operation ID:** `UpdateAggregateInterfacesByID`  
**Tags:** Aggregate Interfaces  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `aggregate-interfaces`  
**Required fields:** `name`  
**Type variants (oneOf/anyOf):** `layer2` | `layer3`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /aggregate-interfaces/{id}`

**Summary:** Delete an Aggregate Interface  
**Operation ID:** `DeleteAggregateInterfacesByID`  
**Tags:** Aggregate Interfaces  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /ethernet-interfaces`

**Summary:** List ethernet interfaces  
**Operation ID:** `ListEthernetInterfaces`  
**Tags:** Ethernet Interfaces  
**Container scope:** folder | snippet | device  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /ethernet-interfaces`

**Summary:** Create an ethernet interface  
**Operation ID:** `CreateEthernetInterfaces`  
**Tags:** Ethernet Interfaces  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `ethernet-interfaces`  
**Required fields:** `id`, `name`  
**Type variants (oneOf/anyOf):** `aggregate_group` | `tap` | `layer2` | `layer3`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /ethernet-interfaces/{id}`

**Summary:** Get an ethernet interface  
**Operation ID:** `GetEthernetInterfacesByID`  
**Tags:** Ethernet Interfaces  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /ethernet-interfaces/{id}`

**Summary:** Update an ethernet interface  
**Operation ID:** `UpdateEthernetInterfacesByID`  
**Tags:** Ethernet Interfaces  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `ethernet-interfaces`  
**Required fields:** `id`, `name`  
**Type variants (oneOf/anyOf):** `aggregate_group` | `tap` | `layer2` | `layer3`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /ethernet-interfaces/{id}`

**Summary:** Delete an ethernet interface  
**Operation ID:** `DeleteEthernetInterfacesByID`  
**Tags:** Ethernet Interfaces  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /layer2-subinterfaces`

**Summary:** List layer 2 subinterfaces  
**Operation ID:** `ListLayer2Subinterfaces`  
**Tags:** Layer 2 Subinterfaces  
**Container scope:** folder | snippet | device  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /layer2-subinterfaces`

**Summary:** Create a layer 2 subinterface  
**Operation ID:** `CreateLayer2Subinterfaces`  
**Tags:** Layer 2 Subinterfaces  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `layer2-subinterfaces`  
**Required fields:** `name`, `vlan_tag`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /layer2-subinterfaces/{id}`

**Summary:** Get a layer 2 subinterface  
**Operation ID:** `GetLayer2SubinterfacesByID`  
**Tags:** Layer 2 Subinterfaces  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /layer2-subinterfaces/{id}`

**Summary:** Update a layer 2 subinterface  
**Operation ID:** `UpdateLayer2SubinterfacesByID`  
**Tags:** Layer 2 Subinterfaces  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `layer2-subinterfaces`  
**Required fields:** `name`, `vlan_tag`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /layer2-subinterfaces/{id}`

**Summary:** Delete a layer 2 subinterface  
**Operation ID:** `DeleteLayer2SubinterfacesByID`  
**Tags:** Layer 2 Subinterfaces  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /layer3-subinterfaces`

**Summary:** List layer 3 subinterfaces  
**Operation ID:** `ListLayer3Subinterfaces`  
**Tags:** Layer 3 Subinterfaces  
**Container scope:** folder | snippet | device  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /layer3-subinterfaces`

**Summary:** Create a layer 3 subinterface  
**Operation ID:** `CreateLayer3Subinterfaces`  
**Tags:** Layer 3 Subinterfaces  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `layer3-subinterfaces`  
**Required fields:** `name`  
**Type variants (oneOf/anyOf):** `static` | `dhcp_client`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /layer3-subinterfaces/{id}`

**Summary:** Get a layer 3 subinterface  
**Operation ID:** `GetLayer3SubinterfacesByID`  
**Tags:** Layer 3 Subinterfaces  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /layer3-subinterfaces/{id}`

**Summary:** Update a layer 3 subinterface  
**Operation ID:** `UpdateLayer3SubinterfacesByID`  
**Tags:** Layer 3 Subinterfaces  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `layer3-subinterfaces`  
**Required fields:** `name`  
**Type variants (oneOf/anyOf):** `static` | `dhcp_client`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /layer3-subinterfaces/{id}`

**Summary:** Delete a layer 3 subinterface  
**Operation ID:** `DeleteLayer3SubinterfacesByID`  
**Tags:** Layer 3 Subinterfaces  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /loopback-interfaces`

**Summary:** List loopback interfaces  
**Operation ID:** `ListLoopbackInterfaces`  
**Tags:** Loopback Interfaces  
**Container scope:** folder | snippet | device  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /loopback-interfaces`

**Summary:** Create a loopback interface  
**Operation ID:** `CreateLoopbackInterfaces`  
**Tags:** Loopback Interfaces  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `loopback-interfaces`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /loopback-interfaces/{id}`

**Summary:** Get a loopback interface  
**Operation ID:** `GetLoopbackInterfacesByID`  
**Tags:** Loopback Interfaces  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /loopback-interfaces/{id}`

**Summary:** Update a loopback interface  
**Operation ID:** `UpdateLoopbackInterfacesByID`  
**Tags:** Loopback Interfaces  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `loopback-interfaces`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /loopback-interfaces/{id}`

**Summary:** Delete a loopback interface  
**Operation ID:** `DeleteLoopbackInterfacesByID`  
**Tags:** Loopback Interfaces  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /interface-management-profiles`

**Summary:** List interface management profiles  
**Operation ID:** `ListInterfaceManagementProfiles`  
**Tags:** Interface Management Profiles  
**Container scope:** folder | snippet | device  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /interface-management-profiles`

**Summary:** Create a interface management profiles  
**Operation ID:** `CreateInterfaceManagementProfiles`  
**Tags:** Interface Management Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `interface-management-profiles`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /interface-management-profiles/{id}`

**Summary:** Get an interface management profile  
**Operation ID:** `GetInterfaceManagementProfilesByID`  
**Tags:** Interface Management Profiles  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /interface-management-profiles/{id}`

**Summary:** Update an interface management profile  
**Operation ID:** `UpdateInterfaceManagementProfilesByID`  
**Tags:** Interface Management Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `interface-management-profiles`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /interface-management-profiles/{id}`

**Summary:** Delete an interface management profile  
**Operation ID:** `DeleteInterfaceManagementProfilesByID`  
**Tags:** Interface Management Profiles  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /tunnel-interfaces`

**Summary:** List tunnel interfaces  
**Operation ID:** `ListTunnelInterfaces`  
**Tags:** Tunnel Interfaces  
**Container scope:** folder | snippet | device  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /tunnel-interfaces`

**Summary:** Create a tunnel interface  
**Operation ID:** `CreateTunnelInterfaces`  
**Tags:** Tunnel Interfaces  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `tunnel-interfaces`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /tunnel-interfaces/{id}`

**Summary:** Get a tunnel interface  
**Operation ID:** `GetTunnelInterfacesByID`  
**Tags:** Tunnel Interfaces  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /tunnel-interfaces/{id}`

**Summary:** Update a tunnel interface  
**Operation ID:** `UpdateTunnelInterfacesByID`  
**Tags:** Tunnel Interfaces  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `tunnel-interfaces`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /tunnel-interfaces/{id}`

**Summary:** Delete a tunnel interface  
**Operation ID:** `DeleteTunnelInterfacesByID`  
**Tags:** Tunnel Interfaces  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /vlan-interfaces`

**Summary:** List VLAN interfaces  
**Operation ID:** `ListVLANInterfaces`  
**Tags:** VLAN Interfaces  
**Container scope:** folder | snippet | device  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /vlan-interfaces`

**Summary:** Create a VLAN interface  
**Operation ID:** `CreateVLANInterfaces`  
**Tags:** VLAN Interfaces  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `vlan-interfaces`  
**Required fields:** `name`  
**Type variants (oneOf/anyOf):** `static` | `dhcp_client`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /vlan-interfaces/{id}`

**Summary:** Get a VLAN interface  
**Operation ID:** `GetVLANInterfacesByID`  
**Tags:** VLAN Interfaces  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /vlan-interfaces/{id}`

**Summary:** Update a VLAN interface  
**Operation ID:** `UpdateVLANlInterfacesByID`  
**Tags:** VLAN Interfaces  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `vlan-interfaces`  
**Required fields:** `name`  
**Type variants (oneOf/anyOf):** `static` | `dhcp_client`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /vlan-interfaces/{id}`

**Summary:** Delete a VLAN interface  
**Operation ID:** `DeleteVLANInterfacesByID`  
**Tags:** VLAN Interfaces  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /bgp-address-family-profiles`

**Summary:** List BGP address family profiles  
**Operation ID:** `ListBGPAddressFamilyProfiles`  
**Tags:** BGP Address Family Profiles  
**Container scope:** folder | snippet | device  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /bgp-address-family-profiles`

**Summary:** Create a BGP address family profile  
**Operation ID:** `CreateBGPAddressFamilyProfiles`  
**Tags:** BGP Address Family Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `bgp-address-family-profiles`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /bgp-address-family-profiles/{id}`

**Summary:** Get a BGP address family profile  
**Operation ID:** `GetBGPAddressFamilyProfilesByID`  
**Tags:** BGP Address Family Profiles  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /bgp-address-family-profiles/{id}`

**Summary:** Update a BGP address family profile  
**Operation ID:** `UpdateBGPAddressFamilyProfilesByID`  
**Tags:** BGP Address Family Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `bgp-address-family-profiles`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /bgp-address-family-profiles/{id}`

**Summary:** Delete a BGP address family profile  
**Operation ID:** `DeleteBGPAddressFamilyProfilesByID`  
**Tags:** BGP Address Family Profiles  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /bgp-auth-profiles`

**Summary:** List BGP authentication profiles  
**Operation ID:** `ListBGPAuthenticationProfiles`  
**Tags:** BGP Authentication Profiles  
**Container scope:** folder | snippet | device  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /bgp-auth-profiles`

**Summary:** Create a BGP authentication profile  
**Operation ID:** `CreateBGPAuthenticationProfiles`  
**Tags:** BGP Authentication Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `bgp-auth-profiles`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /bgp-auth-profiles/{id}`

**Summary:** Get a BGP authentication profile  
**Operation ID:** `GetBGPAuthenticationProfilesByID`  
**Tags:** BGP Authentication Profiles  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /bgp-auth-profiles/{id}`

**Summary:** Update a BGP authentication profile  
**Operation ID:** `UpdateBGPAuthenticationProfilesByID`  
**Tags:** BGP Authentication Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `bgp-auth-profiles`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /bgp-auth-profiles/{id}`

**Summary:** Delete a BGP authentication profile  
**Operation ID:** `DeleteBGPAuthenticationProfilesByID`  
**Tags:** BGP Authentication Profiles  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /bgp-filtering-profiles`

**Summary:** List BGP filtering profiles  
**Operation ID:** `ListBGPFilteringProfiles`  
**Tags:** BGP Filtering Profiles  
**Container scope:** folder | snippet | device  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /bgp-filtering-profiles`

**Summary:** Create a BGP filtering profile  
**Operation ID:** `CreateBGPFilteringProfiles`  
**Tags:** BGP Filtering Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `bgp-filtering-profiles`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /bgp-filtering-profiles/{id}`

**Summary:** Get a BGP filtering profile  
**Operation ID:** `GetBGPFilteringProfilesByID`  
**Tags:** BGP Filtering Profiles  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /bgp-filtering-profiles/{id}`

**Summary:** Update a BGP filtering profile  
**Operation ID:** `UpdateBGPFilteringProfilesByID`  
**Tags:** BGP Filtering Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `bgp-filtering-profiles`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /bgp-filtering-profiles/{id}`

**Summary:** Delete a BGP filtering profile  
**Operation ID:** `DeleteBGPFilteringProfilesByID`  
**Tags:** BGP Filtering Profiles  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /bgp-redistribution-profiles`

**Summary:** List BGP redistribution profiles  
**Operation ID:** `ListBGPRedistributionProfiles`  
**Tags:** BGP Redistribution Profiles  
**Container scope:** folder | snippet | device  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /bgp-redistribution-profiles`

**Summary:** Create a BGP redistribution profile  
**Operation ID:** `CreateBGPRedistributionProfiles`  
**Tags:** BGP Redistribution Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `bgp-redistribution-profiles`  
**Required fields:** `name`, `ipv4`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /bgp-redistribution-profiles/{id}`

**Summary:** Get a BGP redistribution profile  
**Operation ID:** `GetBGPRedistributionProfilesByID`  
**Tags:** BGP Redistribution Profiles  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /bgp-redistribution-profiles/{id}`

**Summary:** Update a BGP redistribution profile  
**Operation ID:** `UpdateBGPRedistributionProfilesByID`  
**Tags:** BGP Redistribution Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `bgp-redistribution-profiles`  
**Required fields:** `name`, `ipv4`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /bgp-redistribution-profiles/{id}`

**Summary:** Delete a BGP redistribution profile  
**Operation ID:** `DeleteBGPRedistributionProfilesByID`  
**Tags:** BGP Redistribution Profiles  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /bgp-route-map-redistributions`

**Summary:** List BGP route map redistributions  
**Operation ID:** `ListBGPRouteMapRedistributions`  
**Tags:** BGP Route Map Redistributions  
**Container scope:** folder | snippet | device  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /bgp-route-map-redistributions`

**Summary:** Create a BGP route map redistribution  
**Operation ID:** `CreateBGPRouteMapRedistributions`  
**Tags:** BGP Route Map Redistributions  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `bgp-route-map-redistributions`  
**Required fields:** `name`  
**Type variants (oneOf/anyOf):** `bgp` | `ospf` | `connected_static`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /bgp-route-map-redistributions/{id}`

**Summary:** Get a BGP route map redistribution  
**Operation ID:** `GetBGPRouteMapRedistributionsByID`  
**Tags:** BGP Route Map Redistributions  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /bgp-route-map-redistributions/{id}`

**Summary:** Update a BGP route map redistribution  
**Operation ID:** `UpdateBGPRouteMapRedistributionsByID`  
**Tags:** BGP Route Map Redistributions  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `bgp-route-map-redistributions`  
**Required fields:** `name`  
**Type variants (oneOf/anyOf):** `bgp` | `ospf` | `connected_static`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /bgp-route-map-redistributions/{id}`

**Summary:** Delete a BGP route map redistribution  
**Operation ID:** `DeleteBGPRouteMapRedistributionsByID`  
**Tags:** BGP Route Map Redistributions  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /bgp-route-maps`

**Summary:** List BGP route maps  
**Operation ID:** `ListBGPRouteMaps`  
**Tags:** BGP Route Maps  
**Container scope:** folder | snippet | device  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /bgp-route-maps`

**Summary:** Create a BGP route map  
**Operation ID:** `CreateBGPRouteMaps`  
**Tags:** BGP Route Maps  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `bgp-route-maps`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /bgp-route-maps/{id}`

**Summary:** Get a BGP route map  
**Operation ID:** `GetBGPRouteMapsByID`  
**Tags:** BGP Route Maps  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /bgp-route-maps/{id}`

**Summary:** Update a BGP route map  
**Operation ID:** `UpdateBGPRouteMapsByID`  
**Tags:** BGP Route Maps  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `bgp-route-maps`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /bgp-route-maps/{id}`

**Summary:** Delete a BGP route map  
**Operation ID:** `DeleteBGPRouteMapsByID`  
**Tags:** BGP Route Maps  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /link-tags`

**Summary:** List link tags  
**Operation ID:** `ListLinkTags`  
**Tags:** Link Tags  
**Container scope:** folder | snippet | device  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /link-tags`

**Summary:** Create a link tag  
**Operation ID:** `CreateLinkTags`  
**Tags:** Link Tags  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `link-tags`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /link-tags/{id}`

**Summary:** Get a link tag  
**Operation ID:** `GetLinkTagsByID`  
**Tags:** Link Tags  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /link-tags/{id}`

**Summary:** Update a link tag  
**Operation ID:** `UpdateLinkTagsByID`  
**Tags:** Link Tags  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `link-tags`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /link-tags/{id}`

**Summary:** Delete a link tag  
**Operation ID:** `DeleteLinkTagsByID`  
**Tags:** Link Tags  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /logical-routers`

**Summary:** List logical routers  
**Operation ID:** `ListLogicalRouters`  
**Tags:** Logical Routers  
**Container scope:** folder | snippet | device  
**Query params:** pagination, limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /logical-routers`

**Summary:** Create a logical router  
**Operation ID:** `CreateLogicalRouters`  
**Tags:** Logical Routers  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `logical-routers`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /logical-routers/{id}`

**Summary:** Get a logical router  
**Operation ID:** `GetLogicalRoutersByID`  
**Tags:** Logical Routers  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /logical-routers/{id}`

**Summary:** Update a logical router  
**Operation ID:** `UpdateLogicalRoutersByID`  
**Tags:** Logical Routers  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `logical-routers`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /logical-routers/{id}`

**Summary:** Delete a logical router  
**Operation ID:** `DeleteLogicalRoutersByID`  
**Tags:** Logical Routers  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /ospf-auth-profiles`

**Summary:** List OSPF authentication profiles  
**Operation ID:** `ListOSPFAuthenticationProfiles`  
**Tags:** OSPF Authentication Profiles  
**Container scope:** folder | snippet | device  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /ospf-auth-profiles`

**Summary:** Create an OSPF authentication profile  
**Operation ID:** `CreateOSPFAuthenticationProfiles`  
**Tags:** OSPF Authentication Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `ospf-auth-profiles`  
**Required fields:** `name`  
**Type variants (oneOf/anyOf):** `password` | `md5`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /ospf-auth-profiles/{id}`

**Summary:** Get an OSPF authentication profile  
**Operation ID:** `GetOSPFAuthenticationProfilesByID`  
**Tags:** OSPF Authentication Profiles  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /ospf-auth-profiles/{id}`

**Summary:** Update an OSPF authentication profile  
**Operation ID:** `UpdateOSPFAuthenticationProfilesByID`  
**Tags:** OSPF Authentication Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `ospf-auth-profiles`  
**Required fields:** `name`  
**Type variants (oneOf/anyOf):** `password` | `md5`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /ospf-auth-profiles/{id}`

**Summary:** Delete an OSPF authentication profile  
**Operation ID:** `DeleteOSPFAuthenticationProfilesByID`  
**Tags:** OSPF Authentication Profiles  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /pbf-rules`

**Summary:** List PBF rules  
**Operation ID:** `ListPBFRules`  
**Tags:** PBF Rules  
**Container scope:** folder | snippet | device  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /pbf-rules`

**Summary:** Create a PBF rule  
**Operation ID:** `CreatePBFRules`  
**Tags:** PBF Rules  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `pbf-rules`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /pbf-rules/{id}`

**Summary:** Get a PBF rule  
**Operation ID:** `GetPBFRulesByID`  
**Tags:** PBF Rules  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /pbf-rules/{id}`

**Summary:** Update a PBF rule  
**Operation ID:** `UpdatePBFRulesByID`  
**Tags:** PBF Rules  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `pbf-rules`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /pbf-rules/{id}`

**Summary:** Delete a PBF rule  
**Operation ID:** `DeletePBFRulesByID`  
**Tags:** PBF Rules  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /route-access-lists`

**Summary:** List route access lists  
**Operation ID:** `ListRouteAccessLists`  
**Tags:** Route Access Lists  
**Container scope:** folder | snippet | device  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /route-access-lists`

**Summary:** Create a route access list  
**Operation ID:** `CreateRouteAccessLists`  
**Tags:** Route Access Lists  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `route-access-lists`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /route-access-lists/{id}`

**Summary:** Get a route access list  
**Operation ID:** `GetRouteAccessListsByID`  
**Tags:** Route Access Lists  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /route-access-lists/{id}`

**Summary:** Update a route access list  
**Operation ID:** `UpdateRouteAccessListsByID`  
**Tags:** Route Access Lists  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `route-access-lists`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /route-access-lists/{id}`

**Summary:** Delete a route access list  
**Operation ID:** `DeleteRouteAccessListsByID`  
**Tags:** Route Access Lists  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /route-community-lists`

**Summary:** List route community lists  
**Operation ID:** `ListRouteCommunityLists`  
**Tags:** Route Community Lists  
**Container scope:** folder | snippet | device  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /route-community-lists`

**Summary:** Create a route community list  
**Operation ID:** `CreateRouteCommunityLists`  
**Tags:** Route Community Lists  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `route-community-lists`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /route-community-lists/{id}`

**Summary:** Get a route community list  
**Operation ID:** `GetRouteCommunityListsByID`  
**Tags:** Route Community Lists  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /route-community-lists/{id}`

**Summary:** Update a route community list  
**Operation ID:** `UpdateRouteCommunityListsByID`  
**Tags:** Route Community Lists  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `route-community-lists`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /route-community-lists/{id}`

**Summary:** Delete a route community list  
**Operation ID:** `DeleteRouteCommunityListsByID`  
**Tags:** Route Community Lists  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /route-path-access-lists`

**Summary:** List route path access lists  
**Operation ID:** `ListRoutePathAccessLists`  
**Tags:** Route Path Access Lists  
**Container scope:** folder | snippet | device  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /route-path-access-lists`

**Summary:** Create a route path access list  
**Operation ID:** `CreateRoutePathAccessLists`  
**Tags:** Route Path Access Lists  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `route-path-access-lists`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /route-path-access-lists/{id}`

**Summary:** Get a route path access list  
**Operation ID:** `GetRoutePathAccessListsByID`  
**Tags:** Route Path Access Lists  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /route-path-access-lists/{id}`

**Summary:** Update a route path access list  
**Operation ID:** `UpdateRoutePathAccessListsByID`  
**Tags:** Route Path Access Lists  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `route-path-access-lists`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /route-path-access-lists/{id}`

**Summary:** Delete a route path access list  
**Operation ID:** `DeleteRoutePathAccessListsByID`  
**Tags:** Route Path Access Lists  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /route-prefix-lists`

**Summary:** List route prefix lists  
**Operation ID:** `ListRoutePrefixLists`  
**Tags:** Route Prefix Lists  
**Container scope:** folder | snippet | device  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /route-prefix-lists`

**Summary:** Create a route prefix list  
**Operation ID:** `CreateRoutePrefixLists`  
**Tags:** Route Prefix Lists  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `route-prefix-lists`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /route-prefix-lists/{id}`

**Summary:** Get a route prefix list  
**Operation ID:** `GetRoutePrefixListsByID`  
**Tags:** Route Prefix Lists  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /route-prefix-lists/{id}`

**Summary:** Update a route prefix list  
**Operation ID:** `UpdateRoutePrefixListsByID`  
**Tags:** Route Prefix Lists  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `route-prefix-lists`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /route-prefix-lists/{id}`

**Summary:** Delete a route prefix list  
**Operation ID:** `DeleteRoutePrefixListsByID`  
**Tags:** Route Prefix Lists  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /auto-vpn-clusters`

**Summary:** List Auto VPN clusters  
**Operation ID:** `ListAutoVPNClusters`  
**Tags:** Auto VPN Clusters  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /auto-vpn-clusters`

**Summary:** Create an Auto VPN cluster  
**Operation ID:** `CreateAutoVPNClusters`  
**Tags:** Auto VPN Clusters  
**Body schema:** `auto-vpn-clusters`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /auto-vpn-clusters/{id}`

**Summary:** Get an Auto VPN cluster  
**Operation ID:** `GetAutoVPNClustersByID`  
**Tags:** Auto VPN Clusters  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /auto-vpn-clusters/{id}`

**Summary:** Update an Auto VPN cluster  
**Operation ID:** `UpdateAutoVPNClustersByID`  
**Tags:** Auto VPN Clusters  
**Body schema:** `auto-vpn-clusters`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /auto-vpn-clusters/{id}`

**Summary:** Delete an Auto VPN cluster  
**Operation ID:** `DeleteAutoVPNClustersByID`  
**Tags:** Auto VPN Clusters  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /auto-vpn-monitor`

**Summary:** Get Auto VPN status  
**Operation ID:** `GetAutoVPNMonitor`  
**Tags:** Auto VPN Monitor  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /auto-vpn-push`

**Summary:** Push Auto VPN configs  
**Operation ID:** `CreateAutoVPNPushConfigs`  
**Tags:** Auto VPN Config Push  
**Body schema:** `auto-vpn-push-config`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /auto-vpn-settings`

**Summary:** Get Auto VPN settings  
**Operation ID:** `GetAutoVPNSettings`  
**Tags:** Auto VPN Settings  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /auto-vpn-settings`

**Summary:** Update Auto VPN settings  
**Operation ID:** `UpdateAutoVPNSettings`  
**Tags:** Auto VPN Settings  
**Body schema:** `auto-vpn-settings`  
**Required fields:** `vpn_address_pool`, `as_range`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /sdwan-error-correction-profiles`

**Summary:** List SD-WAN error correction profiles  
**Operation ID:** `ListSDWANErrorCorrectionProfiles`  
**Tags:** SD-WAN Error Correction Profiles  
**Container scope:** folder | snippet | device  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /sdwan-error-correction-profiles`

**Summary:** Create an SD-WAN error correction profile  
**Operation ID:** `CreateSDWANErrorCorrectionProfiles`  
**Tags:** SD-WAN Error Correction Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `sdwan-error-correction-profiles`  
**Required fields:** `name`, `activation_threshold`, `mode`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /sdwan-error-correction-profiles/{id}`

**Summary:** Get an SD-WAN error correction profile  
**Operation ID:** `GetSDWANErrorCorrectionProfilesByID`  
**Tags:** SD-WAN Error Correction Profiles  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /sdwan-error-correction-profiles/{id}`

**Summary:** Update an SD-WAN error correction profile  
**Operation ID:** `UpdateSDWANErrorCorrectionProfilesByID`  
**Tags:** SD-WAN Error Correction Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `sdwan-error-correction-profiles`  
**Required fields:** `name`, `activation_threshold`, `mode`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /sdwan-error-correction-profiles/{id}`

**Summary:** Delete an SD-WAN error correction profile  
**Operation ID:** `DeleteSDWANErrorCorrectionProfilesByID`  
**Tags:** SD-WAN Error Correction Profiles  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /sdwan-path-quality-profiles`

**Summary:** List SD-WAN path quality profiles  
**Operation ID:** `ListSDWANPathQualityProfiles`  
**Tags:** SD-WAN Path Quality Profiles  
**Container scope:** folder | snippet | device  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /sdwan-path-quality-profiles`

**Summary:** Create an SD-WAN path quality profile  
**Operation ID:** `CreateSDWANPathQualityProfiles`  
**Tags:** SD-WAN Path Quality Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `sdwan-path-quality-profiles`  
**Required fields:** `name`, `metric`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /sdwan-path-quality-profiles/{id}`

**Summary:** Get an SD-WAN path quality profile  
**Operation ID:** `GetSDWANPathQualityProfilesByID`  
**Tags:** SD-WAN Path Quality Profiles  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /sdwan-path-quality-profiles/{id}`

**Summary:** Update an SD-WAN path quality profile  
**Operation ID:** `UpdateSDWANPathQualityProfilesByID`  
**Tags:** SD-WAN Path Quality Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `sdwan-path-quality-profiles`  
**Required fields:** `name`, `metric`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /sdwan-path-quality-profiles/{id}`

**Summary:** Delete an SD-WAN path quality profile  
**Operation ID:** `DeleteSDWANPathQualityProfilesByID`  
**Tags:** SD-WAN Path Quality Profiles  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /sdwan-rules`

**Summary:** List SD-WAN rules  
**Operation ID:** `ListSDWANRules`  
**Tags:** SD-WAN Rules  
**Container scope:** folder | snippet | device  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /sdwan-rules`

**Summary:** Create an SD-WAN rule  
**Operation ID:** `CreateSDWANRules`  
**Tags:** SD-WAN Rules  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `sdwan-rules`  
**Required fields:** `name`, `from`, `position`, `to`, `source`, `source_user`, `destination`, `application`, `service`, `action`, `path_quality_profile`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /sdwan-rules/{id}`

**Summary:** Get an SD-WAN rule  
**Operation ID:** `GetSDWANRulesByID`  
**Tags:** SD-WAN Rules  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /sdwan-rules/{id}`

**Summary:** Update an SD-WAN rule  
**Operation ID:** `UpdateSDWANRulesByID`  
**Tags:** SD-WAN Rules  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `sdwan-rules`  
**Required fields:** `name`, `from`, `position`, `to`, `source`, `source_user`, `destination`, `application`, `service`, `action`, `path_quality_profile`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /sdwan-rules/{id}`

**Summary:** Delete an SD-WAN rule  
**Operation ID:** `DeleteSDWANRulesByID`  
**Tags:** SD-WAN Rules  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /sdwan-saas-quality-profiles`

**Summary:** List SD-WAN SaaS quality profiles  
**Operation ID:** `ListSDWANSaaSQualityProfiles`  
**Tags:** SD-WAN SaaS Quality Profiles  
**Container scope:** folder | snippet | device  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /sdwan-saas-quality-profiles`

**Summary:** Create an SD-WAN SaaS quality profile  
**Operation ID:** `CreateSDWANSaaSQualityProfiles`  
**Tags:** SD-WAN SaaS Quality Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `sdwan-saas-quality-profiles`  
**Required fields:** `name`, `monitor_mode`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /sdwan-saas-quality-profiles/{id}`

**Summary:** Get an SD-WAN SaaS quality profile  
**Operation ID:** `GetSDWANSaaSQualityProfilesByID`  
**Tags:** SD-WAN SaaS Quality Profiles  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /sdwan-saas-quality-profiles/{id}`

**Summary:** Update an SD-WAN SaaS quality profile  
**Operation ID:** `UpdateSDWANSaaSQualityProfilesByID`  
**Tags:** SD-WAN SaaS Quality Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `sdwan-saas-quality-profiles`  
**Required fields:** `name`, `monitor_mode`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /sdwan-saas-quality-profiles/{id}`

**Summary:** Delete an SD-WAN SaaS quality profile  
**Operation ID:** `DeleteSDWANSaaSQualityProfilesByID`  
**Tags:** SD-WAN SaaS Quality Profiles  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /sdwan-traffic-distribution-profiles`

**Summary:** List SD-WAN traffic distribution profiles  
**Operation ID:** `ListSDWANTrafficDistributionProfiles`  
**Tags:** SD-WAN Traffic Distribution Profiles  
**Container scope:** folder | snippet | device  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /sdwan-traffic-distribution-profiles`

**Summary:** Create an SD-WAN traffic distribution profile  
**Operation ID:** `CreateSDWANTrafficDistributionProfiles`  
**Tags:** SD-WAN Traffic Distribution Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `sdwan-traffic-distribution-profiles`  
**Required fields:** `name`, `traffic-distribution`, `link-tags`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /sdwan-traffic-distribution-profiles/{id}`

**Summary:** Get an SD-WAN traffic distribution profile  
**Operation ID:** `GetSDWANTrafficDistributionProfilesByID`  
**Tags:** SD-WAN Traffic Distribution Profiles  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /sdwan-traffic-distribution-profiles/{id}`

**Summary:** Update an SD-WAN traffic distribution profile  
**Operation ID:** `UpdateSDWANTrafficDistributionProfilesByID`  
**Tags:** SD-WAN Traffic Distribution Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `sdwan-traffic-distribution-profiles`  
**Required fields:** `name`, `traffic-distribution`, `link-tags`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /sdwan-traffic-distribution-profiles/{id}`

**Summary:** Delete an SD-WAN traffic distribution profile  
**Operation ID:** `DeleteSDWANTrafficDistributionProfilesByID`  
**Tags:** SD-WAN Traffic Distribution Profiles  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /dhcp-interfaces`

**Summary:** List DHCP interfaces  
**Operation ID:** `ListDHCPInterfaces`  
**Tags:** DHCP Interfaces  
**Container scope:** folder | snippet | device  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /dhcp-interfaces`

**Summary:** Create a DHCP interface  
**Operation ID:** `CreateDHCPInterfaces`  
**Tags:** DHCP Interfaces  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `dhcp-interfaces`  
**Required fields:** `name`  
**Type variants (oneOf/anyOf):** `server` | `relay`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /dhcp-interfaces/{id}`

**Summary:** Get a DHCP interface  
**Operation ID:** `GetDHCPInterfacesByID`  
**Tags:** DHCP Interfaces  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /dhcp-interfaces/{id}`

**Summary:** Update a DHCP interface  
**Operation ID:** `UpdateDHCPInterfacesByID`  
**Tags:** DHCP Interfaces  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `dhcp-interfaces`  
**Required fields:** `name`  
**Type variants (oneOf/anyOf):** `server` | `relay`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /dhcp-interfaces/{id}`

**Summary:** Delete a DHCP interface  
**Operation ID:** `DeleteDHCPInterfacesByID`  
**Tags:** DHCP Interfaces  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /dns-proxies`

**Summary:** List DNS proxies  
**Operation ID:** `ListDNSProxies`  
**Tags:** DNS Proxies  
**Container scope:** folder | snippet | device  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /dns-proxies`

**Summary:** Create a DNS proxy  
**Operation ID:** `CreateDNSProxies`  
**Tags:** DNS Proxies  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `dns-proxies`  
**Required fields:** `name`, `default`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /dns-proxies/{id}`

**Summary:** Get a DNS proxy  
**Operation ID:** `GetDNSProxiesByID`  
**Tags:** DNS Proxies  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /dns-proxies/{id}`

**Summary:** Update a DNS proxy  
**Operation ID:** `UpdateDNSProxiesByID`  
**Tags:** DNS Proxies  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `dns-proxies`  
**Required fields:** `name`, `default`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /dns-proxies/{id}`

**Summary:** Delete a DNS proxy  
**Operation ID:** `DeleteDNSProxiesByID`  
**Tags:** DNS Proxies  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /remote-networks-license-info`

**Summary:** Get Remote Networks License Info  
**Operation ID:** `getRemoteNetworksLicenseInfo`  
**Tags:** Remote Networks License  
**Response codes:** 200, 400, 401, 403, 404, 409, 500, default

### `GET /lldp-profiles`

**Summary:** List LLDP profiles  
**Operation ID:** `ListLLDPProfiles`  
**Tags:** LLDP Profiles  
**Container scope:** folder | snippet | device  
**Query params:** limit, offset, name  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /lldp-profiles`

**Summary:** Create an LLDP profile  
**Operation ID:** `CreateLLDPProfiles`  
**Tags:** LLDP Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `lldp-profiles`  
**Required fields:** `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /lldp-profiles/{id}`

**Summary:** Get an LLDP profile  
**Operation ID:** `GetLLDPProfilesByID`  
**Tags:** LLDP Profiles  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /lldp-profiles/{id}`

**Summary:** Update an LLDP profile  
**Operation ID:** `UpdateLLDPProfilesByID`  
**Tags:** LLDP Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `lldp-profiles`  
**Required fields:** `name`  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `DELETE /lldp-profiles/{id}`

**Summary:** Delete an LLDP profile  
**Operation ID:** `DeleteLLDPProfilesByID`  
**Tags:** LLDP Profiles  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /network_packet_broker_profiles`

**Summary:** List all Network Packet Broker Profiles  
**Operation ID:** `ListNetworkPacketBrokerProfiles`  
**Tags:** Network Packet Broker Profiles  
**Container scope:** folder  
**Query params:** limit, offset  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /network_packet_broker_profiles`

**Summary:** Create a new Network Packet Broker Profile  
**Operation ID:** `CreateNetworkPacketBrokerProfiles`  
**Tags:** Network Packet Broker Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `network_packet_broker_profiles`  
**Required fields:** `id`, `name`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /network_packet_broker_profiles/{id}`

**Summary:** Get Network Packet Broker Profile by ID  
**Operation ID:** `GetNetworkPacketBrokerProfilesByID`  
**Tags:** Network Packet Broker Profiles  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /network_packet_broker_profiles/{id}`

**Summary:** Update Network Packet Broker Profile by ID  
**Operation ID:** `UpdateNetworkPacketBrokerProfilesByID`  
**Tags:** Network Packet Broker Profiles  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `network_packet_broker_profiles`  
**Required fields:** `id`, `name`  
**Response codes:** 200, 400, 401, 403, 404, default

### `DELETE /network_packet_broker_profiles/{id}`

**Summary:** Delete a Network Packet Broker Profile  
**Operation ID:** `DeleteNetworkPacketBrokerProfilesByID`  
**Tags:** Network Packet Broker Profiles  
**Response codes:** 200, 400, 401, 403, 404, 409, default

### `GET /network_packet_broker_rules`

**Summary:** List all Network Packet Broker Rules  
**Operation ID:** `ListNetworkPacketBrokerRules`  
**Tags:** Network Packet Broker Rules  
**Container scope:** folder  
**Query params:** limit, offset  
**Response codes:** 200, 400, 401, 403, 404, default

### `POST /network_packet_broker_rules`

**Summary:** Create a new Network Packet Broker Rule  
**Operation ID:** `CreateNetworkPacketBrokerRules`  
**Tags:** Network Packet Broker Rules  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `network_packet_broker_rules`  
**Required fields:** `id`, `name`, `action`  
**Response codes:** 201, 400, 401, 403, 409, default

### `GET /network_packet_broker_rules/{id}`

**Summary:** Get Network Packet Broker Rule by ID  
**Operation ID:** `GetNetworkPacketBrokerRulesByID`  
**Tags:** Network Packet Broker Rules  
**Response codes:** 200, 400, 401, 403, 404, default

### `PUT /network_packet_broker_rules/{id}`

**Summary:** Update Network Packet Broker Rule by ID  
**Operation ID:** `UpdateNetworkPacketBrokerRulesByID`  
**Tags:** Network Packet Broker Rules  
**Container scope:** folder | snippet | device (in request body)  
**Body schema:** `network_packet_broker_rules`  
**Required fields:** `id`, `name`, `action`  
**Response codes:** 200, 400, 401, 403, 404, default

### `DELETE /network_packet_broker_rules/{id}`

**Summary:** Delete a Network Packet Broker Rule  
**Operation ID:** `DeleteNetworkPacketBrokerRulesByID`  
**Tags:** Network Packet Broker Rules  
**Response codes:** 200, 400, 401, 403, 404, 409, default
