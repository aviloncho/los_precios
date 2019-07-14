"""Measure serializers"""

# Django REST Framework
from rest_framework import serializers

# Models
from los_precios.products.models import Measure


class MeasureModelSerializer(serializers.ModelSerializer):
    """Measure Model Serializer"""

    class Meta:
        model = Measure
        fields = (
            'id',
            'name',
            'abrev',
        )
