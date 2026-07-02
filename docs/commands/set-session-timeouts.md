---
command: "set session-timeouts"
description: "Create session timeouts settings"
category: device-device-settings
scope: global
---

# set session-timeouts

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create session timeouts settings

## Usage

```
set session-timeouts [--remote]
```

## Examples

Run via SCM API:
```
arc > set session-timeouts
```

Run directly on device via SSH:
```
arc:fw-01 > set session-timeouts --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set session-timeouts
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
