---
command: "show bgp-profile"
description: "Show BGP routing profiles (configuration) in the active folder"
feature_flag: bgp_routing
category: network
scope: folder
api: "GET /config/network/v1/bgp-address-family-profiles"
---

# show bgp-profile

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** `show routing protocol bgp summary`

## Description

Show BGP routing profiles (configuration) in the active folder

## Usage

```
show bgp-profile [--remote]
```

## Examples

Run via SCM API:
```
arc > show bgp-profile
```

Run directly on device via SSH:
```
arc:fw-01 > show bgp-profile --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show bgp-profile
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
