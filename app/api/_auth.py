"""Shared OAuth client-credentials flow for Palo Alto cloud services.

SCM and SLS authenticate identically — same token endpoint, same TSG-scoped
client-credentials grant. This is the ONE implementation; SCMClient and
SLSClient wrap it with their own error types and messages.
"""

from __future__ import annotations

import httpx

# pan.dev: openapi-specs/scm/auth/AuthService.yaml
AUTH_URL = "https://auth.apps.paloaltonetworks.com/auth/v1/oauth2/access_token"


def oauth_token(http: httpx.Client, client_id: str, client_secret: str, tsg_id: str) -> tuple[str, int]:
    """Mint a TSG-scoped bearer token via the client-credentials grant.

    Returns ``(access_token, expires_in)`` where *expires_in* is the token's real
    lifetime in seconds from the endpoint (0 when the response omits it — callers
    then treat the expiry as unknown and do not record a fake one).

    Raises httpx.HTTPStatusError on auth failure and ValueError when the
    response carries no token — callers translate both into their own
    service-specific error types with actionable messages.
    """
    resp = http.post(
        AUTH_URL,
        data={
            "grant_type": "client_credentials",
            "scope": f"tsg_id:{tsg_id}",
        },
        auth=(client_id, client_secret),
    )
    resp.raise_for_status()
    payload = resp.json()
    token = payload.get("access_token", "")
    if not token:
        raise ValueError("auth endpoint returned no access_token")
    try:
        expires_in = int(payload.get("expires_in", 0) or 0)
    except (TypeError, ValueError):
        expires_in = 0
    return str(token), expires_in
