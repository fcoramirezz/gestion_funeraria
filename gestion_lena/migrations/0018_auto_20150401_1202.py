# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0017_auto_20141207_2152'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contacto',
            options={'ordering': ['apellido'], 'verbose_name': 'Contacto', 'verbose_name_plural': 'Contactos'},
        ),
        migrations.AlterModelOptions(
            name='pedido',
            options={'ordering': ['-creado_en'], 'verbose_name': 'Pedido', 'verbose_name_plural': 'Pedidos'},
        ),
        migrations.AddField(
            model_name='huellacarbono',
            name='fecha',
            field=models.DateField(default=datetime.date(2015, 4, 1)),
            preserve_default=False,
        ),
    ]
