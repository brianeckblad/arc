---
command: "delete cngfw certs"
description: "Delete a certificate"
category: cloudngfw
scope: global
---

# delete cngfw certs

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a certificate

## Usage

```
delete cngfw certs [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw certs
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw certs --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw certs
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
