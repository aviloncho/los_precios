"""Item serializers"""

# Django REST Framework
from rest_framework import serializers

# Serializers
from los_precios.products.serializers import ItemBrandSerializer

# Models
from los_precios.products.models import Item


class ItemModelSerializer(serializers.ModelSerializer):
    """Item Model Serializer"""
    brand = ItemBrandSerializer(read_only=True)

    class Meta:
        model = Item
        fields = (
            'id',
            'barcode',
            'name',
            'brand',
            'description',
            'quantity',
            'measure',
            'is_pack',
            'pack_quantity',
            'lp_id',
            'lp_url',
            'created',
            'modified',
        )
