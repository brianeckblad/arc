---
command: "show session-timeouts id"
description: "Get existing session settings"
category: device-device-settings
scope: global
---

# show session-timeouts id

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get existing session settings

## Usage

```
show session-timeouts id [--remote]
```

## Examples

Run via SCM API:
```
arc > show session-timeouts id
```

Run directly on device via SSH:
```
arc:fw-01 > show session-timeouts id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show session-timeouts id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
