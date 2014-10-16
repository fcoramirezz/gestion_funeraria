from django.contrib import admin

from gestion_lena.models import Contacto, Pedido, Ingreso, TipoGasto, Gasto

admin.site.register(Contacto)
admin.site.register(Pedido)
admin.site.register(Ingreso)
admin.site.register(TipoGasto)
admin.site.register(Gasto)