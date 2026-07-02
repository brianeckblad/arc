---
command: "show cngfw config-versions"
description: "List configuration versions"
category: cloudngfw
scope: global
---

# show cngfw config-versions

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List configuration versions

## Usage

```
show cngfw config-versions [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw config-versions
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw config-versions --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw config-versions
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
