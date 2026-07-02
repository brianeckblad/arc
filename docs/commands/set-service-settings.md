---
command: "set service-settings"
description: "Create service settings"
category: device-device-settings
scope: global
---

# set service-settings

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create service settings

## Usage

```
set service-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > set service-settings
```

Run directly on device via SSH:
```
arc:fw-01 > set service-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set service-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
