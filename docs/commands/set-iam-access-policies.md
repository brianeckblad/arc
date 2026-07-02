---
command: "set iam access-policies"
description: "Assign an access policy"
category: iam
scope: global
---

# set iam access-policies

**Category:** iam
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Assign an access policy

## Usage

```
set iam access-policies [--remote]
```

## Examples

Run via SCM API:
```
arc > set iam access-policies
```

Run directly on device via SSH:
```
arc:fw-01 > set iam access-policies --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set iam access-policies
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
