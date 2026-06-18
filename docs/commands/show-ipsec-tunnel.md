# show ipsec-tunnel

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** `show vpn ipsec-sa`

## Description

Show IPsec tunnel configurations in the active folder

## Usage

```
show ipsec-tunnel [--remote]
```

## Examples

Run via SCM API:
```
arc > show ipsec-tunnel
```

Run directly on device via SSH:
```
arc:fw-01 > show ipsec-tunnel --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ipsec-tunnel
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
