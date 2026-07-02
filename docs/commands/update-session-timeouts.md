---
command: "update session-timeouts"
description: "Update session settings"
category: device-device-settings
scope: global
---

# update session-timeouts

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update session settings

## Usage

```
update session-timeouts [--remote]
```

## Examples

Run via SCM API:
```
arc > update session-timeouts
```

Run directly on device via SSH:
```
arc:fw-01 > update session-timeouts --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update session-timeouts
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
