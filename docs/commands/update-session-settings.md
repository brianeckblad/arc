---
command: "update session-settings"
description: "Update session settings"
category: device-device-settings
scope: global
---

# update session-settings

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update session settings

## Usage

```
update session-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > update session-settings
```

Run directly on device via SSH:
```
arc:fw-01 > update session-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update session-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
