"""Config loader — reads from environment variables and ~/.arc/config.json.

Sensitive credentials (bearer tokens, client secrets, SSH passwords) are
stored in the OS keychain via the ``keyring`` library:

  - macOS  : Keychain
  - Linux  : Secret Service (GNOME Keyring / KWallet)
  - Windows: Windows Credential Manager

Non-sensitive values (client_id, tsg_id, default_folder, SSH user/key/port)
remain in ``~/.arc/config.json``, which is always written with mode 0600.

Environment variables override both the keychain and the config file —
useful for CI/CD and short-lived overrides without touching stored values.
"""

from __future__ import annotations

import json
import logging
import os
import stat
from dataclasses import dataclass, field
from pathlib import Path

import keyring
import keyring.errors
import platformdirs

logger = logging.getLogger(__name__)

CONFIG_DIR = Path(platformdirs.user_config_dir("arc"))
CONFIG_FILE = CONFIG_DIR / "config.json"

# Keychain service name and per-credential usernames.
# Keep these stable — changing them silently orphans stored secrets.
_KEYCHAIN_SERVICE = "arc"
_KEY_SCM_BEARER    = "scm.bearer_token"
_KEY_SCM_SECRET    = "scm.client_secret"
_KEY_SSH_PASSWORD  = "ssh.password"


class ConfigSecurityError(Exception):
    """Raised when ARC refuses to persist secrets insecurely."""


# ---------------------------------------------------------------------------
# Keychain helpers
# ---------------------------------------------------------------------------

def _keychain_get(key: str) -> str:
    """Return a credential from the OS keychain, or '' if absent / unavailable."""
    try:
        value = keyring.get_password(_KEYCHAIN_SERVICE, key)
        return value or ""
    except keyring.errors.KeyringError as exc:
        logger.debug("Keychain read failed for %s: %s", key, exc)
        return ""


def _keychain_set(key: str, value: str) -> bool:
    """Store *value* in the OS keychain.  Returns True on success.

    An empty value deletes the entry rather than storing a blank secret.
    """
    try:
        if value:
            keyring.set_password(_KEYCHAIN_SERVICE, key, value)
        else:
            _keychain_delete(key)
        return True
    except keyring.errors.KeyringError as exc:
        logger.warning("Keychain write failed for %s: %s", key, exc)
        return False


def _keychain_delete(key: str) -> None:
    """Remove a credential from the keychain.  Silently ignores missing entries."""
    try:
        keyring.delete_password(_KEYCHAIN_SERVICE, key)
    except keyring.errors.PasswordDeleteError:
        pass  # already absent — not an error
    except keyring.errors.KeyringError as exc:
        logger.debug("Keychain delete failed for %s: %s", key, exc)


def keychain_available() -> bool:
    """Return True when the OS keychain can be read/written.

    Used by ``arc auth show`` to surface a warning in headless environments
    where secrets must be supplied through environment variables instead.
    """
    try:
        keyring.get_password(_KEYCHAIN_SERVICE, "__probe__")
        return True
    except keyring.errors.KeyringError:
        return False


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class SCMConfig:
    """SCM API credentials.

    ARC supports either a pre-issued bearer token or OAuth client credentials.
    A bearer token takes precedence when both are present.

    Secrets (bearer_token, client_secret) are stored in the OS keychain.
    client_id and tsg_id are non-sensitive identifiers stored in config.json.
    """

    bearer_token: str = ""
    client_id: str = ""
    client_secret: str = ""
    tsg_id: str = ""

    @property
    def is_configured(self) -> bool:
        return bool(self.bearer_token or (self.client_id and self.client_secret and self.tsg_id))


@dataclass
class SSHConfig:
    """SSH connection defaults.

    ``password`` (if used) is stored in the OS keychain.
    All other fields are non-sensitive and stored in config.json.
    """

    user: str = "admin"
    key_path: str = ""
    password: str = ""
    port: int = 22


@dataclass
class ArcConfig:
    scm: SCMConfig = field(default_factory=SCMConfig)
    ssh: SSHConfig = field(default_factory=SSHConfig)
    debug: bool = False
    default_folder: str = "Shared"


# ---------------------------------------------------------------------------
# Load / save
# ---------------------------------------------------------------------------

