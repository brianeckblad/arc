---
command: "show cngfw decryption-exclusions"
description: "List decryption exclusions"
category: cloudngfw
scope: global
---

# show cngfw decryption-exclusions

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List decryption exclusions

## Usage

```
show cngfw decryption-exclusions [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw decryption-exclusions
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw decryption-exclusions --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw decryption-exclusions
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
