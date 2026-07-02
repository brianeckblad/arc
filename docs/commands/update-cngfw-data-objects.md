---
command: "update cngfw data-objects"
description: "Update Data Object by ID"
category: cloudngfw
scope: global
---

# update cngfw data-objects

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update Data Object by ID

## Usage

```
update cngfw data-objects [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw data-objects
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw data-objects --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw data-objects
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
