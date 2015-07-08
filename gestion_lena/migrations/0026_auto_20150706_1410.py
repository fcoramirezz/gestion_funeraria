# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0025_auto_20150706_0335'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicio',
            options={'ordering': ['precio_de_venta'], 'verbose_name': 'Servicio', 'verbose_name_plural': 'Servicios'},
        ),
    ]
