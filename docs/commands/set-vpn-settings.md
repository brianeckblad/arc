---
command: "set vpn-settings"
description: "Create VPN settings"
category: device-device-settings
scope: global
---

# set vpn-settings

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create VPN settings

## Usage

```
set vpn-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > set vpn-settings
```

Run directly on device via SSH:
```
arc:fw-01 > set vpn-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set vpn-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
