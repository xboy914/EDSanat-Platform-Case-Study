from django.contrib.auth.models import User
from django.db import models


class Order(models.Model):
    class Status(models.TextChoices):
        PLACED = "placed", "Placed"
        PROCESSING = "processing", "Processing"
        COMPLETED = "completed", "Completed"
        CANCELLED = "cancelled", "Cancelled"

    customer = models.ForeignKey(User, on_delete=models.PROTECT, related_name="orders")
    idempotency_key = models.CharField(max_length=64, unique=True)
    status = models.CharField(max_length=16, choices=Status.choices, default=Status.PLACED)
    total = models.DecimalField(max_digits=14, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


class OrderLine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="lines")
    product = models.ForeignKey("catalog.Product", on_delete=models.PROTECT)
    product_name = models.CharField(max_length=200)
    sku = models.CharField(max_length=64)
    unit_price = models.DecimalField(max_digits=14, decimal_places=2)
    quantity = models.PositiveIntegerField()
    line_total = models.DecimalField(max_digits=14, decimal_places=2)
