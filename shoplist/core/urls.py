from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('shoplist.core.views',
    url(r'^shoplist$', 'shoplist', name='shoplist'),
    url(r'^shoplist/update$', 'update_shoplist', name='update_shoplist'),
    url(r'^shoplist/remove$', 'remove_shoplist', name='remove_shoplist'),
)
