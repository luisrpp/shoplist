from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shoplist.views.home', name='home'),
    # url(r'^shoplist/', include('shoplist.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
