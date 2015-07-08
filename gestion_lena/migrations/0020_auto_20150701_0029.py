# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0019_contacto_tipo_de_servicio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacto',
            name='tipo_de_servicio',
        ),
        migrations.AddField(
            model_name='pedido',
            name='tipo_de_servicio',
            field=models.IntegerField(default=1, choices=[(0, b'Cremaci\xc3\xb3n'), (1, b'F\xc3\xbanebre Tradicional'), (2, b'Otro')]),
            preserve_default=True,
        ),
    ]
