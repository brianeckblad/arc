# request system reboot

**Category:** operations
**API mode:** ✓ Live SCM data
**SSH mode:** `request system reboot`

## Description

Reboot a managed device — use --remote  (CAUTION: device will restart)

## Usage

```
request system reboot [--remote]
```

## Examples

Run via SCM API:
```
arc > request system reboot
```

Run directly on device via SSH:
```
arc:fw-01 > request system reboot --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > request system reboot
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
