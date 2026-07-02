---
command: "show service-settings"
description: "List service settings"
category: device-device-settings
scope: global
---

# show service-settings

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List service settings

## Usage

```
show service-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > show service-settings
```

Run directly on device via SSH:
```
arc:fw-01 > show service-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show service-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
