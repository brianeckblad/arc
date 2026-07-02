---
command: "update cngfw saml-server-profiles"
description: "Update a SAML server profile"
category: cloudngfw
scope: global
---

# update cngfw saml-server-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a SAML server profile

## Usage

```
update cngfw saml-server-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw saml-server-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw saml-server-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw saml-server-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
