---
command: "set cngfw ssl-decryption-settings"
description: "POST Ssl Decryption Settings"
category: cloudngfw
scope: global
---

# set cngfw ssl-decryption-settings

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

POST Ssl Decryption Settings

## Usage

```
set cngfw ssl-decryption-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw ssl-decryption-settings
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw ssl-decryption-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw ssl-decryption-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
