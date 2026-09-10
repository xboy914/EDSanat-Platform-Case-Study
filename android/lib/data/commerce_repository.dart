import 'package:http/http.dart' as http;
import 'package:uuid/uuid.dart';
import 'checkout_queue.dart';
import 'platform_api.dart';

class CommerceRepository {
  CommerceRepository(this.api, this.queue, {Uuid? uuid}) : _uuid = uuid ?? const Uuid();
  final PlatformApi api;
  final CheckoutQueue queue;
  final Uuid _uuid;
  Future<bool> checkout(String token, Map<int, int> cart) async {
    final item = QueuedCheckout(idempotencyKey: _uuid.v4(), token: token,
      cart: Map.unmodifiable(cart));
    try {
      await api.checkout(token: item.token, idempotencyKey: item.idempotencyKey, cart: item.cart);
      return true;
    } on http.ClientException {
      queue.enqueue(item);
      return false;
    }
  }
  Future<int> flush() async {
    var completed = 0;
    for (final item in List.of(queue.pending)) {
      try {
        await api.checkout(token: item.token, idempotencyKey: item.idempotencyKey, cart: item.cart);
        queue.remove(item.idempotencyKey);
        completed++;
      } on http.ClientException {
        break;
      }
    }
    return completed;
  }
}
