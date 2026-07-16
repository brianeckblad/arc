---
command: "login"
description: "Authenticate to SCM now via the API and show your identity (no browser)"
usage: "login"
category: auth
scope: global
---

# login

**Category:** auth
**API mode:** obtains a fresh token, then re-initialises the SCM client
**SSH mode:** Not applicable

## Description

`login` authenticates to Strata Cloud Manager **using the API — no browser**. It
mints a fresh token from your service-account credentials via the documented
client-credentials flow, then reads the userinfo endpoint to show **who you are**.
The live SCM client is refreshed (no restart) and the token expiry is recorded in
your preferences.

Two SCM endpoints are used (pan.dev):

| Endpoint | Purpose |
|---|---|
| `POST /auth/v1/oauth2/access_token` | Mint a 15-minute token — Client ID + Client Secret sent as HTTP Basic auth, `grant_type=client_credentials`, `scope=tsg_id:<TSG>`. [Docs](https://pan.dev/scm/api/auth/post-auth-v-1-oauth-2-access-token/) |
| `POST /auth/v1/oauth2/userinfo` | Return the OAuth 2.0 identity claims for the token. [Docs](https://pan.dev/scm/api/auth/post-auth-v-1-oauth-2-userinfo/) |

ARC already authenticates automatically on startup; `login` is an explicit
"authenticate now and confirm my identity" command.

## Requirements

`login` needs SCM credentials already configured — a **service account**
(Client ID + Client Secret + TSG ID) or a pre-issued bearer token. Set them with:

```
setup scm            # in-shell guided wizard
arc auth configure   # outside the shell
```

If no credentials are present, `login` tells you and points at `setup scm`.

## Usage

```
login
```

Example output:

```
✓ Authenticated to SCM — token valid for ~15 min.
  Signed in as ARC Service  <svc@1234.iam.panserviceaccount.com>
  TSG: 1234567890
```

Identity display is best-effort: if the userinfo endpoint returns nothing, `login`
still succeeds (the token is valid) and simply notes that claims were unavailable.

## See also

- `setup scm` — guided credential setup
- `arc auth configure` — configure a service account (outside the shell)
- `arc gui-configure` → Authentication — manage auth in the browser console
