from django.test import TestCase, Client
from django.urls import reverse
from .models import Product


class HomepageTestCase(TestCase):
    def setUp(self):
        products_url = reverse("products")
        c = Client()
        self.response = c.get(products_url)
        self.response = Product.objects.all()

    def test_products_open_200_ok(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, "ALL ITEMS")
 


