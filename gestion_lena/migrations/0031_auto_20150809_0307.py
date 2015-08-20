# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0030_servicio_detalles_del_servicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='tipo_de_contacto',
            field=models.IntegerField(default=2, choices=[(0, b'Proveedor'), (1, b'Cliente'), (2, b'Trabajador'), (3, b'Otro')]),
        ),
    ]
