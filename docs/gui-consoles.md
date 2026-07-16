# ARC browser consoles

ARC ships two local, loopback-only browser GUIs. Both are on-demand: they bind
`127.0.0.1:<port>`, open your browser, and block the shell until you click
**Save & Exit** (or press Ctrl-C). They share one foundation (`app/web/gui_base.py`, `/assets/gui.css`,
`/assets/gui.js` + a reusable widget library) so they look and behave
consistently. **Save & Exit** shuts the local
server down and shows a "you can close this tab" message — close the tab
yourself (browsers won't let a page close a tab it didn't open).

Both consoles share **one GUI theme** (edited in the ARC console under
Appearance) and read it fresh on each launch, so a saved theme applies to both
without restarting ARC.

## `feature gui-configure`

The feature-flag editor (formerly `feature gui`, which still works as a hidden
alias). Manage capability **areas**, per-command **feature states**
(ON / DEV / OFF / HIDDEN), per-command **scope**, **command structure**,
**aliases**, **built-ins**, and per-file **advanced** regeneration settings.

- Port: `features_gui.port` in `config.json` (default **4445**).
- Enable/disable: `features_gui.enabled`.

## `arc gui-configure`

The ARC settings console — a modern, SCM-style admin GUI for everything you'd
otherwise edit by hand. Sections:

| Section | Manages |
|---|---|
| Dashboard | Health: SCM connectivity, keychain, profile/TSG/folder, GUI ports |
| Authentication | Service Account (recommended) + User Account (experimental); Test auth |
| Credentials & Keychain | SCM client id / TSG / secret / bearer + SSH user / key / port / password (secrets → OS keychain) |
| Connection / config.json | Default folder, debug, GUI **ports** + enabled toggles, profiles |
| Preferences | Terminal paging/width/height, spinner |
| Appearance / Theme | GUI palette + per-token colours (saved per user) |
| Branding & Variables | `banner.txt`, `goodbye.txt`, `app-variables.json` |
| API Sources | `scm-sources.json`, `panos-sources.json` |
| Maintenance | **Update Docs & Commands**, catalog rebuild |

- Port: `arc_gui.port` in `config.json` (default **4444**).
- Enable/disable: `arc_gui.enabled`.

Per-user preferences now live inside `config.json` (a `preferences` block) —
the old `preferences.json` is migrated automatically on first run. Every change
routes through the same settings/config/keychain helpers the CLI uses, so GUI
edits and manual edits stay equivalent. Secrets are never written
to `config.json` — only to the OS keychain — and are never read back into the
browser (blank secret fields mean "leave unchanged").

## `login` (experimental user-account auth)

`login` runs an OAuth 2.0 **authorization-code + PKCE** loopback flow: it opens
your browser to authenticate, captures the redirect on a local callback, and
exchanges the code for a bearer token (stored in the keychain; expiry recorded
in preferences). The live SCM client is then re-initialised.

> **Experimental.** SCM's public API is built around OAuth *client-credentials*
> (service accounts). There is no publicly documented browser flow that mints an
> SCM API token for a user account, so `login` requires a compatible endpoint to
> be configured:
>
> - `ARC_OAUTH_AUTH_URL` — authorization endpoint
> - `ARC_OAUTH_TOKEN_URL` — token endpoint
> - `ARC_OAUTH_CLIENT_ID` — public client id
> - `ARC_OAUTH_SCOPE` (optional), `ARC_OAUTH_REDIRECT_PORT` (optional, default 4455)
>
> For production use, prefer a **Service Account**: `arc auth configure`.
