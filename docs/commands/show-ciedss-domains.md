---
command: "show ciedss domains"
description: "Fetch domains from the CIE Directory Sync Service"
category: ciedss
scope: global
---

# show ciedss domains

**Category:** ciedss
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Fetch domains from the CIE Directory Sync Service

## Usage

```
show ciedss domains [--remote]
```

## Examples

Run via SCM API:
```
arc > show ciedss domains
```

Run directly on device via SSH:
```
arc:fw-01 > show ciedss domains --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ciedss domains
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
