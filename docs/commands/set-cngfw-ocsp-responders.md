---
command: "set cngfw ocsp-responders"
description: "Create an OCSP responder"
category: cloudngfw
scope: global
---

# set cngfw ocsp-responders

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create an OCSP responder

## Usage

```
set cngfw ocsp-responders [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw ocsp-responders
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw ocsp-responders --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw ocsp-responders
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
