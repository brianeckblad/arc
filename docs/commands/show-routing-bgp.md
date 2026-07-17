---
command: "show routing bgp"
description: "Show live BGP routing state from device — use --remote"
feature_flag: bgp_routing
category: network
scope: device
api: "(live device state — via the SCM device tunnel; no SSH/2FA)"
---

---
command: "show routing bgp"
description: "Show live BGP routing state from device — use --remote"
feature_flag: bgp_routing
category: network
scope: device
api: "(live device state — via the SCM device tunnel; no SSH/2FA)"
---

---
command: "show routing bgp"
description: "Show live BGP routing state from device — use --remote"
feature_flag: bgp_routing
category: network
scope: device
api: "(live device state — SSH via --remote)"
---

# show routing bgp

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** `show routing protocol bgp peer`

## Description

Show live BGP routing state from device — use --remote

## Usage

```
show routing bgp [--remote]
```

## Examples

Run via SCM API:
```
arc > show routing bgp
```

Run directly on device via SSH:
```
arc:fw-01 > show routing bgp --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show routing bgp
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
