---
command: "delete sase service-connection-groups"
description: "Delete a service connection group"
category: sase
scope: global
---

# delete sase service-connection-groups

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a service connection group

## Usage

```
delete sase service-connection-groups [--remote]
```

## Examples

Run via SCM API:
```
arc > delete sase service-connection-groups
```

Run directly on device via SSH:
```
arc:fw-01 > delete sase service-connection-groups --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete sase service-connection-groups
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
