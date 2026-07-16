"""User-account SCM login via OAuth 2.0 authorization-code + PKCE (experimental).

SCM's public API is designed around OAuth *client-credentials* (service
accounts).  There is no publicly documented browser flow that mints an SCM API
bearer token for an interactive user login, so this module is **experimental**:
it implements the standard authorization-code + PKCE loopback flow and works
only once a compatible authorization endpoint / client ID / redirect URI is
configured (via the ``ARC_OAUTH_*`` environment variables below).

Configuration (all required to attempt a login) — set via the `oauth` block in
config.json (e.g. `arc auth configure --oauth-*` or `arc gui-configure`), or via
environment variables which override the file:
  ARC_OAUTH_AUTH_URL    — authorization endpoint (browser is sent here)
  ARC_OAUTH_TOKEN_URL   — token endpoint (code is exchanged here)
  ARC_OAUTH_CLIENT_ID   — public OAuth client id
Optional:
  ARC_OAUTH_SCOPE       — space-separated scopes (default: "")
  ARC_OAUTH_REDIRECT_PORT — loopback callback port (default: 4455)

On success returns ``(access_token, expires_in_seconds)``.
"""
from __future__ import annotations

import base64
import hashlib
import logging
import os
import secrets
import threading
import urllib.parse
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Optional

import httpx


class LoginError(Exception):
    """Raised when the user-account login flow cannot complete."""


class LoginConfig:
    """OAuth settings — environment first, then config.json (see module docstring)."""

    def __init__(self) -> None:
        # config.json (non-secret `oauth` block) provides persisted defaults;
        # ARC_OAUTH_* env vars override.  load_config() already folds env over
        # the file, so reading cfg.oauth here yields the fully-resolved values.
        auth_url = token_url = client_id = scope = ""
        redirect_port = 4455
        try:
            from app.config import load_config
            oauth = load_config().oauth
            auth_url, token_url = oauth.auth_url, oauth.token_url
            client_id, scope = oauth.client_id, oauth.scope
            redirect_port = oauth.redirect_port
        except Exception:  # noqa: BLE001 — fall back to env-only below
            pass

        self.auth_url = os.environ.get("ARC_OAUTH_AUTH_URL", auth_url).strip()
        self.token_url = os.environ.get("ARC_OAUTH_TOKEN_URL", token_url).strip()
        self.client_id = os.environ.get("ARC_OAUTH_CLIENT_ID", client_id).strip()
        self.scope = os.environ.get("ARC_OAUTH_SCOPE", scope).strip()
        try:
            self.redirect_port = int(os.environ.get("ARC_OAUTH_REDIRECT_PORT", redirect_port))
        except ValueError:
            self.redirect_port = 4455

    @property
    def redirect_uri(self) -> str:
        return f"http://127.0.0.1:{self.redirect_port}/callback"

    @property
    def configured(self) -> bool:
        return bool(self.auth_url and self.token_url and self.client_id)


def _pkce_pair() -> tuple[str, str]:
    """Return (verifier, challenge) for PKCE S256."""
    verifier = base64.urlsafe_b64encode(secrets.token_bytes(48)).rstrip(b"=").decode()
    digest = hashlib.sha256(verifier.encode()).digest()
    challenge = base64.urlsafe_b64encode(digest).rstrip(b"=").decode()
    return verifier, challenge


