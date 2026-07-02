---
command: "show adnsr ca-certs"
description: "List EDL CA certificates"
category: adnsr
scope: global
---

# show adnsr ca-certs

**Category:** adnsr
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List EDL CA certificates

## Usage

```
show adnsr ca-certs [--remote]
```

## Examples

Run via SCM API:
```
arc > show adnsr ca-certs
```

Run directly on device via SSH:
```
arc:fw-01 > show adnsr ca-certs --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show adnsr ca-certs
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
