---
command: "update cngfw tacacs-server-profiles"
description: "Update a TACACS server profile"
category: cloudngfw
scope: global
---

# update cngfw tacacs-server-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a TACACS server profile

## Usage

```
update cngfw tacacs-server-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw tacacs-server-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw tacacs-server-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw tacacs-server-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
