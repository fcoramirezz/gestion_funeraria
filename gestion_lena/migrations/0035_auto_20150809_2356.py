# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0034_auto_20150809_2349'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pedido',
            options={'ordering': ['-fecha_entrega'], 'verbose_name': 'Pedido', 'verbose_name_plural': 'Pedidos'},
        ),
    ]
