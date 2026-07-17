"""SSH connection manager using paramiko.

Authentication order per connection attempt:
  1. SSH agent keys (if agent is running)
  2. Configured key file  (`ARC_SSH_KEY` / `arc auth login --ssh-key`)
  3. Default key files    (~/.ssh/id_ed25519, id_rsa, id_ecdsa, id_dsa)
  4. Keyboard-interactive — auto-fills stored password for "Password:" prompts,
     then passes any remaining challenges (OTP, Duo push, etc.) to the terminal
  5. Plain password auth  (fallback for servers that don't support kb-interactive)

This order means password + 2FA flows work out of the box: the kb-interactive
handler answers the password prompt silently from stored credentials, then the
2FA challenge is printed and the user can approve the push or type a code.
"""

from __future__ import annotations

import getpass
import os
import socket

import paramiko


class SSHError(Exception):
    pass


# ---------------------------------------------------------------------------
# Keyboard-interactive handler
# ---------------------------------------------------------------------------

def _make_interactive_handler(password: str):
    """Return a paramiko keyboard-interactive auth handler.

    Behaviour:
    - First prompt whose text looks like "Password" / "passwd" is auto-filled
      from *password* (if provided) — the user never sees it.
    - A prompt with empty text signals that the server sent an out-of-band push
      (e.g. Duo) and is waiting; we respond with an empty string automatically.
    - All other prompts (OTP, verification code, choice list) are shown in the
      terminal so the user can type their response.

    The ``echo`` flag from the server controls whether input is shown: echo=False
    uses getpass so the response is not echoed.
    """
    password_consumed = [False]

    def handler(title: str, instructions: str, prompt_list: list) -> list:
        if title:
            print(f"\n{title}")
        if instructions:
            print(instructions)

        responses = []
        for prompt_text, echo in prompt_list:
            cleaned = prompt_text.strip().lower().rstrip(":").rstrip()

            # Auto-fill the first password-style prompt from stored credentials.
            if password and not password_consumed[0] and cleaned in (
                "password", "passwd", "secret", "pass",
            ):
                responses.append(password)
                password_consumed[0] = True

            # Empty prompt = server is waiting for out-of-band push (Duo, etc.)
            # Respond with empty string; the server will unblock when approved.
            elif not prompt_text.strip():
                print("[Waiting for 2FA push approval…]")
                responses.append("")

            # All other challenges go to the terminal.
            elif echo:
                responses.append(input(prompt_text))
            else:
                responses.append(getpass.getpass(prompt_text))

        return responses

    return handler


# Default key locations tried when no explicit key is configured —
# mirrors paramiko's look_for_keys=True behaviour.
_DEFAULT_KEY_FILES: list[tuple[str, type]] = [
    ("~/.ssh/id_ed25519", paramiko.Ed25519Key),
    ("~/.ssh/id_rsa",     paramiko.RSAKey),
    ("~/.ssh/id_ecdsa",   paramiko.ECDSAKey),
]

# Key classes tried when loading a user-specified key file.
_ALL_KEY_CLASSES = (
    paramiko.Ed25519Key,
    paramiko.RSAKey,
    paramiko.ECDSAKey,
)


def _try_pubkey(transport: paramiko.Transport, user: str, key) -> bool:
    """Attempt public-key auth with *key*.  Returns True on success."""
    try:
        transport.auth_publickey(user, key)
        return transport.is_authenticated()
    except (paramiko.AuthenticationException, paramiko.SSHException):
        return False


