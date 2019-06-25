"""Prices App"""

# Django
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PricesConfig(AppConfig):
    """Prices App config"""
    
    name = "los_precios.prices"
    verbose_name = _("Prices")
