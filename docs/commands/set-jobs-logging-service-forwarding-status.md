---
command: "set jobs logging-service-forwarding-status"
description: "Initiate a job to request logging service forwarding status for device(s)"
category: operations
scope: global
---

# set jobs logging-service-forwarding-status

**Category:** operations
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Initiate a job to request logging service forwarding status for device(s)

## Usage

```
set jobs logging-service-forwarding-status [--remote]
```

## Examples

Run via SCM API:
```
arc > set jobs logging-service-forwarding-status
```

Run directly on device via SSH:
```
arc:fw-01 > set jobs logging-service-forwarding-status --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set jobs logging-service-forwarding-status
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
