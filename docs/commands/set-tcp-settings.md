---
command: "set tcp-settings"
description: "Create TCP settings"
category: device-device-settings
scope: global
---

# set tcp-settings

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create TCP settings

## Usage

```
set tcp-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > set tcp-settings
```

Run directly on device via SSH:
```
arc:fw-01 > set tcp-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set tcp-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
