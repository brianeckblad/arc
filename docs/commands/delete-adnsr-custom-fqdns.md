---
command: "delete adnsr custom-fqdns"
description: "Delete a Custom FQDN"
category: adnsr
scope: global
---

# delete adnsr custom-fqdns

**Category:** adnsr
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a Custom FQDN

## Usage

```
delete adnsr custom-fqdns [--remote]
```

## Examples

Run via SCM API:
```
arc > delete adnsr custom-fqdns
```

Run directly on device via SSH:
```
arc:fw-01 > delete adnsr custom-fqdns --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete adnsr custom-fqdns
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
