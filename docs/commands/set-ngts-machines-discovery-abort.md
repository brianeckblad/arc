---
command: "set ngts machines discovery abort"
description: "Abort machine discovery"
category: ngts
scope: global
---

# set ngts machines discovery abort

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Abort machine discovery

## Usage

```
set ngts machines discovery abort [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts machines discovery abort
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts machines discovery abort --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts machines discovery abort
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
