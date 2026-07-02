---
command: "delete cngfw decryption-exclusions"
description: "Delete a decryption exclusion"
category: cloudngfw
scope: global
---

# delete cngfw decryption-exclusions

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a decryption exclusion

## Usage

```
delete cngfw decryption-exclusions [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw decryption-exclusions
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw decryption-exclusions --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw decryption-exclusions
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
