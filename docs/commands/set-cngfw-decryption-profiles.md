---
command: "set cngfw decryption-profiles"
description: "Create a decryption profile"
category: cloudngfw
scope: global
---

# set cngfw decryption-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a decryption profile

## Usage

```
set cngfw decryption-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw decryption-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw decryption-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw decryption-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
