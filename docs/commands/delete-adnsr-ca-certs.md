---
command: "delete adnsr ca-certs"
description: "Delete an EDL CA certificate"
category: adnsr
scope: global
---

# delete adnsr ca-certs

**Category:** adnsr
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete an EDL CA certificate

## Usage

```
delete adnsr ca-certs [--remote]
```

## Examples

Run via SCM API:
```
arc > delete adnsr ca-certs
```

Run directly on device via SSH:
```
arc:fw-01 > delete adnsr ca-certs --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete adnsr ca-certs
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
