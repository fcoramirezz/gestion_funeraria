# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0032_auto_20150809_0338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='comuna',
            field=models.ForeignKey(blank=True, to='gestion_lena.Comuna', null=True),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='provincia',
            field=models.ForeignKey(blank=True, to='gestion_lena.Provincia', null=True),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='region',
            field=models.ForeignKey(blank=True, to='gestion_lena.Region', null=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='costo_anexo',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='precio_anexo',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
