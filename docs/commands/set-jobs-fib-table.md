---
command: "set jobs fib-table"
description: "Initiate a job to retrieve FIB table from device(s)"
category: operations
scope: global
---

# set jobs fib-table

**Category:** operations
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Initiate a job to retrieve FIB table from device(s)

## Usage

```
set jobs fib-table [--remote]
```

## Examples

Run via SCM API:
```
arc > set jobs fib-table
```

Run directly on device via SSH:
```
arc:fw-01 > set jobs fib-table --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set jobs fib-table
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
