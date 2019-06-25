# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Utils
from los_precios.utils.models import BaseModel


class Measure(BaseModel):
    """
    Measure class to create product Measures.
    """

    name = models.CharField(
        max_length=50,
        verbose_name=_('name')
    )

    abrev = models.CharField(
        max_length=5,
        verbose_name=_('abbreviation')
    )

    def __str__(self):
        return '{} ({})'.format(self.name, self.abrev)
