using EDSanat.Domain;

namespace EDSanat.Application;

public interface ISyncQueue
{
    Task EnqueueAsync(SyncOperation operation, CancellationToken cancellationToken = default);
    Task<IReadOnlyList<SyncOperation>> PendingAsync(CancellationToken cancellationToken = default);
    Task RemoveAsync(Guid id, CancellationToken cancellationToken = default);
    Task MarkNeedsReviewAsync(Guid id, CancellationToken cancellationToken = default);
    Task IncrementAttemptsAsync(Guid id, CancellationToken cancellationToken = default);
}

public interface IRemoteSyncGateway
{
    Task PushPosOperationAsync(SyncOperation operation, CancellationToken cancellationToken);
}

public sealed class RemoteValidationException(string message) : Exception(message);
