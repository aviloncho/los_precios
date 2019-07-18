"""Store serializers"""

# Django REST Framework
from rest_framework import serializers

# Models
from los_precios.prices.models import Store


class StoreModelSerializer(serializers.ModelSerializer):
    """Store Model Serializer"""

    class Meta:
        model = Store
        fields = (
            'id',
            'name',
        )
