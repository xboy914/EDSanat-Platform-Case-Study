namespace EDSanat.Domain;

public enum SyncStatus { Pending, NeedsReview }

public sealed record SyncOperation(
    Guid ClientOperationId,
    string Kind,
    string Payload,
    DateTimeOffset CreatedAt,
    int Attempts = 0,
    SyncStatus Status = SyncStatus.Pending);
