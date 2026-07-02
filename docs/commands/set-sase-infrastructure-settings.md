---
command: "set sase infrastructure-settings"
description: "Create a GlobalProtect infrastructure setting"
category: sase
scope: global
---

# set sase infrastructure-settings

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a GlobalProtect infrastructure setting

## Usage

```
set sase infrastructure-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > set sase infrastructure-settings
```

Run directly on device via SSH:
```
arc:fw-01 > set sase infrastructure-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set sase infrastructure-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
