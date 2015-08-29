# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0054_duda_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duda',
            name='pregunta',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='duda',
            name='respuesta',
            field=models.TextField(null=True, blank=True),
        ),
    ]
