# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ShopList'
        db.create_table('core_shoplist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('core', ['ShopList'])

        # Adding model 'Product'
        db.create_table('core_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('core', ['Product'])

        # Adding model 'ListItem'
        db.create_table('core_listitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('shop_list', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.ShopList'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Product'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('price', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
        ))
        db.send_create_signal('core', ['ListItem'])


    def backwards(self, orm):
        # Deleting model 'ShopList'
        db.delete_table('core_shoplist')

        # Deleting model 'Product'
        db.delete_table('core_product')

        # Deleting model 'ListItem'
        db.delete_table('core_listitem')


    models = {
        'core.listitem': {
            'Meta': {'ordering': "['product']", 'object_name': 'ListItem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Product']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'shop_list': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.ShopList']"})
        },
        'core.product': {
            'Meta': {'ordering': "['name']", 'object_name': 'Product'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'core.shoplist': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'ShopList'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['core']