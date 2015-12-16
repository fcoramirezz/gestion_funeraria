# coding: utf-8
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from datetime import datetime, date, time, timedelta
import calendar

from django.core.mail import send_mail, BadHeaderError
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse, HttpResponseRedirect
from gestion_lena.forms import ContactForm




from django.shortcuts import render_to_response
from django.template import RequestContext



from gestion_lena.models import Servicio, Contacto, Pedido, Configuracion, Region, Provincia, Comuna, Gasto, TipoGasto, Servicio, Sueldo, Trabajador, Duda
    
from gestion_lena.mixins import LoginRequired, SearchableListMixin
from gestion_lena.forms import ServicioForm, ContactoForm, PedidoForm, PedidoContactoForm, GastoForm, TipoGastoForm, RangoFechaForm, ServicioForm, SueldoForm, TrabajadorForm, DudaForm
   

from gestion_lena.models import Cuenta

import datetime

CONF, created = Configuracion.objects.get_or_create(id=1)
if created:
    CONF.titulo_pagina = "Gestión"
    CONF.footer = "Francisco Ramirez Cerda &copy; Todos los derechos reservados"
    CONF.save()

@login_required
def home(request):
    pedidos = Pedido.objects.exclude(estado="Entregado").order_by('creado_en')[:4]
    return render(request, 'gestion_lena/base.html', {'pedidos': pedidos})





@login_required
def object_list_servicio(request):
    context = {}
    pedidos = Pedido.objects.filter(estado="No Pagado").order_by('creado_en')
    context['pedidos'] = pedidos
    return render(request, 'gestion_lena/object_list_servicio.html', context)

@login_required
def pedido_list_segundo(request):
    context = {}
    pedidos = Pedido.objects.filter(estado="No Pagado").order_by('creado_en')
    context['pedidos'] = pedidos
    return render(request, 'gestion_lena/pedido_list_segundo.html', context)







   

##########CONTACTO###################################
class ContactoListView(LoginRequired, SearchableListMixin, ListView):
    model = Contacto
    template_name = 'gestion_lena/contacto_list.html'
    search_fields = [('nombre','icontains',), ('apellido','icontains',)]
    
class ContactoDetailView(LoginRequired, SearchableListMixin, DetailView):
    model = Contacto
    template_name = 'gestion_lena/contacto_detail.html'
    search_fields = [('nombre','icontains',), ('apellido','icontains',)]

    def get_context_data(self, **kwargs):
        context = super(ContactoDetailView, self).get_context_data(**kwargs)
        context['regiones'] = Region.objects.all()
        context['provincias'] = Provincia.objects.all()
        context['comunas'] = Comuna.objects.all()
        context['servicios'] = Servicio.objects.all()
        return context

class ContactoCreateView(LoginRequired, SearchableListMixin, CreateView):
    model = Contacto
    form_class = ContactoForm
    template_name = 'gestion_lena/contacto_create.html'
    search_fields = [('nombre','icontains',), ('apellido','icontains',)]

class ContactoUpdateView(LoginRequired, SearchableListMixin, UpdateView):
    model = Contacto
    form_class = ContactoForm
    template_name = 'gestion_lena/contacto_update.html'
    search_fields = [('nombre','icontains',), ('apellido','icontains',)]

class ContactoDeleteView(LoginRequired, SearchableListMixin, DeleteView):
    model = Contacto
    success_url = reverse_lazy('contacto_list')
    template_name = 'gestion_lena/contacto_delete.html'
    search_fields = [('nombre','icontains',), ('apellido','icontains',)]

 ########### TRABAJADOR ###################################################   
class TrabajadorListView(LoginRequired, SearchableListMixin, ListView):
    model = Trabajador
    template_name = 'gestion_lena/trabajador_list.html'
    search_fields = [('nombre','icontains',), ('apellido','icontains',)]
    
class TrabajadorDetailView(LoginRequired, SearchableListMixin, DetailView):
    model = Trabajador
    template_name = 'gestion_lena/trabajador_detail.html'
    search_fields = [('nombre','icontains',), ('apellido','icontains',)]

class TrabajadorCreateView(LoginRequired, SearchableListMixin, CreateView):
    model = Trabajador
    form_class = TrabajadorForm
    template_name = 'gestion_lena/trabajador_create.html'
    search_fields = [('nombre','icontains',), ('apellido','icontains',)]

