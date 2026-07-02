---
command: "update iam custom-roles"
description: "Update a Custom Role"
category: iam
scope: global
---

# update iam custom-roles

**Category:** iam
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a Custom Role

## Usage

```
update iam custom-roles [--remote]
```

## Examples

Run via SCM API:
```
arc > update iam custom-roles
```

Run directly on device via SSH:
```
arc:fw-01 > update iam custom-roles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update iam custom-roles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
