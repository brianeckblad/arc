---
command: "set cngfw snippet-audit-logs"
description: "Create snippet audit logs configuration"
category: cloudngfw
scope: global
---

# set cngfw snippet-audit-logs

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create snippet audit logs configuration

## Usage

```
set cngfw snippet-audit-logs [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw snippet-audit-logs
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw snippet-audit-logs --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw snippet-audit-logs
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
