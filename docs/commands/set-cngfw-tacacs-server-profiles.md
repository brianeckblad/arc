---
command: "set cngfw tacacs-server-profiles"
description: "Create a TACACS server profile"
category: cloudngfw
scope: global
---

# set cngfw tacacs-server-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a TACACS server profile

## Usage

```
set cngfw tacacs-server-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw tacacs-server-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw tacacs-server-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw tacacs-server-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
