---
command: "set device-redistribution-collector"
description: "Create device redistribution collector settings"
category: device-device-settings
scope: global
---

# set device-redistribution-collector

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create device redistribution collector settings

## Usage

```
set device-redistribution-collector [--remote]
```

## Examples

Run via SCM API:
```
arc > set device-redistribution-collector
```

Run directly on device via SSH:
```
arc:fw-01 > set device-redistribution-collector --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set device-redistribution-collector
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
