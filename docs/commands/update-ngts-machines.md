---
command: "update ngts machines"
description: "Update a machine details"
category: ngts
scope: global
---

# update ngts machines

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a machine details

## Usage

```
update ngts machines [--remote]
```

## Examples

Run via SCM API:
```
arc > update ngts machines
```

Run directly on device via SSH:
```
arc:fw-01 > update ngts machines --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update ngts machines
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
