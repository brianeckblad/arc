---
command: "set cngfw mfa-servers"
description: "Create an MFA server"
category: cloudngfw
scope: global
---

# set cngfw mfa-servers

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create an MFA server

## Usage

```
set cngfw mfa-servers [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw mfa-servers
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw mfa-servers --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw mfa-servers
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
