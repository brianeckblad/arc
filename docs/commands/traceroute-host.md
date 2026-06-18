# traceroute host

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** `(dynamic)`

## Description

Traceroute from device — traceroute host <ip>  (use --remote)

## Usage

```
traceroute host [--remote]
```

## Examples

Run via SCM API:
```
arc > traceroute host
```

Run directly on device via SSH:
```
arc:fw-01 > traceroute host --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > traceroute host
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
