# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from models import ShopList


class ShopListForm(forms.ModelForm):

    class Meta:
        model = ShopList
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Digite o nome da lista…'}),
        }
        exclude = ('created_at',)

    def clean(self):
        super(ShopListForm, self).clean()

        if not self.cleaned_data.get('name'):
            raise forms.ValidationError(
                _(u'Informe o nome da lista de compras.'))

        return self.cleaned_data

