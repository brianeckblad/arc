---
command: "update authentication-settings"
description: "Update authentication settings"
category: device-device-settings
scope: global
---

# update authentication-settings

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update authentication settings

## Usage

```
update authentication-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > update authentication-settings
```

Run directly on device via SSH:
```
arc:fw-01 > update authentication-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update authentication-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
