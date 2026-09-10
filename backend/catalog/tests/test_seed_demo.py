from io import StringIO

from django.core.management import call_command
from django.test import TestCase

from catalog.models import Category, Product, ProductImage


class SeedDemoCommandTests(TestCase):
    def test_seed_is_synthetic_and_idempotent(self):
        output = StringIO()
        call_command("seed_demo", stdout=output)
        call_command("seed_demo", stdout=output)

        self.assertEqual(Category.objects.filter(slug="demo-industrial-tools").count(), 1)
        self.assertEqual(Product.objects.count(), 3)
        self.assertEqual(ProductImage.objects.count(), 3)
        self.assertFalse(Product.objects.exclude(sku__startswith="DEMO-").exists())
        self.assertIn("Synthetic DEMO catalogue is ready.", output.getvalue())
