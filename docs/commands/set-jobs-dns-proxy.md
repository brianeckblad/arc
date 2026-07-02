---
command: "set jobs dns-proxy"
description: "Initiate a job to retrieve the dns proxy table from device(s)"
category: operations
scope: global
---

# set jobs dns-proxy

**Category:** operations
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Initiate a job to retrieve the dns proxy table from device(s)

## Usage

```
set jobs dns-proxy [--remote]
```

## Examples

Run via SCM API:
```
arc > set jobs dns-proxy
```

Run directly on device via SSH:
```
arc:fw-01 > set jobs dns-proxy --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set jobs dns-proxy
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
