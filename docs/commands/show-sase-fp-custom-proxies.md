---
command: "show sase fp-custom-proxies"
description: "List GlobalProtect regional and custom proxies"
category: sase
scope: global
---

# show sase fp-custom-proxies

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List GlobalProtect regional and custom proxies

## Usage

```
show sase fp-custom-proxies [--remote]
```

## Examples

Run via SCM API:
```
arc > show sase fp-custom-proxies
```

Run directly on device via SSH:
```
arc:fw-01 > show sase fp-custom-proxies --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show sase fp-custom-proxies
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
