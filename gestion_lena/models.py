# coding: utf-8
from django.contrib.humanize.templatetags.humanize import intcomma
from django.db import models
from django.core.urlresolvers import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.utils import timezone
from datetime import datetime, date, time, timedelta



class Configuracion(models.Model):
    titulo_sistema = models.CharField(max_length=255, null=True, blank=True)
    footer = models.CharField(max_length=255, null=True, blank=True)
    precio_lena = models.PositiveIntegerField(null=True, blank=True)
    carga_maxima_dia = models.PositiveIntegerField(null=True, blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = u"Configuracion"
        verbose_name_plural = u"Configuraciones"


class Duda(models.Model):
    titulo = models.CharField(max_length=255,null=True)
    pregunta = models.TextField(null=True, blank=True)
    respuesta = models.TextField(null=True, blank=True)
   
    creado_en = models.DateTimeField(auto_now_add=True,null=True)

    class Meta:
        verbose_name = u"Duda"
        verbose_name_plural = u"Dudas"

    def __unicode__(self):
        return u"%s" % self.titulo

    def get_absolute_url(self):
        return reverse('duda_detail', kwargs={'pk': self.pk})

   


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

TIPO_CONTACTO = (
        (0, 'Proveedor'),
        (1, 'Cliente'),
        (2, 'Trabajador'),
        (3, 'Otro'),
    )

class Contacto(models.Model):
    '''
    Representa un Cliente que realiza
   
    '''
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    '''tipo_de_contacto= models.IntegerField(choices=TIPO_CONTACTO, default=3)'''
    tipo_telefono = models.IntegerField(choices=TIPO_TELEFONO, default=2)
    telefono = models.IntegerField(null=True,blank=True)
    region = models.ForeignKey("Region",null=True,blank=True)
    provincia = models.ForeignKey("Provincia",null=True,blank=True)
    comuna = models.ForeignKey("Comuna",null=True,blank=True)
    direccion =	models.CharField(max_length=255)
    correo =  models.EmailField(null=True, blank=True)
    feha_de_registro = models.DateTimeField(auto_now_add=True)
    ultima_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = u"Contacto"
        verbose_name_plural = u"Contactos"
        ordering =  ['apellido']

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
    ('No Pagado', 'No Pagado'),
    ('Pagado', 'Pagado'),
    )

PUBLICAR = (
    ('Si', 'Si'),
    ('No', 'No'),
    )



class Servicio(models.Model):
    nombre = models.CharField(max_length=255)
    precio_de_venta = models.PositiveIntegerField()
    costo_de_servicio = models.PositiveIntegerField()
    detalles_del_servicio = models.TextField(null=True, blank=True)
    publicar = models.CharField(max_length=100, choices=PUBLICAR, default="Si")
    imagen_pr = models.ImageField(upload_to='media',null=True,blank=True)
    imagen_sec1 = models.FileField(upload_to='media',null=True,blank=True)
    imagen_sec2 = models.ImageField(upload_to='media',null=True,blank=True)
    imagen_sec3 = models.ImageField(upload_to='media',null=True,blank=True)
    creado_en = models.DateTimeField(auto_now_add=True,null=True)

   
   



    class Meta:
        verbose_name = u"Servicio"
        verbose_name_plural = u"Servicios"
        ordering =  ['precio_de_venta']
        
    def __unicode__(self):
        return u"%s %s" % (self.nombre, self.precio_de_venta)

    
    def obtener_ganancia_de_venta(self):
        return self.precio_de_venta - self.costo_de_servicio
    @property
    def obtener_precio_de_venta(self):
        return self.precio_de_venta

    @property
    def obtener_costo_de_servicio(self):
        return self.costo_de_servicio

    def get_absolute_url(self):
        return reverse('servicio_detail', kwargs={'pk': self.pk})

class Imagen(models.Model):
    nombre_foto = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to='media',null=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = u"Imagen"
        verbose_name_plural = u"Imágenes"
        ordering =  ['creado_en']

class Trabajador(models.Model):
 
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    tipo_telefono = models.IntegerField(choices=TIPO_TELEFONO, default=2)
    telefono = models.IntegerField(null=True,blank=True)
    direccion = models.CharField(max_length=255)
    correo =  models.EmailField(null=True, blank=True)
    feha_de_registro = models.DateTimeField(auto_now_add=True)
    ultima_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = u"Trabajador"
        verbose_name_plural = u"Trabajadores"
        ordering =  ['apellido']

    def __unicode__(self):
        return u"%s %s" % (self.nombre, self.apellido)

    def get_absolute_url(self):
        return reverse('trabajador_detail', kwargs={'pk': self.pk})

    @property
    def obtener_tipo_telefono(self):
        return TIPO_TELEFONO[self.tipo_telefono][1]
    @property
    def lista_sueldos(self):
        return self.sueldo_set.order_by('-creado_en')

class Componentes(models.Model):
    nombre_de_componente = models.CharField(max_length=255)
    costo = models.PositiveIntegerField()




