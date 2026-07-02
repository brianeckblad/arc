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

**Writes are staged locally — SCM is untouched until you commit.** Each
`set` / `update` / `delete` is validated against SCM (names resolved, objects
looked up) and then queued locally. Run 50 commands, review them, and nothing
has changed in SCM yet:

```text
arc:global # set address web1 fqdn web1.example.com
✓ Validated and staged: set address web1  (1 pending — show config to review, commit to apply)
arc:global # show config          # list all staged changes
arc:global # commit               # apply everything + push to devices
arc:global # commit watch         # same, then follow the push job to completion
arc:global # abandon              # discard staged changes — SCM never touched
```

Because changes stay local until commit, someone else can commit their own
work elsewhere in the tenant without colliding with your staged queue.
Folder creation (`set folder`, `folder create`) is the one exception — folders
are created immediately so staged objects can target them.

If you `exit` configure mode with staged changes, ARC forces a decision:

```text
arc:global # exit

Uncommitted changes: 2 staged locally — nothing has been sent to SCM.
  commit   — apply the changes and push to managed devices
  abandon  — discard the staged changes (SCM untouched)
  cancel   — stay in configure mode
```

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
show devices | json                    # raw JSON instead of a table (for scripts)
show devices | json | match serial     # filters apply to the JSON lines
```

Filters operate on rendered output lines (`| json` switches the rendering to
raw JSON first). Interactive commands (`connect`, `remote`, `configure`,
`setup`) cannot be filtered.

## Terminal preferences — pager, width, spinner

Per-user settings stored in `config/<user>/preferences.json` and loaded at
every launch:

```text
terminal                     # show current settings
terminal length 24           # page long help/docs output after 24 lines
terminal length 0            # disable paging (default — use scrollback)
terminal width 120           # force render width; 0 = auto-detect
terminal spinner off         # hide the "querying SCM…" spinner
```

## Live device data — API first, SSH when needed

The full PAN-OS op-command tree (show / clear / request / test …) is built in
(enable families with `feature enable panos_<family>`). Three execution paths:

```text
show advanced-routing route        # SCM serves it over the device tunnel —
                                   # no SSH, no 2FA, just your token (cd <device> first)
show routing protocol bgp peer     # SCM can't serve it → arc prints the exact
                                   # --remote / connect syntax to run instead
show routing protocol bgp peer --remote   # SSH: one 2FA per device per session
                                          # (the connection is pooled + kept alive)
watch 10 show routing protocol bgp peer --remote   # re-run every 10s, Ctrl-C stops —
                                                   # no extra 2FA (session reused)
```

## Break-glass device recovery

When SCM is down and a device must be recovered, the PAN-OS config tree is
available over SSH. The `panos_config_recovery` family (mgmt IP/DNS/gateway,
interface, panorama settings) is enabled by default; everything else stays
hidden until you `feature enable panos_config_<family>`. Every device-local
config command prints a DRIFT WARNING — SCM may overwrite local changes at the
next push. Commit on the device with `commit --remote` when done.

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

