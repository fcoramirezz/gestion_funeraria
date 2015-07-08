# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0021_auto_20150701_0037'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HuellaCarbono',
        ),
        migrations.AlterField(
            model_name='pedido',
            name='tipo_de_servicio',
            field=models.CharField(default=b'F\xc3\xbanebre Tradicional', max_length=100, choices=[(b'Cremaci\xc3\xb3n', b'Cremaci\xc3\xb3n'), (b'F\xc3\xbanebre Tradicional', b'F\xc3\xbanebre Tradicional'), (b'Otro', b'Otro')]),
        ),
    ]
