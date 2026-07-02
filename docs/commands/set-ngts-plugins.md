---
command: "set ngts plugins"
description: "Create a local plugin"
category: ngts
scope: global
---

# set ngts plugins

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a local plugin

## Usage

```
set ngts plugins [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts plugins
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts plugins --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts plugins
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
