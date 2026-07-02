---
command: "set posture batch-delete"
description: "Batch Delete Posture Checks"
category: posture
scope: global
---

# set posture batch-delete

**Category:** posture
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Batch Delete Posture Checks

## Usage

```
set posture batch-delete [--remote]
```

## Examples

Run via SCM API:
```
arc > set posture batch-delete
```

Run directly on device via SSH:
```
arc:fw-01 > set posture batch-delete --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set posture batch-delete
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
