---
command: "set ngts machines batchprovisionings abort"
description: "Abort active batch provisioning for a"
category: ngts
scope: global
---

# set ngts machines batchprovisionings abort

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Abort active batch provisioning for a

## Usage

```
set ngts machines batchprovisionings abort [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts machines batchprovisionings abort
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts machines batchprovisionings abort --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts machines batchprovisionings abort
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
