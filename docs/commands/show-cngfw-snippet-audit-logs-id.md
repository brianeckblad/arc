---
command: "show cngfw snippet-audit-logs id"
description: "Get a snippet audit logs"
category: cloudngfw
scope: global
---

# show cngfw snippet-audit-logs id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a snippet audit logs

## Usage

```
show cngfw snippet-audit-logs id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw snippet-audit-logs id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw snippet-audit-logs id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw snippet-audit-logs id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
