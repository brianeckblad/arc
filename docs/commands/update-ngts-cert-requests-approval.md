---
command: "update ngts cert-requests approval"
description: "Update certificate request workflow approval rule"
category: ngts
scope: global
---

# update ngts cert-requests approval

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update certificate request workflow approval rule

## Usage

```
update ngts cert-requests approval [--remote]
```

## Examples

Run via SCM API:
```
arc > update ngts cert-requests approval
```

Run directly on device via SSH:
```
arc:fw-01 > update ngts cert-requests approval --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update ngts cert-requests approval
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
