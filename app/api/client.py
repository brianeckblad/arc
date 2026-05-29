"""Strata Cloud Manager REST API client.

All endpoint paths and base URLs are sourced directly from the pan.dev
OpenAPI specifications:

  https://pan.dev/scm/api/

Gateway map (from the OpenAPI ``servers`` field in each spec):

  Objects  (addresses, services, tags, …)
    https://api.strata.paloaltonetworks.com/config/objects/v1
    Spec: openapi-specs/scm/config/ngfw/objects/objects_v1.3_feb.yaml

  Security (security-rules, url-categories, decryption, …)
    https://api.strata.paloaltonetworks.com/config/security/v1
    Spec: openapi-specs/scm/config/ngfw/security/security-services-R2-2026.yaml

  Setup    (devices, folders, snippets, labels, …)
    https://api.strata.paloaltonetworks.com/config/setup/v1
    Spec: openapi-specs/scm/config/ngfw/setup/config-setup-feb-v1.yaml

  IAM / Tenancy
    https://api.sase.paloaltonetworks.com
    Spec: openapi-specs/scm/iam/ServiceAccounts.yaml
          openapi-specs/scm/tenancy/TenantServiceGroup.yaml

  Authentication
    https://auth.apps.paloaltonetworks.com/auth/v1/oauth2/access_token
    Spec: openapi-specs/scm/auth/AuthService.yaml
"""

from __future__ import annotations

from typing import Any, Optional

import httpx

from app.config import SCMConfig


class SCMError(Exception):
    """Raised when SCM authentication or API requests fail."""


