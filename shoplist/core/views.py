# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from forms import ShopListForm


def shoplist(request):
    """Creates a new shoplist"""
    if request.method == 'POST':
        return _create_shoplist(request)
    else:
        return _new_shoplist(request)

def _new_shoplist(request):
    form = ShopListForm()
    context = RequestContext(request, {'form': form})
    return render_to_response('core/shoplist.html', context)

def _create_shoplist(request):
    form = ShopListForm(request.POST)

    if not form.is_valid():
        context = RequestContext(request, {'form': form})
        return render_to_response('core/shoplist.html', context)

    shop_list = form.save()

    #TODO: Send to another page to create list items
    context = RequestContext(request, {'form': form})
    return render_to_response('core/shoplist.html', context)

