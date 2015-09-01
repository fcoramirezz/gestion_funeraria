# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0060_servicio_imagen_sec3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='imagen_pr',
            field=models.ImageField(upload_to=b'media', null=True, verbose_name=b'Imagen Principal', blank=True),
        ),
    ]
