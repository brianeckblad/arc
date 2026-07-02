---
command: "show ngts credential-configs"
description: "Retrieves a set of Credential Manager"
category: ngts
scope: global
---

# show ngts credential-configs

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Retrieves a set of Credential Manager

## Usage

```
show ngts credential-configs [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts credential-configs
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts credential-configs --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts credential-configs
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
