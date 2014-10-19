# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0005_configuracion_creado_en'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuracion',
            name='carga_maxima_dia',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='precio_lena',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='titulo_sistema',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
