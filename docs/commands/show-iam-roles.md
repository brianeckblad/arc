---
command: "show iam roles"
description: "List all roles"
category: iam
scope: global
---

# show iam roles

**Category:** iam
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List all roles

## Usage

```
show iam roles [--remote]
```

## Examples

Run via SCM API:
```
arc > show iam roles
```

Run directly on device via SSH:
```
arc:fw-01 > show iam roles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show iam roles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
