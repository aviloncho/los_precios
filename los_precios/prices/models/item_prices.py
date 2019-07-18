# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Utils
from los_precios.utils.models import BaseModel

# Models
from los_precios.products.models import Item
from los_precios.prices.models import Store


class ItemPrice(BaseModel):
    """
    ItemPrice class to create Item prices by Store.
    """

    item = models.ForeignKey(
        Item,
        verbose_name=_('item'),
        related_name='prices',
        on_delete=models.PROTECT,
    )

    store = models.ForeignKey(
        Store,
        verbose_name=_('store'),
        on_delete=models.PROTECT,
    )

    price = models.DecimalField(
        max_digits=16,
        decimal_places=2,
        verbose_name=_('price'),
    )

    def __str__(self):
        return '{}({}): {}'.format(self.item.name, self.store.name, self.price)
