---
command: "show aggregate-interfaces id"
description: "Get an Aggregate Interface"
category: network
scope: global
---

# show aggregate-interfaces id

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get an Aggregate Interface

## Usage

```
show aggregate-interfaces id [--remote]
```

## Examples

Run via SCM API:
```
arc > show aggregate-interfaces id
```

Run directly on device via SSH:
```
arc:fw-01 > show aggregate-interfaces id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show aggregate-interfaces id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
