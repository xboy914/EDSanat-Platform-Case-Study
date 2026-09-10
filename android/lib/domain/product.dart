class Product {
  const Product({required this.id, required this.sku, required this.name,
    required this.price, required this.stock});
  final int id;
  final String sku;
  final String name;
  final double price;
  final int stock;
  factory Product.fromJson(Map<String, dynamic> json) => Product(
    id: json['id'] as int, sku: json['sku'] as String, name: json['name'] as String,
    price: double.parse(json['price'] as String), stock: json['stock'] as int);
}
