---
command: "show iam permission-sets"
description: "List permission sets"
category: iam
scope: global
---

# show iam permission-sets

**Category:** iam
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List permission sets

## Usage

```
show iam permission-sets [--remote]
```

## Examples

Run via SCM API:
```
arc > show iam permission-sets
```

Run directly on device via SSH:
```
arc:fw-01 > show iam permission-sets --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show iam permission-sets
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
