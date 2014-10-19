# coding: utf-8
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from gestion_lena.models import Contacto, Pedido, Configuracion
from gestion_lena.mixins import LoginRequired, SearchableListMixin
from gestion_lena.forms import ContactoForm, PedidoForm, PedidoContactoForm

import datetime

CONF, created = Configuracion.objects.get_or_create(id=1)
if created:
    CONF.titulo_pagina = "Gestión de Distribución de Leña"
    CONF.footer = "Diego Ramirez Cerda &copy; Todos los derechos reservados"
    CONF.precio_lena = 17000
    CONF.carga_maxima_dia = 24
    CONF.save()

@login_required
def home(request):
	return render(request, 'gestion_lena/base.html')

##########CONTACTO###################################
class ContactoListView(LoginRequired, SearchableListMixin, ListView):
    model = Contacto
    template_name = 'gestion_lena/contacto_list.html'
    search_fields = [('nombre','icontains',), ('apellido','icontains',)]
    
class ContactoDetailView(LoginRequired, SearchableListMixin, DetailView):
    model = Contacto
    template_name = 'gestion_lena/contacto_detail.html'
    search_fields = [('nombre','icontains',), ('apellido','icontains',)]

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

###########PEDIDO###################################################
class PedidoListView(LoginRequired, SearchableListMixin, ListView):
    model = Pedido
    template_name = 'gestion_lena/pedido_list.html'
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


################################################################################

@login_required
def pedido_cambiar_estado(request, id_pedido):
    pedido = get_object_or_404(Pedido, id=id_pedido)
    if pedido.estado == "Entregado":
        return redirect('contacto_detail', pedido.contacto.id)
    pedido.estado = "Entregado"
    pedido.fecha_entrega = datetime.datetime.now()
    pedido.save()
    return redirect('contacto_detail', pedido.contacto.id)

@login_required
def contacto_nuevo_pedido(request, id_contacto):
    contacto = get_object_or_404(Contacto, id=id_contacto)
    if request.method == "POST":
        form = PedidoContactoForm(request.POST)
        print form
        if form.is_valid():
            print "hola"
            cantidad = form.cleaned_data.get('cantidad', None)
            direccion_destino = form.cleaned_data.get('direccion_destino', None)
            estado = form.cleaned_data.get('estado', None)
            valor_unitario = form.cleaned_data.get('valor_unitario', None)
            Pedido.objects.create(contacto=contacto, cantidad=cantidad, direccion_destino=direccion_destino, estado=estado,
                valor_unitario=valor_unitario)
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
    pedidos = Pedido.objects.filter(estado="En Proceso").order_by('-creado_en')
    maximo = CONF.carga_maxima_dia
    metros = 0
    indice = 0
    for x in pedidos:
        if metros >= maximo:
            breaks
        metros+=x.cantidad
        indice+=1
    pedidos = pedidos[:indice]
    context['pedidos'] = pedidos
    return render(request, 'gestion_lena/calcular_entrega_pedidos.html', context)



#############################################################################

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
        messages.add_message(request, messages.INFO, u"Ingrese con su usuario")
        formulario = AuthenticationForm()
    context['formulario'] = formulario
    return render(request, 'registration/login.html', context)

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('gestion_lena.views.home')

#######################################################################################