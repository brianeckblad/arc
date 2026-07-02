---
command: "delete service-settings"
description: "Delete service settings"
category: device-device-settings
scope: global
---

# delete service-settings

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete service settings

## Usage

```
delete service-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > delete service-settings
```

Run directly on device via SSH:
```
arc:fw-01 > delete service-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete service-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
