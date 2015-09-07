from django.conf.urls import patterns, include, url
from gestion_contacto_lena import settings
from django.contrib import admin
from django.http import HttpResponseRedirect
from tastypie.api import Api
from gestion_lena.api import RegionResource, ProvinciaResource, ComunaResource, ContactoResource

v1_api = Api(api_name='v1')
v1_api.register(RegionResource())
v1_api.register(ProvinciaResource())
v1_api.register(ComunaResource())
v1_api.register(ContactoResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gestion_contacto_lena.views.home', name='home'),
    url(r'^gestion/', include('gestion_lena.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
    url(r'^$', 'gestion_lena.views.pagina', name='pagina'),
    url(r'^password_reset/', include('password_reset.urls')),
    url(r'^nosepo/$', lambda x: HttpResponseRedirect('/gestion/home/')),
	url(r'^accounts/login/$', 'gestion_lena.views.iniciar_sesion', name='login'),
	url(r'^logout/$', 'gestion_lena.views.cerrar_sesion', name='logout'),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),

)