class Pedido(models.Model):
    '''
    Representa el pedido de leña que realiza un contacto.

    '''
 
    contacto = models.ForeignKey('Contacto')
    cantidad = 1
    tipo_de_servicio = models.ForeignKey("Servicio")
    region = models.ForeignKey("Region", null=True, blank=True)
    provincia = models.ForeignKey("Provincia", null=True, blank=True)
    comuna = models.ForeignKey("Comuna", null=True, blank=True)
    direccion_destino = models.CharField(max_length=255,null=True,blank=True) ## Cuidado
    direccion_de_velorio = models.CharField(max_length=255,null=True,blank=True)
    direccion_de_ceremonia = models.CharField(max_length=255,null=True,blank=True)
    direccion_de_sepultacion = models.CharField(max_length=255,null=True,blank=True)

    estado = models.CharField(max_length=100, choices=ESTADO_PEDIDO, default="No Pagado")
    precio_anexo = models.PositiveIntegerField(default=0)
    costo_anexo = models.PositiveIntegerField(default=0)
    fecha_entrega = models.DateField()
    creado_en = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = u"Pedido"
        verbose_name_plural = u"Pedidos"
        ordering = ['creado_en']

    def __unicode__(self):
        return u"%s @ %s" % (self.tipo_de_servicio, self.contacto)

    def get_absolute_url(self):
        return reverse('pedido_detail', kwargs={'pk': self.pk})

    @property
    def obtener_estado_pedido(self):
        return [ESTADO_PEDIDO[0][0], ESTADO_PEDIDO[1][0]]


    @property
    def total(self):
        return self.cantidad * self.tipo_de_servicio.obtener_ganancia_de_venta() + self.precio_anexo - self.costo_anexo

    @property
    def obtener_comuna(self):
        return self.comuna


    @property
    def obtener_color_fila(self):
        if self.estado == "Pagado":
            return 'success'
        return 'warning'

    def save(self, *args, **kwargs):
        #check if the row with this hash already exists.
        if self.estado == "Pagado" and not self.fecha_entrega:
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

'''class Direccion(models.Model):
    direccion = models.CharField(max_length=255)
    pedido = models.ForeignKey('Pedido')

    class Meta:
        verbose_name = u"Direccion"
        verbose_name_plural = u"Direcciones"

    def __unicode__(self):
        return self.direccion

    def get_absolute_url(self):
        return reverse('direccion_detail', kwargs={'pk': self.pk})'''


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

class Sueldo(models.Model):
    trabajador = models.ForeignKey("Trabajador")
    cantidad = models.IntegerField()
    comentario = models.TextField(null=True, blank=True)
    fecha = models.DateField()
    creado_en = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('sueldo_detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        return u"%s - $%s" % (self.trabajador.nombre, intcomma(self.cantidad))

    def delete(self, *args, **kwargs):
        try:
            if self.cuenta:
                cuenta = self.cuenta
                cuenta.sueldo = None
                cuenta.descripcion = "Sueldo de ( %s ) ingresado." % self
                cuenta.save()
                lc = Cuenta.objects.all().last()
                Cuenta.objects.create(cargo=0, abono=self.cantidad, saldo=lc.saldo+self.cantidad,  fecha=timezone.now(), descripcion="Sueldo de (%s) eliminado." % self)                
        except:
            pass
        return super(self.__class__, self).delete(*args, **kwargs)

    class Meta:
        verbose_name = u"Sueldo"
        verbose_name_plural = u"Sueldos"



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
    sueldo = models.OneToOneField("Sueldo", null=True, blank=True)
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
        if instance.estado == "Pagado" and instance.fecha_entrega:    
            Cuenta.objects.create(pedido=instance, abono=instance.total, cargo=0, fecha=timezone.now(), saldo=saldo_total + instance.total)
    else: # Actualizacion
        pedido = instance
        cuenta = None
        try:
            cuenta = pedido.cuenta
        except:
            pass
        if cuenta: # Existe la cuenta
            if pedido.estado == "Pagado" and pedido.fecha_entrega: ##
                if cuenta.abono != pedido.total:
                    cuenta.pedido = None
                    cuenta.descripcion = "Venta de Servicio ( %s ) Ingresada." % pedido
                    cuenta.save()
                    last_obj = Cuenta.objects.create(cargo=cuenta.abono, abono=0, descripcion="Modificación de la Venta de Servicio(%s)." % pedido, fecha=timezone.now(), saldo=saldo_total-cuenta.abono)
                    Cuenta.objects.create(abono=pedido.total, cargo=0, pedido=pedido, fecha=timezone.now(), saldo=last_obj.saldo+pedido.total)
            else:
                cuenta.pedido = None
                cuenta.descripcion = "Venta ( %s ) Ingresada." % pedido
                cuenta.save() 
                Cuenta.objects.create(cargo=pedido.total, abono=0, descripcion="Venta de Servicio( %s ) desmarcada (cambio de estado a 'No Pagado')" % pedido, fecha=timezone.now(), saldo=saldo_total-pedido.total)
        else: # No existe cuenta y se actualiza
            if pedido.estado == "Pagado" and pedido.fecha_entrega: ##
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

@receiver(post_save, sender=Sueldo)
def guardar_sueldo_cuenta_t(sender, **kwargs):
    cuentas = Cuenta.objects.all()
    saldo_total = 0
    if cuentas.count() > 0:
        uc = cuentas.last()
        saldo_total = uc.saldo
    if kwargs.get('created', False): # Creado
        instance = kwargs.get('instance')
        obj, created = Cuenta.objects.get_or_create(sueldo=instance, abono=0, cargo=instance.cantidad, fecha=timezone.now())
        obj.saldo = saldo_total - obj.cargo
        obj.save()
    else: # Actualizacion
        instance = kwargs.get('instance')
        sueldo = instance
        cuenta = sueldo.cuenta
        if cuenta.cargo != sueldo.cantidad:
            cuenta.sueldo = None
            cuenta.descripcion = "Sueldo ( %s ) ingresado." % sueldo
            cuenta.save()
            last_obj = Cuenta.objects.create(abono=cuenta.cargo, cargo=0, descripcion="Modificación del Sueldo (%s)." % sueldo, fecha=timezone.now(), saldo=saldo_total+cuenta.cargo)
            Cuenta.objects.create(abono=0, cargo=sueldo.cantidad, sueldo=sueldo, fecha=timezone.now(), saldo=last_obj.saldo-sueldo.cantidad)

