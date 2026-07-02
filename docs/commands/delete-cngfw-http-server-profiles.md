---
command: "delete cngfw http-server-profiles"
description: "Delete a HTTP server profile"
category: cloudngfw
scope: global
---

# delete cngfw http-server-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a HTTP server profile

## Usage

```
delete cngfw http-server-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw http-server-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw http-server-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw http-server-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
