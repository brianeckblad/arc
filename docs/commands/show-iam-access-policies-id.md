---
command: "show iam access-policies id"
description: "Get an access policy"
category: iam
scope: global
---

# show iam access-policies id

**Category:** iam
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get an access policy

## Usage

```
show iam access-policies id [--remote]
```

## Examples

Run via SCM API:
```
arc > show iam access-policies id
```

Run directly on device via SSH:
```
arc:fw-01 > show iam access-policies id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show iam access-policies id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
