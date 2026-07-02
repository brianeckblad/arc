---
command: "set cngfw kerberos-server-profiles"
description: "Create a Kerberos server profile"
category: cloudngfw
scope: global
---

# set cngfw kerberos-server-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a Kerberos server profile

## Usage

```
set cngfw kerberos-server-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw kerberos-server-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw kerberos-server-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw kerberos-server-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
