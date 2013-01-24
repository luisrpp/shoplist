# -*- coding: utf-8 -*-
from django import forms
from widgets import RealCurrencyInput
from django.utils.translation import ugettext_lazy as _


class RealCurrencyField(forms.DecimalField):
    widget = RealCurrencyInput

    def clean(self, value):
        if value:
            value = value.replace('.', '').replace(',','.')
        return super(RealCurrencyField, self).clean(value)

    def widget_attrs(self, widget):
        return {'class':'real_currency input-mini', 'placeholder': _(u'Preço')}

