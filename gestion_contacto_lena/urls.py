from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gestion_contacto_lena.views.home', name='home'),
    url(r'^gestion/', include('gestion_lena.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
