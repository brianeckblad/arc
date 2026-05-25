"""SSH connection manager using paramiko."""

from __future__ import annotations

import os

import paramiko


class SSHError(Exception):
    pass


class SSHManager:
    """Manages a pool of SSH connections to PAN-OS devices."""

    def __init__(self) -> None:
        self._pool: dict[str, paramiko.SSHClient] = {}

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def verify_connection(
        self,
        host: str,
        user: str = "admin",
        key_path: str = "",
        password: str = "",
        port: int = 22,
    ) -> None:
        """Establish (or reuse) an SSH connection without running a command.

        Raises SSHError if the connection cannot be made.  Used by 'connect'
        to validate SSH access before entering passthrough mode.
        """
        self._get_or_connect(host, user, key_path, password, port)

    def execute(
        self,
        host: str,
        command: str,
        user: str = "admin",
        key_path: str = "",
        password: str = "",
        port: int = 22,
    ) -> str:
        """Run *command* on *host* via SSH and return combined stdout/stderr."""
        client = self._get_or_connect(host, user, key_path, password, port)
        try:
            stdin, stdout, stderr = client.exec_command(command, timeout=30)
            out = stdout.read().decode(errors="replace")
            err = stderr.read().decode(errors="replace")
            return (out + err).strip()
        except Exception as exc:
            # Connection may have dropped — evict and re-raise
            self._pool.pop(host, None)
            raise SSHError(f"SSH command failed on {host}: {exc}") from exc

    def close(self, host: str) -> None:
        client = self._pool.pop(host, None)
        if client:
            client.close()

    def close_all(self) -> None:
        for client in self._pool.values():
            try:
                client.close()
            except Exception:
                pass
        self._pool.clear()

    # ------------------------------------------------------------------
    # Internal
    # ------------------------------------------------------------------

    def _get_or_connect(
        self,
        host: str,
        user: str,
        key_path: str,
        password: str,
        port: int,
    ) -> paramiko.SSHClient:
        if host in self._pool:
            # Test if still alive
            transport = self._pool[host].get_transport()
            if transport and transport.is_active():
                return self._pool[host]
            # Stale — reconnect
            self._pool.pop(host)

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        connect_kwargs: dict = {
            "hostname": host,
            "username": user,
            "port": port,
            "timeout": 15,
            "allow_agent": True,
            "look_for_keys": True,
        }
        if key_path:
            expanded = os.path.expanduser(key_path)
            connect_kwargs["key_filename"] = expanded
        elif password:
            connect_kwargs["password"] = password

        try:
            client.connect(**connect_kwargs)
        except Exception as exc:
            raise SSHError(f"Cannot connect to {host}:{port} as {user}: {exc}") from exc

        self._pool[host] = client
        return client

