---
command: "show vpn-settings"
description: "List VPN settings"
category: device-device-settings
scope: global
---

# show vpn-settings

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List VPN settings

## Usage

```
show vpn-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > show vpn-settings
```

Run directly on device via SSH:
```
arc:fw-01 > show vpn-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show vpn-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
