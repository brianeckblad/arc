---
command: "delete cngfw data-objects"
description: "Delete Data Object by ID"
category: cloudngfw
scope: global
---

# delete cngfw data-objects

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete Data Object by ID

## Usage

```
delete cngfw data-objects [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw data-objects
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw data-objects --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw data-objects
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
