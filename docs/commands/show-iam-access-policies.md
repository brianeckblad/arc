---
command: "show iam access-policies"
description: "List all access policies"
category: iam
scope: global
---

# show iam access-policies

**Category:** iam
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List all access policies

## Usage

```
show iam access-policies [--remote]
```

## Examples

Run via SCM API:
```
arc > show iam access-policies
```

Run directly on device via SSH:
```
arc:fw-01 > show iam access-policies --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show iam access-policies
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
