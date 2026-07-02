---
command: "set session-settings"
description: "Create session settings"
category: device-device-settings
scope: global
---

# set session-settings

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create session settings

## Usage

```
set session-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > set session-settings
```

Run directly on device via SSH:
```
arc:fw-01 > set session-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set session-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
