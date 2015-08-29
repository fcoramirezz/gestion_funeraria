# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0052_duda_nombre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='duda',
            old_name='nombre',
            new_name='pregunta',
        ),
        migrations.RemoveField(
            model_name='duda',
            name='carga_maxima_dia',
        ),
        migrations.AddField(
            model_name='duda',
            name='respuesta',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
    ]
