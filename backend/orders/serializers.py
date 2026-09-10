from typing import ClassVar

from rest_framework import serializers

from .models import Order, OrderLine


class CheckoutLineSerializer(serializers.Serializer):
    product_id = serializers.IntegerField(min_value=1)
    quantity = serializers.IntegerField(min_value=1, max_value=100)


class CheckoutSerializer(serializers.Serializer):
    idempotency_key = serializers.CharField(min_length=8, max_length=64)
    lines = CheckoutLineSerializer(many=True, allow_empty=False)


class OrderLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderLine
        fields: ClassVar = ["product_name", "sku", "unit_price", "quantity", "line_total"]


class OrderSerializer(serializers.ModelSerializer):
    lines = OrderLineSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields: ClassVar = ["id", "status", "total", "created_at", "lines"]
