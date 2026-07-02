---
command: "update cngfw decryption-rules"
description: "Update a decryption rule"
category: cloudngfw
scope: global
---

# update cngfw decryption-rules

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a decryption rule

## Usage

```
update cngfw decryption-rules [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw decryption-rules
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw decryption-rules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw decryption-rules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
