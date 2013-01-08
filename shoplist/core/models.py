# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name=_(u'Categoria'))

    class Meta:
        ordering = ['name']
        verbose_name = _(u'Categoria')
        verbose_name_plural = _(u'Categorias')


    def __unicode__(self):
        return self.name


class ShopList(models.Model):
    name = models.CharField(max_length=200, verbose_name=_(u'Lista'))
    category = models.ForeignKey(Category)
    date = models.DateTimeField(verbose_name=_(u'Data de criação'), auto_now_add=True)

    class Meta:
        ordering = ['name']
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
    shop_list = models.ForeignKey(ShopList)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField(verbose_name=_(u'Quantidade'))
    price = models.DecimalField(verbose_name=_(u'Preço'), max_digits=10, decimal_places=2)

    def __unicode__(self):
        return self.product.name   
