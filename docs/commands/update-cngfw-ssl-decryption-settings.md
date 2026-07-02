---
command: "update cngfw ssl-decryption-settings"
description: "PUT Ssl Decryption Settings"
category: cloudngfw
scope: global
---

# update cngfw ssl-decryption-settings

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

PUT Ssl Decryption Settings

## Usage

```
update cngfw ssl-decryption-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw ssl-decryption-settings
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw ssl-decryption-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw ssl-decryption-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
