# Platform Architecture

The case study separates a Django/DRF system of record from channel-specific clients.

- Next.js serves the public web and operations workspace.
- Flutter provides the Android experience with a future offline cache.
- WinUI 3 represents the offline-first Windows administration and POS client.
- PostgreSQL stores transactional data; Redis is reserved for cache and background work.
- Docker Compose provides a reproducible local environment.

Clients depend on versioned API contracts, not database details. Authentication, catalogue,
inventory, orders, accounting, sync, and audit concerns evolve as bounded modules.
