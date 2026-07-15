# Device access & authentication

ARC reaches your firewalls over **three different planes**, each with its own
authentication. Understanding which plane a command uses tells you whether you
will hit the device's login/2FA.

## The three planes

| Plane | Used by | Auth | 2FA? |
|---|---|---|---|
| **SCM config API** | `set` / `delete` / `show` config (`global`, `folder`) | SCM bearer token | no |
| **SCM ops-job proxy** | operational reads scoped **`device`** | SCM bearer token (runs over the device's management tunnel) | **no** |
| **Direct SSH** | commands scoped **`remote`**, `connect`, `--remote` | the **device's** login — local / RADIUS / **TACACS+** | **yes** (OTP / Duo push) |

Key point: **the SCM bearer token is not device CLI access.** It authenticates
only to SCM's REST API. The device CLI (SSH) is authenticated by the firewall
itself. So SSHing to a device always goes through its auth stack — in a
TACACS+/2FA environment, expect a challenge.

## Scope tells you the plane

Every command has a **scope** (see `feature show` / `feature info`):

- `global` / `folder` — SCM API. No device context, no 2FA.
- `device` — targets a device but runs via the **SCM ops-job proxy**. Needs
  `cd <device>`, but **no SSH and no 2FA**.
- `remote` — can only run by **SSHing to the device**. Needs `cd <device>` and
  triggers the device's login/**2FA**.

As ARC maps more operations to the SCM proxy, commands move from `remote` to
`device` — shrinking the set of commands that need 2FA. You can see the current
split with `feature show remote` / `feature area`.

## Running commands on a device

1. **`cd <device>`** to select a target, then run the command.
   - A `device`-scoped command runs via SCM (no 2FA).
   - A `remote`-scoped command SSHes to the box (2FA once per session).
2. **`connect <device>`** opens a full interactive SSH session (2FA once).
3. **`<command> --remote <device>`** runs a single command over SSH.

ARC **pools the SSH session** per device: you complete 2FA **once**, and further
`remote`/`--remote` commands reuse the warm, already-authenticated connection —
no repeated 2FA.

Once a device has a warm session the prompt shows an **`[ssh]`** marker, and any
`remote`-scoped command you type (no `--remote` needed) auto-routes over that
session. Selecting a different device with `cd` clears the marker.

## Credentials & 2FA behavior

- Store SSH credentials with `arc auth configure` (or `ARC_SSH_USER` /
  `ARC_SSH_KEY` / `ARC_SSH_PASS`). ARC auto-fills the password prompt and then
  surfaces the 2FA challenge (OTP code or Duo push) for you to approve.
- **Keys do not bypass TACACS+ 2FA** for a TACACS-managed admin — a static key
  cannot answer a challenge/response. A local firewall admin with an authorized
  key *can* skip 2FA, but that is an un-audited local account and usually against
  policy; prefer the SCM proxy for automation instead.

## Practical guidance

- Prefer **config via SCM** (default) and **operations via the SCM proxy**
  (`device` scope) — both avoid 2FA and are audited by SCM.
- Use **SSH (`remote`)** only for what SCM can't proxy (debug, tcpdump,
  break-glass device-local config). Do a single `connect` / `cd` + first command
  to authenticate once, then reuse the session.

## Related

- `help connect` · `help remote` — interactive/one-off SSH
- `help features` — scope, `feature scope`, and the feature editor
- `help config osx` / `config win` / `config nix` — storing SSH credentials
