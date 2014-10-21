# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0007_auto_20141020_1047'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comuna',
            options={'verbose_name': 'Comuna', 'verbose_name_plural': 'Comunas'},
        ),
        migrations.AlterModelOptions(
            name='configuracion',
            options={'verbose_name': 'Configuracion', 'verbose_name_plural': 'Configuraciones'},
        ),
        migrations.AlterModelOptions(
            name='contacto',
            options={'verbose_name': 'Contacto', 'verbose_name_plural': 'Contactos'},
        ),
        migrations.AlterModelOptions(
            name='gasto',
            options={'verbose_name': 'Gasto', 'verbose_name_plural': 'Gastos'},
        ),
        migrations.AlterModelOptions(
            name='pedido',
            options={'verbose_name': 'Pedido', 'verbose_name_plural': 'Pedidos'},
        ),
        migrations.AlterModelOptions(
            name='provincia',
            options={'verbose_name': 'Provincia', 'verbose_name_plural': 'Provincias'},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'verbose_name': 'Region', 'verbose_name_plural': 'Regiones'},
        ),
        migrations.AlterModelOptions(
            name='tipogasto',
            options={'verbose_name': 'Tipo de Gasto', 'verbose_name_plural': 'Tipos de Gastos'},
        ),
        migrations.AddField(
            model_name='region',
            name='numero',
            field=models.CharField(default=b'I', max_length=10),
            preserve_default=True,
        ),
    ]
