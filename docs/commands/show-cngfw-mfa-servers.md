---
command: "show cngfw mfa-servers"
description: "List MFA servers"
category: cloudngfw
scope: global
---

# show cngfw mfa-servers

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List MFA servers

## Usage

```
show cngfw mfa-servers [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw mfa-servers
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw mfa-servers --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw mfa-servers
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
