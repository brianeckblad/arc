---
command: "delete session-timeouts"
description: "Delete session settings"
category: device-device-settings
scope: global
---

# delete session-timeouts

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete session settings

## Usage

```
delete session-timeouts [--remote]
```

## Examples

Run via SCM API:
```
arc > delete session-timeouts
```

Run directly on device via SSH:
```
arc:fw-01 > delete session-timeouts --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete session-timeouts
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
