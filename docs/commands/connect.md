# connect

Open an interactive SSH session to a managed device.

With **no argument**, `connect` looks at the devices in your current folder:
- exactly one → it connects straight away;
- several → it lists them and asks you to pick one (by number or name);
- none → it tells you, and suggests `show devices` or `cd folder <name>`.

You can also target a device directly with `connect <name>` (name, hostname, IP,
or serial), or pre-select one with `cd device <name>` and then `connect`.

ARC authenticates using stored credentials (OS keychain / SSH agent) and 2FA,
then hands the terminal over to the device. You are ON the device — every
keystroke goes directly to it, and ARC is a transparent byte pipe. Type `exit`
on the device to close the session and return to the ARC prompt.

**Category:** Shell built-in
**API mode:** Not applicable (SSH only)
**SSH mode:** Opens an interactive PTY session

## Usage

```
connect              # SSH to the current folder's device (prompts if several)
connect <device>     # SSH to a named device / hostname / IP / serial
```

## Examples

Connect to the device in the current folder:

```
arc:Production > connect

  Devices in folder 'Production':
  #    Device                        IP                Status
  1    fw-edge-01                    10.0.0.11         connected
  2    fw-edge-02                    10.0.0.12         —
  Enter # or device name [1]: 1

✓ Authenticated — handing terminal to fw-edge-01
admin@fw-edge-01> show system info
admin@fw-edge-01> exit
arc:Production >
```

Target one directly:

```
arc:Production > connect fw-edge-02
```

## Authentication

If no SSH credentials are stored for your profile, `connect` prompts you inline
before opening the session:

```
arc:Production > connect fw-edge-01
  SSH Username [admin]:
  SSH Password (blank to use SSH agent / default keys):
```

The entered credentials are used for this session only — they are not saved.
To store them for future sessions, use `scm setup` (in-shell wizard) or `arc auth configure`.

When credentials are stored, ARC tries them in this order:
1. SSH agent keys
2. Configured key file (from your profile)
3. Default key files (`~/.ssh/id_ed25519`, `id_rsa`, `id_ecdsa`)
4. Keyboard-interactive (surfaces 2FA prompts)
5. Stored password fallback

## See Also

- `help remote` — run a single command on a named device over SSH
- `help cd` — change device/folder context (`cd folder <name>`, `cd device <name>`)
- `help scm` — log into SCM / manage credential profiles (SCM API auth is separate)
- `arc setup osx` / `arc setup win` / `arc setup linux` — credential storage
