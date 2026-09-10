from django.contrib.auth.models import User
from rest_framework.test import APIClient

from accounts.models import Profile
from catalog.models import Category, Product

from .models import Order


def test_checkout_calculates_price_server_side_and_decrements_stock():
    user = User.objects.create(username="+31600000001")
    Profile.objects.create(user=user, phone_number="+31600000001")
    category = Category.objects.create(name="Synthetic", slug="synthetic")
    product = Product.objects.create(
        sku="DEMO-CART-1", name="Demo Tool", category=category, price="25.00", stock=5
    )
    client = APIClient()
    client.force_authenticate(user)
    response = client.post(
        "/api/orders/checkout/",
        {
            "idempotency_key": "checkout-demo-001",
            "lines": [{"product_id": product.id, "quantity": 2, "price": "0.01"}],
        },
        format="json",
    )
    assert response.status_code == 201
    assert response.json()["total"] == "50.00"
    product.refresh_from_db()
    assert product.stock == 3


def test_checkout_is_idempotent():
    user = User.objects.create(username="+31600000002")
    Profile.objects.create(user=user, phone_number="+31600000002")
    category = Category.objects.create(name="Synthetic 2", slug="synthetic-2")
    product = Product.objects.create(
        sku="DEMO-CART-2", name="Demo Saw", category=category, price="10.00", stock=5
    )
    client = APIClient()
    client.force_authenticate(user)
    payload = {
        "idempotency_key": "checkout-demo-002",
        "lines": [{"product_id": product.id, "quantity": 1}],
    }
    assert client.post("/api/orders/checkout/", payload, format="json").status_code == 201
    assert client.post("/api/orders/checkout/", payload, format="json").status_code == 200
    assert Order.objects.count() == 1
    product.refresh_from_db()
    assert product.stock == 4
