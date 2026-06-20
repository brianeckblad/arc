---
command: "request system shutdown"
description: "Shut down a managed device (CAUTION: device will go offline)"
usage: "request system shutdown  (use --remote)"
feature_flag: request_system_reboot
category: operations
scope: device
api: "(live device state — SSH via --remote)"
---

# request system shutdown

**Category:** operations
**API mode:** ✓ Live SCM data
**SSH mode:** `request system shutdown`

## Description

Shut down a managed device — use --remote  (CAUTION: device will go offline)

## Usage

```
request system shutdown [--remote]
```

## Examples

Run via SCM API:
```
arc > request system shutdown
```

Run directly on device via SSH:
```
arc:fw-01 > request system shutdown --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > request system shutdown
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
