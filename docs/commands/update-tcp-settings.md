---
command: "update tcp-settings"
description: "Update TCP settings"
category: device-device-settings
scope: global
---

# update tcp-settings

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update TCP settings

## Usage

```
update tcp-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > update tcp-settings
```

Run directly on device via SSH:
```
arc:fw-01 > update tcp-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update tcp-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
