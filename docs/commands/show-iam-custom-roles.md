---
command: "show iam custom-roles"
description: "List custom roles"
category: iam
scope: global
---

# show iam custom-roles

**Category:** iam
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List custom roles

## Usage

```
show iam custom-roles [--remote]
```

## Examples

Run via SCM API:
```
arc > show iam custom-roles
```

Run directly on device via SSH:
```
arc:fw-01 > show iam custom-roles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show iam custom-roles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
