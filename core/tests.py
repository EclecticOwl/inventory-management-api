from rest_framework.test import APIRequestFactory
from django.test import TestCase

from . import views
from .models import Product

class ProductViewTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_details(self):
        # Test GET request
        request = self.factory.get('/products/')
        response = views.ProductView.as_view()(request)
        self.assertEqual(response.status_code, 200)

        # Test POST request required fields
        request = self.factory.post('/products/', { "name": "hi", "description": "yo", "price_per_unit": 10})
        response = views.ProductView.as_view()(request)
        self.assertEqual(response.status_code, 400)

        # Test POST request invalid field formatting
        request = self.factory.post('/products/', { "name": "hi", "description": "yo", "price_per_unit": "one", "quantity": 2})
        response = views.ProductView.as_view()(request)
        self.assertEqual(response.status_code, 400)

        # Success POST
        request = self.factory.post('/products/', { "name": "hi", "description": "yo", "price_per_unit": 1, "quantity": 2})
        response = views.ProductView.as_view()(request)
        self.assertEqual(response.status_code, 201)
        product = Product.objects.get(pk=1)
        self.assertEqual(product.name, 'hi')
        self.assertEqual(product.description, 'yo')
        self.assertEqual(product.price_per_unit, 1)
        self.assertEqual(product.quantity, 2)

