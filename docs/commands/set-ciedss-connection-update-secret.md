---
command: "set ciedss connection update-secret"
description: "Update directory connection client secret"
category: ciedss
scope: global
---

# set ciedss connection update-secret

**Category:** ciedss
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update directory connection client secret

## Usage

```
set ciedss connection update-secret [--remote]
```

## Examples

Run via SCM API:
```
arc > set ciedss connection update-secret
```

Run directly on device via SSH:
```
arc:fw-01 > set ciedss connection update-secret --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ciedss connection update-secret
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
