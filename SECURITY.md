# Security policy

## Supported version

This public case study supports the latest commit on `main`. It is not the production EDSanat
system and must not receive real customer data or credentials.

## Reporting

Please do not open a public issue for a suspected vulnerability. Use GitHub's private vulnerability
reporting for this repository. Include affected component, reproduction steps, impact, and a minimal
proof of concept that contains no real-world data.

## Demonstrated controls

- short-lived JWT access tokens and single-use OTP challenges
- server-authoritative prices and transactional inventory updates
- idempotent checkout and offline operation identifiers
- required runtime secrets, non-root application containers, and health checks
- synthetic fixtures only; no production integrations or internal endpoints

This document describes portfolio controls, not a security certification. An internet-facing
deployment additionally requires TLS, managed secrets, rate limiting, monitoring, backups, patch
management, network policy, and an independent security review.
