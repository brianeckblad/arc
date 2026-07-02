---
command: "delete ngts plugins disablements"
description: "Remove plugin disablement"
category: ngts
scope: global
---

# delete ngts plugins disablements

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Remove plugin disablement

## Usage

```
delete ngts plugins disablements [--remote]
```

## Examples

Run via SCM API:
```
arc > delete ngts plugins disablements
```

Run directly on device via SSH:
```
arc:fw-01 > delete ngts plugins disablements --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete ngts plugins disablements
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
