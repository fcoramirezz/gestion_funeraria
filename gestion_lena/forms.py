# coding: utf-8
from django import forms
from gestion_lena.models import Contacto, Pedido

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        #help_texts = {
        #    'nombre': ('Ingrese un nombre representativo para su unidad. Por ejemplo "Clase de Intermediarios de __Nombre Institución__" '),
        #    'tipo_unidad': ('Seleccione el tipo de unidad que representa a la su clase.'),
        #}

class PedidoForm(forms.ModelForm):
	class Meta:
		model = Pedido