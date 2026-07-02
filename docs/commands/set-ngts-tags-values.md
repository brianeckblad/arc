---
command: "set ngts tags values"
description: "Create tag values"
category: ngts
scope: global
---

# set ngts tags values

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create tag values

## Usage

```
set ngts tags values [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts tags values
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts tags values --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts tags values
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
