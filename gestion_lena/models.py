# coding: utf-8
from django.contrib.humanize.templatetags.humanize import intcomma
from django.db import models
from django.core.urlresolvers import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.utils import timezone


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

    def save(self, *args, **kwargs):
        #check if the row with this hash already exists.
        if self.estado == "Entregado" and not self.fecha_entrega:
            self.fecha_entrega = timezone.now()
        super(Pedido, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        try:
            if self.cuenta:
                cuenta = self.cuenta
                cuenta.pedido = None
                cuenta.descripcion = "Venta ( %s ) ingresada." % self
                cuenta.save()
                lc = Cuenta.objects.all().last()
                Cuenta.objects.create(cargo=self.total, abono=0, saldo=lc.saldo-self.total,  fecha=timezone.now(), descripcion="Venta (%s) eliminada." % self)
        except:
            pass
        return super(self.__class__, self).delete(*args, **kwargs)

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


    def delete(self, *args, **kwargs):
        try:
            if self.cuenta:
                cuenta = self.cuenta
                cuenta.gasto = None
                cuenta.descripcion = "Gasto ( %s ) ingresado." % self
                cuenta.save()
                lc = Cuenta.objects.all().last()
                Cuenta.objects.create(cargo=0, abono=self.valor, saldo=lc.saldo+self.valor,  fecha=timezone.now(), descripcion="Gasto (%s) eliminado." % self)                
        except:
            pass
        return super(self.__class__, self).delete(*args, **kwargs)

    class Meta:
        verbose_name = u"Gasto"
        verbose_name_plural = u"Gastos"

class Cuenta(models.Model):
    fecha = models.DateTimeField()
    cargo = models.IntegerField()
    abono = models.IntegerField()
    saldo = models.IntegerField(null=True, blank=True)
    pedido = models.OneToOneField("Pedido", null=True, blank=True)
    gasto = models.OneToOneField("Gasto", null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return u"%s" % self.fecha

@receiver(post_save, sender=Pedido)
def guardar_entrega_cuenta_t(sender, **kwargs):
    instance = kwargs.get('instance')
    cuentas = Cuenta.objects.all()
    saldo_total = 0
    if cuentas.count() > 0:
        uc = cuentas.last()
        saldo_total = uc.saldo
    if kwargs.get('created', False): # creado
        if instance.estado == "Entregado" and instance.fecha_entrega:    
            Cuenta.objects.create(pedido=instance, abono=instance.total, cargo=0, fecha=timezone.now(), saldo=saldo_total + instance.total)
    else: # Actualizacion
        pedido = instance
        cuenta = None
        try:
            cuenta = pedido.cuenta
        except:
            pass
        if cuenta: # Existe la cuenta
            if pedido.estado == "Entregado" and pedido.fecha_entrega: ##
                if cuenta.abono != pedido.total:
                    cuenta.pedido = None
                    cuenta.descripcion = "Venta ( %s ) Ingresada." % pedido
                    cuenta.save()
                    last_obj = Cuenta.objects.create(cargo=cuenta.abono, abono=0, descripcion="Modificación de la Venta (%s)." % pedido, fecha=timezone.now(), saldo=saldo_total-cuenta.abono)
                    Cuenta.objects.create(abono=pedido.total, cargo=0, pedido=pedido, fecha=timezone.now(), saldo=last_obj.saldo+pedido.total)
            else:
                cuenta.pedido = None
                cuenta.descripcion = "Venta ( %s ) Ingresada." % pedido
                cuenta.save() 
                Cuenta.objects.create(cargo=pedido.total, abono=0, descripcion="Venta ( %s ) desmarcada (cambio de estado a 'En Proceso')" % pedido, fecha=timezone.now(), saldo=saldo_total-pedido.total)
        else: # No existe cuenta y se actualiza
            if pedido.estado == "Entregado" and pedido.fecha_entrega: ##
                Cuenta.objects.create(pedido=pedido, abono=pedido.total, cargo=0, fecha=timezone.now(), saldo=saldo_total + pedido.total)

@receiver(post_save, sender=Gasto)
def guardar_gasto_cuenta_t(sender, **kwargs):
    cuentas = Cuenta.objects.all()
    saldo_total = 0
    if cuentas.count() > 0:
        uc = cuentas.last()
        saldo_total = uc.saldo
    if kwargs.get('created', False): # Creado
        instance = kwargs.get('instance')
        obj, created = Cuenta.objects.get_or_create(gasto=instance, abono=0, cargo=instance.valor, fecha=timezone.now())
        obj.saldo = saldo_total - obj.cargo
        obj.save()
    else: # Actualizacion
        instance = kwargs.get('instance')
        gasto = instance
        cuenta = gasto.cuenta
        if cuenta.cargo != gasto.valor:
            cuenta.gasto = None
            cuenta.descripcion = "Gasto ( %s ) ingresado." % gasto
            cuenta.save()
            last_obj = Cuenta.objects.create(abono=cuenta.cargo, cargo=0, descripcion="Modificación del Gasto (%s)." % gasto, fecha=timezone.now(), saldo=saldo_total+cuenta.cargo)
            Cuenta.objects.create(abono=0, cargo=gasto.valor, gasto=gasto, fecha=timezone.now(), saldo=last_obj.saldo-gasto.valor)

