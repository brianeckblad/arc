---
command: "show ngts dist-issuers configurations id"
description: "Get configurations details for a specific"
category: ngts
scope: global
---

# show ngts dist-issuers configurations id

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get configurations details for a specific

## Usage

```
show ngts dist-issuers configurations id [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts dist-issuers configurations id
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts dist-issuers configurations id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts dist-issuers configurations id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
