---
command: "set ngts certs retirement"
description: "Retire certificates"
category: ngts
scope: global
---

# set ngts certs retirement

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Retire certificates

## Usage

```
set ngts certs retirement [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts certs retirement
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts certs retirement --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts certs retirement
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
