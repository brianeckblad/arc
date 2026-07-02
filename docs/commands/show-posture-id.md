---
command: "show posture id"
description: "Get Posture Check"
category: posture
scope: global
---

# show posture id

**Category:** posture
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get Posture Check

## Usage

```
show posture id [--remote]
```

## Examples

Run via SCM API:
```
arc > show posture id
```

Run directly on device via SSH:
```
arc:fw-01 > show posture id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show posture id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
