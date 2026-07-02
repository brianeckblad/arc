---
command: "set cngfw decryption-rules move"
description: "Move a decryption rule"
category: cloudngfw
scope: global
---

# set cngfw decryption-rules move

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Move a decryption rule

## Usage

```
set cngfw decryption-rules move [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw decryption-rules move
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw decryption-rules move --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw decryption-rules move
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
