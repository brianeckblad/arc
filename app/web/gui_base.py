"""Shared foundation for ARC's local browser GUIs.

Both the feature editor (``feature gui-configure``) and the ARC settings console
(``arc gui-configure``) are tiny, on-demand, loopback-only HTTP servers with the
same lifecycle: bind 127.0.0.1:<port>, open the browser to a cache-busted URL,
block until the page signals close (``POST /api/close``) or Ctrl-C, then shut
down.  This module factors that machinery into ``BaseGuiServer`` so each GUI only
implements its own routes (``route_get`` / ``route_post``) and HTML.

Static assets shared by both pages live in ``app/web/assets/`` and are served at
``/assets/<name>``.
"""
from __future__ import annotations

import json
import logging
import threading
import time
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)

ASSETS_DIR = Path(__file__).with_name("assets")

# Max POST body accepted by any console endpoint.  The GUIs only ever send small
# JSON payloads (settings/theme/source edits); this caps a runaway/abusive body.
_MAX_BODY_BYTES = 2 * 1024 * 1024  # 2 MB

# Heartbeat: the page pings ``/api/ping`` on a short interval.  If no ping (or
# explicit close) arrives within this window, the watchdog assumes the tab was
# closed / the browser crashed / the machine slept and shuts the server down so
# the blocked CLI is released.  Must exceed background-tab timer throttling
# (~60s in modern browsers) so a merely-backgrounded tab is NOT reaped.
_HEARTBEAT_TIMEOUT = 90.0  # seconds without a ping before we give up
_WATCHDOG_INTERVAL = 5.0   # how often the watchdog checks

_CONTENT_TYPES = {
    ".css": "text/css; charset=utf-8",
    ".js": "application/javascript; charset=utf-8",
    ".html": "text/html; charset=utf-8",
    ".json": "application/json",
    ".svg": "image/svg+xml",
    ".png": "image/png",
    ".ico": "image/x-icon",
}


class QuietThreadingHTTPServer(ThreadingHTTPServer):
    """ThreadingHTTPServer that ignores client-disconnect errors.

    Browsers routinely cancel in-flight requests (fast navigation, refresh,
    duplicate fetches); the resulting BrokenPipe/ConnectionReset is harmless but
    the default handler prints a full traceback to stderr, spamming the shell.
    """

    daemon_threads = True

    def handle_error(self, request, client_address):  # noqa: D102
        import sys
        exc = sys.exc_info()[1]
        if isinstance(exc, (BrokenPipeError, ConnectionResetError, ConnectionError)):
            return  # client went away — nothing to report
        super().handle_error(request, client_address)


