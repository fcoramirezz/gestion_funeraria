# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0057_remove_pedido_fecha_entrega2'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='imagen_pr',
            field=models.ImageField(null=True, upload_to=b'media'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='servicio',
            name='imagen_sec1',
            field=models.ImageField(null=True, upload_to=b'media'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='servicio',
            name='imagen_sec2',
            field=models.ImageField(null=True, upload_to=b'media'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='servicio',
            name='imagen_sec3',
            field=models.ImageField(null=True, upload_to=b'media'),
            preserve_default=True,
        ),
    ]
