# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Utils
from los_precios.utils.models import BaseModel


class Brand(BaseModel):
    """
    Brand class to create product brands.
    """

    name = models.CharField(
        max_length=50,
        verbose_name=_('name')
    )

    def __str__(self):
        return self.name
