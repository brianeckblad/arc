---
command: "set sase mobileagent enable"
description: "Enable GlobalProtect"
category: sase
scope: global
---

# set sase mobileagent enable

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Enable GlobalProtect

## Usage

```
set sase mobileagent enable [--remote]
```

## Examples

Run via SCM API:
```
arc > set sase mobileagent enable
```

Run directly on device via SSH:
```
arc:fw-01 > set sase mobileagent enable --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set sase mobileagent enable
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
