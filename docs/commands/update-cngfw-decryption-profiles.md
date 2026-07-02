---
command: "update cngfw decryption-profiles"
description: "Update a decryption profile"
category: cloudngfw
scope: global
---

# update cngfw decryption-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a decryption profile

## Usage

```
update cngfw decryption-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw decryption-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw decryption-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw decryption-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
