---
command: "update vpn-settings"
description: "Update VPN settings"
category: device-device-settings
scope: global
---

# update vpn-settings

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update VPN settings

## Usage

```
update vpn-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > update vpn-settings
```

Run directly on device via SSH:
```
arc:fw-01 > update vpn-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update vpn-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
