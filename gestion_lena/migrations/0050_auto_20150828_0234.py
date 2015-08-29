# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0049_duda_creado_en'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duda',
            name='pregunta',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='duda',
            name='respuesta',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
