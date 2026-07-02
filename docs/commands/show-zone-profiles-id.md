---
command: "show zone-profiles id"
description: "Get a zone protection profile"
category: network
scope: global
---

# show zone-profiles id

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a zone protection profile

## Usage

```
show zone-profiles id [--remote]
```

## Examples

Run via SCM API:
```
arc > show zone-profiles id
```

Run directly on device via SSH:
```
arc:fw-01 > show zone-profiles id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show zone-profiles id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
