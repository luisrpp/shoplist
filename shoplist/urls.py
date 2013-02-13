from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Main Page
    url(r'^$', 'shoplist.core.views.index', name='index'),
    # Home
    url(r'^home/$', 'shoplist.core.views.home', name='home'),
    # Admin
    url(r'^admin/', include(admin.site.urls)),
    # Core app
    (r'^', include('shoplist.core.urls', namespace='core')),
   # contact form
    url(r'^', include('shoplist.contact.urls', namespace='contact')),
    # django-social-auth
    url(r'', include('social_auth.urls')),
    # Logout using django.contrib.auth
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
else:
    # Defining URL mapping in the static files for environment Heroku
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.contrib.staticfiles.views.serve', {
            'document_root': settings.STATIC_ROOT,
            'insecure': True}),
    )

