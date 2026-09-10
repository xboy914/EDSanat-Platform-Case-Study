from decimal import Decimal

from django.db import transaction
from rest_framework.exceptions import ValidationError

from catalog.models import Product

from .models import Order, OrderLine


@transaction.atomic
def checkout(*, customer, idempotency_key: str, lines: list[dict]) -> tuple[Order, bool]:
    existing = Order.objects.filter(idempotency_key=idempotency_key).first()
    if existing:
        if existing.customer_id != customer.id:
            raise ValidationError("Idempotency key already belongs to another customer.")
        return existing, False

    product_ids = [line["product_id"] for line in lines]
    products = {
        product.id: product
        for product in Product.objects.select_for_update().filter(
            id__in=product_ids, is_active=True
        )
    }
    if len(products) != len(set(product_ids)):
        raise ValidationError("One or more products are unavailable.")

    total = Decimal("0")
    prepared = []
    for line in lines:
        product = products[line["product_id"]]
        quantity = line["quantity"]
        if product.stock < quantity:
            raise ValidationError(f"Insufficient stock for {product.sku}.")
        line_total = product.price * quantity
        total += line_total
        prepared.append((product, quantity, line_total))

    order = Order.objects.create(
        customer=customer, idempotency_key=idempotency_key, total=total
    )
    for product, quantity, line_total in prepared:
        OrderLine.objects.create(
            order=order,
            product=product,
            product_name=product.name,
            sku=product.sku,
            unit_price=product.price,
            quantity=quantity,
            line_total=line_total,
        )
        product.stock -= quantity
        product.save(update_fields=["stock"])
    return order, True
