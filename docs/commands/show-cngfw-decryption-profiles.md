---
command: "show cngfw decryption-profiles"
description: "List decryption profiles"
category: cloudngfw
scope: global
---

# show cngfw decryption-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List decryption profiles

## Usage

```
show cngfw decryption-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw decryption-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw decryption-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw decryption-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
