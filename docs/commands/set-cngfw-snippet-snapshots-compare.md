---
command: "set cngfw snippet-snapshots compare"
description: "Compare Snippet Snapshots"
category: cloudngfw
scope: global
---

# set cngfw snippet-snapshots compare

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Compare Snippet Snapshots

## Usage

```
set cngfw snippet-snapshots compare [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw snippet-snapshots compare
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw snippet-snapshots compare --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw snippet-snapshots compare
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
