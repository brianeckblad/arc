---
command: "delete authentication-settings"
description: "Delete authentication settings"
category: device-device-settings
scope: global
---

# delete authentication-settings

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete authentication settings

## Usage

```
delete authentication-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > delete authentication-settings
```

Run directly on device via SSH:
```
arc:fw-01 > delete authentication-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete authentication-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
