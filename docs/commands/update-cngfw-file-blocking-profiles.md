---
command: "update cngfw file-blocking-profiles"
description: "Update a file blocking profile"
category: cloudngfw
scope: global
---

# update cngfw file-blocking-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a file blocking profile

## Usage

```
update cngfw file-blocking-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw file-blocking-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw file-blocking-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw file-blocking-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
