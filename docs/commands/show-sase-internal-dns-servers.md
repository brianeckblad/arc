---
command: "show sase internal-dns-servers"
description: "List internal DNS servers"
category: sase
scope: global
---

# show sase internal-dns-servers

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List internal DNS servers

## Usage

```
show sase internal-dns-servers [--remote]
```

## Examples

Run via SCM API:
```
arc > show sase internal-dns-servers
```

Run directly on device via SSH:
```
arc:fw-01 > show sase internal-dns-servers --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show sase internal-dns-servers
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
