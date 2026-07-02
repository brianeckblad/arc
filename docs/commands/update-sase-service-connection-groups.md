---
command: "update sase service-connection-groups"
description: "Update a service connection group"
category: sase
scope: global
---

# update sase service-connection-groups

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a service connection group

## Usage

```
update sase service-connection-groups [--remote]
```

## Examples

Run via SCM API:
```
arc > update sase service-connection-groups
```

Run directly on device via SSH:
```
arc:fw-01 > update sase service-connection-groups --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update sase service-connection-groups
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
