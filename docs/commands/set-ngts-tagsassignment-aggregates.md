---
command: "set ngts tagsassignment aggregates"
description: "Bulk operation to retrieve number of"
category: ngts
scope: global
---

# set ngts tagsassignment aggregates

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Bulk operation to retrieve number of

## Usage

```
set ngts tagsassignment aggregates [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts tagsassignment aggregates
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts tagsassignment aggregates --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts tagsassignment aggregates
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
