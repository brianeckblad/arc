---
command: "show adnsr ca-certs id"
description: "Get an EDL CA certificate"
category: adnsr
scope: global
---

# show adnsr ca-certs id

**Category:** adnsr
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get an EDL CA certificate

## Usage

```
show adnsr ca-certs id [--remote]
```

## Examples

Run via SCM API:
```
arc > show adnsr ca-certs id
```

Run directly on device via SSH:
```
arc:fw-01 > show adnsr ca-certs id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show adnsr ca-certs id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
