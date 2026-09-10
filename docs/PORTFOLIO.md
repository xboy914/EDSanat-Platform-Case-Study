# Reviewer guide

EDSanat Platform Case Study demonstrates full-stack engineering across one shared commerce domain
without publishing the private product.

| Surface | Evidence |
| --- | --- |
| Backend | Django/DRF modules, OTP/JWT, RBAC, catalogue, transactional checkout |
| Web | Next.js App Router, typed API boundary, storefront, cart and checkout |
| Android | Flutter client boundary, durable offline queue and reconnect tests |
| Windows | .NET 8 layered core, SQLite queue, stable operation IDs and xUnit tests |
| Operations | Docker Compose, PostgreSQL, Redis, Gunicorn, health checks and CI |
| Security | synthetic-only fixtures, server-side pricing, short-lived tokens, non-root containers |

## End-to-end story

A reviewer can request a development OTP, receive JWT credentials, browse the synthetic catalogue,
submit a checkout using a stable idempotency key, and observe inventory change exactly once. Android
and Windows clients demonstrate how pending operations survive offline periods and replay in order.

## Scope honesty

This repository intentionally demonstrates architecture and engineering decisions rather than the
private product's UI, data, algorithms, or integrations. Redis is infrastructure-ready; no
background worker is claimed. WinUI presentation source is not included; the portable .NET core is
the public evidence.

## Fast review

1. Read the root README and architecture diagram.
2. Inspect `backend/orders/services.py` for transactional checkout.
3. Inspect Android and Windows queue tests.
4. Review `compose.yml` and the five CI jobs.
5. Run the quick-start commands with synthetic data only.
