---
command: "update ngts updatesconfig"
description: "Create or Update Configuration"
category: ngts
scope: global
---

# update ngts updatesconfig

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create or Update Configuration

## Usage

```
update ngts updatesconfig [--remote]
```

## Examples

Run via SCM API:
```
arc > update ngts updatesconfig
```

Run directly on device via SSH:
```
arc:fw-01 > update ngts updatesconfig --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update ngts updatesconfig
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
