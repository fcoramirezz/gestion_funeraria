# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0036_auto_20150810_0211'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pedido',
            options={'ordering': ['creado_en'], 'verbose_name': 'Pedido', 'verbose_name_plural': 'Pedidos'},
        ),
    ]
