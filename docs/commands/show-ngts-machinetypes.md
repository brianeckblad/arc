---
command: "show ngts machinetypes"
description: "List Machine Types"
category: ngts
scope: global
---

# show ngts machinetypes

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List Machine Types

## Usage

```
show ngts machinetypes [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts machinetypes
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts machinetypes --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts machinetypes
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
