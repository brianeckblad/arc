---
command: "set cngfw certs import"
description: "Import a certificate"
category: cloudngfw
scope: global
---

# set cngfw certs import

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Import a certificate

## Usage

```
set cngfw certs import [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw certs import
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw certs import --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw certs import
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
