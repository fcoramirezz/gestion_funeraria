# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0050_auto_20150828_0234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='duda',
            name='pregunta',
        ),
        migrations.RemoveField(
            model_name='duda',
            name='respuesta',
        ),
        migrations.AddField(
            model_name='duda',
            name='carga_maxima_dia',
            field=models.PositiveIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
