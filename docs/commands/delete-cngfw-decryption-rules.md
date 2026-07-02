---
command: "delete cngfw decryption-rules"
description: "Delete a decryption rule"
category: cloudngfw
scope: global
---

# delete cngfw decryption-rules

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a decryption rule

## Usage

```
delete cngfw decryption-rules [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw decryption-rules
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw decryption-rules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw decryption-rules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
