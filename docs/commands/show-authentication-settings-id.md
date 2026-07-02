---
command: "show authentication-settings id"
description: "Get existing authentication settings"
category: device-device-settings
scope: global
---

# show authentication-settings id

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get existing authentication settings

## Usage

```
show authentication-settings id [--remote]
```

## Examples

Run via SCM API:
```
arc > show authentication-settings id
```

Run directly on device via SSH:
```
arc:fw-01 > show authentication-settings id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show authentication-settings id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
