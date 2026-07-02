---
command: "show authentication-settings"
description: "List authentication settings"
category: device-device-settings
scope: global
---

# show authentication-settings

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List authentication settings

## Usage

```
show authentication-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > show authentication-settings
```

Run directly on device via SSH:
```
arc:fw-01 > show authentication-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show authentication-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
