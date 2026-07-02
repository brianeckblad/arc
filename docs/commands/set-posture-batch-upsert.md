---
command: "set posture batch-upsert"
description: "Batch Upsert Posture Checks"
category: posture
scope: global
---

# set posture batch-upsert

**Category:** posture
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Batch Upsert Posture Checks

## Usage

```
set posture batch-upsert [--remote]
```

## Examples

Run via SCM API:
```
arc > set posture batch-upsert
```

Run directly on device via SSH:
```
arc:fw-01 > set posture batch-upsert --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set posture batch-upsert
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
