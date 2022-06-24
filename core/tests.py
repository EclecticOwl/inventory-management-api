from rest_framework.test import APIRequestFactory, APIClient, APITestCase
from django.urls import reverse
from . import views
from .models import Product

class ProductViewTest(APITestCase):
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
        

class ProductDetailViewTest(APITestCase):

    def test_details(self):
        self.client.post('/products/', { "name": "hi", "description": "yo", "price_per_unit": 1, "quantity": 2})
        # Test detail GET request
        response = self.client.get(reverse('product-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        # Test PUT request
        response = self.client.put(reverse('product-detail', kwargs={'pk': 1}), {"name": "test"})
        self.assertEqual(response.status_code, 200)
        # Test DELETE request
        response = self.client.delete(reverse('product-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 204)
        

        
        
