---
command: "show sdwan-error-profiles id"
description: "Get an SD-WAN error correction profile"
category: network
scope: global
---

# show sdwan-error-profiles id

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get an SD-WAN error correction profile

## Usage

```
show sdwan-error-profiles id [--remote]
```

## Examples

Run via SCM API:
```
arc > show sdwan-error-profiles id
```

Run directly on device via SSH:
```
arc:fw-01 > show sdwan-error-profiles id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show sdwan-error-profiles id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
