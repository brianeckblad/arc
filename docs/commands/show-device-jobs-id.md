---
command: "show device jobs id"
description: "Retrieve job status and results, running on a device"
category: operations
scope: global
---

# show device jobs id

**Category:** operations
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Retrieve job status and results, running on a device

## Usage

```
show device jobs id [--remote]
```

## Examples

Run via SCM API:
```
arc > show device jobs id
```

Run directly on device via SSH:
```
arc:fw-01 > show device jobs id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show device jobs id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
