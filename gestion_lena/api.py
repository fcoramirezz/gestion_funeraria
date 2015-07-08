from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie import fields
from gestion_lena.models import Region, Provincia, Comuna, Contacto


class RegionResource(ModelResource):
    class Meta:
        queryset = Region.objects.all()
        resource_name = 'region'
        allowed_methods = ['get']

class ProvinciaResource(ModelResource):
    region = fields.ForeignKey(RegionResource, 'region')

    class Meta:
        queryset = Provincia.objects.all()
        resource_name = 'provincia'
        filtering = {
            'region': ALL_WITH_RELATIONS,
        }
        allowed_methods = ['get']

class ComunaResource(ModelResource):
    provincia = fields.ForeignKey(ProvinciaResource, 'provincia')

    class Meta:
        queryset = Comuna.objects.all()
        resource_name = 'comuna'
        filtering = {
            'provincia': ALL_WITH_RELATIONS,
        }
        allowed_methods = ['get']

class ContactoResource(ModelResource):
    region = fields.ForeignKey(RegionResource, 'region', full=True)
    provincia = fields.ForeignKey(ProvinciaResource, 'provincia', full=True)
    comuna = fields.ForeignKey(ComunaResource, 'comuna', full=True)

    class Meta:
        queryset = Contacto.objects.all()
        resource_name = 'contacto'
        allowed_methods = ['get']

