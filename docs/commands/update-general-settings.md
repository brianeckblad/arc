---
command: "update general-settings"
description: "Update general settings"
category: device-device-settings
scope: global
---

# update general-settings

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update general settings

## Usage

```
update general-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > update general-settings
```

Run directly on device via SSH:
```
arc:fw-01 > update general-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update general-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
