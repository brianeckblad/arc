---
command: "set ngts credential-configs"
description: "Add a set of Credential Manager"
category: ngts
scope: global
---

# set ngts credential-configs

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Add a set of Credential Manager

## Usage

```
set ngts credential-configs [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts credential-configs
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts credential-configs --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts credential-configs
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
