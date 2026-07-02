---
command: "set ngts certs recovery"
description: "Recover a set of certificates"
category: ngts
scope: global
---

# set ngts certs recovery

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Recover a set of certificates

## Usage

```
set ngts certs recovery [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts certs recovery
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts certs recovery --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts certs recovery
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
