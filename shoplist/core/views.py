# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response


def shoplist(request):
    context = RequestContext(request)
    return render_to_response('core/shoplist.html',
                             context)
