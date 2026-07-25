"""Validate a staged write's request body against the endpoint's OpenAPI schema.

Route-keyed (method + gateway base_url + path template) so it covers EVERY write —
generated commands, hand-written commands, and future features — with no
per-command code.  The schema comes from ``app/settings/request_schemas.py``
(AUTO-GENERATED from the specs by ``generate_request_schemas.py``, refreshed on
docsupdate / catalog rebuild).

Used by ``set`` staging (soft warning), ``commit check`` (report), and the
``commit`` pre-flight (prompt).  Never raises and never touches the network:
returns a list of human-readable problems ([] = valid, unknown route, or a body
we can't check).
"""
from __future__ import annotations

import re

try:
    from app.settings.request_schemas import REQUEST_SCHEMAS
except Exception:  # pragma: no cover - artifact missing/malformed
    REQUEST_SCHEMAS = []

_INDEX: "dict | None" = None


def _index() -> dict:
    """Lazily build ``(method, base_url) -> [(template_segments, record)]``."""
    global _INDEX
    if _INDEX is None:
        idx: dict = {}
        for rec in REQUEST_SCHEMAS:
            idx.setdefault((rec["method"], rec["base_url"]), []).append(
                (rec["path"].split("/"), rec)
            )
        _INDEX = idx
    return _INDEX


def _match(method: str, base_url: str, path: str) -> "dict | None":
    """Match a CONCRETE path to a path-template route (id segments are wildcards)."""
    if not path:
        return None
    path = path.split(":", 1)[0]  # strip an action suffix like /rules/{id}:move
    segs = path.split("/")
    for tmpl_segs, rec in _index().get((method, base_url), []):
        if len(tmpl_segs) != len(segs):
            continue
        if all(
            t == s or (t.startswith("{") and t.endswith("}"))
            for t, s in zip(tmpl_segs, segs)
        ):
            return rec
    return None


def _present(container: object, key: str) -> bool:
    if not isinstance(container, dict) or key not in container:
        return False
    val = container[key]
    return not (
        val is None
        or (isinstance(val, str) and not val.strip())
        or (isinstance(val, (list, dict)) and not val)
    )


def validate_request_body_by_route(
    method: str, base_url: str, path: str, body: object, params: object = None
) -> list[str]:
    """Return schema problems for one write op ([] = valid / not checkable)."""
    method = (method or "").upper()
    if method not in ("POST", "PUT", "PATCH") or not isinstance(body, dict):
        return []
    rec = _match(method, base_url or "", path or "")
    if rec is None:
        return []  # unknown / not-yet-regenerated route — never a false alarm
    params = params if isinstance(params, dict) else {}
    problems: list[str] = []

    # Required — satisfied by the body OR a query param (ARC sends folder/position
    # as ?query=, not in the body).
    for field in rec.get("required", []):
        if not (_present(body, field) or _present(params, field)):
            problems.append(f"missing required field <{field}>")

    for field, cons in (rec.get("props") or {}).items():
        if field not in body:
            continue
        val = body[field]
        if isinstance(val, str):
            enum = cons.get("enum")
            if enum and val not in enum and not any(c.lower() == val.lower() for c in enum):
                shown = ", ".join(enum[:8]) + (", …" if len(enum) > 8 else "")
                problems.append(f"{field} must be one of: {shown}")
            ml = cons.get("maxLength")
            if isinstance(ml, int) and len(val) > ml:
                problems.append(f"{field} is too long ({len(val)} > {ml})")
            mn = cons.get("minLength")
            if isinstance(mn, int) and len(val) < mn:
                problems.append(f"{field} is too short ({len(val)} < {mn})")
            pat = cons.get("pattern")
            if isinstance(pat, str) and pat:
                try:
                    ok = re.search(pat, val) is not None
                except re.error:
                    ok = True  # malformed spec regex — don't block
                if not ok:
                    problems.append(f"{field} does not match the required format")
        elif isinstance(val, (int, float)) and not isinstance(val, bool):
            lo, hi = cons.get("minimum"), cons.get("maximum")
            if isinstance(lo, (int, float)) and val < lo:
                problems.append(f"{field} must be >= {lo}")
            if isinstance(hi, (int, float)) and val > hi:
                problems.append(f"{field} must be <= {hi}")
        elif isinstance(val, list):
            mi = cons.get("maxItems")
            if isinstance(mi, int) and len(val) > mi:
                problems.append(f"{field} has too many items ({len(val)} > {mi})")
            items_enum = cons.get("items_enum")
            if items_enum:
                for item in val:
                    if isinstance(item, str) and item not in items_enum \
                            and not any(c.lower() == item.lower() for c in items_enum):
                        problems.append(f"{field}: '{item}' is not an allowed value")

    # Variant groups (oneOf/anyOf): at least one member must be supplied.
    for group in rec.get("variants", []):
        if group and not any(_present(body, m) or _present(params, m) for m in group):
            problems.append("needs one of: " + ", ".join(group))

    return problems
