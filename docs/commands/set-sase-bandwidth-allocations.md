---
command: "set sase bandwidth-allocations"
description: "Create a bandwidth allocation"
category: sase
scope: global
---

# set sase bandwidth-allocations

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a bandwidth allocation

## Usage

```
set sase bandwidth-allocations [--remote]
```

## Examples

Run via SCM API:
```
arc > set sase bandwidth-allocations
```

Run directly on device via SSH:
```
arc:fw-01 > set sase bandwidth-allocations --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set sase bandwidth-allocations
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
