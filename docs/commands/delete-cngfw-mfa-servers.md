---
command: "delete cngfw mfa-servers"
description: "Delete an MFA server"
category: cloudngfw
scope: global
---

# delete cngfw mfa-servers

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete an MFA server

## Usage

```
delete cngfw mfa-servers [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw mfa-servers
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw mfa-servers --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw mfa-servers
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
