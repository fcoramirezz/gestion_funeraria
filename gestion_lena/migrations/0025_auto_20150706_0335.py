# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0024_auto_20150705_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='fecha_entrega',
            field=models.DateField(),
        ),
    ]
