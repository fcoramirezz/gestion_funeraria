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

from gestion_lena.models import Servicio, Contacto, Pedido, Configuracion, Region, Provincia, Comuna, Gasto, TipoGasto, Servicio, Sueldo, Trabajador
    
from gestion_lena.mixins import LoginRequired, SearchableListMixin
from gestion_lena.forms import ServicioForm, ContactoForm, PedidoForm, PedidoContactoForm, GastoForm, TipoGastoForm, RangoFechaForm, ServicioForm, SueldoForm, TrabajadorForm
   

from gestion_lena.models import Cuenta

import datetime

CONF, created = Configuracion.objects.get_or_create(id=1)
if created:
    CONF.titulo_pagina = "Gestión de Distribución de Leña"
    CONF.footer = "Francisco Ramirez Cerda &copy; Todos los derechos reservados"
    CONF.precio_lena = 17000
    CONF.carga_maxima_dia = 24
    CONF.save()

@login_required
def home(request):
    pedidos = Pedido.objects.exclude(estado="Pagado").order_by('creado_en')[:4]
    return render(request, 'gestion_lena/base.html',{'pedidos': pedidos} )


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
    context = {}
    tipo_de_servicio = Servicio.objects.filter(publicar="Si").order_by('creado_en')
    context['servicios'] = tipo_de_servicio
    return render(request, 'gestion_lena/pagina.html', context)



    

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
            if d_i < d_f and d_i <= hoy :
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
    total = 0
    if cuentas.count() > 0:
        total = cuentas.last().saldo
    return render(request, 'gestion_lena/cuenta_t.html', {'cuentas':cuentas, 'fecha_inicial': f_i, 'fecha_final': f_f, 'total': total})

############################################################################

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