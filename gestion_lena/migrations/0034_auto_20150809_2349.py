# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0033_auto_20150809_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='comuna',
            field=models.ForeignKey(blank=True, to='gestion_lena.Comuna', null=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='provincia',
            field=models.ForeignKey(blank=True, to='gestion_lena.Provincia', null=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='region',
            field=models.ForeignKey(blank=True, to='gestion_lena.Region', null=True),
        ),
    ]
