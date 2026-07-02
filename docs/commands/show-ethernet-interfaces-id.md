---
command: "show ethernet-interfaces id"
description: "Get an ethernet interface"
category: network
scope: global
---

# show ethernet-interfaces id

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get an ethernet interface

## Usage

```
show ethernet-interfaces id [--remote]
```

## Examples

Run via SCM API:
```
arc > show ethernet-interfaces id
```

Run directly on device via SSH:
```
arc:fw-01 > show ethernet-interfaces id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ethernet-interfaces id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
