# coding: utf-8
from django.contrib.humanize.templatetags.humanize import intcomma
from django.db import models
from django.core.urlresolvers import reverse


class Configuracion(models.Model):
    titulo_sistema = models.CharField(max_length=255, null=True, blank=True)
    footer = models.CharField(max_length=255, null=True, blank=True)
    precio_lena = models.PositiveIntegerField(null=True, blank=True)
    carga_maxima_dia = models.PositiveIntegerField(null=True, blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = u"Configuracion"
        verbose_name_plural = u"Configuraciones"


class Region(models.Model):
    nombre = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)

    class Meta:
        verbose_name = u"Region"
        verbose_name_plural = u"Regiones"

    def __unicode__(self):
        return u"%s" % self.nombre

class Provincia(models.Model):
    nombre = models.CharField(max_length=255)
    region = models.ForeignKey("Region")

    class Meta:
        verbose_name = u"Provincia"
        verbose_name_plural = u"Provincias"

    def __unicode__(self):
        return u"%s" % self.nombre

class Comuna(models.Model):
    nombre = models.CharField(max_length=255)
    provincia = models.ForeignKey("Provincia")

    class Meta:
        verbose_name = u"Comuna"
        verbose_name_plural = "Comunas"

    def __unicode__(self):
        return u"%s" % self.nombre

TIPO_TELEFONO = (
        (0, 'Movil'),
        (1, 'Fijo'),
        (2, 'No Menciona'),
    )

class Contacto(models.Model):
    '''
    Representa un Cliente que realiza
    un pedido de leña.
    '''
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    tipo_telefono = models.IntegerField(choices=TIPO_TELEFONO, default=2)
    telefono = models.IntegerField(null=True,blank=True)
    region = models.ForeignKey("Region")
    provincia = models.ForeignKey("Provincia")
    comuna = models.ForeignKey("Comuna")
    direccion =	models.CharField(max_length=255)
    correo =  models.EmailField(null=True, blank=True)
    feha_de_registro = models.DateTimeField(auto_now_add=True)
    ultima_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = u"Contacto"
        verbose_name_plural = u"Contactos"

    def __unicode__(self):
        return u"%s %s" % (self.nombre, self.apellido)

    def get_absolute_url(self):
        return reverse('contacto_detail', kwargs={'pk': self.pk})

    @property
    def obtener_tipo_telefono(self):
        return TIPO_TELEFONO[self.tipo_telefono][1]

    @property
    def lista_pedidos(self):
        return self.pedido_set.order_by('-creado_en')

    @property
    def total(self):
        return  sum(map(lambda x: x.total, self.pedido_set.all()))

ESTADO_PEDIDO = (
    ('En Proceso', 'En Proceso'),
    ('Entregado', 'Entregado'),
    )


class Pedido(models.Model):
    '''
    Representa el pedido de leña que realiza un contacto.

    '''
    contacto = models.ForeignKey('Contacto')
    cantidad = models.PositiveIntegerField()
    region = models.ForeignKey("Region")
    provincia = models.ForeignKey("Provincia")
    comuna = models.ForeignKey("Comuna")
    direccion_destino = models.CharField(max_length=255) ## Cuidado
    estado = models.CharField(max_length=100, choices=ESTADO_PEDIDO, default="En Proceso")
    valor_unitario = models.PositiveIntegerField()
    fecha_entrega = models.DateTimeField(null=True, blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = u"Pedido"
        verbose_name_plural = u"Pedidos"

    def __unicode__(self):
        return u"%s @ %s" % (self.pk, self.contacto)

    def get_absolute_url(self):
        return reverse('pedido_detail', kwargs={'pk': self.pk})

    @property
    def obtener_estado_pedido(self):
        return [ESTADO_PEDIDO[0][0], ESTADO_PEDIDO[1][0]]

    @property
    def total(self):
        return self.cantidad * self.valor_unitario

    @property
    def obtener_color_fila(self):
        if self.estado == "Entregado":
            return 'success'
        return 'warning'

class TipoGasto(models.Model):
    nombre = models.CharField(max_length=255)
    creado_en = models.DateTimeField(auto_now_add=True)


    def get_absolute_url(self):
        return reverse('tipo_gasto_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = u"Tipo de Gasto"
        verbose_name_plural = u"Tipos de Gastos"


    def __unicode__(self):
        return self.nombre

class Gasto(models.Model):
    tipo_gasto = models.ForeignKey("TipoGasto")
    valor = models.IntegerField()
    comentario = models.TextField(null=True, blank=True)
    fecha = models.DateField()
    creado_en = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('gasto_detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        return u"%s - $%s" % (self.tipo_gasto.nombre, intcomma(self.valor))

    class Meta:
        verbose_name = u"Gasto"
        verbose_name_plural = u"Gastos"

