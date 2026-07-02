---
command: "delete iam custom-roles"
description: "Delete a custom role"
category: iam
scope: global
---

# delete iam custom-roles

**Category:** iam
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a custom role

## Usage

```
delete iam custom-roles [--remote]
```

## Examples

Run via SCM API:
```
arc > delete iam custom-roles
```

Run directly on device via SSH:
```
arc:fw-01 > delete iam custom-roles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete iam custom-roles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
