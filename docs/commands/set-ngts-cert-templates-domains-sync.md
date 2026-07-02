---
command: "set ngts cert-templates domains-sync"
description: "Synchronize issuing templates domains with CA"
category: ngts
scope: global
---

# set ngts cert-templates domains-sync

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Synchronize issuing templates domains with CA

## Usage

```
set ngts cert-templates domains-sync [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts cert-templates domains-sync
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts cert-templates domains-sync --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts cert-templates domains-sync
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
