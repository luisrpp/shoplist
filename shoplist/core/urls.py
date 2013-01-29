from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('shoplist.core.views',
    url(r'^shoplist/$', 'shoplist', name='shoplist'),
    url(r'^shoplist/update$', 'update_shoplist', name='update_shoplist'),
    url(r'^shoplist/remove$', 'remove_shoplist', name='remove_shoplist'),
    url(r'^shoplist/(\d+)/items/$', 'shoplist_items', name='shoplist_items'),
    url(r'^shoplist/(\d+)/item/update$', 'update_list_item', name='update_list_item'),
    url(r'^shoplist/(\d+)/item/remove$', 'remove_list_item', name='remove_list_item'),
    url(r'^search_product_offers/$', 'search_product_offers', name='search_product_offers'),
)

