---
command: "set cngfw certs"
description: "Generate a certificate"
category: cloudngfw
scope: global
---

# set cngfw certs

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Generate a certificate

## Usage

```
set cngfw certs [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw certs
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw certs --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw certs
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
