---
command: "show cngfw config-versions id"
description: "Get config by version"
category: cloudngfw
scope: global
---

# show cngfw config-versions id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get config by version

## Usage

```
show cngfw config-versions id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw config-versions id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw config-versions id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw config-versions id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
