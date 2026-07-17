---
command: "show vpn tunnel"
description: "Show live VPN tunnel state from device — use --remote"
feature_flag: ipsec_vpn
category: network
scope: device
api: "(live device state — via the SCM device tunnel; no SSH/2FA)"
---

---
command: "show vpn tunnel"
description: "Show live VPN tunnel state from device — use --remote"
feature_flag: ipsec_vpn
category: network
scope: device
api: "(live device state — via the SCM device tunnel; no SSH/2FA)"
---

---
command: "show vpn tunnel"
description: "Show live VPN tunnel state from device — use --remote"
feature_flag: ipsec_vpn
category: network
scope: device
api: "(live device state — SSH via --remote)"
---

# show vpn tunnel

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** `show vpn tunnel`

## Description

Show live VPN tunnel state from device — use --remote

## Usage

```
show vpn tunnel [--remote]
```

## Examples

Run via SCM API:
```
arc > show vpn tunnel
```

Run directly on device via SSH:
```
arc:fw-01 > show vpn tunnel --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show vpn tunnel
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
