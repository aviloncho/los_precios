"""Items Views"""

# Django REST Framework
from rest_framework import mixins, viewsets

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Serializers
from los_precios.products.serializers import ItemModelSerializer

# Models
from los_precios.products.models import Item


class ItemViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    """Item ViewSet"""
    serializer_class = ItemModelSerializer

    queryset = Item.objects.all()

    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('barcode', 'name',)
    ordering_fields = ('name', 'quantity',)
    filter_fields = (
        'id',
        'barcode',
        'name',
        'is_pack',
        'lp_id',
    )