class _CallbackServer:
    """One-shot loopback server that captures the ?code= (or ?error=) redirect."""

    def __init__(self, port: int, expected_state: str) -> None:
        self._port = port
        self._state = expected_state
        self.code: Optional[str] = None
        self.error: Optional[str] = None
        self._done = threading.Event()
        outer = self

        class _H(BaseHTTPRequestHandler):
            def log_message(self, *_a):  # noqa: N802
                pass

            def do_GET(self):  # noqa: N802
                parsed = urllib.parse.urlparse(self.path)
                # Only the expected callback path is honoured; ignore stray hits
                # (favicon, probes) so they can't set the result prematurely.
                if parsed.path.rstrip("/") not in ("/callback", ""):
                    self.send_response(404)
                    self.send_header("Content-Length", "0")
                    self.end_headers()
                    return
                q = urllib.parse.parse_qs(parsed.query)
                if (q.get("state") or [""])[0] != outer._state:
                    outer.error = "state mismatch (possible CSRF)"
                elif "error" in q:
                    # Log the provider's detail for debugging; show the user a
                    # generic message (OAuth error_description is developer-facing).
                    detail = (q.get("error_description") or q.get("error") or [""])[0]
                    logging.getLogger(__name__).debug("OAuth callback error: %s", detail)
                    outer.error = "authorization was denied or failed"
                else:
                    outer.code = (q.get("code") or [""])[0] or None
                    if not outer.code:
                        outer.error = "no authorization code in callback"
                body = (
                    b"<!doctype html><meta charset=utf-8><body style='font-family:sans-serif;"
                    b"background:#0B0E1A;color:#D8DCF0;text-align:center;padding:4rem'>"
                    b"<h2>ARC login complete</h2><p>You can close this tab and return to the shell.</p>"
                    b"<script>setTimeout(()=>{try{window.close()}catch(e){}},400)</script></body>"
                )
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                try:
                    self.wfile.write(body)
                except OSError:
                    pass
                outer._done.set()

        self._httpd = HTTPServer(("127.0.0.1", port), _H)

    def wait(self, timeout: float) -> None:
        thread = threading.Thread(target=self._httpd.serve_forever, daemon=True)
        thread.start()
        try:
            if not self._done.wait(timeout):
                self.error = self.error or "timed out waiting for the browser callback"
        finally:
            try:
                self._httpd.shutdown()
                self._httpd.server_close()
            except Exception:  # pragma: no cover
                pass


def run_user_login(timeout: float = 180.0) -> tuple[str, int]:
    """Run the interactive login flow; return (access_token, expires_in).

    Raises :class:`LoginError` when not configured or the flow fails.
    """
    cfg = LoginConfig()
    if not cfg.configured:
        raise LoginError(
            "User-account login is not configured. Set the OAuth endpoints via "
            "`arc auth configure --oauth-auth-url … --oauth-token-url … "
            "--oauth-client-id …` (or `arc gui-configure` → Authentication, or the "
            "ARC_OAUTH_* environment variables)."
        )
    verifier, challenge = _pkce_pair()
    state = secrets.token_urlsafe(16)
    params = {
        "response_type": "code",
        "client_id": cfg.client_id,
        "redirect_uri": cfg.redirect_uri,
        "state": state,
        "code_challenge": challenge,
        "code_challenge_method": "S256",
    }
    if cfg.scope:
        params["scope"] = cfg.scope
    auth_url = cfg.auth_url + ("&" if "?" in cfg.auth_url else "?") + urllib.parse.urlencode(params)

    server = _CallbackServer(cfg.redirect_port, state)
    try:
        webbrowser.open(auth_url)
    except Exception:  # pragma: no cover
        pass
    server.wait(timeout)
    if server.error:
        raise LoginError(server.error)
    if not server.code:
        raise LoginError("login did not return an authorization code")

    data = {
        "grant_type": "authorization_code",
        "code": server.code,
        "redirect_uri": cfg.redirect_uri,
        "client_id": cfg.client_id,
        "code_verifier": verifier,
    }
    try:
        resp = httpx.post(cfg.token_url, data=data, timeout=30)
        resp.raise_for_status()
        payload = resp.json()
    except httpx.HTTPError as exc:
        raise LoginError(f"token exchange failed: {exc}") from exc
    token = payload.get("access_token")
    if not token:
        raise LoginError("token endpoint returned no access_token")
    try:
        expires_in = int(payload.get("expires_in", 3600))
    except (TypeError, ValueError):
        expires_in = 3600
    return token, expires_in
