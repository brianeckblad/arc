---
command: "update cngfw ocsp-responders"
description: "Update an OCSP responder"
category: cloudngfw
scope: global
---

# update cngfw ocsp-responders

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update an OCSP responder

## Usage

```
update cngfw ocsp-responders [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw ocsp-responders
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw ocsp-responders --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw ocsp-responders
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
