---
command: "show adnsr custom-fqdns"
description: "List Custom FQDNs"
category: adnsr
scope: global
---

# show adnsr custom-fqdns

**Category:** adnsr
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List Custom FQDNs

## Usage

```
show adnsr custom-fqdns [--remote]
```

## Examples

Run via SCM API:
```
arc > show adnsr custom-fqdns
```

Run directly on device via SSH:
```
arc:fw-01 > show adnsr custom-fqdns --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show adnsr custom-fqdns
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
