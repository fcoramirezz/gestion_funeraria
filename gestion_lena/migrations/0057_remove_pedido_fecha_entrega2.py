# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0056_pedido_fecha_entrega2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='fecha_entrega2',
        ),
    ]
