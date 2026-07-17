---
command: "show nat-rules"
description: "Show NAT rules in the active folder"
feature_flag: nat_rules
category: network
scope: folder
api: "GET /config/network/v1/nat-rules"
---

---
command: "show nat-rules"
description: "Show NAT rules in the active folder"
feature_flag: nat_rules
category: network
scope: folder
api: "GET /config/network/v1/nat-rules"
---

---
command: "show nat-rules"
description: "Show NAT rules in the active folder"
feature_flag: nat_rules
category: network
scope: folder
api: "GET /config/network/v1/nat-rules"
---

# show nat-rules

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** `show running nat-policy`

## Description

Show NAT rules in the active folder

## Usage

```
show nat-rules [--remote]
```

## Examples

Run via SCM API:
```
arc > show nat-rules
```

Run directly on device via SSH:
```
arc:fw-01 > show nat-rules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show nat-rules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
