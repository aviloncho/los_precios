# Django
from django.contrib import admin

# Models
from los_precios.products.models import Brand, Measure, Item

# AdminInline
from los_precios.prices.admin import ItemPriceInLine

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    """Brand Admin"""
    list_display = ('name',)
    list_display_links = ('name',)
    ordering = ('name',)
    search_fields = ('name',)


@admin.register(Measure)
class MeasureAdmin(admin.ModelAdmin):
    """Measure Admin"""
    list_display = ('name', 'abrev',)
    list_display_links = ('name',)
    ordering = ('name',)
    search_fields = ('name', 'abrev')


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """Item Admin"""
    list_display = (
        'barcode',
        'name',
        'brand',
        'is_pack',
        'lp_id',
        'quantity',
    )
    list_display_links = ('name',)
    ordering = ('name',)
    search_fields = ('name', 'brand')

    inlines = [ItemPriceInLine,]
