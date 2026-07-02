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

## Configure mode (write operations)

Write operations (`set`, `update`, `delete`) require configure mode — a Cisco-style
workflow that separates read-only browsing from configuration changes.

```text
arc:global > configure
arc:global # set address web1 fqdn api.example.com
arc:global # update address web1 description "Updated desc"
arc:global # delete address old-host
arc:global # commit
arc:global # exit
arc:global >
```

The prompt changes to `#` when in configure mode. Type `exit` to leave configure mode
and return to the normal `>` prompt.

**Why configure mode?** It provides a clear visual and operational boundary between
inspection and mutation, reduces accidental changes, and aligns with familiar
Cisco/Junos conventions for network operators.

## API-first command execution

Commands run through SCM/SCM APIs unless you explicitly choose SSH.

```text
show system info
show routing route
show security policy
```

## Filter output — `| match`, `| except`, `| count`

Any output-producing command can be piped through PAN-OS-style filters:

```text
show devices | match production        # only lines matching (regex, case-insensitive)
show security policy | except deny     # drop matching lines
show devices | match PA-4 | count      # chain filters; count matching lines
```

Filters operate on rendered output lines. Interactive commands
(`connect`, `remote`, `configure`, `setup`) cannot be filtered.

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

