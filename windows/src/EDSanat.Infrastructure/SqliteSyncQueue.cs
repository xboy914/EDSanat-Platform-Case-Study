using EDSanat.Application;
using EDSanat.Domain;
using Microsoft.Data.Sqlite;

namespace EDSanat.Infrastructure;

public sealed class SqliteSyncQueue(string connectionString) : ISyncQueue
{
    public async Task InitializeAsync()
    {
        await using var connection = new SqliteConnection(connectionString);
        await connection.OpenAsync();
        var command = connection.CreateCommand();
        command.CommandText = """
            CREATE TABLE IF NOT EXISTS sync_queue (
              client_operation_id TEXT PRIMARY KEY,
              kind TEXT NOT NULL,
              payload TEXT NOT NULL,
              created_at TEXT NOT NULL,
              attempts INTEGER NOT NULL,
              status INTEGER NOT NULL
            );
            """;
        await command.ExecuteNonQueryAsync();
    }

    public async Task EnqueueAsync(SyncOperation operation, CancellationToken cancellationToken = default)
    {
        await using var connection = await OpenAsync(cancellationToken);
        var command = connection.CreateCommand();
        command.CommandText = """
            INSERT OR IGNORE INTO sync_queue
            (client_operation_id, kind, payload, created_at, attempts, status)
            VALUES ($id, $kind, $payload, $created, $attempts, $status);
            """;
        command.Parameters.AddWithValue("$id", operation.ClientOperationId.ToString());
        command.Parameters.AddWithValue("$kind", operation.Kind);
        command.Parameters.AddWithValue("$payload", operation.Payload);
        command.Parameters.AddWithValue("$created", operation.CreatedAt.ToString("O"));
        command.Parameters.AddWithValue("$attempts", operation.Attempts);
        command.Parameters.AddWithValue("$status", (int)operation.Status);
        await command.ExecuteNonQueryAsync(cancellationToken);
    }

    public async Task<IReadOnlyList<SyncOperation>> PendingAsync(
        CancellationToken cancellationToken = default)
    {
        await using var connection = await OpenAsync(cancellationToken);
        var command = connection.CreateCommand();
        command.CommandText = "SELECT * FROM sync_queue WHERE status = 0 ORDER BY created_at;";
        await using var reader = await command.ExecuteReaderAsync(cancellationToken);
        var result = new List<SyncOperation>();
        while (await reader.ReadAsync(cancellationToken))
            result.Add(new SyncOperation(Guid.Parse(reader.GetString(0)), reader.GetString(1),
                reader.GetString(2), DateTimeOffset.Parse(reader.GetString(3)),
                reader.GetInt32(4), (SyncStatus)reader.GetInt32(5)));
        return result;
    }

    public Task RemoveAsync(Guid id, CancellationToken cancellationToken = default) =>
        ExecuteAsync("DELETE FROM sync_queue WHERE client_operation_id = $id;", id, cancellationToken);

    public Task MarkNeedsReviewAsync(Guid id, CancellationToken cancellationToken = default) =>
        ExecuteAsync("UPDATE sync_queue SET status = 1 WHERE client_operation_id = $id;",
            id, cancellationToken);

    public Task IncrementAttemptsAsync(Guid id, CancellationToken cancellationToken = default) =>
        ExecuteAsync("UPDATE sync_queue SET attempts = attempts + 1 WHERE client_operation_id = $id;",
            id, cancellationToken);

    private async Task ExecuteAsync(string sql, Guid id, CancellationToken cancellationToken)
    {
        await using var connection = await OpenAsync(cancellationToken);
        var command = connection.CreateCommand();
        command.CommandText = sql;
        command.Parameters.AddWithValue("$id", id.ToString());
        await command.ExecuteNonQueryAsync(cancellationToken);
    }

    private async Task<SqliteConnection> OpenAsync(CancellationToken cancellationToken)
    {
        var connection = new SqliteConnection(connectionString);
        await connection.OpenAsync(cancellationToken);
        return connection;
    }
}
