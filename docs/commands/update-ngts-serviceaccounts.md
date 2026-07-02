---
command: "update ngts serviceaccounts"
description: "Updates a Service Account"
category: ngts
scope: global
---

# update ngts serviceaccounts

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Updates a Service Account

## Usage

```
update ngts serviceaccounts [--remote]
```

## Examples

Run via SCM API:
```
arc > update ngts serviceaccounts
```

Run directly on device via SSH:
```
arc:fw-01 > update ngts serviceaccounts --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update ngts serviceaccounts
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
