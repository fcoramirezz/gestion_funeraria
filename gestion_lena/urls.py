from django.conf.urls import patterns, include, url
from gestion_lena.views import ContactoListView, ContactoDetailView, ContactoCreateView, ContactoUpdateView, ContactoDeleteView, GastoListView, GastoDetailView, GastoCreateView, GastoUpdateView, GastoDeleteView, TipoGastoListView, TipoGastoCreateView, TipoGastoDeleteView, TipoGastoDetailView, TipoGastoUpdateView
    
from gestion_lena.views import ServicioListView, ServicioDetailView, ServicioCreateView, ServicioUpdateView, ServicioDeleteView, PedidoListView, PedidoDetailView, PedidoCreateView, PedidoUpdateView, PedidoDeleteView, SueldoListView, SueldoDetailView, SueldoCreateView, SueldoUpdateView, SueldoDeleteView, TrabajadorListView, TrabajadorDetailView, TrabajadorCreateView, TrabajadorUpdateView, TrabajadorDeleteView
from gestion_lena.views import DudaListView, DudaDetailView, DudaCreateView, DudaUpdateView, DudaDeleteView
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from gestion_contacto_lena import settings

admin.autodiscover()
urlpatterns = patterns('gestion_lena.views',

    url(r'^home/', 'home', name='home'),
    url(r'^contactos/$', ContactoListView.as_view(), name='contacto_list'),
    url(r'^contacto/(?P<pk>\d+)/$', ContactoDetailView.as_view(), name='contacto_detail'),
    url(r'^contacto/nuevo/$', ContactoCreateView.as_view(), name='contacto_create'),
    url(r'^contacto/(?P<pk>\d+)/actualizar/$', ContactoUpdateView.as_view(), name='contacto_update'),
    url(r'^contacto/(?P<pk>\d+)/eliminar/$', ContactoDeleteView.as_view(), name='contacto_delete'),
    ################################################
    url(r'^trabajadores/$', TrabajadorListView.as_view(), name='trabajador_list'),
    url(r'^trabajador/(?P<pk>\d+)/$', TrabajadorDetailView.as_view(), name='trabajador_detail'),
    url(r'^trabajador/nuevo/$', TrabajadorCreateView.as_view(), name='trabajador_create'),
    url(r'^trabajador/(?P<pk>\d+)/actualizar/$', TrabajadorUpdateView.as_view(), name='trabajador_update'),
    url(r'^trabajador/(?P<pk>\d+)/eliminar/$', TrabajadorDeleteView.as_view(), name='trabajador_delete'),
    ##########################################################
    url(r'^servicios/$', PedidoListView.as_view(), name='pedido_list'),
    url(r'^servicios/$', PedidoListView.as_view(), name='pedido_list_segundo'),
    url(r'^servicio/(?P<pk>\d+)/$', PedidoDetailView.as_view(), name='pedido_detail'),
    url(r'^servicio/nuevo/$', PedidoCreateView.as_view(), name='pedido_create'),
    url(r'^servicio/(?P<pk>\d+)/actualizar/$', PedidoUpdateView.as_view(), name='pedido_update'),
    url(r'^servicio/(?P<pk>\d+)/eliminar/$', PedidoDeleteView.as_view(), name='pedido_delete'),
    ############SERVICIO######
    url(r'^tipo_servicios/$', ServicioListView.as_view(), name='servicio_list'),
    url(r'^tipo_servicio/(?P<pk>\d+)/$', ServicioDetailView.as_view(), name='servicio_detail'),
    url(r'^tipo_servicio/nuevo/$', ServicioCreateView.as_view(), name='servicio_create'),
    url(r'^tipo_servicio/(?P<pk>\d+)/actualizar/$', ServicioUpdateView.as_view(), name='servicio_update'),
    url(r'^tipo_servicio/(?P<pk>\d+)/eliminar/$', ServicioDeleteView.as_view(), name='servicio_delete'),
    ########################## SUELDO  #######################
    url(r'^sueldos/$', SueldoListView.as_view(), name='sueldo_list'),
    url(r'^sueldo/(?P<pk>\d+)/$', SueldoDetailView.as_view(), name='sueldo_detail'),
    url(r'^sueldo/nuevo/$', SueldoCreateView.as_view(), name='sueldo_create'),
    url(r'^sueldo/(?P<pk>\d+)/actualizar/$', SueldoUpdateView.as_view(), name='sueldo_update'),
    url(r'^sueldo/(?P<pk>\d+)/eliminar/$', SueldoDeleteView.as_view(), name='sueldo_delete'),




    url(r'^dudas/$', DudaListView.as_view(), name='duda_list'),
    url(r'^duda/(?P<pk>\d+)/$', DudaDetailView.as_view(), name='duda_detail'),
    url(r'^duda/nuevo/$', DudaCreateView.as_view(), name='duda_create'),
    url(r'^duda/(?P<pk>\d+)/actualizar/$', DudaUpdateView.as_view(), name='duda_update'),
    url(r'^duda/(?P<pk>\d+)/eliminar/$', DudaDeleteView.as_view(), name='duda_delete'),

    #########################
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
  
   ##########################################################################################
    url(r'^servicio/(?P<id_pedido>\d+)/entregado/$', 'pedido_cambiar_estado', name='pedido_cambiar_estado'),
    url(r'^contacto/(?P<id_contacto>\d+)/nuevo/pedido/$', 'contacto_nuevo_pedido', name='contacto_nuevo_pedido'),
    url(r'^contacto/(?P<id_pedido>\d+)/pedido/delete/$', 'contacto_pedido_delete', name='contacto_pedido_delete'),
    ###############################################################################################################
    url(r'^servicios/entregas/$', 'calcular_entrega_pedidos', name='calcular_entrega_pedidos'),
    url(r'^servicios/ruta/$', 'ruta_servicio', name='ruta_servicio'),
    url(r'^servicios/ruta/$', 'ruta_servicio', name='ruta_servicio'),
    url(r'^serviciosss/entregas/$', 'object_list_servicio', name='object_list_servicio'),
    url(r'^reporte/cuenta/(?P<fecha_inicial>[-\d]+)/(?P<fecha_final>[-\d]+)/$', 'cuenta_t', name='cuenta_t'),
    url(r'^reporte/filtrar/$', 'form_cuenta_t', name='form_cuenta_t'),
    url(r'^reporte/cuenta/$', 'reporte_cuenta', name='reporte_cuenta'),
    #url(r'^cont/$', 'contacto_view', name= 'vista_contacto'),



) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
