"""ItemPrices serializers"""

# Django REST Framework
from rest_framework import serializers

# Serializers
from los_precios.prices.serializers import StoreModelSerializer

# Models
from los_precios.prices.models import ItemPrice


class ItemPriceModelSerializer(serializers.ModelSerializer):
    """ItemPrice Model Serializer"""
    store = StoreModelSerializer(read_only=True)

    class Meta:
        model = ItemPrice
        fields = (
            'id',
            'store',
            'price',
        )
