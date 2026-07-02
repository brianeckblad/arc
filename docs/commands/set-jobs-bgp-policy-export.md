---
command: "set jobs bgp-policy-export"
description: "Initiate a job for BGP Policy Export from device(s)"
category: operations
scope: global
---

# set jobs bgp-policy-export

**Category:** operations
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Initiate a job for BGP Policy Export from device(s)

## Usage

```
set jobs bgp-policy-export [--remote]
```

## Examples

Run via SCM API:
```
arc > set jobs bgp-policy-export
```

Run directly on device via SSH:
```
arc:fw-01 > set jobs bgp-policy-export --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set jobs bgp-policy-export
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
