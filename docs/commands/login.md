---
command: "login"
description: "Log in to SCM with a user account via the browser (experimental OAuth)"
usage: "login"
category: auth
scope: global
---

# login

**Category:** auth
**API mode:** N/A (obtains a token, then re-initialises the SCM client)
**SSH mode:** Not applicable

## Description

`login` performs an interactive **user-account** sign-in to SCM using the OAuth
2.0 **authorization-code + PKCE** flow: it opens your browser to authenticate,
captures the redirect on a local `127.0.0.1` callback, exchanges the code for a
bearer token, stores the token in the OS keychain (with its expiry in your
preferences), and re-initialises the live SCM client — no restart needed.

> **Experimental.** SCM's public API is built around OAuth *client-credentials*
> (service accounts). There is no publicly documented browser flow that mints an
> SCM API token for a user account, so `login` only works once a compatible
> authorization endpoint is configured. For production use, prefer a **Service
> Account**: `arc auth configure`.

## Configuration

Set these environment variables before running `login`:

| Variable | Required | Purpose |
|---|---|---|
| `ARC_OAUTH_AUTH_URL` | yes | Authorization endpoint (browser is sent here) |
| `ARC_OAUTH_TOKEN_URL` | yes | Token endpoint (code is exchanged here) |
| `ARC_OAUTH_CLIENT_ID` | yes | Public OAuth client id |
| `ARC_OAUTH_SCOPE` | no | Space-separated scopes |
| `ARC_OAUTH_REDIRECT_PORT` | no | Loopback callback port (default 4455) |

## Usage

```
login
```

When unconfigured, `login` prints clear guidance and does nothing else. You can
also manage authentication (Service vs User account) in the browser via
`arc gui-configure` → Authentication.

## See also

- `arc auth configure` — service-account (recommended) setup
- `docs/gui-consoles.md` — the ARC settings console
