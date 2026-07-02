---
command: "show session-settings"
description: "List session settings"
category: device-device-settings
scope: global
---

# show session-settings

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List session settings

## Usage

```
show session-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > show session-settings
```

Run directly on device via SSH:
```
arc:fw-01 > show session-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show session-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
