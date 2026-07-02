---
command: "update sase shared-infrastructure-settings"
description: "Update infrastructure settings"
category: sase
scope: global
---

# update sase shared-infrastructure-settings

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update infrastructure settings

## Usage

```
update sase shared-infrastructure-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > update sase shared-infrastructure-settings
```

Run directly on device via SSH:
```
arc:fw-01 > update sase shared-infrastructure-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update sase shared-infrastructure-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
