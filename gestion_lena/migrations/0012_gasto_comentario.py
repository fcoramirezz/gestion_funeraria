# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_lena', '0011_auto_20141020_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='gasto',
            name='comentario',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
