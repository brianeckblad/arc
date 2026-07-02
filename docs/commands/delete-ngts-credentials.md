---
command: "delete ngts credentials"
description: "Delete shared credentials"
category: ngts
scope: global
---

# delete ngts credentials

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete shared credentials

## Usage

```
delete ngts credentials [--remote]
```

## Examples

Run via SCM API:
```
arc > delete ngts credentials
```

Run directly on device via SSH:
```
arc:fw-01 > delete ngts credentials --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete ngts credentials
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
