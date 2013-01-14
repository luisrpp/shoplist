from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('shoplist.core.views',
    url(r'^shoplist/add$', 'shoplist', name='shoplist'),
)
