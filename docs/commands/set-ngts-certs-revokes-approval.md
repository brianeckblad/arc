---
command: "set ngts certs revokes approval"
description: "Create an approval rule for certificate"
category: ngts
scope: global
---

# set ngts certs revokes approval

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create an approval rule for certificate

## Usage

```
set ngts certs revokes approval [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts certs revokes approval
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts certs revokes approval --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts certs revokes approval
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
