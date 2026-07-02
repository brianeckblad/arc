---
command: "show service-accounts id"
description: "Get a service account"
category: iam
scope: global
---

# show service-accounts id

**Category:** iam
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a service account

## Usage

```
show service-accounts id [--remote]
```

## Examples

Run via SCM API:
```
arc > show service-accounts id
```

Run directly on device via SSH:
```
arc:fw-01 > show service-accounts id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show service-accounts id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
