# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0075_auto_20151008_0024'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Imagen',
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='detalles_del_servicio',
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='imagen_sec1',
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='imagen_sec2',
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='imagen_sec3',
        ),
    ]
