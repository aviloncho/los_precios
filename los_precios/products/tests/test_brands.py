"""Brands tests"""

#Django
from django.test import TestCase

#Django REST Framework
from rest_framework.test import APITestCase
from rest_framework import status

#Model
from los_precios.products.models import Brand
from los_precios.users.models import User


class BrandManagerTestCase(TestCase):

    def setUp(self):
        """Test case setup"""
        self.user = User.objects.create(
            name='Juan Avila',
            email='juanavila@mail.com',
            username='juanavila',
            password='admin123'
        )

    def test_brand_creation(self):
        """Test id Brand creation"""
        brand = Brand.objects.create(
            name='Brand Name'
        )

        self.assertIsNotNone(brand)
    
class BrandAPITestCase(APITestCase):

    def setUp(self):
        """Test case setup"""
        self.user = User.objects.create(
            name='Juan Avila',
            email='juanavila@mail.com',
            username='juanavila',
            password='admin123'
        )
    
    def test_response_success(self):
        url = '/products/brands/'
        request = self.client.get(url)
        self.assertEqual(request.status_code, status.HTTP_200_OK)
