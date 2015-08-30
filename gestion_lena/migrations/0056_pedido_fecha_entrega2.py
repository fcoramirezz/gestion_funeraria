# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0055_auto_20150828_0330'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='fecha_entrega2',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
    ]
