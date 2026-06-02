# tsg

Switch the active **Tenant Services Group (TSG)** context inside the current ARC session.

## Why you need this

Palo Alto SCM service accounts are created at the **root** level of your tenant hierarchy.
When you use OAuth client credentials (`client_id` / `client_secret`) the `tsg_id` you
configure tells ARC which TSG to scope the access token to during authentication.

A **bearer token** (`bearer_token`) can be issued at the root and covers all child TSGs in
the hierarchy.  In both cases, the `tsg` command lets you change which TSG your session is
targeting **without restarting ARC**.

## Usage

```
tsg                Show the currently active TSG ID
tsg <id>           Switch to a different TSG
```

Press **Tab** after `tsg ` to auto-complete with the TSG ID stored in your ARC config.

## Behaviour by auth type

| Auth type | What `tsg <id>` does |
|-----------|----------------------|
| Bearer token | Updates the session TSG context. The bearer token is used as-is — SCM enforces TSG-level access based on the token scope. |
| OAuth client credentials | Re-authenticates immediately using `client_id` / `client_secret` with the new TSG as the OAuth scope, obtaining a fresh access token. Rolls back on failure. |

## Examples

```
arc > tsg
Active TSG: 1234567890
Config TSG (from arc auth / config.json): 1234567890

arc > tsg 9876543210
TSG context set to: 9876543210

arc > pwd
Context: SCM / global  [API mode]
SCM folder: Shared
TSG: 9876543210
```

## How TSG ID relates to your Palo Alto account

Your TSG ID is visible in the Strata Cloud Manager portal URL and in the service account
setup screen.  It looks like a large decimal number (e.g. `1234567890`).

To configure a default TSG that loads automatically when ARC starts, store it during
initial setup:

```bash
arc auth configure
# When prompted: enter your client_id, client_secret, and tsg_id
```

See `help configuration` for the full config setup guide.

