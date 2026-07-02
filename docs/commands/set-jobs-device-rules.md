---
command: "set jobs device-rules"
description: "Initiate a job to retrieve rules on one or more device(s)"
category: operations
scope: global
---

# set jobs device-rules

**Category:** operations
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Initiate a job to retrieve rules on one or more device(s)

## Usage

```
set jobs device-rules [--remote]
```

## Examples

Run via SCM API:
```
arc > set jobs device-rules
```

Run directly on device via SSH:
```
arc:fw-01 > set jobs device-rules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set jobs device-rules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
