---
command: "set adnsr ca-certs upload"
description: "Upload an EDL CA certificate from file"
category: adnsr
scope: global
---

# set adnsr ca-certs upload

**Category:** adnsr
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Upload an EDL CA certificate from file

## Usage

```
set adnsr ca-certs upload [--remote]
```

## Examples

Run via SCM API:
```
arc > set adnsr ca-certs upload
```

Run directly on device via SSH:
```
arc:fw-01 > set adnsr ca-certs upload --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set adnsr ca-certs upload
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
