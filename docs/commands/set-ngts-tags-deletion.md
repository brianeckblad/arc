---
command: "set ngts tags deletion"
description: "Delete tags in bulk"
category: ngts
scope: global
---

# set ngts tags deletion

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete tags in bulk

## Usage

```
set ngts tags deletion [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts tags deletion
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts tags deletion --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts tags deletion
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
