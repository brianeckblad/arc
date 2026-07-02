---
command: "show cngfw ocsp-responders id"
description: "Get an OCSP responder"
category: cloudngfw
scope: global
---

# show cngfw ocsp-responders id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get an OCSP responder

## Usage

```
show cngfw ocsp-responders id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw ocsp-responders id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw ocsp-responders id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw ocsp-responders id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
