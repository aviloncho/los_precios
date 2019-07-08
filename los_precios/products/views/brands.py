"""Brands Views"""

# Django REST Framework
from rest_framework import mixins, viewsets

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Serializers
from los_precios.products.serializers import BrandModelSerializer

# Models
from los_precios.products.models import Brand


class BrandViewSet(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   viewsets.GenericViewSet):
    """Brand ViewSet"""
    serializer_class = BrandModelSerializer

    queryset = Brand.objects.all()

    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('name',)
    ordering_fields = ('name',)
    filter_fields = ('id', 'name',)
