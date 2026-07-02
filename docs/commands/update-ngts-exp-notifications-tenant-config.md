---
command: "update ngts exp-notifications tenant-config"
description: "Update the certificate expiration notification con"
category: ngts
scope: global
---

# update ngts exp-notifications tenant-config

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update the certificate expiration notification con

## Usage

```
update ngts exp-notifications tenant-config [--remote]
```

## Examples

Run via SCM API:
```
arc > update ngts exp-notifications tenant-config
```

Run directly on device via SSH:
```
arc:fw-01 > update ngts exp-notifications tenant-config --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update ngts exp-notifications tenant-config
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
