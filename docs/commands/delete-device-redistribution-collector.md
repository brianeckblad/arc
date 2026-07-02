---
command: "delete device-redistribution-collector"
description: "Delete device redistribution collector settings"
category: device-device-settings
scope: global
---

# delete device-redistribution-collector

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete device redistribution collector settings

## Usage

```
delete device-redistribution-collector [--remote]
```

## Examples

Run via SCM API:
```
arc > delete device-redistribution-collector
```

Run directly on device via SSH:
```
arc:fw-01 > delete device-redistribution-collector --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete device-redistribution-collector
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
