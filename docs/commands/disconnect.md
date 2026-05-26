# disconnect

**This command no longer exists.**

ARC previously had an SSH "passthrough mode" where the shell stayed active and
forwarded commands to a device. The `disconnect` command exited that mode.

## What replaced it

`connect` and `remote` now open a true interactive SSH session — your terminal
is handed directly to the device. ARC is not a middle layer; it's a transparent
byte pipe.

To end the session, type `exit` on the device itself (not in ARC). The SSH
channel closes and you return to the ARC prompt automatically.

## Migration

**Old workflow (no longer valid):**

```
remote fw-dallas-01   ← entered "SSH mode"
show system info      ← forwarded to device via ARC
disconnect            ← returned to ARC prompt
```

**New workflow:**

```
remote fw-dallas-01   ← opens interactive SSH session
<you are now ON the device, not in ARC>
admin@fw-dallas-01> show system info
admin@fw-dallas-01> exit   ← closes SSH, returns to ARC
arc:fw-dallas-01 >
```

## See Also

- `help connect` — SSH to the current device
- `help remote` — SSH to a named device
- `help exit` — exit ARC entirely
