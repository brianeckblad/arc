---
command: "update service-accounts"
description: "Update a service account"
category: iam
scope: global
---

# update service-accounts

**Category:** iam
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a service account

## Usage

```
update service-accounts [--remote]
```

## Examples

Run via SCM API:
```
arc > update service-accounts
```

Run directly on device via SSH:
```
arc:fw-01 > update service-accounts --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update service-accounts
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
