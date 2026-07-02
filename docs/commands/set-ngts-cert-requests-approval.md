---
command: "set ngts cert-requests approval"
description: "Approve or reject pending certificate request"
category: ngts
scope: global
---

# set ngts cert-requests approval

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Approve or reject pending certificate request

## Usage

```
set ngts cert-requests approval [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts cert-requests approval
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts cert-requests approval --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts cert-requests approval
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
