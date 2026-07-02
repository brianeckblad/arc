---
command: "show sdwan-rules id"
description: "Get an SD-WAN rule"
category: network
scope: global
---

# show sdwan-rules id

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get an SD-WAN rule

## Usage

```
show sdwan-rules id [--remote]
```

## Examples

Run via SCM API:
```
arc > show sdwan-rules id
```

Run directly on device via SSH:
```
arc:fw-01 > show sdwan-rules id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show sdwan-rules id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
