---
command: "delete motd-banner-settings"
description: "Delete login banner settings"
category: device-device-settings
scope: global
---

# delete motd-banner-settings

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete login banner settings

## Usage

```
delete motd-banner-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > delete motd-banner-settings
```

Run directly on device via SSH:
```
arc:fw-01 > delete motd-banner-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete motd-banner-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
