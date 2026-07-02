---
command: "show iam sso-users"
description: "Verify a user account"
category: iam
scope: global
---

# show iam sso-users

**Category:** iam
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Verify a user account

## Usage

```
show iam sso-users [--remote]
```

## Examples

Run via SCM API:
```
arc > show iam sso-users
```

Run directly on device via SSH:
```
arc:fw-01 > show iam sso-users --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show iam sso-users
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
