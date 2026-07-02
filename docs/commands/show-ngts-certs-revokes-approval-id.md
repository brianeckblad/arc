---
command: "show ngts certs revokes approval id"
description: "Retrieve certificate revocation approval rule by"
category: ngts
scope: global
---

# show ngts certs revokes approval id

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Retrieve certificate revocation approval rule by

## Usage

```
show ngts certs revokes approval id [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts certs revokes approval id
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts certs revokes approval id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts certs revokes approval id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
