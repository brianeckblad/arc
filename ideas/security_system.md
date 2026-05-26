# ARC Security & Licensing System — Design Idea

**Status:** Concept / Not Implemented  
**Author:** Brian Eckblad  
**Date:** 2026-05-25

---

## Overview

ARC currently has no access control — anyone with the source code can run it.
This document outlines a design for a **registration-based licensing system** that:

- Requires email registration to obtain a cryptographic license key
- Stores the key locally at `~/.arc/arc.key`
- Verifies the key **against a live backend on every startup** — no internet = no launch
- Expires keys on a schedule (30/90/365-day tiers)
- Self-destructs the installation when a key is missing, invalid, expired, or revoked

---

## Goals

| Goal | Description |
|------|-------------|
| **Access control** | Only registered users with a valid, non-expired key can run ARC |
| **Always-online** | ARC will not start without a successful network verification call |
| **Self-healing revocation** | Bad/expired key triggers immediate self-deletion of the ARC installation |
| **Tamper resistance** | Removing or patching the verification code should still fail due to server-side enforcement |
| **Audit trail** | Every verification attempt is logged server-side (email, IP, timestamp, result) |

---

## Key Concepts

### License Key Format

Keys are **signed JWTs** (JSON Web Tokens) using RS256 (asymmetric — only the server can issue, anyone can verify the signature with the public key).

```
Header:  { "alg": "RS256", "kid": "arc-2026-01" }
Payload: {
  "sub":  "test@zerouptime.io",          // registered email
  "jti":  "a1b2c3d4-...",               // unique key ID (for revocation)
  "iat":  1748217600,                    // issued at (Unix timestamp)
  "exp":  1756080000,                    // expiry (Unix timestamp)
  "tier": "pro",                         // free | pro | enterprise
  "iss":  "https://keys.arc-cli.io"      // issuer
}
Signature: RS256(header.payload, PRIVATE_KEY)
```

The key file at `~/.arc/arc.key` contains the raw JWT string (single line, no newlines).

### Verification Flow

Every ARC startup calls a **live verification endpoint** — the local key alone is not enough.
The server checks:

1. JWT signature is valid (not tampered with)
2. `exp` claim has not passed
3. `jti` is not in the server-side revocation list
4. The IP/device fingerprint is not flagged for abuse

If all checks pass → server returns `200 { "status": "ok", "ttl_seconds": 86400 }`.  
Any failure → server returns a non-200 response → ARC triggers self-deletion.

---

## System Components

### 1. Registration Portal / API

A lightweight web service (could be a serverless function — AWS Lambda, Cloudflare Worker, etc.).

```
POST /register
Body: { "email": "test@zerouptime.io", "tier": "free" }

→ Generates a signed JWT with a 30-day expiry (free tier)
→ Emails the key to the address (SendGrid / SES)
→ Stores { jti, email, tier, issued_at, expires_at, revoked: false } in a database
→ Returns: { "message": "Check your email for your ARC license key." }
```

The key is **sent by email only** — never displayed in the API response itself.  
This ensures the email address is valid and owned by the requester.

### 2. Verification Endpoint

Called by ARC on every startup (and optionally every N hours during a long session).

```
POST /verify
Headers: Authorization: Bearer <arc.key contents>

→ Server decodes the JWT, checks signature, expiry, revocation list
→ 200: { "status": "ok",       "email": "...", "ttl_seconds": 86400 }
→ 401: { "status": "expired",  "reason": "Key expired 2026-05-01" }
→ 403: { "status": "revoked",  "reason": "Key revoked by admin" }
→ 503: (network error or timeout — triggers offline-mode failure)
```

### 3. Revocation Endpoint (Admin)

```
POST /revoke
Headers: X-Admin-Secret: <admin_token>
Body: { "jti": "a1b2c3d4-...", "reason": "TOS violation" }
```

Marks the key as revoked in the database. Within seconds, any running ARC instance
that calls `/verify` will receive a `403` and self-destruct.

### 4. Key Renewal

```
POST /renew
Headers: Authorization: Bearer <current arc.key>
Body: { "email": "test@zerouptime.io" }

→ If the current key is valid and within 7 days of expiry:
   - Issues a new key, emails it
   - Invalidates the old jti
→ If already expired: user must re-register
```

---

## ARC Client Integration

### New file: `app/auth/license.py`

Responsible for:
- Reading `~/.arc/arc.key`
- Calling `/verify` at startup
- Triggering self-deletion on failure

```python
VERIFY_URL      = "https://keys.arc-cli.io/verify"
KEY_PATH        = Path.home() / ".arc" / "arc.key"
VERIFY_TIMEOUT  = 8           # seconds — fail closed if network is slow
MAX_RETRIES     = 1           # one retry on network error, then fail
```

