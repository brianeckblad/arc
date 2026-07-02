---
command: "show cngfw tls-service-profiles"
description: "List TLS service profiles"
category: cloudngfw
scope: global
---

# show cngfw tls-service-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List TLS service profiles

## Usage

```
show cngfw tls-service-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw tls-service-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw tls-service-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw tls-service-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
