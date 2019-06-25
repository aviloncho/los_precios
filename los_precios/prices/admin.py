# Django
from django.contrib import admin

# Models
from los_precios.prices.models import Store

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    """Country Admin"""
    list_display = ('name',)
    list_display_links = ('name',)
    ordering = ('name',)
    search_fields = ('name',)
