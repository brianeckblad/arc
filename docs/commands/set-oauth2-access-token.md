---
command: "set oauth2 access-token"
description: "Create an access token"
category: auth
scope: global
---

# set oauth2 access-token

**Category:** auth
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create an access token

## Usage

```
set oauth2 access-token [--remote]
```

## Examples

Run via SCM API:
```
arc > set oauth2 access-token
```

Run directly on device via SSH:
```
arc:fw-01 > set oauth2 access-token --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set oauth2 access-token
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
