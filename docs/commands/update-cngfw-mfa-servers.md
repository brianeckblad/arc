---
command: "update cngfw mfa-servers"
description: "Update an MFA server"
category: cloudngfw
scope: global
---

# update cngfw mfa-servers

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update an MFA server

## Usage

```
update cngfw mfa-servers [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw mfa-servers
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw mfa-servers --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw mfa-servers
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
