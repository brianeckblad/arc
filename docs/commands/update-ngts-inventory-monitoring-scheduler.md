---
command: "update ngts inventory-monitoring scheduler"
description: "Update inventory monitoring scheduler by type"
category: ngts
scope: global
---

# update ngts inventory-monitoring scheduler

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update inventory monitoring scheduler by type

## Usage

```
update ngts inventory-monitoring scheduler [--remote]
```

## Examples

Run via SCM API:
```
arc > update ngts inventory-monitoring scheduler
```

Run directly on device via SSH:
```
arc:fw-01 > update ngts inventory-monitoring scheduler --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update ngts inventory-monitoring scheduler
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
