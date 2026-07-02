---
command: "show cngfw config-versions running"
description: "Get running configuration versions"
category: cloudngfw
scope: global
---

# show cngfw config-versions running

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get running configuration versions

## Usage

```
show cngfw config-versions running [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw config-versions running
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw config-versions running --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw config-versions running
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
