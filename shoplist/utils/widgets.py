# -*- coding: utf-8 -*-
from decimal import Decimal
from django import forms
from django.utils.translation import ugettext_lazy as _
from formatters import decimal_to_real

class RealCurrencyInput(forms.TextInput):

    def render(self, name, value, attrs=None):
        value = value or ''
        if isinstance(value, Decimal):
            value = decimal_to_real(str(value), 2)
        attrs = attrs or {}
        attrs['class'] = 'real_currency input-mini'
        attrs['alt'] = 'decimal'
        attrs['placeholder'] = _(u'Preço')
        return super(RealCurrencyInput, self).render(name, value, attrs)

