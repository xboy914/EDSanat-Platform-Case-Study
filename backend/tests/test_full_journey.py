from django.core.management import call_command
from django.test import override_settings
from rest_framework.test import APIClient

from catalog.models import Product


@override_settings(DEBUG=True)
def test_synthetic_customer_journey():
    call_command("seed_demo")
    product = Product.objects.get(sku="DEMO-DRV-001")
    initial_stock = product.stock
    client = APIClient()

    otp = client.post(
        "/api/auth/otp/request/",
        {"phone_number": "+31655501000"},
        format="json",
    )
    assert otp.status_code == 201
    verified = client.post(
        "/api/auth/otp/verify/",
        {
            "phone_number": "+31655501000",
            "code": otp.json()["development_code"],
        },
        format="json",
    )
    assert verified.status_code == 200
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {verified.json()['access']}")

    catalogue = client.get("/api/products/")
    assert catalogue.status_code == 200
    assert any(item["sku"] == product.sku for item in catalogue.json())

    payload = {
        "idempotency_key": "DEMO-E2E-CHECKOUT-001",
        "lines": [{"product_id": product.id, "quantity": 2}],
    }
    first = client.post("/api/orders/checkout/", payload, format="json")
    retry = client.post("/api/orders/checkout/", payload, format="json")
    assert first.status_code == 201
    assert retry.status_code == 200
    assert first.json()["id"] == retry.json()["id"]

    product.refresh_from_db()
    assert product.stock == initial_stock - 2
