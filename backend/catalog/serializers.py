from typing import ClassVar

from rest_framework import serializers

from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields: ClassVar = ["id", "name", "slug", "parent"]


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True)

    class Meta:
        model = Product
        fields: ClassVar = [
            "id", "sku", "name", "category", "category_name", "price", "stock"
        ]
