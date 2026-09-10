import 'dart:convert';
import 'package:http/http.dart' as http;
import '../domain/product.dart';

class PlatformApi {
  PlatformApi({required this.baseUrl, http.Client? client}) : _client = client ?? http.Client();
  final String baseUrl;
  final http.Client _client;
  Future<List<Product>> catalogue() async {
    final response = await _client.get(Uri.parse('$baseUrl/api/products/'));
    if (response.statusCode != 200) throw http.ClientException('Catalogue request failed');
    final body = jsonDecode(response.body) as List<dynamic>;
    return body.map((item) => Product.fromJson(item as Map<String, dynamic>)).toList();
  }
  Future<void> checkout({required String token, required String idempotencyKey,
      required Map<int, int> cart}) async {
    final response = await _client.post(Uri.parse('$baseUrl/api/orders/checkout/'),
      headers: {'Content-Type': 'application/json', 'Authorization': 'Bearer $token'},
      body: jsonEncode({'idempotency_key': idempotencyKey,
        'lines': cart.entries.map((e) => {'product_id': e.key, 'quantity': e.value}).toList()}));
    if (response.statusCode != 200 && response.statusCode != 201) {
      throw http.ClientException('Checkout request failed');
    }
  }
}
