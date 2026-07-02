---
command: "set cngfw certificate-profiles"
description: "Create a certificate profile"
category: cloudngfw
scope: global
---

# set cngfw certificate-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a certificate profile

## Usage

```
set cngfw certificate-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw certificate-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw certificate-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw certificate-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
