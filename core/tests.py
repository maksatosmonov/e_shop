from django.test import TestCase, Client
from django.urls import reverse


class HomepageTestCase(TestCase):
    def setUp(self):
        c = Client()
        self.response = c.get("/")

    # def tearDown(self):


    def test_redirect_from_homepage_302_succes(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertEqual(self.response.url, reverse("product/all"))

    def test_open_homepage(self):
        self.assertNotEqual(self.response.status_code, 200)

