# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from models import (ShopList, ListItem, Product)


class ShopListForm(forms.ModelForm):

    class Meta:
        model = ShopList
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': _(u'Digite o nome da lista…')}),
        }
        exclude = ('created_at',)

    def clean(self):
        super(ShopListForm, self).clean()

        if not self.cleaned_data.get('name'):
            raise forms.ValidationError(
                _(u'Informe o nome da lista de compras.'))

        return self.cleaned_data


class ListItemForm(forms.ModelForm):
    product = forms.CharField(label=_(u"Produto"),
                            widget=forms.TextInput(attrs={'class': 'input-large', 'placeholder': _(u'Produto')}))

    class Meta:
        model = ListItem
        widgets = {
            'quantity': forms.TextInput(attrs={'class': 'input-mini', 'placeholder': _(u'Qtde')}),
            'price': forms.TextInput(attrs={'class': 'input-mini', 'placeholder': _(u'Preço')}),
        }
        exclude = ('product',)


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product

