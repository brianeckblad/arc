---
command: "update ngts inventory-monitoring"
description: "Updates existing inventory monitoring configuratio"
category: ngts
scope: global
---

# update ngts inventory-monitoring

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Updates existing inventory monitoring configuratio

## Usage

```
update ngts inventory-monitoring [--remote]
```

## Examples

Run via SCM API:
```
arc > update ngts inventory-monitoring
```

Run directly on device via SSH:
```
arc:fw-01 > update ngts inventory-monitoring --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update ngts inventory-monitoring
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
