---
command: "show ngts serviceaccounts"
description: "Retrieves all the Service Accounts the"
category: ngts
scope: global
---

# show ngts serviceaccounts

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Retrieves all the Service Accounts the

## Usage

```
show ngts serviceaccounts [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts serviceaccounts
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts serviceaccounts --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts serviceaccounts
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
