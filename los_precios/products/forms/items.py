from django import forms
from los_precios.products.models import Item


class ItemForm(forms.ModelForm):
    """Form definition for Item."""

    class Meta:
        """Meta definition for Iteform."""

        model = Item
        exclude = ()

    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['pack_unit_items'].queryset = Item.objects.filter(is_pack=False)
