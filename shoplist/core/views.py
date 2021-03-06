# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.db.models import Count
from django.core import serializers
from django.contrib.auth.decorators import login_required
from models import (ShopList, ListItem, Product)
from forms import (ShopListForm, ListItemForm)


def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('home'))
    else:
        context = RequestContext(request)
        return render_to_response('index.html', context)


@login_required
def home(request):
    context = RequestContext(request)
    return render_to_response('home.html', context)


@login_required
def shoplist(request):
    """Creates a new shoplist"""

    shoplists = ShopList.objects.filter(user=request.user).annotate(num_products=Count('listitem'))

    if request.method == 'POST':
        form = ShopListForm(request.POST)

        if not form.is_valid():
            #TODO form validation
            context = RequestContext(request, {'form': form, 'shoplists': shoplists},)
            return render_to_response('core/shoplist.html', context)

        shop_list = form.save(request.user)

        return HttpResponseRedirect(reverse('core:shoplist_items', args=[shop_list.pk]))
    else:
        form = ShopListForm()
        context = RequestContext(request, {'form': form, 'shoplists': shoplists})
        return render_to_response('core/shoplist.html', context)


@login_required
def update_shoplist(request):
    if request.is_ajax():
        sl = ShopList.objects.get(id=request.GET.get('id'), user=request.user)
        sl.name = request.GET.get('name')
        sl.save()

        data = serializers.serialize('json', [sl,])

        return HttpResponse(data, mimetype='application/json')


@login_required
def remove_shoplist(request):
    if request.is_ajax():
        sl = ShopList.objects.get(id=request.GET.get('id'), user=request.user)
        sl.delete()

        data = serializers.serialize('json', [])

        return HttpResponse(data, mimetype='application/json')


@login_required
def shoplist_items(request, pk):
    shop_list = get_object_or_404(ShopList, pk=pk, user=request.user)
    list_items = ListItem.objects.filter(shop_list=shop_list, user=request.user)

    if request.method == 'POST':
        form = ListItemForm(request.POST)

        if not form.is_valid():
            #TODO form validation
            context = RequestContext(request, {'form': form, 'shoplist': shop_list, 'list_items': list_items})
            return render_to_response('core/shoplist_items.html', context)

        form.save(user=request.user)

        form = ListItemForm(initial={'shop_list': shop_list.pk })
        context = RequestContext(request, {'form': form, 'shoplist': shop_list, 'list_items': list_items})
        return render_to_response('core/shoplist_items.html', context)

    else:
        form = ListItemForm(initial={'shop_list': shop_list.pk })

        context = RequestContext(request, {'form': form, 'shoplist': shop_list, 'list_items': list_items})
        return render_to_response('core/shoplist_items.html', context)


@login_required
def update_list_item(request, shoplist_id):
    if request.is_ajax():
        get_values = request.GET.copy()
        get_values['shop_list'] = str(shoplist_id)

        form = ListItemForm(get_values)

        #TODO form validation
        form.is_valid()

        item = form.save(user=request.user, commit=False)
        item.pk = request.GET['id']
        item.save()

        data = serializers.serialize('json', [])

        return HttpResponse(data, mimetype='application/json')


@login_required
def remove_list_item(request, shoplist_id):
    if request.is_ajax():
        li = ListItem.objects.get(id=request.GET.get('id'), user=request.user)
        li.delete()

        data = serializers.serialize('json', [])

        return HttpResponse(data, mimetype='application/json')


@login_required
def search_product_offers(request):
    if request.is_ajax():
        from offers.online_offers import OffersFinderFactory

        product = request.GET.get('product')
        product = product.encode("utf8")

        offers = OffersFinderFactory.get_instance(strategy="BUSCAPE")
        results = offers.find(product)

        template = 'core/offer_results.html'
        data = {
            'results': results,
        }
        context = RequestContext(request)

        return render_to_response(template, data, context)

