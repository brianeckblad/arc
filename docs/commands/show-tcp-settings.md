---
command: "show tcp-settings"
description: "List TCP settings"
category: device-device-settings
scope: global
---

# show tcp-settings

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List TCP settings

## Usage

```
show tcp-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > show tcp-settings
```

Run directly on device via SSH:
```
arc:fw-01 > show tcp-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show tcp-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
