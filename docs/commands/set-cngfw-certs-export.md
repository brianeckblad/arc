---
command: "set cngfw certs export"
description: "Export a certificate"
category: cloudngfw
scope: global
---

# set cngfw certs export

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Export a certificate

## Usage

```
set cngfw certs export [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw certs export
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw certs export --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw certs export
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
