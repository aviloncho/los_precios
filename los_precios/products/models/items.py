# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Utils
from los_precios.utils.models import BaseModel

# Models
from los_precios.products.models import Brand, Measure


class Item(BaseModel):
    """
    Item class to create productos
    """
    class Meta:
        verbose_name = _('Item')
        verbose_name_plural = _('Items')

    barcode = models.CharField(
        max_length=100,
        verbose_name=_('barcode'),
        unique=True
    )

    name = models.CharField(
        max_length=50,
        verbose_name=_('name'),
    )

    brand = models.ForeignKey(
        Brand,
        verbose_name=_('brand'),
        on_delete=models.PROTECT,
    )

    description = models.TextField(
        blank=True,
        verbose_name=_('description'),
    )

    quantity = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        verbose_name=_('quantity'),
    )

    measure = models.ForeignKey(
        Measure,
        verbose_name=_('measure'),
        on_delete=models.PROTECT,
    )

    is_pack = models.BooleanField(
        default=False,
        verbose_name=_('is pack'),
    )

    pack_quantity = models.CharField(
        max_length=200,
        verbose_name=_('pack quantity'),
        blank=True,
        null=True,
    )

    pack_unit_items = models.ManyToManyField(
        'self',
        verbose_name=_('pack unit barcode'),
        blank=True,
    )

    lp_id = models.IntegerField(
        verbose_name=_('los precios id'),
        blank=True,
        null=True,
    )

    lp_url = models.URLField(
        verbose_name=_('los precios URL'),
        blank=True,
        null=True,
    )

    lp_product = models.CharField(
        max_length=300,
        verbose_name=_('los precios product'),
        blank=True,
        null=True,
    )

    lp_brand = models.CharField(
        max_length=200,
        verbose_name=_('los precios brand'),
        blank=True,
        null=True,
    )

    lp_size = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        verbose_name=_('los precios size'),
        blank=True,
        null=True,
    )

    lp_complement = models.TextField(
        blank=True,
        null=True,
        verbose_name=_('los precios complement'),
    )

    lp_store_id = models.IntegerField(
        verbose_name=_('los precios store id'),
        blank=True,
        null=True,
    )

    lp_store_url = models.URLField(
        verbose_name=_('los precios store URL'),
        blank=True,
        null=True,
    )

    def __str__(self):
        return '{} {}{}'.format(self.name, self.quantity, self.measure.abrev)
