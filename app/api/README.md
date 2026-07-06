# `app/api/` — API Clients (SCM + SLS)

SCM is ARC's only management-API integration; SLS (Strata Logging Service) is
the fleet log store. Both authenticate with the same TSG-scoped OAuth
client-credentials flow (`auth.apps.paloaltonetworks.com`).

## What lives here

| File | One line |
|---|---|
| `client.py` | `SCMClient`: one `_request()` core + thin per-domain wrappers (`get_addresses`, `ops_job_start/_status`, config-versions, …) over the SCM gateways |
| `sls.py` | SLS/CDL Query Service v2 client — SQL query jobs over `firewall.traffic` / `.threat` / `.system`, powering `show log …` |

## How the pieces relate

`client.py` maps each SCM domain to its gateway
(`api.strata.paloaltonetworks.com/config/<domain>/v1`; IAM + tenancy at
`api.sase.paloaltonetworks.com`) — the base URLs must match
`docs/scm-api/MANIFEST.md`. A 401 mid-session re-authenticates once inside
`_request` (client-credentials only). `sls.py` uses the regional base
`api.<region>.cdl.paloaltonetworks.com` (`ARC_SLS_REGION`, default `us`;
optional `ARC_SLS_TENANT_ID`): create job → poll → page results. The service
account needs a Logging Service role — a config-only SCM role gets 403 here.

## How to change things here

- **Never guess an endpoint.** Look it up in `app/scripts/API_INDEX.md` (one line per
  endpoint) or the mirrored spec `docs/scm-api/specs/<category>.md`.
- New client method: a one-line wrapper calling `self._request(...)` — then
  reference it from a `CommandDef` via `show_handler('get_x')` or a named
  handler. Validate: full `python app/scripts/smoke_test.py`.
- After `python app/scripts/docsupdate.py`: read `docs/scm-api/CHANGES.md`; fix any
  removed/renamed endpoints here and in the affected commands.
- SLS changes: run the offline unit tests — `python app/scripts/test_sls.py`
  (fake transport; exercises job lifecycle, SQL builder, error translation).

## Do not

- Never swallow errors into `[]` or bare `except Exception` — raise
  (`httpx.HTTPStatusError` etc.); `_execute_api` turns them into operator
  messages.
- Never log or print unmasked secrets — use `_mask()`.
- Do not add non-SCM management integrations — SCM is intentionally the only
  one (SSH covers the rest).
- Do not hard-code gateway URLs that disagree with `docs/scm-api/MANIFEST.md`.
