---
command: "show cngfw tls-service-profiles id"
description: "Get a TLS service profile"
category: cloudngfw
scope: global
---

# show cngfw tls-service-profiles id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a TLS service profile

## Usage

```
show cngfw tls-service-profiles id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw tls-service-profiles id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw tls-service-profiles id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw tls-service-profiles id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
