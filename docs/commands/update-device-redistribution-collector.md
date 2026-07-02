---
command: "update device-redistribution-collector"
description: "Update device redistribution collector settings"
category: device-device-settings
scope: global
---

# update device-redistribution-collector

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update device redistribution collector settings

## Usage

```
update device-redistribution-collector [--remote]
```

## Examples

Run via SCM API:
```
arc > update device-redistribution-collector
```

Run directly on device via SSH:
```
arc:fw-01 > update device-redistribution-collector --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update device-redistribution-collector
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
