---
command: "delete ngts machines"
description: "Delete a machine"
category: ngts
scope: global
---

# delete ngts machines

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a machine

## Usage

```
delete ngts machines [--remote]
```

## Examples

Run via SCM API:
```
arc > delete ngts machines
```

Run directly on device via SSH:
```
arc:fw-01 > delete ngts machines --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete ngts machines
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
