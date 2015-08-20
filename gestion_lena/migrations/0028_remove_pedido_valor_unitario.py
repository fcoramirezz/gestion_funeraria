# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0027_auto_20150802_1925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='valor_unitario',
        ),
    ]
