# Windows Client Architecture

The production source is not included. This folder documents a clean-room reference architecture:

- WinUI 3 and .NET 8 presentation
- CommunityToolkit.Mvvm view models
- Application use cases behind interfaces
- Domain entities without UI dependencies
- Infrastructure adapters for REST, SQLite, sync, and printing
- Offline-first reads and queued writes
- Role-aware admin, sales, accounting, and POS workspaces

A compilable public client will be introduced in a later milestone using only synthetic contracts.
