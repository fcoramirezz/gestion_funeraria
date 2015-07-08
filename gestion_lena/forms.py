# coding: utf-8
from django import forms
from gestion_lena.models import Contacto, Pedido, Gasto, TipoGasto, Servicio




class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        labels = {
            'nombre': ('Nombres'),
            'apellido': ('Apellidos'),
        }

    def __init__(self, *args, **kwargs):
        super(ContactoForm, self).__init__(*args, **kwargs)
        self.fields['region'].widget.attrs.update({'id': 'selector_region', 'onchange': 'regionCambio(this.value)'})
        self.fields['provincia'].widget.attrs.update({'id': 'selector_provincia', 'onchange': 'provinciaCambio(this.value)'})
        self.fields['comuna'].widget.attrs.update({'id': 'selector_comuna'})
        self.fields['region'].empty_label = "Seleccione una Region"
        self.fields['provincia'].empty_label = "Seleccione una Provincia"
        self.fields['comuna'].empty_label = None
        self.es_actualizacion = kwargs.get('instance', None)

    def clean(self):
        cleaned_data = super(ContactoForm, self).clean()
        nombres = cleaned_data.get("nombre")
        apellidos = cleaned_data.get("apellido")
        nombres = nombres.title()
        apellidos = apellidos.title()
        cleaned_data['nombre'] = nombres
        cleaned_data['apellido'] = apellidos
        n = 0

        if self.es_actualizacion: ##actualizacion
            n = 1
        print Contacto.objects.filter(nombre__iexact=nombres, apellido__iexact=apellidos).count()
        if Contacto.objects.filter(nombre__iexact=nombres, apellido__iexact=apellidos).count() > n:
            self._errors["nombre"] = self.error_class([""])
            self._errors["apellido"] = self.error_class([""])

            # These fields are no longer valid. Remove them from the
            # cleaned data.
            del cleaned_data["nombre"]
            del cleaned_data["apellido"]

            raise forms.ValidationError("El contacto %s %s ya existe." % (nombres, apellidos))

        return cleaned_data

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        help_texts = {
            'contacto': 'Seleccione a alguno de sus contactos disponibles o registre un nuevo contacto.',
            'cantidad': ' Ingrese tipo de servicio.',
            'valor_unitario': 'Ingrese el precio del servicio.',
            'tipo_de_servicio': 'Ingrese el tipo de servicio a ingresar',
        }

    def __init__(self, *args, **kwargs):
        super(PedidoForm, self).__init__(*args, **kwargs)
        self.fields['region'].widget.attrs.update({'id': 'selector_region', 'onchange': 'regionCambio(this.value)'})
        self.fields['provincia'].widget.attrs.update({'id': 'selector_provincia', 'onchange': 'provinciaCambio(this.value)'})
        self.fields['comuna'].widget.attrs.update({'id': 'selector_comuna'})
        self.fields['contacto'].widget.attrs.update({'onchange': 'pedidoLlenarDireccion(this.value)'})
        self.fields['region'].empty_label = "Seleccione una Región"
        self.fields['provincia'].empty_label = None
        self.fields['comuna'].empty_label = None
        self.fields['fecha_entrega'].widget.attrs.update({'class': 'dateinput'})


###############       SERVICIO FORM
class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio

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

class RangoFechaForm(forms.Form):
    fecha_inicial = forms.DateField(required=True, label="Fecha Inicial")
    fecha_final = forms.DateField(required=True, label="Fecha Final")

    def __init__(self, *args, **kwargs):
        super(RangoFechaForm, self).__init__(*args, **kwargs)
        self.fields['fecha_inicial'].widget.attrs.update({'class': 'dateinput'})
        self.fields['fecha_final'].widget.attrs.update({'class': 'dateinput'})
