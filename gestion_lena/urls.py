from django.conf.urls import patterns, include, url
from gestion_lena.views import ContactoListView, ContactoDetailView, ContactoCreateView, ContactoUpdateView, ContactoDeleteView, \
    GastoListView, GastoDetailView, GastoCreateView, GastoUpdateView, GastoDeleteView, TipoGastoListView, TipoGastoCreateView, TipoGastoDeleteView, TipoGastoDetailView, TipoGastoUpdateView, \
    HuellaCarbonoListView, HuellaCarbonoDetailView, HuellaCarbonoDeleteView
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
    url(r'^gastos/$', GastoListView.as_view(), name='gasto_list'),
    url(r'^gasto/(?P<pk>\d+)/$', GastoDetailView.as_view(), name='gasto_detail'),
    url(r'^gasto/nuevo/$', GastoCreateView.as_view(), name='gasto_create'),
    url(r'^gasto/(?P<pk>\d+)/actualizar/$', GastoUpdateView.as_view(), name='gasto_update'),
    url(r'^gasto/(?P<pk>\d+)/eliminar/$', GastoDeleteView.as_view(), name='gasto_delete'),
    url(r'^tipo_gastos/$', TipoGastoListView.as_view(), name='tipo_gasto_list'),
    url(r'^tipo_gasto/(?P<pk>\d+)/$', TipoGastoDetailView.as_view(), name='tipo_gasto_detail'),
    url(r'^tipo_gasto/nuevo/$', TipoGastoCreateView.as_view(), name='tipo_gasto_create'),
    url(r'^tipo_gasto/(?P<pk>\d+)/actualizar/$', TipoGastoUpdateView.as_view(), name='tipo_gasto_update'),
    url(r'^tipo_gasto/(?P<pk>\d+)/eliminar/$', TipoGastoDeleteView.as_view(), name='tipo_gasto_delete'),
    #####################################################################################################
    url(r'^huella/$', HuellaCarbonoListView.as_view(), name='huella_carbono_list'),
    url(r'^huella/(?P<pk>\d+)/$', HuellaCarbonoDetailView.as_view(), name='huella_carbono_detail'),
    url(r'^huella/(?P<pk>\d+)/eliminar/$', HuellaCarbonoDeleteView.as_view(), name='huella_carbono_delete'),
    ##########################################################################################
    url(r'^pedido/(?P<id_pedido>\d+)/entregado/$', 'pedido_cambiar_estado', name='pedido_cambiar_estado'),
    url(r'^contacto/(?P<id_contacto>\d+)/nuevo/pedido/$', 'contacto_nuevo_pedido', name='contacto_nuevo_pedido'),
    url(r'^contacto/(?P<id_pedido>\d+)/pedido/delete/$', 'contacto_pedido_delete', name='contacto_pedido_delete'),
    ###############################################################################################################
    url(r'^pedidos/entregas/$', 'calcular_entrega_pedidos', name='calcular_entrega_pedidos'),
    url(r'^reporte/cuenta/(?P<fecha_inicial>[-\d]+)/(?P<fecha_final>[-\d]+)/$', 'cuenta_t', name='cuenta_t'),
    url(r'^reporte/filtrar/$', 'form_cuenta_t', name='form_cuenta_t'),
    url(r'^reporte/cuenta/$', 'reporte_cuenta', name='reporte_cuenta'),
)