class SSHManager:
    """Manages a pool of SSH connections to PAN-OS devices.

    Each call to ``verify_connection`` or ``execute`` that requires a new
    connection works through the authentication sequence described at the top
    of this module.  Established connections are pooled by host and reused
    until they go stale.
    """

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
        to validate SSH access before opening an interactive shell.
        """
        self._get_or_connect(host, user, key_path, password, port)

    def open_shell(
        self,
        host: str,
        user: str = "admin",
        key_path: str = "",
        password: str = "",
        port: int = 22,
    ) -> "paramiko.Channel":
        """Authenticate and open an interactive PTY shell channel on *host*.

        The returned channel is ready for raw I/O.  The caller owns the I/O
        loop and must close the channel when done.

        Raises SSHError if connection or authentication fails.
        """
        client = self._get_or_connect(host, user, key_path, password, port)
        channel = client.invoke_shell(term="xterm-256color")
        return channel

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
            _, stdout, stderr = client.exec_command(command, timeout=30)
            out = stdout.read().decode(errors="replace")
            err = stderr.read().decode(errors="replace")
            return (out + err).strip()
        except Exception as exc:
            # Connection may have dropped — evict and re-raise
            self._pool.pop(host, None)
            raise SSHError(f"SSH command failed on {host}: {exc}") from exc

    def run_config_commands(
        self,
        host: str,
        commands: list[str],
        user: str = "admin",
        key_path: str = "",
        password: str = "",
        port: int = 22,
        timeout_s: int = 60,
    ) -> str:
        """Run PAN-OS *config-mode* commands via a scripted interactive shell.

        PAN-OS `set`/`delete` config commands only work inside `configure`,
        which `exec_command` cannot enter — so this scripts an interactive
        channel: wait for prompt → `configure` → each command → `exit`.
        The operator commits separately (`commit --remote`); nothing here
        auto-commits. Returns the combined captured output.
        """
        import time as _time

        client = self._get_or_connect(host, user, key_path, password, port)
        try:
            channel = client.invoke_shell(term="dumb", width=200)
            channel.settimeout(timeout_s)

            def _read_until_prompt(deadline: float) -> str:
                chunks: list[str] = []
                while _time.monotonic() < deadline:
                    if channel.recv_ready():
                        chunks.append(channel.recv(65536).decode(errors="replace"))
                        # PAN-OS prompts end in '>' (op) or '#' (configure) as
                        # the LAST line — checking only that line avoids false
                        # triggers on banner text containing those characters.
                        text = "".join(chunks).rstrip()
                        last_line = text.splitlines()[-1].strip() if text else ""
                        if last_line.endswith((">", "#")):
                            return "".join(chunks)
                    else:
                        _time.sleep(0.1)
                # Deadline expired without seeing a prompt — raise so the caller
                # knows output is incomplete rather than silently returning partial data.
                partial = "".join(chunks)
                last = partial.splitlines()[-1].strip() if partial.strip() else "(no output)"
                raise SSHError(
                    f"Timed out waiting for device prompt on {host} "
                    f"(last line: {last!r}). "
                    f"Increase timeout_s (current: {timeout_s}s) or check device health."
                )
                return "".join(chunks)  # unreachable; satisfies type checker

            deadline = _time.monotonic() + timeout_s
            _read_until_prompt(deadline)                      # banner + first prompt
            channel.send("set cli pager off\n")
            _read_until_prompt(deadline)
            channel.send("configure\n")
            _read_until_prompt(deadline)
            output: list[str] = []
            for command in commands:
                channel.send(command + "\n")
                output.append(_read_until_prompt(deadline))
            channel.send("exit\n")
            _read_until_prompt(deadline)
            channel.close()
            return "".join(output).strip()
        except Exception as exc:
            self._pool.pop(host, None)
            raise SSHError(f"SSH config session failed on {host}: {exc}") from exc

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
        """Return a live SSH client for *host*, connecting if needed."""
        # Return pooled connection if still alive.
        if host in self._pool:
            transport = self._pool[host].get_transport()
            if transport and transport.is_active():
                return self._pool[host]
            self._pool.pop(host)

        # --- Phase 1: TCP + SSH handshake ---
        try:
            sock = socket.create_connection((host, port), timeout=15)
        except OSError as exc:
            raise SSHError(f"Cannot reach {host}:{port}: {exc}") from exc

        # Host keys are intentionally not verified: ARC targets firewalls whose
        # keys rotate on redeploy, and operators connect by inventory hostname.
        transport = paramiko.Transport(sock)
        try:
            transport.start_client(timeout=15)
        except paramiko.SSHException as exc:
            transport.close()
            raise SSHError(f"SSH handshake failed with {host}:{port}: {exc}") from exc

        # --- Phase 2: Authentication ---
        authenticated = self._authenticate(transport, host, user, key_path, password, port)

        if not authenticated:
            transport.close()
            _no_creds_hint = (
                f"Authentication failed for {user}@{host}:{port}.\n"
                "  • Run `arc auth configure` to store SSH credentials.\n"
                "  • See `arc setup osx` / `arc setup win` / `arc setup linux` for platform steps."
            )
            raise SSHError(_no_creds_hint)

        # Keepalives stretch the pooled session between commands so the
        # operator 2FAs once per device per sitting, not per command.
        transport.set_keepalive(30)

        # Wrap the authenticated transport in an SSHClient so exec_command works.
        client = paramiko.SSHClient()
        client._transport = transport  # noqa: SLF001 — intentional private access
        self._pool[host] = client
        return client

    def _authenticate(
        self,
        transport: paramiko.Transport,
        host: str,
        user: str,
        key_path: str,
        password: str,
        port: int,
    ) -> bool:
        """Work through the auth method sequence.  Returns True if authenticated."""

        # 1. SSH agent keys.
        try:
            agent = paramiko.Agent()
            for agent_key in agent.get_keys():
                if _try_pubkey(transport, user, agent_key):
                    return True
        except Exception:
            pass  # no agent running — not an error

        # 2. Configured key file.
        if key_path:
            expanded = os.path.expanduser(key_path)
            for key_class in _ALL_KEY_CLASSES:
                try:
                    key = key_class.from_private_key_file(expanded)
                    if _try_pubkey(transport, user, key):
                        return True
                except (paramiko.SSHException, IOError, OSError):
                    continue

        # 3. Default key files (~/.ssh/id_*).
        if not key_path:
            for default_path, key_class in _DEFAULT_KEY_FILES:
                expanded = os.path.expanduser(default_path)
                if not os.path.exists(expanded):
                    continue
                try:
                    key = key_class.from_private_key_file(expanded)
                    if _try_pubkey(transport, user, key):
                        return True
                except (paramiko.SSHException, IOError, OSError):
                    continue

        # 4. Keyboard-interactive — handles password + 2FA chains (Duo, TOTP, etc.)
        #    The handler auto-fills password prompts and surfaces 2FA challenges.
        handler = _make_interactive_handler(password)
        try:
            transport.auth_interactive(user, handler)
            if transport.is_authenticated():
                return True
        except paramiko.AuthenticationException:
            pass

        # 5. Plain password auth — fallback for servers that don't support
        #    keyboard-interactive (rare, but some older devices).
        if password:
            try:
                transport.auth_password(user, password)
                if transport.is_authenticated():
                    return True
            except paramiko.AuthenticationException:
                pass

        return False
