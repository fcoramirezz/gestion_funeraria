from django.contrib import admin

from gestion_lena.models import Contacto, Pedido, TipoGasto, Gasto, Configuracion

admin.site.register(Contacto)
admin.site.register(Pedido)
admin.site.register(TipoGasto)
admin.site.register(Gasto)
admin.site.register(Configuracion)