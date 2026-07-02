---
command: "set ngts cert-requests approval bulk"
description: "Approve or reject multiple pending approval"
category: ngts
scope: global
---

# set ngts cert-requests approval bulk

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Approve or reject multiple pending approval

## Usage

```
set ngts cert-requests approval bulk [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts cert-requests approval bulk
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts cert-requests approval bulk --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts cert-requests approval bulk
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
