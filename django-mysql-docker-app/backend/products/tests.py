from django.test import TestCase
from .models import Product

class ProductModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Product.objects.create(name="Test Product", price=10.99, description="A test product")

    def test_product_name(self):
        product = Product.objects.get(id=1)
        self.assertEqual(product.name, "Test Product")

    def test_product_price(self):
        product = Product.objects.get(id=1)
        self.assertEqual(product.price, 10.99)

    def test_product_description(self):
        product = Product.objects.get(id=1)
        self.assertEqual(product.description, "A test product")