---
command: "set ngts cert-instance-search"
description: "Retrieve certificate instance data matching search"
category: ngts
scope: global
---

# set ngts cert-instance-search

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Retrieve certificate instance data matching search

## Usage

```
set ngts cert-instance-search [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts cert-instance-search
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts cert-instance-search --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts cert-instance-search
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
