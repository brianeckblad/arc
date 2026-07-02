---
command: "delete ngts serviceaccounts"
description: "Deletes a Service Account"
category: ngts
scope: global
---

# delete ngts serviceaccounts

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Deletes a Service Account

## Usage

```
delete ngts serviceaccounts [--remote]
```

## Examples

Run via SCM API:
```
arc > delete ngts serviceaccounts
```

Run directly on device via SSH:
```
arc:fw-01 > delete ngts serviceaccounts --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete ngts serviceaccounts
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
