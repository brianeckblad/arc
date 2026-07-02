---
command: "show local-config download"
description: "Download local configuration file"
category: operations
scope: global
---

# show local-config download

**Category:** operations
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Download local configuration file

## Usage

```
show local-config download [--remote]
```

## Examples

Run via SCM API:
```
arc > show local-config download
```

Run directly on device via SSH:
```
arc:fw-01 > show local-config download --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show local-config download
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
