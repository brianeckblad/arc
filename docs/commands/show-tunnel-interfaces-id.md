---
command: "show tunnel-interfaces id"
description: "Get a tunnel interface"
category: network
scope: global
---

# show tunnel-interfaces id

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a tunnel interface

## Usage

```
show tunnel-interfaces id [--remote]
```

## Examples

Run via SCM API:
```
arc > show tunnel-interfaces id
```

Run directly on device via SSH:
```
arc:fw-01 > show tunnel-interfaces id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show tunnel-interfaces id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
