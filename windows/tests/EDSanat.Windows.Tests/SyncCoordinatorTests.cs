using EDSanat.Application;
using EDSanat.Domain;
using EDSanat.Infrastructure;

namespace EDSanat.Windows.Tests;

public sealed class SyncCoordinatorTests : IAsyncLifetime
{
    private readonly string _path = Path.GetTempFileName();
    private SqliteSyncQueue Queue => new($"Data Source={_path}");

    public async Task InitializeAsync() => await Queue.InitializeAsync();
    public Task DisposeAsync() { File.Delete(_path); return Task.CompletedTask; }

    [Fact]
    public async Task Successful_push_removes_operation()
    {
        var operation = SyncCoordinator.CreatePosOperation("""{"synthetic":true}""");
        await Queue.EnqueueAsync(operation);
        var completed = await new SyncCoordinator(Queue, new SuccessGateway()).FlushAsync();
        Assert.Equal(1, completed);
        Assert.Empty(await Queue.PendingAsync());
    }

    [Fact]
    public async Task Network_failure_keeps_operation_and_increments_attempts()
    {
        var operation = SyncCoordinator.CreatePosOperation("{}");
        await Queue.EnqueueAsync(operation);
        await new SyncCoordinator(Queue, new OfflineGateway()).FlushAsync();
        var pending = Assert.Single(await Queue.PendingAsync());
        Assert.Equal(operation.ClientOperationId, pending.ClientOperationId);
        Assert.Equal(1, pending.Attempts);
    }

    [Fact]
    public async Task Duplicate_client_operation_is_coalesced()
    {
        var operation = SyncCoordinator.CreatePosOperation("{}");
        await Queue.EnqueueAsync(operation);
        await Queue.EnqueueAsync(operation);
        Assert.Single(await Queue.PendingAsync());
    }

    private sealed class SuccessGateway : IRemoteSyncGateway
    {
        public Task PushPosOperationAsync(SyncOperation operation, CancellationToken token) =>
            Task.CompletedTask;
    }

    private sealed class OfflineGateway : IRemoteSyncGateway
    {
        public Task PushPosOperationAsync(SyncOperation operation, CancellationToken token) =>
            throw new HttpRequestException("offline");
    }
}
