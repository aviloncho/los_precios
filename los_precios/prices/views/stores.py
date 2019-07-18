"""Store Views"""

# Django REST Framework
from rest_framework import mixins, viewsets

# Permissions
from rest_framework.permissions import IsAuthenticated

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Serializers
from los_precios.prices.serializers import StoreModelSerializer

# Models
from los_precios.prices.models import Store


class StoreViewSet(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   viewsets.GenericViewSet):
    """Store ViewSet"""
    serializer_class = StoreModelSerializer

    queryset = Store.objects.all()

    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('name',)
    ordering_fields = ('name',)
    filter_fields = ('id', 'name',)

    def get_permissions(self):
        permissions = [IsAuthenticated]

        return [permission() for permission in permissions]
