---
command: "delete sase internal-dns-servers"
description: "Delete an internal DNS server"
category: sase
scope: global
---

# delete sase internal-dns-servers

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete an internal DNS server

## Usage

```
delete sase internal-dns-servers [--remote]
```

## Examples

Run via SCM API:
```
arc > delete sase internal-dns-servers
```

Run directly on device via SSH:
```
arc:fw-01 > delete sase internal-dns-servers --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete sase internal-dns-servers
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
