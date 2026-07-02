---
command: "set ngts plugins disablements"
description: "Disable a plugin"
category: ngts
scope: global
---

# set ngts plugins disablements

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Disable a plugin

## Usage

```
set ngts plugins disablements [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts plugins disablements
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts plugins disablements --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts plugins disablements
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
