---
command: "delete ngts tags values"
description: "Delete a tag value"
category: ngts
scope: global
---

# delete ngts tags values

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a tag value

## Usage

```
delete ngts tags values [--remote]
```

## Examples

Run via SCM API:
```
arc > delete ngts tags values
```

Run directly on device via SSH:
```
arc:fw-01 > delete ngts tags values --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete ngts tags values
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
