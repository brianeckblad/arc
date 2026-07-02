---
command: "show sase locations"
description: "List locations"
category: sase
scope: global
---

# show sase locations

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List locations

## Usage

```
show sase locations [--remote]
```

## Examples

Run via SCM API:
```
arc > show sase locations
```

Run directly on device via SSH:
```
arc:fw-01 > show sase locations --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show sase locations
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
