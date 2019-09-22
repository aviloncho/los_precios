"""Item serializers"""

# Django REST Framework
from rest_framework import serializers

# Serializers
from los_precios.products.serializers import BrandModelSerializer, MeasureModelSerializer
from los_precios.prices.serializers import ItemPriceModelSerializer

# Models
from los_precios.products.models import Item


class ItemModelSerializer(serializers.ModelSerializer):
    """Item Model Serializer"""

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
            'lp_product',
            'lp_brand',
            'lp_size',
            'lp_complement',
            'lp_store_id',
            'lp_store_url',
            'created',
            'modified',
        )


class ViewItemModelSerializer(serializers.ModelSerializer):
    """Item Model Serializer"""
    brand = BrandModelSerializer(read_only=True)
    measure = MeasureModelSerializer(read_only=True)
    prices = ItemPriceModelSerializer(read_only=True, many=True)

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
            'lp_product',
            'lp_brand',
            'lp_size',
            'lp_complement',
            'lp_store_id',
            'lp_store_url',
            'prices',
            'created',
            'modified',
        )
