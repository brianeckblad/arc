---
command: "set cngfw snippet-snapshots diff"
description: "Diff Snippet Snapshots"
category: cloudngfw
scope: global
---

# set cngfw snippet-snapshots diff

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Diff Snippet Snapshots

## Usage

```
set cngfw snippet-snapshots diff [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw snippet-snapshots diff
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw snippet-snapshots diff --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw snippet-snapshots diff
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
