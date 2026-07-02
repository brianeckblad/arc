---
command: "set authentication-settings"
description: "Create authentication settings"
category: device-device-settings
scope: global
---

# set authentication-settings

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create authentication settings

## Usage

```
set authentication-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > set authentication-settings
```

Run directly on device via SSH:
```
arc:fw-01 > set authentication-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set authentication-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
