---
command: "show nat-rules id"
description: "Get a NAT rule"
category: network
scope: global
---

# show nat-rules id

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a NAT rule

## Usage

```
show nat-rules id [--remote]
```

## Examples

Run via SCM API:
```
arc > show nat-rules id
```

Run directly on device via SSH:
```
arc:fw-01 > show nat-rules id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show nat-rules id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
