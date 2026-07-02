---
command: "show ngts plugins"
description: "Retrieve all plugins"
category: ngts
scope: global
---

# show ngts plugins

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Retrieve all plugins

## Usage

```
show ngts plugins [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts plugins
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts plugins --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts plugins
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
