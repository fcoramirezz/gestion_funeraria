# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0023_auto_20150705_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='tipo_de_servicio',
            field=models.ForeignKey(to='gestion_lena.Servicio'),
        ),
    ]
