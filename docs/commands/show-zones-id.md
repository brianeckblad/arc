---
command: "show zones id"
description: "Get a security zone"
category: network
scope: global
---

# show zones id

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a security zone

## Usage

```
show zones id [--remote]
```

## Examples

Run via SCM API:
```
arc > show zones id
```

Run directly on device via SSH:
```
arc:fw-01 > show zones id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show zones id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
