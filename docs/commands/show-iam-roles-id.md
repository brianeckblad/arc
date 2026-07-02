---
command: "show iam roles id"
description: "Get a role"
category: iam
scope: global
---

# show iam roles id

**Category:** iam
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a role

## Usage

```
show iam roles id [--remote]
```

## Examples

Run via SCM API:
```
arc > show iam roles id
```

Run directly on device via SSH:
```
arc:fw-01 > show iam roles id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show iam roles id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
