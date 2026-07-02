---
command: "delete vpn-settings"
description: "Delete VPN settings"
category: device-device-settings
scope: global
---

# delete vpn-settings

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete VPN settings

## Usage

```
delete vpn-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > delete vpn-settings
```

Run directly on device via SSH:
```
arc:fw-01 > delete vpn-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete vpn-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
