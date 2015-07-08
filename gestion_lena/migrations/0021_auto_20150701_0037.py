# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0020_auto_20150701_0029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='cantidad',
        ),
        migrations.AddField(
            model_name='contacto',
            name='tipo_de_contacto',
            field=models.IntegerField(default=2, choices=[(0, b'Proveedor'), (1, b'Cliente'), (2, b'Otro')]),
            preserve_default=True,
        ),
    ]
