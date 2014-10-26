# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0014_cuenta'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuenta',
            name='descripcion',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
