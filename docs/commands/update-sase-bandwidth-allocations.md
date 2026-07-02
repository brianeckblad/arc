---
command: "update sase bandwidth-allocations"
description: "Update a bandwidth allocation"
category: sase
scope: global
---

# update sase bandwidth-allocations

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a bandwidth allocation

## Usage

```
update sase bandwidth-allocations [--remote]
```

## Examples

Run via SCM API:
```
arc > update sase bandwidth-allocations
```

Run directly on device via SSH:
```
arc:fw-01 > update sase bandwidth-allocations --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update sase bandwidth-allocations
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
