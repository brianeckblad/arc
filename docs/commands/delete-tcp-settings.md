---
command: "delete tcp-settings"
description: "Delete TCP settings"
category: device-device-settings
scope: global
---

# delete tcp-settings

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete TCP settings

## Usage

```
delete tcp-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > delete tcp-settings
```

Run directly on device via SSH:
```
arc:fw-01 > delete tcp-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete tcp-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