class BaseGuiServer:
    """A blocking, on-demand, loopback HTTP server for one ARC browser GUI.

    Subclasses set :attr:`HTML_FILE` and :attr:`LABEL`, and implement
    :meth:`route_get` / :meth:`route_post`.  Everything else — binding, the
    request handler, ``/`` (HTML), ``/assets/*``, ``POST /api/close``, JSON
    encoding, disconnect tolerance, browser launch, and the block-until-closed
    lifecycle — is handled here.
    """

    #: Path to the page's HTML file (set by subclass).
    HTML_FILE: Path = Path(__file__).with_name("missing.html")
    #: Human label used in status strings ("Feature editor", "ARC settings…").
    LABEL: str = "ARC GUI"

    def __init__(self, shell, port: int, host: str = "127.0.0.1") -> None:
        self._shell = shell
        self._port = port
        self._host = host
        self._lock = threading.Lock()
        self._closed = threading.Event()
        self._last_ping = time.monotonic()
        self._httpd: ThreadingHTTPServer | None = None
        self._html = self._load_html()

    # -- overridable routing ----------------------------------------------

    def route_get(self, path: str, qs: dict) -> Optional[dict]:
        """Return a JSON-serialisable dict for a GET data route, or None for 404.

        ``path`` excludes the query string; ``qs`` is ``parse_qs`` output.
        The base class already handles ``/``, ``/index.html`` and ``/assets/*``.
        """
        return None

    def route_post(self, path: str, data: dict) -> Optional[dict]:
        """Handle a POST mutation and return a result dict, or None for 404.

        The base class already handles ``/api/close``.  The returned dict is
        merged into ``{"ok": True, ...}``.  Raise ``ValueError`` for a 400 or
        ``RuntimeError`` for a 500 with a clean message.
        """
        return None

    # -- helpers -----------------------------------------------------------

    def _load_html(self) -> bytes:
        try:
            return self.HTML_FILE.read_bytes()
        except OSError as exc:  # pragma: no cover - packaging safety net
            logger.error("%s HTML missing: %s", self.LABEL, exc)
            return (
                b"<!doctype html><meta charset=utf-8>"
                b"<h1>" + self.HTML_FILE.name.encode() + b" not found</h1>"
            )

    @staticmethod
    def _asset(name: str) -> Optional[tuple[bytes, str]]:
        """Return (bytes, content-type) for a shared asset, or None if missing."""
        # Guard against path traversal: strip to a bare filename AND restrict to
        # a safe charset, then confirm the resolved path stays inside ASSETS_DIR.
        import re as _re

        safe = Path(name).name
        if not _re.fullmatch(r"[A-Za-z0-9._-]+", safe):
            return None
        target = (ASSETS_DIR / safe).resolve()
        if not (target.is_file() and target.is_relative_to(ASSETS_DIR.resolve())):
            return None
        ctype = _CONTENT_TYPES.get(target.suffix, "application/octet-stream")
        try:
            return target.read_bytes(), ctype
        except OSError:  # pragma: no cover
            return None

    @property
    def url(self) -> str:
        return f"http://{self._host}:{self._port}/"

    # -- lifecycle ---------------------------------------------------------

    def serve(self) -> str:
        """Start the server, open the browser, and BLOCK until the page closes.

        Returns a short status string for the caller to print.  On a bind
        failure (port already in use) returns immediately without blocking so
        the shell stays responsive.
        """
        server = self  # captured by the handler

        class _Handler(BaseHTTPRequestHandler):
            def log_message(self, *_args) -> None:  # noqa: N802
                pass

            def _send(self, code: int, body: bytes, ctype: str) -> None:
                try:
                    self.send_response(code)
                    self.send_header("Content-Type", ctype)
                    self.send_header("Content-Length", str(len(body)))
                    self.send_header("Cache-Control", "no-store")
                    self.end_headers()
                    self.wfile.write(body)
                except (BrokenPipeError, ConnectionResetError, ConnectionError):
                    pass

            def _send_json(self, obj: dict, code: int = 200) -> None:
                self._send(code, json.dumps(obj).encode("utf-8"), "application/json")

            def _host_ok(self) -> bool:
                """Reject requests whose Host header isn't our loopback address.

                Defends against DNS-rebinding: a malicious web page can't drive
                a browser to POST to these local settings/secret endpoints under
                an attacker-controlled hostname, because the Host header won't
                match 127.0.0.1/localhost:<port>.
                """
                host = (self.headers.get("Host") or "").strip().lower()
                allowed = {
                    f"127.0.0.1:{server._port}",
                    f"localhost:{server._port}",
                    f"[::1]:{server._port}",
                }
                return host in allowed

            def do_GET(self) -> None:  # noqa: N802
                from urllib.parse import parse_qs, urlparse

                if not self._host_ok():
                    self._send(403, b"forbidden", "text/plain")
                    return
                parsed = urlparse(self.path)
                path = parsed.path
                qs = parse_qs(parsed.query)
                if path in ("/", "/index.html"):
                    self._send(200, server._html, "text/html; charset=utf-8")
                    return
                if path.startswith("/assets/"):
                    asset = server._asset(path[len("/assets/"):])
                    if asset is None:
                        self._send(404, b"not found", "text/plain")
                    else:
                        self._send(200, asset[0], asset[1])
                    return
                try:
                    result = server.route_get(path, qs)
                except Exception as exc:  # pragma: no cover
                    self._send_json({"error": str(exc)}, 500)
                    return
                if result is None:
                    self._send(404, b"not found", "text/plain")
                else:
                    self._send_json(result)

            def do_POST(self) -> None:  # noqa: N802
                if not self._host_ok():
                    self._send(403, b"forbidden", "text/plain")
                    return
                path = self.path.split("?", 1)[0]
                if path == "/api/close":
                    self._send_json({"ok": True, "closing": True})
                    server._closed.set()
                    return
                if path == "/api/ping":
                    # Liveness heartbeat from the open tab; refreshes the
                    # watchdog deadline.  Body (if any) is ignored.
                    server._last_ping = time.monotonic()
                    self._send_json({"ok": True})
                    return
                try:
                    length = int(self.headers.get("Content-Length", 0))
                    if length > _MAX_BODY_BYTES:
                        self._send_json({"error": "request too large"}, 413)
                        return
                    raw = self.rfile.read(length) if length else b"{}"
                    data = json.loads(raw or b"{}")
                except Exception as exc:
                    self._send_json({"error": f"bad request: {exc}"}, 400)
                    return
                try:
                    result = server.route_post(path, data)
                except ValueError as exc:
                    self._send_json({"error": str(exc)}, 400)
                    return
                except RuntimeError as exc:
                    self._send_json({"error": str(exc)}, 500)
                    return
                except Exception as exc:  # pragma: no cover
                    self._send_json({"error": str(exc)}, 500)
                    return
                if result is None:
                    self._send(404, b"not found", "text/plain")
                else:
                    self._send_json({"ok": True, **result})

        try:
            self._httpd = QuietThreadingHTTPServer((self._host, self._port), _Handler)
        except OSError as exc:
            return (
                f"[error] Could not start {self.LABEL} on "
                f"{self._host}:{self._port} — {exc}. "
                f"Is another editor already running, or the port in use?"
            )

        thread = threading.Thread(target=self._httpd.serve_forever, daemon=True)
        thread.start()

        # Watchdog: releases the blocked CLI if the tab is closed (or the browser
        # crashes / the box sleeps) WITHOUT a Save & Exit.  The page pings
        # ``/api/ping`` regularly; if the gap exceeds _HEARTBEAT_TIMEOUT we close.
        # A short grace period after launch tolerates a slow first page load.
        self._last_ping = time.monotonic()
        watchdog = threading.Thread(target=self._watchdog, daemon=True)
        watchdog.start()

        # Cache-bust the URL per launch so the browser opens a FRESH page (and
        # re-fetches saved prefs/theme) instead of re-focusing a stale tab.
        import time as _time
        url = f"http://{self._host}:{self._port}/?v={int(_time.time())}"
        try:
            webbrowser.open(url)
        except Exception:  # pragma: no cover - headless safety net
            pass

        try:
            self._closed.wait()
        except KeyboardInterrupt:
            pass
        finally:
            self.stop()
        return f"{self.LABEL} closed — {url}"

    def _watchdog(self) -> None:
        """Close the server if the page stops sending heartbeats.

        Runs until :attr:`_closed` is set (normal Save & Exit / Ctrl-C) or the
        last ping is older than :data:`_HEARTBEAT_TIMEOUT`, at which point we
        assume the tab was closed and release the blocked CLI.
        """
        while not self._closed.wait(_WATCHDOG_INTERVAL):
            if time.monotonic() - self._last_ping > _HEARTBEAT_TIMEOUT:
                logger.debug("%s: heartbeat timeout — closing", self.LABEL)
                self._closed.set()
                return

    def stop(self) -> None:
        if self._httpd is not None:
            try:
                self._httpd.shutdown()
                self._httpd.server_close()
            except Exception:  # pragma: no cover
                pass
            self._httpd = None
        self._closed.set()
