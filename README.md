# EDSanat Platform Case Study

A privacy-safe, clean-room full-stack portfolio project inspired by the architecture of a real
multi-channel industrial commerce platform.

## Languages and technologies

| Area | Languages | Technologies |
| --- | --- | --- |
| Backend | Python, SQL | Django, Django REST Framework, Simple JWT, Gunicorn |
| Web | TypeScript, TSX, CSS | Next.js App Router, React |
| Android | Dart | Flutter, offline operation queue |
| Windows | C#, SQL | .NET 8, WinUI 3 architecture, SQLite, xUnit |
| Data | SQL | PostgreSQL, SQLite, Redis |
| API and security | JSON | REST API, phone OTP, JWT, RBAC, CORS |
| DevOps | YAML, Dockerfile, Shell | Docker, Docker Compose, GitHub Actions |
| Quality | Python, TypeScript, Dart, C# | Ruff, Django TestCase, TypeScript type checking, Flutter Test, xUnit |

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
- end-to-end journey plus automated tests, linting, type checking and builds

## Privacy boundary

Only newly written demo code and synthetic fixtures are public. No production source, customer
records, secrets, internal endpoints, financial rules, licensing logic, or proprietary assets are
included. See [privacy boundary](docs/PRIVACY.md).

## Release v1.0.0

The portfolio case study is complete across backend, web, Android, Windows, operations, security, and
documentation. Start with the [reviewer guide](docs/PORTFOLIO.md), then explore the
[architecture](docs/ARCHITECTURE.md) and [security policy](SECURITY.md).

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

See [local deployment](docs/DEPLOYMENT.md), [authentication](docs/AUTHENTICATION.md),
[commerce](docs/COMMERCE.md), [Android architecture](docs/ANDROID.md), and
[Windows architecture](windows/README.md).

## License

MIT
