---
command: "set ngts machines"
description: "Add a machine"
category: ngts
scope: global
---

# set ngts machines

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Add a machine

## Usage

```
set ngts machines [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts machines
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts machines --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts machines
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
