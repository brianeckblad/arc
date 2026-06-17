# Security Coding Checklist

## General Secure Coding Baseline — All Apps

Apply these rules to every app, CLI, worker, script, and service.

- **Threat-model before coding** — identify inputs, trust boundaries, secrets, filesystem/network access, destructive actions
- **Validate at boundaries** — parse and validate external input before business logic
- **Authorize server-side** — never trust client-provided user, role, path, tenant, or account identifier
- **Keep secrets out of code** — use environment variables or secrets manager; never commit `.env`, tokens, keys
- **Sanitize logs** — never log credentials, tokens, cookies, passwords, MFA codes, private URLs
- **Avoid dangerous primitives** — no `eval`, `exec`, unsafe deserialization, shell interpolation, raw SQL/XML/HTML concatenation with user input
- **Use safe subprocess calls** — pass argument lists with `shell=False`; never concatenate user input into commands
- **Use timeouts for I/O** — network calls, subprocesses, locks need explicit timeouts
- **Fail closed** — malformed state, missing authorization, expired sessions, invalid config should deny access
- **Prefer least privilege** — credentials, IAM roles, file permissions, API tokens should have only required access
- **Audit dependencies** — pin versions and check for known CVEs before deployment
- **Handle destructive actions carefully** — require explicit confirmation, scope narrowly, log without exposing secrets

## Web App Security — Examples

### Error Responses — Never Leak Internals

```python
# BAD
return jsonify({'error': str(e)}), 500

# GOOD
logger.exception("operation failed")
return jsonify({'error': safe_error_message(e)}), 500
```

### File Upload Validation

```python
# BAD — trusting client
filename = request.files['upload'].filename
path = f"/uploads/{filename}"

# GOOD — sanitize and validate
from werkzeug.utils import secure_filename
from pathlib import Path

filename = secure_filename(request.files['upload'].filename)
if not filename.endswith(('.jpg', '.png')):
    abort(400)
    
base = Path(UPLOAD_DIR).resolve()
target = (base / filename).resolve()
if not target.is_relative_to(base):
    abort(400)
```

### Path Safety

```python
# BAD — path traversal vulnerability
user_path = request.args.get('file')
with open(f"/data/{user_path}") as f:
    return f.read()

# GOOD — confine to base directory
from pathlib import Path
from werkzeug.utils import secure_filename

base = Path("/data").resolve()
safe_name = secure_filename(request.args.get('file'))
target = (base / safe_name).resolve()

if not target.is_relative_to(base):
    abort(400)
    
with open(target) as f:
    return f.read()
```

### Session Security

```python
# Production session cookies must have:
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SECURE=True,      # HTTPS only
    SESSION_COOKIE_SAMESITE='Lax',
    PERMANENT_SESSION_LIFETIME=3600, # 1 hour
)
```

### TOTP / 2FA Rules

- TOTP enrollment **must require the current password** — stolen session alone must not enroll attacker device
- TOTP setup secrets are short-lived; clear pending setup state after success or expiry
- Never log TOTP secrets, QR payloads, or one-time codes
- Implement two-step login: password → `totp_pending`; valid TOTP code → `logged_in=True`
- Pending TOTP sessions expire quickly (≤5 minutes) and are rate-limited separately from password attempts
