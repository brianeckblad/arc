---
command: "show rn-license-info"
description: "Get Remote Networks License Info"
category: network
scope: global
---

# show rn-license-info

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get Remote Networks License Info

## Usage

```
show rn-license-info [--remote]
```

## Examples

Run via SCM API:
```
arc > show rn-license-info
```

Run directly on device via SSH:
```
arc:fw-01 > show rn-license-info --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show rn-license-info
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
