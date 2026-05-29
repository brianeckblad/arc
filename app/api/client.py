"""Strata Cloud Manager REST API client."""

from __future__ import annotations

from typing import Any, Optional

import httpx

from app.config import SCMConfig


class SCMError(Exception):
    """Raised when SCM authentication or API requests fail."""


class SCMClient:
    """Strata Cloud Manager (SCM) REST API client.

    ARC is SCM-only for API calls. Device-local execution is handled separately
    through SSH. A configured bearer token is used directly; otherwise ARC uses
    OAuth client credentials to obtain one.
    """

    AUTH_URL = "https://auth.apps.paloaltonetworks.com/oauth2/access_token"
    BASE_URL = "https://api.sase.paloaltonetworks.com"

    def __init__(self, cfg: SCMConfig) -> None:
        self._cfg = cfg
        self._http = httpx.Client(timeout=30)
        self._token: str = ""

        # Auth priority:
        #   1. OAuth client credentials (client_id + client_secret + tsg_id) — always
        #      preferred because they produce a fresh token scoped to the correct TSG.
        #   2. Pre-issued bearer token — used only when no client credentials are
        #      configured (e.g. a short-lived token supplied for testing).
        #
        # Reason: a bearer token stored in the keychain may be stale or scoped to a
        # different TSG.  Client credentials are the standard service-account flow and
        # always produce a valid, correctly-scoped token.
        if cfg.client_id and cfg.client_secret and cfg.tsg_id:
            self._authenticate()
        elif cfg.bearer_token.strip():
            self._token = cfg.bearer_token.strip()
        else:
            raise SCMError(
                "SCM is not configured. Provide client_id + client_secret + tsg_id "
                "(recommended), or a pre-issued SCM_BEARER_TOKEN."
            )

    def _authenticate(self) -> None:
        if not (self._cfg.client_id and self._cfg.client_secret and self._cfg.tsg_id):
            raise SCMError(
                "SCM is not configured. Set SCM_BEARER_TOKEN, or set "
                "SCM_CLIENT_ID / SCM_CLIENT_SECRET / SCM_TSG_ID."
            )

        resp = self._http.post(
            self.AUTH_URL,
            data={
                "grant_type": "client_credentials",
                "scope": f"tsg_id:{self._cfg.tsg_id}",
            },
            auth=(self._cfg.client_id, self._cfg.client_secret),
        )
        try:
            resp.raise_for_status()
        except httpx.HTTPStatusError as exc:
            raise SCMError(f"SCM authentication failed: {exc}") from exc
        self._token = resp.json().get("access_token", "")
        if not self._token:
            raise SCMError("SCM auth returned no access_token.")

    def _headers(self) -> dict[str, str]:
        return {"Authorization": f"Bearer {self._token}"}

    def get(self, path: str, params: Optional[dict] = None) -> Any:
        resp = self._http.get(
            f"{self.BASE_URL}{path}",
            headers=self._headers(),
            params=params,
        )
        resp.raise_for_status()
        return resp.json()

    def post(self, path: str, json: Optional[dict] = None) -> Any:
        resp = self._http.post(
            f"{self.BASE_URL}{path}",
            headers=self._headers(),
            json=json,
        )
        resp.raise_for_status()
        return resp.json()

    def reauthenticate(self, tsg_id: str) -> None:
        """Obtain a fresh OAuth token scoped to a different TSG.

        Used by the ``tsg <id>`` shell command to switch context without
        creating a new client.  Closes the current HTTP session and opens
        a new one so there are no stale connection-level state issues.
        """
        if not (self._cfg.client_id and self._cfg.client_secret):
            raise SCMError(
                "Cannot re-authenticate: no client_id / client_secret configured. "
                "TSG switching requires OAuth client credentials."
            )
        # Swap the TSG on a copy of the config so the original is unchanged.
        import copy  # Deferred: avoids import at module level for a rarely-called path
        new_cfg = copy.copy(self._cfg)
        new_cfg.tsg_id = tsg_id
        self._cfg = new_cfg
        # Re-open HTTP client to avoid any connection-level caching issues.
        self._http.close()
        self._http = httpx.Client(timeout=30)
        self._authenticate()

    def get_tenants(self) -> list[dict]:
        """Return child TSG entries visible to the current token.

        Tries two strategies ordered by permission requirement:

        1. ``GET /iam/v1/tenants`` — lists all tenants the token can see.
        2. ``GET /iam/v1/tenants?parent_id=<tsg_id>`` — scoped to direct
           children of the configured TSG (useful when the token lacks
           global IAM read but does have tenant-scoped read).

        Returns a list of dicts; each has at minimum ``id`` and
        ``display_name`` (or ``name``).  Returns [] on any failure so
        callers can fall back gracefully.
        """
        # Strategy 1: unscoped list
        try:
            resp = self.get("/iam/v1/tenants")
            entries = resp.get("data", []) or []
            if entries:
                return entries
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code not in (403, 404):
                return []
            # 403/404 — fall through to strategy 2
        except (httpx.HTTPError, ValueError, TypeError):
            return []

        # Strategy 2: scoped to parent TSG
        if self._cfg.tsg_id:
            try:
                resp = self.get("/iam/v1/tenants", params={"parent_id": self._cfg.tsg_id})
                entries = resp.get("data", []) or []
                if entries:
                    return entries
            except (httpx.HTTPError, ValueError, TypeError):
                pass

        return []

    def get_folders(self) -> list[str]:
        """Return SCM folder names for tab completion.

        Tries the ``/sse/config/v1/folders`` endpoint.  Falls back to common
        defaults if the endpoint is unavailable or returns a 403/404 (some
        read-only service accounts do not have folder-list permission).
        """
        try:
            scm_response = self.get("/sse/config/v1/folders")
            names = [
                f.get("name", "")
                for f in scm_response.get("data", [])
                if f.get("name")
            ]
            return names if names else ["Shared", "Global"]
        except httpx.HTTPStatusError as exc:
            # 403/404 = no permission or endpoint absent — use safe defaults.
            if exc.response.status_code in (403, 404):
                return ["Shared", "Global"]
            raise
        except (httpx.HTTPError, ValueError, TypeError):
            return ["Shared", "Global"]

    def get_devices(self, folder: str = "Shared") -> list[dict]:
        """Return managed devices. Returns [] on 403 so callers can handle quietly."""
        try:
            scm_response = self.get("/sse/config/v1/devices", params={"folder": folder})
            return scm_response.get("data", [])
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code == 403:
                return []
            raise

    def get_addresses(self, folder: str = "Shared") -> list[dict]:
        scm_response = self.get("/sse/config/v1/addresses", params={"folder": folder})
        return scm_response.get("data", [])

    def get_address_groups(self, folder: str = "Shared") -> list[dict]:
        scm_response = self.get("/sse/config/v1/address-groups", params={"folder": folder})
        return scm_response.get("data", [])

    def get_services(self, folder: str = "Shared") -> list[dict]:
        scm_response = self.get("/sse/config/v1/services", params={"folder": folder})
        return scm_response.get("data", [])

    def get_security_policy(self, folder: str = "Shared", position: str = "pre") -> list[dict]:
        scm_response = self.get(
            "/sse/config/v1/security-rules",
            params={"folder": folder, "position": position},
        )
        return scm_response.get("data", [])

    def close(self) -> None:
        self._http.close()
