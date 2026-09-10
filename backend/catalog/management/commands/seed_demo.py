from decimal import Decimal

from django.core.management.base import BaseCommand
from django.db import transaction

from catalog.models import Category, Product, ProductImage


class Command(BaseCommand):
    help = "Create an idempotent, synthetic DEMO catalogue. Never imports production data."

    @transaction.atomic
    def handle(self, *args, **options):
        category, _ = Category.objects.get_or_create(
            slug="demo-industrial-tools",
            defaults={"name": "Demo Industrial Tools"},
        )
        fixtures = (
            ("DEMO-DRV-001", "Demo Variable Speed Drive", "1250.00", 12),
            ("DEMO-SNS-002", "Demo Proximity Sensor", "89.90", 40),
            ("DEMO-CTL-003", "Demo Control Panel", "2350.00", 5),
        )
        for sku, name, price, stock in fixtures:
            product, _ = Product.objects.update_or_create(
                sku=sku,
                defaults={
                    "name": name,
                    "category": category,
                    "price": Decimal(price),
                    "stock": stock,
                    "is_active": True,
                },
            )
            ProductImage.objects.update_or_create(
                product=product,
                position=0,
                defaults={
                    "url": f"https://placehold.co/800x600?text={sku}",
                    "alt_text": f"Synthetic illustration for {name}",
                },
            )
        self.stdout.write(self.style.SUCCESS("Synthetic DEMO catalogue is ready."))
