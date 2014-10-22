# coding: utf-8
from django import forms
from gestion_lena.models import Contacto, Pedido, Gasto, TipoGasto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto

    def __init__(self, *args, **kwargs):
        super(ContactoForm, self).__init__(*args, **kwargs)
        self.fields['region'].widget.attrs.update({'id': 'selector_region', 'onchange': 'regionCambio(this.value)'})
        self.fields['provincia'].widget.attrs.update({'id': 'selector_provincia', 'onchange': 'provinciaCambio(this.value)'})
        self.fields['comuna'].widget.attrs.update({'id': 'selector_comuna'})
        self.fields['region'].empty_label = "Seleccione una Region"
        self.fields['provincia'].empty_label = None
        self.fields['comuna'].empty_label = None

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        exclude = ['fecha_entrega']

    def __init__(self, *args, **kwargs):
        super(PedidoForm, self).__init__(*args, **kwargs)
        self.fields['region'].widget.attrs.update({'id': 'selector_region', 'onchange': 'regionCambio(this.value)'})
        self.fields['provincia'].widget.attrs.update({'id': 'selector_provincia', 'onchange': 'provinciaCambio(this.value)'})
        self.fields['comuna'].widget.attrs.update({'id': 'selector_comuna'})
        self.fields['contacto'].widget.attrs.update({'onchange': 'pedidoLlenarDireccion(this.value)'})
        self.fields['region'].empty_label = "Seleccione una Region"
        self.fields['provincia'].empty_label = None
        self.fields['comuna'].empty_label = None

class PedidoContactoForm(forms.ModelForm):
	class Meta:
		model = Pedido
		exclude = ['fecha_entrega', 'contacto']

class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto

    def __init__(self, *args, **kwargs):
        super(GastoForm, self).__init__(*args, **kwargs)
        self.fields['fecha'].widget.attrs.update({'class': 'dateinput'})

class TipoGastoForm(forms.ModelForm):
    class Meta:
        model = TipoGasto