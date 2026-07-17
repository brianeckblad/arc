---
command: "login"
description: "SSH into the current device (select it with 'cd device <name>' first)"
usage: "login [device]"
category: device
scope: device
---

# login

**Category:** device
**API mode:** Not applicable
**SSH mode:** opens an interactive SSH session to the selected device

## Description

`login` opens an interactive **SSH** session to the device you are currently in.
Select a device first with `cd device <name>`, then type `login` — this is the
same action as [`connect`](connect.md). You can also pass a device directly:
`login <name>`.

It reuses your stored SSH credentials (username, key or password, port) from
setup. Because it SSHes to the live device, **TACACS/RADIUS 2FA may prompt** —
this is the explicit device-access path.

> SCM API access is separate and needs no `login` — ARC authenticates to SCM
> automatically at startup from your stored service account. To check that,
> use `arc auth test` (from your terminal).

## Requirements

- A device context: run `cd device <name>` first (or `login <name>`).
- SSH credentials configured — see [`arc setup scm keystore`](../setup.md) or the
  per-OS guides (`arc setup osx|linux|win`). Prefer an SSH key or agent.

## Usage

```
cd device fw01
login
```

or, in one step:

```
login fw01
```

Type `exit` (or the device's logout) to close the session and return to ARC.

## See also

- `connect` — the same interactive SSH session (accepts a device name)
- `cd device <name>` — select the device context (never opens SSH itself)
- `help device-access` — SCM API vs SCM proxy vs SSH/2FA planes
