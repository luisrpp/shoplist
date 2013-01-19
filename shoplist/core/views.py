# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.db.models import Count
from django.core import serializers
from models import (ShopList, ListItem, Product)
from forms import (ShopListForm, ListItemForm, ProductForm)


def shoplist(request):
    """Creates a new shoplist"""

    shoplists = ShopList.objects.annotate(num_products=Count('listitem'))

    if request.method == 'POST':
        form = ShopListForm(request.POST)

        if not form.is_valid():
            context = RequestContext(request, {'form': form, 'shoplists': shoplists},)
            return render_to_response('core/shoplist.html', context)

        shop_list = form.save()

        return HttpResponseRedirect(reverse('core:shoplist_items', args=[shop_list.pk]))
    else:
        form = ShopListForm()
        context = RequestContext(request, {'form': form, 'shoplists': shoplists})
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


def shoplist_items(request, pk):
    shop_list = get_object_or_404(ShopList, pk=pk)
    list_items = ListItem.objects.filter(shop_list=shop_list)

    if request.method == 'POST':
        form_p = ProductForm({ 'name': request.POST['product'] })

        if not form_p.is_valid():
            form = ListItemForm(request.POST)
            context = RequestContext(request, {'form': form, 'shoplist': shop_list, 'list_items': list_items})
            return render_to_response('core/shoplist_items.html', context)

        p, product_created = Product.objects.get_or_create(name=request.POST['product'])

        post_values = request.POST.copy()
        post_values['product'] = str(p.pk)

        form = ListItemForm(post_values)

        if not form.is_valid():
            form = ListItemForm(request.POST)
            
            if product_created:
                p.delete()

            context = RequestContext(request, {'form': form, 'shoplist': shop_list, 'list_items': list_items})
            return render_to_response('core/shoplist_items.html', context)

        item = form.save(commit=False)
        item.product = p
        item.save()

        form = ListItemForm(initial={'shop_list': shop_list.pk })
        context = RequestContext(request, {'form': form, 'shoplist': shop_list, 'list_items': list_items})
        return render_to_response('core/shoplist_items.html', context)

    else:
        form = ListItemForm(initial={'shop_list': shop_list.pk })

        context = RequestContext(request, {'form': form, 'shoplist': shop_list, 'list_items': list_items})
        return render_to_response('core/shoplist_items.html', context)
