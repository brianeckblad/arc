---
command: "show ike-gateway"
description: "Show IKE gateway configurations (VPN) in the active folder"
feature_flag: ipsec_vpn
category: network
scope: folder
api: "GET /config/network/v1/ike-gateways"
---

# show ike-gateway

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** `show vpn ike-sa gateway all`

## Description

Show IKE gateway configurations (VPN) in the active folder

## Usage

```
show ike-gateway [--remote]
```

## Examples

Run via SCM API:
```
arc > show ike-gateway
```

Run directly on device via SSH:
```
arc:fw-01 > show ike-gateway --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ike-gateway
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
