---
command: "show ngts edgeworkers"
description: "Retrieve Satellite Workers"
category: ngts
scope: global
---

# show ngts edgeworkers

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Retrieve Satellite Workers

## Usage

```
show ngts edgeworkers [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts edgeworkers
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts edgeworkers --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts edgeworkers
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
