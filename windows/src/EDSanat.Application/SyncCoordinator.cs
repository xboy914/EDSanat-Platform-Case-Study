using EDSanat.Domain;

namespace EDSanat.Application;

public sealed class SyncCoordinator(ISyncQueue queue, IRemoteSyncGateway gateway)
{
    public async Task<int> FlushAsync(CancellationToken cancellationToken = default)
    {
        var completed = 0;
        foreach (var operation in await queue.PendingAsync(cancellationToken))
        {
            try
            {
                await gateway.PushPosOperationAsync(operation, cancellationToken);
                await queue.RemoveAsync(operation.ClientOperationId, cancellationToken);
                completed++;
            }
            catch (RemoteValidationException)
            {
                await queue.MarkNeedsReviewAsync(operation.ClientOperationId, cancellationToken);
            }
            catch (HttpRequestException)
            {
                await queue.IncrementAttemptsAsync(operation.ClientOperationId, cancellationToken);
                break;
            }
        }
        return completed;
    }

    public static SyncOperation CreatePosOperation(string payload) =>
        new(Guid.NewGuid(), "pos.order.create", payload, DateTimeOffset.UtcNow);
}
