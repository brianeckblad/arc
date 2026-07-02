---
command: "show posture reports bpa-result id"
description: "Get BPA Processing Status"
category: posture
scope: global
---

# show posture reports bpa-result id

**Category:** posture
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get BPA Processing Status

## Usage

```
show posture reports bpa-result id [--remote]
```

## Examples

Run via SCM API:
```
arc > show posture reports bpa-result id
```

Run directly on device via SSH:
```
arc:fw-01 > show posture reports bpa-result id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show posture reports bpa-result id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
