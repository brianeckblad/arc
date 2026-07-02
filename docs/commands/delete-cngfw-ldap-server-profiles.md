---
command: "delete cngfw ldap-server-profiles"
description: "Delete an LDAP server profile"
category: cloudngfw
scope: global
---

# delete cngfw ldap-server-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete an LDAP server profile

## Usage

```
delete cngfw ldap-server-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw ldap-server-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw ldap-server-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw ldap-server-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
