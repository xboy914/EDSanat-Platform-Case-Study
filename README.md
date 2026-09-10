# EDSanat Platform Case Study

A privacy-safe, clean-room full-stack portfolio project inspired by the architecture of a real
multi-channel industrial commerce platform.

## Four engineering surfaces

- **Backend:** Django, Django REST Framework, PostgreSQL
- **Web:** Next.js App Router, React, TypeScript
- **Android:** Flutter and Dart
- **Windows:** C#, .NET 8, WinUI 3, SQLite, offline-first sync

## Demonstrated capabilities

- passwordless phone OTP, JWT, and role boundaries
- hierarchical catalogue and ordered product galleries
- interactive Next.js storefront and client-side cart
- server-authoritative, transactional and idempotent checkout
- offline-first Android and Windows sync boundaries
- Docker Compose deployment with PostgreSQL and Redis
- automated tests, linting, type checking, builds, and container validation

## Privacy boundary

Only newly written demo code and synthetic fixtures are public. No production source, customer
records, secrets, internal endpoints, financial rules, licensing logic, or proprietary assets are
included. See [privacy boundary](docs/PRIVACY.md).

## Milestone v0.7.0

The full stack now runs as production-shaped containers: a non-root Gunicorn API, a Next.js
production server, PostgreSQL persistence, Redis infrastructure, health checks, startup migrations,
and an idempotent synthetic catalogue seed. See [local deployment](docs/DEPLOYMENT.md).

## Quick start

```bash
cp .env.example .env
# Replace the placeholder secrets in .env
docker compose up --build
```

Open http://localhost:3000 and verify the API at http://localhost:8000/health/.

## Local checks

```bash
cd backend && pip install -e ".[dev]" && python manage.py test
cd web && npm install && npm run typecheck && npm run build
```

See [authentication](docs/AUTHENTICATION.md), [commerce](docs/COMMERCE.md),
[Android architecture](docs/ANDROID.md), [Windows architecture](windows/README.md), and
[system architecture](docs/ARCHITECTURE.md).

## License

MIT
