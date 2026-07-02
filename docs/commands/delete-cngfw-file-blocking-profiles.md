---
command: "delete cngfw file-blocking-profiles"
description: "Delete a file blocking profile"
category: cloudngfw
scope: global
---

# delete cngfw file-blocking-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a file blocking profile

## Usage

```
delete cngfw file-blocking-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw file-blocking-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw file-blocking-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw file-blocking-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
