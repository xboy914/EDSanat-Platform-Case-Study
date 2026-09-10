# EDSanat Platform Case Study

A privacy-safe, clean-room full-stack portfolio project inspired by the architecture of a real
multi-channel industrial commerce platform.

## Four engineering surfaces

- **Backend:** Django, Django REST Framework, PostgreSQL
- **Web:** Next.js App Router, React, TypeScript
- **Android:** Flutter and Dart
- **Windows:** C#, .NET 8, WinUI 3, SQLite, offline-first sync

## What is public

This repository contains newly written demo code, synthetic fixtures, API contracts, architecture
decisions, tests, CI, and deployment examples.

## What is not public

No production source, customer records, secrets, internal endpoints, financial rules, licensing
logic, or proprietary EDSanat assets are included. See [privacy boundary](docs/PRIVACY.md).

## Repository map

- `backend/` — Django/DRF catalogue foundation
- `web/` — responsive Next.js architecture showcase
- `android/` — Flutter Android client scaffold
- `windows/` — offline-first WinUI architecture boundary
- `docs/` — architecture and disclosure policy

## Milestone v0.3.0

The platform now demonstrates a server-authoritative commerce flow: hierarchical catalogue,
multiple product images, transactional stock reservation, immutable order-line price snapshots,
customer order history, and idempotent checkout. See [commerce design](docs/COMMERCE.md) and
[authentication design](docs/AUTHENTICATION.md).

## Local checks

```bash
cd backend && pip install -e ".[dev]" && python manage.py test
cd web && npm install && npm run typecheck && npm run build
```

## License

MIT
