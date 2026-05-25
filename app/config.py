"""Config loader — reads from environment variables and ~/.arc/config.json."""

from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from pathlib import Path

import platformdirs

CONFIG_DIR = Path(platformdirs.user_config_dir("arc"))
CONFIG_FILE = CONFIG_DIR / "config.json"


@dataclass
class SCMConfig:
    """SCM API configuration.

    ARC supports either a pre-issued bearer token or OAuth client credentials.
    A bearer token takes precedence when both are present.
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


def load_config() -> ArcConfig:
    """Load config from file then overlay with environment variables."""
    cfg = ArcConfig()

    if CONFIG_FILE.exists():
        try:
            raw = json.loads(CONFIG_FILE.read_text())
            scm = raw.get("scm", {})
            cfg.scm = SCMConfig(
                bearer_token=scm.get("bearer_token", ""),
                client_id=scm.get("client_id", ""),
                client_secret=scm.get("client_secret", ""),
                tsg_id=scm.get("tsg_id", ""),
            )
            ssh = raw.get("ssh", {})
            cfg.ssh = SSHConfig(
                user=ssh.get("user", "admin"),
                key_path=ssh.get("key_path", ""),
                password=ssh.get("password", ""),
                port=int(ssh.get("port", 22)),
            )
            cfg.default_folder = raw.get("default_folder", "Shared")
        except (OSError, json.JSONDecodeError, TypeError, ValueError):
            # Invalid local config should not prevent shell startup. Commands that
            # require credentials will fail closed with a clear configuration error.
            pass

    cfg.scm.bearer_token = os.environ.get("SCM_BEARER_TOKEN", cfg.scm.bearer_token)
    cfg.scm.client_id = os.environ.get("SCM_CLIENT_ID", cfg.scm.client_id)
    cfg.scm.client_secret = os.environ.get("SCM_CLIENT_SECRET", cfg.scm.client_secret)
    cfg.scm.tsg_id = os.environ.get("SCM_TSG_ID", cfg.scm.tsg_id)

    cfg.ssh.user = os.environ.get("ARC_SSH_USER", cfg.ssh.user)
    cfg.ssh.key_path = os.environ.get("ARC_SSH_KEY", cfg.ssh.key_path)
    cfg.ssh.password = os.environ.get("ARC_SSH_PASS", cfg.ssh.password)

    cfg.debug = os.environ.get("ARC_DEBUG", "0") == "1"

    return cfg


def save_config(cfg: ArcConfig) -> None:
    """Persist config to ~/.arc/config.json."""
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    data = {
        "scm": {
            "bearer_token": cfg.scm.bearer_token,
            "client_id": cfg.scm.client_id,
            "client_secret": cfg.scm.client_secret,
            "tsg_id": cfg.scm.tsg_id,
        },
        "ssh": {
            "user": cfg.ssh.user,
            "key_path": cfg.ssh.key_path,
            "password": cfg.ssh.password,
            "port": cfg.ssh.port,
        },
        "default_folder": cfg.default_folder,
    }
    CONFIG_FILE.write_text(json.dumps(data, indent=2))
