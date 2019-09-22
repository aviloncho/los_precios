# Django
from django.contrib import admin

# Models
from los_precios.products.models import Brand, Measure, Item

# Forms
from los_precios.products.forms.items import ItemForm

# AdminInline
from los_precios.prices.admin import ItemPriceInLine


class ItemInLine(admin.TabularInline):
    model = Item
    extra = 0
    fields = (
        'barcode',
        'name',
        'brand',
        'quantity',
        'measure',
    )


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    """Brand Admin"""
    list_display = ('name',)
    list_display_links = ('name',)
    ordering = ('name',)
    search_fields = ('name',)

    inlines = [ItemInLine, ]


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
    form = ItemForm
    list_display = (
        'barcode',
        'name',
        'brand',
        'quantity',
        'measure',
        'is_pack',
        'lp_id',
        'lp_product',
        'lp_brand',
        'lp_store_id',
    )
    list_display_links = ('name',)
    list_filter = ('is_pack', 'measure',)
    ordering = ('name',)
    search_fields = ('barcode', 'name', 'brand__name')
    filter_horizontal = ('pack_unit_items',)

    inlines = [ItemPriceInLine, ]
