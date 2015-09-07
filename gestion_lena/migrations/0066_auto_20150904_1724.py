# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0065_auto_20150904_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='imagen_pr',
            field=models.ImageField(null=True, upload_to=b'media', blank=True),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='precio_de_venta',
            field=models.PositiveIntegerField(),
        ),
    ]