class TrabajadorUpdateView(LoginRequired, SearchableListMixin, UpdateView):
    model = Trabajador
    form_class = TrabajadorForm
    template_name = 'gestion_lena/trabajador_update.html'
    search_fields = [('nombre','icontains',), ('apellido','icontains',)]

class TrabajadorDeleteView(LoginRequired, SearchableListMixin, DeleteView):
    model = Trabajador
    success_url = reverse_lazy('trabajador_list')
    template_name = 'gestion_lena/trabajador_delete.html'
    search_fields = [('nombre','icontains',), ('apellido','icontains',)]
###########PEDIDO###################################################

class PedidoListView(LoginRequired, SearchableListMixin, ListView):
    model = Pedido
    template_name = 'gestion_lena/pedido_list.html'
    search_fields = [('contacto__nombre','icontains',), ('contacto__apellido','icontains',)]

class PedidoListView(LoginRequired, SearchableListMixin, ListView):
    model = Pedido
    template_name = 'gestion_lena/pedido_list_segundo.html'
    search_fields = [('contacto__nombre','icontains',), ('contacto__apellido','icontains',)]
    
class PedidoDetailView(LoginRequired, SearchableListMixin, DetailView):
    model = Pedido
    template_name = 'gestion_lena/pedido_detail.html'
    search_fields = [('contacto__nombre','icontains',), ('contacto__apellido','icontains',)]

