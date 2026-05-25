# Configuration

ARC reads configuration from `~/.arc/config.json` and environment variables. Environment variables override file values.

## SCM bearer token

If you already have an SCM bearer token, use it directly:

```bash
export SCM_BEARER_TOKEN=your-bearer-token
```

## SCM OAuth client credentials

If you do not provide `SCM_BEARER_TOKEN`, ARC uses OAuth client credentials:

```bash
export SCM_CLIENT_ID=your-client-id
export SCM_CLIENT_SECRET=your-client-secret
export SCM_TSG_ID=your-tsg-id
```

## SSH

SSH is used for `remote <device>`, `connect`, and command-level `--remote` execution.

```bash
export ARC_SSH_USER=admin
export ARC_SSH_KEY=~/.ssh/panos_key
# optional password fallback
export ARC_SSH_PASS=your-ssh-password
```

## Config helper

```bash
arc auth login
arc auth show
```

Secrets are masked by `arc auth show`.
