---
command: "delete service-accounts"
description: "Delete a service account"
category: iam
scope: global
---

# delete service-accounts

**Category:** iam
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a service account

## Usage

```
delete service-accounts [--remote]
```

## Examples

Run via SCM API:
```
arc > delete service-accounts
```

Run directly on device via SSH:
```
arc:fw-01 > delete service-accounts --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete service-accounts
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
