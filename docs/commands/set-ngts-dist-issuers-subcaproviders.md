---
command: "set ngts dist-issuers subcaproviders"
description: "Create a new Sub CA provider"
category: ngts
scope: global
---

# set ngts dist-issuers subcaproviders

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a new Sub CA provider

## Usage

```
set ngts dist-issuers subcaproviders [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts dist-issuers subcaproviders
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts dist-issuers subcaproviders --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts dist-issuers subcaproviders
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
