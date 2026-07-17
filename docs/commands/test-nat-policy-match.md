---
command: "test nat-policy-match"
description: "Test NAT policy match — source <ip> destination <ip>  (use --remote)"
feature_flag: test_nat
category: network
scope: device
api: "(live device state — via the SCM device tunnel; no SSH/2FA)"
---

---
command: "test nat-policy-match"
description: "Test NAT policy match — source <ip> destination <ip>  (use --remote)"
feature_flag: test_nat
category: network
scope: device
api: "(live device state — via the SCM device tunnel; no SSH/2FA)"
---

---
command: "test nat-policy-match"
description: "Test NAT policy match (use --remote)"
usage: "test nat-policy-match source <ip> destination <ip>"
feature_flag: test_nat
category: network
scope: device
api: "(live device state — SSH via --remote)"
---

# test nat-policy-match

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** `(dynamic)`

## Description

Test NAT policy match — source <ip> destination <ip>  (use --remote)

## Usage

```
test nat-policy-match [--remote]
```

## Examples

Run via SCM API:
```
arc > test nat-policy-match
```

Run directly on device via SSH:
```
arc:fw-01 > test nat-policy-match --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > test nat-policy-match
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
