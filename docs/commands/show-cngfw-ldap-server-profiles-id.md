---
command: "show cngfw ldap-server-profiles id"
description: "Get an LDAP server profile"
category: cloudngfw
scope: global
---

# show cngfw ldap-server-profiles id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get an LDAP server profile

## Usage

```
show cngfw ldap-server-profiles id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw ldap-server-profiles id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw ldap-server-profiles id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw ldap-server-profiles id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
