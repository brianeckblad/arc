---
command: "show sdwan-path-profiles id"
description: "Get an SD-WAN path quality profile"
category: network
scope: global
---

# show sdwan-path-profiles id

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get an SD-WAN path quality profile

## Usage

```
show sdwan-path-profiles id [--remote]
```

## Examples

Run via SCM API:
```
arc > show sdwan-path-profiles id
```

Run directly on device via SSH:
```
arc:fw-01 > show sdwan-path-profiles id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show sdwan-path-profiles id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
