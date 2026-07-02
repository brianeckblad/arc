---
command: "delete cngfw certificate-profiles"
description: "Delete a certificate profile"
category: cloudngfw
scope: global
---

# delete cngfw certificate-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a certificate profile

## Usage

```
delete cngfw certificate-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw certificate-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw certificate-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw certificate-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
