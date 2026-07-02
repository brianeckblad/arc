---
command: "show service-accounts"
description: "List all service accounts"
category: iam
scope: global
---

# show service-accounts

**Category:** iam
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List all service accounts

## Usage

```
show service-accounts [--remote]
```

## Examples

Run via SCM API:
```
arc > show service-accounts
```

Run directly on device via SSH:
```
arc:fw-01 > show service-accounts --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show service-accounts
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
