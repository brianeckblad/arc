---
command: "show update-schedule id"
description: "Get existing update schedule settings"
category: device-device-settings
scope: global
---

# show update-schedule id

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get existing update schedule settings

## Usage

```
show update-schedule id [--remote]
```

## Examples

Run via SCM API:
```
arc > show update-schedule id
```

Run directly on device via SSH:
```
arc:fw-01 > show update-schedule id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show update-schedule id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
