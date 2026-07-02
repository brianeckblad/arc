---
command: "set ciedss cache-users"
description: "Fetch user information from the CIE Directory Sync Service across multiple scenarios."
category: ciedss
scope: global
---

# set ciedss cache-users

**Category:** ciedss
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Fetch user information from the CIE Directory Sync Service across multiple scenarios.

## Usage

```
set ciedss cache-users [--remote]
```

## Examples

Run via SCM API:
```
arc > set ciedss cache-users
```

Run directly on device via SSH:
```
arc:fw-01 > set ciedss cache-users --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ciedss cache-users
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
