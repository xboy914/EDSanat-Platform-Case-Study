# Android Client

The Flutter client demonstrates a typed catalogue API and an offline checkout queue.

Checkout requests retain one idempotency key across retries. Network failure queues the exact
request instead of duplicating it. Queue flushing stops at the first connectivity failure to
preserve ordering. Django remains authoritative for price and stock.

The in-memory queue is a replaceable milestone adapter. A later SQLite adapter can persist the same
domain objects without coupling UI code to storage. No production endpoints, tokens, products, or
EDSanat mobile source are included.
