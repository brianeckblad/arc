---
command: "show iam permissions id"
description: "Get a permission"
category: iam
scope: global
---

# show iam permissions id

**Category:** iam
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a permission

## Usage

```
show iam permissions id [--remote]
```

## Examples

Run via SCM API:
```
arc > show iam permissions id
```

Run directly on device via SSH:
```
arc:fw-01 > show iam permissions id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show iam permissions id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
