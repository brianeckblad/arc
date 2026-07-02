---
command: "set ngts serviceaccounts"
description: "Creates a Service Account"
category: ngts
scope: global
---

# set ngts serviceaccounts

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Creates a Service Account

## Usage

```
set ngts serviceaccounts [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts serviceaccounts
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts serviceaccounts --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts serviceaccounts
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
