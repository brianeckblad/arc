---
command: "show iam permissions"
description: "List all access permissions"
category: iam
scope: global
---

# show iam permissions

**Category:** iam
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List all access permissions

## Usage

```
show iam permissions [--remote]
```

## Examples

Run via SCM API:
```
arc > show iam permissions
```

Run directly on device via SSH:
```
arc:fw-01 > show iam permissions --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show iam permissions
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
