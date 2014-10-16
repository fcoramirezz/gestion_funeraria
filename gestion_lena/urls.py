from django.conf.urls import patterns, include, url
from gestion_lena.views import ContactoListView, ContactoDetailView, ContactoCreateView, ContactoUpdateView, ContactoDeleteView
from gestion_lena.views import PedidoListView, PedidoDetailView, PedidoCreateView, PedidoUpdateView, PedidoDeleteView


urlpatterns = patterns('gestion_lena.views',
    url(r'^home/', 'home', name='home'),
    url(r'^contactos/$', ContactoListView.as_view(), name='contacto_list'),
    url(r'^contacto/(?P<pk>\d+)/$', ContactoDetailView.as_view(), name='contacto_detail'),
    url(r'^contacto/nuevo/$', ContactoCreateView.as_view(), name='contacto_create'),
    url(r'^contacto/(?P<pk>\d+)/actualizar/$', ContactoUpdateView.as_view(), name='contacto_update'),
    url(r'^contacto/(?P<pk>\d+)/eliminar/$', ContactoDeleteView.as_view(), name='contacto_delete'),
    url(r'^pedidos/$', PedidoListView.as_view(), name='pedido_list'),
    url(r'^pedido/(?P<pk>\d+)/$', PedidoDetailView.as_view(), name='pedido_detail'),
    url(r'^pedido/nuevo/$', PedidoCreateView.as_view(), name='pedido_create'),
    url(r'^pedido/(?P<pk>\d+)/actualizar/$', PedidoUpdateView.as_view(), name='pedido_update'),
    url(r'^pedido/(?P<pk>\d+)/eliminar/$', PedidoDeleteView.as_view(), name='pedido_delete'),
)
