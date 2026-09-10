# Authentication and Roles

The public demo uses passwordless phone authentication:

1. A normalized E.164-compatible phone number requests a challenge.
2. A cryptographically random six-digit code is stored only as a keyed digest.
3. The latest challenge expires after five minutes, allows at most five attempts, and is single-use.
4. Successful verification returns short-lived JWT access and refresh tokens.

The code is returned only when Django DEBUG is enabled so automated tests and local demos need no
SMS vendor. Production adapters should send the code through a provider without logging it.

Roles are customer, seller, support, and admin. API views declare allowed roles at the boundary.
Production EDSanat users, phone numbers, tokens, and provider configuration are not included.
