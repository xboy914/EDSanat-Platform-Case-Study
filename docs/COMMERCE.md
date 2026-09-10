# Commerce Boundary

The demo checkout is intentionally server-authoritative:

- Clients submit product identifiers and quantities, never trusted prices.
- Products are locked during checkout to protect stock under concurrency.
- Unit price, line total, and order total are calculated with Decimal values on the server.
- Order lines snapshot the public product name, SKU, and price.
- Idempotency keys prevent duplicate orders after mobile or offline retries.
- Invalid products and insufficient stock fail the complete atomic transaction.

All products, prices, images, and orders in this repository are synthetic.
