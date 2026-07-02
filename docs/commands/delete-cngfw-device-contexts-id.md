---
command: "delete cngfw device-contexts id"
description: "Delete a device context segment"
category: cloudngfw
scope: global
---

# delete cngfw device-contexts id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a device context segment

## Usage

```
delete cngfw device-contexts id [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw device-contexts id
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw device-contexts id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw device-contexts id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
