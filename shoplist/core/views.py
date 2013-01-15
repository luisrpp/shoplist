# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.db.models import Count
from django.core import serializers
from models import ShopList
from forms import ShopListForm


def shoplist(request):
    """Creates a new shoplist"""

    shoplists = ShopList.objects.annotate(num_products=Count('listitem'))

    if request.method == 'POST':
        return _create_shoplist(request, shoplists)
    else:
        return _new_shoplist(request, shoplists)


def _new_shoplist(request, shoplists=None):
    form = ShopListForm()
    context = RequestContext(request, {'form': form, 'shoplists': shoplists})
    return render_to_response('core/shoplist.html', context)


def _create_shoplist(request, shoplists=None):
    form = ShopListForm(request.POST)

    if not form.is_valid():
        context = RequestContext(request, {'form': form, 'shoplists': shoplists},)
        return render_to_response('core/shoplist.html', context)

    shop_list = form.save()

    #TODO: Send to another page to create list items
    context = RequestContext(request, {'form': form, 'shoplists': shoplists},)
    return render_to_response('core/shoplist.html', context)


def update_shoplist(request):
    if request.is_ajax():
        sl = ShopList.objects.get(id=request.GET.get('id'))
        sl.name = request.GET.get('name')
        sl.save()

        data = serializers.serialize('json', [sl,])

        return HttpResponse(data, mimetype='application/json')


def remove_shoplist(request):
    if request.is_ajax():
        sl = ShopList.objects.get(id=request.GET.get('id'))
        sl.delete()

        data = serializers.serialize('json', [])

        return HttpResponse(data, mimetype='application/json')
