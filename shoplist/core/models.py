# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _


class ShopList(models.Model):
    name = models.CharField(max_length=200, verbose_name=_(u'Lista'))
    created_at = models.DateTimeField(verbose_name=_(u'Data de criação'), auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = _(u'Lista')
        verbose_name_plural = _(u'Listas')

    def __unicode__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name=_(u'Produto'))

    class Meta:
        ordering = ['name']
        verbose_name = _(u'Produto')
        verbose_name_plural = _(u'Produtos')

    def __unicode__(self):
        return self.name


class ListItem(models.Model):
    shop_list = models.ForeignKey(ShopList, verbose_name=_(u'Lista'))
    product = models.ForeignKey(Product, verbose_name=_(u'Produto'))
    quantity = models.IntegerField(verbose_name=_(u'Quantidade'))
    price = models.DecimalField(verbose_name=_(u'Preço'), max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Item da Lista')
        verbose_name_plural = _(u'Itens da Lista')

    def __unicode__(self):
        return self.product.name   
