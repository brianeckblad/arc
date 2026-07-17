---
command: "show vpn ike-sa"
description: "Show live IKE security associations from device — use --remote"
feature_flag: ipsec_vpn
category: network
scope: device
api: "(live device state — via the SCM device tunnel; no SSH/2FA)"
---

---
command: "show vpn ike-sa"
description: "Show live IKE security associations from device — use --remote"
feature_flag: ipsec_vpn
category: network
scope: device
api: "(live device state — via the SCM device tunnel; no SSH/2FA)"
---

---
command: "show vpn ike-sa"
description: "Show live IKE security associations from device — use --remote"
feature_flag: ipsec_vpn
category: network
scope: device
api: "(live device state — SSH via --remote)"
---

# show vpn ike-sa

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** `show vpn ike-sa`

## Description

Show live IKE security associations from device — use --remote

## Usage

```
show vpn ike-sa [--remote]
```

## Examples

Run via SCM API:
```
arc > show vpn ike-sa
```

Run directly on device via SSH:
```
arc:fw-01 > show vpn ike-sa --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show vpn ike-sa
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
