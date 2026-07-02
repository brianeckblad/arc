---
command: "set iam sso-users"
description: "Create an SSO account"
category: iam
scope: global
---

# set iam sso-users

**Category:** iam
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create an SSO account

## Usage

```
set iam sso-users [--remote]
```

## Examples

Run via SCM API:
```
arc > set iam sso-users
```

Run directly on device via SSH:
```
arc:fw-01 > set iam sso-users --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set iam sso-users
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
