from django.test import TestCase
from rest_framework.test import APIClient

from .models import Category, Product


class CatalogApiTests(TestCase):
    def test_catalog_contract_uses_synthetic_data(self):
        category = Category.objects.create(name="Demo Tools", slug="demo-tools")
        Product.objects.create(
            sku="DEMO-001", name="Synthetic Drill", category=category, price="125.00", stock=7
        )
        response = APIClient().get("/api/products/")
        assert response.status_code == 200
        assert response.json()[0]["sku"] == "DEMO-001"

    def test_health_contract(self):
        assert APIClient().get("/health/").json()["status"] == "ok"
