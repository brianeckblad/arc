---
command: "update ngts credential-configs"
description: "Update a Credential Manager Service configuration"
category: ngts
scope: global
---

# update ngts credential-configs

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a Credential Manager Service configuration

## Usage

```
update ngts credential-configs [--remote]
```

## Examples

Run via SCM API:
```
arc > update ngts credential-configs
```

Run directly on device via SSH:
```
arc:fw-01 > update ngts credential-configs --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update ngts credential-configs
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
