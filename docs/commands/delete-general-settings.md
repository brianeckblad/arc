---
command: "delete general-settings"
description: "Delete general settings"
category: device-device-settings
scope: global
---

# delete general-settings

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete general settings

## Usage

```
delete general-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > delete general-settings
```

Run directly on device via SSH:
```
arc:fw-01 > delete general-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete general-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
