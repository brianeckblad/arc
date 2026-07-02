---
command: "show sase bandwidth-allocations"
description: "List bandwidth regions"
category: sase
scope: global
---

# show sase bandwidth-allocations

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List bandwidth regions

## Usage

```
show sase bandwidth-allocations [--remote]
```

## Examples

Run via SCM API:
```
arc > show sase bandwidth-allocations
```

Run directly on device via SSH:
```
arc:fw-01 > show sase bandwidth-allocations --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show sase bandwidth-allocations
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
