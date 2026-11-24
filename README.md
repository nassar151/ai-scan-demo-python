# ai-scan-demo-python

A small Python + Flask shop API with **intentional** security issues, used to test
AI Scan Review on every finding type: code, secret and dependency (direct and indirect).
Do not deploy it.

## Code

| Issue | Where | Expected |
|---|---|---|
| SQL injection | `app/routes/users.py` | Reachable from `GET /users/search` |
| SQL built with `%` | `app/routes/reports.py` | False positive: `sort` is checked against an allowlist first |
| Command injection | `app/routes/tools.py` | Reachable from `POST /tools/ping` |
| Command injection | `scripts/legacy_cleanup.py` | Not reachable: nothing imports or runs it |
| Insecure deserialization (`pickle`, `yaml.Loader`) | `app/routes/imports.py` | Reachable from `POST /imports/*` |
| SSRF + TLS verification disabled | `app/routes/proxy.py` | Reachable from `GET /proxy/preview` |
| Server-side template injection / XSS | `app/routes/pages.py` | Reachable from `GET /hello` |
| MD5 for passwords | `app/utils/security.py` | Used by `POST /auth/login` |
| Hard-coded JWT signing key | `app/routes/auth.py` | Used by `POST /auth/login` |
| Hard-coded Flask `SECRET_KEY` | `app/__init__.py` | Signs every session cookie |
| Server bound to `0.0.0.0` with `debug=True` | `run.py` | Exposed when run directly |

## Secrets

| Secret | Where | Expected |
|---|---|---|
| Mailgun API key (fake) | `app/config.py` | Used by `POST /auth/forgot-password` |
| JWT service token (fake) | `app/config.py` | Defined but never used |

## Dependencies (`requirements.txt`, pip-compile format)

| Package | Relation | Expected |
|---|---|---|
| `pyyaml@5.3.1` | Direct | Reachable: `yaml.load` in `imports.py` |
| `requests@2.25.1` | Direct | Reachable: `proxy.py`, `mailer.py` |
| `pyjwt@1.7.1` | Direct | Reachable: `jwt.encode` in `auth.py` |
| `flask@1.1.2` | Direct | Reachable: the whole app |
| `pillow@10.0.0` | Direct | Not reachable: never imported |
| `werkzeug@1.0.1`, `jinja2@2.11.2` | Indirect via `flask` | Reachable through Flask |
| `urllib3@1.26.4`, `certifi@2020.12.5`, `idna@2.10` | Indirect via `requests` | Reachable through `requests` |
