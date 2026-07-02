---
command: "set incidents incidents search"
description: "Incidents List Search"
category: incidents
scope: global
---

# set incidents incidents search

**Category:** incidents
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Incidents List Search

## Usage

```
set incidents incidents search [--remote]
```

## Examples

Run via SCM API:
```
arc > set incidents incidents search
```

Run directly on device via SSH:
```
arc:fw-01 > set incidents incidents search --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set incidents incidents search
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
