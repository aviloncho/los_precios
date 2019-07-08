"""Brand serializers"""

# Django REST Framework
from rest_framework import serializers

# Models
from los_precios.products.models import Brand


class ItemBrandSerializer(serializers.ModelSerializer):
    """ItemBrand Model Serializer"""

    class Meta:
        model = Brand
        fields = (
            'id',
            'name',
        )


class BrandModelSerializer(serializers.ModelSerializer):
    """Brand Model Serializer"""

    class Meta:
        model = Brand
        fields = (
            'id',
            'name',
            'created',
            'modified',
        )
