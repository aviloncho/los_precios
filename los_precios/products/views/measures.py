"""Measures Views"""

# Django REST Framework
from rest_framework import mixins, viewsets

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Serializers
from los_precios.products.serializers import MeasureModelSerializer

# Models
from los_precios.products.models import Measure


class MeasureViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    """Measure ViewSet"""
    serializer_class = MeasureModelSerializer

    queryset = Measure.objects.all()

    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('name', 'abrev',)
    ordering_fields = ('name', 'abrev',)
    filter_fields = ('id', 'name', 'abrev',)
