---
command: "show arp"
description: "Show live ARP table from device — use --remote"
feature_flag: show_arp
category: network
scope: device
api: "(live device state — SSH via --remote)"
---

# show arp

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** `show arp all`

## Description

Show live ARP table from device — use --remote

## Usage

```
show arp [--remote]
```

## Examples

Run via SCM API:
```
arc > show arp
```

Run directly on device via SSH:
```
arc:fw-01 > show arp --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show arp
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
