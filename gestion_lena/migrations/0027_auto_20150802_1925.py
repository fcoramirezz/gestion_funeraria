# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0026_auto_20150706_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='costo_anexo',
            field=models.PositiveIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pedido',
            name='precio_anexo',
            field=models.PositiveIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pedido',
            name='valor_unitario',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
    ]
