---
command: "update service-settings"
description: "Update service settings"
category: device-device-settings
scope: global
---

# update service-settings

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update service settings

## Usage

```
update service-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > update service-settings
```

Run directly on device via SSH:
```
arc:fw-01 > update service-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update service-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
