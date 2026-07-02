---
command: "set ngts cert-instances validation"
description: "Request validation for a set of"
category: ngts
scope: global
---

# set ngts cert-instances validation

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Request validation for a set of

## Usage

```
set ngts cert-instances validation [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts cert-instances validation
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts cert-instances validation --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts cert-instances validation
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
