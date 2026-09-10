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
- mobile and desktop architecture boundaries
- automated backend tests, linting, frontend typecheck, and production build

## Privacy boundary

Only newly written demo code and synthetic fixtures are public. No production source, customer
records, secrets, internal endpoints, financial rules, licensing logic, or proprietary assets are
included. See [privacy boundary](docs/PRIVACY.md).

## Milestone v0.4.0

The web client now consumes the DRF catalogue, manages a typed cart, accepts a demo JWT, and submits
only product IDs and quantities to secure checkout. Django owns prices and stock. CORS is explicitly
restricted to configured origins.

## Local checks

```bash
cd backend && pip install -e ".[dev]" && python manage.py test
cd web && npm install && npm run typecheck && npm run build
```

See [authentication](docs/AUTHENTICATION.md), [commerce](docs/COMMERCE.md), and
[architecture](docs/ARCHITECTURE.md).

## License

MIT