#### Startup check pseudocode

```python
def check_license() -> None:
    """
    Called once at ARC startup, before the shell launches.
    Raises SystemExit and triggers self-deletion on any failure.
    """
    # 1. Key file must exist
    if not KEY_PATH.exists():
        _fail("No license key found. Run: arc register <your@email.com>")

    key = KEY_PATH.read_text().strip()

    # 2. Must be able to reach the verification server
    try:
        resp = httpx.post(VERIFY_URL, headers={"Authorization": f"Bearer {key}"}, timeout=VERIFY_TIMEOUT)
    except (httpx.ConnectError, httpx.TimeoutException):
        _fail("ARC requires internet connectivity to verify your license. "
              "Check your network and try again.", delete=False)
        # NOTE: network errors do NOT trigger deletion — only auth failures do.

    # 3. Non-200 = revoked, expired, or invalid → self-destruct
    if resp.status_code != 200:
        reason = resp.json().get("reason", "License invalid")
        _fail(f"License check failed: {reason}", delete=True)
```

#### Self-deletion pseudocode

```python
def _fail(message: str, delete: bool = False) -> None:
    """Print the failure reason, optionally wipe the ARC installation, then exit."""
    console.print(f"\n[red bold]ARC License Error:[/red bold] {message}\n")

    if delete:
        _self_destruct()

    raise SystemExit(1)


def _self_destruct() -> None:
    """
    Delete the ARC installation.

    Targets:
      - The ARC package directory (site-packages or editable install path)
      - ~/.arc/   (config, key, cache)
      - The `arc` console-script entry point (if locatable via shutil.which)
      - Optionally: the uv-managed project directory (if ARC_PROJECT_DIR is set)

    Does NOT delete:
      - Files outside the ARC install scope
      - SSH keys or other unrelated ~/.ssh/ contents
    """
    import shutil, site

    arc_package = Path(__file__).resolve().parents[2]  # points to the arc/ project root
    arc_config  = Path.home() / ".arc"

    console.print("[red]Wiping ARC installation…[/red]")

    # Remove config + key
    if arc_config.exists():
        shutil.rmtree(arc_config, ignore_errors=True)

    # Remove the console-script symlink / wrapper
    arc_bin = shutil.which("arc")
    if arc_bin:
        Path(arc_bin).unlink(missing_ok=True)

    # Remove the package itself — last so error messages still render
    shutil.rmtree(arc_package, ignore_errors=True)

    console.print("[red]ARC has been removed. Contact support to renew your license.[/red]")
```

### New CLI command: `arc register`

```
arc register test@zerouptime.io
```

Calls `POST /register`, prints:

```
✓ Registration submitted for test@zerouptime.io
  Check your email for your ARC license key.
  Once received, save it with:

  arc install-key <paste-key-here>
```

### New CLI command: `arc install-key`

```
arc install-key eyJhbGci...
```

Writes the key to `~/.arc/arc.key` (mode 600), then immediately calls `/verify` to
confirm it works before accepting it.

---

## Startup Flow (Full Picture)

```
arc (launched)
  │
  ├─ check_license()
  │     │
  │     ├─ ~/.arc/arc.key missing?
  │     │     └─→ print "No key" + exit(1)   [NO deletion — user just needs to register]
  │     │
  │     ├─ POST https://keys.arc-cli.io/verify
  │     │     │
  │     │     ├─ Network unreachable / timeout?
  │     │     │     └─→ print "No internet" + exit(1)   [NO deletion — could be temporary]
  │     │     │
  │     │     ├─ 200 OK?
  │     │     │     └─→ continue to shell ✓
  │     │     │
  │     │     ├─ 401 Expired?
  │     │     │     └─→ print reason + SELF-DESTRUCT
  │     │     │
  │     │     └─ 403 Revoked / 4xx/5xx auth error?
  │     │           └─→ print reason + SELF-DESTRUCT
  │     │
  │     └─ TTL caching: store last-verified timestamp in ~/.arc/verify.cache
  │           Re-verify at most once per hour during active sessions
  │           (but always verify on cold start)
  │
  └─ ArcShell.run()
```

---

## Self-Deletion Scope

What gets deleted:

| Path | Why |
|------|-----|
| `~/.arc/` | Config, key, cache — all ARC runtime state |
| The `arc` binary / console-script | Removes the entry point |
| The ARC Python package directory | Removes all source code |
| `uv` project directory (if `ARC_PROJECT_DIR` env is set) | Optional — only if explicitly configured |

What is **never** deleted:

| Path | Why not |
|------|---------|
| `~/.ssh/` | SSH keys belong to the user, not ARC |
| Any directory outside the ARC install scope | Least-privilege principle |
| Other Python packages / site-packages | Would break unrelated tools |

---

## Offline / Grace Period Policy

