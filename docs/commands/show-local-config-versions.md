---
command: "show local-config versions"
description: "List local configuration versions for a device"
category: operations
scope: global
---

# show local-config versions

**Category:** operations
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List local configuration versions for a device

## Usage

```
show local-config versions [--remote]
```

## Examples

Run via SCM API:
```
arc > show local-config versions
```

Run directly on device via SSH:
```
arc:fw-01 > show local-config versions --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show local-config versions
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
