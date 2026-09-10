# Windows Offline-First Core

This clean-room .NET 8 implementation keeps the production WinUI source private while demonstrating
the testable layers behind it.

- Domain owns sync operation identity and status.
- Application owns queue and remote gateway contracts plus ordered orchestration.
- Infrastructure persists the queue in SQLite.
- WinUI 3 remains a presentation adapter for admin, sales, accounting, and POS workspaces.
- Only POS write operations may enter the offline queue; other disconnected modules are read-only.

Every operation receives a stable client operation ID. Successful pushes are removed, network
failures remain pending with an incremented attempt count, and server validation failures move to
NeedsReview. SQLite uses a primary key plus INSERT OR IGNORE to coalesce duplicates.

Run on any .NET 8 SDK:

```bash
dotnet test tests/EDSanat.Windows.Tests/EDSanat.Windows.Tests.csproj
```
