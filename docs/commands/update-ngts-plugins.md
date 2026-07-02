---
command: "update ngts plugins"
description: "Update a local plugin"
category: ngts
scope: global
---

# update ngts plugins

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a local plugin

## Usage

```
update ngts plugins [--remote]
```

## Examples

Run via SCM API:
```
arc > update ngts plugins
```

Run directly on device via SSH:
```
arc:fw-01 > update ngts plugins --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update ngts plugins
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
