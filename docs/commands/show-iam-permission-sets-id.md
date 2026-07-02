---
command: "show iam permission-sets id"
description: "Get a permission set"
category: iam
scope: global
---

# show iam permission-sets id

**Category:** iam
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a permission set

## Usage

```
show iam permission-sets id [--remote]
```

## Examples

Run via SCM API:
```
arc > show iam permission-sets id
```

Run directly on device via SSH:
```
arc:fw-01 > show iam permission-sets id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show iam permission-sets id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
