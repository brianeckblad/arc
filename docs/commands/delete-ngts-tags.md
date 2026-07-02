---
command: "delete ngts tags"
description: "Delete tag by name"
category: ngts
scope: global
---

# delete ngts tags

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete tag by name

## Usage

```
delete ngts tags [--remote]
```

## Examples

Run via SCM API:
```
arc > delete ngts tags
```

Run directly on device via SSH:
```
arc:fw-01 > delete ngts tags --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete ngts tags
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
