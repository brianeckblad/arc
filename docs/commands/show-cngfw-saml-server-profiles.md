---
command: "show cngfw saml-server-profiles"
description: "List SAML server profiles"
category: cloudngfw
scope: global
---

# show cngfw saml-server-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List SAML server profiles

## Usage

```
show cngfw saml-server-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw saml-server-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw saml-server-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw saml-server-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
