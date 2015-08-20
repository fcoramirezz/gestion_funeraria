# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0035_auto_20150809_2356'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pedido',
            options={'ordering': ['-creado_en'], 'verbose_name': 'Pedido', 'verbose_name_plural': 'Pedidos'},
        ),
    ]
