# Using ARC

## Launch

```bash
arc
# or
python run.py
```

## Navigation

```text
folder Shared          Set the active SCM folder
show devices           List managed devices
cd fw-dallas-01        Change Device in SCM/API context
pwd                    Show device, mode, and folder
```

## API-first command execution

Commands run through SCM/SCM APIs unless you explicitly choose SSH.

```text
show system info
show routing route
show security policy
```

## Interactive SSH session

`connect` and `remote <device>` open a true interactive SSH session. ARC
authenticates using stored credentials (keychain + 2FA), then hands the
terminal directly to the device.

You are ON the device — every keystroke goes to it; every byte from the device
is written to your terminal. ARC is a transparent byte pipe; no interception, no
logging, no command dispatch.

Type `exit` on the device to close the session and return to the ARC prompt.

### SSH to a named device directly

```text
arc > remote fw-dallas-01

✓ Authenticated — handing terminal to fw-dallas-01
ARC is now a transparent pipe. Every keystroke goes directly to the device.
Type 'exit' on the device to close the session and return to ARC.

admin@fw-dallas-01> show system info
...
admin@fw-dallas-01> exit

SSH session ended. Back in ARC — device context fw-dallas-01 preserved.
arc:fw-dallas-01 >
```

### SSH to the current device

Use `cd` to set the device context, then `connect`:

```text
arc > cd fw-dallas-01
arc:fw-dallas-01 > connect

✓ Authenticated — handing terminal to fw-dallas-01
...
admin@fw-dallas-01> show system info
admin@fw-dallas-01> exit

SSH session ended. Back in ARC — device context fw-dallas-01 preserved.
arc:fw-dallas-01 >
```

