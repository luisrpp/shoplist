from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('shoplist.contact.views',
    url(r'^contact/$', 'contact', name='contact'),
)

