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
        self._token: str = cfg.bearer_token.strip()
        if not self._token:
            self._authenticate()

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

    def get_folders(self) -> list[str]:
        """Return SCM folder names for tab completion.

        Tries the `/sse/config/v1/folders` endpoint; falls back to common
        defaults if the endpoint is unavailable or returns no data.
        """
        try:
            scm_response = self.get("/sse/config/v1/folders")
            names = [folder.get("name", "") for folder in scm_response.get("data", []) if folder.get("name")]
            return names if names else ["Shared", "Global"]
        except (httpx.HTTPError, ValueError, TypeError):
            return ["Shared", "Global"]

    def get_devices(self, folder: str = "Shared") -> list[dict]:
        scm_response = self.get("/sse/config/v1/devices", params={"folder": folder})
        return scm_response.get("data", [])

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
