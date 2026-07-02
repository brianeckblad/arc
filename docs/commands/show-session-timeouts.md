---
command: "show session-timeouts"
description: "List session timeouts settings"
category: device-device-settings
scope: global
---

# show session-timeouts

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List session timeouts settings

## Usage

```
show session-timeouts [--remote]
```

## Examples

Run via SCM API:
```
arc > show session-timeouts
```

Run directly on device via SSH:
```
arc:fw-01 > show session-timeouts --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show session-timeouts
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
