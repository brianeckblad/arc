---
command: "delete iam access-policies"
description: "Delete an access policy"
category: iam
scope: global
---

# delete iam access-policies

**Category:** iam
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete an access policy

## Usage

```
delete iam access-policies [--remote]
```

## Examples

Run via SCM API:
```
arc > delete iam access-policies
```

Run directly on device via SSH:
```
arc:fw-01 > delete iam access-policies --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete iam access-policies
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
