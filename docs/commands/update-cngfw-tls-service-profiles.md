---
command: "update cngfw tls-service-profiles"
description: "Update a TLS service profile"
category: cloudngfw
scope: global
---

# update cngfw tls-service-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a TLS service profile

## Usage

```
update cngfw tls-service-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw tls-service-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw tls-service-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw tls-service-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
