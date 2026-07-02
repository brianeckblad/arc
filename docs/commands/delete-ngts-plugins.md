---
command: "delete ngts plugins"
description: "Delete a local plugin"
category: ngts
scope: global
---

# delete ngts plugins

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a local plugin

## Usage

```
delete ngts plugins [--remote]
```

## Examples

Run via SCM API:
```
arc > delete ngts plugins
```

Run directly on device via SSH:
```
arc:fw-01 > delete ngts plugins --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete ngts plugins
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
