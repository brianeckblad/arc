---
command: "delete ngts certs revokes approval"
description: "Delete certificate revocation workflow approval ru"
category: ngts
scope: global
---

# delete ngts certs revokes approval

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete certificate revocation workflow approval ru

## Usage

```
delete ngts certs revokes approval [--remote]
```

## Examples

Run via SCM API:
```
arc > delete ngts certs revokes approval
```

Run directly on device via SSH:
```
arc:fw-01 > delete ngts certs revokes approval --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete ngts certs revokes approval
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
