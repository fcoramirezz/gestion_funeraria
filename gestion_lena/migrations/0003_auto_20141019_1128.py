# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0002_auto_20141017_1830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingreso',
            name='pedido',
        ),
        migrations.DeleteModel(
            name='Ingreso',
        ),
        migrations.AddField(
            model_name='pedido',
            name='fecha_modificacion',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 19, 11, 28, 50, 4643), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='valor_unitario',
            field=models.PositiveIntegerField(default=5),
            preserve_default=False,
        ),
    ]
