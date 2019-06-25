"""Products App"""

# Django
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ProductsConfig(AppConfig):
    """Products App config"""
    
    name = "precios.products"
    verbose_name = _("Products")
