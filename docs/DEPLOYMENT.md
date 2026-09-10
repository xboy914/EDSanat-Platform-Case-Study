# Local deployment

This deployment is a clean-room demonstration. It contains only newly written code and synthetic
fixtures; it does not connect to any EDSanat production system.

## Start

1. Copy `.env.example` to `.env`.
2. Replace both placeholder secrets with long random values.
3. Run `docker compose up --build`.
4. Open the web app at http://localhost:3000 and API health at http://localhost:8000/health/.

The API waits for PostgreSQL and Redis, applies Django migrations with `--run-syncdb`, and runs the
idempotent `seed_demo` command before Gunicorn starts. Every fixture SKU begins with `DEMO-`.

## Services

| Service | Purpose | Published port |
| --- | --- | --- |
| web | Next.js production server | 3000 |
| api | Django REST API through Gunicorn | 8000 |
| db | PostgreSQL persistence | internal only |
| redis | cache/queue-ready infrastructure | internal only |

Redis is provisioned for future background jobs; this milestone does not claim a worker integration.

## Operations

- Stop services: `docker compose down`
- Rebuild: `docker compose up --build`
- Remove only demo volumes: `docker compose down --volumes`

Do not reuse the example configuration as-is for an internet-facing deployment. Production requires
managed secrets, TLS termination, backups, observability, restrictive network policy, and a reviewed
Django security configuration.
