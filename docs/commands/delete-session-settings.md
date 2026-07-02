---
command: "delete session-settings"
description: "Delete session settings"
category: device-device-settings
scope: global
---

# delete session-settings

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete session settings

## Usage

```
delete session-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > delete session-settings
```

Run directly on device via SSH:
```
arc:fw-01 > delete session-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete session-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
