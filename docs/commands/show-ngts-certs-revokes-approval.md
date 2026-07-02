---
command: "show ngts certs revokes approval"
description: "Get all certificate revocation approval rules"
category: ngts
scope: global
---

# show ngts certs revokes approval

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get all certificate revocation approval rules

## Usage

```
show ngts certs revokes approval [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts certs revokes approval
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts certs revokes approval --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts certs revokes approval
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
