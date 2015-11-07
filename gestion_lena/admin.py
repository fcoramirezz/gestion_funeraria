from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from gestion_lena.models import Contacto, Pedido, TipoGasto, Gasto, Configuracion, Cuenta, Servicio, Sueldo, Trabajador
from gestion_lena.models import Region, Provincia, Comuna, Duda


class RegionResource(resources.ModelResource):
    class Meta:
        model = Region

class ProvinciaResource(resources.ModelResource):
    class Meta:
        model = Provincia

class ComunaResource(resources.ModelResource):
    class Meta:
        model = Comuna

class RegionAdmin(ImportExportModelAdmin):
    resource_class = RegionResource

class ProvinciaAdmin(ImportExportModelAdmin):
    resource_class = ProvinciaResource

class ComunaAdmin(ImportExportModelAdmin):
    resource_class = ComunaResource


admin.site.register(Contacto)
admin.site.register(Pedido)
admin.site.register(TipoGasto)
admin.site.register(Gasto)
admin.site.register(Configuracion)
admin.site.register(Cuenta)
admin.site.register(Servicio)

admin.site.register(Sueldo)
admin.site.register(Trabajador)
admin.site.register(Duda)




admin.site.register(Region, RegionAdmin)
admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Comuna, ComunaAdmin)