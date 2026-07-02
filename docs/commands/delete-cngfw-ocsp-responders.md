---
command: "delete cngfw ocsp-responders"
description: "Delete an OCSP responder"
category: cloudngfw
scope: global
---

# delete cngfw ocsp-responders

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete an OCSP responder

## Usage

```
delete cngfw ocsp-responders [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw ocsp-responders
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw ocsp-responders --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw ocsp-responders
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
