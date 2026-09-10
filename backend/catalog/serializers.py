from typing import ClassVar

from rest_framework import serializers

from .models import Category, Product, ProductImage


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields: ClassVar = ["id", "name", "slug", "parent"]


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields: ClassVar = ["url", "alt_text", "position"]


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields: ClassVar = [
            "id", "sku", "name", "category", "category_name", "price", "stock", "images"
        ]
