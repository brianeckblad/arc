---
command: "delete ngts cert-requests approval"
description: "Delete certificate request workflow approval rule"
category: ngts
scope: global
---

# delete ngts cert-requests approval

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete certificate request workflow approval rule

## Usage

```
delete ngts cert-requests approval [--remote]
```

## Examples

Run via SCM API:
```
arc > delete ngts cert-requests approval
```

Run directly on device via SSH:
```
arc:fw-01 > delete ngts cert-requests approval --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete ngts cert-requests approval
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
