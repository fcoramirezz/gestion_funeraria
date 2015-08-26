# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0046_servicio_creado_en'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='publicar',
            field=models.CharField(default=b'Si', max_length=100, choices=[(b'Si', b'Si'), (b'No', b'No')]),
            preserve_default=True,
        ),
    ]
