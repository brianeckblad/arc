---
command: "set oauth2 userinfo"
description: "Retrieve oAuth oAuth 2.0 claims"
category: auth
scope: global
---

# set oauth2 userinfo

**Category:** auth
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Retrieve oAuth oAuth 2.0 claims

## Usage

```
set oauth2 userinfo [--remote]
```

## Examples

Run via SCM API:
```
arc > set oauth2 userinfo
```

Run directly on device via SSH:
```
arc:fw-01 > set oauth2 userinfo --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set oauth2 userinfo
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
