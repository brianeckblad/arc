---
command: "show cngfw ocsp-responders"
description: "List OCSP responders"
category: cloudngfw
scope: global
---

# show cngfw ocsp-responders

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List OCSP responders

## Usage

```
show cngfw ocsp-responders [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw ocsp-responders
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw ocsp-responders --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw ocsp-responders
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
