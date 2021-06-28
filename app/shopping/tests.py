from django.test import TestCase, Client

from .models import Product

# Create your tests here.
"""class ProductTestCase(TestCase):
    def setUp(self):
        # Products
        Product.objects.create(
            name = 'My Product 1',
            description = 'Description of My Product 1 LoremIpsuuuuuuuuuum',
        )
        Product.objects.create(
            name = 'My Product 2',
        )

        self.c = Client()

    def test_product_null_image(self):
        pass"""