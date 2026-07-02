---
command: "show ngts plugins disablements"
description: "Retrieve all disabled plugins"
category: ngts
scope: global
---

# show ngts plugins disablements

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Retrieve all disabled plugins

## Usage

```
show ngts plugins disablements [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts plugins disablements
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts plugins disablements --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts plugins disablements
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