def load_config() -> ArcConfig:
    """Load config from keychain + config file, then overlay environment variables.

    Priority (later overrides earlier):
      1. OS keychain (for secrets)
      2. ~/.arc/config.json (for non-sensitive values; legacy secrets as fallback)
      3. Environment variables (always win — useful for CI and quick overrides)
    """
    cfg = ArcConfig()

    # --- Pull secrets from keychain first ---
    cfg.scm.bearer_token  = _keychain_get(_KEY_SCM_BEARER)
    cfg.scm.client_secret = _keychain_get(_KEY_SCM_SECRET)
    cfg.ssh.password      = _keychain_get(_KEY_SSH_PASSWORD)

    # --- Overlay with config file (non-sensitive fields; legacy secret fallback) ---
    if CONFIG_FILE.exists():
        try:
            raw = json.loads(CONFIG_FILE.read_text())

            scm = raw.get("scm", {})
            cfg.scm.client_id   = scm.get("client_id", "")
            cfg.scm.tsg_id      = scm.get("tsg_id", "")
            # Legacy plaintext secrets: migrate to keychain on next save.
            # Only used if the keychain returned nothing.
            if not cfg.scm.bearer_token:
                cfg.scm.bearer_token  = scm.get("bearer_token", "")
            if not cfg.scm.client_secret:
                cfg.scm.client_secret = scm.get("client_secret", "")

            ssh = raw.get("ssh", {})
            cfg.ssh.user      = ssh.get("user", "admin")
            cfg.ssh.key_path  = ssh.get("key_path", "")
            cfg.ssh.port      = int(ssh.get("port", 22))
            if not cfg.ssh.password:
                cfg.ssh.password = ssh.get("password", "")

            cfg.default_folder = raw.get("default_folder", "Shared")

        except (OSError, json.JSONDecodeError, TypeError, ValueError) as exc:
            # Invalid config must not block startup.  Commands requiring
            # credentials will fail closed with a clear error.
            logger.debug("Could not parse config file: %s", exc)

    # --- Environment variables always win ---
    cfg.scm.bearer_token  = os.environ.get("SCM_BEARER_TOKEN", cfg.scm.bearer_token)
    cfg.scm.client_id     = os.environ.get("SCM_CLIENT_ID",    cfg.scm.client_id)
    cfg.scm.client_secret = os.environ.get("SCM_CLIENT_SECRET", cfg.scm.client_secret)
    cfg.scm.tsg_id        = os.environ.get("SCM_TSG_ID",        cfg.scm.tsg_id)

    cfg.ssh.user          = os.environ.get("ARC_SSH_USER", cfg.ssh.user)
    cfg.ssh.key_path      = os.environ.get("ARC_SSH_KEY",  cfg.ssh.key_path)
    cfg.ssh.password      = os.environ.get("ARC_SSH_PASS", cfg.ssh.password)

    cfg.debug = os.environ.get("ARC_DEBUG", "0") == "1"

    return cfg


def save_config(cfg: ArcConfig) -> None:
    """Persist config: secrets to OS keychain, non-sensitive values to config.json.

    The config file is always written with mode 0600 (owner read/write only).
    Secrets are never written to disk.  If the OS keychain cannot store a
    non-empty secret, non-sensitive config is still saved and ConfigSecurityError
    is raised so callers can tell the user to use keychain or env vars.
    """
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    CONFIG_DIR.chmod(stat.S_IRWXU)

    # Store secrets in the keychain.  Empty values delete existing entries.
    failed_secret_keys: list[str] = []
    for key, value in (
        (_KEY_SCM_BEARER, cfg.scm.bearer_token),
        (_KEY_SCM_SECRET, cfg.scm.client_secret),
        (_KEY_SSH_PASSWORD, cfg.ssh.password),
    ):
        saved = _keychain_set(key, value)
        if value and not saved:
            failed_secret_keys.append(key)

    # Build the on-disk payload.  Secrets are deliberately omitted even when
    # keychain storage fails.  This also strips legacy plaintext secrets from
    # config.json the next time save_config() runs.
    scm_block: dict = {
        "client_id": cfg.scm.client_id,
        "tsg_id":    cfg.scm.tsg_id,
    }

    ssh_block: dict = {
        "user":     cfg.ssh.user,
        "key_path": cfg.ssh.key_path,
        "port":     cfg.ssh.port,
    }

    data = {
        "scm":            scm_block,
        "ssh":            ssh_block,
        "default_folder": cfg.default_folder,
    }

    flags = os.O_WRONLY | os.O_CREAT | os.O_TRUNC
    fd = os.open(CONFIG_FILE, flags, 0o600)
    with os.fdopen(fd, "w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2)
        handle.write("\n")
    CONFIG_FILE.chmod(stat.S_IRUSR | stat.S_IWUSR)

    if failed_secret_keys:
        failed = ", ".join(failed_secret_keys)
        raise ConfigSecurityError(
            "OS keychain could not store ARC secret(s): "
            f"{failed}. Secrets were not written to config.json. "
            "Use `arc auth login` on a machine with keychain access, or provide "
            "secrets through environment variables for this session."
        )


def clear_keychain() -> None:
    """Remove all ARC secrets from the OS keychain.

    Called by ``arc auth clear``.  Does not touch the config file.
    """
    for key in (_KEY_SCM_BEARER, _KEY_SCM_SECRET, _KEY_SSH_PASSWORD):
        _keychain_delete(key)