class PedidoCreateView(LoginRequired, SearchableListMixin, CreateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'gestion_lena/pedido_create.html'
    search_fields = [('contacto__nombre','icontains',), ('contacto__apellido','icontains',)]

class PedidoUpdateView(LoginRequired, SearchableListMixin, UpdateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'gestion_lena/pedido_update.html'
    search_fields = [('contacto__nombre','icontains',), ('contacto__apellido','icontains',)]

    def get_success_url(self):
        n =  self.request.GET.get('next', None)
        if n:
            return reverse(n, kwargs={'pk': self.object.contacto.id})
        return self.object.get_absolute_url()

class PedidoDeleteView(LoginRequired, SearchableListMixin, DeleteView):
    model = Pedido
    success_url = reverse_lazy('pedido_list')
    template_name = 'gestion_lena/pedido_delete.html'
    search_fields = [('contacto__nombre','icontains',), ('contacto__apellido','icontains',)]


#########################SERVICIO ########################################
class ServicioListView(LoginRequired, SearchableListMixin, ListView):
    model = Servicio
    template_name = 'gestion_lena/servicio_list.html'
    search_fields = [('nombre','icontains',)]

class ServicioDetailView(LoginRequired, SearchableListMixin, DetailView):
    model = Servicio
    template_name = 'gestion_lena/servicio_detail.html'
    search_fields = [('nombre','icontains',)]

class ServicioCreateView(LoginRequired, SearchableListMixin, CreateView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'gestion_lena/servicio_create.html'
    search_fields = [('nombre','icontains',)]

class ServicioUpdateView(LoginRequired, SearchableListMixin, UpdateView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'gestion_lena/servicio_update.html'
    search_fields = [('nombre','icontains',)]

class ServicioDeleteView(LoginRequired, SearchableListMixin, DeleteView):
    model = Servicio
    success_url = reverse_lazy('servicio_list')
    template_name = 'gestion_lena/servicio_delete.html'
    search_fields = [('nombre','icontains',)]





class DudaListView(LoginRequired, SearchableListMixin, ListView):
    model = Duda
    template_name = 'gestion_lena/duda_list.html'
    search_fields = [('titulo','icontains',)]

class DudaDetailView(LoginRequired, SearchableListMixin, DetailView):
    model = Duda
    template_name = 'gestion_lena/duda_detail.html'
    search_fields = [('titulo','icontains',)]

class DudaCreateView(LoginRequired, SearchableListMixin, CreateView):
    model = Duda
    form_class = DudaForm
    template_name = 'gestion_lena/duda_create.html'
    search_fields = [('titulo','icontains',)]

class DudaUpdateView(LoginRequired, SearchableListMixin, UpdateView):
    model = Duda
    form_class = DudaForm
    template_name = 'gestion_lena/duda_update.html'
    search_fields = [('titulo','icontains',)]

class DudaDeleteView(LoginRequired, SearchableListMixin, DeleteView):
    model = Duda
    success_url = reverse_lazy('duda_list')
    template_name = 'gestion_lena/duda_delete.html'
    search_fields = [('titulo','icontains',)]

###########Gasto###################################################
class GastoListView(LoginRequired, SearchableListMixin, ListView):
    model = Gasto
    template_name = 'gestion_lena/gasto_list.html'
    search_fields = [('tipo_gasto__nombre','icontains',)]

class GastoDetailView(LoginRequired, SearchableListMixin, DetailView):
    model = Gasto
    template_name = 'gestion_lena/gasto_detail.html'
    search_fields = [('tipo_gasto__nombre','icontains',)]

class GastoCreateView(LoginRequired, SearchableListMixin, CreateView):
    model = Gasto
    form_class = GastoForm
    template_name = 'gestion_lena/gasto_create.html'
    search_fields = [('tipo_gasto__nombre','icontains',)]

class GastoUpdateView(LoginRequired, SearchableListMixin, UpdateView):
    model = Gasto
    form_class = GastoForm
    template_name = 'gestion_lena/gasto_update.html'
    search_fields = [('tipo_gasto__nombre','icontains',)]

class GastoDeleteView(LoginRequired, SearchableListMixin, DeleteView):
    model = Gasto
    success_url = reverse_lazy('gasto_list')
    template_name = 'gestion_lena/gasto_delete.html'
    search_fields = [('tipo_gasto__nombre','icontains',)]


################################################################################




###########   SUELDO   ###################################################

class SueldoListView(LoginRequired, SearchableListMixin, ListView):
   model = Sueldo
   template_name = 'gestion_lena/sueldo_list.html'
   search_fields = [('trabajador__nombre','icontains',)]

class SueldoDetailView(LoginRequired, SearchableListMixin, DetailView):
    model = Sueldo
    template_name = 'gestion_lena/sueldo_detail.html'
    search_fields = [('trabajador__nombre','icontains',)]

class SueldoCreateView(LoginRequired, SearchableListMixin, CreateView):
    model = Sueldo
    form_class = SueldoForm
    template_name = 'gestion_lena/sueldo_create.html'
    search_fields = [('trabajador__nombre','icontains',)]

class SueldoUpdateView(LoginRequired, SearchableListMixin, UpdateView):
    model = Sueldo
    form_class = SueldoForm
    template_name = 'gestion_lena/sueldo_update.html'
    search_fields = [('trabajador__nombre','icontains',)]

class SueldoDeleteView(LoginRequired, SearchableListMixin, DeleteView):
    model = Sueldo
    success_url = reverse_lazy('sueldo_list')
    template_name = 'gestion_lena/sueldo_delete.html'
    search_fields = [('trabajador__nombre','icontains',)]

###########Tipo Gasto###################################################
class TipoGastoListView(LoginRequired, SearchableListMixin, ListView):
    model = TipoGasto
    template_name = 'gestion_lena/tipo_gasto_list.html'
    search_fields = [('nombre','icontains',)]

class TipoGastoDetailView(LoginRequired, SearchableListMixin, DetailView):
    model = TipoGasto
    template_name = 'gestion_lena/tipo_gasto_detail.html'
    search_fields = [('nombre','icontains',)]

class TipoGastoCreateView(LoginRequired, SearchableListMixin, CreateView):
    model = TipoGasto
    form_class = TipoGastoForm
    template_name = 'gestion_lena/tipo_gasto_create.html'
    search_fields = [('nombre','icontains',)]

class TipoGastoUpdateView(LoginRequired, SearchableListMixin, UpdateView):
    model = TipoGasto
    form_class = TipoGastoForm
    template_name = 'gestion_lena/tipo_gasto_update.html'
    search_fields = [('nombre','icontains',)]

class TipoGastoDeleteView(LoginRequired, SearchableListMixin, DeleteView):
    model = TipoGasto
    success_url = reverse_lazy('tipo_gasto_list')
    template_name = 'gestion_lena/tipo_gasto_delete.html'
    search_fields = [('nombre','icontains',)]

################################################################################


###########Huellas de Carbono###################################################


################################################################################


@login_required
def pedido_cambiar_estado(request, id_pedido):
    next = request.GET.get('next', None)
    if not next:
        next = "/gestion/home/"
    pedido = get_object_or_404(Pedido, id=id_pedido)
    if pedido.estado == "Pagado":
        return redirect(next)
    pedido.estado = "Pagado"
    pedido.fecha_entrega = datetime.datetime.now()
    pedido.save()
    return redirect(next)

@login_required
def contacto_nuevo_pedido(request, id_contacto):
    contacto = get_object_or_404(Contacto, id=id_contacto)
    if request.method == "POST":
        form = PedidoContactoForm(request.POST)
        print form
        if form.is_valid():
            cantidad = form.cleaned_data.get('cantidad', None)
            direccion_destino = form.cleaned_data.get('direccion_destino', None)
            estado = form.cleaned_data.get('estado', None)
            region = form.cleaned_data.get('region', None)
            provincia = form.cleaned_data.get('provincia', None)
            comuna = form.cleaned_data.get('comuna', None)
            valor_unitario = form.cleaned_data.get('valor_unitario', None)
            Pedido.objects.create(contacto=contacto, cantidad=cantidad,
                direccion_destino=direccion_destino, estado=estado,
                valor_unitario=valor_unitario, region=region, provincia=provincia,
                comuna=comuna)
    return redirect('contacto_detail', contacto.id)

@login_required
def contacto_pedido_delete(request, id_pedido):
    pedido = get_object_or_404(Pedido, id=id_pedido)
    contacto = pedido.contacto
    pedido.delete()
    return redirect('contacto_detail', contacto.id)

#############################################################################

@login_required
def calcular_entrega_pedidos(request):
    context = {}
    pedidos = Pedido.objects.filter(estado="No Pagado").order_by('creado_en')
    
    context['pedidos'] = pedidos
    return render(request, 'gestion_lena/calcular_entrega_pedidos.html', context)

#############################################################################


@login_required
def ruta_servicio(request):
    return render(request, 'gestion_lena/ruta_servicio.html', context)


def pagina(request):
    info_enviado = False
    nombre = ""
    telefono = ""
    email = ""
    consulta = ""

    if request.method == "POST":
        formulario = ContactForm(request.POST)
        if formulario.is_valid():
            info_enviado = True
            nombre = formulario.cleaned_data['Nombre']
            telefono = formulario.cleaned_data['Telefono']
            email = formulario.cleaned_data['Email']
            consulta = formulario.cleaned_data['Consulta']

            to_admin ='fcoramirezz@gmail.com'
            html_content = "<strong>Hola Don Marcelo, usted tiene la siguiente consulta de su pagina web: </strong><br><br>"+(consulta)+"<br><br> <strong>Nombre: </strong>"+(nombre)+"<br><br><strong>Telefono: </strong>"+str(telefono)+"<br><br><strong>Email: </strong>"+(email)
            msg = EmailMultiAlternatives('Correo de Contacto', html_content, 'from@server.com',[to_admin])
            msg.attach_alternative(html_content,'text/html')
            msg.send()

    else:
        formulario = ContactForm()
    context = {'form': formulario, 'nombre': nombre, 'telefono': telefono, 'email': email, 'consulta': consulta,'info_enviado': info_enviado}
    tipo_de_servicio = Servicio.objects.filter(publicar="Si").order_by('precio_de_venta')
    context['servicios'] = tipo_de_servicio
    dudas = Duda.objects.order_by('creado_en')
    context['dudas'] = dudas
    
    
    return render_to_response('gestion_lena/pagina.html',context,context_instance=RequestContext(request))


    

@login_required
def reporte_cuenta(request):
    context = {}
    cuentas = Cuenta.objects.order_by('fecha')
    context['cuentas'] = cuentas
    total = 0
    if cuentas.count() > 0:
        total = cuentas.last().saldo
    context['total'] = total
    return render(request, 'gestion_lena/reporte_cuenta.html', context)

@login_required
def form_cuenta_t(request):
    hoy = date.today()
    context = {}
    if request.method == "POST":
        form = RangoFechaForm(request.POST)
        if form.is_valid():
            d_i = form.cleaned_data['fecha_inicial']
            d_f = form.cleaned_data['fecha_final']
            if d_i <= d_f and d_i <= hoy :
                return redirect('cuenta_t', d_i, d_f)
            else:
                messages.add_message(request, messages.ERROR, u"Fecha Inicial debe ser menor a hoy y menor a la Fecha Final")
    else:
        form = RangoFechaForm()
    context['form'] = form
    return render(request, 'gestion_lena/form_cuenta_t.html', context)

@login_required
def cuenta_t(request, fecha_inicial, fecha_final):
    
    f_i = datetime.datetime.strptime(fecha_inicial, "%Y-%m-%d").date()
    f_f = datetime.datetime.strptime(fecha_final, "%Y-%m-%d").date()
    cuentas = Cuenta.objects.filter(fecha__gte=f_i, fecha__lte=f_f).order_by('fecha')
    sueldos = Sueldo.objects.filter(fecha__gte=f_i, fecha__lte=f_f).order_by('fecha')
    gastos = Gasto.objects.filter(fecha__gte=f_i, fecha__lte=f_f).order_by('fecha')
    pedidos = Pedido.objects.filter(fecha_entrega__gte=f_i, fecha_entrega__lte=f_f, estado= 'Pagado').order_by('fecha_entrega')
  
    total_sueldos = 0
    total_gastos = 0
    total_ingresos = 0

    
    cant_ped_chillan = 0

    for n in pedidos: 
        if str(n.comuna) == 'Chillán':
            cant_ped_chillan = cant_ped_chillan + 1



    cant_ped_chillan_viejo = 0

    for n in pedidos: 
        if str(n.comuna) == 'Chillán Viejo':
            cant_ped_chillan_viejo = cant_ped_chillan_viejo+ 1



    cant_ped_cobquecura = 0

    for n in pedidos: 
        if str(n.comuna) == 'Cobquecura':
            cant_ped_cobquecura = cant_ped_cobquecura+ 1


    cant_ped_coelemu = 0

    for n in pedidos: 
        if str(n.comuna) == 'Coelemu':
            cant_ped_coelemu = cant_ped_coelemu+ 1


    cant_ped_coihueco = 0

    for n in pedidos: 
        if str(n.comuna) == 'Coihueco':
            cant_ped_coihueco = cant_ped_coihueco+ 1

    cant_ped_elcarmen = 0

    for n in pedidos: 
        if str(n.comuna) == 'El Carmen':
            cant_ped_elcarmen = cant_ped_elcarmen+ 1



    cant_ped_ninhue = 0

    for n in pedidos: 
        if str(n.comuna) == 'Ninhue':
            cant_ped_ninhue = cant_ped_ninhue+ 1


    cant_ped_niquen = 0

    for n in pedidos: 
        if str(n.comuna) == 'Ñiquen':
            cant_ped_niquen = cant_ped_niquen+ 1



    cant_ped_pemuco = 0

    for n in pedidos: 
        if str(n.comuna) == 'Pemuco':
            cant_ped_pemuco = cant_ped_pemuco+ 1


    cant_ped_pinto = 0

    for n in pedidos: 
        if str(n.comuna) == 'Pinto':
            cant_ped_pinto = cant_ped_pinto+ 1


    cant_ped_portezuelo = 0

    for n in pedidos: 
        if str(n.comuna) == 'Portezuelo':
            cant_ped_portezuelo = cant_ped_portezuelo+ 1


    cant_ped_quillon = 0

    for n in pedidos: 
        if str(n.comuna) == 'Quillón':
            cant_ped_quillon = cant_ped_quillon+ 1


    cant_ped_quirihue = 0

    for n in pedidos: 
        if str(n.comuna) == 'Quirihue':
            cant_ped_quirihue = cant_ped_quirihue+ 1


    cant_ped_ranquil = 0

    for n in pedidos: 
        if str(n.comuna) == 'Ránquil':
            cant_ped_ranquil = cant_ped_ranquil+ 1


    cant_ped_sancarlos = 0

    for n in pedidos: 
        if str(n.comuna) == 'San Carlos':
            cant_ped_sancarlos = cant_ped_sancarlos+ 1


    cant_ped_sanfabian = 0

    for n in pedidos: 
        if str(n.comuna) == 'San Fabián':
            cant_ped_sanfabian = cant_ped_sanfabian+ 1


    cant_ped_sanignacio = 0

    for n in pedidos: 
        if str(n.comuna) == 'San Ignacio':
            cant_ped_sanignacio = cant_ped_sanignacio+ 1


    cant_ped_sannicolas = 0

    for n in pedidos: 
        if str(n.comuna) == 'San Nicolás':
            cant_ped_sannicolas = cant_ped_sannicolas+ 1


    cant_ped_treguaco = 0

    for n in pedidos: 
        if str(n.comuna) == 'Treguaco':
            cant_ped_treguaco = cant_ped_treguaco+ 1






        


    for n in pedidos:
        total_ingresos= total_ingresos + n.total

    for i in sueldos:
        total_sueldos = total_sueldos + i.cantidad

    total = 0

    for c in gastos:
        total_gastos = total_gastos + c.valor

    total_egresos= total_sueldos + total_gastos

############################### INGRESOS #################################################################

    total_ingreso_enero = 0
    for n in pedidos:
        if (n.fecha_entrega.month == 1) and (n.fecha_entrega.year == f_i.year):
            total_ingreso_enero = n.total + total_ingreso_enero

    total_ingreso_febrero = 0
    for n in pedidos:
        if (n.fecha_entrega.month == 2) and (n.fecha_entrega.year == f_i.year):
            total_ingreso_febrero = n.total + total_ingreso_febrero

    total_ingreso_marzo = 0
    for n in pedidos:
        if (n.fecha_entrega.month == 3) and (n.fecha_entrega.year == f_i.year):
            total_ingreso_marzo = n.total + total_ingreso_marzo

    total_ingreso_abril = 0
    for n in pedidos:
        if (n.fecha_entrega.month == 4) and (n.fecha_entrega.year == f_i.year):
            total_ingreso_abril = n.total + total_ingreso_abril

    total_ingreso_mayo = 0
    for n in pedidos:
        if (n.fecha_entrega.month == 5) and (n.fecha_entrega.year == f_i.year):
            total_ingreso_mayo = n.total + total_ingreso_mayo

    total_ingreso_junio = 0
    for n in pedidos:
        if (n.fecha_entrega.month == 6) and (n.fecha_entrega.year == f_i.year):
            total_ingreso_junio = n.total + total_ingreso_junio

    total_ingreso_julio = 0
    for n in pedidos:
        if (n.fecha_entrega.month == 7) and (n.fecha_entrega.year == f_i.year):
            total_ingreso_julio = n.total + total_ingreso_julio

    total_ingreso_agosto = 0
    for n in pedidos:
        if (n.fecha_entrega.month == 8) and (n.fecha_entrega.year == f_i.year):
            total_ingreso_agosto = n.total + total_ingreso_agosto

    total_ingreso_septiembre = 0
    for n in pedidos:
        if (n.fecha_entrega.month == 9) and (n.fecha_entrega.year == f_i.year):
            total_ingreso_septiembre = n.total + total_ingreso_septiembre

    total_ingreso_octubre = 0
    for n in pedidos:
        if (n.fecha_entrega.month == 10) and (n.fecha_entrega.year == f_i.year):
            total_ingreso_octubre = n.total + total_ingreso_octubre

    total_ingreso_noviembre = 0
    for n in pedidos:
        if (n.fecha_entrega.month == 11) and (n.fecha_entrega.year == f_i.year):
            total_ingreso_noviembre = n.total + total_ingreso_noviembre

    total_ingreso_diciembre = 0
    for n in pedidos:
        if (n.fecha_entrega.month == 12) and (n.fecha_entrega.year == f_i.year):
            total_ingreso_diciembre = n.total + total_ingreso_diciembre
############################### EGRESOS #################################################################
    total_egresos_enero = 0
    for n in sueldos:
        if (n.fecha.month == 1) and (n.fecha.year == f_i.year):
            total_egresos_enero = n.cantidad + total_egresos_enero
    for n in gastos:
        if (n.fecha.month == 1) and (n.fecha.year == f_i.year):
            total_egresos_enero = n.valor + total_egresos_enero

    total_egresos_febrero = 0
    for n in sueldos:
        if (n.fecha.month == 2) and (n.fecha.year == f_i.year):
            total_egresos_febrero = n.cantidad + total_egresos_febrero
    for n in gastos:
        if (n.fecha.month == 2) and (n.fecha.year == f_i.year):
            total_egresos_febrero = n.valor + total_egresos_febrero

    total_egresos_marzo = 0
    for n in sueldos:
        if (n.fecha.month == 3) and (n.fecha.year == f_i.year):
            total_egresos_marzo = n.cantidad + total_egresos_marzo
    for n in gastos:
        if (n.fecha.month == 3) and (n.fecha.year == f_i.year):
            total_egresos_marzo = n.valor + total_egresos_marzo

    total_egresos_abril = 0
    for n in sueldos:
        if (n.fecha.month == 4) and (n.fecha.year == f_i.year):
            total_egresos_abril = n.cantidad + total_egresos_abril
    for n in gastos:
        if (n.fecha.month == 4) and (n.fecha.year == f_i.year):
            total_egresos_abril = n.valor + total_egresos_abril

    total_egresos_mayo = 0
    for n in sueldos:
        if (n.fecha.month == 5) and (n.fecha.year == f_i.year):
            total_egresos_mayo = n.cantidad + total_egresos_mayo
    for n in gastos:
        if (n.fecha.month == 5) and (n.fecha.year == f_i.year):
            total_egresos_mayo = n.valor + total_egresos_mayo

    total_egresos_junio = 0
    for n in sueldos:
        if (n.fecha.month == 6) and (n.fecha.year == f_i.year):
            total_egresos_junio = n.cantidad + total_egresos_junio
    for n in gastos:
        if (n.fecha.month == 6) and (n.fecha.year == f_i.year):
            total_egresos_junio = n.valor + total_egresos_junio

    total_egresos_julio = 0
    for n in sueldos:
        if (n.fecha.month == 7) and (n.fecha.year == f_i.year):
            total_egresos_julio = n.cantidad + total_egresos_julio
    for n in gastos:
        if (n.fecha.month == 7) and (n.fecha.year == f_i.year):
            total_egresos_julio = n.valor + total_egresos_julio


    total_egresos_agosto = 0
    for n in sueldos:
        if (n.fecha.month == 8) and (n.fecha.year == f_i.year):
            total_egresos_agosto = n.cantidad + total_egresos_agosto
    for n in gastos:
        if (n.fecha.month == 8) and (n.fecha.year == f_i.year):
            total_egresos_agosto = n.valor + total_egresos_agosto

    total_egresos_septiembre = 0
    for n in sueldos:
        if (n.fecha.month == 9) and (n.fecha.year == f_i.year):
            total_egresos_septiembre = n.cantidad + total_egresos_septiembre
    for n in gastos:
        if (n.fecha.month == 9) and (n.fecha.year == f_i.year):
            total_egresos_septiembre = n.valor + total_egresos_septiembre

    total_egresos_octubre = 0
    for n in sueldos:
        if (n.fecha.month == 10) and (n.fecha.year == f_i.year):
            total_egresos_octubre = n.cantidad + total_egresos_octubre
    for n in gastos:
        if (n.fecha.month == 10) and (n.fecha.year == f_i.year):
            total_egresos_octubre = n.valor + total_egresos_octubre

    total_egresos_noviembre = 0
    for n in sueldos:
        if (n.fecha.month == 11) and (n.fecha.year == f_i.year):
            total_egresos_noviembre = n.cantidad + total_egresos_noviembre
    for n in gastos:
        if (n.fecha.month == 11) and (n.fecha.year == f_i.year):
            total_egresos_noviembre = n.valor + total_egresos_noviembre

    total_egresos_diciembre = 0
    for n in sueldos:
        if (n.fecha.month == 12) and (n.fecha.year == f_i.year):
            total_egresos_diciembre = n.cantidad + total_egresos_diciembre
    for n in gastos:
        if (n.fecha.month == 12) and (n.fecha.year == f_i.year):
            total_egresos_diciembre = n.valor + total_egresos_diciembre




    total = total_ingresos - total_egresos     
    if cuentas.count() > 0:
        total = cuentas.last().saldo
    return render(request, 'gestion_lena/cuenta_t.html', {'cant_ped_treguaco':cant_ped_treguaco,'cant_ped_sannicolas':cant_ped_sannicolas,'cant_ped_sanignacio':cant_ped_sanignacio,'cant_ped_sanfabian':cant_ped_sanfabian,'cant_ped_sancarlos':cant_ped_sancarlos,'cant_ped_ranquil':cant_ped_ranquil,'cant_ped_quirihue':cant_ped_quirihue,'cant_ped_quillon':cant_ped_quillon,'cant_ped_portezuelo':cant_ped_portezuelo,'cant_ped_pinto':cant_ped_pinto,'cant_ped_pemuco':cant_ped_pemuco,'cant_ped_niquen':cant_ped_niquen,'cant_ped_ninhue':cant_ped_ninhue,'cant_ped_elcarmen':cant_ped_elcarmen,'cant_ped_coihueco':cant_ped_coihueco,'cant_ped_coelemu':cant_ped_coelemu,'cant_ped_cobquecura':cant_ped_cobquecura,'cant_ped_chillan_viejo':cant_ped_chillan_viejo,'cant_ped_chillan':cant_ped_chillan, 'total_egresos_diciembre':total_egresos_diciembre,'total_egresos_noviembre':total_egresos_noviembre,'total_egresos_octubre':total_egresos_octubre,'total_egresos_septiembre':total_egresos_septiembre,'total_egresos_julio':total_egresos_julio,'total_egresos_junio':total_egresos_junio,'total_egresos_mayo':total_egresos_mayo,'total_egresos_abril':total_egresos_abril,'total_egresos_marzo':total_egresos_marzo,'total_egresos_febrero':total_egresos_febrero,'total_egresos_enero':total_egresos_enero,'total_egresos_agosto':total_egresos_agosto,'total_ingreso_diciembre':total_ingreso_diciembre,'total_ingreso_noviembre':total_ingreso_noviembre,'total_ingreso_octubre':total_ingreso_octubre,'total_ingreso_septiembre':total_ingreso_septiembre,'total_ingreso_julio':total_ingreso_julio,'total_ingreso_junio':total_ingreso_junio,'total_ingreso_mayo':total_ingreso_mayo,'total_ingreso_abril':total_ingreso_abril,'total_ingreso_marzo':total_ingreso_marzo,'total_ingreso_febrero':total_ingreso_febrero,'total_ingreso_enero':total_ingreso_enero,'total_ingreso_agosto':total_ingreso_agosto,'cuentas':cuentas,'sueldos':sueldos,'pedidos':pedidos,'gastos':gastos, 'fecha_inicial': f_i,'total_ingresos': total_ingresos, 'total_egresos': total_egresos,'fecha_final': f_f, 'total': total})

############################################################################
def contacto(request):
    info_enviado = False
    email = ""
    titulo = ""
    texto = ""
    if request.method == "POST":
        formulario = ContactForm(request.POST)
        if formulario.is_valid():
            info_enviado = True
            email = formulario.cleaned_data['Email']
            titulo = formulario.cleaned_data['Titulo']
            texto = formulario.cleaned_data['Texto']

            to_admin ='fcoramirezz@gmail.com'
            html_content = "Hola usted tiene la siguiente consulta de su pagina web"+(texto)
            msg = EmailMultiAlternatives('Correo de Contacto', html_content, 'from@server.com',[to_admin])
            msg.attach_alternative(html_content,'text/html')
            msg.send()

    else:
        formulario = ContactForm()
    ctx = {'form': formulario, 'email': email, 'titulo': titulo, 'texto': texto, 'info_enviado': info_enviado}
    return render_to_response('gestion_lena/contacto.html',ctx,context_instance=RequestContext(request))



def iniciar_sesion(request):
    context = {}
    if request.method == "POST":
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('gestion_lena.views.home')
                else:
                    messages.add_message(request, messages.ERROR, u"Su cuenta se encuentra inactiva, revise su correo para activar su cuenta o escribanos a <correo>.")
            else:
                messages.add_message(request, messages.ERROR, u"Error en su contraseña o nombre de usuario. Vuelva a intentarlo.")
    else:
        #messages.add_message(request, messages.INFO, u"Ingrese con su usuario")
        formulario = AuthenticationForm()
    context['formulario'] = formulario
    return render(request, 'registration/login.html', context)


@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('gestion_lena.views.pagina')


#######################################################################################