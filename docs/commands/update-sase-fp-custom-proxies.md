---
command: "update sase fp-custom-proxies"
description: "Update a GlobalProtect regional and custom proxy"
category: sase
scope: global
---

# update sase fp-custom-proxies

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a GlobalProtect regional and custom proxy

## Usage

```
update sase fp-custom-proxies [--remote]
```

## Examples

Run via SCM API:
```
arc > update sase fp-custom-proxies
```

Run directly on device via SSH:
```
arc:fw-01 > update sase fp-custom-proxies --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update sase fp-custom-proxies
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
