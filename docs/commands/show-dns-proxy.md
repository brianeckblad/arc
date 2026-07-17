---
command: "show dns-proxy"
description: "Show DNS proxy configurations in the active folder"
feature_flag: dns_proxy
category: network
scope: folder
api: "GET /config/network/v1/dns-proxies"
---

---
command: "show dns-proxy"
description: "Show DNS proxy configurations in the active folder"
feature_flag: dns_proxy
category: network
scope: folder
api: "GET /config/network/v1/dns-proxies"
---

---
command: "show dns-proxy"
description: "Show DNS proxy configurations in the active folder"
feature_flag: dns_proxy
category: network
scope: folder
api: "GET /config/network/v1/dns-proxies"
---

# show dns-proxy

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** `show dns-proxy dns-signature statistics`

## Description

Show DNS proxy configurations in the active folder

## Usage

```
show dns-proxy [--remote]
```

## Examples

Run via SCM API:
```
arc > show dns-proxy
```

Run directly on device via SSH:
```
arc:fw-01 > show dns-proxy --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show dns-proxy
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
