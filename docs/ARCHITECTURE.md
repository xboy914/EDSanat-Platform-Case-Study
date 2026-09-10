# Platform architecture

The case study separates a Django/DRF system of record from channel-specific clients.

```mermaid
flowchart TB
  Web["Next.js web"] --> API["Django REST API"]
  Android["Flutter Android"] --> API
  Windows[".NET Windows core"] --> API
  API --> DB[("PostgreSQL")]
  API -. "future jobs/cache" .-> Redis[("Redis")]
```

## Boundaries

- The API owns identity, catalogue, authoritative prices, inventory, and order transactions.
- Web is an online typed client; Android and Windows expose durable offline-operation boundaries.
- PostgreSQL stores transactional state. Redis is provisioned but no worker integration is claimed.
- Docker Compose is the reproducible local deployment, not an internet-production prescription.

## Checkout sequence

```mermaid
sequenceDiagram
  participant C as Client
  participant A as API
  participant D as PostgreSQL
  C->>A: JWT + idempotency key + lines
  A->>D: lock products in transaction
  A->>D: price, decrement stock, create order
  D-->>A: committed order
  A-->>C: authoritative total
  C->>A: retry same key
  A-->>C: same order, no second decrement
```

## Privacy boundary

All public implementation and fixtures are newly written. The repository excludes production source,
customer records, credentials, internal URLs, financial rules, licensing logic, private screenshots,
and proprietary assets.
