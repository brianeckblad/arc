---
command: "update cngfw decryption-exclusions"
description: "Update a decryption exclusion"
category: cloudngfw
scope: global
---

# update cngfw decryption-exclusions

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a decryption exclusion

## Usage

```
update cngfw decryption-exclusions [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw decryption-exclusions
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw decryption-exclusions --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw decryption-exclusions
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