class SCMClient:
    """Strata Cloud Manager (SCM) REST API client.

    Uses three separate base URLs sourced from pan.dev OpenAPI specs —
    all share the same OAuth bearer token.
    """

    # pan.dev: openapi-specs/scm/auth/AuthService.yaml
    AUTH_URL = "https://auth.apps.paloaltonetworks.com/auth/v1/oauth2/access_token"

    # pan.dev: openapi-specs/scm/config/ngfw/objects/objects_v1.3_feb.yaml
    OBJECTS_URL = "https://api.strata.paloaltonetworks.com/config/objects/v1"

    # pan.dev: openapi-specs/scm/config/ngfw/security/security-services-R2-2026.yaml
    SECURITY_URL = "https://api.strata.paloaltonetworks.com/config/security/v1"

    # pan.dev: openapi-specs/scm/config/ngfw/setup/config-setup-feb-v1.yaml
    SETUP_URL = "https://api.strata.paloaltonetworks.com/config/setup/v1"

    # pan.dev: openapi-specs/scm/iam/ServiceAccounts.yaml
    #          openapi-specs/scm/tenancy/TenantServiceGroup.yaml
    IAM_URL = "https://api.sase.paloaltonetworks.com"

    # Keep BASE_URL pointing at the sase gateway for backward-compat with
    # any callers that use the generic .get() / .post() methods directly.
    BASE_URL = "https://api.sase.paloaltonetworks.com"

    def __init__(self, cfg: SCMConfig) -> None:
        self._cfg = cfg
        self._http = httpx.Client(timeout=30)
        self._token: str = ""

        # Auth priority:
        #   1. OAuth client credentials (client_id + client_secret + tsg_id) — always
        #      preferred; produces a fresh token scoped to the correct TSG.
        #   2. Pre-issued bearer token — only when no client credentials exist.
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
        """Obtain an OAuth token via the client-credentials flow.

        pan.dev ref: https://pan.dev/scm/api/auth/post-auth-v-1-oauth-2-access-token/
        """
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

    # ------------------------------------------------------------------
    # Generic request helpers
    # ------------------------------------------------------------------

    def get(self, path: str, params: Optional[dict] = None) -> Any:
        """GET against the IAM/sase gateway (api.sase.paloaltonetworks.com)."""
        resp = self._http.get(
            f"{self.BASE_URL}{path}",
            headers=self._headers(),
            params=params,
        )
        resp.raise_for_status()
        return resp.json()

    def post(self, path: str, json: Optional[dict] = None) -> Any:
        """POST against the IAM/sase gateway."""
        resp = self._http.post(
            f"{self.BASE_URL}{path}",
            headers=self._headers(),
            json=json,
        )
        resp.raise_for_status()
        return resp.json()

    def _get_objects(self, path: str, params: Optional[dict] = None) -> Any:
        """GET from api.strata.paloaltonetworks.com/config/objects/v1."""
        resp = self._http.get(
            f"{self.OBJECTS_URL}{path}",
            headers=self._headers(),
            params=params,
        )
        resp.raise_for_status()
        return resp.json()

    def _get_security(self, path: str, params: Optional[dict] = None) -> Any:
        """GET from api.strata.paloaltonetworks.com/config/security/v1."""
        resp = self._http.get(
            f"{self.SECURITY_URL}{path}",
            headers=self._headers(),
            params=params,
        )
        resp.raise_for_status()
        return resp.json()

    def _get_setup(self, path: str, params: Optional[dict] = None) -> Any:
        """GET from api.strata.paloaltonetworks.com/config/setup/v1."""
        resp = self._http.get(
            f"{self.SETUP_URL}{path}",
            headers=self._headers(),
            params=params,
        )
        resp.raise_for_status()
        return resp.json()

    # Keep the public alias used by shell.py _cmd_tsg and auth_test
    def get_setup(self, path: str, params: Optional[dict] = None) -> Any:
        """Public alias for _get_setup — kept for backward compatibility."""
        return self._get_setup(path, params)

    # ------------------------------------------------------------------
    # TSG switching
    # ------------------------------------------------------------------

    def reauthenticate(self, tsg_id: str) -> None:
        """Obtain a fresh OAuth token scoped to a different TSG.

        Used by the ``tsg <id>`` shell command.
        """
        if not (self._cfg.client_id and self._cfg.client_secret):
            raise SCMError(
                "Cannot re-authenticate: no client_id / client_secret configured. "
                "TSG switching requires OAuth client credentials."
            )
        import copy  # Deferred: avoids import at module level for a rarely-called path
        new_cfg = copy.copy(self._cfg)
        new_cfg.tsg_id = tsg_id
        self._cfg = new_cfg
        self._http.close()
        self._http = httpx.Client(timeout=30)
        self._authenticate()

    # ------------------------------------------------------------------
    # Tenancy / IAM  (api.sase.paloaltonetworks.com)
    # pan.dev: https://pan.dev/scm/api/tenancy/
    # ------------------------------------------------------------------

    def get_tenants(self) -> list[dict]:
        """Return child TSG entries.

        pan.dev: GET /tenancy/v1/tenant_service_groups/{tsg_id}/operations/list_children
        Fallback: GET /tenancy/v1/tenant_service_groups (list all visible)

        Returns [] on any permission error so callers can handle gracefully.
        """
        # Strategy 1: list children of current TSG
        if self._cfg.tsg_id:
            try:
                resp = self._http.get(
                    f"{self.IAM_URL}/tenancy/v1/tenant_service_groups"
                    f"/{self._cfg.tsg_id}/operations/list_children",
                    headers=self._headers(),
                )
                if resp.status_code < 400:
                    data = resp.json()
                    entries = data.get("data", data.get("items", []))
                    if entries:
                        return entries
            except (httpx.HTTPError, ValueError, TypeError):
                pass

        # Strategy 2: flat list of all visible TSGs
        try:
            resp = self._http.get(
                f"{self.IAM_URL}/tenancy/v1/tenant_service_groups",
                headers=self._headers(),
            )
            if resp.status_code < 400:
                data = resp.json()
                return data.get("data", data.get("items", []))
        except (httpx.HTTPError, ValueError, TypeError):
            pass

        return []

    # ------------------------------------------------------------------
    # Setup  (api.strata.paloaltonetworks.com/config/setup/v1)
    # pan.dev: https://pan.dev/scm/api/config/cloudngfw/setup/
    # ------------------------------------------------------------------

    def get_devices(self, folder: str = "Shared") -> list[dict]:
        """Return managed NGFW devices.

        pan.dev: GET /config/setup/v1/devices
        Spec: openapi-specs/scm/config/ngfw/setup/config-setup-feb-v1.yaml

        The folder param is accepted for interface compatibility; the endpoint
        returns all visible devices regardless of folder.
        Returns [] on 403 so callers can handle quietly.
        """
        try:
            data = self._get_setup("/devices")
            return data.get("data", [])
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code == 403:
                return []
            raise
        except (httpx.HTTPError, ValueError, TypeError):
            return []

    def get_folders(self) -> list[str]:
        """Return folder names for tab completion.

        pan.dev: GET /config/setup/v1/folders
        Spec: openapi-specs/scm/config/ngfw/setup/config-setup-feb-v1.yaml

        Falls back to common defaults on any error.
        """
        try:
            data = self._get_setup("/folders")
            names = [f.get("name", "") for f in data.get("data", []) if f.get("name")]
            return names if names else ["Shared", "Global"]
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code in (403, 404):
                return ["Shared", "Global"]
            raise
        except (httpx.HTTPError, ValueError, TypeError):
            return ["Shared", "Global"]

    # ------------------------------------------------------------------
    # Objects  (api.strata.paloaltonetworks.com/config/objects/v1)
    # pan.dev: https://pan.dev/scm/api/config/cloudngfw/objects/
    # Spec: openapi-specs/scm/config/ngfw/objects/objects_v1.3_feb.yaml
    # ------------------------------------------------------------------

    def get_addresses(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/objects/v1/addresses"""
        data = self._get_objects("/addresses", params={"folder": folder})
        return data.get("data", [])

    def get_address_groups(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/objects/v1/address-groups"""
        data = self._get_objects("/address-groups", params={"folder": folder})
        return data.get("data", [])

    def get_services(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/objects/v1/services"""
        data = self._get_objects("/services", params={"folder": folder})
        return data.get("data", [])

    def get_tags(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/objects/v1/tags"""
        data = self._get_objects("/tags", params={"folder": folder})
        return data.get("data", [])

    def get_external_dynamic_lists(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/objects/v1/external-dynamic-lists"""
        data = self._get_objects("/external-dynamic-lists", params={"folder": folder})
        return data.get("data", [])

    # ------------------------------------------------------------------
    # Security  (api.strata.paloaltonetworks.com/config/security/v1)
    # pan.dev: https://pan.dev/scm/api/config/cloudngfw/security/
    # Spec: openapi-specs/scm/config/ngfw/security/security-services-R2-2026.yaml
    # ------------------------------------------------------------------

    def get_security_policy(self, folder: str = "Shared", position: str = "pre") -> list[dict]:
        """pan.dev: GET /config/security/v1/security-rules"""
        data = self._get_security(
            "/security-rules",
            params={"folder": folder, "position": position},
        )
        return data.get("data", [])

    def get_url_categories(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/security/v1/url-categories"""
        data = self._get_security("/url-categories", params={"folder": folder})
        return data.get("data", [])

    def get_dns_security_profiles(self, folder: str = "Shared") -> list[dict]:
        """pan.dev: GET /config/security/v1/dns-security-profiles"""
        data = self._get_security("/dns-security-profiles", params={"folder": folder})
        return data.get("data", [])

    def close(self) -> None:
        self._http.close()