| Scenario | Behavior |
|----------|----------|
| No network on cold start | Refuse to launch. Print clear message. **No deletion.** |
| Network drops mid-session | Continue current session. Re-verify on next cold start. |
| Key missing | Refuse to launch. Prompt to register. **No deletion.** |
| Key expired | Delete installation. Print support contact. |
| Key revoked | Delete installation. Print support contact. |
| Verification server down (5xx) | Treat as network error — refuse but **do not delete** |
| Key within 7 days of expiry | Warn user on startup: "Your key expires in N days. Run `arc renew`." |

**Rationale:** Deletion is reserved strictly for authentication failures (expired/revoked).
Transient network issues should not destroy a legitimate user's install.

---

## Security Hardening Considerations

### Server-side

- **Rate limit** `/verify` per IP (e.g. 60 req/hour) to prevent enumeration
- **Rate limit** `/register` per IP and email domain to prevent bulk signups
- **Short-lived tokens** — even "enterprise" keys expire in 365 days max; no perpetual keys
- **Key ID (`jti`) is random UUID** — not derivable from email or timestamp
- **Verify endpoint is HTTPS only** — no HTTP fallback
- **Audit log** every verification with IP, user-agent, result — stored for 90 days

### Client-side

- `arc.key` file permissions enforced to `600` (owner read/write only) on write
- Key is never logged or printed in full — only the `sub` (email) claim is shown
- `ARC_DEBUG=1` does NOT print the key contents
- The self-destruct function runs in a `try/finally` to ensure it completes even if
  the console print raises an exception

### Anti-tamper notes

This design does **not** attempt to prevent a determined developer from patching out
the license check (the source is accessible). The goal is:

1. Casual / accidental unauthorized use is blocked
2. Revocation reaches every legitimate user within hours (no offline bypass)
3. Server-side audit provides visibility into who is using the tool

For stronger tamper resistance, compiled distribution (PyInstaller, Nuitka) or an
obfuscated entry-point wrapper would be needed — that is out of scope for this idea.

---

## Database Schema (Server-Side)

```sql
-- Minimal Postgres / SQLite schema

CREATE TABLE licenses (
    jti         TEXT PRIMARY KEY,          -- JWT ID (UUID)
    email       TEXT NOT NULL,
    tier        TEXT NOT NULL DEFAULT 'free',
    issued_at   TIMESTAMPTZ NOT NULL,
    expires_at  TIMESTAMPTZ NOT NULL,
    revoked     BOOLEAN NOT NULL DEFAULT FALSE,
    revoke_reason TEXT,
    last_verified TIMESTAMPTZ,
    verify_count  INTEGER DEFAULT 0
);

CREATE INDEX idx_licenses_email ON licenses(email);
```

---

## Tier Structure (Example)

| Tier | Duration | Price | Notes |
|------|----------|-------|-------|
| `free` | 30 days | $0 | Renewable; limited to 1 device fingerprint |
| `pro` | 365 days | $X/year | Multiple devices; priority support |
| `enterprise` | 365 days | Custom | Bulk keys; custom domain allow-list; audit export |

---

## Open Questions

- **Key file location:** `~/.arc/arc.key` vs `~/.ssh/arc.key` (user asked for `~/.ssh/arc.key`) — `~/.arc/arc.key` is preferred to keep ARC state scoped to its own directory; `~/.ssh/` should remain for SSH keys only.
- **Device binding:** Should a key be locked to a device fingerprint (MAC, hostname hash)? Pros: prevents key sharing. Cons: breaks legitimate re-installs after hardware change.
- **Offline grace window:** Could allow a 24-hour grace window after the last successful online verify (store encrypted timestamp in `~/.arc/verify.cache`) — reduces friction on flaky networks without eliminating the online requirement entirely.
- **Deletion notification:** Should ARC email the user when it self-destructs? Requires the server to know deletion happened, which means a `DELETE /license/<jti>` call — but if the client is about to be deleted, this call may not be made reliably.
- **Renewal UX:** Should `arc renew` work in-place (no email re-send) or always trigger an email flow? In-place renewal is smoother but requires the old key to still be valid.
- **Backend hosting:** A simple Cloudflare Worker + D1 (SQLite) would be zero-cost for low volume and globally edge-distributed, making verification fast from anywhere.

---

## Summary

This system enforces that ARC is:

1. **Registered** — tied to a real email address
2. **Online** — cannot function without a live verification call to `keys.arc-cli.io`
3. **Time-limited** — keys expire; renewal is explicit and intentional
4. **Self-revoking** — an expired or revoked key causes ARC to delete itself rather than degrade gracefully

The design prioritizes **simplicity of the server side** (a single HTTPS endpoint, a small database) and **clarity of the client behavior** (fail closed, no ambiguous states, explicit deletion).

