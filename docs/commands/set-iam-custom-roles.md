---
command: "set iam custom-roles"
description: "Create a custom role"
category: iam
scope: global
---

# set iam custom-roles

**Category:** iam
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a custom role

## Usage

```
set iam custom-roles [--remote]
```

## Examples

Run via SCM API:
```
arc > set iam custom-roles
```

Run directly on device via SSH:
```
arc:fw-01 > set iam custom-roles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set iam custom-roles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
