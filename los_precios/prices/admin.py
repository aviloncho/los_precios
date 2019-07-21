# Django
from django.contrib import admin

# Models
from los_precios.prices.models import Store, ItemPrice


class ItemPriceInLine(admin.TabularInline):
    model = ItemPrice
    extra = 0


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    """Store Admin"""
    list_display = ('name',)
    list_display_links = ('name',)
    ordering = ('name',)
    search_fields = ('name',)

    inlines = [ItemPriceInLine, ]


@admin.register(ItemPrice)
class ItemPrice(admin.ModelAdmin):
    """ItemPrice Admin"""
    list_display = ('item', 'store', 'price')
    list_display_links = ('item',)
    ordering = ('item', 'price',)
    search_fields = ('item__name', 'store__name',)
