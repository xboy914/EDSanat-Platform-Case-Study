class QueuedCheckout {
  const QueuedCheckout({required this.idempotencyKey, required this.token, required this.cart});
  final String idempotencyKey;
  final String token;
  final Map<int, int> cart;
}
class CheckoutQueue {
  final List<QueuedCheckout> _items = [];
  List<QueuedCheckout> get pending => List.unmodifiable(_items);
  void enqueue(QueuedCheckout checkout) {
    if (_items.any((item) => item.idempotencyKey == checkout.idempotencyKey)) return;
    _items.add(checkout);
  }
  void remove(String key) => _items.removeWhere((item) => item.idempotencyKey == key);
}
