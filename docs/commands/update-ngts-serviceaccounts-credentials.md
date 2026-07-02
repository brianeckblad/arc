---
command: "update ngts serviceaccounts credentials"
description: "Updates a Service Account credentials"
category: ngts
scope: global
---

# update ngts serviceaccounts credentials

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Updates a Service Account credentials

## Usage

```
update ngts serviceaccounts credentials [--remote]
```

## Examples

Run via SCM API:
```
arc > update ngts serviceaccounts credentials
```

Run directly on device via SSH:
```
arc:fw-01 > update ngts serviceaccounts credentials --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update ngts serviceaccounts credentials
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
