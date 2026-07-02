---
command: "set ngts credentials"
description: "Add a set of new shared"
category: ngts
scope: global
---

# set ngts credentials

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Add a set of new shared

## Usage

```
set ngts credentials [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts credentials
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts credentials --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts credentials
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
