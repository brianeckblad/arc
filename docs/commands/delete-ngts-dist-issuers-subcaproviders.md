---
command: "delete ngts dist-issuers subcaproviders"
description: "Remove a Sub CA provider"
category: ngts
scope: global
---

# delete ngts dist-issuers subcaproviders

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Remove a Sub CA provider

## Usage

```
delete ngts dist-issuers subcaproviders [--remote]
```

## Examples

Run via SCM API:
```
arc > delete ngts dist-issuers subcaproviders
```

Run directly on device via SSH:
```
arc:fw-01 > delete ngts dist-issuers subcaproviders --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete ngts dist-issuers subcaproviders
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
