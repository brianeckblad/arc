---
command: "show ngts exp-notifications tenant-config"
description: "Retrieve the certificate expiration notification c"
category: ngts
scope: global
---

# show ngts exp-notifications tenant-config

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Retrieve the certificate expiration notification c

## Usage

```
show ngts exp-notifications tenant-config [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts exp-notifications tenant-config
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts exp-notifications tenant-config --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts exp-notifications tenant-config
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
