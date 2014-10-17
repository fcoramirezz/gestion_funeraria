from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponseRedirect

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gestion_contacto_lena.views.home', name='home'),
    url(r'^gestion/', include('gestion_lena.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', lambda x: HttpResponseRedirect('/gestion/home/')),
	url(r'^accounts/login/$', 'gestion_lena.views.iniciar_sesion', name='login'),
	url(r'^logout/$', 'gestion_lena.views.cerrar_sesion', name='logout'),
)


