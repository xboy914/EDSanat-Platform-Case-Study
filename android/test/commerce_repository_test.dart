import 'package:edsanat_case_study/data/checkout_queue.dart';
import 'package:edsanat_case_study/data/commerce_repository.dart';
import 'package:edsanat_case_study/data/platform_api.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:http/http.dart' as http;
import 'package:http/testing.dart';

void main() {
  test('network failure queues checkout', () async {
    final client = MockClient((_) async => throw http.ClientException('offline'));
    final queue = CheckoutQueue();
    final repository = CommerceRepository(
      PlatformApi(baseUrl: 'https://demo.invalid', client: client), queue);
    expect(await repository.checkout('demo-token', {7: 2}), isFalse);
    expect(queue.pending.single.cart, {7: 2});
  });
  test('duplicate queue keys are coalesced', () {
    final queue = CheckoutQueue();
    const item = QueuedCheckout(idempotencyKey: 'stable-key',
      token: 'demo-token', cart: {1: 1});
    queue..enqueue(item)..enqueue(item);
    expect(queue.pending, hasLength(1));
  });
  test('catalogue maps typed products', () async {
    final client = MockClient((_) async => http.Response(
      '[{"id":1,"sku":"DEMO","name":"Synthetic Tool","price":"12.50","stock":3}]', 200));
    final products = await PlatformApi(
      baseUrl: 'https://demo.invalid', client: client).catalogue();
    expect(products.single.price, 12.5);
  });
}
