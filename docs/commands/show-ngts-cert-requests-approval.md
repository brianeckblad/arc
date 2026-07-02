---
command: "show ngts cert-requests approval"
description: "Get all approval rules"
category: ngts
scope: global
---

# show ngts cert-requests approval

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get all approval rules

## Usage

```
show ngts cert-requests approval [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts cert-requests approval
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts cert-requests approval --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts cert-requests approval
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
